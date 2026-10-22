# Positive slow-tail forcing with the correct center data

Date: 2026-10-20. Status: PROVED counterexample to a transport-only obstruction. This is NOT a B2 profile.

## Exact statement

For every beta>2 and a0>0, there are smooth whole-plane fields with B2 reflection parity, Theta(0,y)=0, Theta>=0, and Omega>0 on x>0, satisfying all of the following:

    U=(-Psi_y,Psi_x), -Delta Psi=Omega,
    V=U-U(0) is the canonical once-subtracted whole-plane inverse,
    W=beta X+V, W.grad Theta=(beta-2)Theta,
    Theta=a0 x^2+O(|X|^4),
    Psi_xy(0)=1+beta/2, Omega_x(0)=4a0/beta,
    U=O(r^(1-1/beta)), DU=O(r^(-1/beta)) at infinity.

The whole plane is the backward basin of the source0. The vorticity has a nonzero r^(-1/beta) leading tail, and Theta has a continuous homogeneous angular limit of degree(beta-2)/beta, positive off the axis. Nevertheless,

    R_Omega=W.grad Omega+Omega-Theta_x

has a strictly positive xy Taylor coefficient, explicitly computed below. Thus these auxiliary properties, the inverse relation and temperature equation alone do not exclude positive-vorticity profiles. The vorticity equation must be used beyond its center normalization to obtain such an exclusion.

## Formula and elliptic verification

Put

    p=(beta-1)/(2beta), c=1+beta/2, lambda=(beta-2)/2,
    L=3c sqrt(beta)/(4a0), h=sqrt(beta)L,
    S0=L^2+h^2,
    B=c/[2p h S0^(p-1)],
    z=y-h, s=x^2+z^2, S=L^2+s.

Here1/4<p<1/2 and all scale constants are positive. Define

    Psi=-B x S^p,
    U1=2Bp xz S^(p-1),
    U2=-B[S^p+2p x^2 S^(p-1)],
    Omega=4Bp x S^(p-2)[2L^2+(p+1)s].        (1)

Direct differentiation of Psi gives these formulas, with div U=0 and -curl U=Omega. All fields are smooth since S>=L^2>0. Parity in x and strict positivity of Omega in the right half-plane are immediate. The chosen absolute representative has

    U(0)=(0,-B S0^p),

which is generally nonzero. This is an explicit representative for this manufactured example, not an assertion that the lead has selected a general absolute gauge.

Differentiating U at0 gives DU(0)=diag(-c,c), because2Bp h S0^(p-1)=c. If q(y)=Omega_x(0,y), then

    q(y)=4Bp [L^2+(y-h)^2]^(p-2)
                    [2L^2+(p+1)(y-h)^2],
    q(0)=3c/h=4a0/beta.                     (2)

The identity follows after inserting h^2=beta L^2 and p=(beta-1)/(2beta). Expansion of(1) at infinity gives, uniformly in angle,

    Omega(r cos theta,r sin theta)
       =4Bp(p+1)r^(-1/beta)cos theta+O(r^(-1-1/beta)),
    U=O(r^(1-1/beta)), DU=O(r^(-1/beta)).     (3)

The mass over any fixed sector in x>0 is comparable to R^(2-1/beta). Omega is not in L^j for any1<=j<=2beta; the critical case diverges logarithmically. These observations agree with, rather than contradict, the circulation lower bound.

## Canonical full-plane inverse

For the sign convention of(1), K(Z)=(Z2,-Z1)/(2pi|Z|^2). The integral

    Vtilde(X)=integral_R2 [K(X-Y)-K(-Y)]Omega(Y)dY

is absolutely convergent at infinity, since its integrand is bounded there by C|X||Y|^(-2-1/beta). Its two local kernel singularities are integrable against smooth Omega. The standard distributional differentiation of the logarithmic fundamental solution gives div Vtilde=0 and curl Vtilde=-Omega.

For completeness its growth can be estimated without any unknown boundary condition. Split into |Y|<2r and |Y|>=2r, where r=|X|>=1. The outer integral is O(r^(1-1/beta)). In the inner region split a disk of radius r/2 around X; there the vorticity is O(r^(-1/beta)) and the 1/|X-Y| kernel has integral O(r). Away from that disk use the kernel bound O(1/r), the mass estimate O(r^(2-1/beta)), and the separate integrable term |Omega(Y)|/|Y|. This also gives O(1+r^(1-1/beta)).

The difference V-Vtilde has zero divergence and curl, hence harmonic components. It is sublinear. The interior gradient estimate for an entire harmonic function f gives, at any fixed center, |grad f|<=C R^(-1)sup_B_R|f|, which tends to0 here. Thus the difference is constant. Both velocities vanish at0, so it is zero. This proves the claimed canonical relative inverse; it does not invoke a finite-box inverse.

## Global backward contraction

Write e=1-p. Direct differentiation of U gives the traceless symmetric part of DU. Its two independent entries, after taking out2Bp S^(p-1), are

    z(1-2e x^2/S),
    x[-1+e(x^2-z^2)/S].

Squaring and adding them gives

    sigma^2=(2Bp)^2 S^(2p-2)
             s[1-x^2(2e/S-e^2s/S^2)],       (4)

where sigma is the absolute eigenvalue of Sym DU. Since0<e<1 and s<S, the parenthesis subtracted is nonnegative. Thus

    sigma<=2Bp sqrt(s)(L^2+s)^(p-1).

The maximum of r(L^2+r^2)^(p-1) occurs at r=L/sqrt(1-2p)=h. The definition of B therefore gives sigma<=c and

    Sym DW >= (beta-c)I=lambda I, lambda>0. (5)

The explicit derivatives are bounded, so W is globally Lipschitz and has a complete flow phi_t. Since W(0)=0, integration of(5) along a line segment gives X.W(X)>=lambda|X|^2. Hence

    |phi_-t X|<=e^(-lambda t)|X|, t>=0.      (6)

In particular0 is the only equilibrium and the whole plane is its backward basin.

## A smooth transported temperature

Define g=W1/x by its smooth axis continuation:

    g(X)=beta+2Bp z S^(p-1).

The same maximizing relation h^2=beta L^2 gives g(0)=lambda and Dg(0)=0. Set

    I(X)=integral_0^infty [g(phi_-t X)-lambda]dt,
    xi(X)=x exp[-I(X)], Theta(X)=a0 xi(X)^2. (7)

On compact sets(6) bounds the integrand by C|X|^2e^(-2lambda t), so I converges and is O(|X|^2) near0. The backward variational equation and(5) give ||D phi_-t||<=e^(-lambda t). On a fixed compact set all higher derivatives of W on the backward trajectories are bounded. Induction in the differentiated flow equation gives ||D^k phi_-t||<=C_k e^(-lambda t): each nonlinear forcing term contains at least two lower-order flow derivatives and is therefore O(e^(-2lambda t)); variation of constants proves the asserted bound. Every differentiated integrand in(7) is consequently integrable, locally uniformly, to every finite order. Thus I,xi,Theta are smooth.

Because dot x=xg, formula(7) also reads

    xi(X)=lim_t->infinity e^(lambda t)(phi_-t X)1.

The group law gives xi(phi_s X)=e^(lambda s)xi(X), hence W.grad xi=lambda xi and

    W.grad Theta=2lambda Theta=(beta-2)Theta.

The exponential in(7) is positive, so Theta>0 off x=0. Reflection of the flow makes xi odd in x and Theta even. Since I=O(|X|^2), xi=x+O(|X|^3), giving the stated normalized temperature jet. Also(5) implies b'=d_y W2(0,y)>=lambda>0, so the axis has no additional zero.

## Temperature at infinity

Let alpha=(beta-2)/beta. For all sufficiently large r, W_r>=beta r/2. Use radius along an outgoing trajectory. The angular equation has right side V_theta/[r(beta r+V_r)]=O(r^(-1-1/beta)); its angular derivative has the same bound by(3). The angular maps from a fixed large circle therefore converge in C1 to a circle diffeomorphism, with derivatives bounded above and away from0. The inverse maps converge too.

Along this trajectory Q=Theta/r^alpha solves

    dQ/dr=[(beta-2)/(beta r+V_r)-alpha/r]Q.

The coefficient is O(r^(-1-1/beta)), so its integrating factor converges uniformly to a positive function of the starting angle. Transporting the smooth initial circle data by the limiting angular map proves

    r^(-alpha)Theta(r cos theta,r sin theta) -> A(theta)

uniformly. A is continuous and positive off the two axis angles, where it is zero, because the angular diffeomorphism preserves each half-plane and the axis endpoints.

## Exact failure of the remaining PDE

For this example the axis velocity is

    b(y)=beta y+B[S0^p-(L^2+(y-h)^2)^p].

Its second derivative at0 is

    b''(0)=-2Bp S0^(p-2)[L^2+(2p-1)h^2]=0. (8)

The temperature equation gives, by the first axis equation derived directly above or in packet28, a'(0)=2b''(0)a0/(1+3beta/2)=0. On the other hand differentiating(2) gives

    q'(0)=8Bp(1-p)h S0^(p-3)
                    [3L^2+(p+1)h^2] >0.    (9)

The x coefficient of R_Omega on the axis is bq'+(2beta+1-b')q-2a. Differentiating at0 gives

    d_y d_x R_Omega(0)
       =(2beta+1)q'(0)-b''(0)q(0)-2a'(0)
       =(2beta+1)q'(0)>0.                  (10)

Thus the vorticity equation fails in every neighborhood of0, even though its lowest required center jet is correct. For beta4, the constants reduce to L=9/(2a0), h=2L, B=2*5^(5/8)*L^(1/4), and(10) is17a0^2/15. This is an exact algebraic failure, not an inference from an optimizer residual.

## Dependencies and scope

This is an independent derivation of the lead's `astra/posvort/PROOF.md` section5, with the source retained read-only. Its ingredients are explicit differentiation, whole-plane harmonic uniqueness, contracting ODEs, and integrable radial transport. Packet28 supplies a reusable general form of the third-order center identity, but it is rederived for this example above. Numerical checks to follow are supplementary; the proof precedes the computation.

Neither a full YES nor a full NO follows. The vorticity in(1) is imposed externally; replacing it by vorticity transported in this velocity changes the inverse and is a new closure problem. The construction does not cover beta2. No formalization or rigorous numerical certificate is claimed.
