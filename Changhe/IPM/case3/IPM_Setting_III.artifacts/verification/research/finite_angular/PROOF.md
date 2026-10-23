# No exact profile with finite angular Fourier support

Status: independently derived, reviewed by the actual claude-opus-5-5 endpoint, and checked again by the verifier. This is a restricted nonexistence result, not a NO endpoint for the primary problem.

## Statement

Let rho be a smooth function on the whole plane, even in x and odd in y, satisfying

    |rho(X)|+(1+|X|)|grad rho(X)| <= C(1+|X|)^gamma,
    0<gamma<1.

The canonical velocity means div U=0, curl U=-partial_x rho, the parity induced by an odd-odd stream function, and U=o(|X|) at infinity. Let psi be that stream function, so U=(-psi_y,psi_x) and -Delta psi=partial_x rho. Suppose, for a real constant c_l,

    (c_l X+U).grad rho=rho.

If there is a finite odd integer N>=1 such that

    rho(r,theta)=sum_(k=1,3,...,N) b_k(r) sin(k theta)

for all r>0, then rho is identically zero. The statement does not require rho_y(0)!=0, c_l>1, or a sign condition. It does require a single finite upper angular cutoff valid at every radius. It does not exclude a smooth profile with infinitely many angular modes or rule out accurate finite-mode approximations to such a profile.

## Canonical mode uniqueness

The stream function has only even sine modes by its odd-odd parity. Since |grad psi|=|U|=o(r), integration along radial segments gives psi=o(r^2), uniformly in angle. A fixed mode j>=2 therefore has coefficient o(r^2) at infinity and is bounded near zero. If its forcing vanishes, its radial equation has only the solutions a r^j+b r^-j. The condition at zero gives b=0, and the condition at infinity gives a=0, including j=2.

For a nonzero smooth forcing mode f_j=O(r^j) at zero and O(r^(gamma-1)) at infinity, the Green formula below is regular at zero and O(r^(gamma+1)) at infinity. Its difference from the canonical coefficient is a homogeneous mode, so the same argument proves equality. The forcing bounds follow by projecting the smooth function rho_x on its fixed angular mode and by the assumed first-derivative growth bound. This proves both the Green formula used here and the absence of unforced modes above the top forcing. It does not assume a freely chosen harmonic strain.

## The top stream-function coefficient

Suppose rho is not zero and choose the largest odd index N for which b_N is not identically zero on (0,infinity). Put b=b_N and m=N+1. The Poisson forcing has no modes above m. Canonical uniqueness and the modal Green formula therefore imply that psi has no modes above m. Its coefficient h of sin(m theta) is

    h(r)=-(1/2)r^-m integral_0^r s^m b(s) ds.          (1)

For completeness, the top forcing is f=(b'-Nb/r)/2. In the modal Green formula

    h=(1/(2m))[r^-m integral_0^r s^(m+1)f(s) ds
                +r^m integral_r^infinity s^(1-m)f(s) ds],

integration by parts gives the lower integral

    (1/2)r^(m+1)b(r)-m integral_0^r s^m b(s) ds,

and the upper integral is -(1/2)r^-N b(r). The upper integral is absolutely convergent since b'=O(r^(gamma-1)) there. The boundary term at infinity vanishes because b=O(r^gamma) and gamma<N; the one at zero vanishes by local smoothness. The two explicit b(r) terms cancel, proving (1). In particular,

    h'=-b/2-m h/r.                                    (2)

This step fixes the harmonic datum using the whole-plane canonical inverse. An independently chosen harmonic strain or top harmonic polynomial would invalidate (1).

## The highest nonlinear angular coefficient

In polar coordinates,

    U.grad rho=(psi_r rho_theta-psi_theta rho_r)/r.

The highest possible angular frequency is m+N=2N+1. Only the product of the top two modes contributes to this frequency. Its coefficient is

    [N h' b-m h b']/(2r).

The linear terms c_l r rho_r-rho have frequencies at most N. Hence exact transport forces

    N h'b-m hb'=0                                    (3)

at every r>0. This conclusion does not divide by b or h and remains valid at all their zeros.

## A scalar equation without divisions at zeros

Define

    I(r)=integral_0^r s^m b(s) ds,
    t=r^2/2,  J(t)=I(sqrt(2t)).

Then J is continuous at t=0 with J(0)=0, and is smooth for t>0. Equations (1)-(3) give

    m I(r)[b'(r)+N b(r)/r]=N r^m b(r)^2.

Since

    J'=r^N b,
    J''=r^(N-1)[b'+N b/r],

we obtain the exact equation

    m J J''=N (J')^2,  N=m-1.                         (4)

The growth assumption implies

    |J(t)| <= C(1+t)^beta,
    beta=(N+gamma+2)/2 < N+1=m.                        (5)

## No nonzero component is possible

Let (a,e) be a connected component of the open set where J!=0, with 0<=a<e<=infinity. On that interval J has fixed sign, and

    F(t)=sgn(J(t)) |J(t)|^(1/m)

is smooth. Differentiating twice and using (4) shows F''=0. Thus F is affine on this component.

At its left endpoint, continuity gives J(a)=0, including a=0 because J(0)=0. Consequently F tends to zero there. If e is finite, the same reasoning at the right endpoint forces an affine F to have two distinct zeros. That would make F identically zero, a contradiction.

Therefore the component extends to infinity. The bound (5), with beta<m, forces the slope of the affine F to be zero: a nonzero slope would give |J(t)| asymptotic to a positive constant times t^m. A constant F with zero left endpoint limit is zero, again a contradiction.

Thus J has no nonzero component. It is identically zero, so J'=r^N b=0 and b=0, contrary to the choice of the top mode. This proves rho=0.

## Dependencies, exceptions, and numerical meaning

The only nonlocal input is the top coefficient (1), which follows from the canonical full-plane inverse and gamma<1. The rest uses exact angular orthogonality, an ordinary differential equation, continuity at zero, and growth at infinity. No positivity, axis monotonicity, finite critical-point set, analyticity, or interior-flow topology is assumed.

This theorem covers a pure sin(theta) density y F(r) as its N=1 case. It explains why such a radial factor cannot by itself solve the exact smooth problem. It does not prove nonexistence in the full angular class. A numerical approximation with finitely many modes can still approximate an infinite-mode solution; the theorem must not be used to reject numerical existence evidence merely because a finite spectral basis was used. Finite residuals, however small, do not satisfy the exact highest-mode identity (3).

The strict sublinear assumption matters: rho=y, U=0, c_l=1 is an exact affine solution at growth exponent gamma=1. In that case the boundary term at infinity used in (1) does not vanish. The restricted theorem gives no quantitative lower bound for the residual of a finite-mode approximation.
