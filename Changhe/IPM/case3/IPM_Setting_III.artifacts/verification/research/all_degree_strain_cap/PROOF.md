# The first nonlinear Taylor term under a strain cap

Date: 2026-10-20. Status: independent reconstruction of the all-degree claim;
implementation verification is recorded separately. This is a conditional
result. No global bound on strain is proved for the primary class.

## Statement and notation

Let rho,psi,U be an exact smooth primary Setting III profile. Write ell>1,
D=ell-1, A=2ell-1, B=A-1>0, a=rho_y(0)!=0, h=rho-ay,
phi=psi+Dxy, v=(-phi_y,phi_x), and sigma=sup|sym DU|_op. Suppose
sigma<=D. If h has a first nonzero Taylor term of degree n=2K+1>=3, then

    a >= (n-1)A.                                            (1)

In particular a>0. If a<2A, or if a<0, then h is flat at the origin.
Flatness means all Taylor coefficients vanish. It does not mean that h
vanishes on an open set or globally.

More precisely, consider just the homogeneous linear equations for the two
leading terms and the necessary strain sign (phi_(n+1))_xy>=0. A nonzero
compatible pair satisfying that sign exists if and only if a>=(n-1)A.
This last sufficiency concerns polynomial jets only, not exact profiles.
The gradient sign a(h_n)_y<=0 follows from this strain sign and compatibility.
The gradient sign alone does not imply (1); a rational degree-five
counterexample is given below.

## Reduction from the exact equation

The center identity gives U=(Dx,-Dy)+v and W=ell X+U. Exact transport yields

    W.grad h-h=-a phi_x,  -Delta phi=h_x.                    (2)

If h=O(r^n) in its smooth Taylor expansion, (2) gives phi_x=O(r^n).
Oddness in x permits integration from x=0, proving phi=O(r^(n+1)).
All lower Taylor coefficients then vanish, so v=O(r^n) as well. This uses
smooth Taylor coefficients, not differentiation of an arbitrary O remainder.
The first nonzero homogeneous terms obey

    (A x partial_x+y partial_y-1)h_n=-a partial_x phi_(n+1),
    -Delta phi_(n+1)=partial_x h_n.                         (3)

The symmetric strain has the exact matrix

    S11=D-phi_xy, S22=-S11, S12=(phi_xx-phi_yy)/2.

The cap forces |S11|<=D, hence phi_xy>=0 everywhere. In particular its
first nonzero homogeneous term is nonnegative. In fact this last local
nonnegativity suffices for the Taylor theorem; the global cap is only one
way to obtain it.

Set N=n-1=2K and e_j=N+2Bj. Expand

    h_n=sum_(j=0)^K alpha_j x^(2j)y^(n-2j),
    phi_(n+1)=sum_(j=0)^K beta_j x^(2j+1)y^(n-2j).

Comparing coefficients in (3) gives

    alpha_j=-a(2j+1)beta_j/e_j,
    (2j+2)(2j+3)(e_(j+1)-a)beta_(j+1)
       =-(n-2j)(n-2j-1)e_(j+1)beta_j.                     (4)

Every e_j is positive, so the first division is harmless. Define

    g_j=(2j+1)(n-2j)beta_j,
    P(t)=sum g_j t^j, Q(t)=sum (g_j/e_j)t^j.

Then phi_xy=y^N P(x^2/y^2), while a(h_n)_y=-a^2 y^N Q(x^2/y^2).
The axis values are obtained by continuity of the homogeneous polynomials.
The strain sign is exactly P>=0 on [0,infinity). Moreover

    Q(t)=integral_0^1 s^(N-1)P(s^(2B)t)ds,                (5)

so that sign implies Q>=0. This proves the asserted implication to the
gradient condition without needing a separate global gradient argument.

## A positive integral that excludes every subthreshold jet

Put eta=1+K/B>1 and chi=1+(N-a)/(2B). Equation (4) becomes

    (2j+2)(2j+1)(j+chi)g_(j+1)
      =-(N-2j)(N-2j-1)(j+eta)g_j.                       (6)

Its solution is, up to a common scalar, the polynomial

    F_chi(t)=sum_(j=0)^K (-1)^j binom(2K,2j)
                      (eta)_j (chi+j)_(K-j)t^j,         (7)

where (z)_j is the rising factorial, with empty product 1. Formula (7)
has a nonzero top coefficient for all real chi and satisfies (6) without
dividing by j+chi.

Here is the complete treatment of dimension, including resonances. If
chi is not 0,-1,...,1-K, recurrence from g_0 determines the solution.
If chi=1-l, 1<=l<=K, the row j=l-1 forces g_(l-1)=0 because j+eta>0.
Earlier rows give g_0=...=g_(l-1)=0, g_l is free, and later rows determine
the rest. Thus the space is one dimensional in every case and (7) spans it.

Suppose a<NA, equivalently chi>1-K. Set u=chi+K-1>0. Consider two
positive variables t>0, 0<s<1 with product probability density proportional to

    t^(u-1)(1+t)^(-u-K-1/2) s^(-1/2)(1-s)^(eta-3/2).     (8)

Each factor is integrable and positive in its open interval. The product
z=ts assigns positive mass to every open subinterval of (0,infinity).
Beta integration, or a substitution followed by integration by parts,
gives the exact moments for 0<=j<=K:

    E(t^j)=(-1)^j(u)_j/(1/2-K)_j,
    E(s^j)=(1/2)_j/(eta)_j.                             (9)

The denominator in the first expression never vanishes because it consists
of nonzero half integers. The tail of the t density has exponent -K-3/2,
so moments through K, including absolute polynomial integrals, are finite.
Since

    binom(2K,2j)=(-K)_j(1/2-K)_j/((1/2)_j j!),

(7)-(9) yield

    E F_chi(ts)=sum_(j=0)^K (-1)^j binom(K,j)
                            (chi+j)_(K-j)(chi+K-1)_j=0. (10)

For completeness, away from zeros of (chi)_K(chi)_(K-1), the sum equals

    (chi)_K/(chi)_(K-1)
      *sum_(j=0)^K (-1)^j binom(K,j)(chi+j)_(K-1).

The last sum is the Kth finite difference of a polynomial in j of degree
K-1, and is zero. The original expression in (10) is polynomial in chi,
so the identity holds also at every exceptional chi. Thus no resonant
parameter is lost in the cancellation.

If a nonzero scalar multiple of F_chi were nonnegative on [0,infinity),
its integral against the positive measure (8) would be strictly positive:
it is positive on some open interval and integrable. Equation (10) rules
this out for either common scalar sign. This proves (1).

At a=NA=e_K, the resonant solution has only g_K nonzero, and g_K>0 works.
For a>NA, all factors e_(j+1)-a are negative. Choosing g_0>0 in (4)
makes every g_j>0. Formula (5) also gives the gradient sign. This proves
the precise sufficiency statement about homogeneous polynomial signs.

## An independent degree-five countertest for the gradient shortcut

Take ell=19, A=37, B=36, a=-2 and n=5. Define

    h_5=y^5/10-(2/39)x^2y^3+(38/2925)x^4y,
    phi_6=xy^5/5-(76/117)x^3y^3+(2812/14625)x^5y.

Exact differentiation verifies both equations (3). Here

    P(t)=1-(76/13)t+(2812/2925)t^2,
    Q(t)=1/4-t/13+(19/2925)t^2.

The discriminant of Q is -22/38025<0 and its leading coefficient is
positive. Thus Q>0 on the real line and a(h_5)_y<0 away from the origin.
This also makes |grad(-2y+h_5)|<=2 on a sufficiently small ball: its
strictly negative homogeneous degree-four correction dominates the
homogeneous degree-eight square term uniformly in angle.

However P(1)=-11363/2925<0, while a=-2<4A. The strain sign fails.
These polynomial fields satisfy only the leading linear equations; their
nonlinear transport residual begins in degree nine and their growth is
inadmissible at infinity. They refute a gradient-only jet proof, not any
assertion about global exact capped profiles.

## Consequences, dependencies and scope

Either a smooth h has a first nonzero Taylor degree, or it is flat. This
is an exhaustive dichotomy without analyticity. Result61 proves for flat
h that sigma>=ell-|a|/2, using the full-plane weighted inverse at arbitrarily
large odd weights. Combining it with (1) excludes exact profiles with
sigma<=D and |a|<2. For a<0, the cap forces flat h and |a|>=2. A separate
sharpening of the limiting weighted constant can strengthen the flat
alternative; it is not assumed in this proof.

The local conclusion is stronger in another direction: if a<2A and an
exact profile is not flat, its strain exceeds D arbitrarily close to zero.
Indeed its nonnegative-jet alternative has just been excluded, so the
leading phi_xy is negative in some direction, and S11=D-phi_xy>D on a
short segment of that ray. This is strict but gives no universal size
for the excess.

The Taylor proof depends only on the exact center identity, smoothness,
parity and equations (2). The flat consequence additionally uses result61,
whose whole-plane weighted integrability and harmonic uniqueness are stated
there. Under spatial dilation, a,A,D,sigma are unchanged and both leading
coefficient arrays are multiplied by the same positive factor lambda^(1-n).
All signs, thresholds and flatness statements are dilation invariant.
No bound sigma<=D is derived for the primary class, and no principal NO
or existence conclusion follows. Implementation checks use independently
written rational polynomial operations and positive moment sums; they are
additional checks of this informal proof, not formal verification.

Verification update 2026-10-20T20:15:16.231038+00:00: independent implementation checks passed2026-10-20T20:13:40Z. Exact counts and rational evidence are in verification/checks.json. Verdict CONFIRMED with the conditional scope above.
