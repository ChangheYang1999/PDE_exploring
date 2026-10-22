"""Small independent parser diagnostics and actual missing-full-dependency gate."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import importlib.util,io,struct,json,subprocess,sys,hashlib,os
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1];E=D/'evidence';p=D/'code/check.py'
spec=importlib.util.spec_from_file_location('independent_linkage_reader',p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
def header(h,ver=1):
 raw=(repr(h)+'\n').encode('ascii');return b'\x93NUMPY'+bytes([ver,0])+len(raw).to_bytes(2 if ver==1 else 4,'little')+raw
good={'descr':'<f8','fortran_order':False,'shape':(2,3)};passed=0
for v in [1,2,3]:assert m.npy_header(io.BytesIO(header(good,v)))==(2,3);passed+=1
bad=[b'notNPY',header(good)[:-1],header(good).replace(b'\x01\x00',b'\x04\x00',1)]
for key,value in [('descr','>f8'),('descr','<f4'),('fortran_order',True),('shape',(2,0)),('shape',(True,3)),('shape',[2,3])]:
 h=dict(good);h[key]=value;bad.append(header(h))
for b in bad:
 try:m.npy_header(io.BytesIO(b))
 except (ValueError,AssertionError):passed+=1
 else:raise AssertionError('invalid header accepted')
for v in [0.0,-0.0,1.0,-1.0,2.0**-1074,-2.0**-1074,1.0+2.0**-52,2.0**1023]:
 q=F(*v.as_integer_ratio());assert m.ieee(struct.pack('<d',v))==q;passed+=1
for v in [float('inf'),float('-inf'),float('nan')]:
 try:m.ieee(struct.pack('<d',v))
 except ValueError:passed+=1
 else:raise AssertionError('nonfinite scalar accepted')
# This preflight is intentionally made before a full radial verdict exists.
assert not (B/'research/radial_tm_refined/evidence/verdict.json').exists()
assert not (E/'full_checks.json').exists()
proc=subprocess.run([sys.executable,str(p)],cwd=B,capture_output=True,text=True,timeout=45,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1'})
assert proc.returncode!=0 and 'FileNotFoundError' in proc.stderr and 'radial_tm_refined/evidence/verdict.json' in proc.stderr
assert not (E/'full_checks.json').exists();(E/'full_gate_rejection.log').write_text(proc.stdout+proc.stderr)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_PARSER_AND_MISSING_FULL_VERDICT_GATE','parser_cases':passed,'valid_headers':3,'rejected_headers':len(bad),'exact_binary64_values':8,'rejected_nonfinite_scalars':3,'actual_missing_full_verdict_rejected':True,'full_artifact_absent':True,'files':{str(q.relative_to(B)):sha(q) for q in [p,Path(__file__),E/'full_gate_rejection.log']}}
with (E/'parser_checks.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps(out),flush=True)
