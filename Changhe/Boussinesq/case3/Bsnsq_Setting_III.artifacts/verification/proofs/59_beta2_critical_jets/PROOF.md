# Finite-order critical directions and bounded vorticity jets at beta2

Date:2026-10-20. Status: CONFIRMED by independent derivation and exact symbolic checks.
The lead independent auditX agrees on the finite-order result. Actual Opus
requests returned no written audit; this limitation is recorded below.
This audits the lead draft4.7(x). It is a restricted theorem, not an endpoint.

## 1. Exact statement, hypotheses and dependencies

Assume a smooth full-plane B2 profile at beta=2 with the canonical relative
velocity, x-reflection parity, Theta(0,y)=0, the nonzero center coefficient
Theta=a0 x^2+O(|X|^3), and U=o(|X|). Put

    W=2X+U-U(0), divW=4, -curlW=Omega,
    W.gradTheta=0, W.gradOmega+Omega=Theta_x.

Assume Omega has one weak sign in x>0. Its sign must match that of a0 near
the center because Omega_x(0)=2a0. The following previously proved facts
are precise inputs, with proofs in the cited topic folders:

- Packets33,36,39: the escape set E has a C1 scattering diffeomorphism Phi
  onto R^2 minus0, detDPhi=1, and Phi(phi_tY)=e^{2t}Phi(Y). The angular
  temperature h is smooth and Theta=h(alpha), alpha=argPhi locally on E.
  Smoothness of h comes from packet36 Section6, the uniform C^j
  physical continuation and angular expansion, not from composition with
  the C1 inverse scattering map alone. This distinction matters for the
  lead auditX, whose supplied question omitted that additional input.
- Packet54: at X(t,alpha)=phi_t(Phi^{-1}(e(alpha))),

      gradalpha=(-W2,W1)/(2e^{4t}) != 0.

- Outward radial flow outside a large ball makes every negative semiorbit
  bounded. Smooth fields and all their fixed-order derivatives are bounded
  on its compact closure. Reflection commutes with Phi; an orbit whose
  angle lies in the open right semicircle lies wholly in x>0.
- Packet56: for weakly signed Omega in this target, no escaping orbit in
  x>0 is horizontal. This uses the nonzero angular tail and the exact
  full-plane angular inverse, and assumes neither isolated equilibria nor
  a particular backward limit.

Fix alpha_star in the open right semicircle and its complete escaping orbit
O. Suppose its backward limit set is the singleton {p}, with W(p)=0 and
DW(p) having no negative eigenvalue. Let N>=2 be finite and suppose

    h^(j)(alpha_star)=0 for 1<=j<N, h^(N)(alpha_star)!=0.    (1)

Then N is odd. Consequently h-h(alpha_star) is flat at every local extremum
satisfying the same backward-limit condition. At such an extremum,
Theta-h(alpha_star) and Omega have zero jets of every order at every point
of O. Flatness is pointwise in physical space; it asserts neither analyticity
nor local constancy.

If Z={W=0}=gamma, the compact center equilibrium arc, packet53 proves the
backward-limit condition with eigenvalues0,4 at every possible limit,
including endpoints. Thus this theorem covers endpoint-originating orbits
as well as interior fibres. Packet58 is stronger on interior fibres: it
also rules out opposite signs of hprime accumulating at a flat critical
point, but its proof does not cover endpoints.

## 2. Taylor jets of a smooth composite with a C1 angle

Fix Y on O and write ell=gradalpha(Y), a nonzero covector. C1 regularity gives

    alpha(Y+z)-alpha_star=ell.z+o(|z|).

Taylor's theorem for the one-variable smooth h and(1) give

    Theta(Y+z)-h(alpha_star)
      = h^(N)(alpha_star)(ell.z)^N/N! + o(|z|^N).           (2)

No derivative of alpha beyond the first occurs. Since Theta itself is
smooth, uniqueness of its multivariable Taylor polynomial through order N
in(2) gives

    D^jTheta(Y)=0 (1<=j<N),
    D^NTheta(Y)=h^(N)(alpha_star) ell^{tensor N}.           (3)

For completeness, uniqueness follows by subtracting the two polynomials
and restricting to z=tv for each fixed v. Every lower homogeneous
coefficient then vanishes, and polarization determines each symmetric
multilinear tensor from its diagonal polynomial.

Put F_n=D^nTheta_x along O. It follows that

    F_n=0 for 0<=n<=N-2,
    F_{N-1}=h^(N)(alpha_star) alpha_x
                               (gradalpha)^{tensor(N-1)}. (4)

The nonzero tensor in the second line cannot vanish unless alpha_x=0.
These statements use the smoothness of Theta, not a falsely assumed smooth
scattering angle.

## 3. The differentiated transport equation

Let J_n=D^nOmega along O, as a symmetric covariant n-tensor. For n=0 the
forcing is zero because hprime(alpha_star)=0. Hence

    dOmega(X(t))/dt+Omega(X(t))=0.

A nonzero solution grows like e^{-t} as t tends to minus infinity. Its
boundedness on the negative semiorbit forces J_0=0 on the whole orbit.
Continuity then gives Omega(p)=0. In two dimensions -curlW(p)=Omega(p)=0,
so DW(p) is a REAL SYMMETRIC matrix. In particular no ambiguity about
complex eigenvalues is present at this critical backward limit. This also
removes the non-normality concern raised in the lead draft's general form.

For n>=1, write I=(i1,...,in) and let S range over subsets of its labelled
slots; repetitions of coordinate labels still count as distinct slots.
Repeated product differentiation of W_j partial_jOmega gives

    d(J_n)_I/dt + (J_n)_I
      + sum_{ell=1}^n (partial_{iell}W_j)
                       (J_n)_{i1,...,iell-1,j,iell+1,...,in}
      = (F_n)_I
        - sum_{S subset {1,...,n}, |S|>=2}
                 (partial_{I_S}W_j)
                 partial_j partial_{I_complement(S)}Omega. (5)

Repeated j is summed over1,2. The last sum contains only vorticity
jets of orders n-|S|+1<=n-1. Define L_n(t) to be the identity plus the
n-slot derivation action of DW(X(t))^T. Then(5) is the lead's jet ODE,
with all binomial multiplicities fixed by the explicit subset formula.
If all lower jets vanish, its last sum is zero.

## 4. Backward growth and the precise estimate

Fix a tensor order n. On the tensor space with its Euclidean inner product,
if M=DW(p) is symmetric with eigenvalues lambda1,lambda2, then L_n(p) is
symmetric with eigenvalues

    1+k lambda1+(n-k)lambda2, 0<=k<=n.                    (6)

This follows by diagonalizing M in an orthonormal basis and taking symmetric
products of its eigen-covectors. Under the theorem's nonnegative-eigenvalue
assumption, L_n(p)>=I. Since X(-tau) tends to p, continuity gives

    <J,L_n(-tau)J> >= (1/2)|J|^2                         (7)

for all sufficiently large tau. Only convergence is needed, without any
rate or integrability of DW(X(-tau))-DW(p).

If the forcing and lower jets in(5) vanish, then in backward time

    dJ_n/dtau=L_n(-tau)J_n.

Consequently(7) gives d|J_n|^2/dtau>=|J_n|^2. Any nonzero value therefore
grows exponentially backward. This contradicts boundedness of D^nOmega
on the compact negative semiorbit. Thus J_n vanishes at all sufficiently
negative times and, by uniqueness for the linear homogeneous ODE, along
all of O.

There is also an elementary repair of the lead's adapted-norm argument
without using symmetry. If a constant real matrix A has eigenvalues with
positive real part, define

    P=int_0^infinity exp(-A^T s) exp(-A s) ds.

The integral converges, P is positive definite, and A^T P+P A=I, by
integrating the derivative of its integrand. If A(tau) tends to A, then
A(tau)^T P+P A(tau)>=I/2 eventually. Hence a solution J'=A(tau)J obeys

    d(J^T P J)/dtau >= |J|^2/2
                         >= (J^T P J)/(2 lambda_max(P)).

This proves the same backward growth under mere matrix convergence. A
semigroup bound for the constant limit alone would not be the entire
argument; this positive quadratic form supplies the missing perturbation
step. It is not necessary for the present symmetric limiting matrix.

## 5. Vanishing lower jets and exclusion of even N

Starting with J_0=0, induct on n=1,...,N-2. Equation(4) makes F_n zero,
and the induction makes all lower terms in(5) zero. Section4 then forces
J_n=0. This range is empty when N=2, for which the argument below requires
no backward-limit assumption at all, as already proved in packet56.

Suppose N is even. At every Y on O, the lower vanishing jets give

    Omega(Y+z)=J_{N-1}(Y)[z,...,z]/(N-1)!+o(|z|^{N-1}).   (8)

A small ball about Y lies in x>0. The left side has one weak sign there.
A nonzero homogeneous polynomial of odd degree changes sign under z to -z.
Thus the odd-degree term in(8) must vanish identically, and polarization
gives J_{N-1}(Y)=0. This applies at EVERY Y on O. Its derivative along O
is therefore zero, not merely its value at one time. Equation(5) at order
N-1 now gives F_{N-1}=0, because all the lower jets and J_{N-1} vanish.
By(4), h^(N)!=0 and gradalpha!=0, this forces alpha_x=0 along all of O.
The exact gradient formula in Section1 gives W2=0 throughout O. Its y
coordinate is constant, contradicting the no-horizontal-orbit theorem.
This proves that N is odd.

A finite first nonzero derivative at a local extremum has even order.
Therefore an extremum satisfying the backward-limit hypothesis has no
nonzero derivative of positive order. For each integer m, flatness of h
and alpha(Y+z)-alpha_star=O(|z|) give

    Theta(Y+z)-h(alpha_star)=o(|z|^m).

Smoothness of Theta gives all positive-order temperature jets zero.
Then every F_n is zero, and the same finite-order induction and Section4
show J_n=0 for each n. There is no passage to an infinite tensor system:
every order is established separately with its own finite constants.

## 6. Saddle scope and an exact local sharpness example

Suppose instead that the critical limit is a saddle, with eigenvalues
-nu and4+nu, nu>0. Formula(6) has smallest eigenvalue1-n nu. To exclude an
even finite order N>=4, the above induction suffices under

    nu < 1/(N-2).                                        (9)

The inequality is STRICT. The equality case is not proved by backward
growth. For N=2 no threshold is necessary. Flatness of Omega at a flat
extremum does not follow from this argument for any fixed nu>0, because
arbitrarily large tensor orders eventually violate1-n nu>0.

Here is a coupled local B2-P example showing that a bounded homogeneous
jet of weakly signed Omega really can survive at equality. Let m>=2 be
an even integer and set

    W1=-x/m,
    W2=(4+1/m)y-x^{m+1}/(m+1),
    Omega=x^m, Theta=0.                                  (10)

Then divW=4, -curlW=Omega, W.gradTheta=0, and
W.gradOmega+Omega=(-1+1)x^m=0=Theta_x. Put V=W-2X; it is divergence free,
V(0)=0, and locally V=(-Psi_y,Psi_x) with

    Psi=(2+1/m)xy-x^{m+2}/((m+1)(m+2)).                   (11)

Thus -DeltaPsi=Omega as well. The orbit x=0,y>0 has backward limit0;
Omega=0 on it but D_x^mOmega=m! survives as a nonzero constant jet.
At nu=1/m this is exactly the zero eigenvalue1-m nu of L_m. Choosing
N=m+2 makes equality in(9). Weak sign does not kill this even-degree jet.

Example(10) is LOCAL SHARPNESS OF THE JET ARGUMENT ONLY. It violates the
nontrivial temperature normalization, the required global reflection
parity (its shear term is odd in x), and the full-plane sublinear-velocity
condition. It is not a counterexample to any global B2 theorem and is not
an example of a finite-order h extremum. It establishes why equality in
(9) cannot be silently included by the bounded-jet argument.

## 7. What the result does not prove

Odd-order critical inflections, flat extrema, and plateau intervals are
not excluded by this theorem. The fact that Omega and Theta-hstar are
flat on an escaping curve does not imply they vanish on a neighborhood
for smooth functions. Far-field smoothness also does not supply analytic
unique continuation. For example a smooth angular bump can be flat at
one angle and nonzero arbitrarily close; this is a logical illustration,
not a B2 construction. No further contradiction at a flat extremum has
been established here.

All-hyperbolic or endpoint hypotheses from other packets must not be
silently inserted. The present theorem under weak sign and a nonsaddle
backward limit is CONFIRMED by the independent verifier. Actual Opus
collaboration was attempted but did not provide a written audit of it.
The unrestricted profile existence problem remains OPEN.

## 8. Verification and provenance

The complete informal proof was written before running symbolic checks.
The source lead draft is copied with SHA256 and actual UTC in
verification/source.json. Independent code code_independent/critical_jet_checks.py completed
20 exact multi-index product-rule checks, three coupled equality examples
at m=2,4,6, and an exact non-normal Lyapunov-matrix example, in
1.408026589 seconds. All checks passed, including the stream sign.
Results are in verification/exact_checks.json.
No solver code from the numerics lane is used. No formal Lean source or
Lean/Lake execution is claimed or permitted.


## 9. Flatness without presupposing a smooth angular label

This supplements Section5 and independently checks the repair in the lead
astra/auditX/PROOF.md. The finite-order proof only needs a nonzero Peano
term h(alpha_star+u)-hstar=C u^N+o(|u|^N), not derivatives of h beyond
that expansion. Choose a fixed smooth transverse line Y0+sv with
b(s)=alpha(Y0+sv)-alpha_star, bprime(0)!=0. The restriction
f(s)=Theta(Y0+sv)-hstar is smooth, b is a C1 local diffeomorphism, and
f(s)=h(alpha_star+b(s))-hstar. If h has a local extremum, so does f.
A first nonzero Taylor term of f would have even order N. Substituting
b^{-1}(u)=u/bprime(0)+o(|u|) would produce a nonzero even Peano term of h,
contradicting Sections2-5. Thus f is flat. For each m, its flat estimate
and the local Lipschitz inverse give h(alpha_star+u)-hstar=o(|u|^m).
Composition with the locally Lipschitz angle then makes all smooth
physical temperature jets zero. The vorticity induction gives all its
jets zero as before. Under packet36's separately proved smoothness, this
pointwise angular flatness is also ordinary derivative flatness.

A useful endpoint exclusion does not need any high derivatives: critical
h gives Omega=0 on O, weak sign gives gradOmega=0 there, and continuity
gives gradOmega(p)=0. Since Omega_x(0)=2a0!=0, p cannot equal0. This
rules out only the marked center as a backward endpoint of a critical
orbit, not other points of gamma.

## 10. Flat first two far-field vorticity coefficients

At a flat extremum, let a,b be the smooth angular coefficients proved in
packet36, so for each finite j,

    r^s Omega(r e(theta))=a(theta)+r^{-s}b(theta)+o_Cj(r^{-s}),
    s=1/2.

Along O, r(t) is asymptotic to a positive constant times e^{2t}.
The bound V=O(r^{1-s}) gives |theta'(t)|<=C r(t)^{-s}; integrating toward
infinity proves |theta(t)-alpha_star|<=C r(t)^{-s}. Each angular derivative
of Omega at X(t) is zero because it is a finite linear combination of its
zero Cartesian jets at that point. Uniform C^j leading convergence then
gives a^(j)(alpha_star)=0 for every j. This conclusion requires the actual
uniform derivative expansion; pointwise values alone would not suffice.

Fix j and any integer M>1. Taylor's theorem at the now flat a gives
|a^(j)(theta(t))|<=C_M |theta(t)-alpha_star|^M=O(r(t)^{-Ms}).
Multiplying the order-j differentiated expansion by r(t)^s gives

    0=r(t)^s a^(j)(theta(t))+b^(j)(theta(t))+o(1).

The first term tends to zero. Hence b^(j)(alpha_star)=0. Both a and b are
flat at this angle. The constants may depend on j,M; no uniform estimate
in derivative order is used. This verifies the lead18:38 observation
with all moving-angle and remainder assumptions explicit. It gives no
contradiction: a smooth nonnegative function can have a flat zero.

## 11. Actual collaboration record

Requests54,56 and59 requested us.anthropic.claude-opus-5-5 and each returned
actual model claude-opus-5-5. Request54 exhausted12000 output tokens without
any written audit (110.483370776seconds). Requests56 and59 returned no text
with stop_reason refusal (7.683126154 and5.078431171seconds). Their raw
responses label the refusal category cyber, despite the mathematical
subject. No mathematical reason or verdict was supplied. These records
are not endorsements, and no substitute model was silently used.

The separate lead auditX was read in full in actual local file output on
2026-10-20. Its finite-order tensor identity, symmetric-limit observation,
Lyapunov argument, strict saddle threshold and transverse-line repair
were independently checked above. Its statement that smooth h was not
supplied applies to its question; our proof explicitly cites packet36.
Its own Opus attempt reports credential retrieval failure, so it is an
independent Codex audit, not an Opus endorsement. Its illustrative rough
reparametrization and its external Khalil citation are not dependencies
of this proof. The matrix argument is proved directly in Section4.
