"""Finite failure-injection and exact-conversion diagnostics, not a full claim."""
from common import *
from mpmath import iv
import engine_arb,engine_iv,engine_complex

def main():
 nodes,keys,tables,dep,selected=load_geometry();counts={};iv.dps=180;ctx.prec=512
 examples=[0.0,-0.0,float.fromhex('0x0.0000000000001p-1022'),-float.fromhex('0x0.0000000000001p-1022'),float.fromhex('0x1.fffffffffffffp+1023'),1.0,-1.25,2.0**-500]
 for x in examples:
  p,q=x.as_integer_ratio();v=iv.mpf(x);ref=iv.mpf(p)/q
  assert (v.a==ref.a) is True and (v.b==ref.b) is True and dy(arb(x))==F(p,q)
 counts['exact_binary64_conversions_per_library']=len(examples)
 assert (iv.mpf([0,2])<=iv.mpf([1,3])) is None;counts['uncertain_iv_rejected']=1
 def rejected(call):
  try:call()
  except AssertionError:return True
  return False
 cache=new_cache();indices=[0,7,25245,50999]
 for i in indices:
  node=tuple(map(int,nodes[i]));a,b=ancestry_node(*node);m,r,g,p=source_packet(cache,a,b,node,keys[i],tables,selected)
  for engine in (engine_arb,engine_iv,engine_complex):
   assert engine.check(node,m,r,g)==(COEFF,7)
   badm=m.copy();badr=r.copy();badm[0,0,0]=123.0;badr[0,0,0]=0.0
   assert rejected(lambda:engine.check(node,badm,badr,g))
   badg=g.copy();badg[10]=0.0;assert rejected(lambda:engine.check(node,m,r,badg))
 counts['complete_cells_each_engine']=len(indices);counts['deflated_wrong_coefficient_rejected']=3*len(indices);counts['zero_halfwidth_rejected']=3*len(indices)
 # Compare the stack construction with independently addressed ancestry on all nodes.
 for i,(a,b,node) in enumerate(actual_nodes()):
  aa,bb=ancestry_node(*node);assert endpoints_record(a,b,node)==endpoints_record(aa,bb,node)
 counts['exact_endpoint_path_agreements']=i+1;assert i+1==TOTAL
 out={'utc':utc(),'status':'PASS_FINITE_MANUFACTURED_DIAGNOSTICS','counts':counts,'source_sha256':sha(__file__),'source_files':current_files(dep),'runtime':runtime()}
 write_json(E/'manufactured_checks.json',out);print(canon({'utc':out['utc'],'status':out['status'],'counts':counts}),flush=True)
if __name__=='__main__':main()
