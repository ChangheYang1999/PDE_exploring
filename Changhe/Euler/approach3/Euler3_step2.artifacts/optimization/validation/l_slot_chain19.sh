#!/bin/bash
# Chain 19 (16:28Z; V371 ADMITTED gauge_row_dd.py v4.5 6dc4db700e3325fb with the pre-input 7eb9cebb61160bd3 / a5352272efbeec6c): the registered SPEC 3.6 (n) (5) evaluation of manu_a column 189 ONLY, frozen copy, GPU 4 (next to chain 18).
cd RUN_ROOT/numerics/degree6_free_parameters_48h; LOG=validation/logs/l_slot_chain.log; GPU=4
echo "$(date -u +%FT%TZ) chain19 started ((n)(5) evaluation manu_a column 189; V371 admission)" >> $LOG
bash validation/l_launch.sh frozen gaugedd_eval_189_$(date -u +%H%M) $GPU gauge_row_dd.py evaluate manu_a 189 cuda:0
echo "$(date -u +%FT%TZ) chain19 done" >> $LOG
