# Lossless replay storage

Completed pool A JSONL replay files were compressed after their validation.
The original result JSON, source archives, hashes and conclusions are unchanged.
The manifest `bot_research/runs/validation/archived-poolA-replays-001.json`
records every original path and SHA256, its `.gz` path and compressed SHA256,
and a successful decompression hash check before the original was removed.
Readers that expect the original JSONL path require restoration first.

From the project root, restore one file as follows, replacing the replay path
with an `original_path` listed in the manifest:

```sh
PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1 \
  nice -n 19 taskset -c 29 .venv/bin/python -B \
  -m bot_research.experiments.validation.restore_archived_replay \
  --replay bot_research/runs/validation/final-best-v9a-poolA-001/replays/one_round_factory_prefix-07-side0.jsonl
```

The tool verifies both hashes and refuses to overwrite a file. The restored
file is byte identical to the original. Recompress or remove restored duplicates
after use to stay within the lane's storage budget. This storage operation adds
no independent game or statistical evidence.

## Later completed development archives

The same restore command accepts `--manifest` for later archive batches. Each
manifest records the original and compressed hashes, sizes, and successful
round-trip verification. No result row or source archive was removed.

| Manifest in `bot_research/runs/validation/` | Files | Bytes saved | Archive completion, UTC |
| --- | ---: | ---: | --- |
| `archived-wave2-replays-001.json` | 30 | 23369146 | 2026-10-31T15:10:34.820833+00:00 |
| `archived-wave3-replays-001.json` | 307 | 212490041 | 2026-10-31T15:11:09.033266+00:00 |
| `archived-wave4-replays-001.json` | 156 | 170450061 | 2026-10-31T16:18:26.512208+00:00 |
| `archived-wave5-replays-001.json` | 284 | 84605958 | 2026-10-31T16:39:48.358183+00:00 |

| `archived-wave6-replays-001.json` | 640 | 95458511 | 2026-10-31T16:55:50.363193+00:00 |

The newest batch archived 640 completed development replays.
Its per-file journal was flushed before each original was removed. Pool C
replays remain uncompressed and its final audits are complete.

## 2026-10-31T17:29:31.200814+00:00: Historical replay wave 7

Losslessly compressed 312 completed route-challenge, projection-selector and early-guard replay logs. Saved 178791005 bytes. Every gzip round-trip was checked against its original SHA256 before removing the raw copy, with a flushed journal receipt. The final pool-C and current campaign logs remain raw. Restore exact original paths with restore_archived_replay using runs/validation/archived-wave7-replays-001.json before running old path-based readers. Results and source archives are unchanged.

## 2026-10-31T17:54:48.802859+00:00: Wave 8

Losslessly compressed 650 completed historical replay files, saving 247297273 bytes in 5.254348 seconds. Receipt: `bot_research/runs/validation/archived-wave8-replays-001.json`. Every compressed file was decompressed and SHA-256 checked before its raw copy was removed; the fsynced journal preserves per-file evidence. No current early-wall, bait/guard or reserved-pool replay was archived. Use `bot_research.experiments.validation.restore_archived_replay` with the receipt and original replay path before a reader that requires raw JSONL.
