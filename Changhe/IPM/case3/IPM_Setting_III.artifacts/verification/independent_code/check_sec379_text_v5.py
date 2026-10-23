"""Result226 follow-up: three exact repairs, independent local residues and corner."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
from html.parser import HTMLParser
class TextReader(HTMLParser):
 def __init__(self):super().__init__();self.parts=[]
 def handle_data(self,x):self.parts.append(x)
def htmltext(path):
 r=TextReader();r.feed(path.read_text());return ' '.join(' '.join(r.parts).split())
import mpmath as mp
R=Path('research/sec379_text_audit');V=R/'verification/v5';mp.mp.dps=70
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
flat=lambda t:' '.join(t.split())
checks=[];rows=[]
def check(name,ok,evidence=None):checks.append(dict(name=name,passed=bool(ok),evidence=evidence))
for row in json.loads((V/'INPUTS.json').read_text())['files']:
 if 'frozen'in row:check('frozen '+Path(row['frozen']).name,sha(row['frozen'])==row['sha256'])
g=json.loads((R/'verification/v4/CHECKS.json').read_text());check('prior52gate',g['status']=='PASS'and g['count']==52)
for f,n in [('body_sha256','body.txt'),('app_sha256','app.txt')]:check('prior exact '+n,g[f]==sha(R/'verification/v4'/n))
oldb=flat((R/'verification/v4/body.txt').read_text());newb=flat((V/'body.txt').read_text())
olda=flat((R/'verification/v4/app.txt').read_text());newa=flat((V/'app.txt').read_text())
breps=[('extension of such a solution does not satisfy (1)','extension of a solution with h\'(0+) != 0 does not satisfy (1)')]
areps=[('X = 0 as the residues at sigma = k and 1 - b_1 + k,','X = 0 as minus the sum of the residues at sigma = k and 1 - b_1 + k,'),('< 0, the residue at sigma = 0.)','< 0, minus the residue at sigma = 0, since the upward contour closes clockwise to the right.)')]
for kind,old,new,reps in [('body',oldb,newb,breps),('appendix',olda,newa,areps)]:
 for a,b in reps:
  check(kind+' unique replacement '+a,old.count(a)==1 and new.count(b)==1);old=old.replace(a,b)
 check(kind+' entire normalized diff accounted',old==new)
for clause in ['The symmetry, the sign of K and the statement in (c) on the solutions of (1) are exact','the derivation of (1) as the leading inner problem is formal','proves no nonexistence']:
 check('scope retained '+clause,clause in newb)
for clause in ['Moving the contour to the left','expansion of u_G as the sum of these residues','relative residuals below 1e-20','h = h(0+) E + h\'(0+) E_1 on z > 0 by uniqueness']:
 check('unchanged clause '+clause,clause in newa)
for name,pts,sign in [('right',[(0,-1),(0,1),(1,1),(1,-1)],-1),('left',[(0,-1),(0,1),(-1,1),(-1,-1)],1)]:
 area=sum(pts[i][0]*pts[(i+1)%4][1]-pts[(i+1)%4][0]*pts[i][1]for i in range(4))/2
 check('upward '+name+' oriented area',sign*area>0,area)
for p in [mp.mpf(1)/4,mp.mpf(1)/3,mp.mpf(3)/4]:
 a1=-p/2;a2=(1-p)/2;b1=p/(p+1);X=mp.mpf('0.4')
 I=lambda s:mp.gamma(-s)*mp.gamma(1-b1-s)*mp.gamma(a1+s)*mp.gamma(a2+s)*X**s/mp.gamma(2+s)
 c0=mp.gamma(1-b1)*mp.gamma(a1)*mp.gamma(a2)/mp.gamma(2)
 cO=mp.gamma(a2)*mp.gamma(1-b1+a2)*mp.gamma(a1-a2)/mp.gamma(2-a2)
 check(str(p)+' constant and odd signs',c0<0 and cO<0)
 for name,center,radius,exact in [('right0',mp.mpf(0),min(p/2,a2,1-b1)/12,-c0),('leftodd',-a2,min(a2,mp.mpf('.5'))/8,cO*X**(-a2))]:
  vals=[]
  for N in [32,64]:
   vv=mp.fsum(I(center+radius*mp.exp(2j*mp.pi*k/N))*radius*mp.exp(2j*mp.pi*k/N)for k in range(N))/N
   err=abs(vv-exact)/max(1,abs(exact));check(str(p)+' '+name+' circle'+str(N),err<mp.mpf('1e-20'),float(err));vals.append(mp.nstr(vv,35))
  rows.append(dict(p=mp.nstr(p,30),pole=name,residue=mp.nstr(exact,35),circle32=vals[0],circle64=vals[1]))
for k in range(6):
 e=mp.mpf('1e-35');v=e*mp.gamma(-(mp.mpf(k)+e));expected=mp.mpf((-1)**(k+1))/mp.factorial(k)
 check('Gamma(-s) residue '+str(k),abs(v-expected)<mp.mpf('1e-32'))
for B in [-2,0,3]:
 phi2=lambda x:(4*x*x-2)*mp.exp(-x*x)
 weak=2*mp.quad(lambda x:B*x*phi2(x),[0,1,mp.inf])
 check('corner weak second derivative '+str(B),abs(weak-2*B)<mp.mpf('1e-60'))
check('zero solution explicitly allowed',breps[0][1]in newb)
for sec,word in [('5.2','of residue'),('16.17','negative sense')]:
 check('primary source '+sec,word in htmltext(V/('DLMF_'+sec+'.html')))
out=dict(status='PASS'if all(c['passed']for c in checks)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,rows=rows,body_sha256=sha(V/'body.txt'),app_sha256=sha(V/'app.txt'),proof_sha256=sha(R/'REVISION5_PROOF.md'),driver_sha256=sha(__file__),scope='Three repaired sentences and their complete diff; prior theorem evidence retained, no PDE endpoint.')
(V/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['count']);print([c for c in checks if not c['passed']])
if out['status']!='PASS':raise SystemExit(1)
