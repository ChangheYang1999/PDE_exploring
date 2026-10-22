"""Fresh exact affine tail audit, independent of the accepted172 checker."""
from common import *
import ast,zipfile,math,struct,operator,time
from fractions import Fraction as F
from flint import fmpq,arb,ctx
from mpmath import iv
import numpy as np

def fq(q):return F(int(q.numerator),int(q.denominator))
def q(x):return fmpq(str(x))
def hx(s):
 m=re.fullmatch(r'([+-]?)0x([0-9a-f]+)\.([0-9a-f]*)p([+-]?\d+)',s);need(m is not None,'exact hexadecimal schema');sg,a,b,e=m.groups();return (-1 if sg=='-' else 1)*F(int(a+b,16))*F(2)**(int(e)-4*len(b))
def hx2(s):
 left,ex=s.split('p');sg=-1 if left.startswith('-') else 1;left=left.lstrip('+-');need(left.startswith('0x'),'second hexadecimal prefix');a,b=left[2:].split('.');v=fmpq(int(a,16))
 for i,c in enumerate(b,1):v+=fmpq(int(c,16),16**i)
 return fq(sg*v*fmpq(2)**int(ex))
def ieee(b):
 need(len(b)==8,'exact eight-byte word');bits=int.from_bytes(b,'little');sign=-1 if bits>>63 else 1;expo=(bits>>52)&2047;mant=bits&((1<<52)-1);need(expo!=2047,'finite binary64');return sign*F(mant+(1<<52) if expo else mant)*F(2)**(expo-1075 if expo else -1074)
def npy(b,shape,descr='<f8'):
 need(b[:8]==b'\x93NUMPY\x01\x00','NPY1');n=int.from_bytes(b[8:10],'little');header=ast.literal_eval(b[10:10+n].decode());need(header=={'descr':descr,'fortran_order':False,'shape':shape},'NPY exact schema');data=b[10+n:];need(len(data)==8*math.prod(shape),'complete NPY payload')
 return [ieee(data[i:i+8]) if descr=='<f8' else int.from_bytes(data[i:i+8],'little',signed=True) for i in range(0,len(data),8)]
def rn(x):
 x=F(x)
 if not x:return x
 sg=1 if x>0 else -1;x=abs(x);e=x.numerator.bit_length()-x.denominator.bit_length()
 if x<F(2)**e:e-=1
 need(e<=1023,'finite round range');step=F(2)**max(-1074,e-52);scaled=x/step;a,b=divmod(scaled.numerator,scaled.denominator)
 if 2*b>scaled.denominator or (2*b==scaled.denominator and a%2):a+=1
 return sg*a*step
def rn2(x):
 x=q(x)
 if not x:return F(0)
 sg=1 if x>0 else -1;x=abs(x);e=int(x.numerator).bit_length()-int(x.denominator).bit_length()
 while x<fmpq(2)**e:e-=1
 while x>=fmpq(2)**(e+1):e+=1
 need(e<=1023,'second finite range');unit=fmpq(2)**max(-1074,e-52);scaled=x/unit;low=int(scaled.floor());left=scaled-low
 if left>fmpq(1,2) or left==fmpq(1,2) and low%2:low+=1
 return fq(sg*low*unit)
def ai(x):return arb(x.numerator)/arb(x.denominator)
def ii(x):return iv.mpf(x.numerator)/iv.mpf(x.denominator)
def endpoint(x):
 need(len(x)==4,'iv endpoint tuple');s,m,e,b=map(operator.index,x);need(s in [0,1] and m>=0 and b>=0 and b==m.bit_length(),'finite normalized iv endpoint');return (-1)**s*F(m)*F(2)**e
def hypothesis(A,Bv,lam,nu,mu,det):need(A[0]>0 and Bv[1]>0 and mu<lam<nu and det>0,'strict exterior hypotheses')
def main():
 start=now();tic=time.monotonic();pins,parents,review=base();ctx.prec=320;ctx.threads=1;iv.dps=110
 with zipfile.ZipFile(B/V) as zp,np.load(B/V,allow_pickle=False) as nz:
  need(len(zp.namelist())==len(set(zp.namelist())),'unique ZIP names');arrays={}
  for n,shape in [('A0',(260,)),('Bm',(261,)),('k',()),('t0',())]:
   a=npy(zp.read(n+'.npy'),shape);b=[F(*float(x).as_integer_ratio()) for x in nz[n].ravel()];need(a==b,'two full imports '+n);arrays[n]=a
  mh=npy(zp.read('Mh.npy'),(),'<i8')[0];need(mh==int(nz['Mh'])==16,'literal Mh=16')
 A=arrays['A0'];Bv=arrays['Bm'];k=arrays['k'][0];t0=arrays['t0'][0];src=load(B/S);need(src['arrays']['Aout']['shape']==[260,10],'full Aout shape');aout=[hx(s) for s in src['arrays']['Aout']['hex']];need(aout==[hx2(s) for s in src['arrays']['Aout']['hex']] and len(aout)==2600,'independent exact hex parsers');need(A==aout[::10] and k==hx(src['scalars_hex']['k'])==F(1615536043799051,9007199254740992) and t0==hx(src['arrays']['knots']['hex'][-1]),'entire canonical leading source and exact scalar identities')
 zrec=load(B/Z);need(zrec['input_sha256']==SH,'normalization source identity');zz=zrec['values']['A00_correction'];zlo=F(zz['lower_exact_dyadic']);zhi=F(zz['upper_exact_dyadic']);need(zlo<=zhi<0 and all(z.denominator&(z.denominator-1)==0 for z in [zlo,zhi]),'ordered dyadic Z');need([zlo,zhi]==[fq(q(zz[key])) for key in ['lower_exact_dyadic','upper_exact_dyadic']],'two Z parsers')
 jl=src['outer_jl'];tree=ast.parse((B/'research/scaling_tail_obstruction/sources/modal_fit.py').read_text());assign=next(n for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='OUTER_JL' for t in n.targets));need([list(x) for x in ast.literal_eval(assign.value)]==jl and len(jl)==10 and jl[0]==[0,0] and len({tuple(x) for x in jl})==10,'source exact exponent pairs');need(all(type(j) is int and type(l) is int and j>=0 and l>=0 and (j,l)!=(0,0) for j,l in jl[1:]),'strict lower exponent indices')
 exact=[k-3-j*(1-k)-2*l for j,l in jl];exact2=[fq(q(k)-3-j*(1-q(k))-2*l) for j,l in jl];literal=[rn(rn(rn(k-3)-rn(j*rn(1-k)))-2*l) for j,l in jl];literal2=[]
 for j,l in jl:
  leading2=rn2(q(k)-3);one_minus2=rn2(1-q(k));product2=rn2(j*q(one_minus2));difference2=rn2(q(leading2)-q(product2));literal2.append(rn2(q(difference2)-2*l))
 hardware=[F((float(k)-3)-j*(1-float(k))-2*l) for j,l in jl];need(exact==exact2 and literal==literal2==hardware,'two exact rate methods and elementary binary64 operations');lam=exact[0];nu=literal[0];need(nu-lam==F(1,2**53),'actual exponent mismatch retained');bo=hx(src['scalars_hex']['bo']);low=exact[1:]+[-bo]+literal[1:]+[-bo];mu=max(low);need(len(low)==20 and all(eta<=mu<lam<nu for eta in low) and 0<k<1,'all strict lower rates and nonzero scaling factor')
 expected=[F(0)]*261;expected[0]=rn(A[1]/2);expected[1]=rn(A[0]+rn(A[2]/2))
 for j in range(2,260):expected[j]=rn(rn(A[j-1]+A[j+1])/2) if j+1<260 else rn(A[j-1]/2)
 need(Bv==expected and Bv[260]==0,'complete literal Bm recipe including omitted final coefficient');need(A[0]>0 and Bv[1]>0,'nonzero exceptional directions')
 det=[(A[0]+z)*Bv[1]-A[1]*Bv[0] for z in [zlo,zhi]];det2=[fq((q(A[0])+q(z))*q(Bv[1])-q(A[1])*q(Bv[0])) for z in [zlo,zhi]];need(det==det2 and det[0]<=det[1] and det[0]>0,'two exact monotone affine endpoints');hypothesis(A,Bv,lam,nu,mu,det[0])
 ar=(ai(A[0])+ai(zlo).union(ai(zhi)))*ai(Bv[1])-ai(A[1])*ai(Bv[0]);ziv=ii(zlo)+iv.mpf([0,1])*ii(zhi-zlo);ir=(ii(A[0])+ziv)*ii(Bv[1])-ii(A[1])*ii(Bv[0]);bounds={'arb320':[fq(ar.lower().fmpq()),fq(ar.upper().fmpq())],'iv110':list(map(endpoint,ir._mpi_))};window=[F('5.859714459e-15'),F('5.859714461e-15')]
 for name,(lo,hi) in bounds.items():need(window[0]<lo<=det[0]<=det[1]<=hi<window[1],name+' directed positive inclusion')
 piece=[]
 for s in [F(0),F(1,8),F(7,3),F(200)]:
  a=t0+s;b=fq(q(t0)+q(s));need(a==b,'shifted polynomial identity');piece.append({'s':str(s),'KP_polynomial':str(a),'TAU_polynomial':'1'})
 # Independent simple examples check the rounding and strict-gap predicates, not the analytic limit itself.
 ties=[F(1)+F(1,2**53),F(1)+F(3,2**53),-F(1)-F(1,2**53),-F(1)-F(3,2**53),F(1,2**1075),F(3,2**1075),F(2)**-1022-F(1,2**1075),F(7,3)]
 for x in ties:need(rn(x)==rn2(x)==F(float(x)),'nearest-even manufactured case')
 guards=[]
 def case(name,fn,reject):
  try:fn()
  except ValueError:
   need(reject,'unexpected rejection '+name);guards.append({'name':name,'result':'EXPECTED_REJECTION'})
  else:
   need(not reject,'invalid input accepted '+name);guards.append({'name':name,'result':'VALID_CONTROL'})
 case('finite IEEE zero',lambda:ieee(bytes(8)),False)
 for name,b in [('IEEE inf',struct.pack('<Q',2047<<52)),('IEEE nan',struct.pack('<Q',(2047<<52)|1)),('short IEEE word',bytes(7))]:case(name,lambda b=b:ieee(b),True)
 case('finite iv zero',lambda:endpoint(iv.mpf(0)._mpi_[0]),False)
 for n,x in [('iv inf',iv.inf),('iv negative inf',-iv.inf),('iv nan',iv.nan)]:case(n,lambda x=x:endpoint(x._mpi_[0]),True)
 case('valid strict gap',lambda:hypothesis([F(1)],[F(0),F(1)],F(-3),F(-2),F(-4),F(1)),False)
 bad=[('zero A',[F(0)],[F(0),F(1)],-3,-2,-4,1),('zero B',[F(1)],[F(0),F(0)],-3,-2,-4,1),('no lower gap',[F(1)],[F(0),F(1)],-3,-2,-3,1),('no upper gap',[F(1)],[F(0),F(1)],-3,-3,-4,1),('zero determinant',[F(1)],[F(0),F(1)],-3,-2,-4,0)]
 for name,a,b,l,n,m,d in bad:case(name,lambda a=a,b=b,l=l,n=n,m=m,d=d:hypothesis(a,b,F(l),F(n),F(m),F(d)),True)
 need(len(guards)==14 and sum(x['result']=='EXPECTED_REJECTION' for x in guards)==11,'all guards actually executed');need(F(-4)<F(-3)<F(-2),'manufactured canonical exponent -3 lies strictly between finite low rate -4 and rounded high rate -2')
 out={'start_utc':start,'utc':now(),'status':'PASS_CANONICAL_SCALING_EXTERIOR_NONMEMBERSHIP_REQUIRES_ACTUAL_REVIEW','counts':{'manual_and_numpy_dyadics':sum(len(a) for a in arrays.values()),'integer_metadata_identities':1,'full_Aout_hex_two_parsers':len(aout),'leading_source_identities':len(A),'literal_B_recipe':len(expected),'exact_and_rounded_rates_each_two_methods':len(exact)+len(literal),'rate_bound_comparisons':len(low),'determinant_endpoints_two_exact_methods':len(det),'directed_affine_enclosures':len(bounds),'piece_shift_cases_two_exact_methods':len(piece),'rounding_manufactured_cases':len(ties),'guard_cases':len(guards),'guard_rejections':sum(x['result']=='EXPECTED_REJECTION' for x in guards)},'parents':parents,'proof_review':review,'source_sha256':SH,'normalization_sha256':ZH,'vector_sha256':VH,'Mh':mh,'stride':{'explicit_recipe_parameter':16,'stored_in_vector_metadata':False,'tail_argument_independent_of_stride':True},'k_exact':str(k),'t0_exact':str(t0),'Z_exact':[str(zlo),str(zhi)],'first_A_exact':list(map(str,A[:3])),'first_B_exact':list(map(str,Bv[:2])),'canonical_A0_range':[str(A[0]+zlo),str(A[0]+zhi)],'lambda_exact':str(lam),'nu_literal_exact':str(nu),'nu_minus_lambda_exact':str(nu-lam),'mu_exact':str(mu),'lambda_minus_mu_exact':str(lam-mu),'scaling_factor_exact':str(1-k),'exact_rates':list(map(str,exact)),'literal_rates':list(map(str,literal)),'all_twenty_lower_rates':list(map(str,low)),'determinant_exact_range':list(map(str,det)),'directed_determinant_enclosures':{n:list(map(str,z)) for n,z in bounds.items()},'strict_positive_decimal_window':list(map(str,window)),'piece_shift_cases':piece,'manufactured_rounding_inputs':list(map(str,ties)),'guards':guards,'manufactured_gap_example':{'mu':'-4','lambda':'-3','nu':'-2','meaning':'exp(-3s) is o(exp(-2s)), but cannot be a finite polynomial-exponential sum with rates at most -4; analytic statement proved in PROOF.md, not numerically tested'},'files':dict(sorted(pins.items())),'seconds':time.monotonic()-tic,'scope':'Exact distinguished normalized K_star is in neither the mathematical-rate nor literal-rate exterior span built from frozen A/B and finite strictly lower rates. Actual stored B retained; no canonicalized/free-tail span, norm closure/distance, historical assembly, ideal projection, coercivity, physical forcing norm, inverse, X3 distance, nonlinear closure or decisive endpoint.'}
 rehash(pins);write(E/'checks.json',out);print(json.dumps({k:out[k] for k in ['utc','status','counts','nu_minus_lambda_exact','lambda_minus_mu_exact','strict_positive_decimal_window','seconds']}))
if __name__=='__main__':main()
