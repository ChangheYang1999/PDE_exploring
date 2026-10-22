"""Lightweight exact provenance/cover audit and interval-dispatch checks."""
import os
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,hashlib,inspect,bisect
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import mpmath,flint
from mpmath import iv
from mpmath.libmp import libmpi
from flint import arb,acb,ctx
BASE=Path(__file__).resolve().parents[3];E=BASE/'research/axis_points/evidence';ctx.prec=384;iv.dps=65
sys.path.insert(0,str(BASE/'research/canonical_inverse/code'))
import exact_audit

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def q(v):v=F(v);return iv.mpf(v.numerator)/v.denominator
def iq(a,b):return iv.mpf([q(a).a,q(b).b])
def aa(v):v=F(v);return arb(v.numerator)/v.denominator
def fd(v):m,e=v.man_exp();return F(int(m))*F(2)**int(e)
def fi(t):sign,m,e,bc=t;return (-1 if sign else 1)*F(int(m))*F(2)**int(e)
def compare(box,point):
 for I,B in ((box.real,point.real),(box.imag,point.imag)):
  lo,hi=map(fi,I._mpi_);m,r=fd(B.mid()),fd(B.rad());assert lo<=m-r and m+r<=hi,(str(I),str(B))
# Direct dispatch and defining formulas are captured from the executing installation.
assert 'mpci_pow' in inspect.getsource(mpmath.ctx_iv)
assert 'return mpci_exp(mpci_mul(y, mpci_log(x, wp), wp), prec)' in inspect.getsource(libmpi.mpci_pow)
assert 'mpi_atan2' in inspect.getsource(libmpi.mpci_arg)
assert 'round_floor' in inspect.getsource(libmpi.mpi_atan2) and 'round_ceiling' in inspect.getsource(libmpi.mpi_atan2)
libpaths=[Path(inspect.getsourcefile(libmpi)),Path(inspect.getsourcefile(mpmath.ctx_iv))]
librecords=[]
for p in libpaths:
 target=E/('library_'+p.name);target.write_bytes(p.read_bytes());librecords.append({'installed_path':str(p),'snapshot':str(target.relative_to(BASE)),'sha256':sha(p)})
# These finite checks supplement source/primitive contracts. They are not a proof of the library.
checks=0
boxes=[('1e-16','2e-16','-1e-17','1e-17'),('.1','.2','-.03','.03'),('.9','1.1','-.2','.2'),('1','2','3','4'),('1e-8','2e-8','-.1','.1')]
for sa,sb,sc,sd in boxes:
 a,b,c,d=map(F,(sa,sb,sc,sd));Z=iv.mpc(iq(a,b),iq(c,d));exponent=iq(F('2.431'),F('2.432'));P=Z**exponent
 for x in (a,(a+b)/2,b):
  for y in (c,(c+d)/2,d):
   z=acb(aa(x),aa(y))
   for p in (F('2.431'),F('2.432')):compare(P,z.pow(acb(aa(p)),analytic=True));checks+=1
   compare(iv.sin(Z),z.sin());compare(iv.cos(Z),z.cos());checks+=2
raw=json.loads((BASE/'data_exact/x3.json').read_text());knots=[F.from_float(float.fromhex(v)) for v in raw['spline_knots_hex']]
assert sha(BASE/'research/canonical_inverse/code/exact_audit.py')=='331771590a0dd764208306640b4b3af63aec8cfe966ed6a0d086ec512d617b42'
# The Cox factors are x+(mid-t_i), and (t_j-mid)-x, proving the physical centered variable.
coxs=inspect.getsource(exact_audit.exact_poly);assert 'fq(mid-d.t[i]),1' in coxs and 'fq(d.t[i+degree+1]-mid),-1' in coxs
expected={
 'axis7':{'partition':'27a7b70670fa14d74748d7fd83048c0d736208cfd1e04f449063035fb573ff86','log':'0ed3a36cc6ff5a939c62cf2de5985a0119b4b29d7bbe502a8222798d65111ed3','result':'cec34ae87e3634b6bc8d2dc52cba99adc12496ecc2e84cd0d2379cc26b92b6f5','source':'849f35aa2b1e1034b70a79bacca1be977e58833e0f1e08681e7097ab88115f4c'},
 'axis10':{'partition':'ce6d09b48c7de1e6407d6285f779a9af0b0e6fde05dd751a55bba049e1007402','log':'40d2dfcd1ce26fff09597d139c444d87f600cdc3df8583c9e7a4b65aaa33030b','result':'32a2159ed5432aabf4f4c17d1beccdf4589dbdca360fd26c666391fde4fb2dd8','source':'ffcb8d6c7e008316616b7578f94d1b2680fff036f6b20b8170ea76f3e022272e'}}
cover=json.loads((E/'rule_cover_audit.json').read_text());complex_result=json.loads((E/'complex_iv_audit.json').read_text());downstream=json.loads((E/'final_iv_audit.json').read_text())
assert complex_result['source_sha256']==sha(BASE/'research/axis_points/code/audit_complex_iv.py')
records=[]
for tag,hs in expected.items():
 pp=E/(tag+'_partition.json');lp=E/(tag+'_run.log');rp=E/(tag+'_result.json')
 assert sha(pp)==hs['partition'] and sha(lp)==hs['log'] and sha(rp)==hs['result']
 part=json.loads(pp.read_text());res=json.loads(rp.read_text());qs=[tuple(map(F,v)) for v in part['q']];ts=[tuple(map(F,v)) for v in part['theta_over_pi_half']]
 assert part['script_sha256']==hs['source'] and res['partition_sha256']==hs['partition'] and part['settings']==res['settings']
 source=BASE/'research/axis_points/code'/('axis_arb_v2_archived.py' if tag=='axis7' else 'axis_arb.py');assert sha(source)==hs['source']
 assert part['dependency_sha256']==sha(BASE/'research/canonical_inverse/code/strain_arb.py')=='923db118bcc6f95039cba684100b8cd7ec39ae39f18e05343290b6e3ab494f0e'
 assert part['input_sha256']==sha(BASE/'data_exact/x3.json')=='1a8decfb0beb666a36bc14f08514d25b371b778872bdf13d5801c2a4c40b7946'
 cap=F(part['cap_q']);hole=tuple(map(F,part['removed_q_strip']));pieces=sorted(qs+[(F(0),cap),hole,(1-cap,F(1))])
 assert pieces[0][0]==0 and pieces[-1][1]==1
 assert all(a<b for a,b in pieces) and all(a[1]==b[0] for a,b in zip(pieces,pieces[1:]))
 assert ts[0][0]==0 and ts[-1][1]==1-F(part['cap_theta_normalized']) and all(a<b for a,b in ts)
 assert all(a[1]==b[0] for a,b in zip(ts,ts[1:]))
 for a,b in qs:
  sp=bisect.bisect_right(knots,(a+b)/2)-1;assert knots[sp]<=a<b<=knots[sp+1]
 entries=[]
 for line in lp.read_text().splitlines():
  try:entries.append(json.loads(line))
  except json.JSONDecodeError:pass
 initial=[v for v in entries if v.get('stage')=='start'][0];prepared=[v for v in entries if v.get('stage')=='prepared'][0];last=[v for v in entries if v.get('stage')=='quadrature'][-1]
 assert initial['settings']==part['settings'] and initial['input_sha256']==part['input_sha256']
 assert prepared['radial_cells']==len(qs) and prepared['angular_cells']==len(ts) and last['done']==last['total']==len(qs)
 for table in (cover['partition_checks'],complex_result['points'],downstream['points']):
  row=[v for v in table if v['tag']==tag];assert len(row)==1 and row[0]['partition_sha256']==hs['partition']
 records.append({'tag':tag,'hashes':hs,'cover':'EXACT_RATIONAL_TILING','physical_Cox_variable_and_span':'CONFIRMED','run_settings_counts_and_immutable_hashes':'CONFIRMED','real_quadrature_count':len(qs)*len(ts)*28*32})
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','source_sha256':sha(__file__),'mpmath_version':mpmath.__version__,'python_flint_version':flint.__version__,'FLINT_version':flint.__FLINT_VERSION__,'installed_library_source':librecords,'complex_interval_corner_comparisons_to_384_bit_Acb':checks,'library_trust_scope':'Complex operations explicitly dispatch to interval libmpi formulas and directed real primitives, not scalar fallback. Analytic right-half-plane log branch is checked by the main computation. Supplementary finite comparisons do not formally verify the libraries. As with Arb, the documented elementary outward arithmetic primitives are trusted.','complex_audit_sha256':sha(E/'complex_iv_audit.json'),'complex_source_sha256':complex_result['source_sha256'],'records':records}
(E/'library_provenance_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
