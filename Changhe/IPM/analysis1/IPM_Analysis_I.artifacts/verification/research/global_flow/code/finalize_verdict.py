"""Exact final audit of conditional flow statements, scalar data and review pins."""
import json,hashlib,os,sys
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/global_flow/evidence'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def bounds(x):l,h=F(x['lower_exact']),F(x['upper_exact']);assert l<=h;return l,h

def main():
 proof=B/'research/global_flow/PROOF.md';code=B/'research/global_flow/code/check_identities.py';ep=E/'checks.json';e=json.loads(ep.read_text())
 fixed={str(proof.relative_to(B)):'afa8cffd1a81b80e034135ea29ca297bf1b5d79f7e76c4e45dc127b98680af0f',str(code.relative_to(B)):'88bfdb82a425703b18a88e19a6ec48a3b659f2a8f8ff6e6a4db5dadcc27c464b','research/modal_source/evidence/source_result.json':'51f283cd4ea7145f633e5449236cdd0bc2879b9ccf922d9fbadb6a609afa4691','research/modal_source/evidence/output_audit.json':'1ac210fb952eb83594ab9975bb0fafd4c56759ddbd654a4443c58190f83e2e6e','data_exact/modal_v2.json':'57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'}
 for p,h in fixed.items():assert sha(B/p)==h
 assert e['status']=='PASS_EXACT_CONTRACTS_AND_INTERVAL_SCALARS' and e['source_sha256']==sha(code) and e['proof_sha256']==sha(proof)
 k=F(1615536043799051,9007199254740992);a=F(129,20);b=F(307,100);gam=F(1129,1000);cl=1/k;kap=1-(gam-1)/k
 wanted={'k':k,'cl':cl,'A0':2/k-1,'D0':4/k-1,'T_corner':a-b-1+(-1-2*a+4*b)/k,'T_source_frozen_mu1':b-1-cl,'T_far':-kap,'kappa_inf':kap,'inverse_lower_bound_conditional':1/kap,'quarter_margin':kap-F(1,4),'unweighted_inverse_upper':k/(1+k)}
 assert len(e['rational_values'])==len(wanted);seen=set()
 for r in e['rational_values']:
  name=r['name'];assert name not in seen and F(r['exact'])==wanted[name];seen.add(name)
  for m in ['arb','iv']:l,h=bounds(r[m]);assert l<=wanted[name]<=h
 assert kap>F('0.2807') and kap<F('0.281') and 1/kap>F('3.56')
 assert e['contracts']=={'rational_scalar_arb_iv_containments':22,'actual_source_margin_containments':2,'conic_margin_identities':162,'finite_history_orbit_inequalities':79,'symbol_psd_direction_checks':30}
 src=json.loads((B/'research/modal_source/evidence/source_result.json').read_text());au=json.loads((B/'research/modal_source/evidence/output_audit.json').read_text());assert au['verdict']=='PASS' and au['source_result_sha256']==fixed['research/modal_source/evidence/source_result.json']
 depmap={'input_sha256':'data_exact/modal_v2.json','scalar_input_sha256':'research/modal_repair/evidence/independent_gauss_iv.json','source_sha256':'research/modal_source/code/certify_source.py','moments_sha256':'research/exponential_moments/code/moments.py','Cox_sha256':'research/canonical_inverse/code/exact_audit.py'}
 for key,p in depmap.items():assert sha(B/p)==src[key]==au['verified_dependencies'][key];fixed[p]=sha(B/p)
 p='research/modal_source/code/audit_output.py';assert sha(B/p)==au['audit_source_sha256'];fixed[p]=sha(B/p)
 l,h=bounds(src['final_values']['mu_minus_1']);l+=1;h+=1;assert 0<l<h<1
 expected=[-(1+cl)+b*l,-(1+cl)+b*h];actual=e['actual_source_margin'];assert list(map(F,actual['exact_enclosure']))==expected and expected[1]<F('-3.505')
 for m in ['arb','iv']:x,y=bounds(actual[m]);assert x<=expected[0]<=expected[1]<=y
 assert actual['input_audit_sha256']==fixed['research/modal_source/evidence/output_audit.json'] and actual['input_result_sha256']==fixed['research/modal_source/evidence/source_result.json']
 paths={B/p for p in fixed}|{Path(__file__),proof,code,ep,E/'lead_global_flow_v1.md',E/'planar_dependency.md',E/'planar_fetch.json'};reviews={}
 for tag in ['global_flow_repaired','global_flow_closure']:
  mp=B/f'notes/reviews/{tag}_metadata.json';m=json.loads(mp.read_text());rq=(B/f'notes/reviews/{tag}_request.txt').read_text();assert m['actual_response_model']=='claude-opus-5-5' and m['stop_reason']=='end_turn' and hashlib.sha256(rq.encode()).hexdigest()==m['input_sha256']
  if tag.endswith('closure'):
   for p in [proof,code,ep,E/'planar_dependency.md',E/'planar_fetch.json']:
    marker='\n\nFILE '+str(p.relative_to(B))+'\n';assert rq.split(marker,1)[1].split('\n\nFILE ',1)[0]==p.read_text()
  reviews[tag]={'actual_model':m['actual_response_model'],'end_utc':m['end_utc'],'verdict':'ACCEPT_CONDITIONAL_ONLY'}
  for suff in ['request.txt','response.json','response.md','metadata.json']:paths.add(B/f'notes/reviews/{tag}_{suff}')
 result={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED','claims':['conditional non-trapping and global C1 flow section','conditional uniform transit outside fixed end neighborhoods including the incoming separatrix','weighted L2 and weighted essential-sup transport inversion on explicit maximal distributional domains','measurable bounded orbit correction with correct backward weight inequality','uniform-axis hypothesis needed for conic far margin','pure-transport inverse norm at least1/kappa_inf under the stated tail/weight asymptotics','exact scalar margins and finite algebraic contracts only'],'methods':'Independent planar argument with declared classical Poincare-Bendixson dependency; elementary C1 mollifier commutator; exact rational conic and symbol identities; Arb384 and differently arranged iv160 scalar formulas; complete source/audit pin chain; actual Opus5.5 follow-up and final actual-file hash comparison.','scalar_public_bounds':{'kappa_inf_strict_lower':'0.2807','kappa_inf_strict_upper':'0.281','conditional_far_inverse_norm_strict_lower':'3.56','actual_source_margin_strict_upper':'-3.505'},'reviews':reviews,'files':{str(p.relative_to(B)):sha(p) for p in sorted(paths)},'scope':'Conditional analytic theorem only. Actual finite-domain equilibrium list/axis signs, global H1-H4 assembly, numerical transit and orbit costs, smooth Garding weight, coupled IPM inverse, high norms, nonlinear closure and decisive endpoint remain OPEN. This note does not by itself certify the actual uniform tail quotients. The separate exterior_flow topic addresses those tails.'}
 tmp=E/'verdict.json.tmp';tmp.write_text(json.dumps(result,indent=2)+'\n');os.replace(tmp,E/'verdict.json')
 for p,h in result['files'].items():assert sha(B/p)==h
 print(json.dumps({'utc':result['utc'],'status':result['status'],'pins':len(paths),'sha256':sha(E/'verdict.json'),'scalar_public_bounds':result['scalar_public_bounds']}))
if __name__=='__main__':main()
