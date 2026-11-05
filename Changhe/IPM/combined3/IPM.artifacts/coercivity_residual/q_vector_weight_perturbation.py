"""Certified L2 distance for a genuine Q-source test vector.

Phi=R J^(-1/10)psi and PhiQ=R[W^-1 J^(-1/10)psi], W=sqrt(1+4r²).
Since 0<=1-W^-1<=2r², ||PhiQ-Phi||₂<=2||r²J^(-1/10)psi||₂.
The latter squared norm is an exact finite Tricomi-U combination derived by
Fourier differentiation. This file does not claim a completed Q residual bound.
"""
import argparse,json,math
from datetime import datetime,timezone
from hashlib import sha256
from pathlib import Path
from flint import arb,fmpq as Q,fmpq_poly as Poly,ctx


def calculate(width='3/200',bits=384):
    ctx.prec=bits;a=Q(width);A=a*a;p=Q(1,20);s=Poly([0,1]);P=2-A*s
    lam=A/2;d=P.derivative()-lam*P
    dd=P.derivative().derivative()-2*lam*P.derivative()+lam*lam*P
    L=[8*d+4*s*dd,-8*p*P-8*p*s*d,4*s*p*(p+1)*P]
    total=arb(0);terms=[]
    for i in range(3):
        for j in range(3):
            poly=s*L[i]*L[j];v=2*p+i+j;part=arb(0)
            for k,coefficient in enumerate(poly):
                if coefficient:
                    # U(alpha,beta,z)=Gamma(alpha)^-1 * integral_0^inf
                    # exp(-zt)t^(alpha-1)(1+t)^(beta-alpha-1)dt.
                    alpha=k+1;beta=Q(k+2)-v
                    part+=arb(coefficient)*math.factorial(k)*arb(A).hypgeom_u(alpha,arb(beta))
            total+=part;terms.append({'i':i,'j':j,'polynomial':list(map(str,poly)),'integral':part.str(70)})
    norm2=arb(a**4)/2*total;assert norm2>0
    distance=2*norm2.sqrt()
    return {'status':'CERTIFIED_Q_VECTOR_L2_DISTANCE_UPPER','width':str(a),'bits':bits,
        'r_squared_J_minus_delta_psi_norm_squared':norm2.str(80),
        'vector_distance_upper':distance.upper().str(80),
        'identity':'PhiQ=R[W^-1 J^(-1/10)psi]; <R(WJ^(21/10)F),PhiQ>=<F,(1-Delta)psi>',
        'derivation':'Fourier hhat=i*a²/sqrt(pi)*kappa*sin(theta)*f(kappa²), f=(2-a²s)exp(-a²s/2)(1+s)^(-1/20); Delta(kappa*sin(theta)*f(s))=kappa*sin(theta)*(8fprime+4s*fsecond).',
        'scope':'L2 distance and exact test identity only; an actual Q matrix residual coordinate/Gram certificate remains separate.',
        'terms':terms,'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'finished_utc':datetime.now(timezone.utc).isoformat()}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--width',default='3/200');ap.add_argument('--bits',type=int,default=384);args=ap.parse_args()
    result=calculate(args.width,args.bits);args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items()if k!='terms'},indent=2),flush=True)
if __name__=='__main__':main()
