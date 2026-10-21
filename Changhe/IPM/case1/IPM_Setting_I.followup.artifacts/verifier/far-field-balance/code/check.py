from pathlib import Path
from datetime import datetime,timezone
import sys,json,hashlib
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'inverse/code'))
from collocation import NodalDensity
root=Path(__file__).resolve().parents[1]

def angular_data(source,n):
 d=NodalDensity(source);theta=np.arange(n)*2*np.pi/n;c=np.cos(theta);sine=np.sin(theta);sq=d.map_inverse(np.arctan2(abs(sine),abs(c)));m=np.arange(d.M)
 modes=2*m[:,None]*sq;bc=d.co.sum(axis=0);bqc=2*np.sum(np.arange(d.N+1)[:,None]**2*d.co,axis=0)
 b=bc@np.cos(modes);bq=bqc@np.cos(modes);bth=((-2*m*bc)@np.sin(modes))*np.sign(c*sine)/(1+d.beta*np.cos(2*sq))
 k=d.k;F=d.L**(3-k)*c*c*sine*b;Fp=d.L**(3-k)*((c**3-2*c*sine*sine)*b+c*c*sine*bth);G=-d.L**(4-2*k)*c*c*sine*bq
 source_theta=k*c*F-sine*Fp;wave=np.fft.fftfreq(n,d=1/n);phat=np.fft.fft(source_theta)/(wave*wave-(k+1)**2);P=np.fft.ifft(phat).real;Pp=np.fft.ifft(1j*wave*phat).real
 ur=-Pp;ut=(k+1)*P;H=k*ur*F+ut*Fp;D=(1-d.cl)*G+H
 den=abs(F)+d.cl*(abs(c*(k*c*F-sine*Fp))+abs(sine*(k*sine*F+c*Fp)))
 return d,{'theta':theta,'F':F,'Fp':Fp,'G':G,'P':P,'Pp':Pp,'ur':ur,'ut':ut,'H':H,'D':D,'den':den}

def at(theta,values,targets):
 # Periodic Fourier interpolation, using an independently assembled trigonometric sum.
 n=len(values);w=np.fft.fftfreq(n,d=1/n);hat=np.fft.fft(values)/n
 return np.real(np.exp(1j*np.asarray(targets)[:,None]*w)@hat)

inputs=[('manufactured',Path('verifier/far-field-trace/verification/manufactured.npz')),('dnSB',Path('numerics/data/dnSB_n120m48.npz')),('dnR8',Path('numerics/runs/dnR8_n120m48.npz')),('dnB96',Path('verifier/grid-states/data/dnB_n96m40S.npz')),('dnCS2',Path('verifier/grid-states/data/dnCS2_n120m48.npz')),('physical_s2_t0p5',Path('verifier/physical-correction/data/physical_s2_t0p5.npz'))]
targets=[.3,1.,1.55];rows=[]
for tag,source in inputs:
 refinements=[];old=None;fine=None
 for n in [2048,4096,8192,16384]:
  d,a=angular_data(source,n);item={'n':n,'D_max_abs':float(np.max(abs(a['D']))),'D_l2_circle':float(np.sqrt(np.mean(a['D']**2))),'F_max_abs':float(np.max(abs(a['F']))),'G_max_abs':float(np.max(abs(a['G']))),'sampled_D':at(a['theta'],a['D'],targets).tolist()}
  if old is not None:item['nested_max_D_change']=float(np.max(abs(a['D'][::2]-old['D'])))
  if tag=='manufactured':
   theta=a['theta'];p=(15/128)*np.sin(2*theta)-(5/208)*np.sin(4*theta);pp=(30/128)*np.cos(2*theta)-(20/208)*np.cos(4*theta)
   item['manufactured_P_error']=float(np.max(abs(a['P']-p)));item['manufactured_Pp_error']=float(np.max(abs(a['Pp']-pp)))
   assert item['manufactured_P_error']<1e-12 and item['manufactured_Pp_error']<1e-12
  refinements.append(item);old=a;fine=a
 np.savez_compressed(root/'verification'/(tag+'_angular.npz'),**fine)
 samples={key:at(fine['theta'],fine[key],targets).tolist() for key in ['F','G','ur','ut','D','den']}
 row={'tag':tag,'source':str(source),'source_md5':hashlib.md5(source.read_bytes()).hexdigest(),'cl':d.cl,'k':d.k,'L':d.L,'targets':targets,'samples':samples,'refinements':refinements};rows.append(row)
 print(tag,'Dmax',refinements[-1]['D_max_abs'],'nested',refinements[-1].get('nested_max_D_change'),'Dtargets',samples['D'],flush=True)
 out={'date':datetime.now(timezone.utc).isoformat(),'scope':'independent angular homogeneous inverse and first subleading transport balance; floating calculations, not interval certificates','rows':rows}
 (root/'verification/summary.json').write_text(json.dumps(out,indent=2)+'\n')
