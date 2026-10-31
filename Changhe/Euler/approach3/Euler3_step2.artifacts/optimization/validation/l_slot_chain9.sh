#!/bin/bash
# Chain 9 v5 (add-on in a frozen copy) (lead 12:42:29Z item 3; GPU 4 from the P2 FREE segment-2 end): S20_own seven-step G3 add-on first (alone on GPU 4, about 60 GB), then the S05 z_c qualification as soon as its tie inputs (dd check record and J_cw l_eval record in chain 7's copy) exist, then the Jacobian-cost measurement.
cd RUN_ROOT/numerics/degree6_free_parameters_48h; LOG=validation/logs/l_slot_chain.log; WAIT=$1; GPU=4
echo "$(date -u +%FT%TZ) chain9 v5 armed: wait for pid $WAIT; GPU $GPU" >> $LOG
while kill -0 $WAIT 2>/dev/null; do sleep 15; done
go() { [ -f validation/STOP_L_CHAIN9 ] && { echo "$(date -u +%FT%TZ) STOP_L_CHAIN9" >> $LOG; exit 0; }; bash validation/l_launch.sh "$@"; }
go frozen g3addon_31b_S20_$(date -u +%H%M) $GPU g3_addon.py --tag gpu_v1_31b --cases S20_own
while [ ! -f validation/.chain7_S05_zc_check_name ] || [ ! -f "runs_l/$(cat validation/.chain7_S05_zc_check_name 2>/dev/null)/validation/dd_chain_check_S05_shift_c_optimizer_z_c.json" ] || [ ! -f "runs_l/$(cat validation/.chain7_S05_zc_check_name 2>/dev/null)/validation/l_eval_S05_shift_c_Jcw_optimizer_z_c_arrays.npz" ] || [ ! -f "runs_l/$(cat validation/.chain7_S05_zc_check_name 2>/dev/null)/validation/l_eval_S05_shift_c_Jcw_optimizer_z_c.json" ]; do sleep 30; done
sleep 30; N=$(cat validation/.chain7_S05_zc_check_name)
go frozen trigqual_S05_zc_$(date -u +%H%M) $GPU l_trig_qual.py S05_shift_c optimizer:z_c RUN_ROOT/numerics/degree6_free_parameters_48h/validation/gates_gpu_v1_S05_shift_c.json cuda:0 RUN_ROOT/numerics/degree6_free_parameters_48h/runs_l/$N
go frozen jaccost_$(date -u +%H%M) $GPU jac_cost.py cuda:0
echo "$(date -u +%FT%TZ) chain9 v5 done" >> $LOG
