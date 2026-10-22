"""Manufactured directed-rounding and dual-root checks, no parent application."""
from common import *
import ast
from evaluate import ceiling,reduction
from replay import qdecimal,ceiling_record
for n in ['common.py','extract.py','evaluate.py','replay.py','gate.py','selfcheck.py']:ast.parse((D/'code'/n).read_text())
first=load(E/'proof_first.json');assert first['code_files']==[] and first['proof_sha256']==sha(D/'PROOF.md') and first['constants_sha256']==sha(E/'constants.json')
values=[F(0),F(1),F(1,3),F(1,10**80),F(10)**80,F(10)**24-F(1,10**20),F(2)**480/F(3),F(999999,10**9)]
for q in values:
 z=ceiling(q);assert ceiling_record(z,q)==qdecimal(z['decimal'])
sets=[[F(0)]*3,[F(1,3),F(2,7),F(1,11)],[F(2)**400,F(3,2**400),F(7,13)],[F(1,10**80),F(9,10**81),F(0)]]
count=0
for values in sets:
 r=reduction(values);total=sum(values,F(0));assert F(r['sum_exact'])==total
 for eng in ENGINES:
  lo,hi=pair(r['engines'][eng]['sum']);assert lo<=total<=hi
  lo,hi=pair(r['engines'][eng]['root']);assert lo*lo<=total<=hi*hi;count+=1
 q=F(r['whole_plane_norm_ceiling']['exact']);assert q*q>total if total else q==0
bad=0
for value in ['1e-3','nan','inf','-1','+2','.1','1.','1/2']:
 try:qdecimal(value)
 except AssertionError:bad+=1
 else:raise AssertionError(value)
assert bad==8 and count==8
identity=load(E/'identity_expected.json')
for n,h in identity['files'].items():assert sha(ROOT/n)==h
v={'utc':now(),'status':'PASS_REGIONAL_SCALAR_WORKFLOW_SELF_CHECKS','source_sha256':sha(Path(__file__)),'directed_decimal_examples':8,'root_examples':len(sets),'integer_root_endpoint_checks':count,'malformed_decimal_rejections':bad,'canonical_identity_files':len(identity['files']),'numerical_parent_applications':0,'scope':'Manufactured arithmetic examples and fixed source identity only. No179/180/181 numerical application.'}
write(E/'selfcheck.json',v);print(json.dumps(v))
