# Acceptance of the independent complete-plane Hessian certificates

## Exact statement and hypotheses

Fix one of the immutable exact potentials007,016,017 whose raw SHA256 is
recorded in verification/result.json. Use its rational parameter c>1 and
put delta=1-1/c. Define rho=-partial_y Delta chi on R2. The accepted raw
normalization and generator proofs give smoothness at the origin and
D^k rho=O(r^(1/c-k)) at infinity for k<=2. These endpoint facts imply
D2rho belongs to L2(R2): at infinity the squared radial integrand is
O(r^(2/c-3)), whose exponent is less than-1. Define

    E_ab=integral_R2 |partial_a partial_b rho|^2, ab=xx,xy,yy,
    X^2=E_xx+E_xy, Y^2=E_xy+E_yy, H^2=X^2+Y^2,
    kappa^2=((log(2)-1/2)X^2+(3log(2)-2)Y^2)/(16pi).

This result accepts N4-268 through the independent T4-366 reproduction.
For016 kappa<0.735053672993720766; for017
kappa<0.729080538628955349. For007 the computation agrees with the
previously accepted exact Hessian energy sums. Under the independently
audited gradient-commutator identity, the operator

    K=1/2[R1,[R1,rho_y]]-1/2[R1,[R2,rho_x]],
    Fourier multiplier Rj=i xi_j/|xi|,

has Hilbert-Schmidt norm kappa, so ||K||<=kappa. This is an upper bound
only. The result provides no global bound for
sup_R2 (|grad rho|-rho_y)/2, no inverse, and no existence assertion.

## Independent derivative construction

Set t=r^2/(1+r^2) and v=1-t. Every density has the finite exact form
rho=r sum_(j,n) v^((j+1)delta/2) A_(j,n)(t) sin(n theta), where each A
is rational with denominator (1+624v)^p(1+2499v)^q and nonnegative
integer p,q. These factors are positive throughout0<=v<=1.
For r^d v^a A(t), radial differentiation gives r^(d-1)v^a B(t), where
B=(d-2at)A+2tv A'. Cartesian differentiation follows from
partial_x=cos(theta)partial_r-sin(theta)partial_theta/r and
partial_y=sin(theta)partial_r+cos(theta)partial_theta/r. The sine and
cosine product identities therefore give the exact n-1,n+1 recurrences
in the frozen T4 proof. Negative sine frequencies reverse sign, negative
cosine frequencies do not, and sine0 is zero.

Apply the recurrence twice, with d=1 and then d=0. Compare xy and yx
as exact rational fields. Each resulting rational coefficient has an
exact factor t. Removing it uses r^-1 t=r v and gives

    rho_ab=r sum_(j,n) v^(1+(j+1)delta/2) B_ab,(j,n)(t) trig(n theta).

This proves the fields used for integration equal the Cartesian Hessian.
The own lane derives them instead from fifth derivatives of chi. Nine
physical comparisons per candidate also check the two field paths, but
point samples play no role in the integral upper bound.

## Integral identity and enclosure

All retained Hessian frequencies are positive and odd. Orthogonality on
0<=theta<=2pi gives pi for equal-frequency equal-kind products and zero
otherwise. Group all equal-frequency pairs, including twice each distinct
unordered pair, by ell=j+j'+2. If W_ell is the resulting rational sum,
then r dr=-dv/(2v^2) gives exactly

    E_ab=(pi/2) sum_ell integral_0^1
         v^(ell delta/2-1) (1-v) W_ell(1-v) dv.

The exponent b=ell delta/2-1 exceeds-1 since ell>=2 and delta>0.
Thus every signed branch-group integral converges separately. Exact
polynomial division and partial fractions express its rational factor
as P(v)+sum c_(a,k)/(1+av)^k. Multiplication by the full denominator
replays this identity in Q[v]. Monomials integrate to1/(b+j+1).
For a>0 and k>=1, Euler's convergent integral yields

    integral_0^1 v^b/(1+av)^k dv
      =2F1(k,b+1;b+2;-a)/(b+1).

T4 encloses this formula directly using outward Arb arithmetic. Our
independent calculation uses a recurrence in the pole order derived by
integrating a derivative, with direct-formula regression checks. The
proofs of both identities and the exact field constructions, rather than
mere agreement of decimals, establish the enclosures. Agreement of all
135 actual group integrals and all scalar assemblies checks the retained
records against those arguments. Both paths use Arb; no independent
implementation of its ball arithmetic is claimed.

The three component energies are positive. The definitions of X,Y,H
and kappa follow by finite sums and positive square roots. Both log
weights are positive. Reassembling every scalar in the acceptance
checker confirms the reported containing balls and strict rational caps.
For007 use pi/2 times the previously accepted exact rational energy
sum, or a containing norm ball. A directed decimal upper endpoint is
not itself a containing ball for the true norm; the known Y endpoint
mismatch is retained as an expected diagnostic.

## Source binding and scope of acceptance

Freeze the T4 manifests, results, proofs, and invoked helper source, or
retain an identical already frozen file by SHA256. Verify every raw
hash, every declared input hash, each complete group map, each exact
replay flag, endpoint hypothesis, moment accuracy and physical value.
Then recompute sums, scalar identities and strict caps from the stored
outward balls. The accepted source code is read as text, not executed.
Our previous independent full computation is a required input. This
proof is written and checked before the new comparison code runs.
Formal sources are absent; verification/ contains numerical certificate
evidence only. Independent review does not establish any omitted analytic
hypothesis of a proposed existence theorem.

Implementation correction before acceptance: the optional directed-endpoint
diagnostic is replayed from the exact007 rational energy sum at2048bits.
Reassembling a norm from published90-digit group intervals broadens it and
can overlap a directed endpoint that does not contain the exact norm.
Such an overlap is not required to match the narrow diagnostic. The first
failed logs also retain an unsupported decimal-string rational parser;
strict decimal caps are now entered as integer ratios. Neither failed
checker produced an acceptance record.
