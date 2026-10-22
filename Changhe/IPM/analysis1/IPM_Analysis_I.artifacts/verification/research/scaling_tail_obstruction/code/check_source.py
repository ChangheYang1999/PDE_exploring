from check import *
P=B.parent/'ipmA-num/data/trial_v2_h0.008.npz';PH='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
def trial_npy(b,shape):
 need(b[:8]==b'\x93NUMPY\x01\x00','trial NPY v1');l=int.from_bytes(b[8:10],'little');h=ast.literal_eval(b[10:10+l].decode())
 if h.get('fortran_order') is False:return npy(b,shape)
 need(len(shape)==2 and h=={'descr':'<f8','fortran_order':True,'shape':shape},'explicit two-dimensional Fortran representation');raw=b[10+l:];rows,cols=shape;need(len(raw)==8*rows*cols,'complete Fortran payload')
 return [ieee(raw[8*(i+rows*j):8*(i+rows*j+1)]) for i in range(rows) for j in range(cols)]
def main():
 start=now();pins={};main=load(E/'checks.json')
 for n,h in main['files'].items():need(sha(B/n)==h,'main immutable');pins[n]=h
 need(sha(P)==PH and load(B/S)['source_npz_sha256']==PH,'complete explicit trial source');pins[str(P)]=PH
 src=load(B/S);count=0
 with zipfile.ZipFile(P) as zp,np.load(P,allow_pickle=False) as nz:
  need(len(zp.namelist())==len(set(zp.namelist())),'unique trial ZIP')
  for n in ['Aout','Eo','knots','k','L','bo']:
   shape=tuple(src['arrays'][n]['shape']) if n in src['arrays'] else ();expected=list(map(hx,src['arrays'][n]['hex'])) if n in src['arrays'] else [hx(src['scalars_hex'][n])];raw=trial_npy(zp.read(n+'.npy'),shape)
   need(raw==expected==[F(*float(x).as_integer_ratio()) for x in nz[n].ravel()],'all exact trial source '+n);count+=len(raw)
  with np.load(B/V,allow_pickle=False) as vz:
   need(nz['Aout'][:,0].tobytes()==vz['A0'].tobytes() and nz['k'].tobytes()==vz['k'].tobytes() and nz['knots'][-1:].tobytes()==vz['t0'].tobytes(),'literal leading and scalar byte identity')
 with zipfile.ZipFile(B/V) as z:
  b=z.read('Mh.npy');need(b[:8]==b'\x93NUMPY\x01\x00','Mh NPY');l=int.from_bytes(b[8:10],'little');h=ast.literal_eval(b[10:10+l].decode());need(h=={'descr':'<i8','fortran_order':False,'shape':()} and len(b)==18+l,'Mh schema');Mh=int.from_bytes(b[10+l:],'little',signed=True);need(Mh==16<=260,'explicit actual section modes')
 # Two exact evaluation routes for the actual outer piece convention.
 t0=hx(src['arrays']['knots']['hex'][-1]);cases=[]
 for u in [F(0),F(1,8),F(7,3),F(200)]:
  h=t0+u;q=qf(fmpq(str(t0))+fmpq(str(u)));need(h==q,'absolute t from shifted piece');cases.append({'u':str(u),'t':str(h),'kp_polynomial':str(h),'tau_polynomial':'1'})
 for n in ['REVIEW_RESOLUTION.md','sources/lin_assembly.py','code/check_source.py','evidence/checks.json']:pins[str((D/n).relative_to(B))]=sha(D/n)
 for n,h in pins.items():need(sha(B/n)==h,'all source bytes unchanged')
 out={'start_utc':start,'utc':now(),'status':'PASS_EXPLICIT_TRIAL_PAIR_AND_SHIFTED_PIECE_CONVENTION','trial_scalars_each_import_path':count,'Mh':Mh,'piece_cases':cases,'main_checks_sha256':sha(E/'checks.json'),'files':dict(sorted(pins.items())),'scope':'Explicit frozen vector/trial pairing and audited function recipe; no historical producer-run identity or assembled operator claim.'}
 with (E/'source_checks.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(json.dumps({k:out[k] for k in ['utc','status','trial_scalars_each_import_path','Mh']}))
if __name__=='__main__':main()
