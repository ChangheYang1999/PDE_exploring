"""Exact public fields of the separately inherited regional conclusions."""
from check import *

def main():
 start=now();pins={};v=load(E/'chain_checks.json');merge(pins,v);pin(pins,str((E/'chain_checks.json').relative_to(B)))
 def get(n):need(n in pins and sha(B/n)==pins[n],'accepted scoped source');return load(B/n)
 vp=get('research/global_residual_assembly/evidence/verdict.json');old=get('research/global_residual_assembly/evidence/primary_assembly_v2.json');p=get('research/middle_residual/evidence/primary_acceptance.json');s=get('research/middle_residual/evidence/full_q16_summary.json');j=get('research/middle_second/evidence/full_q16_verdict.json');maincheck=load(E/'checks.json')
 need(vp['status']=='CONFIRMED_PRIMARY_ONLY_WHOLE_PLANE_ZEROTH_RESIDUAL_ASSEMBLY' and p['status']=='CONFIRMED_PRIMARY_ASSEMBLY','accepted primary evidence level');need(p['cells']==s['cells_complete']==j['cells']==7809 and s['source_footer_read'] is True,'full primary/joint region')
 oldsum=sum((ff(old['regions'][r]['squared_norm_exact']) for r in ['inner','middle','outer']),F(0));need(oldsum==ff(old['global_N2']['input_squared_exact'])==ff(vp['N2']['input_squared_exact']) and oldsum<F('0.001903991978')**2 and ff(vp['N2']['strict_upper_exact'])==F('0.001903991978'),'old whole-plane independent exact sum and ceiling')
 direct=sum((fmpq(old['regions'][r]['squared_norm_exact']) for r in ['outer','inner','middle']),fmpq(0));need(qf(direct)==oldsum,'second exact earlier sum')
 pd=['0.000134943','0.000291625','0.000427591','0.000372741'];jd=['0.000134942914','0.000291624061','0.000427590787','0.000372740952'];public={}
 for (key,mkey),a,b in zip(MKEYS.items(),pd,jd,strict=True):
  pa=ff(s['maxima'][mkey]['bound_exact']);ja=ff(j['maxima'][mkey]['upper_exact']);need(pa==ff(old['regions']['middle']['maxima_exact'][key]) if 'maxima_exact' in old['regions']['middle'] else pa==ff(vp['suprema'][key]['regional_upper_exact']['middle']),'actual primary saved maximum source')
  need(pa<ff(p['public_strict_bounds'][mkey])==F(a) and ja<ff(j['strict_public_ceilings'][mkey])==F(b) and pa<=ja,'both regional exact ceilings')
  vals=list(map(ff,vp['suprema'][key]['regional_upper_exact'].values()));mx=max(vals);need(mx==ff(vp['suprema'][key]['authoritative_upper_exact'])<ff(vp['suprema'][key]['strict_upper_exact'])==F(maincheck['suprema'][key]['strict_decimal']),'old global suprema same strict ceilings');need(qf(max(fmpq(str(x)) for x in vals))==mx,'second exact old maximum')
  public[key]={'primary_strict_decimal':a,'joint_strict_decimal':b,'global_strict_decimal':maincheck['suprema'][key]['strict_decimal']}
 psq=ff(old['regions']['middle']['squared_norm_exact']);jsq=ff(j['L2_squared_upper_exact']);need(psq>0 and psq<F('0.000523709')**2 and ff(p['L2_strict_upper_exact'])==F('0.000523709') and jsq>0 and jsq<F('0.000523708529')**2 and ff(j['strict_public_ceilings']['L2'])==F('0.000523708529'),'both strict regional norms by exact squaring')
 need(ff(j['L2_upper_exact'])**2>=jsq and ff(j['L2_upper_exact'])<F('0.000523708529'),'joint saved root outward square')
 for n in ['SCOPE_ADDENDUM.md','code/check_scope.py']:pin(pins,str((D/n).relative_to(B)))
 x={'start_utc':start,'utc':now(),'status':'PASS_PRIMARY_JOINT_REGIONAL_AND_BOTH_GLOBAL_CEILINGS','public_suprema':public,'public_norms':{'primary_middle':'0.000523709','joint_middle':'0.000523708529','primary_whole_plane':'0.001903991978','joint_whole_plane':'0.001903991978'},'regional_squared_exact':{'primary_middle':str(psq),'joint_middle':str(jsq)},'primary_global_squared_exact':str(oldsum),'files':dict(sorted(pins.items())),'scope':'Each accepted regional theorem receives the same canonical-input premise separately. No deduction of sharper regional bounds from a larger whole-plane ceiling.'};write(E/'scope_checks.json',x);print(json.dumps({k:x[k] for k in ['utc','status','public_norms']}))
if __name__=='__main__':main()
