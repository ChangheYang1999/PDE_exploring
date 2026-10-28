#!/bin/bash
# Historical packaging helper; requires the original source layout supplied as its argument.
cd -- "${1:?Usage: refresh_artifacts.sh SOURCE_DIRECTORY}" || exit 1
cp research/code/*.py artifacts/code/
cp research/runs/*.sh artifacts/code/
for f in wnorm_cert_131.json wnorm_cert_multi_131.json certSups_131_summary2.json certSups_131_frob_recombined.json stationary_order7.json stationary_order6_check.json \
         nb_Mpen2_exact.json nb_d2_exact.json nb_b6_exact.json nb_stableA3_Mscan.json nb_stableA4_Mscan.json nb_stableA5_Mscan.json nb_Mpen_Mscan.json nb_Mpen2_Mscan.json nb_b6_Mscan.json nb_d2_Mscan.json \
         nb_stableA4_hm1.json nb_stableA5_hm1.json nb_Mpen_hm1.json nb_Mpen2_hm1.json nb_b6_hm1.json nb_d2_hm1.json nb_stableA4_exact_lead.json nb_stableA5_exact_lead.json nb_Mpen_exact_lead.json nb_Mpen2_exact_lead.json nb_b6_exact_lead.json nb_d2_exact_lead.json \
         w_scan_d2.json w_scan_131.json w_scan_Mpen2.json w_scan_d2w.json nb_d2w_exact.json \
         state131_exact.json state131_farfield.json state131_origin_taylor.json exact_constants_131.json \
         farfield_M_cert_131.json certM_131_summary.json certM_131_B2.json certM_088_B2.json certM_131_Mk.json certM_131_far_summary.json certM_131_far_B2.json certM_131_far_Mk.json \
         farfield_Mk_cert_131.json certM_131_decay.json farfield_M_cert_131_arb.json farfield_Mk_cert_131_arb.json farfield_F_cert_131_arb.json certM_131_summary_arb.json certM_131_B2_arb.json certM_131_decay_arb.json origin_N4_131.json farfield_F_cert_131.json farfield_F_sharp_131.json state131_origin_taylor_deg34.json; do
  [ -f research/data/$f ] && cp research/data/$f artifacts/data/
done
rm -f artifacts/data/nb_Mpen_exact.json   # superseded by Mpen2 and d2 (size)
for f in research/runs/*.log; do b=$(basename $f); case $b in nb_*_coefs*|*certSups_131.log) ;; *) cp $f artifacts/logs/;; esac; done
cp NUM_REPORT.md NOTES_FOR_TEAM.md RUN_STATUS.md WORKLOG.md artifacts/
du -sh artifacts | cut -f1
