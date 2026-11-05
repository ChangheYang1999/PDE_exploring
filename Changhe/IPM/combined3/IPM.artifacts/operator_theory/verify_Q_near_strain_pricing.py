#!/usr/bin/env python3
"""Closed-Gamma, whole-plane near-strain pricing for G=W J^q g.

This is a Q-norm certificate; no old-N low-band price is transferred.
"""
import argparse,math,json
from fractions import Fraction as F
from pathlib import Path
from flint import arb,ctx

def aa(x):
    x=F(x);return arb(x.numerator)/arb(x.denominator)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--scale',default='2');ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--D',default='4/5');ap.add_argument('--Ds',default='1/10');ap.add_argument('--ey',default='1/200')
    args=ap.parse_args();ctx.prec=256;pi=arb.pi();q=aa(F(21,10));s=aa(F(137,125));nu=aa(F(1,40));scale=aa(F(args.scale))
    ell=arb(8).log()/(2*pi.sqrt())
    def Imom(p):return arb(8)**aa(F(p,2))*(p*p*ell*ell/4).exp()*(p*ell/(2*arb(2).sqrt())).erfc()/p
    A0=s*(2*pi*scale**2*Imom(2)).sqrt()
    A1=s*(2*pi*(scale**2*Imom(2)+4*scale**4*Imom(4))).sqrt()
    A2=s*(2*pi*scale**6*Imom(6)).sqrt()
    L=arb(8000000);assert L>=1000000
    # Gaussian derivative maxima used in the smooth input cutoff proof.
    ee=arb(1).exp()
    assert (2/ee).sqrt()<1 and 4/ee+2*arb(2).sqrt()<5
    assert 8*aa(F(3,2))**aa(F(3,2))*(-aa(F(3,2))).exp()+12*(-aa(F(1,2))).exp()<12
    assert 2/ee<aa(F(3,4))
    assert 4*aa(F(3,2))**aa(F(3,2))*(-aa(F(3,2))).exp()+2*(-aa(F(1,2))).exp()<3
    assert 32/(ee*ee)+12*arb(2).sqrt()/ee<11
    assert 2+1/L+aa(F(3,2))<4
    assert 6+10/L+5/L**2<7
    assert 60+18/L+52/L**2+12/L**3<61
    def E(p,lam):
        p=arb(p)
        return lam**(p+1)/4*arb(2)**(-(p+1)/4)*((p+1)/4).gamma()
    def FF(beta,p,lam):
        beta=arb(beta);p=arb(p)
        if beta<=0:return E(p,lam)
        C=arb(1) if beta<=1 else arb(2)**(beta-1)
        return C*(E(p,lam)+E(p+2*beta,lam))
    def Finteger(j,p):
        if j<0:return E(p,nu)
        return sum((math.comb(j,k)*E(p+2*k,nu) for k in range(j+1)),arb(0))
    def round_up(v):
        assert v.is_finite()
        n=int(float(v.mid()))+1;assert v<n;return n
    # Very-low R kernel K=R exp(-(|xi|/nu)^4), before Jq is applied.
    norms=[E(2*j+1,nu)/(2*pi) for j in range(4)]
    weighted=[None]
    for j in range(1,4):
        V=((j*j+j+1)*E(2*j-1,nu)-8*j/nu**4*E(2*j+3,nu)+16/nu**8*E(2*j+7,nu))/(2*pi)
        assert V>0
        weighted.append((A1*A1*norms[j]+4*A0*A0*V).sqrt())
    P0=(A1*A1*norms[0]+A0*A0*(aa(F(9,50))/pi+128/pi*(L*nu).log()+32/pi)).sqrt()
    # ||D^l(W exp(-r²/L²))||infty <= 4,7,61 for l=1,2,3.
    T=[P0]
    M=[None,arb(4),arb(7),arb(61)]
    for j in range(1,4):
        T.append(weighted[j]+A0*sum((math.comb(j,l)*M[l]*norms[j-l].sqrt() for l in range(1,j+1)),arb(0)))
    H2=(T[0]**2+2*T[1]**2+T[2]**2).sqrt()
    H3=(T[0]**2+3*T[1]**2+3*T[2]**2+T[3]**2).sqrt()
    lowR=H2**aa(F(9,10))*H3**aa(F(1,10))
    eta=(8*A2*A2*norms[0]/L**4+128*A0*A0/(pi*L**2)).sqrt()
    eta_upper=F(11,1000000);assert eta<aa(eta_upper)
    # A direct H2/H3 product estimate for a nonsingular low correction.
    # |b|<=C r^d, |b'|<=D r^(d-1). Angular tensor rank is one or two.
    def finite_low_W(j,d,C,D,angular=1):
        C,D=aa(C),aa(D)
        I=C*C*Finteger(j,2*d+1)/(2*pi)
        V=(3*j*j*C*C*Finteger(j-2,2*d+3)+(3*D*D+angular*C*C)*Finteger(j,2*d-1)+48*C*C/nu**8*Finteger(j,2*d+7))/(2*pi)
        return (A1*A1*I+4*A0*A0*V).sqrt()
    def finite_low_L(j,d,C):return (aa(C)**2*Finteger(j,2*d+1)/(2*pi)).sqrt()
    def product_price(W2,Wg,L0,L1,L2):
        P2=W2+A0*(4*L1+8*L0)
        Pg=Wg+A0*(2*L2+4*L2+16*L1+32*L0)
        P3=(P2*P2+Pg*Pg).sqrt()
        return P2**aa(F(9,10))*P3**aa(F(1,10))
    def correction(d,C,D):
        W2=finite_low_W(2,d,C,D)
        Wg=finite_low_W(2,d+1,C,F(C)+F(D),2)
        LL=[finite_low_L(j,d,C) for j in range(3)]
        return product_price(W2,Wg,*LL)
    # nR=R-mR, |m|<=r, |m'|<=1;
    # pR=R-(1-p)R, 1-p<=r²/2, |(1-p)'|<=r.
    correction_n=correction(1,F(1),F(1))
    correction_p=correction(2,F(1,2),F(1))
    lowP=lowR+correction_p;lowN=lowR+correction_n
    # Quartic mid-band K=R(psi_mu-psi_nu), optionally multiplied by p or n.
    def weighted_mid(beta,d,mu,angular=1):
        i0=FF(beta,1,mu)
        ider=2*d*d*FF(beta-1,1,mu)+64*(FF(beta,7,mu)/mu**8+FF(beta,7,nu)/nu**8)
        # At beta=0 use r^-1<=1 on r>=1, avoiding the false E(-1) pole.
        ep=max(2*beta-1,arb(0))
        iang=(1+nu*nu)**beta/8+arb(2)**beta*((1/nu).log()+E(ep,mu))
        return (A1*A1/(2*pi)*i0+2*A0*A0/pi*(ider+angular*iang)).sqrt()
    rows=[]
    for mm in [10,12,16,20]:
        mu=arb(mm);prices=[];raw=[]
        for name,order,d2,d3,low in [('n',2,2,3,lowN),('p',1,1,2,lowP),('R',0,2,3,lowR)]:
            W2=weighted_mid(arb(2-order),arb(d2),mu)
            Wg=weighted_mid(arb(3-order),arb(d3),mu,2)
            LL=[(FF(arb(j-order),1,mu)/(2*pi)).sqrt() for j in range(3)]
            v=low+product_price(W2,Wg,*LL);prices.append(round_up(v));raw.append(str(v))
        an,apc,ar=prices;ey=F(args.ey);D=F(args.D);Ds=F(args.Ds);qr=F(21,10);sr=F(137,125)
        assert ey>0 and D>0 and Ds>0
        eh=qr*sr*(F(2,mm*mm)+F(1,4*mm**4))
        et=eh+8*qr*eta_upper+ey;es=qr*sr/F(mm*mm)+2*qr*eta_upper
        ct=qr*qr*F(an+apc+ar)**2/D+qr*qr*F(an)**2/ey
        cs=qr*qr*F(apc)**2/Ds
        rows.append({'mu':mm,'A_n_A_p_A_R_upper':prices,'A_values_arb':raw,'TIS_rate':str(et),'TIS_C':str(ct),
                     'sandwich_rate':str(es),'sandwich_C':str(cs),'combined_rate':str(et+es),'combined_C':str(ct+cs),'p_damping_used':str(D+Ds)})
    out={'status':'Q_NEAR_STRAIN_PRICING_CERTIFICATE_PASS','scope':'G=W J^q g, q=21/10; no N-to-Q lowband transfer',
         'strain_scale':args.scale,'nu':'1/40','D':args.D,'Ds':args.Ds,'ey':args.ey,'smooth_input_cut_L':'8000000','A0_arb':str(A0),'A1_arb':str(A1),'A2_arb':str(A2),
         'low_R_price_arb':str(lowR),'low_p_correction_arb':str(correction_p),'low_n_correction_arb':str(correction_n),
         'low_R_p_n_upper':[round_up(lowR),round_up(lowP),round_up(lowN)],'eta_arb':str(eta),'eta_upper':str(eta_upper),'cases':rows,
         'profile_numeric_input':'inherited global ||S||infty,op<=137/125','stationary_existence':'NOT CLAIMED'}
    args.output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
