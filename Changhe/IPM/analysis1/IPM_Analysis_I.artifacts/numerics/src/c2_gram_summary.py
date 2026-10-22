"""Tabulate the C2-Gram outputs runs/c2/c2gram_*.json (floating, evidence only): per run (tag, mode, NJ) and section, the retained dimension,
constraint rank, whitening error, sigma_max, the 5 smallest singular values, spectrum quantiles, the shares of the smallest direction
(J_code, J_inner, tails, KP/TAU, kinds), the principal cosines of the 5 smallest directions vs the tail span and vs J_inner, and the ell values.
Usage: python3 src/c2_gram_summary.py > runs/c2/c2gram_summary.txt
"""
import glob, json, os, re
lane = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
files = sorted(glob.glob(os.path.join(lane, "runs/c2/c2gram_*_*_NJ*.json")))
print("%-22s %-5s %-3s %-11s %6s %5s %9s %10s %-44s %-30s %6s %6s %6s %6s %-28s %-10s" % ("run", "mode", "NJ", "section", "ncol", "kept", "whit_err", "sigma_max", "sigma_small5", "quantiles 1%/5%/25%/50%", "J_code", "J_inn", "tails", "KPTAU", "pc(tails) first 3", "pc(J_inn)"))
for f in files:
    d = json.load(open(f)); base = os.path.basename(f)[7:-5]
    m = re.match(r"(.*)_(H1m|H1|L2y)_NJ(\d)", base); tag, mode, nj = m.groups()
    for name, sec in d["sections"].items():
        sh = sec["smallest5_shares"][0]; q = sec["sigma_quantiles"]
        print("%-22s %-5s %-3s %-11s %6d %5d %9.1e %10.3e %-44s %-30s %6.3f %6.3f %6.3f %6.3f %-28s %-10.4f" % (
            tag, mode, nj, name, sec["ncol"], sec["n_kept"], sec["whitening_error_refined_quadrature"], sec["sigma_max"],
            " ".join("%.3e" % x for x in sec["sigma_small5"]), " ".join("%.2e" % q[k] for k in ("0.01", "0.05", "0.25", "0.5")),
            sh["J_code"] if sh["J_code"] is not None else float("nan"), sh["J_inner"], sh["tails"], sh["KP_TAU"],
            " ".join("%.3f" % x for x in sec["principal_cosines_near_null_vs_tails"][:3]), sec["principal_cosine_near_null_vs_Jinner"]))
    if "ell" in d:
        for lab, v in d["ell"]["values"].items():
            print("    ell %-28s dk %.4e dtau %.4e rel_res %.3f rank %d ||h||_X %.3e" % (lab, v["dk"], v["dtau"], v["rel_residual"], v["rank"], v["h_X_norm"]))
