# Exact cusp functionals and the new constrained hydrostatic trials

Result229. Written before the coefficient and residual audit. This result concerns
finite trial functions and necessary far-field identities of the auxiliary
hydrostatic equation. It proves no existence or nonexistence for SettingIII.

## Full cusp functional of a finite angular trace

Fix0<p<1. Let

    f(x,y)=r^p*sin(theta)*sum_(k=0)^(M-1) b_k*cos(2k*theta),
    Q=f_xx(0,1), K=f(0,1), r=sqrt(x^2+y^2).

The b_k are real and the sum finite. Define the full finite part

    Cp=lim_(S->infinity)[int_0^S t*f_xx(1,t)dt-Q*S^p/p].             (1)

The limit exists: smoothness of the angular trace near the vertical axis gives
f_xx(1,t)=Q*t^(p-2)+O(t^(p-4)), so the subtracted tail is integrable. It also
converges near zero. No finite cutoff is substituted for infinity in this definition.

There is a closed form with an exact rational kernel when p and b_k are rational.
Put beta=(p+2)/2, alpha=(1-p)/2, and

    w_k = sum_(j=0)^k (-1)^j*binom(2k,2j)*(3/2)_j*(-beta)_(k-j)
                                                        /(alpha)_k,
    Fp = (p+1)*(p+2)/2 * B(3/2,-beta).

Then

    Cp=Fp*sum_k b_k*w_k.                                          (2)

The beta value is its analytic continuation. No pole occurs for0<p<1, and Fp>0
since Gamma(-beta)>0 for1<beta<3/2 and the other gamma arguments are positive.
In particular w0=1 and w1=-(p+5)/(1-p).

To prove(2), let h(t)=f(1,t). Homogeneity gives
f_xx(1,t)=p*(p-1)*h-2*(p-1)*t*h'+t^2*h''. Two integrations by parts yield

    int_0^S t*f_xx(1,t)dt
      =(p+1)*(p+2)*int_0^S t*h(t)dt
          +S^3*h'(S)-(2p+1)*S^2*h(S).                           (3)

The boundary at zero vanishes because h=O(t). Its expansion at infinity is
h=K*t^p+L2*t^(p-2)+O(t^(p-4)). The displayed boundary terms have only powers
S^(p+2),S^p and negative powers, with no constant since0<p<1. Taking the finite
part in(3) proves Cp=(p+1)*(p+2)*FP int_0^infinity t*h(t)dt.

For the k-th mode,

    h_k(t)=t*(1+t^2)^((p-1)/2-k)
                    *sum_(j=0)^k (-1)^j*binom(2k,2j)*t^(2j).

The finite part of each integral is
B(j+3/2,k-j-beta)/2. This follows by v=t^2/(1+t^2) and subtracting the two possible
divergent endpoint powers. Equivalently it is the continued beta integral;
its parameters avoid nonpositive integer poles. Dividing by B(3/2,-beta) gives
exactly(3/2)_j*(-beta)_(k-j)/(alpha)_k by the gamma recurrence. Substitution proves(2).
This derivation is independent of finite cutoff quadrature and of the producer's
functional row. A second check can differentiate each monomial directly and
integrate its three terms by beta values.

For stored local-basis data, let P be the exact binary map exponent, p=1-1/P,
C=L/2^P and q_k(t)=sum_j a_kj*T_j(t), with the a_kj reconstructed exactly from
stored local nodes as in result227. Then b_k=C^(1/P)*sum_j a_kj. The positive
factor C^(1/P) is common. Thus the sum in(2) can be evaluated in exact rational
arithmetic before one gamma factor and one positive real power are applied.
This avoids cancellation in a floating point sum of separately approximated rows.
It does not prove that any trial solves the transport equation.

## Finite cutoff error and a manufactured zero

The difference between(1) and its S-truncation is

    Cp-Cp(S)=int_S^infinity [t*f_xx(1,t)-Q*t^(p-1)]dt
             =O(S^(p-2)).                                        (4)

Consequently meeting a row defined at S=1e4 need not set the full functional to
zero. The coefficient in(4) depends on the trace and may be large at high angular
resolution. It must be computed or bounded. A finite-cutoff row may be a useful
approximation, but it is not the exact full-plane condition without a tail check.

The smooth angular trace with b0=(p+5)/(p+2) and b1=(1-p)/(p+2), divided by an
optional common normalization, has Cp=0 by w1 above. More precisely, the normalized
manufactured trace from result197 has b0=(p+5)/(2*(p+2)) and
b1=(1-p)/(2*(p+2)); its vertical value b0-b1 is1. Both versions give the same zero.
The normalized trace equals
sin(theta)*[3*cos(theta)^2+(p+2)*sin(theta)^2]/(p+2), whose full inverse was
independently verified previously. This supplies a known zero for the exact kernel.

## A convergent tail series with an explicit remainder bound

Put H(u)=f(sqrt(u),1)=sum_(ell>=0) A_ell*u^ell for |u|<1. The finite angular formula gives

    A_ell=sum_k b_k sum_(m=0)^min(k,ell)
       (-1)^(k-m)*binom(2k,2m)*binom((p-1)/2-k,ell-m).

Consequently Q_ell=2*ell*(2*ell-1)*A_ell, Q_1=Q, and for S>1,

    Cp-Cp(S)=sum_(ell>=2) Q_ell*S^(p-2*ell+2)/(2*ell-p-2).       (6)

The expansion follows by homogeneity, f_xx(1,t)=t^(p-2)*f_xx(1/t,1), and termwise integration of a power series on t>=S>1. For an explicit bound choose R0=1/4 and put

    M0=sum_k |b_k|*(1-R0)^((p-1)/2-k)
                     *sum_(m=0)^k binom(2k,2m)*R0^m.

The branch (1+u)^((p-1)/2-k) is analytic on |u|<1; on |u|=R0 its modulus is at most (1-R0)^((p-1)/2-k). Thus Cauchy's coefficient estimate gives |A_ell|<=M0/R0^ell. For a truncation through ell=L>=2, let q=1/(R0*S^2)<1. Since 2*ell*(2*ell-1)/(2*ell-p-2)<=4*ell for ell>=3, the remainder in (6) has absolute value at most

    4*M0*S^(p+2)*q^(L+1)*[(L+1)-L*q]/(1-q)^2.                 (7)

This is an analytic bound for the exact coefficients. Floating evaluations of its value remain finite-precision estimates unless enclosed by interval arithmetic. No such rounding enclosure is claimed here.

For an independent check of (2), differentiate each monomial of h_k before taking its finite part. Set n=2*(k-j), a=(p-1)/2-k and R=1+t^2. Its contribution to f_xx(1,t), before the factor (-1)^j*binom(2k,2j), is

    t^(2j+1)*[n*(n-1)*R^a+2*a*(2*n+1)*R^(a-1)
                                  +4*a*(a-1)*R^(a-2)].

After multiplication by t, each term integrates to one half of B(j+3/2,k-j-beta+s), for s=0,1,2 respectively. This separately differentiated formula has the same finite part (1), and supplies an independent multiprecision cross-check of the rational kernel.

## Why a small nonzero r2 prevents the stated infinite-radius limit

Assume0<p<1/2, c=1/p, K>0 and the smooth expansions established for the saved
finite basis in result227. On the positive vertical axis,

    G(y)=K*y^p+c2*y^(2p-1)+O(y^(3p-2)),
    V2(0,y)=Q/[p*(1-p)]*y^p+m0+O(y^(2p-1)).

Termwise differentiation is justified by the smooth compactified formula. For
the positive-sign hydrostatic residual R=(c*y+V2)*G'-G,

    R(y)=r2*y^(2p-1)+p*K*m0*y^(p-1)+O(y^(3p-2)),
    r2=[c*(2p-1)-1]*c2+K*Q/(1-p).

At large y, G and(c*y+V2)*G' are positive, so Nf is their sum. Since p<1/2,
expanding this denominator gives

    y*R/Nf = r2/(2*K)*y^p+p*m0/2+o(1).                          (5)

Thus a nonzero r2 prevents convergence to p*m0/2, however small it is. Several
finite values near that constant establish no limit. With exact saved binary P,
cp-1 also need not vanish; the leading residual K*(cp-1)*y^p must then be retained.
The exact formula includes that term, whose effect eventually supersedes(5).

Moreover Cp=0 alone cannot force r2=0 for arbitrary smooth trial fields. Add

    eta(x,y)=epsilon*y*r^2*(1+r^2)^(p-2).

This perturbation is smooth, even in x, odd in y, and has zero first derivative
at the origin. It also leaves the hydrostatic center strain unchanged. Indeed,
write F(s)=s*(1+s)^(p-2); then eta_xx(0,y)=2*epsilon*y*F'(y^2), and its integral
from zero to infinity is epsilon*[F(infinity)-F(0)]=0 because p<1. Its far degree
is2p-1, so it changes neither the leading trace nor K,Q,Cp, while its axis
coefficient c2 changes by epsilon. Hence r2 changes by
[c*(2p-1)-1]*epsilon=-(c-1)*epsilon, which is nonzero. Any observed reduction in
r2 after imposing a cusp row is a property of those numerical solves, not an
identity between the two independent conditions.

## Audit plan and dependencies

Freeze the new hsH64/96 numeric inputs, reconstruct coefficients independently,
and use the same own Cartesian analytic jets, complete vertical inverse,
774 physical probes, three quadrature settings and maximizing-point witnesses
as result227. Recompute exact centers, cubic residuals, true Cp via(2), Q,c2,r2,
m0, and finite-axis ratios. Use the known trace zero and direct monomial beta
integrals as manufactured checks. Check finite-cutoff tails separately. All large
coefficient data are exact JSON certificates, not manually written numeral tables.

Dependencies: ../hydrostatic_resolved_map_audit/PROOF.md for reconstruction,
residuals and the full auxiliary inverse; ../hydrostatic_axis_core_moment/PROOF.md
for m0; ../hydrostatic_cusp_trace/PROOF.md for the manufactured trace. New inputs
and dated checks belong under verification/. The principal endpoint remains OPEN.
