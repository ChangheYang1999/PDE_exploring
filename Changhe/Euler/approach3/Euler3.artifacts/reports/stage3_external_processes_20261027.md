# External (non-campaign) GPU processes seen on the assigned GPUs 0, 1, 4, 5 during the Stage III early-start jobs (lead ND items 2 and 5)

Rule: sample nvidia-smi --query-compute-apps at least every 15 min while an external process is present; record first and last sighting per device; the KO7-type sentence with the device's interval goes into each affected job's reading; hourly status lines for affected jobs carry only the LM iteration count and its log timestamp (no cost value). No external process is touched; no job is stopped, relaunched or moved (ND item 1).

Jobs: GPU 0 s3r1_L8_cl0.45_om+1.0_fixed_p1e-2_s31001 pid 21129 (launched 07:03:15Z); GPU 1 s3r1_L8_cl0.45_om+1.0_fixed_p3e-2_s31002 pid 186803 (07:13:23Z); GPU 4 s3r1_L8_cl0.45_om+1.0_fixed_p1e-1_s31003 pid 235589 (07:15:25Z); GPU 5 s3r3_L8_cl0.45_om+1.0_fixed_allm_odd1e-1_s31030 pid 248785 (07:16:46Z). Physical placement confirmed by the lead from /proc/<pid>/environ CUDA_VISIBLE_DEVICES (0, 1, 4, 5).

## Process A: pid 175411 <other project> (ps lstart 07:13:05Z; parent 139773); ENDED (absent from ps and nvidia-smi at 07:20:22Z and 07:21:07Z)
| sample (UTC) | GPU 0 | GPU 1 | GPU 4 | GPU 5 | other GPUs |
|---|---|---|---|---|---|
| 07:14:07Z | 604 MiB | - | - | - | - |
| 07:14:23Z | 606 MiB | - | - | - | - |
| 07:15:14Z | 606 MiB | - | - | - | - |
| 07:15:59Z | 606 MiB | 418 MiB | - | - | GPU 2 416 MiB |
| 07:16:36Z (lead) | 610 MiB | 494 MiB | - | - | GPU 2 418 MiB |
| 07:16:41Z | 610 MiB | 494 MiB | - | - | GPU 2 418 MiB |
| 07:20:22Z | absent | absent | absent | absent | absent |
Intervals: GPU 0 (s31001) 07:14:07Z to 07:16:41Z; GPU 1 (s31002) 07:15:59Z to 07:16:41Z; GPU 4, GPU 5 never.

## Process B: pid 296033 <other project> distributed_train sweep (ps lstart 07:20:54Z per the lead); on all 8 GPUs; ENDED (absent from ps and nvidia-smi at 07:45:01Z; last sighting 07:30:08Z)
| sample (UTC) | GPU 0 | GPU 1 | GPU 4 | GPU 5 | other GPUs |
|---|---|---|---|---|---|
| 07:23:08Z (lead) | 636 MiB | 584 MiB | 562 MiB | 560 MiB | GPUs 2, 3, 6, 7: 554 to 593 MiB; utilisation 0 per cent on 2, 3, 6, 7 at 07:23:20Z |
| 07:25:37Z | 752 MiB | 660 MiB | 620 MiB | 618 MiB | GPU 2 640, GPU 3 640, GPU 6 616, GPU 7 612 MiB |
| 07:30:08Z | 840 MiB | 800 MiB | 834 MiB | 758 MiB | GPU 2 804 MiB, GPU 3 828 MiB, GPU 6 688 MiB, GPU 7 638 MiB |
| 07:45:01Z | absent | absent | absent | absent | GPU 2 absent, GPU 3 absent, GPU 6 absent, GPU 7 absent |
Intervals (process B): GPU 0 (s31001), GPU 1 (s31002), GPU 4 (s31003), GPU 5 (s31030): first sighting 07:23:08Z (lead), last 07:30:08Z, absent at 07:45:01Z (process start 07:20:54Z).

## Process C: pid 579692 <other project> tensor_parallel_train (ps lstart 07:42:09Z; parent 575361); on all 8 GPUs; ENDED (absent from nvidia-smi and ps at 07:49:36Z per the lead; absent at 07:57:43Z, my sample)
| sample (UTC) | GPU 0 | GPU 1 | GPU 4 | GPU 5 | other GPUs |
|---|---|---|---|---|---|
| 07:45:01Z | 1624 MiB | 1028 MiB | 660 MiB | 660 MiB | GPU 2 878, GPU 3 750, GPU 6 660, GPU 7 662 MiB |
Intervals (process C): every assigned device (GPU 0 s31001, GPU 1 s31002, GPU 4 s31003, GPU 5 s31030): first and last sighting 07:45:01Z (a single sample; absent at 07:49:36Z). A process start time is not a sighting.

## Process D: pid 634498 <other project> distributed_train (ps start 07:46:29Z, nice 5, parent lake pid 629522; per the lead NH); on all 8 GPUs; ENDED (absent from nvidia-smi and ps at 07:57:43Z, my sample)
| sample (UTC) | GPU 0 | GPU 1 | GPU 4 | GPU 5 | other GPUs |
|---|---|---|---|---|---|
| 07:49:36Z (lead) | 638 MiB | 704 MiB | 598 MiB | 598 MiB | GPU 2 652, GPU 3 628, GPU 6 598, GPU 7 598 MiB |
| 07:57:43Z | absent | absent | absent | absent | absent |
Intervals (process D): every assigned device: first and last sighting 07:49:36Z (the lead's sample; my 07:45:01Z sample preceded its start and my next sample at 07:57:43Z found it gone; the planned 08:00Z sample was lost to a shell timeout).

## Process F (lettered after E because E was named first; it started earlier): pid 751563 <other project> distributed_train elastic (ps start 07:54:04Z, nice 5, parent 746636; per the lead NI); on all 8 GPUs; ENDED (absent at the lead's 07:58:58Z sample and from ps)
| sample (UTC) | GPU 0 | GPU 1 | GPU 4 | GPU 5 | other GPUs |
|---|---|---|---|---|---|
| 07:54:54Z (lead) | 592 MiB | 552 MiB | 548 MiB | 550 MiB | GPU 2 552, GPU 3 552, GPU 6 540, GPU 7 540 MiB |
| 07:58:58Z (lead) | absent | absent | absent | absent | absent |
Intervals (process F): every assigned device: first and last sighting 07:54:54Z (the lead's sample).

## Process E: pid 823974 <other project> sequence_parallel (ps lstart 07:57:35Z, nice 5); on all 8 GPUs; ENDED (absent at the lead's 07:58:58Z sample; absent from nvidia-smi and ps at 08:07:51Z, my sample)
| sample (UTC) | GPU 0 | GPU 1 | GPU 4 | GPU 5 | other GPUs |
|---|---|---|---|---|---|
| 07:57:43Z | 554 MiB | 536 MiB | 528 MiB | 528 MiB | GPU 2 532, GPU 3 530, GPU 6 526, GPU 7 526 MiB |
| 07:58:58Z (lead) | absent | absent | absent | absent | absent (no external process on any GPU; only our four pids) |
| 08:07:51Z | absent | absent | absent | absent | absent (no external process on any GPU) |
Intervals (process E): every assigned device: first and last sighting 07:57:43Z (my sample).

## Summary of external-process intervals per assigned device (for the KO7-type sentences; updated 2026-10-27T08:08:40Z)
- GPU 0 (s31001, pid 21129): A 07:14:07Z to 07:16:41Z (0.60 to 0.61 GB); B 07:23:08Z to 07:30:08Z (0.64 to 0.84 GB); C 07:45:01Z (1.62 GB, single sample); D 07:49:36Z (0.64 GB, single sample, lead); F 07:54:54Z (0.59 GB, single sample, lead); E 07:57:43Z (0.55 GB, single sample).
- GPU 1 (s31002, pid 186803): A 07:15:59Z to 07:16:41Z (0.42 to 0.49 GB); B 07:23:08Z to 07:30:08Z (0.58 to 0.80 GB); C 07:45:01Z (1.03 GB); D 07:49:36Z (0.70 GB, lead); F 07:54:54Z (0.55 GB, lead); E 07:57:43Z (0.54 GB).
- GPU 4 (s31003, pid 235589): B 07:23:08Z to 07:30:08Z (0.56 to 0.83 GB); C 07:45:01Z (0.66 GB); D 07:49:36Z (0.60 GB, lead); F 07:54:54Z (0.55 GB, lead); E 07:57:43Z (0.53 GB).
- GPU 5 (s31030, pid 248785): B 07:23:08Z to 07:30:08Z (0.56 to 0.76 GB); C 07:45:01Z (0.66 GB); D 07:49:36Z (0.60 GB, lead); F 07:54:54Z (0.55 GB, lead); E 07:57:43Z (0.53 GB).
| 08:17:36Z | absent | absent | absent | absent | absent (no external process on any GPU) |
| 08:28:11Z | absent | absent | absent | absent | absent (no external process on any GPU) |
| 08:37:14Z | absent | absent | absent | absent | absent (no external process on any GPU) |
| 08:46:55Z | absent | absent | absent | absent | absent (no external process on any GPU) |
| 08:55:11Z | absent | absent | absent | absent | absent (no external process on any GPU) |
| 09:03:39Z | absent | absent | absent | absent | absent (no external process on any GPU) |
| 09:12:04Z | absent | absent | absent | absent | absent (no external process on any GPU) |
| 09:20:32Z | absent | absent | absent | absent | absent (no external process on any GPU) |
| 09:28:55Z | absent | absent | absent | absent | absent (no external process on any GPU) |
| 09:37:14Z | absent | absent | absent | absent | absent (no external process on any GPU) |
| 09:44:58Z | absent | absent | absent | absent | absent (no external process on any GPU) |
| 09:50:28Z | absent | absent | absent | absent | absent (no external process on any GPU) |
| 10:01:42Z | absent | absent | absent | absent | absent (no external process on any GPU) |
| 10:09:36Z | absent | absent | absent | absent | absent (no external process on any GPU) |
| 10:20:52Z | absent | absent | absent | absent | absent (no external process on any GPU) |
| 10:29:24Z | absent | absent | absent | absent | absent (no external process on any GPU) |
| 10:31:56Z | absent | absent | absent | absent | absent (no external process on any GPU; only our four pids 2350739 GPU 0, 2438011 GPU 1, 2454828 GPU 4, 248785 GPU 5) |
| 10:36:33Z | absent | absent | absent | absent | absent (no external process on any GPU; only our four pids) |
| 10:39:20Z | absent | absent | absent | absent | absent (no external process on any GPU; only our four pids) |
| 10:42:47Z | absent | absent | absent | absent | absent (no external process on any GPU; only our four pids) |
| 10:44:04Z | absent | absent | absent | absent | absent (no external process on any GPU; only our four pids) |
| 10:49:54Z | absent | absent | absent | absent | absent (no external process on any GPU; only our four pids) |
| 10:54:49Z | absent | absent | absent | absent | absent (no external process on any GPU; only our four pids) |
| 10:59:13Z | absent | absent | absent | absent | absent (no external process on any GPU; only our four pids) |
| 11:01:37Z | absent | absent | absent | absent | absent (no external process on any GPU; only our four pids) |
| 11:04:51Z | absent | absent | absent | absent | absent (no external process on any GPU; only our four pids) |
| 11:07:07Z | absent | absent | absent | absent | absent (no external process on any GPU; only our four pids) |
| 11:10:54Z | absent | absent | absent | absent | absent (no external process on any GPU; only our four pids) |
| 11:14:34Z | absent | absent | absent | absent | absent (no external process on any GPU; only our four pids) |
| 11:19:54Z | absent | absent | absent | absent | absent (no external process on any GPU; only our four pids) |
| 11:24:05Z | absent | absent | absent | absent | absent (no external process on any GPU; only our four pids) |
| 11:26:45Z | absent | absent | absent | absent | absent (no external process on any GPU; only our four pids) |
| 11:32:39Z | absent | absent | absent | absent | absent (no external process on any GPU; only our four pids) |
| 11:38:16Z | absent | absent | absent | absent | absent (no external process on any GPU; only our four pids; sampled by the command above) |
| 11:41:25Z | absent | absent | absent | absent | absent (no external process on any GPU; only our four pids; R3 in its battery) |
| 11:45:31Z | absent | absent | absent | absent | absent (no external process on any GPU; only our four pids; R3 in its battery) |
| 11:50:51Z | absent | absent | absent | absent | absent (no external process on any GPU; only our four pids) |
| 11:56:45Z | absent | absent | absent | absent | absent (no external process on any GPU; only our four pids; R3 in its battery) |
| 12:02:29Z | absent | absent | absent | absent | absent (no external process on any GPU; only our four pids; R3 in its battery) |
| 12:08:16Z | absent | absent | absent | absent | absent (no external process on any GPU; only our four pids; R3 and R2c in their batteries) |
| 12:13:57Z | absent | absent | absent | absent | absent (no external process on any GPU; only our four pids; R3 and R2c in their batteries) |
| 12:19:40Z | absent | absent | absent | absent | GPU 6 (uuid eada0581, not ours): pid 3026291, 794 MiB, process G (identified below); none on GPUs 0, 1, 4, 5 |
Process G (identification): pid 3026291, started 12:14:09Z, nice 19, the VERIFIER lane's own job (<independent-route directory>/independent/.venv/bin/python ... verification_stage3/selected_pressure_wo...), on GPU 6 only (not an assigned numerics device; none of ours affected); sightings on GPU 6: 12:19:40Z (794 MiB), 12:20:59Z (794 MiB).
| 12:24:44Z | absent | absent | absent | absent | GPU 6 (not ours): verifier pid 3026291, 794 MiB; none on GPUs 0, 1, 4, 5 |
| 12:28:34Z | absent | absent | absent | absent (R3 ended 12:27:04Z, GPU 5 empty) | GPU 6 (not ours): verifier pid 3026291, 794 MiB |
| 12:31:17Z | absent | absent | absent | absent (GPU 5 empty since 12:27Z) | GPU 6 (not ours): verifier pid 3026291, 794 MiB; R2a, R2b, R2c all in their batteries |
| 12:34:51Z | absent | absent | absent | absent (GPU 5 idle) | GPU 6 (not ours): verifier pid 3026291, 794 MiB; R2a, R2b, R2c in their batteries |
| 12:41:04Z | absent | absent | absent | absent (GPU 5 idle) | GPU 6 (not ours): verifier pid 3026291, 794 MiB; R2a, R2b, R2c in their batteries |
| 12:48:25Z | absent | absent | absent | absent (GPU 5 idle) | GPU 6 (not ours): verifier pid 3026291, 808 MiB; R2a, R2b, R2c in their batteries |
| 12:50:07Z | absent | absent | absent | absent (GPU 5 idle) | absent (the verifier's GPU 6 process pid 3026291 is gone: sightings 12:19:40Z to 12:48:25Z) |
| 13:01:02Z | absent | absent | absent (R4 control pid 3181582 since 12:58:17Z) | absent (GPU 5 idle) | absent |
| 13:05:00Z | absent | absent | absent (R4 control pid 3181582) | absent (GPU 5 idle) | absent |
| 13:09:57Z | absent | absent | absent (R4 control pid 3181582) | absent (GPU 5 idle) | absent |
| 13:15:36Z | absent | absent | absent (R4 control pid 3181582, 42.6 GB) | absent (GPU 5 idle) | absent |
| 13:20:22Z | absent | absent (R4 perturbed pid 3251094 since 13:19:15Z) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | absent |
| 13:22:04Z | absent | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | GPU 6 (not ours): pid 3259495, 794 MiB (process H, identified below) |
| 13:25:11Z | absent | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | GPU 6 (not ours): verifier pid 3259495 (started 13:21:37Z), 794 MiB |
| 13:32:09Z | absent (GPU 0 idle since 13:26Z) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | GPU 6 (not ours): verifier pid 3259495, 794 MiB |
| 13:35:08Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | GPU 6 (not ours): verifier pid 3259495, 794 MiB |
| 13:39:12Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094, 42.6 GB) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | GPU 6 (not ours): verifier pid 3259495, 794 MiB |
| 13:42:50Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094, 43.0 GB) | absent (R4 control pid 3181582, 43.7 GB) | absent (GPU 5 idle) | GPU 6 (not ours): verifier pid 3259495, 794 MiB |
| 13:47:06Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | GPU 6 (not ours): verifier pid 3259495, 794 MiB |
| 13:50:05Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | GPU 6 (not ours): verifier pid 3259495, 794 MiB |
| 13:53:52Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | GPU 6 (not ours): verifier pid 3259495, 794 MiB |
| 13:56:25Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | GPU 6 (not ours): verifier pid 3259495, 794 MiB |
| 14:00:47Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | GPU 6 (not ours): verifier pid 3259495, 794 MiB |
| 14:06:29Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | GPU 6 (not ours): verifier pid 3259495, 794 MiB |
| 14:12:17Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | GPU 6 (not ours): verifier pid 3259495, 794 MiB |
| 14:16:42Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | GPU 6 (not ours): verifier pid 3259495, 808 MiB |
| 14:22:04Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | absent (the verifier's GPU 6 process pid 3259495 is gone: sightings 13:21:37Z (start) to 14:16:42Z) |
| 14:27:48Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | absent |
| 14:33:33Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | absent |
| 14:39:22Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | absent |
| 14:45:04Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | absent |
| 14:50:49Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | GPU 6 (not ours): pid 3539217, 794 MiB (process I, identified in the next line) |
Process I (identification, 14:51:06Z): pid 3539217 = Tue Oct 27 14:48:04 2026 <independent-route directory>/independent/.venv/bin/python -I -B <shared volume>/pde-e  ; on GPU 6 only (not an assigned numerics device).
| 14:54:03Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | GPU 6 (not ours): verifier pid 3539217, 794 MiB |
| 14:59:48Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | GPU 6 (not ours): verifier pid 3539217, 794 MiB |
| 15:05:34Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | GPU 6 (not ours): verifier pid 3539217, 794 MiB |
| 15:11:19Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | GPU 6 (not ours): verifier pid 3539217, 794 MiB |
| 15:14:03Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | GPU 6 (not ours): verifier pid 3539217, 794 MiB |
| 15:19:40Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | GPU 6 (not ours): verifier pid 3539217, 794 MiB |
| 15:25:23Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | GPU 6 (not ours): verifier pid 3539217, 794 MiB |
| 15:31:05Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | GPU 6 (not ours): verifier pid 3539217, 794 MiB |
| 15:36:49Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | GPU 6 (not ours): verifier pid 3539217, 794 MiB |
| 15:42:31Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | GPU 6 (not ours): verifier pid 3539217, 794 MiB |
| 15:48:16Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | GPU 6 (not ours): verifier pid 3539217, 808 MiB |
| 15:52:50Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | GPU 6 (not ours): verifier pid 3539217, 808 MiB |
| 15:58:31Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | absent (the verifier's GPU 6 process pid 3539217 is gone: sightings 14:48:04Z (start) to 15:52:50Z) |
| 16:04:13Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | absent |
| 16:09:21Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | absent |
| 16:15:06Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | absent |
| 16:20:50Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | absent |
| 16:24:42Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | absent (sampled by this command; see nvidia-smi output in WORKLOG context) |
| 16:26:37Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | absent |
| 16:33:23Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | GPU 6 (not ours): verifier SOURCE R3 pid 3854886, 794 MiB (first seen by this lane 16:31:51Z; the verifier records its launch at 16:26:43Z) |
| 16:38:21Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | absent (no compute process on GPU 6 at this sample) |
| 16:41:46Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | absent (no compute process on GPU 6) |
| 16:46:15Z | ours: VT validation pid 3917990 (lead QD VT, launched 16:45:11Z; not external) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | absent (no compute process on GPU 6) |
| 16:51:26Z | ours: VT validation pid 3917990, 13224 MiB (not external) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | absent (no compute process on GPU 6) |
| 17:13:35Z | ours: VT validation pid 3917990, 23950 MiB (not external) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | absent (no compute process on GPU 6) |
| 17:17:28Z | ours: VT validation pid 3917990 (not external) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | absent (no compute process on GPU 6) |
| 17:26:45Z | ours: VT validation pid 3917990, 40540 MiB (not external) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | absent (no compute process on GPU 6) |
| 17:36:18Z | ours: VT validation pid 3917990, 40540 MiB (not external) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | absent (no compute process on GPU 6) |
| 17:53:47Z | ours: VT validation pid 3917990, 40540 MiB (not external) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | ours: resume test worker pid 109474, 1492 MiB (lead QM RS; not external) | absent (no compute process on GPU 6) |
| 17:59:02Z | ours: VT validation pid 3917990, 40540 MiB (not external) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle again; the resume test ended 17:56:58Z) | GPU 6 (not ours): verifier pid 126361, 794 MiB (first seen 17:56:51Z) |
| 18:14:23Z | ours: VT validation pid 3917990, 40540 MiB (not external) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | GPU 6 (not ours): verifier source_R3_002 pid 126361, 794 MiB (released run, launched 17:55:00Z per lead QO) |
| 18:25:03Z | ours: VT validation pid 3917990, 40540 MiB (not external) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | GPU 6 (not ours): verifier source_R3_002 pid 126361, 794 MiB |
| 18:33:30Z | ours: VT validation pid 3917990, 40540 MiB (not external) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | GPU 6 (not ours): verifier source_R3_002 pid 126361, 794 MiB |
| 18:46:09Z | absent (GPU 0 idle; the VT exited 18:42:07Z) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | GPU 6 (not ours): verifier source_R3_002 pid 126361, 794 MiB |
| 18:55:42Z | EXTERNAL: pid 810357 <other project>, 858 MiB (another project's test job; also on GPUs 2 and 3 at 514 MiB each; GPU 0 ours and idle; first sighting; not touched) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | GPU 6 (not ours): verifier source_R3_002 pid 126361, 808 MiB; GPUs 2 and 3 (not ours): the same nn_tests_suite pid 810357 |
| 18:56:10Z | EXTERNAL: pid 810357 nn_tests_suite still present (process elapsed 7 min 16 s at this sample) | absent (R4 perturbed) | absent (R4 control) | absent (GPU 5 idle) | GPUs 2, 3 (not ours): nn_tests_suite pid 810357; GPU 6: verifier pid 126361 |
| 19:04:47Z | absent (GPU 0 idle; the external nn_tests_suite pid 810357 is gone: sightings 18:55:42Z to 18:56:10Z) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | absent (GPUs 2, 3 and 6 empty at this sample) |
| 19:13:48Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | absent (GPUs 2, 3, 6 empty) |
| 19:34:46Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094, 43678 MiB) | absent (R4 control pid 3181582, 43678 MiB) | absent (GPU 5 idle) | absent (GPUs 2, 3, 6, 7 empty; shift 15 first sample) |
| 19:48:28Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094, 43678 MiB; util 95 per cent) | absent (R4 control pid 3181582, 43678 MiB; util 100 per cent) | absent (GPU 5 idle) | absent (GPUs 2, 3, 6, 7 empty) |
| 19:51:01Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094, 43678 MiB) | absent (R4 control pid 3181582, 43678 MiB) | absent (GPU 5 idle) | absent (GPUs 2, 3, 6, 7 empty) |
| 19:54:19Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094, 43678 MiB) | absent (R4 control pid 3181582, 43678 MiB) | absent (GPU 5 idle) | absent (GPUs 2, 3, 6, 7 empty) |
| 19:57:02Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094, 43678 MiB) | absent (R4 control pid 3181582, 43678 MiB) | absent (GPU 5 idle) | absent (GPUs 2, 3, 6, 7 empty) |
| 20:00:15Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094, 43678 MiB; util 100 per cent) | absent (R4 control pid 3181582, 43678 MiB; util 100 per cent) | absent (GPU 5 idle) | absent (GPUs 2, 3, 6, 7 empty) |
| 20:06:04Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094, 43678 MiB) | absent (R4 control pid 3181582, 43678 MiB) | absent (GPU 5 idle) | GPU 6 (not ours): verifier lane pid 2208009 (<independent-route directory>/independent/.venv python), 794 MiB, started about 20:04:39Z (elapsed 85 s at the sample); GPUs 2, 3, 7 empty |
| 20:12:19Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094, 43678 MiB) | absent (R4 control pid 3181582, 43678 MiB) | absent (GPU 5 idle) | GPU 6 (not ours): verifier lane pid 2208009, 794 MiB (lead RE: source_R4_001 released); GPUs 2, 3, 7 empty |
| 20:14:25Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094, 43678 MiB) | absent (R4 control pid 3181582, 43678 MiB) | absent (GPU 5 idle) | GPU 6 (not ours): verifier lane pid 2208009, 794 MiB; GPUs 2, 3, 7 empty; <shared volume> free 279663280128 bytes |
| 20:15:21Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | absent (GPU 5 idle) | GPU 6 (not ours): verifier pid 2208009; <shared volume> free 278754566144 bytes |
| 20:18:45Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094, 43678 MiB) | absent (R4 control pid 3181582, 43678 MiB) | absent (GPU 5 idle) | GPU 6 (not ours): verifier pid 2208009, 794 MiB; GPUs 2, 3, 7 empty; <shared volume> free 274626035712 bytes (20.2 MB/s since 20:15:21Z) |
| 20:24:56Z to 20:35:04Z (60 s samples, runs/_logs/shift15/disk_gpu_poll.log) | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094, 43678 MiB) | absent (R4 control pid 3181582, 43678 MiB) | absent (GPU 5 idle) | GPU 6 (not ours): verifier pid 2208009, 794 MiB; GPUs 2, 3, 7 empty; <shared volume> free 268500824064 -> 260374695936 bytes (12.6 MB/s average, 4.3 MB/s over the last minute) |
| 20:35:31Z to 21:10:42Z (60 s samples, runs/_logs/shift15/disk_gpu_poll.log) | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094, 43678 MiB) | absent (R4 control pid 3181582, 43678 MiB) | absent (GPU 5 idle) | GPU 6 (not ours): verifier pid 2208009, 794 MiB; GPUs 2, 3, 7 empty; <shared volume> free 260254412800 -> 239951642624 bytes (9.6 MB/s average; 4 MB/s over 21:02Z to 21:10Z) |
| 22:14:49Z to 22:43:46Z (60 s samples, poll log) | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094, 43678 MiB) | absent (R4 control pid 3181582, 43678 MiB) | absent (GPU 5 idle) | GPU 6 (not ours): verifier pid 2208009, 794 to 808 MiB; <shared volume> free 236168028160 -> 226156494848 bytes (about 5.8 MB/s) |
| 22:44:46Z to 22:48:04Z | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | EXTERNAL: pid 1733245 python3.12 census.py --tag eager-bitexact (another project, nice 10), 1046 to 1391 MiB, from about 22:46:33Z (elapsed 91 s at 22:48:04Z); GPU 5 ours and idle; not touched | GPUs 3 and 7 (not ours): the same project pids 1733247 and 1733240 (census.py eager-tritonmm-real, eager-real), 1382 MiB each; earlier pids 1679121 (22:44:46Z, 1046 MiB) and 1673575 (22:45:47Z, 642 MiB) on GPUs 2, 3 or 7, gone by 22:46:47Z; GPU 6: verifier pid 2208009, 808 MiB |
| 22:48:36Z to 22:56:38Z (60 s samples, poll log) | EXTERNAL: pid 1771519 (another project), 2242 to 3254 MiB, 22:49:36Z to 22:51:37Z, gone by 22:52:37Z; GPU 0 ours and idle; not touched | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | EXTERNAL: pid 1733245 census.py to 22:50:37Z, then pid 1812688 (same project) 1382 to 1386 MiB from 22:53:37Z; GPU 5 ours and idle; not touched | GPUs 3 and 7 (not ours): pids 1733247, 1733240, then 1812686; GPU 6: verifier pid 2208009, 808 MiB; <shared volume> free 224920797184 -> 221864361984 bytes |
| 22:57:13Z to 23:05:14Z (60 s samples, poll log) | EXTERNAL: pids 1937762 (3372 MiB, 23:03:14Z) and 1948149 (3268 MiB, 23:04:14Z), another project's short census.py-type jobs, gone by 23:05:14Z; GPU 0 ours and idle; not touched | absent (R4 perturbed pid 3251094) | absent (R4 control pid 3181582) | EXTERNAL: pid 1812688 census.py to 22:59:13Z, gone by 23:00:13Z; GPU 5 ours and idle | GPU 7 (not ours): pids 1812686, 1864291, 1919368; GPU 6: verifier pid 2208009, 808 MiB; <shared volume> free 221731692544 -> 218682089472 bytes (about 6 MB/s) |
| 23:05:44Z to 23:22:18Z (60 s samples, poll log) | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094, 43678 MiB) | absent (R4 control pid 3181582; 6528 to 7748 MiB in the battery since 23:06:13Z) | absent (GPU 5 idle) | GPU 6: verifier pid 2208009 (808 MiB) until 23:20:17Z, gone at 23:21:18Z; GPUs 2, 3, 7 empty; <shared volume> free 218576048128 -> 214345371648 bytes |
| 23:23:35Z to 23:59:31Z (60 s samples, poll log) | absent (GPU 0 idle) | absent (R4 perturbed pid 3251094; 6.5 to 11.0 GB in the battery since 23:28:32Z) | absent (R4 control pid 3181582; 7.7 to 11.3 GB in the battery) | absent (GPU 5 idle) | GPUs 2, 3, 6 empty; GPU 7 (not ours): pid 2507284, 1384 MiB, from 23:59:31Z; <shared volume> free 214061449216 -> 207070453760 bytes (about 3 MB/s) |
