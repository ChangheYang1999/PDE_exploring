"""Continue the single CPU18 queue after the edge3 audit."""
from pathlib import Path
from datetime import datetime, timezone
import json, subprocess, sys, time
while True:
    try:
        if Path('/proc/3684546/stat').read_text().split()[2] == 'Z':
            break
    except FileNotFoundError:
        break
    time.sleep(5)
print(json.dumps(dict(started_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'))), flush=True)
for tag, command, timeout in [
    ('edge_radius_approach', ['code/edge_radius_approach_check.py'], 480),
    ('edge_top_constant', ['code/edge_top_constant_check.py'], 580),
]:
    with open('logs/after_edge3_'+tag+'.log', 'w') as out:
        result = subprocess.run([sys.executable, '-u', *command], stdout=out,
                                stderr=subprocess.STDOUT, timeout=timeout)
    print(json.dumps(dict(step=tag,returncode=result.returncode)),flush=True)
    if result.returncode:
        raise SystemExit(result.returncode)
