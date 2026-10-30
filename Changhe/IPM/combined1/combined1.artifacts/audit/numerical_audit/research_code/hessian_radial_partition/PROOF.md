# Exact radial partition of the background Hessian energy

## Statement, hypotheses and scope

Fix one of the immutable exact references C1-N1-016-legqs25-quot013 or
C1-N1-017-legqs50-quot013. Use the exact c, density rho and rational
Cartesian fields of ../scaled_background_hessian/PROOF.md. Its endpoint
hypotheses, exact generator normalization and raw hashes are required.
Let r0=1/50 and R=4178237423365963/500000000000. The latter is exactly the
decimal radius 8356.474846731926 appearing in the recorded diagnostic
commands. This result computes each of the three nonnegative quantities

    E_ab(D)=integral_D (partial_a partial_b rho)^2 dx dy,
    ab in {xx,xy,yy},

on D0={r<r0}, Dmid={r0<=r<=R}, and Dfar={r>R}. Their sum equals the
complete-plane energy. Boundaries have measure zero. All integrations
include every angular mode and every branch. We compare the middle
integrals with the saved FLOAT diagnostics, but do not identify that
difference with quadrature error alone. The exact reference coefficients
and their floating evaluation can differ.

The saved diagnostic uses nodes selected by a radial cutoff, with their
original Gaussian weights. Its actual binary64 radius is a rounded
version of the displayed decimal, and the final panel may be truncated
by node selection. The calculation below audits that selection separately.
The exact nominal annulus and a collection of complete Gaussian panels
are different domains. This proof makes no assumption equating them.

## Exact primitive formula

From the cited complete Hessian proof, each component energy is

    E_ab(R2)=(pi/2) sum_ell integral_0^1 v^b (1-v) W_ell(1-v) dv,
    b=ell delta/2-1>-1, v=1/(1+r^2).

Here W_ell is rational, its denominator is a product of (1+a v)^k
with a>0, and all coefficients are exact rationals. Form the complete
numerator (1-v) numerator(W_ell), then perform exact partial fractions,
replaying the resulting rational identity. Write the result as

    P(v)+sum_(a,k) c_(a,k)/(1+a v)^k.

For 0<V<=1, substituting v=Vu gives

    integral_0^V v^b/(1+a v)^k dv = V^(b+1) J_k(b,aV),
    J_k(b,z)=integral_0^1 u^b/(1+zu)^k du.

Each polynomial monomial c_j v^j contributes
c_j V^(b+j+1)/(b+j+1). The exact moment interface in
../rational_pole_moments/PROOF.md proves the recurrence

    J_0=1/(b+1),
    J_1=2F1(1,b+1;b+2;-z)/(b+1),
    J_k=((1+z)^(1-k)-(b-k+2)J_(k-1))/(k-1), k>=2.

Its proof follows by integrating the derivative of
u^(b+1)/(1+zu)^(k-1). The boundary at zero vanishes because b>-1.
Also, Euler's real integral gives independently

    J_k=2F1(k,b+1;b+2;-z)/(b+1).

Positive z and b>-1 avoid a singularity on the integration path. Arb
outward evaluations of these formulas, including the power V^(b+1),
therefore enclose the exact primitive. All exact decompositions and all
recurrence versus direct hypergeometric values actually used are checked.
The two evaluations share Arb, so this is an internal formula check,
not an independent arithmetic implementation.

## Domain decomposition and scalar assembly

Let T_ab(V) be pi/2 times the sum of these primitives. Then

    E_ab(Dfar)=T_ab(1/(1+R^2)),
    E_ab(Dmid)=T_ab(1/(1+r0^2))-T_ab(1/(1+R^2)),
    E_ab(D0)=T_ab(1)-T_ab(1/(1+r0^2)).

Each is nonnegative by its integral definition, despite signed individual
branch groups. We require strictly positive enclosing intervals for the
actual references, and compare T_ab(1) group by group with the complete
Hessian calculation. Exact component and group hashes must match it.
The identities telescope, and interval overlap verifies the retained
numerical outputs. The relation to X, Y and kappa on each domain is

    X_D^2=E_xx(D)+E_xy(D), Y_D^2=E_xy(D)+E_yy(D),
    kappa_D^2=[(log2-1/2)X_D^2+(3log2-2)Y_D^2]/(16pi).

Both weights are positive. Thus squared quantities add across the three
domains. Norms themselves do not add. The fraction of the squared full
norm omitted from the nominal annulus is exactly the corresponding sum
of origin and far contributions divided by the complete squared norm.
The signed difference between the exact middle norm and the recorded
FLOAT value is retained separately; it cannot certify the FLOAT code.

## Evidence and limitations

Code, frozen publisher source text, exact inputs and verification output
are retained alongside this proof. Publisher source is read as text only.
The mesh audit is a separate own NumPy reconstruction of the documented
Gaussian rule and is marked FLOAT. All exact integrations use the raw
rational coefficients and outward ball arithmetic. No mesh sample is used
as an integral upper bound. All input hashes are verified, including the
complete Hessian results and their dependencies. This result does not
bound global theta, prove an inverse estimate or establish existence.
The new scaled Hessian results and this partition remain OPEN until an
independent lane reproduces the applicable calculation.
