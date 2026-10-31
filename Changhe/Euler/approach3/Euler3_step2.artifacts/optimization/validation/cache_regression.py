"""D6FP (lead 22:49Z item 3): O1 at S01 evaluated twice in one process (the second time from the angular-table cache) equals the value of a
fresh process bitwise; also the tables returned from the cache are clones (modifying one does not change the next hit)."""
import sys, os, json, subprocess
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import torch
torch.set_default_dtype(torch.float64)
from validation.gates import Case, ROOT
import src.bases.solid_harmonics as SH
start = os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt")
c1 = Case("S01", "cuda:0", start=start); o1 = c1.cost; r1 = c1.r.detach().clone(); n_dd_1 = SH.PATH_COUNTS["dd"]; del c1; torch.cuda.empty_cache()
c2 = Case("S01", "cuda:0", start=start); o2 = c2.cost; r2 = c2.r.detach().clone(); n_dd_2 = SH.PATH_COUNTS["dd"]
hits = len(SH._TABLE_CACHE)
# fresh process
code = "import sys, os; sys.path.insert(0, os.getcwd()); import torch; torch.set_default_dtype(torch.float64); from validation.gates import Case, ROOT; c = Case('S01', 'cuda:0', start=os.path.join(ROOT, 'starts', 'S01_nest6_cl0.45_om1.0_p0.pt')); print(repr(c.cost))"
o3 = float(subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, cwd=ROOT, env=dict(os.environ)).stdout.strip().splitlines()[-1])
# clone check
A = SH.eval_solid(c2.model.grid.n, c2.model.modes, c2.model.L_ext, 2, path="dd"); A[0][0, 0] += 1.0
B = SH.eval_solid(c2.model.grid.n, c2.model.modes, c2.model.L_ext, 2, path="dd")
out = dict(O1_first=o1, O1_second_cached=o2, O1_fresh_process=o3, bitwise_first_second=(o1 == o2), bitwise_second_fresh=(o2 == o3), residual_bitwise=bool(torch.equal(r1, r2)),
           cache_entries=hits, dd_calls_first=n_dd_1, dd_calls_total=n_dd_2, cached_hit_unmodified_by_caller=bool(float(B[0][0, 0]) != float(A[0][0, 0])))
print(json.dumps(out, indent=1)); json.dump(out, open(os.path.join(ROOT, "validation", "cache_regression.json"), "w"), indent=1)
