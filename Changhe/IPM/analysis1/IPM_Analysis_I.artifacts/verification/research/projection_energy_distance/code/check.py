"""Only arithmetic and schema of frozen floating projection experiments."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from collections import Counter
import json,hashlib,zipfile,struct,ast,sys
import numpy as np
from flint import arb,fmpq,ctx
from mpmath import iv
assert not sys.flags.optimize
ctx.prec=256;ctx.threads=1;iv.dps=80
B=Path(__file__).resolve().parents[3];D=B/'research/projection_energy_distance';E=D/'evidence';S=D/'source'
now=lambda:datetime.now(timezone.utc).isoformat()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
load=lambda p:json.loads(p.read_text())
counts=Counter();pins={};start=now()
for n,item in load(E/'source_snapshot.json')['files'].items():
 p=B/n;assert sha(p)==item['sha256'];pins[n]=item['sha256']
def ieee(blob):
 v=int.from_bytes(blob,'little');sgn=-1 if v>>63 else 1;ex=(v>>52)&2047;ma=v&((1<<52)-1);assert ex!=2047
 if ex:ma|=1<<52;pow2=ex-1023-52
 else:pow2=-1074
 return sgn*F(ma)*F(2)**pow2

def npy(blob):
 assert blob[:6]==b'\x93NUMPY'
 version=tuple(blob[6:8]);assert version in [(1,0),(2,0),(3,0)]
 hlen=int.from_bytes(blob[8:10] if version==(1,0) else blob[8:12],'little');off=10 if version==(1,0) else 12
 head=ast.literal_eval(blob[off:off+hlen].decode('latin1'));body=blob[off+hlen:]
 assert head['shape']==() and head['fortran_order'] is False
 desc=head['descr']
 if desc in ('<f8','=f8'):assert len(body)==8;return ieee(body)
 if desc in ('<i8','=i8'):assert len(body)==8;return int.from_bytes(body,'little',signed=True)
 if desc.startswith('<U'):assert len(body)==4*int(desc[2:]);return body.decode('utf-32-le').rstrip('\x00')
 raise AssertionError(desc)

def ar(q):return arb(fmpq(q.numerator,q.denominator))
def vi(q):return iv.mpf(q.numerator)/q.denominator
def ae(x):
 def ep(y):m,e=y.man_exp();return F(int(m))*F(2)**int(e)
 return ep(x.lower()),ep(x.upper())
def ve(x):
 def ep(y):s,m,e,_=y;return (-1 if s else 1)*F(int(m))*F(2)**int(e)
 return tuple(ep(y) for y in x._mpi_)
def pack(x):return {'lower_exact':str(x[0]),'upper_exact':str(x[1])}
results=[];legacy=[]
boxes={'Kproj2_M16_s16_NJ0.npz':('1.81764','1.81766'),'Kproj2_M16_s16_NJ1.npz':('1.81776','1.81779'),'Kproj2_M16_s16_NJ1_free.npz':('1.76198','1.76201')}
for p in sorted(S.glob('Kproj*.npz')):
 with np.load(p,allow_pickle=False) as npz,zipfile.ZipFile(p) as z:
  names={x.removesuffix('.npy') for x in z.namelist()};assert set(npz.files)==names
  fields={}
  for key in ['PK_norm2','K2_full','cos2_full','summary']+(['K2_gram','dist_rel','nF','nfun','n_kept','whitening_error','join_residual','cross_err','cross_err_cw'] if p.name.startswith('Kproj2_') else ['cos2_low']):
   direct=npy(z.read(key+'.npy'));value=npz[key].item();exact=value if isinstance(value,(int,str)) else F(value)
   assert exact==direct,(p.name,key);fields[key]=direct;counts['independent_manual_NPY_scalar_equalities']+=1
  if not p.name.startswith('Kproj2_'):
   ratio=fields['PK_norm2']/fields['K2_full'];assert ratio>1 and fields['cos2_full']>1
   legacy.append({'file':p.name,'ratio_exact':str(ratio),'saved_cos2_exact':str(fields['cos2_full']),'scope':'cannot be exact full-K orthogonal energy ratio in one norm'});counts['legacy_full_ratio_over_one']+=1
   continue
  assert fields['K2_full']==fields['K2_gram'] and fields['nfun']==1953
  assert fields['nF']==1953+2+(16 if 'free' in p.name else 0) and 'cos2_low' not in names
  summary=json.loads(fields['summary']);assert F(summary['thresh']['PK_norm2'])==fields['PK_norm2'] and summary['thresh']['n_kept']==fields['n_kept']
  for cut,row in summary.items():
   pk=F(row['PK_norm2']);k=fields['K2_gram'];assert 0<pk<k
   q=(k-pk)/k;ab=ae((1-ar(pk)/ar(k)).sqrt());vb=ve(iv.sqrt((vi(k)-vi(pk))/vi(k)))
   assert ab[0]>0 and vb[0]>0 and max(ab[0],vb[0])<=min(ab[1],vb[1])
   assert ab[0]**2<=q<=ab[1]**2 and vb[0]**2<=q<=vb[1]**2
   for key,val in [('dist_rel',row['dist_rel']),('cos2',row['cos2'])]:
    assert np.isfinite(val)
    if key=='dist_rel':assert abs(F(val)**2-q)<F(1,10**16)
    else:assert abs(F(val)-pk/k)<F(1,10**15)
   if cut=='thresh':
    lo,hi=map(F,boxes[p.name]);assert lo<100*ab[0]<=100*ab[1]<hi and lo<100*vb[0]<=100*vb[1]<hi
   results.append({'file':p.name,'cut':cut,'retained':row['n_kept'],'missing_energy_exact':str(q),'distance_arb256':pack(ab),'distance_iv80':pack(vb),'percent_interval':list(boxes[p.name]) if cut=='thresh' else None})
   counts['two_engine_positive_distance_comparisons']+=1
  counts['version2_schema_checks']+=1

# Exact logical counterexample to the old 99.5percent-energy phrasing.
q=F(1,200);assert F(707,10000)**2<q<F(708,10000)**2
assert (1-F(1,200)**2)==F('0.999975') and F('0.999975')!=F('0.995')
counts['exact_energy_distance_identity_examples']=2
# Read the frozen source AST; do not import or execute it.
tree=ast.parse((S/'c2_Kproj.py').read_text());fun={n.name:n for n in tree.body if isinstance(n,ast.FunctionDef)}
def subs(node):
 return [n.slice.value for n in ast.walk(node) if isinstance(n,ast.Subscript) and isinstance(n.value,ast.Name) and n.value.id=='P' and isinstance(n.slice,ast.Constant)]
assert 'cos2_low' not in subs(fun['main_B']) and 'cos2_full' in subs(fun['main_B']) and 'dist_rel' in subs(fun['main_B'])
saves=[n for n in ast.walk(fun['main_A']) if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and isinstance(n.func.value,ast.Name) and n.func.value.id=='np' and n.func.attr=='savez']
assert len(saves)==1;written={k.arg for k in saves[0].keywords};assert 'cos2_full' in written and 'dist_rel' in written and 'cos2_low' not in written
counts['repaired_current_A_B_scalar_schema_compatible']=1
for p in sorted(S.glob('KprojB*.json')):
 j=load(p);assert Path(j['proj']).name.startswith('Kproj_') and not Path(j['proj']).name.startswith('Kproj2_');assert (S/Path(j['proj']).name).exists()
 with np.load(S/Path(j['proj']).name,allow_pickle=False) as z:assert F(j['cos2'])==F(z['cos2_full'].item())
 counts['old_B_outputs_bound_to_old_projection']=1+counts['old_B_outputs_bound_to_old_projection']
for p in [D/'PROOF.md',D/'ADDENDUM.md',E/'proof_first.json',E/'source_snapshot.json',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
out={'start_utc':start,'utc':now(),'status':'PASS_SAVED_PROJECTION_SCALARS_WITH_REFUTED_OLD_NORM_INTERPRETATION','counts':dict(counts),'new_distance_diagnostics':results,'old_inconsistent_full_ratios':legacy,'scope':'Exact artifact scalars only. Hilbert projection identity proved separately. Floating Gram, cross block, physical projection, image and tails not certified.','files':pins}
with (E/'checks.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({k:out[k] for k in ['utc','status','counts']}))
