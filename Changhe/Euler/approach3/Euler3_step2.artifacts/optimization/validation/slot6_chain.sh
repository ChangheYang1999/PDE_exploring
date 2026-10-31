#!/bin/bash
# Lead 10:00:40Z item 1: the slot freed by P1's FIXED-CONTROL member (about 10:31Z) is used, on GPU 6 beside the FREE member, for (a) the table
# screen if v4 is preflighted, else (b) manu_a seven-step G3 ladder + (k) add-on, then the manu_allm_c add-on. One process at a time; ledger rows.
# v2 (V246, lead 10:18:52Z item 1): the ledger is append-only; the sharing interval is two appended events interval_start / interval_end.
# Usage: validation/slot6_chain.sh <wait_pid> <item> [<item> ...]   items: screen_S01zc | screen_S05zc | screen_S05cl | ddcheck_S01 | g3_manu_a | addon_manu_a | addon_manu_allm_c
cd RUN_ROOT/numerics/degree6_free_parameters_48h; PY=python3
WAIT=$1; shift; LOG=validation/logs/slot6_chain.log
echo "$(date -u +%FT%TZ) chain armed: wait for pid $WAIT, then: $*" >> $LOG
while kill -0 $WAIT 2>/dev/null; do sleep 15; done
T0=$(date -u +%FT%TZ); echo "$T0 pid $WAIT gone; slot 6 chain starts" >> $LOG
$PY - "$T0" "$*" <<'PYEOF'
import json, sys
ts, items = sys.argv[1], sys.argv[2]
with open('status/ledger.jsonl', 'a') as f:      # V246: append-only; the interval is two appended events (interval_start here, interval_end at the chain end)
    f.write(json.dumps(dict(ts=ts, event='sharing_condition_interval_start', job='p1_s1_S01_L6_cl0.4500_om1.0000_free', start=ts,
                            detail=f"P1 FIXED-CONTROL member ended; its host slot runs validation items on GPU 6 beside the FREE member (lead 10:00:40Z item 1): {items}; the FREE member's sharing condition in this interval = one validation process on its GPU")) + '\n')
PYEOF
run() { echo "$(date -u +%FT%TZ) start: $*" >> $LOG; CUDA_VISIBLE_DEVICES=6 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 10 taskset -c 31-34 "$@"; echo "$(date -u +%FT%TZ) done exit $?: $*" >> $LOG; }
for item in "$@"; do
  case $item in
    screen_S01zc) run $PY -u validation/l_screen.py S01_shift_a validation/gates_gpu_v1_S01_shift_a.json optimizer:z_c 4 cuda:0 > validation/logs/l_screen_S01_shift_a_zc.log 2>&1 ;;
    screen_S05zc) run $PY -u validation/l_screen.py S05_shift_c validation/gates_gpu_v1_S05_shift_c.json optimizer:z_c 4 cuda:0 > validation/logs/l_screen_S05_shift_c_zc.log 2>&1 ;;
    screen_S05cl) run $PY -u validation/l_screen.py S05_shift_c validation/gates_gpu_v1_S05_shift_c.json physical:c_l 4 cuda:0 > validation/logs/l_screen_S05_shift_c_cl.log 2>&1 ;;
    ddcheck_S01) run $PY -u validation/dd_chain.py S01_shift_a optimizer:z_c Jcw,Jf,Jc cuda:0 > validation/logs/dd_chain_check_S01_shift_a.log 2>&1 ;;
    ddcheck_S05) run $PY -u validation/dd_chain.py S05_shift_c physical:c_l Jcw,Jf,Jc cuda:0 > validation/logs/dd_chain_check_S05_shift_c.log 2>&1 ;;
    g3_manu_a) run $PY -u validation/g3_addon.py --tag gpu_v1_31 --cases manu_a > validation/logs/g3_addon_gpu_v1_31_manu_a.log 2>&1 ;;   # separate tag: the gpu_v1 aggregate of the four release cases is not rewritten
    addon_manu_a) run $PY -u validation/g1_step_addon.py manu_a validation/gates_gpu_v1_manu_a.json > validation/logs/g1_step_addon_manu_a.log 2>&1 ;;
    addon_manu_allm_c) run $PY -u validation/g1_step_addon.py manu_allm_c validation/gates_gpu_v1_manu_allm_c.json > validation/logs/g1_step_addon_manu_allm_c.log 2>&1 ;;
    *) echo "$(date -u +%FT%TZ) unknown item $item" >> $LOG ;;
  esac
  [ -f validation/STOP_SLOT6_CHAIN ] && { echo "$(date -u +%FT%TZ) STOP_SLOT6_CHAIN present" >> $LOG; break; }
done
T1=$(date -u +%FT%TZ); echo "$T1 slot 6 chain done" >> $LOG
$PY - "$T1" <<'PYEOF'
import json, sys
ts = sys.argv[1]
with open('status/ledger.jsonl', 'a') as f:
    f.write(json.dumps(dict(ts=ts, event='sharing_condition_interval_end', job='p1_s1_S01_L6_cl0.4500_om1.0000_free', end=ts, detail='slot-6 validation chain ended; the FREE member runs alone on GPU 6 again')) + '\n')
PYEOF
