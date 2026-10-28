# Interruption and resume test (disposable job runs/resume_test, SPEC T11)

- 2026-10-24T18:01Z: worker started on GPU 5 (L=4, Nk=10, vorticity LM, checkpoint interval 30 s for the test).
- 18:03:28Z: kill -9 of the worker process (checkpoint state: start 0 at iteration 227).
- 18:03:33Z: restarted from the same job file: log shows "RESUME from checkpoint ... current=0" and "start 0: resuming at iteration 227"; the job then completed both starts.
- Determinism: the same job run uninterrupted (runs/resume_test_uninterrupted, GPU 5) gives the rms_final values printed in logs/resume_test_T11.txt; start 0 (interrupted and resumed) agrees with the uninterrupted run to the printed relative difference.
- The supervisor's own recovery (orphaned running jobs moved back to pending, workers resume from checkpoint.pt) is exercised whenever scripts/start_supervisor.sh is run after a supervisor death; see logs/supervisor.log.

- 2026-10-25T05:57Z Relabelling (verifier 05:40Z, lead 05:42Z): the 0.992 "relative difference" in logs/resume_test_T11.txt compared two differently defined metrics (the interrupted run's rms_final is the LM per-entry rms, the uninterrupted run's is the physical vorticity RMS); identically defined metrics agree exactly and the saved final tensors are bitwise identical. The ten post-resume iterates are now compared by tests/test_T11_resume_iterates.py (worker checkpoint/resume state at the API level: coefficients 8.7e-11, damping exact, acceptance flags equal, default and deterministic cuBLAS), which is the SPEC T11 statement; the worker-level kill -9 test above remains the end-to-end check.
