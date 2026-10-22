"""Exact input and norm linkage for the new selected-annulus consequence."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib
R=Path(__file__).resolve().parents[3];D=R/'research/scaling_selected_application';E=D/'evidence'
load=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
A=R/'research/scaling_norm_lower_bound/evidence/constants.json';B=R/'research/derivative_norm_regional_composition/evidence/both/verdict.json';I=R/'research/derivative_norm_regional_composition/evidence/identity_expected.json';G=R/'research/modal_graph_scaling/evidence/verdict.json'
a,b,i,g=map(load,[A,B,I,G]);assert b['mode']=='both' and b['status']=='CONFIRMED_COMPLETE_CANONICAL_REGIONAL_DERIVATIVE_COMPOSITION'
assert b['norms']==['epsilon','epsilon-D_epsilon']
assert F(a['k'])==F(b['geometry_exact']['k']) and F(a['L'])==F(b['geometry_exact']['L'])
assert a['norm']=='weighted weak H1: integral (f^2+r^2|grad f|^2) L^6 r^-6 (1+r^2/L^2)^(3/2-k) dX'
p={str(f.relative_to(R)):sha(f) for f in [A,B,I,G,Path(__file__).resolve()]}
for n,h in a['canonical_identity_files'].items():
 assert b['files'][n]==h==g['files'][n]==sha(R/n);p[n]=h
assert all(i['files'][n]==h for n,h in a['canonical_identity_files'].items())
for n in ['research/modal_graph_scaling/PROOF.md','research/modal_graph_scaling/ADDENDUM.md','research/modal_graph_scaling/REVIEW_RESOLUTIONS.md','research/modal_graph_scaling/FINAL_ADJUDICATION.md','research/derivative_norm_regional_composition/PROOF.md']:
 p[n]=sha(R/n)
z={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_SAME_TRIAL_CONSTANTS_CANONICAL_DATA_AND_NORM_LABEL_LINKAGE','k':a['k'],'L':a['L'],'norm':a['norm'],'denominator':b['published_whole_plane_norm_ceilings'][1],'files':p,'scope':'Exact data identity and scalar/label linkage. Mathematical equality of norm formulas and graph-limit consequence are separately read and adjudicated; this script does not prove those prose identities.'}
with (E/'linkage_check.json').open('x') as f:json.dump(z,f,indent=2);f.write('\n')
print(z['utc'],z['status'])
