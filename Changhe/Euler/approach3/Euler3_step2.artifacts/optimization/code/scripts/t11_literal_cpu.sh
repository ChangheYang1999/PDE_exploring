#!/bin/bash
# SPEC T11, literal worker-level criterion (gate I.4: ten post-kill iterates on the current worker): two identical disposable CPU jobs; A runs
# uninterrupted; B is killed with SIGKILL once its checkpoint holds an iteration >= KILL_AT, then restarted from the same job file (the supervisor's
# resume path); the per-iteration LM histories (cost, damping, acceptance, sha256 of the iterate) and the final vectors are compared.
ROOT=$(cd "$(dirname "$0")/.." && pwd); cd $ROOT
export CUDA_VISIBLE_DEVICES=-1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONUNBUFFERED=1
KILL_AT=${1:-12}; D=runs/t11lit; LOG=$D/t11_literal_cpu.log
echo "$(date -u +%FT%TZ) T11 literal CPU test: kill B at checkpoint iteration >= $KILL_AT" | tee $LOG
for X in A B; do rm -rf $D/$X; mkdir -p $D/$X; rm -f status/heartbeat_resume_test_t11lit_cpu_$X.json; done
.venv/bin/python scripts/worker.py $D/job_A.json $D/A > $D/A/stdout.log 2>&1 &
PA=$!
.venv/bin/python scripts/worker.py $D/job_B.json $D/B > $D/B/stdout1.log 2>&1 &
PB=$!; echo "$(date -u +%FT%TZ) A pid $PA, B pid $PB" | tee -a $LOG
for i in $(seq 1 600); do
  sleep 2
  IT=$(python3 -c "import torch,sys;s=torch.load('$D/B/checkpoint.pt',map_location='cpu',weights_only=False);c=s['current'];print(-1 if c is None else c['it'])" 2>/dev/null || echo -1)
  if [ "$IT" -ge "$KILL_AT" ] 2>/dev/null; then break; fi
  if ! kill -0 $PB 2>/dev/null; then echo "B finished before the kill point (it $IT)" | tee -a $LOG; break; fi
done
kill -9 $PB 2>/dev/null; sleep 1
echo "$(date -u +%FT%TZ) B killed -9 with checkpoint at iteration $IT" | tee -a $LOG
.venv/bin/python scripts/worker.py $D/job_B.json $D/B > $D/B/stdout2.log 2>&1; echo "$(date -u +%FT%TZ) B resumed run exit $?" | tee -a $LOG
wait $PA; echo "$(date -u +%FT%TZ) A exit $?" | tee -a $LOG
grep -E "RESUME|resuming" $D/B/worker.log | tee -a $LOG
.venv/bin/python - <<PY | tee -a $LOG
import torch, hashlib
A = torch.load('$D/A/starts/start_000.pt', map_location='cpu', weights_only=False); B = torch.load('$D/B/starts/start_000.pt', map_location='cpu', weights_only=False)
hA, hB = A['history'], B['history']; k = $IT
def vdiff(a, b):
    za, zb = a.get('z_iter'), b.get('z_iter')
    if za is None or zb is None: return ''
    return f"| max|dz| {(za - zb).abs().max().item():.2e} rel-norm {((za - zb).norm() / za.norm()).item():.2e}"

print(f"iterations: A {len(hA)}, B {len(hB)}; resume point k = {k} (B's history before k comes from the checkpoint)")
ok = True; n_cmp = 0
for i in range(k, min(len(hA), len(hB), k + 10)):
    a, b = hA[i], hB[i]; n_cmp += 1
    same = (a.get('z_sha256_12') == b.get('z_sha256_12')) and (a['lam'] == b['lam']) and (a.get('accepted') == b.get('accepted')) and (a['cost'] == b['cost'])
    ok &= same
    print(f"  it {i+1}: cost A {a['cost']:.16e} B {b['cost']:.16e} | lam {a['lam']:.6e} / {b['lam']:.6e} | accepted {a.get('accepted')} / {b.get('accepted')} | z hash {a.get('z_sha256_12')} / {b.get('z_sha256_12')} {vdiff(a, b)} | {'EQUAL' if same else 'DIFF'}")
zA, zB = A['z'], B['z']
print(f"final vectors bitwise equal: {torch.equal(zA, zB)}; max |dz| {(zA - zB).abs().max().item():.3e}; sha A {hashlib.sha256(zA.numpy().tobytes()).hexdigest()[:12]} B {hashlib.sha256(zB.numpy().tobytes()).hexdigest()[:12]}")
allsame = all((hA[i].get('z_sha256_12') == hB[i].get('z_sha256_12')) and hA[i]['cost'] == hB[i]['cost'] for i in range(min(len(hA), len(hB))))
vmax = max([((hA[i]['z_iter'] - hB[i]['z_iter']).norm() / hA[i]['z_iter'].norm()).item() for i in range(k, min(len(hA), len(hB), k + 10)) if hA[i].get('z_iter') is not None and hB[i].get('z_iter') is not None] or [float('nan')])
cmax = max(abs(hA[i]['cost'] - hB[i]['cost']) / hA[i]['cost'] for i in range(k, min(len(hA), len(hB), k + 10)))
print(f"RESULT: ten post-kill iterates compared {n_cmp}: bitwise {'PASS' if ok and n_cmp == 10 else 'FAIL'}; largest relative-norm coefficient difference over the ten iterates {vmax:.3e} (registered T11 tolerance 1e-10: {'PASS' if vmax <= 1e-10 else 'FAIL'}); largest relative cost difference {cmax:.2e}; whole history bitwise equal: {allsame}; status A {A['status']} B {B['status']}")
PY
