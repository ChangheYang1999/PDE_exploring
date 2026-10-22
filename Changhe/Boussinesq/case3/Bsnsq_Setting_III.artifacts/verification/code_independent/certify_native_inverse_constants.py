"""Apply packet111 exact JSON certificates to a new immutable native manifest."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import sys,time,json,hashlib,subprocess
from higher_inverse_constant import export,evaluate
root=Path(sys.argv[1]);target=root/'inverse_constant_certificates';target.mkdir(exist_ok=True);start=time.monotonic();rows=[]
for state in json.loads((root/'manifest.json').read_text())['states']:
 archive=root/state['snapshot'];assert hashlib.sha256(archive.read_bytes()).hexdigest()==state['sha256'];label=state['label']
 inp=target/(label+'_input.json');cert=target/(label+'_certificate.json');data=export(archive,inp);result=evaluate(data)
 cert.write_text(json.dumps({'created_utc':datetime.now(timezone.utc).isoformat(),'input_sha256':hashlib.sha256(inp.read_bytes()).hexdigest(),'result':result},indent=2)+'\n')
 lo,hi=map(Q,result['constant_C2']);D=1000;low=Q(lo.numerator*D//lo.denominator,D);high=-Q((-hi).numerator*D//(-hi).denominator,D)
 with (target/(label+'_check.log')).open('wb') as f:
  cp=subprocess.run([sys.executable,'code_independent/higher_inverse_constant.py',str(inp),str(cert),'--check'],stdout=f,stderr=subprocess.STDOUT,timeout=60)
 assert cp.returncode==0
 row={'label':label,'beta':data['beta'],'C2_enclosure':[str(low),str(high)],'C2_enclosure_float':[float(low),float(high)],'input':str(inp),'certificate':str(cert),'archive_sha256':data['archive_sha256'],'verdict':'CONFIRMED_NONZERO' if low*high>0 else 'OPEN'};rows.append(row);print(row,flush=True)
(target/'summary.json').write_text(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'rows':rows,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},indent=2)+'\n')
