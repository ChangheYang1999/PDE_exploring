"""Prepare an explicitly scoped exact-data contract for accepted distances."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json
R=Path(__file__).resolve().parents[3];B=R/'research/final_table_trace'
def sha(p):return sha256(p.read_bytes()).hexdigest()
def info(p):
 p=Path(p);p=p if p.is_absolute() else R/p
 return {'path':str(p.relative_to(R)),'sha256':sha(p)}
paths={7:'research/angular_probe_audit/verification/candidate007_n7.json',8:'research/n3_stronger_weak008/verification/result.json',9:'research/successor_weak_probes/reviews/T4_225_231/ACCEPTANCE.json',10:'research/scaled_weak_backend/reviews/T4_010/ACCEPTANCE_n7.json',12:'research/successor_weak_probes/reviews/T4_236/ACCEPTANCE.json',13:'research/factored_monomial_audit/verification/result.json',14:'research/successor_factored_weak/reviews/T4_014/ACCEPTANCE.json',15:'research/candidate015_three_weak_peer/verification/result.json',**{i:f'research/candidate{i:03d}_weak_peer/verification/result.json' for i in range(16,27)}}
paths[17]='research/candidate017_weak19_peer/verification/result.json'
claims={7:157,8:238,9:183,10:215,12:188,13:204,14:224,15:383,16:253,17:267,18:276,19:290,20:299,21:320,22:334,23:350,24:359,25:371,26:379}
rownums={7:56,8:60,9:62,10:65,12:67,13:71,14:75,15:77,16:80,17:82,18:84,19:86,20:88,21:90,22:92,23:94,24:96,25:99,26:101}
displays={7:'0.004769166867',8:'0.03632',9:'0.0169',10:'0.0224795',12:'0.0186',13:'0.00199234339',14:'0.001983',15:'0.0030334',16:'0.0014704',17:'0.001671830698',18:'0.001655825792',19:'0.001661806967',20:'0.001855374677',21:'0.001864696855',22:'0.00135251',23:'0.002634958',24:'0.001556067',25:'0.002065801',26:'0.001355907'}
summaryfloors={7:'0.004769166867',8:'0.036323397462385412',9:'0.016967603956',10:'0.022479506978',12:'0.018641021006',13:'0.00199234339',14:'0.00198301351067',15:'0.003033479200692324',16:'0.001470360924123708',17:'0.00167183069831928',18:'0.00165582579205606',19:'0.001661806967193251',20:'0.001855374677442712',21:'0.001864696854799172',22:'0.00135251075726327',23:'0.002634958245163687',24:'0.001556067368832641',25:'0.002065801265578052',26:'0.001355907204057457'}
proofs={7:'research/angular_probe_audit/PROOF.md',8:'research/n3_stronger_weak008/PROOF.md',9:'research/successor_weak_probes/PROOF.md',10:'research/scaled_weak_backend/PROOF.md',12:'research/successor_weak_probes/PROOF.md',13:'research/factored_monomial_audit/PROOF.md',14:'research/successor_factored_weak/PROOF.md',15:'research/candidate015_three_weak_peer/PROOF.md'}
for i,p in paths.items():proofs.setdefault(i,str(Path(p).parents[1]/'PROOF.md'))
now=datetime.now(timezone.utc).isoformat()
prepared={'utc':now,'proof':info(B/'DISTANCE_PROOF.md'),'checker_exists':(B/'code/check_distance_v01.py').exists(),'preparation_code':info(Path(__file__).resolve())}
assert not prepared['checker_exists']
with (B/'verification/DISTANCE_PROOF_FIRST_v01.json').open('x') as f:json.dump(prepared,f,indent=2);f.write('\n')
entries=[]
for i,p in paths.items():
 root=json.loads((R/p).read_text());dirs=list((R/'research/candidate_audits/data').glob(f'C1-N1-{i:03d}-*'));assert len(dirs)==1
 folder=dirs[0];man=json.loads((folder/'MANIFEST.json').read_text());candidate=man['id'];raw=folder/man['coefficient_files'][0]['name'];assert sha(raw)==man['coefficient_files'][0]['sha256']
 original=None;index=None;row=root
 if i==8:index=1;row=root['rows'][index]
 elif i==9:index=2;row=root['rows'][index];original=f'research/successor_weak_probes/verification/{candidate}_n7.json'
 elif i==10:original=f'research/scaled_weak_backend/verification/{candidate}_n7.json'
 elif i==12:index=0;row=root['rows'][index];original=f'research/successor_weak_probes/verification/{candidate}_n7.json'
 elif i==14:original=f'research/successor_factored_weak/verification/{candidate}_n021_K00522.json'
 elif i==15:index=2;row=root['rows'][index];original=next(k for k,h in root['inputs'].items() if h==row['own_source_sha256'])
 elif i>=16:index=1 if i==16 else 0;row=root['rows'][index];matches=[k for k,h in root['own_inputs'].items() if k.endswith(f'{candidate}_n019_K01800.json')];assert len(matches)==1,(i,matches);original=matches[0]
 orig=json.loads((R/original).read_text()) if original else root
 if i in (9,12):assert sha(R/original)==row['own_sha256']
 if i in (10,14):assert sha(R/original)==root['own_result_sha256']
 floor_key='strict_sharp_floor' if i==15 else ('strict_floor' if i>=16 else 'strict_lower_exact')
 radius_record=original if i in (9,10,12,14) else p
 radius_index=None if i in (9,10,12,14) else index
 radius_key='sharp_root' if i==15 else ('radius_recomputed' if i>=16 else 'radius')
 floor=row[floor_key]
 if i in (10,14):floor=root[floor_key]
 rawbridge=R/f'research/candidate_audits/verification/{candidate}.json'
 bridge=info(rawbridge) if rawbridge.exists() else None
 n,K=(7,3) if i in (7,9,10,12) else ((1,2048) if i==8 else ((21,522) if i in (13,14) else ((23,2400) if i==15 else (19,1800))))
 peer=[]
 if i==7:peer=[info('research/angular_probe_audit/source/T4_n7_a0.json')]
 elif i==8:peer=[info('research/n3_stronger_weak008/source/N3_008_wlap.json')]
 elif i in (9,12):peer=[info(Path(p).parent/f'{i:03d}_n7_result.json')]
 elif i==10:peer=[info('research/scaled_weak_backend/reviews/T4_010/T4_n7.json')]
 elif i==13:peer=[info(k) for k,h in root['inputs'].items() if '/source/' in k and k.endswith('.json')]
 elif i==14:peer=[info(k) for k,h in root['frozen_or_retained_sources'].items() if h==root['peer_result_sha256']]
 elif i==15:peer=[info(k) for k,h in root['inputs'].items() if '/source/' in k and k.endswith('.json')]
 else:peer=[dict(path=k,sha256=e['stored_sha256'],decoded_sha256=e['sha256'],gzip=e.get('gzip',False)) for k,e in root['frozen_or_retained_sources'].items() if e['sha256']==row['peer_result_sha256']]
 assert peer,(i,'missing independent record')
 entries.append({'number':i,'candidate':candidate,'claim':f'N4-{claims[i]:03d}','accepted_result':info(p),'accepted_row_index':index,'accepted_floor_key':floor_key,'accepted_floor':floor,'original_result':info(original) if original else info(p),'radius_record':info(radius_record),'radius_row_index':radius_index,'radius_key':radius_key,'probe':{'n':n,'K':K},'proof':info(proofs[i]),'immutable_manifest':info(folder/'MANIFEST.json'),'immutable_raw':info(raw),'c_exact':man['c_l_exact'],'canonical_bridge':bridge,'independent_records':peer,'report_primary_row':rownums[i],'report_principal_strict_floor':displays[i],'own_summary_floor':summaryfloors[i],'scope':'Only the named principal certificate and displays; other probes and all dyadic rows need separate evidence.'})
result={'utc':now,'proof':info(B/'DISTANCE_PROOF.md'),'entries':entries,'comparison_ceilings':{'graded':'25/54684','sharpw_upper':'1781/625000000','TB_sharp_upper':'3793/1000000000'},'scope':'Nineteen principal successor distance certificates and their selected displays. Direct input integrity and accepted numerical provenance only.'}
with (B/'source/distance_contract_v01.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'entries':len(entries),'contract_sha256':sha(B/'source/distance_contract_v01.json'),'proof_first_sha256':sha(B/'verification/DISTANCE_PROOF_FIRST_v01.json')},indent=2))
