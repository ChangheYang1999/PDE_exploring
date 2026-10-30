"""Independent exact margin and Arb endpoint-threshold checks for R1-038."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction
import json,time
from flint import fmpq as Q,arb,ctx
B=Path(__file__).resolve().parents[1]
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def q(s):
 f=Fraction(s);return Q(f.numerator,f.denominator)
def ar(a):
 a=Q(a);return arb(a.numerator)/arb(a.denominator)
def main():
 start=time.monotonic();ctx.prec=768
 manifest=json.loads((B/'data/manifest.json').read_text())
 assert sha(B/'PROOF.md')==manifest['proof_sha256']
 for name,h in manifest['source_files'].items():assert sha(B/name)==h,name
 assert sha(B/'data/parameters.json')==manifest['parameters_sha256']
 p=json.loads((B/'data/parameters.json').read_text());c=q(p['c']);delta=1-1/c;qq=1/c-4
 identities={'D_delta':1-c*(qq-delta)==5*c-1,'D_zero':1-c*qq==4*c,'fourth_nonintegrable':1-4*delta>-1,'fifth_integrable':1-5*delta<-1,'radial_descendants_integrable':1-delta-2<-1};assert all(identities.values())
 margins=[];mins=[]
 for row in p['screening_rows']:
  out=[]
  for ceiling,displayed in zip(p['ceilings'],row['displayed_margins'],strict=True):
   value=q(row['distance_floor'])-q(ceiling);assert value>0 and value>q(displayed),(row['candidate'],ceiling)
   out.append({'ceiling':ceiling,'margin_exact':str(value),'displayed':displayed,'strict_lower':True})
  margins.append({'candidate':row['candidate'],'margins':out});mins.append((q(out[-1]['margin_exact']),row['candidate']))
 smallest=min(mins);assert smallest[1]=='015' and q('7.75277e-4')<smallest[0]<q('7.75278e-4')
 beta_checks=[];CI=ar(c);D=ar(delta);qI=ar(qq);den=ar(5*c-1);Bup=ar(q(p['B_upper']));Glo=ar(q(p['G_lower']));Elo=ar(q(p['E_lower']));s=(-2*qI-2).sqrt()
 for i,b in enumerate(p['numerical_b_lower']):
  assert q(b)<=q(p['ceilings'][i]);bb=ar(q(b));R=(Bup/(bb*s))**(1/(-qI-1));Emax=den/Glo*R**D;EH=33919*Emax;ratio=Elo/Emax
  checks={'Rmax_upper':R<ar(q(p['Rmax_upper'][i])),'Emax_upper':Emax<ar(q(p['Emax_upper'][i])),'EHmax_upper':EH<ar(q(p['EHmax_upper'][i])),'ratio_lower':ratio>ar(q(p['E_ratio_lower'][i]))};assert all(checks.values()),(i,checks)
  beta_checks.append({'b_lower':b,'Rmax':R.str(100),'Emax':Emax.str(100),'EHmax':EH.str(100),'E_ratio':ratio.str(100),'checks':checks})
 rlo=(Elo*Glo/den)**(1/D);cap=Bup*rlo**(qI+1)/s;assert cap<ar(q('9.27595e-11')) and Bup/(2*arb.pi()).sqrt()<33919
 K=q('1/33917');assert K<q('2.9484e-5') and q('33917')/2==q('16958.5')
 # Exact generic translation examples include the equality boundary tau=d-b.
 # The theorem itself is the triangle-inequality proof, not these checks.
 monotonicity_checks=[]
 exponent=(qq+1)/delta;assert exponent<0
 for scale in [q('1'),q('3/2'),q('2'),q('10')]:
  modified=cap*ar(scale)**ar(exponent);assert modified<=cap if scale==1 else modified<cap
  monotonicity_checks.append({'H_scale':str(scale),'cap':modified.str(70)})
 result={'utc':datetime.now(timezone.utc).isoformat(),'precision_bits':ctx.prec,'source_sha256':sha(B/'source/T1_REVIEWS_v35.md'),'identity_checks':identities,'screening_margins':margins,'margin_count':sum(len(r['margins']) for r in margins),'smallest_graded_candidate':smallest[1],'smallest_graded_margin':str(smallest[0]),'endpoint_thresholds':beta_checks,'old_CI_cap':cap.str(100),'H_monotonicity':monotonicity_checks,'K_upper_exact':str(K),'inputs':{str(f.relative_to(B)):sha(f) for f in [B/'PROOF.md',B/'data/manifest.json',B/'data/parameters.json',Path(__file__)]},'elapsed_seconds':time.monotonic()-start,'foreign_code_executed':False,'no_PDE_apriori_nonexistence_inference':True,'verdict':'CONFIRMED scoped screening and cap arithmetic; logical qualifications in PROOF.md'}
 with (B/'verification/result.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
 print(result['utc'],result['elapsed_seconds'],result['margin_count'],'margins',cap.str(40))
if __name__=='__main__':main()
