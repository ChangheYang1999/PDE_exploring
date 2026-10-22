"""Per-resolution tables of the C2 Gram sections (NUM_REPORT 7.4b). Floating, evidence only.
Table 1 (version-2 outputs runs/c2/c2gram_<tag>_<variant>.json): spectrum and piecewise reference correlations.
Table 2 (version-3 outputs runs/c2/c2gram2_<tag>_H1m_NJ<n>.json, src/c2_gram2.py): the same three smallest values (consistency) and the cos^2 of the
X-angle between the 5 smallest singular directions and the CONTINUOUS references ref_J, ref_Jin, ref_wide (C^4 steps of x^2 y in log r), their
X-norms, and the cos^2 of each reference with the whole F- column span.
Usage: python3 src/c2_gram_table.py  -> prints and writes runs/c2/c2gram_table.md (table 1) and runs/c2/c2gram2_table.md (table 2)"""
import json, math, os
def sec(d, name): return d.get(name) or d.get("sections", {}).get(name)
specs = [("M16_s16_p2", "ppc 2"), ("M16_s16_p4", "ppc 4"), ("M16_s16_p6", "ppc 6"), ("M24_s8_p4", "M24/s8/Mout32 ppc 4")]
lines = ["| section (M16/s16/Mout40 unless noted) | rows | Gram / joins | retained | 3 smallest singular values (F-) | sigma_min/sqrt(rows) | largest | cos^2 of the 5 smallest directions with the J column (max) | with the tail span (max) | with J_inner, KP/TAU (max) | sigma_min (free tails) |", "|---|---:|---|---:|---|---:|---:|---:|---:|---|---:|"]
for tag, label in specs:
    for var in ("H1m_NJ0", "H1m_NJ1", "L2y_NJ0"):
        p = "runs/c2/c2gram_%s_%s.json" % (tag, var)
        if not os.path.exists(p): continue
        d = json.load(open(p)); F = sec(d, "Fminus"); fr = sec(d, "free"); n = d["nrows"]
        s5 = F["sigma_small5"]; sh = F["smallest5_shares"]; mx = lambda k: max(x[k] for x in sh)
        joins = ("NJ1 (v2, MIS-SPECIFIED: outer value jumps allowed, see 7.4b)" if var.endswith("NJ1") else "NJ0 (C^0)")
        lines.append("| %s (%s) | %d | %s / %s | %d | %.4f, %.4f, %.4f | %.3e | %.2e | %.1e | %.1e | %.1e, %.1e | %.4f |" % (
            label, tag, n, var.split("_")[0], joins, F["n_kept"], s5[0], s5[1], s5[2], s5[0] / math.sqrt(n), F["sigma_max"], mx("J_code"), mx("tails"), mx("J_inner"), mx("KP_TAU"), fr["sigma_small5"][0]))
table = "\n".join(lines); open("runs/c2/c2gram_table.md", "w").write(table + "\n"); print(table)
lines2 = ["| section | rows | joins | retained | 3 smallest (F-, version 3) | cos^2 of the 5 smallest directions with ref_J (max) | with ref_Jin (max) | with ref_wide (max) | principal cosine (5 smallest) vs ref_J, ref_Jin, ref_wide | X-norm ref_J, ref_Jin, ref_wide | cos^2 of ref_J, ref_Jin, ref_wide with the F- span |",
          "|---|---:|---|---:|---|---:|---:|---:|---|---|---|"]
specs3 = specs + [("M16_s8_o40_p4", "M16/s8/Mout40 ppc 4"), ("M24_s16_o40_p4", "M24/s16/Mout40 ppc 4"), ("M24_s16_o32_p4", "M24/s16/Mout32 ppc 4"), ("M24_s8_o40_p4", "M24/s8/Mout40 ppc 4"), ("M16_s16_p4_re2", "M16/s16/Mout40 ppc 4 (re2)")]
for tag, label in specs3:
    for NJ in (0, 1):
        p = "runs/c2/c2gram2_%s_H1m_NJ%d.json" % (tag, NJ)
        if not os.path.exists(p): continue
        d = json.load(open(p)); F = sec(d, "Fminus"); n = d["nrows"]; s5 = F["sigma_small5"]; sh = F["smallest5_shares"]
        mx = lambda rn: max(x["refs"][rn] for x in sh); pc = F["principal_cosine_near_null_vs_refs"]; R = d["Xnorm2"]["refs"]
        lines2.append("| %s (%s) | %d | C^%d | %d | %.4f, %.4f, %.4f | %.1e | %.1e | %.1e | %.1e, %.1e, %.1e | %.3e, %.3e, %.3e | %.4f, %.1e, %.4f |" % (
            label, tag, n, NJ, F["n_kept"], s5[0], s5[1], s5[2], mx("ref_J"), mx("ref_Jin"), mx("ref_wide"), pc["ref_J"], pc["ref_Jin"], pc["ref_wide"],
            R["ref_J"]["Xnorm"], R["ref_Jin"]["Xnorm"], R["ref_wide"]["Xnorm"], R["ref_J"]["cos2_with_section_span"], R["ref_Jin"]["cos2_with_section_span"], R["ref_wide"]["cos2_with_section_span"]))
table2 = "\n".join(lines2); open("runs/c2/c2gram2_table.md", "w").write(table2 + "\n"); print(); print(table2)

lines3 = ["| section, row type (L2q: value rows with radial trapezoid weights; H1: value + angular derivative + radial FD collocation rows; H1q: the same with trapezoid weights; all C^1 joins) | rows | retained | 3 smallest (F-) | sigma_min/sqrt(rows) | largest | cos^2 of the 5 smallest with the J column (max) | tail span | J_inner | ref_J | ref_Jin | ref_wide |",
          "|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
for tag, label in specs3:
  for rows in ("rowsL2q", "rowsH1", "rowsH1q"):
    p = "runs/c2/c2gram2_%s_H1m_NJ1_%s.json" % (tag, rows)
    if not os.path.exists(p): continue
    d = json.load(open(p)); F = sec(d, "Fminus"); n = d["nrows"]; s5 = F["sigma_small5"]; sh = F["smallest5_shares"]
    mx = lambda k: max(x[k] for x in sh); mr = lambda rn: max(x["refs"][rn] for x in sh)
    perrow = ("%.3e" % (s5[0] / math.sqrt(n))) if d["rows_mode"] == "H1" else "n/a (quadrature-weighted rows are comparable as they stand)"
    lines3.append("| %s (%s), %s | %d | %d | %.4f, %.4f, %.4f | %s | %.2e | %.1e | %.1e | %.1e | %.1e | %.1e | %.1e |" % (
        label, tag, d["rows_mode"], n, F["n_kept"], s5[0], s5[1], s5[2], perrow, F["sigma_max"], mx("J_code"), mx("tails"), mx("J_inner"), mr("ref_J"), mr("ref_Jin"), mr("ref_wide")))
table3 = "\n".join(lines3); open("runs/c2/c2gram2_rowsH1_table.md", "w").write(table3 + "\n"); print(); print(table3)
