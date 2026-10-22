"""Exact upward publication checks and pinned local collar verdict."""
import sys,json,hashlib,argparse
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
B=Path(__file__).resolve().parents[3];E=B/'research/collar_coupling/evidence'
assert sys.flags.optimize==0

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p):
 def bad(x):raise ValueError(x)
 return json.loads(Path(p).read_bytes(),parse_constant=bad)
def decimal(q):
 q=F(q);assert q>0;n=q.numerator*10**12//q.denominator+1;s=str(n).zfill(13);out=s[:-12]+'.'+s[-12:];assert F(out)>q;return out

def run(prepare):
 src=B/'research/collar_coupling/code/audit_constants.py';proof=B/'research/collar_coupling/PROOF.md';snap=E/'lead_collar_v2.md';rp=E/'constants_audit.json';r=load(rp)
 assert r['status']=='PASS_REQUIRES_REVIEW' and r['source_sha256']==sha(src) and r['proof_sha256']==sha(proof) and r['lead_snapshot_sha256']==sha(snap)
 assert r['interval_containments']==46 and r['exact_identities']=={'reflection_series_checks':42,'coupling_polynomial_monomials':21,'coupling_identity':'PASS'}
 assert r['Arb_bits']==320 and r['iv_dps']==160
 for p,h in r['dependency_pins'].items():assert sha(B/'research/collar_coupling'/p)==h
 serial=load(E/'serialized_audit_v2.json');assert serial['returncode']==0 and serial['resumed'] is True
 rows=[];count=0
 for row in r['cases']:
  vals={}
  for key,v in row['values'].items():
   al,ah,il,ih=[F(v[k]) for k in ['arb_lower_exact','arb_upper_exact','iv_lower_exact','iv_upper_exact']];assert 0<al<=il<=ih<=ah
   d=decimal(max(ah,ih));assert F(d)>ah and F(d)>ih;count+=2;vals[key]=d
  rows.append({'inputs_exact':row['inputs_exact'],'strict_upper_decimals':vals})
 assert count==92
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_OUTPUT_REQUIRES_REVIEW','source_sha256':sha(src),'proof_sha256':sha(proof),'constant_result_sha256':sha(rp),'interval_containments':46,'strict_rational_publication_checks':count,'exact_identities':r['exact_identities'],'cases':rows,'independence':'Arb320 versus iv160; different Gamma-moment assemblies for the face constant and trace coefficient, different factorization of far A_m. Cutoff powers J_j,k_p and positive sums use shared mathematically derived formulas. Agreement is a consistency check; each interval expression independently encloses its stated constant.'}
 if prepare:
  (E/'output_digest.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));return
 digest=load(E/'output_digest.json');assert digest['constant_result_sha256']==sha(rp) and digest['cases']==rows and digest['strict_rational_publication_checks']==92
 reviews=[];paths=[src,proof,snap,rp,E/'serialized_audit_v2.json',E/'output_digest.json',Path(__file__).resolve(),B/'research/edge_velocity/evidence/verdict.json']
 for tag in ['collar_theorem_extended','collar_code_focus','collar_final_closure']:
  meta=B/'notes/reviews'/f'{tag}_metadata.json';reply=B/'notes/reviews'/f'{tag}_response.md';m=load(meta);assert m['actual_response_model']=='claude-opus-5-5' and m['stop_reason']=='end_turn' and reply.stat().st_size>0
  reviews.append({'tag':tag,'actual_model':m['actual_response_model'],'end_utc':m['end_utc']});paths.extend([meta,reply])
 out.update(status='CONFIRMED',reviews=reviews,files={str(p.relative_to(B)):sha(p) for p in paths},scope='Local collar mapping and forcing theorem with x1>2d, 5/2<b<7/2, 0<g<2, separate finite raw strain and H^(b-3/2) regularity of the cutoff edge coefficient when that target is claimed. No corner, conic summation, source transition, global inverse, derivative residual certificate or decisive endpoint.')
 (E/'verdict.json').write_text(json.dumps(out,indent=2)+'\n')
 text='# Local collar theorem and constants\n\n'+out['utc']+'; CONFIRMED.\n\n'+out['scope']+'\n\nThe raw strain is sigma=psi_xy(0); its scaling contribution is sigma/3. The endpoint g=2 and inference of finite strain from the collar norm alone are invalid for the stated weighted class. Global cutoff tails are claimed only for j<3.\n\n| b | K_n < | A_0 < | K_f < |\n|---|---|---|---|\n'
 for row in rows:
  v=row['strict_upper_decimals'];text+='| '+row['inputs_exact']['b']+' | '+v['K_n']+' | '+v['A0']+' | '+v['K_f']+' |\n'
 text+='\nBoth rows have g=23/20, I=[1,7], d=9/20. All46 constants and92 exact upward comparisons are recorded in evidence/verdict.json. The42 rational reflection checks supplement the general proof; the21-monomial polynomial check verifies the full forcing identity.\n\n'+out['independence']+'\n'
 (B/'research/collar_coupling/RESULT.md').write_text(text);print(json.dumps({'status':out['status'],'utc':out['utc'],'verdict_sha256':sha(E/'verdict.json')}))
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--prepare',action='store_true');a=ap.parse_args();run(a.prepare)
