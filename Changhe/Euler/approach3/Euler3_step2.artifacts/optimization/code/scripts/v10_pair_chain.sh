#!/bin/bash
# Genuine same-version admission pair with the candidate producer record_63a v10 (lead 20:06:30Z item 2, 20:11:10Z item 3; V439, V443):
# the P1 start reference (start mode) and the P1 segment-4 end (--full) on one exclusive GPU, then the decision wrapper (answer 'no' until admission).
# Usage: bash scripts/v10_pair_chain.sh <gpu> <lineage: P1|P2|F2>   (F2: end record against f2_start_v10 AND P1_start_v10, lead 18:49:47Z item 3)
set -u; cd RUN_ROOT/numerics/degree6_free_parameters_48h; D=$(pwd); PY=python3; export CUDA_VISIBLE_DEVICES=
GPU=$1; LIN=$2; LOG=validation/logs/l_slot_chain.log
case $LIN in
  P1) REF=P1_start_v10; JOB=$D/queue/done/p1_s1_S01_L6_cl0.4500_om1.0000_free.json; RUN=$D/runs/cont1_s4_S01_L6_cl0.4500_om1.0000_free; END=cont1_s4_S01_end_v10 ;;
  P2) REF=P2_start_v10; JOB=$D/queue/done/p2_s1_S09_L6_cl0.4500_om0.3000_free.json; RUN=$D/runs/cont2_s4_S09_L6_cl0.4500_om0.3000_free; END=cont2_s4_S09_end_v10 ;;
  F2) REF=f2_start_v10; JOB=$D/queue/done/f2_S01_k0_keep_L6_cl0.4597_om1.3389_free.json; RUN=$D/runs/f2_S01_k0_keep_m1_L6_cl0.4597_om1.3389_free; END=f2_S01_k0_keep_m1_end_v10; REF2=P1_start_v10 ;;
  *) echo "unknown lineage $LIN"; exit 2 ;;
esac
echo "$(date -u +%FT%TZ) v10 pair chain $LIN on GPU $GPU: producer $(sha256sum validation/record_63a.py | cut -c1-16), wrapper $(sha256sum scripts/r63a_decide.py | cut -c1-16)" | tee -a $LOG
[ -f validation/records_63a/$REF.json ] || bash scripts/r63a_run.sh $GPU $REF start $JOB
REF2=${REF2:-}; REF2OPT=""; REF2DEC=""
if [ -n "$REF2" ]; then [ -f validation/records_63a/$REF2.json ] || { echo "second reference $REF2 missing"; exit 3; }; REF2OPT="--start-ref $D/validation/records_63a/$REF2.json"; REF2DEC="--ref $REF2"; fi
bash scripts/r63a_run.sh $GPU $END end $RUN --full --start-ref $D/validation/records_63a/$REF.json $REF2OPT
DEC=$($PY scripts/r63a_decide.py --end $END --ref $REF $REF2DEC)
echo "$(date -u +%FT%TZ) 6.3 (a) decision for $END vs $REF: $DEC" | tee -a $LOG
echo "$(date -u +%FT%TZ) v10 pair chain $LIN done: $REF $(sha256sum validation/records_63a/$REF.json 2>/dev/null | cut -c1-16), $END $(sha256sum validation/records_63a/$END.json 2>/dev/null | cut -c1-16)" | tee -a $LOG
