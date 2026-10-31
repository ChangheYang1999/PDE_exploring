#!/usr/bin/env python
"""scripts/lrs_multi.py v2.1 (2026-10-30T03:08Z; --tool <file> selects the tool source, default scripts/linear_response_start.py); v2 (c1a8f42883ce4834): run several displacements of scripts/linear_response_start.py (unchanged, imported) IN ONE PYTHON PROCESS, so that the
host-slot guard sees one continuous computation (incident 4, 02:40:05Z: a shell loop of short python calls launched through l_launch_v6 cmd let another launcher
start in the gap between two calls). v2: groups with their own run directory and output prefix, and displacements with both coordinates.
Usage:
  python scripts/lrs_multi.py <device> --run <run dir> --prefix <out prefix> <spec> [<spec> ...] [--run <run dir 2> --prefix <prefix 2> <spec> ...]
  <spec> = dzw=<v> | dzc=<v> | dzc=<v>,dzw=<v> | name=<label>:dzc=<v>,dzw=<v>   (missing coordinate = 0; the output file is <prefix>_<label or spec text>)
v1 (dd80927faa60ea96): single run, one coordinate per spec."""
import sys, os, importlib.util
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
TOOL = "linear_response_start.py"
args0 = sys.argv[1:]
if args0 and args0[0] == "--tool":
    TOOL = args0[1]; args0 = args0[2:]
spec = importlib.util.spec_from_file_location("lrs_tool", os.path.join(ROOT, "scripts", TOOL) if not os.path.isabs(TOOL) else TOOL); L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)
dev = args0[0]; args = args0[1:]
groups = []; i = 0
while i < len(args):
    if args[i] == "--run":
        groups.append(dict(run=args[i + 1], prefix=None, specs=[])); i += 2
    elif args[i] == "--prefix":
        groups[-1]["prefix"] = args[i + 1]; i += 2
    else:
        groups[-1]["specs"].append(args[i]); i += 1
rc_all = 0
for g in groups:
    for s in g["specs"]:
        label = None
        if s.startswith("name="):
            label, s = s[5:].split(":", 1)
        parts = dict(kv.split("=") for kv in s.split(","))
        dzc = parts.get("dzc", "0"); dzw = parts.get("dzw", "0")
        out = f"{g['prefix']}_{label or s.replace(',', '_').replace('=', '')}"
        sys.argv = ["linear_response_start.py", g["run"], "--out", out, "--device", dev, "--dzc", dzc, "--dzw", dzw]
        print(f"=== {out} (dzc {dzc}, dzw {dzw})", flush=True)
        try:
            rc = L.main() or 0
        except SystemExit as e:
            rc = int(e.code or 0)
        except Exception as e:
            print(f"ERROR {out}: {e!r}", flush=True); rc = 3
        rc_all = max(rc_all, rc)
sys.exit(rc_all)
