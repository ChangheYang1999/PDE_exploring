from pathlib import Path
import time,subprocess,sys,json
while True:
 try:
  if Path('/proc/3910288/stat').read_text().split()[2]=='Z':break
 except FileNotFoundError:break
 time.sleep(2)
with open('logs/tuned_radius_certificate.log','w') as out:
 result=subprocess.run([sys.executable,'-u','code/tuned_radius_certificate.py'],stdout=out,stderr=subprocess.STDOUT,timeout=500)
print(json.dumps({'step':'tuned_radius_certificate','returncode':result.returncode}),flush=True)
