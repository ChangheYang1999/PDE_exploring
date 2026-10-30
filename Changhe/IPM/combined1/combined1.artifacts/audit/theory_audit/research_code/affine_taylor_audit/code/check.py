"""Exact candidate binding for the nonlinear versus affine Taylor distinction."""
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
from datetime import datetime,timezone
import importlib.util,json,time,sys
sys.set_int_max_str_digits(0)
from flint import arb,ctx
start=time.monotonic();ctx.prec=256
base=Path(__file__).resolve().parents[1];root=base.parents[1]
jpath=root/'research/taylor_projection/code/jets.py'
spec=importlib.util.spec_from_file_location('jets',jpath);J=importlib.util.module_from_spec(spec);spec.loader.exec_module(J)
rawpath=root/'research/taylor_projection/source/canonical007.json'
parpath=root/'research/taylor_projection/verification/parameters.json'
raw=json.loads(rawpath.read_text());par=json.loads(parpath.read_text())
H=lambda p:sha256(Path(p).read_bytes()).hexdigest()
assert par['source_canonical_sha256']==H(rawpath)
phi=J.add(*(J.scale(J.canonical_jet(*idx),Q(v)) for idx,v in zip(raw['order'],raw['coefficients']) if idx[2]<=4))
eta=J.add(*(J.scale(J.canonical_jet(*x['index']),Q(x['coefficient'])) for x in par['canonical_changes'] if x['index'][2]<=4))
ts={tuple(x['pair']):Q(x['coefficient']) for x in par['parameters']};alpha,beta=ts[2,1],ts[0,3]
assert alpha!=0
expected={(2,0):192*alpha**2,(1,1):8640*alpha*beta}
expected={k:v for k,v in expected.items() if v}
aff=J.add(J.residual(phi),J.linear(phi,eta));actual=J.residual(J.add(phi,eta))
assert actual=={} and aff==expected
ball=lambda x:(arb(x.numerator)/arb(x.denominator)).str(65)
out={'utc':datetime.now(timezone.utc).isoformat(),'input_sha256':{str(p.relative_to(root)):H(p) for p in [rawpath,parpath,jpath]},'proof_sha256':H(base/'PROOF.md'),'code_sha256':H(__file__),'alpha_nonzero':True,'alpha_ball':ball(alpha),'nonlinear_five_coefficients_exactly_zero':True,'affine_defect_exact':[{'index':list(k),'coefficient':str(v),'ball':ball(v)} for k,v in sorted(aff.items())],'identity_all_coefficients':True,'elapsed_seconds':time.monotonic()-start,'verdict':'REFUTED: exact nonlinear repair is not a solution of the affine linearized Taylor equation for007'}
with (base/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(out['utc'],out['verdict'],out['elapsed_seconds']);print('alpha',out['alpha_ball']);print('affine defects',[(x['index'],x['ball']) for x in out['affine_defect_exact']])
