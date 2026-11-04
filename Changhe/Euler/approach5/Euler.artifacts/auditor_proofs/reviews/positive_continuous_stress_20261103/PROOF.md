# Positive pressure at a continuous stress zero

## 1. Exact statement

Let v:B_R(0)->R3 and P:B_R(0)->R be continuous and satisfy div div(v tensor v+P I)=0 in distributions on B_R. Assume |v(x)|<=C|x|^m near0 for some C<infinity and m>0. Put pi=P-P(0). If

    pi(x)>=delta |v(x)|²

on a full neighborhood for one fixed delta>1/(2m), then v=0 and P=P(0) on a neighborhood. In particular, if v has infinite value vanishing order at0, any fixed delta>0 suffices. This confirms the later Section5 refinement of LIT250 at continuous regularity. It imposes no momentum, homogeneity, rotation or helicity premise.

The strict positive constant matters even in the smooth divergence-free pressure-pair class: Section4 constructs a nonzero infinitely flat pair with P(0)=0 and P>0 off0, but no uniform positive lower bound for P/|v|². That pair is not a similarity tail or a full Euler solution.

## 2. Distributional radial identity and proof

With normalized sphere averages, let

    E(r)=average |v(rn)|², A(r)=average (v(rn).n)²,
    q(r)=average pi(rn), Y=q+A.

Then 0<=A<=E=O(r^(2m)), all functions are continuous and Y(0)=0. Testing the stress equation against a radial psi supported in(0,R) gives

    integral [r²Y psi''+r(E-3A+2Y)psi']dr=0.

Thus -r²Y'+r(E-3A)=K in distributions, for a constant K. Since (E-3A)/r is integrable at0 and Y is bounded there, the possible K/r primitive forces K=0. Consequently

    Y(r)=integral_0^r (E(t)-3A(t))/t dt,
    rY'=E-3A, Y=O(r^(2m)).                              (1)

In particular Y is C1 away from0. The normalized pressure inequality implies Y>=delta E+A>=delta E>=0. Therefore

    rY'=E-3A<=E<=Y/delta.

It follows that r^(-1/delta)Y is nonnegative and nonincreasing. Its limit at0 is zero because 2m>1/delta and (1) holds. Hence it vanishes identically. E=0 follows, so v=0 on each sufficiently small sphere and on the ball by continuity. Then q=0, and pi>=0 pointwise with zero sphere average forces pi=0. This proves both asserted conclusions without differentiating P.

For infinite flatness, given delta>0 choose m>1/(2delta) and the corresponding finite-order estimate. No uniform control of the estimates as m varies is required.

## 3. Same-regularity ratio bounds

Assume additionally P(0)=0, H=|v|²/2-P>=0 on a full neighborhood and v=0 on {H=0}. Let v have infinite value order and be supported at0, meaning it is nonzero in every neighborhood. Define Rratio=|v|²/H only on {H>0}.

If liminf_(x->0,H>0) Rratio>2, then on a sufficiently small neighborhood of0 within {H>0}, Rratio>=Rstar>2 for some fixed Rstar. There

    P=(1/2-1/Rratio)|v|²>=(1/2-1/Rstar)|v|².

At H=0 both v and P vanish, so the undivided inequality extends to the full neighborhood. Section2 applies with delta=1/2-1/Rstar>0 and contradicts support. Thus

    liminf_(x->0,H>0) Rratio<=2.

The already checked negative-pressure result A1614-A1617 supplies limsup>=2/3 at exactly the same continuous-stress regularity and zero-set scope. These are statements about limits over {H>0}, not a pointwise confinement of the ratio or a convergence assertion. The two-sided local gap relevant to the coupled tail equations remains open.

## 4. A smooth divergence-free endpoint countertest

This independent example tests only replacement of delta>0 by nonnegative pressure. Let Jx=e3 cross x, r=|x|, mu=x3/r, and for r>0 define

    Omega(r)=exp(-1/r²), f(r)=Omega(r)²,
    I1(r)=integral_0^r s f(s)ds,
    I4(r)=integral_0^r s^4 f(s)ds,
    L2(mu)=(3mu²-1)/2,
    v(x)=Omega(r)Jx,
    P(x)=(2/3)[I1(r)-r^(-3)I4(r)L2(mu)].                (2)

Set v(0)=0 and P(0)=0. The flat exponential dominates every inverse power, and the integral derivatives have the same property. In particular I4(r)/r^5 is a smooth radial flat function after extension at0. Rewriting its contribution as a multiple of I4(r)r^(-5)(3x3²-r²) proves that (2) extends to C-infinity fields, with all derivatives flat at0.

Since Jx is tangent to spheres and tr J=0, div v=0. Put rho²=x1²+x2². The advective derivative is (v.grad)v=Omega² J²x=-f(x1,x2,0), because v.grad Omega=0. Consequently

    tr((Dv)²)=div((v.grad)v)=-2f-(f'/r)rho²,
    -tr((Dv)²)=2f+(2/3)r f'-(2/3)r f' L2(mu).          (3)

For P=p0(r)+p2(r)L2(mu), formula (2) gives p0=(2/3)I1 and p2=-(2/3)r^(-3)I4. Direct differentiation yields

    p0''+2p0'/r=2f+(2/3)r f',
    p2''+2p2'/r-6p2/r²=-(2/3)r f'.                     (4)

Equations (3)-(4) prove -Delta P=tr((Dv)²) off0; smoothness extends the equality through0. Thus div div(v tensor v+P I)=0 on the full ball, with divergence freedom as well.

For every r>0, r^(-3)I4<I1, since s^4/r³<s for0<s<r and f>0. As L2(mu)<=1, equation (2) gives P>0 everywhere off0. The velocity is nonzero off the rotation axis, so this is a supported infinitely flat nonzero pressure pair with nonnegative normalized pressure.

It has no uniform delta>0. On the equatorial plane, P=(2/3)(I1+I4/(2r³))<=I1, whereas |v|²=r²f. Since f'=4f/r³,

    I1(r)=integral_0^r (s^4/4) f'(s)ds<=r^4 f(r)/4.

Hence along that plane 0<P/|v|²<=r²/4, which tends to zero. The strict positive comparison constant in the infinite-flatness theorem therefore cannot be replaced by zero even in its smooth divergence-free pressure-pair subclass.

This construction does not test the full ratio hypotheses of Section3: on the rotation axis v=0 and P>0, so H<0 there. It has no twisted homogeneity and no asserted momentum equation. It does not refute any incompressible rotating similarity theorem or establish sharpness of the finite-order constant.

## 5. Verification and remaining scope

All six sections of the revised LIT250 source were read and compared with A1614-A1621. The only new source theorem is the continuous positive-pressure extension. Sections2-3 give its complete independent proof; Section4 is an exact divergence-free endpoint test with every Poisson derivative displayed. No numerical computation, external theorem or build is needed.

Pressure normalization, a full-neighborhood inequality, strict constants and supported zero-set conditions are indispensable parts of the statements. The main bare-decay conjecture and the coupled local ratio gap remain open. Comparison proceeds through existing configured model working files, with runtime identity unattested and no new client or agent.
