"""Post-hoc evaluation of the saved weakest directions of a C2 Gram section under ALL FOUR row functionals (L2, L2q, H1, H1q) from their saved
unweighted collocation images (Lh)_N(t_i) (c2_gram2.py v3, <section>_img in the _vec.npz; rows i*Mout + N), so that the same vectors are compared
in the different image norms (astra gram4, item 2).  The quotient is ||rows(img)||_2 / sqrt(h^T G h) with the saved hGh (about 1).  Floating.
Usage: python3 src/c2_img_eval.py out_vec.npz [section=Fminus]"""
import sys, json
import numpy as np


def row_functionals(img, t_eval, w_i, Mout):
    Ne = len(t_eval); X3 = img.reshape(Ne, Mout, -1)
    dtv = np.diff(t_eval); om = np.zeros(Ne); om[:-1] += 0.5 * dtv; om[1:] += 0.5 * dtv
    ang = np.sqrt(1.0 + (2 * np.arange(Mout) + 1.0) ** 2); wm = 0.5 * (w_i[1:] + w_i[:-1])
    out = {}
    for rows in ("L2", "L2q", "H1", "H1q"):
        q = rows.endswith("q"); so = np.sqrt(om) if q else np.ones(Ne); sd = np.sqrt(dtv) if q else np.ones(Ne - 1)
        val = X3 * (w_i * so)[:, None, None]
        if rows.startswith("H1"):
            val = val * ang[None, :, None]
            der = (X3[1:] - X3[:-1]) * (wm * sd / dtv)[:, None, None]
            tot = (val ** 2).sum((0, 1)) + (der ** 2).sum((0, 1))
        else: tot = (val ** 2).sum((0, 1))
        out[rows] = np.sqrt(tot)
    return out


def main(vec, section="Fminus"):
    v = np.load(vec, allow_pickle=True)
    img = v[section + "_img"]; hGh = v[section + "_hGh"]; sig = v[section + "_sigma"]
    f = row_functionals(img, v["t_eval"], v["w_i"], int(v["Mout"]))
    res = dict(vec=vec, section=section, rows_mode_of_run=str(v["ROWS"]), sigma_saved=[float(x) for x in sig],
               quotients={k: [float(x / np.sqrt(g)) for x, g in zip(val, hGh)] for k, val in f.items()})
    print("%s (%s; run rows %s): saved sigma %s" % (vec, section, res["rows_mode_of_run"], ["%.5f" % x for x in sig]))
    for k, q in res["quotients"].items(): print("   %-4s quotients of the same vectors: %s" % (k, ["%.5f" % x for x in q]))
    jo = vec.replace("_vec.npz", "_imgeval_%s.json" % section); json.dump(res, open(jo, "w"), indent=1); print("saved", jo)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "Fminus")
