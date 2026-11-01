# Audit of the finite-truncation exterior existence theorem

Status: historical initial audit. The repaired fixed-truncation existence theorem is PROVED in topic110 and V204; the objections below document the initial draft. The cross-truncation uniqueness inference is refuted by the explicit harmonic discrepancy in this note. No claim about convergence of the infinite canonical series is proved by this construction.

## Exact scope of the proposed theorem

The draft Theorem S fixes c>1, a smooth nonzero S1 leading density, a finite truncation N, a nonexceptional weight beta in (p_(N+1),p_N), and a regularity index k>=4. It constructs an exterior pair rho,psi solving

    (c x dot grad + u dot grad)rho=rho,
    -Delta psi=partial_x rho, u=(-partial_y psi,partial_x psi),

with rho-rho_N=O(r^beta), psi-psi_N=O(r^(beta+1)), and the corresponding finite derivative estimates. Different N, beta, cutoffs or regularity indices may produce different solutions or exterior radii. The draft does not construct a common potential or one smooth solution carrying all asymptotic orders.

The cutoff Poisson map in the draft is denoted Phi_beta. It solves

    -Delta Phi_beta[w]=partial_x(chi_T w),

with a weighted whole-cylinder Fourier inverse, where chi_T(t)=0 for t<=T+1 and chi_T(t)=1 for t>=T+2. This agrees with the desired exterior Poisson equation only beyond T+2. The auxiliary transport equation is solved on the larger cylinder t>T.

## Algebra and multiplier checks

With t=log r and mu=beta+1, the conjugated Poisson symbol on stream frequency q=2j>=2 is

    q^2-(i xi+mu)^2.

Its squared modulus is exactly

    ((q-mu)^2+xi^2)((q+mu)^2+xi^2).

Since beta<1 and beta avoids -3,-5,..., the symbol has a positive ellipticity constant relative to 1+q^2+xi^2. It therefore gains two derivatives, while its density forcing costs one derivative. The correction velocity gains no derivative relative to the density, as required by the iteration. The cutoff followed by zero extension is bounded at every fixed Sobolev order because it vanishes in a full neighborhood of the left boundary.

The transport signs in the draft also agree with the stationary equation. With a=e^(-2t)(Psi_t,Psi_theta), w=e^(beta t)v, and kappa=1-c beta>0, the operator is

    L_a v=(c-a^theta)v_t+a^t v_theta-(kappa+beta a^theta)v.

Its forward t component stays positive when a is small. Integration by parts gives a nonpositive boundary term at t=T in integral v L_a v, and hence a coercive estimate for -L_a. The stated future-characteristic integral has the correct minus sign. The cutoff produces no problem for the physical equation because the theorem restricts its conclusion to t>T+2.

The pressure conclusion follows from the Poisson equation and symmetry. Curl(u+(0,rho))=0. Reflection in x preserves this vector field with the usual vector parity and reverses the orientation of a circle, so its circulation is zero. A single-valued pressure therefore exists on the exterior annulus.

## Repairs needed in the Sobolev transport proof

1. In Step4(v), the displayed bound for the difference of mollified-coefficient transport operators uses

       ||a_e-a_f||_infinity ||v_f||_(W^(1,infinity))

   to control an L2 norm on an infinite cylinder. That bound is false. The correct estimate is

       ||(L_(a_e)-L_(a_f))v_f||_L2
          <= C_beta ||a_e-a_f||_infinity ||v_f||_H1.

   The already proved uniform Hk bound supplies the required H1 bound, so this repair preserves the argument. A simple failure of the old bound is a constant angular transport coefficient difference epsilon and v_L(t,theta)=eta_L(t)sin(theta), where eta_L is1 on an interval of length L and has uniformly bounded first derivative. The left side is comparable to epsilon sqrt(L), while the proposed right side is bounded by a constant times epsilon.

2. The Step4 lemma is stated for k>=3, but its last paragraph asserts H^(k-1) embeds in C1. At k=3 this is the false endpoint H2 to C1 in dimension two. Either state the lemma for k>=4, as its actual application already does, or use interpolation into H^(3-epsilon), 0<epsilon<1, and then embed into C1. One can also pass the equation in distributions and recover the stated regularity from the uniform Hk bound.

3. The iteration constant for (L_a-L_b)v must control the zeroth-order term beta(a^theta-b^theta)v as well as first derivatives. Define the constant to bound ||Dv||_infinity+|beta|||v||_infinity by ||v||_Hk, or insert the factor depending on beta explicitly.

4. Uniqueness must be stated for the auxiliary equation on all of t>T, with the fixed cutoff, fixed N,beta,T, and the stated correction norm. Merely imposing the physical equations on t>T+2 does not enforce the auxiliary equation in the cutoff strip. The proof's uniqueness argument uses that auxiliary equation on its full domain.

5. The symmetry statement should distinguish density S1 from stream S2. The fields do not both have the same angular sine parity.

These are repairs to the proposed proof and statement. They are not a counterexample to the fixed-truncation existence conclusion.

## Counterexample to the cross-truncation uniqueness inference

Choose c=3, delta=2/3, F_1=sin(theta), N=1 with beta_1=0, and N=2 with beta_2=-2/3. Both weights lie in the same interval (-1,infinity) used in draft Remark2. Their stream weights mu_1=1 and mu_2=1/3 lie strictly between -2 and2, so every stream mode uses the same two-sided Green kernel. Use the same admissible smooth cutoff with 0<=chi_T<=1.

The exact difference between the first two truncations is

    rho_2-rho_1 = r^(-1/3) f_2(theta),
    f_2 = -3sin(theta)/40 - sin(3theta)/40,

    psi_2-psi_1 = r^(2/3) g_2(theta),
    g_2 = 3sin(2theta)/640 + 3sin(4theta)/1120.

These coefficients are independently checked in topic102. Write P=2/3 and, for A>0, define the strictly positive finite integral

    I_A = integral_(-infinity)^infinity exp(A s)(1-chi_T(s)) ds.

For t>T+2 the cutoff Poisson inverse gives exactly

    Phi_(beta_1)[rho_2-rho_1] - (psi_2-psi_1)
       = -(3/80) I_(8/3) exp(-2t) sin(2theta)
         -(1/80) I_(14/3) exp(-4t) sin(4theta).  (1)

In particular it does not vanish.

To prove (1), consider one density component A_m exp(p t)sin(m theta), P=p+1, and its upward stream frequency q=m+1. Its cutoff forcing in the radial equation q^2-D^2 is

    (A_m/2) exp(Ps)[(P-q)chi_T(s)+chi_T'(s)].

The two-sided Green kernel is exp(-q|t-s|)/(2q). The uncut particular coefficient is -A_m exp(Pt)/(2(P+q)). For P+q>0 and t>T+2, subtract the uncut solution and integrate chi_T' by parts. The boundary terms vanish, giving the discrepancy

    (A_m/2) exp(-qt) I_(P+q).

For the downward frequency q=m-1>0, the forcing instead has (P+q)chi_T+chi_T'; the same integration by parts makes that discrepancy zero. Applying these formulas to the two coefficients in f_2 proves (1). Strict positivity of I_A follows because 1-chi_T is nonnegative and equals1 on a nonempty half-line.

Here the affine correction classes consist of functions on the entire auxiliary cylinder t>T, with the fixed cutoff and the stated weighted norms. Suppose the same pair on that full cylinder belonged to both classes. Write w_1=rho-rho_1 and w_2=rho-rho_2. Then w_1=w_2+(rho_2-rho_1). Since beta_2<beta_1, w_2 belongs to both weighted domains. The two Poisson maps agree on that common domain, as claimed in the draft. Linearity would imply

    0=(psi_2-psi_1)-Phi_(beta_1)[rho_2-rho_1],

contradicting (1). Thus the two full-cylinder affine velocity classes are incompatible even though their linear Poisson maps agree on common inputs. Operator equality does not identify classes translated by different truncations. This calculation does not rule out accidental agreement of the restricted exterior pairs if their extensions through T<t<T+2 differ: in that situation w_1-w_2 need not equal the truncation difference on the cutoff strip, and extra harmonic moments can enter. The counterexample invalidates the stated uniqueness inference, not every possible cross-N matching construction.

Consequently the draft Remark2 cannot infer a single solution with several truncations from weight independence and uniqueness. Its additional phrase about all N with p_(N+1)<beta is also missing an upper-order restriction and, literally, names infinitely many N. The safe conclusion is the fixed-N statement, with no cross-N identification unless a separate harmonic matching argument is supplied.

## Dependencies and verification scope

This audit uses the draft snapshot retained in sources, elementary Fourier multiplier algebra, the two-sided scalar Green function and the exact order2 coefficients of topic102. The multiplier and transport checks concern the proposed physical-space proof, not a formal-series convergence theorem. The primary remaining work is to inspect the corrected theorem and its auxiliary uniqueness class, then close the fixed-truncation result if every correction is incorporated.
