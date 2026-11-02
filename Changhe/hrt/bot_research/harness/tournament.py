"""Parallel tournament driver on the unchanged engine.

Each match runs in a fresh worker process (``maxtasksperchild=1``) so module
state cannot leak between matches. Every pairing is played with both player
assignments. Results are appended as JSON lines; a summary table is written
at the end and can be regenerated with ``--summarize-only``.

Example (from the project root):

    PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" .venv/bin/python -B \\
        -m bot_research.harness.tournament --name smoke \\
        --candidates bot_research.harness.baselines:@greedy_eco \\
        --opponents td_bots.protocol:idle bot_research.harness.baselines:@rush \\
        --jobs 2

Outputs go to ``bot_research/runs/lead/<name>/`` unless ``--out-dir`` is given.
Logs are kept for every match unless ``--keep-logs`` is ``none`` or ``losses``
(``losses`` keeps logs where the candidate did not win, plus the first match of
each pairing).
"""
from __future__ import annotations

import argparse
import json
import multiprocessing as mp
import os
import sys
import time
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def _slug(spec: str) -> str:
    keep = []
    for ch in spec.split(":")[-1] + "_" + spec.split(":")[0].split(".")[-1]:
        keep.append(ch if ch.isalnum() or ch in "-_=" else "-")
    return "".join(keep)[:60]


def _run_one(task: dict) -> dict:
    os.chdir(ROOT)
    sys.path.insert(0, str(ROOT))
    from bot_research.harness.match import play_match

    log = Path(task["log"])
    try:
        row = play_match(task["a"], task["b"], log, scenario=task.get("scenario"),
                         metadata={"pair": task["pair"], "candidate_side": task["candidate_side"]})
        row["candidate_side"] = task["candidate_side"]
        row["pair"] = task["pair"]
        row["error"] = None
    except Exception as exc:  # harness-level failure (not a bot error)
        row = {"spec_a": task["a"], "spec_b": task["b"], "scenario": task.get("scenario"),
               "candidate_side": task["candidate_side"], "pair": task["pair"],
               "error": f"{type(exc).__name__}: {exc}"}
    keep = task.get("keep_logs", "all")
    if row.get("error") is None and keep != "all":
        cand_won = row["winner"] == task["candidate_side"]
        if keep == "none" or (keep == "losses" and cand_won and not task.get("first_of_pair")):
            try:
                log.unlink()
                row["log"] = None
            except OSError:
                pass
    return row


def candidate_view(row: dict) -> dict:
    """Return outcome fields from the candidate's perspective."""
    side = row["candidate_side"]
    winner = row["winner"]
    outcome = "D" if winner is None else ("W" if winner == side else "L")
    hp_diff = row["hp_diff_a"] if side == 0 else -row["hp_diff_a"]
    me, opp = row["players"][side], row["players"][1 - side]
    return {"outcome": outcome, "hp_diff": hp_diff, "rounds": row["rounds"],
            "rejected": me["n_rejected"], "errors": len(me["bot_errors"]),
            "opp_rejected": opp["n_rejected"], "opp_errors": len(opp["bot_errors"]),
            "decide_s": row["decide_seconds"][side], "decide_max_s": row["decide_max_seconds"][side],
            "reason": row["reason"]}


def _labels(rows: list[dict]) -> dict:
    """Map (spec, version) to a display label; specs seen with several versions get a suffix."""
    versions = defaultdict(set)
    for row in rows:
        for side in "ab":
            versions[row[f"spec_{side}"]].add(row.get(f"version_{side}"))
    labels = {}
    for spec, vs in versions.items():
        for v in vs:
            labels[(spec, v)] = spec if len(vs) == 1 else f"{spec} [v:{(v or 'none')[:8]}]"
    return labels


def summarize(rows: list[dict]) -> str:
    table = defaultdict(list)
    failures = [r for r in rows if r.get("error")]
    labels = _labels(rows)
    mixed = sorted({lab for lab in labels.values() if "[v:" in lab})
    changed = sum(1 for r in rows if r.get("source_changed"))
    for row in rows:
        if row.get("error"):
            continue
        c, o = ("a", "b") if row["candidate_side"] == 0 else ("b", "a")
        cand = labels[(row[f"spec_{c}"], row.get(f"version_{c}"))]
        opp = labels[(row[f"spec_{o}"], row.get(f"version_{o}"))]
        table[(cand, opp)].append(candidate_view(row))
    lines = ["| candidate | opponent | n | W | D | L | mean HP diff | min HP diff | mean end round | cand rejected | cand errors | opp errors | cand decide s/match (max call) |",
             "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |"]
    totals = defaultdict(lambda: [0, 0, 0, 0])
    for (cand, opp), views in sorted(table.items()):
        n = len(views)
        w = sum(v["outcome"] == "W" for v in views)
        d = sum(v["outcome"] == "D" for v in views)
        l = sum(v["outcome"] == "L" for v in views)
        mean_hp = sum(v["hp_diff"] for v in views) / n
        min_hp = min(v["hp_diff"] for v in views)
        mean_r = sum(v["rounds"] for v in views) / n
        rej = sum(v["rejected"] for v in views)
        err = sum(v["errors"] for v in views)
        oerr = sum(v["opp_errors"] for v in views)
        dec = sum(v["decide_s"] for v in views) / n
        dmax = max(v["decide_max_s"] for v in views)
        lines.append(f"| {cand} | {opp} | {n} | {w} | {d} | {l} | {mean_hp:.1f} | {min_hp} | {mean_r:.1f} | {rej} | {err} | {oerr} | {dec:.2f} ({dmax:.2f}) |")
        t = totals[cand]
        t[0] += n; t[1] += w; t[2] += d; t[3] += l
    lines.append("")
    lines.append("| candidate | matches | W | D | L | score (W + D/2) / n |")
    lines.append("| --- | ---: | ---: | ---: | ---: | ---: |")
    for cand, (n, w, d, l) in sorted(totals.items()):
        lines.append(f"| {cand} | {n} | {w} | {d} | {l} | {(w + d / 2) / n:.3f} |")
    # Standings counting every match for both participants (round-robin view).
    standing = defaultdict(lambda: [0, 0, 0, 0, 0])
    for row in rows:
        if row.get("error"):
            continue
        for side, key in ((0, "a"), (1, "b")):
            st = standing[labels[(row[f"spec_{key}"], row.get(f"version_{key}"))]]
            st[0] += 1
            if row["winner"] is None:
                st[2] += 1
            elif row["winner"] == side:
                st[1] += 1
            else:
                st[3] += 1
            st[4] += row["hp_diff_a"] if side == 0 else -row["hp_diff_a"]
    lines.append("")
    lines.append("| bot (all matches, both perspectives) | matches | W | D | L | score | mean HP diff |")
    lines.append("| --- | ---: | ---: | ---: | ---: | ---: | ---: |")
    for spec, (n, w, d, l, hp) in sorted(standing.items(), key=lambda kv: -(kv[1][1] + kv[1][2] / 2) / kv[1][0]):
        lines.append(f"| {spec} | {n} | {w} | {d} | {l} | {(w + d / 2) / n:.3f} | {hp / n:.1f} |")
    if mixed or changed:
        lines.append("")
        lines.append(f"Version warning: {len(mixed)} spec/version labels from mixed-version results; "
                     f"{changed} matches with source changed during the match.")
    if failures:
        lines.append("")
        lines.append(f"Harness failures: {len(failures)}")
        for f in failures[:20]:
            lines.append(f"- {f['spec_a']} vs {f['spec_b']} ({f.get('scenario')}): {f['error']}")
    return "\n".join(lines) + "\n"


def load_rows(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as stream:
        return [json.loads(line) for line in stream if line.strip()]


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--name", required=True, help="experiment name (directory under runs/lead/)")
    parser.add_argument("--out-dir", help="override output directory (must be inside bot_research/)")
    parser.add_argument("--candidates", nargs="+", default=[])
    parser.add_argument("--opponents", nargs="+", default=[])
    parser.add_argument("--round-robin", nargs="+", default=None, help="play every pair among these specs")
    parser.add_argument("--scenarios", nargs="+", default=[None],
                        help="scenario names (see harness/scenarios.py); 'none' for the standard start")
    parser.add_argument("--jobs", type=int, default=2)
    parser.add_argument("--keep-logs", choices=("all", "losses", "none"), default="losses")
    parser.add_argument("--summarize-only", action="store_true")
    parser.add_argument("--append", action="store_true", help="allow adding to an existing results.jsonl")
    args = parser.parse_args(argv)

    out_dir = Path(args.out_dir) if args.out_dir else ROOT / "bot_research" / "runs" / "lead" / args.name
    out_dir = out_dir.resolve()
    if ROOT / "bot_research" not in out_dir.parents:
        parser.error("output directory must be inside bot_research/")
    results_path = out_dir / "results.jsonl"
    if args.summarize_only:
        (out_dir / "summary.md").write_text(summarize(load_rows(results_path)), encoding="utf-8")
        print((out_dir / "summary.md").read_text(encoding="utf-8"))
        return 0

    if results_path.exists() and not args.append:
        parser.error(f"{results_path.relative_to(ROOT)} exists; use a new --name or --append")
    scenarios = [None if s in (None, "none") else s for s in args.scenarios]
    pairs = []
    if args.round_robin:
        specs = args.round_robin
        for i, a in enumerate(specs):
            for b in specs[i + 1:]:
                pairs.append((a, b))
    for cand in args.candidates:
        for opp in args.opponents:
            pairs.append((cand, opp))
    tasks = []
    stamp = time.strftime("%Y%m%dT%H%M%S", time.gmtime())
    (out_dir / "logs").mkdir(parents=True, exist_ok=True)
    counter = 0
    for pair_index, (cand, opp) in enumerate(pairs):
        for scenario in scenarios:
            for side in (0, 1):
                a, b = (cand, opp) if side == 0 else (opp, cand)
                counter += 1
                scen = (scenario or "std").replace(":", "-")
                log = out_dir / "logs" / f"{stamp}-{counter:05d}-{_slug(a)}-vs-{_slug(b)}-{scen}.jsonl"
                tasks.append({"a": a, "b": b, "scenario": scenario, "candidate_side": side,
                              "pair": pair_index, "log": str(log), "keep_logs": args.keep_logs,
                              "first_of_pair": scenario == scenarios[0]})
    print(f"{len(tasks)} matches -> {out_dir.relative_to(ROOT)}", flush=True)
    ctx = mp.get_context("spawn")
    started = time.perf_counter()
    rows = []
    with ctx.Pool(args.jobs, maxtasksperchild=1) as pool, results_path.open("a", encoding="utf-8") as stream:
        for row in pool.imap_unordered(_run_one, tasks):
            row["experiment"] = args.name
            stream.write(json.dumps(row, separators=(",", ":")) + "\n")
            stream.flush()
            rows.append(row)
            if row.get("error"):
                print(f"[{len(rows)}/{len(tasks)}] ERROR {row['error']}", flush=True)
            else:
                v = candidate_view(row)
                print(f"[{len(rows)}/{len(tasks)}] {row['spec_a']} vs {row['spec_b']} {row.get('scenario') or ''} "
                      f"-> cand {v['outcome']} hp_diff {v['hp_diff']} r{v['rounds']} ({row['wall_seconds']}s)", flush=True)
    elapsed = time.perf_counter() - started
    all_rows = load_rows(results_path)
    (out_dir / "summary.md").write_text(summarize(all_rows), encoding="utf-8")
    print(f"done in {elapsed:.1f}s; summary at {(out_dir / 'summary.md').relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
