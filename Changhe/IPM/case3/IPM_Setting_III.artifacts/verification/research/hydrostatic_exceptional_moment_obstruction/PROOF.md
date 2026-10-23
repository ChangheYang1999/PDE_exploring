# Exceptional polynomial axis exponents and positive moments

Result258. Written 2026-10-21 before supporting code. Independently reconstructed from the lead's proposed polynomial-coordinate argument, with an additional completed-square proof that replaces its degree-nine elimination. The lead's frozen notes are evidence of the proposed claim, not proof of it.

## Statement and dependencies

Let C>0, P>1, H a nonzero real polynomial with H(0)=0, k a real polynomial, w=1-t^2, y=Ct w^(-P) for 0<t<1 and G(y)=yH(w(t(y))). Suppose on a nonempty open interval of positive y there are a differentiable V and a real c satisfying V_y=k(w) and (cy+V)G_y=G. Write H=w^n h, n>=1, h(0)!=0, and let m be the odd degree of F(t)=Ct h(1-t^2).

Then necessarily P=n+m/2, with odd m>=11. Thus no such identity exists for 1<P<13/2, or for non-half-integer P>1. More precisely, in the polynomial coordinates below every surviving case has delta=1, e>=2 and unequal nonzero-root multiplicities. In the case e=2, one pair of nonzero roots must have strictly smaller multiplicity than the other two pairs. This last condition describes only a necessary configuration; it does not assert that it exists.

We use the already independently proved result253 only for P=n+m/2 and m>=5. Its full hypotheses are restated above. Everything from that reduction onward is proved here. This is an auxiliary finite polynomial-axis result. It excludes neither a nonpolynomial axis trace nor a limit of increasing degree, and gives no full-plane IPM NO endpoint.

## Polynomial coordinate and logarithmic derivative

Put x=t/sqrt(w), s=1+x^2 and N=P-1/2=n+(m-1)/2. Then

    Y=Cx s^N,    Y'=C s^(N-1) q,    q=1+2P x^2.

If F(t)=sum_j f_j t^(2j+1), define

    Psi(x)=x sum_j f_j x^(2j) s^((m-1)/2-j).

Direct substitution gives G=Psi. Its leading coefficient is F(1)!=0, so its degree is exactly m. Also Psi(i)=f_((m-1)/2) i^m !=0 and similarly at -i: every other summand has a positive power of s. Thus no root of Psi is ±i. This explicit fact is needed for the pole argument.

On a smaller open interval where Psi' is nonzero, E:=cY+V=Psi Y'/Psi'. Therefore E'/Y'-c=k(1/s). All displayed quantities are rational functions of x, so interval equality gives a rational identity. In particular E'/(s^(N-1)q) has no finite poles except possibly ±i.

Let u_*=-1/(2P), beta=i/sqrt(2P). At a root alpha of Psi' which is not a root of Psi, if alpha is neither ±i nor ±beta, E has a pole and differentiation produces a higher-order pole not canceled by division by s^(N-1)q. If alpha=±beta and its multiplicity in Psi' is at least two, multiplication by the simple q zero leaves a pole of E; differentiation and division by q again produce a pole. Hence any uncanceled critical roots are only ±i, of some common multiplicity e>=0, and ±beta, of common multiplicity delta=0 or1. A root of Psi contributes a simple pole to Psi'/Psi, regardless of its multiplicity in Psi. Parity and reality give

    Psi'/Psi = m s^e (x^2-u_*)^delta / R(x),
    R(x)=x prod_(k=1)^r (x^2-u_k),
    deg R=2e+2delta+1.

Here R is the monic radical of Psi, all u_k are distinct and nonzero, none is -1, and whenever delta=1 none is u_*. The coefficient m follows from Psi'/Psi~m/x. Let A0 be the odd positive multiplicity of the zero root of Psi and Ak=2mu_k the even positive multiplicity of its kth nonzero pair. In u=x^2 the identity is

    g(u):=m(1+u)^e(u-u_*)^delta/[u prod_k(u-u_k)]
         = A0/u+sum_k Ak/(u-u_k),    A0+sum Ak=m.       (1)

Reality ensures that nonreal u_k and their residues occur in conjugate pairs.

## The case delta=0 is impossible

Here E=(C/m)R q s^(N-1-e). Evaluating the numerator of E'/(s^(N-1)q) at x=beta gives R(beta)q'(beta)s(beta), times a nonzero constant. Thus R(beta)=0, and u_* is one of the poles of g. Both u_* and 0 are real poles with positive residues. Choose two consecutive real poles in the compact interval [u_*,0]. The rational function g is real and continuous between them; it tends to +infinity from the right of the left pole and to -infinity from the left of the right pole. It has a zero between them by the intermediate value theorem. But (1), with delta=0, has no zero except possibly -1<u_*. Contradiction. Nonreal poles do not affect continuity or the endpoint signs on this interval.

## Conditions for delta=1

Now r=e+1, R(beta)!=0 and E=(2PC/m)R s^(N-1-e). The sole extra pole condition away from ±i is

    [R' s+2(N-1-e)xR](beta)=0.

Divide by R(beta), multiply by beta, and use R'/R=1/x+sum 2x/(x^2-u_k) and 1+(2N+1)u_*=0. This gives

    sum_k (1+u_k)/(u_*-u_k)=0.                        (2)

Set v_k=1/(1+u_k), z=1/(1+u_*)=2P/(2P-1)>1, pi(v)=prod_(k=1)^(e+1)(v-v_k). The v_k are distinct, nonzero, different from1, and different from z. Each summand in (2) equals -z/(z-v_k). Thus (2) is precisely pi'(z)=0.

The zero of order e of g at u=-1 gives the moment equations

    M_l=A0+sum Ak v_k^l=0,   1<=l<=e.                 (3)

Indeed 1/(u-u_k)=-v_k sum_(j>=0)[v_k(u+1)]^j near u=-1. The coefficient of (u+1)^(l-1) in g is -M_l. With Phi(v)=(v-1)pi(v), the rational function g in the v coordinate has numerator of degree at most2 and vanishes at v=0. Its linear coefficient is fixed by g~mv there; its quadratic coefficient is fixed by g~-M_(e+1)v^(-e) at infinity. Consequently

    g=v[m Phi(0)-M_(e+1)v]/Phi(v),
    M_(e+1) z=(-1)^e m prod_k v_k.                    (4)

These are necessary conditions. Only (2)-(4) are used below.

## Excluding e=0 and e=1

If e=0, pi is monic linear and pi'(z)=1, impossible.

If e=1, write a=A0,b=A1,d=A2, m=a+b+d. Equation pi'(z)=0 gives v1+v2=2z, and M1=0 gives a+bv1+dv2=0. If b=d this says a+2bz=0, impossible. Otherwise solve the two linear equations and substitute into M2 z=-m v1v2 from (4). Multiplying by -(b-d)^2 produces exactly

    (a+(b+d)z)[a m-4bd z(z-1)]=0.

The first factor is positive, hence am=4bd z(z-1). Since 2P=2n+m>=m+2,

    z(z-1)=2P/(2P-1)^2 <= (m+2)/(m+1)^2,
    4bd <= (m-a)^2 < m^2.

It follows that a < m(m+2)/(m+1)^2 <1, contradicting a>=1. This proof also covers nonreal possibilities: the stated algebra is over the complex numbers and its final factors use only the real positive residues and z.

## Excluding equal nonzero multiplicities for every e

If all Ak=b>0, then (3) says sum v_k^l=-a with a=A0/b>0 for 1<=l<=e. As formal power series,

    prod(1-v_k t)=exp[-sum_(l>=1)(sum v_k^l)t^l/l]
                =(1-t)^(-a)+O(t^(e+1)).

The coefficients c_l for 0<=l<=e are (a)_l/l!>0. Since pi(v)=sum_(l=0)^(e+1)c_l v^(e+1-l), its derivative for v>0 is

    pi'(v)=sum_(l=0)^e(e+1-l)c_l v^(e-l)>0,

contradicting pi'(z)=0. This includes squarefree nonzero roots and does not require the v_k themselves to be real.

## A completed square for three nonzero root pairs

Suppose e=2, so there are three v_k. If all three are real then M2=A0+sum Ak v_k^2>0, impossible. Hence there is one real root x and a nonreal conjugate pair v2,v3, whose residues must agree. Write a=A0>0, b for the residue at x, and d for the common residue of v2,v3. Put S=v2+v3 and T=v2v3. The first two moments give

    S=-(a+bx)/d,
    T=[a+b x^2+d S^2]/(2d).

For pi(v)=(v-x)(v^2-Sv+T), substitution and completion of the square yield, when b>d,

    pi'(z) = b(b-d)/(2d^2) [x+(a+2dz)/b]^2
             +(1+2d/b)z^2+2az/b+a/(2d)+a^2/(2bd).    (5)

Every term is nonnegative and the last four are strictly positive for z>0. Thus pi'(z)>0, impossible. If b=d, the equal-multiplicity argument already applies. Every remaining e=2 configuration therefore has b<d. Formula (5) is valid for every positive a,b,d with b!=0; positivity uses b>d. No elimination, root approximations or integer scan is needed for this exclusion.

## Degrees five, seven and nine

Since R is the radical, deg R=2e+3<=m. At m=5 only e<=1 is possible, already excluded. At m=7 the remaining possibility e=2 requires A0=1 and all three mu_k=1, excluded by equal multiplicities. At m=9, e=3 requires A0=1 and all four mu_k=1, again excluded. If e=2, the only possibilities are A0=3 with all mu_k=1, or A0=1 with mu=(2,1,1). The former has equal multiplicities; the latter has one larger multiplicity. In the latter case reality forces the uniquely larger-multiplicity root to be real, or all three roots real. Both were excluded above. This proves m>=11.

For comparison with result254, the transformation preserves each finite root multiplicity: a factor t^(A0) prod(t^2-tau_k)^mu_k of F transforms to x^(A0) prod((1-tau_k)x^2-tau_k)^mu_k of Psi. No tau_k=1 because F(1)!=0, and the map tau -> tau/(1-tau) is injective. Thus this theorem is compatible with the squarefree and distinct-root restrictions in result254; it strengthens their small-degree exclusion.

## Scope and verification

No statement for degree11 or larger is deduced from the lead's finite elimination outputs here. No root location, monotonicity, analyticity or sign assumption has been added to the finite polynomial hypotheses. The incomplete principal PDE remains open. Supporting exact tests will check the coordinate map, pole reductions, moment transform, e=1 factorization, completed square, equal-weight formal coefficients, and enumeration through degree9. Such tests support the displayed proof rather than substitute for its all-degree arguments.
