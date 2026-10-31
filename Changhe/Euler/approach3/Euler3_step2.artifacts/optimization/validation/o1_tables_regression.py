"""D6FP G5(c) requirement (lead 22:35Z item 5): O1 and the residual at the saved states S01, S05, S09 with float64 and with double-double angular tables."""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import torch
torch.set_default_dtype(torch.float64)
import src.bases.solid_harmonics as SH
from validation.gates import Case, ROOT
out = {}
for cname, fn in (("S01", "S01_nest6_cl0.45_om1.0_p0.pt"), ("S05", "S05_nest6_cl0.45_om0.3_p0.pt"), ("S09", "S09_d6w_cl0.45_om0.3_R1.pt")):
    vals = {}
    for mode in ("fp64", "dd"):
        SH.DD_TABLES = (mode == "dd"); SH._TABLE_CACHE.clear()
        case = Case(cname, "cuda:0", start=os.path.join(ROOT, "starts", fn))
        vals[mode] = dict(O1=case.cost, r=case.r.detach().clone(), far=case.r[case.row_group == 2].detach().clone())
        del case; torch.cuda.empty_cache()
    rel = abs(vals["dd"]["O1"] - vals["fp64"]["O1"]) / vals["fp64"]["O1"]
    rrel = float((vals["dd"]["r"] - vals["fp64"]["r"]).norm() / vals["fp64"]["r"].norm()); frel = float((vals["dd"]["far"] - vals["fp64"]["far"]).norm() / vals["fp64"]["far"].norm())
    out[cname] = dict(O1_fp64=vals["fp64"]["O1"], O1_dd=vals["dd"]["O1"], O1_rel_change=rel, residual_rel_change=rrel, far_group_residual_rel_change=frel)
    print(cname, json.dumps(out[cname]), flush=True)
SH.DD_TABLES = True
json.dump(out, open(os.path.join(ROOT, "validation", "o1_tables_regression.json"), "w"), indent=1)
print("DONE")
