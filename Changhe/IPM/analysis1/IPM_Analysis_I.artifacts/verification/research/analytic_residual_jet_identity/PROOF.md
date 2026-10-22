# Analytic residual jets and the angular H1 norm identity

## Exact statement

Fix M>=0. On an open log-radius interval I let R_j and psi_n be real C3
functions, for 0<=j<=M and 1<=n<=M+1. Put t=log r, q_j=2j+1,
  rho(t,theta)=sum_j R_j(t) sin(q_j theta),
  psi(t,theta)=sum_n psi_n(t) sin(2n theta).
Let the velocity in polar components be
  U_r=-psi_theta/r, U_theta=psi_r,
and let c be a constant. Define
  eps=c rho_t-rho+U.grad rho.
Then eps and its first two t derivatives are odd trigonometric polynomials.
With
  P=-psi_theta rho_t+psi_t rho_theta,
we have eps=c rho_t-rho+e^(-2t)P, and for i=0,1,2,
  eps^(i)=c rho^(i+1)-rho^(i)
            +e^(-2t) sum_(l=0)^i binom(i,l)(-2)^(i-l) P^(l).
The n,j contribution to P^(l) has two coefficient factors
  A_l=-n sum_(a=0)^l binom(l,a) psi_n^(a) R_j^(l-a+1),
  B_l=(q_j/2) sum_(a=0)^l binom(l,a) psi_n^(a+1) R_j^(l-a),
and equals
  A_l[sin((q_j+2n)theta)+sin((q_j-2n)theta)]
 +B_l[sin((2n+q_j)theta)+sin((2n-q_j)theta)].
Negative odd frequencies are reflected with a minus sign. The greatest
positive frequency is 4M+3, of index 2M+1. An array with indices0..2M+2
therefore has one unused final coefficient, identically zero.

For a real finite odd sine series f=sum_N f_N(t)sin((2N+1)theta), with
C1 coefficients, and any nonnegative measurable radial weight w for which
the following integrals exist, its weighted H1 energy on a radial annulus is
  integral (f^2+r^2|grad f|^2)w dX
   =pi integral e^(2t)w(t) sum_N[(1+(2N+1)^2)f_N^2+(f_N')^2]dt.
For f=eps-eps_t the two radial coefficient arrays are E0-E1 and E1-E2.
For K=rho-rho_t they are R0-R1 and R1-R2. These are algebraic identities,
conditional on the stated polar convention and input fields.

## Proof

The polar gradient is e_r rho_r+e_theta rho_theta/r, and rho_r=rho_t/r.
Thus U.grad rho=r^(-2)(-psi_theta rho_t+psi_t rho_theta). This proves the
residual formula. Differentiating i times with the Leibniz rule and
D_t^a e^(-2t)=(-2)^a e^(-2t) proves the derivative formula, including both
binomial factors. All products require at most third radial derivatives
under i<=2, supplied by the hypotheses.

For fixed n,j, the first product is -2n psi_n R_j' cos(2n theta)
sin(q_j theta); the second is q_j psi_n' R_j sin(2n theta)cos(q_j theta).
Apply 2cos a sin b=sin(b+a)+sin(b-a) and
2sin a cos b=sin(a+b)+sin(a-b), then differentiate l times by Leibniz.
This gives A_l,B_l and the claimed signs. Each q_j is odd and 2n even,
so zero frequency never occurs. The maximal sum is (2M+1)+2(M+1)=4M+3.
Reflection sin(-k theta)=-sin(k theta) accounts for every difference term.

For the energy identity, r^2|grad f|^2=f_t^2+f_theta^2 and dX=e^(2t)dt dtheta.
Distinct positive integral sine frequencies are orthogonal on0..2pi, as
are distinct cosines; each squared sine or cosine integrates to pi.
Expand the finite sums, integrate the cross terms, and sum the surviving
squares. This proves the annular formula. The same formula holds on larger
intervals by exhaustion and monotone convergence if either side is allowed
to be infinite; it provides no finite bound by itself. The K and eps-eps_t
formulas follow directly by differentiation.

## Independent computational verification and scope

The source snapshot xnorm_jets.py implements the A/B scatter formula. The
harness extracts only eps_mode_jets from its Python AST, never imports the
producer modules or constructs a Green archive. Independent code represents
each sine as (z^k-z^(-k))/(2i), differentiates the Laurent monomials in theta
by their signed exponents, and multiplies coefficient dictionaries directly.
The two routes are compared on deterministic integer jets with t=0 and
c=3/4, at five mode counts including the actual M=260 and all derivative
orders0..2. Every floating intermediate in this test is a bounded dyadic
rational; the independent side uses exact integers/fmpq and requires exact
binary64 equality, with no tolerance. Further basis-pair tests check every
bilinear input pair at two small mode counts, with c=0. These are executable
checks of the source algebra, not a proof of arbitrary floating accuracy.
The displayed derivation supplies the identity for arbitrary admissible
fields; the tests do not establish the physical identity of saved input jets.

The fixture does not build the numerical trial, verify its Green moments,
recompute its radial quadrature, authenticate the historical script version,
or certify a full-plane norm or inverse. The finite annulus used by the
reported full_g4 computation excludes r<1e-4 and r>1e7. Its floating result
is not a rigorous full-plane enclosure. Existing interval scalar ceilings
also require physical linkage, coverage and tail arguments. The claims
here give no C lower bound, nonlinear closure or IPM endpoint.
