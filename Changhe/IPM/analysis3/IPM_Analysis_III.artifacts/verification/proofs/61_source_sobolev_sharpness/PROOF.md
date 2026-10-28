# Sharp Sobolev failure for the coupled frozen source

## Statement and realization

Let A>mu>0, g>=0, and

    L=A x partial_x+mu y partial_y-1-gM,
    Mhat(xi,eta)=xi^2/(xi^2+eta^2),
    b=1+(A+mu)/2, a=g/(A-mu),
    q=(1+g)/A, d=1+mu/A, s_fast=q+d/2=(b+g)/A.

The Fourier transform is unitary on L2(R2), with prefactor (2pi)^(-1).
For s>=0 use the usual inhomogeneous Hs norm and the maximal domain

    D_s={h in Hs: A x h_x+mu y h_y is in Hs distributionally}.

There is a real f in C_c^infinity(R2), even in x and odd in y, whose
support can be placed in any prescribed neighborhood of0, such that:

1. The unique L2 solution h=R f satisfies h not in Hs(R2) for every
   s>=s_fast. Consequently L:D_s->Hs is not onto for any such s.
2. For every ball B about0, h is not in Hs(B) for every s>s_fast.
   This is a singularity at the source, not only a failure of decay.
3. In the physical scaling x~lambda^(-1), y~lambda^(-mu/A), h has a
   nonzero distributional leading term of degree q, in the precise
   frequency-tested sense proved below. The corresponding Sobolev
   threshold includes the anisotropic volume correction d/2.

These statements keep the full Riesz multiplier M. They do not transfer
this obstruction to the variable-coefficient IPM operator by cutting off
h. A separate nonlocal commutator and domain argument would be required
for that transfer.

On the independently certified source box

    10<=A<=51/5, 99/100<=mu<=101/100, 29<=g<=30,

one has s_fast<b/mu. Therefore the sufficient Hs inverse window of
proof 08 is exactly 0<=s<s_fast for each frozen coefficient triple, and
the failure at and above its endpoint is proved here. The uniform lower
endpoint 2373/680 from proof 08 is a box minimum, not the exact modal
source threshold. The evidence file encloses that actual threshold
using the previously independently certified source coefficients.

## Exact semigroup formula

Proof 08 proves that L has a closed maximal L2 realization and a unique
bounded inverse R=-integral_0^infinity S_t dt, with
||S_t||_(L2->L2)<=exp(-b t). With B=diag(A,mu), direct Fourier transport
and integration of the multiplier give

    (S_t f)hat(zeta)
       = exp((a mu-A-mu-1)t)
           |zeta|^(-a)|exp(-Bt)zeta|^a fhat(exp(-Bt)zeta).  (1)

The identity follows from

    d/dt log|exp(-Bt)zeta|
       = -mu-(A-mu)m(exp(-Bt)zeta),

and the Fourier Jacobian exp(-(A+mu)t), together with the scalar -1.
At g=0, a=0 and the multiplier ratio is1. The formula is used as a
single bounded operator, with no separate fractional multiplier at
zero frequency. For nonzero zeta and Schwartz f the inverse integral
converges pointwise, so it represents the same L2 inverse.

## A fixed compact forcing with a nonzero scaling limit

Choose nonzero real even functions u,v in C_c^infinity(R), with nonzero
integrals. Put phi=u*u, psi=v*v, and

    f(x,y)=-phi(x)psi'(y).

The supports can be chosen arbitrarily small. With a positive Fourier
normalization constant c_F,

    fhat(xi,eta)=-i c_F eta |uhat(xi)|^2 |vhat(eta)|^2.       (2)

For eta>0 this has a fixed imaginary sign. It is nonzero when both
frequencies are sufficiently small and nonzero.

Let lambda>=1, zeta_lambda=(lambda kappa,lambda^(mu/A)nu), with kappa,nu
positive and bounded away from0. Substitute t=log(lambda)/A+tau into
the inverse formula. All powers cancel exactly to give

    lambda^(q+d) hhat(zeta_lambda)
      = -(kappa^2+lambda^(-2(1-mu/A))nu^2)^(-a/2)
          integral_(-log(lambda)/A)^infinity
            exp((a mu-A-mu-1)tau)
            |exp(-Btau)(kappa,nu)|^a
            fhat(exp(-Btau)(kappa,nu)) d tau.               (3)

At tau->+infinity, the norm factor is O(exp(-a mu tau))
and oddness in eta gives fhat=O(exp(-mu tau)). The integrand is therefore
O(exp(-(A+2mu+1)tau)). At tau->-infinity, kappa exp(-A tau) tends to
infinity; the arbitrary Schwartz decay of uhat dominates every fixed
exponential factor. The bounds are uniform on each compact positive
frequency rectangle. Dominated convergence yields a continuous limit

    Hhat(kappa,nu)=-|kappa|^(-a)
       integral_R exp((a mu-A-mu-1)tau)
          |exp(-Btau)(kappa,nu)|^a
          fhat(exp(-Btau)(kappa,nu))d tau.                  (4)

The integrand has one imaginary sign by (2), and it is strictly nonzero
for all sufficiently large tau. Thus Hhat never vanishes on the
positive quadrant. In particular it is bounded below in modulus by
some c>0 on any fixed positive compact rectangle.

Define the rescaled physical distributions

    H_lambda(X,Y)=lambda^q h(X/lambda,Y/lambda^(mu/A)).

Their Fourier transforms are the left side of (3). Hence H_lambda
converges to the nonzero profile (4) when tested against Schwartz
functions whose Fourier support is compact in the positive quadrant.
This is the precise asserted anisotropic leading term. No pointwise
asymptotic or additional axis-supported term is silently asserted.

## Global Hs failure, including the endpoint

Choose a rectangle K=[kappa0,kappa1] times [nu0,nu1] with positive
endpoints and kappa1<2 kappa0. Its anisotropic images K_j under
(kappa,nu)->(2^j kappa,2^(j mu/A)nu) are pairwise disjoint. Their measures
are 2^(j d)|K|, and |zeta| is comparable to2^j on K_j.
Uniform convergence in (3) gives, for all sufficiently large j,

    |hhat(zeta)|>=c 2^(-j(q+d)), zeta in K_j.

Consequently the squared Hs integral on K_j is bounded below by

    C 2^(j(2s-2q-d)).                                    (5)

The sum over j diverges whenever s>=q+d/2, including equality.
This proves statement1's norm failure. If a solution in D_s existed
for that same f, it would also belong to the maximal L2 domain and
solve Lh=f there, because M is L2 bounded and the equation gives the
dilation derivative in L2. L2 uniqueness would identify it with Rf,
contradicting (5). Thus non-surjectivity is proved for the stated domain.

## Local Hs failure for strict orders

Choose a Schwartz test W with Fourier support compact in K and phase
such that <Hhat,What> is nonzero. Such a test exists by (4). Let

    W_lambda(x,y)=lambda^d W(lambda x,lambda^(mu/A)y).

Equation (3) and Plancherel imply

    |<h,W_lambda>|>=c lambda^(-q)                         (6)

for all sufficiently large lambda. Its H^(-s) norm is bounded by
C lambda^(d/2-s), since its Fourier support lies at |zeta|~lambda.
If h belonged to Hs(B), take an Hs extension h_B to the full plane and
a cutoff chi in C_c^infinity(B), equal1 on a smaller ball about0. Then
chi h=chi h_B is in Hs(R2), so

    |<chi h,W_lambda>|<=C lambda^(d/2-s)||h||_Hs(B).

The other term is bounded by ||h||_2 times the L2 norm of W_lambda
outside that smaller ball. Schwartz decay makes this O(lambda^(-N))
for every fixed N; the slower shrinking y-scale lambda^(-mu/A) still
permits arbitrary N because mu/A>0. Therefore

    c lambda^(-q)<=C lambda^(d/2-s)||h||_Hs(B)+C_N lambda^(-N).

For s>q+d/2 and N>q this is impossible. This proves statement2.
The argument does not claim local endpoint failure; the global endpoint
failure has already been proved separately by disjoint frequency tiles.

## The active threshold in the certified box

The inequality s_fast<b/mu is equivalent to

    (A-mu)(1+(A+mu)/2)-mu g>0.

The left side increases with A and decreases with mu and g. Its minimum
on the box occurs at A=10, mu=101/100, g=30, and equals563599/20000>0.
Thus the fast threshold is the active one throughout the box. The
minimum and maximum of s_fast there are2373/680 and7301/2000. The
near equality mu~1 creates no isolated transport pole in this coupled
calculation.

The code uses exact rational endpoint arithmetic to enclose q, d and
s_fast for the modal source, reading the exact rational endpoints from
proof 15's independently reconstructed original-coefficient certificate.
It verifies the analytic scaling identities symbolically. These checks
supplement the proof above; no numerical sample is used to establish
non-surjectivity or the singularity.

## Dependencies and scope

Dependencies: the closed L2 inverse and maximal-domain proof in proof 08;
Fourier inversion, Plancherel and elementary dominated convergence;
proof 15's independently audited source coefficient enclosure for the
actual numerical association. No information from a raw X3 source is
substituted for the exactly normalized trial.

CONFIRMED: the sharp global frozen Hs endpoint, the strict local failure,
the nonzero anisotropic leading distribution, and their association to
the certified modal source. OPEN: the variable-coefficient high inverse,
its variable-order domain and all nonlinear closure constants.
