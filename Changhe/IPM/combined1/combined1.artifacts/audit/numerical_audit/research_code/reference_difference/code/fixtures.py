"""Closed Euler moment calibration of the full density-difference procedure."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,sys,time
from flint import fmpq as Q,fmpq_poly as Poly,arb,ctx
sys.path.insert(0,str(Path(__file__).resolve().parent));import check as C
R=C.ROOT;B=C.B;ctx.prec=1536
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def main():
 start=time.monotonic();output=B/'verification/fixtures.json';assert not output.exists();c=Q(4076476460239181,2251799813685248);delta=1-1/c;p=2-5*delta/2;empty={'cl_exact':str(c),'generators':[]};raw={'cl_exact':str(c),'generators':[{'j':4,'m':0,'spec':['mono',0],'coef':'1'}]};checks={}
 diff,prefix=C.difference(empty,raw);checks['all_four_prefixes']=all(x['equal'] for x in prefix);zero,zprefix=C.difference(raw,raw);checks['zero_generator_difference']=not zero['generators'];model,fields,endpoints=C.compact_fields(diff)
 expected=-8*p*(p-1)*(2+(p-2)*C.T);checks['closed_density']=set(fields['rho'])=={(5,'s',1)} and fields['rho'][5,'s',1]==C.Rat(expected);points=C.point_checks(diff,fields,delta);checks['all_nine_cartesian_points']=points['value_count']==9 and points['minimum_accuracy_bits']>1000
 norm=C.norm(fields['rho'],delta);Pv=C.V*expected(C.V)**2;b=5*delta-3;exact=sum((q/(b+j+1) for j,q in enumerate(Pv)),Q(0));square=arb.pi()/2*C.ar(exact);checks['closed_full_square']=square.overlaps(arb(norm['square_ball'])) and square>0 and norm['group_count']==1 and norm['ordered_pairs']==1;checks['outward_tau']=square.sqrt()<C.ar(Q(norm['tau_upper_exact']));checks['delta_range']=Q(2,5)<delta<Q(1,2)
 # A q=1 scaled perturbation has no potential leading coefficient at all.
 scaled={'cl_exact':str(c),'generators':[{'j':0,'m':2,'spec':['legqs',1,2,1,25],'coef':'3/7'}]};sdiff,sprefix=C.difference(empty,scaled);sm,sf,se=C.compact_fields(sdiff);checks['scaled_prefix_and_endpoint']=all(row['equal'] for row in sprefix) and len(se)>0 and all(row['value']=='0' for row in se);spoints=C.point_checks(sdiff,sf,delta);checks['scaled_cartesian_points']=spoints['value_count']==9 and spoints['minimum_accuracy_bits']>1000
 zmodel,zfields,zendpoints=C.compact_fields(zero);znorm=C.norm(zfields['rho'],delta);checks['exact_zero_norm']=znorm['exact_zero'] and znorm['square_ball']=='0' and znorm['tau_upper_exact']=='0';assert all(checks.values()),checks
 paths=[B/'PROOF.md',Path(__file__),B/'code/check.py',R/'research/joint_scaled_factored_weak/code/fields_joint.py',R/'research/joint_scaled_factored_weak/PROOF.md',R/'research/multiscale_generators/code/cartesian.py',R/'research/multiscale_generators/PROOF.md',R/'research/rational_pole_moments/code/moments.py',R/'research/rational_pole_moments/PROOF.md']
 data={'utc':datetime.now(timezone.utc).isoformat(),'checks':checks,'check_count':len(checks),'inputs':{str(p.relative_to(R)):sha(p) for p in paths},'delta':str(delta),'exact_closed_radial_square_without_pi_over_two':str(exact),'closed_square_ball':square.str(100),'unscaled_fixture':diff,'unscaled_norm':norm,'unscaled_points':points,'scaled_fixture':sdiff,'scaled_endpoint_checks':se,'scaled_points':spoints,'zero_norm':znorm,'status':'CONFIRMED finite exact field, endpoint, canonical-tail hypotheses and closed density norm fixtures; actual candidate differences OPEN','elapsed_seconds':time.monotonic()-start}
 with output.open('x') as f:json.dump(data,f,indent=2);f.write('\n')
 print('FIXTURES_PASS',len(checks),sha(output),data['utc'],'seconds',data['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
