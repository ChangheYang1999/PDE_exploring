# Bounded vorticity: the derivative growth gap and transverse mean decay

## 1. Exact hypotheses and conclusions

Let 0<c<1, omega be any finite real number, Jx=(-x2,x1,0), A=cI-omega J and L=(1-c)I+omega J. Let U in C2(R3;R3), P in C1(R3) satisfy

    div U=0, LU+DU(Ay+U)+grad P=0,
    U(y)->0 uniformly as |y|->infinity,
    |U(y)|<=C_U(1+|y|)^(-a), 0<=a<=3/2,
    |curl U(y)|<=W0 outside a fixed ball.

Compact regularity also bounds curl U on the omitted ball. Set k=min(1+a,1/c)>=1. If |DU|<=C(1+|y|)^delta for one 0<=delta<k, then DU is bounded, DU->0, and |DU|+|curl U|=O(1/r). For 1/3<c<1, also DU=O(r^(-1/c)). Thus the extended-real limsup of log|DU|/log r is either at most -1 or at least k, taking log0=-infinity.

Independently of the derivative-growth premise, define outside a large ball

    G=DU, W=curl U, B=Ay+U, e=B/|B|, Pi=I-e tensor e,
    T=Pi G Pi, g=Pi G^T e, h=Ge, sigma=W.e.

For a>0, T and G-e tensor g have the quantitative L2 mean bounds in Section5. For a=0, they still tend to zero in L2 on unit balls and in every finite Ls there, as Sections6-7 prove. No conclusion of pointwise derivative decay follows from these mean bounds alone. Constants may depend on c, omega and the fixed profile.

## 2. The local Holder argument has the claimed wider premise list

The full independent A757 proof was reread, especially its Section4. Put delta1=max(delta,1/2). Then delta1<k and c delta1<1. Use physical variables tau=1-t, s=-log tau, y=exp(sA)x, Q_s=exp(omega sJ),

    u=tau^(c-1)Q_s U(y), xi=tau^(-1)Q_s W(y).

On a fixed annulus, |grad u|+|xi|<=C tau^(-1-c delta1) and |u|<=M tau^(c-1), M=sup|U|. The local proof uses only these bounds, compact C2 regularity and c delta1<1. Neither the stronger velocity decay of the full A757 theorem nor delta1<=5/4 enters that section.

More explicitly its nested physical balls have r0(t)=1/4+(2M/c)tau^c. Pair paths ending in the inner ball remain in earlier larger balls, with margin d(q,t)=(M/c)((1-q)^c-tau^c). A local Biot-Savart split and harmonic remainder give the Holder integral inequality for Theta=[xi]_(1/2,B(xstar,r0(t))). The inhomogeneous term contains w0²(v^(-1/2)(1+|log v|)), with w0²<=C tau^(-2-2c delta1); its exponent is below four. The loose upper bound C tau^-6 used in A757 therefore still applies. The transport exponential is at most exp(C tau^(-c delta1)). Gronwall gives

    Theta(t)<=C tau^-6 exp(C tau^(-c delta1)).       (1)

This derivation uses no bounded-vorticity hypothesis yet. The case M=0 is trivial and avoids the zero-margin convention.

## 3. Exact rescaling activates the confirmed transverse theorem

For every exterior y, choose tau=|y|^(-1/c) and xstar=exp(-sA)y on the unit sphere. The map x->exp(sA)x is a rotation followed by dilation tau^(-c), so it maps B(xstar,1/4) exactly onto B(y,|y|/4). Also W(y)=tau Q_s^(-1)xi(x,t). Therefore

    [W]_(1/2,B(y,|y|/4))
      =tau^(1+c/2)[xi]_(1/2,B(xstar,1/4)).

Combining with (1) yields log(2+[W]_(1/2))<=C|y|^delta1+C log|y|. Choose delta1<p_H<k. The confirmed Theorem TV, A1223, applies with Holder exponent 1/2 and logarithmic exponent p_H. Its exact other premises are the uniform velocity decay, the a bound and bounded exterior vorticity already assumed. It gives every derivative conclusion in Section1.

If the limsup exponent is below k, choose a nonnegative delta strictly between it and k and absorb the compact ball into the constant. This gives the growth premise. Conversely bounded DU activates TV and gives O(1/r). Under the natural tail in 2/5<c<1/2, a=1/c-1 and k=1/c. No vorticity smallness threshold is changed by this reformulation.

## 4. Exact pointwise tensor identities and actual pressure

The pressure is C2, since its gradient equals -LU-GB and is C1. Taking divergence gives -Delta P=tr(G²): the two rotational terms cancel, and div U=0 removes the linear c trace. In an oriented orthonormal frame with e=e3,

    G=((t11,t12,h1),(t21,t22,h2),(g1,g2,h3)),
    sigma=t21-t12.

Consequently tr(T²)=|T|²-sigma² and tr(G²)=tr(T²)+2g.h+(e.h)². The general matrix identity tr(G²)=|G|²-|curl U|² gives

    |T|²=-Delta P+sigma²-2g.h-(e.h)²,
    |G|²-|W|²=-Delta P,
    |G-e tensor g|²=|T|²+|h|².                  (2)

The last equality uses G-e tensor g=T+h tensor e and T e=0, so its Frobenius cross term vanishes. All identities are exact and use no slowly varying frame approximation.

## 5. Quantitative L2 means when a>0

For |y|=r large and 0<rho<=r/2, the ball B(y,rho) lies between radii r/2 and 3r/2. Gauss applied to (2) gives

    mean_B |T|² <=(3/rho)sup_boundaryB|grad P|
                   +sup_B(sigma²+2|g||h|),
    mean_B |G|² <=mean_B |W|²+(3/rho)sup_boundaryB|grad P|.       (3)

The independent pressure lemma A1228 gives |grad P|<=Cr^(-a)log²(2+r). As |B|>=cr/2, actual momentum gives |h|<=Cr^(-1-a)log²(2+r). The exact curl decomposition gives |g|<=|W|+|h|, hence g is bounded on the exterior.

Fix 0<a1<a and nu=min(1+a1,1/c). Then h=O(r^(-1-a1)). Along the complete exterior carrier characteristics,

    B.grad sigma=-sigma+W.h+W.Pi h.

The source has magnitude at most 2W0|h|. Every exterior point reaches a fixed sphere backward in finite time; the radius ratio is comparable to exp(c times elapsed time). Integrating damping one from that sphere gives |sigma|<=Cr^(-nu)log(2+r), with the logarithm covering the resonance c(1+a1)=1. This is the already checked TV Step3, and it uses no Holder premise.

Substitution into (3), with L_r=log(2+r), proves

    mean_B |T|² <=C r^(-a)L_r²/rho
                  +C r^(-1-a)L_r²+C r^(-2nu)L_r²,
    mean_B |G|² <=mean_B |W|²+C r^(-a)L_r²/rho.       (4)

The same first bound holds for mean |G-e tensor g|² because |h|²=O(r^(-2-2a)L_r^4) is absorbed by the second term. Unit-radius, fixed-relative-radius and uniform rho>=1 consequences follow directly. This verifies Lemma TP at its entire stated quantitative scope.

## 6. Additional qualitative extension to bare uniform velocity decay

Now retain a=0, so no positive power rate is imposed. A1228 still gives grad P->0 uniformly. Actual momentum then gives h=o(1/r), while g remains bounded. In the scalar characteristic equation above, first use |h|<=C/r and c<1 to get sigma=O(1/r). More precisely start on a sphere where |h|<=epsilon/r. Integrating the source gives at most C epsilon/r because the damping gap is 1-c>0. The fixed-sphere term is O(r^(-1/c))=o(1/r). Let r tend to infinity and then epsilon to zero. Thus sigma=o(1/r).

Put epsilon_P(r)=sup_(|z|>=r/2)|grad P(z)| and epsilon_h(r)=sup_(|z|>=r/2)|z||h(z)|. Both tend to zero. The same Gauss inequality gives, uniformly for 1<=rho<=r/2,

    mean_B |T|² <=3 epsilon_P(r)/rho
                   +o(r^-2)+C epsilon_h(r)/r ->0.

The identical qualitative conclusion holds for G-e tensor g. Also mean |G|²-mean |W|²<=3 epsilon_P(r)/rho tends to at most zero uniformly over those radii. Hence the structural mean decay survives under bare uniform velocity decay and bounded vorticity, although no rate is supplied. This does not make W or DU pointwise small.

## 7. Finite-exponent norm decay and its precise analytic dependency

For any center y, cut off W smoothly in B(y,4), equal to W on B(y,3), and let v be its Biot-Savart potential. The degree-minus-two velocity kernel gives |v|<=C||W||infinity on B(y,2). Since -Delta U=curl W, the difference U-v is harmonic on B(y,3), with uniformly bounded size on B(y,2), so its gradient is bounded on B(y,1).

For every 1<s<infinity, the derivative of the Biot-Savart potential is a finite sum of homogeneous degree-zero Fourier multipliers, smooth away from zero. Their symbols are bounded combinations of xi_i xi_j/|xi|². The precise standard dependency is the Ls boundedness of such multipliers: Terence Tao, Lecture notes4 for UCLA247A, Theorem4.4 and the Riesz-transform application, pages19-21, with Corollary2.10 on page9. These primary pages and the preceding Calderon-Zygmund proof were read; the PDF is pinned under verification. Applying that theorem to the compactly supported bounded cutoff vorticity gives a uniform Ls bound for Dv, hence for DU on every unit ball.

For 1<=s<=2, L2 decay of T and G-e tensor g gives Ls decay by the finite-volume Holder inequality. For 2<s<infinity, interpolate their L2 decay with the uniform Lq bound for any q>s. The multipliers e and Pi have norm at most one; no derivatives of these coefficients enter this interpolation. Thus both tensors tend to zero in every finite Ls on unit balls, including the qualitative a=0 case. This uses no false L-infinity boundedness of a singular integral.

## 8. A complete proof of the claimed pointwise-method comparison

The source's TP pointwise sufficient condition is H(r)=[T]_(beta,B(y,1))=o(r^(a beta)log^(-2beta)r), 0<beta<=1. Optimizing the small-ball bound in (4) proves that this condition forces T(y)->0. Its asserted containment in TV.4 is also valid, but a sharper elementary interpolation makes the whole 0<c<1 range transparent.

The unit-ball L2 bound for T and its Holder seminorm give, for 0<rho<=1,

    |T(y)|²<=C rho^-3+C H(r)²rho^(2beta).

Choose rho=min(1,H(r)^(-2/(2beta+3))). Then |T(y)|<=C(1+H(r)^(3/(2beta+3))). Since g and h are bounded, the same growth bound holds for |G(y)|. Under the stated TP condition this gives

    |G(y)|=O(r^delta0), delta0=3a beta/(2beta+3)<=9/10<1<=k.

The numerical fraction follows only from a<=3/2 and beta<=1; no approximation is involved. Thus TV.4 already gives pointwise decay. This argument avoids assuming a beta<k, which is not automatic for the source's full c range. No new pointwise class is obtained by the TP optimization.

## 9. What remains open

The one-scale or liminf-envelope version in source Section4 is not proved. Its enlarged spatial balls require values of a derivative envelope beyond the evaluation radius; a subsequence upper bound does not directly supply the global polynomial barrier used in Sections2-3. Neither the mean estimates nor the standard Ls bounds eliminate that issue. The vorticity threshold also remains unchanged. No nonexistence result is claimed from C52 alone.

## 10. Verification and model comparison

The full C52 source, the complete independent A757 proof and the relevant C51 pressure and characteristic arguments were read and checked. Sections2-5 confirm the submitted main theorem and lemma; Section6 adds the a=0 qualitative result, Section7 verifies the finite-exponent remark with a precise primary analytic dependency, and Section8 completes its method comparison at the full stated c range. No symbolic test was rerun because exact hand calculations resolve the questions. The existing configured model Theory Agent A 's proof is the received collaboration for C52; comparisons of the additional Sections6 and8 are requested through the existing agents. Provider runtime remains unattested, and no new client or agent is used.
