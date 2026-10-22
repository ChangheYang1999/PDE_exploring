# A negative direction for unweighted density energy

Status: analytic test and explicit X3 point witness independently checked with Arb and mpmath.iv. This statement concerns coercivity of one pairing and does not imply noninvertibility or nonexistence.

## Statement

Let a background density bar-rho have the prescribed parity, C^1 regularity, and canonical velocity bar-U in C^1. Put bar-V=c_l X+bar-U, with div bar-U=0, and

L_0 h = bar-V dot grad h -h +U[h] dot grad bar-rho.

Suppose there is a point in the open first quadrant where

(bar-rho_x-bar-rho_y)/2 > c_l+1.

Then the quadratic form -integral h L_0 h is negative for some smooth, compactly supported, parity-compatible h=x^2 y g, where g is smooth and g(0)=0, and satisfying c[h]=0. Thus a positive lower bound in the unweighted density L2 pairing is false. The same tests apply to L=L_0+c[h]G because the rank-one term vanishes exactly.

## Proof

Choose a small rectangle around the stated point where the strict inequality persists, and a nonzero smooth real cutoff b supported in that rectangle. Put

Phi_N=(1/(2N^2)) b(x,y) cos(N(x+y)),  h_N=-Delta Phi_N.

Reflect Phi_N evenly in x and oddly in y, with disjoint supports, and define h_N after reflection. These potentials and densities vanish on a neighborhood of both axes and the origin. Thus h_N/(x^2 y), defined as zero near the axes, is smooth and compactly supported, and its value at the center is zero. The canonical stream function of h_N is partial_x Phi_N, because -Delta(partial_x Phi_N)=partial_x h_N and the resulting velocity is compactly supported. Consequently U[h_N]=(-Phi_{N,xy},Phi_{N,xx}) and c[h_N]=Phi_{N,xxy}(0)/3=0.

On the original rectangle, direct differentiation gives, in L2,

h_N=b cos(N(x+y))+O(N^{-1}),
U_1[h_N]=(1/2)b cos(N(x+y))+O(N^{-1}),
U_2[h_N]=-(1/2)b cos(N(x+y))+O(N^{-1}).

The reflected rectangles have the same quadratic contributions by the background parity and the reflection law for the potential. Integration by parts, with no boundary terms, gives

-integral h_N L_0 h_N = (c_l+1) integral h_N^2 - integral h_N U[h_N] dot grad bar-rho.

Here integral h_N bar-V dot grad h_N = -c_l integral h_N^2, since div bar-V=2c_l. Substituting the three expansions yields, on each reflected copy, the limit

(1/2) integral b^2 [c_l+1-(bar-rho_x-bar-rho_y)/2] <0.

The cos(2N(x+y)) terms tend to zero by integration by parts, or the Riemann-Lebesgue lemma for compactly supported continuous coefficients. All O(N^{-1}) terms tend to zero by Cauchy-Schwarz and the bounded background gradient on the support. For all sufficiently large N the quadratic form is therefore strictly negative.

## Why a point enclosure suffices

The strict gradient inequality at one point, once certified, persists in an open rectangle by the continuous exact trial derivatives. No numeric radius or frequency is needed to refute the universal positive coercivity claim: the existential cutoff construction provides smooth admissible tests. This argument supplies no eigenvalue and no inverse estimate.

## Independent point-evaluation formulas

Let t=log(r/L), q=1-(1+(r/L)^2)^(-(1-k)/2), s=(r/L)^2/(1+(r/L)^2), chi=(r/L)^2/[(r/L)^2+r_0^2], and q_t=(1-k)s(1-q). Write the radial mode amplitudes R_m=chi^{j_m} b_m(q), j_m=max(m-1,0). Then

(R_m)_t=chi^{j_m}[b_m'(q) q_t +2 j_m(1-chi)b_m(q)].

For the singular amplitude Z=s^{p/2}T(2q-1),

Z_t=p(1-s)Z +2s^{p/2}T'(2q-1)q_t.

Insert these into S_t and S_theta, and use H_t=(k-3)s+S_t. The derivative of the angular singular factor on 0<theta<pi/2 is

partial_theta[cos^{p-2}(theta)sin^2(theta)] = 2 cos^{p-1}(theta)sin(theta) -(p-2)cos^{p-3}(theta)sin^3(theta).

With A=cos^2(theta)sin(theta), A'=cos^3(theta)-2cos(theta)sin^2(theta), density derivatives are

rho=r^3 exp(H) A,
rho_t=(3+H_t)rho,
rho_theta=r^3 exp(H)(A'+A H_theta),
rho_x=(rho_t cos(theta)-rho_theta sin(theta))/r,
rho_y=(rho_t sin(theta)+rho_theta cos(theta))/r.

These identities are obtained by differentiating the explicit trial formula. The implementation differentiates the exact degree-seven spline polynomial on a rigorously checked knot span and uses outward Arb arithmetic. It imports the scalar certificate's exact-input reader, not the numerics lane's defective point evaluator.

## Exact witness and scope

The background here is the exact dyadic-input X3 density, and the held dilation parameter is defined mathematically as c_l=1/k. The stored rounded c_l is recorded separately and is not used in the witness. At r=25/2 and theta=31/25, the two independent implementations give

- rho_x in [19.70073669508093,19.70073669508094],
- rho_y in [-0.57349632166395,-0.57349632166394],
- (rho_x-rho_y)/2-(1/k+1) in [3.56175389773089,3.56175389773090].

These outward decimal intervals are wider than the saved balls. The first implementation uses Arb evaluation of the exact degree-seven span polynomial and handwritten differentiation. The second uses mpmath.iv, Cox basis recursion, forward Chebyshev recursion, and independent forward automatic differentiation. The input dimension check establishes that exactly six Chebyshev coefficients are present. The scalar normalization defect is unrelated to the sign test: the test concerns this trial and this held dilation parameter.

The same two implementations certify the stronger margin

(rho_x-rho_y)/2-7 > 3.13.

Thus the negative direction exists for every dilation parameter c_l<=6 with the same density. This includes the held 1/k, directly checked to be below 6, and includes the canonical (1+c)/3 once the independent scalar enclosure c<17 is adopted. The proof of this stronger gradient inequality requires no strain computation. A correction preserves normalization by having center factor zero; the corrected background continues to have center factor one.

The canonical case uses ../canonical_inverse/evidence/strain_arb_20_32_result.json, SHA256 16135e23513f905fb835c57df9dbd424f5efe0b7d5fe76831bb18221520723db, together with its final_audit_manifest.json. Its certified upper endpoint is below 17. The held and all-c_l<=6 statements do not depend on that scalar file.
