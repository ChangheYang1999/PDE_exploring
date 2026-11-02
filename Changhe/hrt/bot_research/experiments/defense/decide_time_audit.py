"""Decision-time audit over all tournament results in runs/defense: per candidate spec version, the maximum
single decide call and the maximum per-match decide total, plus rejected actions and bot errors.
Writes bot_research/runs/defense/decide_time_audit.txt."""
import glob
import json
import collections

agg = collections.defaultdict(lambda: {"matches": 0, "max_call": 0.0, "max_match": 0.0, "rejected": 0, "errors": 0})
for fn in sorted(glob.glob("bot_research/runs/defense/*/results.jsonl")):
    for line in open(fn):
        r = json.loads(line)
        if r.get("error"):
            continue
        side = r["candidate_side"]
        spec = (r["spec_a"] if side == 0 else r["spec_b"])
        if "bots.defense" not in spec:
            continue
        key = spec.split(":")[0].split(".")[-2] if "frozen" in spec else "live"
        a = agg[key]
        a["matches"] += 1
        a["max_call"] = max(a["max_call"], r["decide_max_seconds"][side])
        a["max_match"] = max(a["max_match"], r["decide_seconds"][side])
        a["rejected"] += r["players"][side]["n_rejected"]
        a["errors"] += len(r["players"][side]["bot_errors"])
out = ["| version | matches | max single decide (s) | max decide per match (s) | rejected actions | bot errors |", "| --- | ---: | ---: | ---: | ---: | ---: |"]
for k in sorted(agg, key=lambda k: (k != "live", k)):
    a = agg[k]
    out.append(f"| {k} | {a['matches']} | {a['max_call']:.2f} | {a['max_match']:.1f} | {a['rejected']} | {a['errors']} |")
text = "\n".join(out)
print(text)
open("bot_research/runs/defense/decide_time_audit.txt", "w").write(text)
