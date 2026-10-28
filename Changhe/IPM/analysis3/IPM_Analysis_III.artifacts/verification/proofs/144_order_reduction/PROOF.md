# Order reduction and the lower norms in the high-frequency estimate

## Statement

Use the cylinder C=R times S1, the smooth order s, the smooth bounded escape function Lambda, and the spaces X_s of proof 123. All derivatives of s and Lambda are bounded, 41/20<=s<=25/4, and s=25/4 on a fixed open neighborhood of the vertical cutoff support. Fix N>=0 and write

 A_v=Op(e^(N Lambda(X))<xi>^s(X)),  A_u=e^(N Lambda(X))<D>^(25/4).

Use a uniform, properly supported quantization, with any smooth low-frequency convention. The same conclusions hold for the usual global left quantization; its difference from the properly supported version has a uniformly smoothing kernel. Constants below may depend on N and the fixed cutoffs. For every 0<epsilon<=1/32:

 (i) ||A_v v||_2<=C||v||_(H^s),
     ||v||_(H^s)<=C(||A_v v||_2+||v||_(H^(s-epsilon))).       (1)

 (ii) ||A_v v||_(H^(-r))<=C_r||v||_(H^(s-r)), 0<=r<=1.       (2)

The same statements hold with s replaced by the constant 25/4 and A_v by A_u. In particular the sum of the squares of the two order-reduced L2 norms, plus ||h||_(X_(s-epsilon))^2, is equivalent to ||h||_(X_s)^2. No invertibility of the bare left-quantized A_v at low frequency is assumed.

For the cofactor component u=chi h/(b p), choose nested open vertical sectors with closure(supp chi) strictly inside Q_1 and closure(Q_1) strictly inside Q_2, on which s=25/4. If psi=1 on Q_1 and supp psi is contained in Q_2, then for every integer K>=0,

 ||(1-psi) A_u u||_(H^K)+||(1-psi) R A_u u||_(H^K)
                          <=C_K ||u||_(H^(25/4-epsilon)),    (3)

where R=grad<D>^(-1). Thus sector positivity may be applied to R A_u u after angular localization; its discarded part has a lower-norm bound. It must not be justified by claiming that A_u u retains the support of u.

## Smooth variable-order calculus

The smooth calculus used here is the scalar case of Krainer and Mendoza, Elliptic systems of variable order, arXiv:1301.5820, Propositions4.4,4.11,4.12 and5.2. The retained PDF and text are in references/finite_regularity. Its scalar bundle action is multiplication by the real smooth function s(X). On each coordinate patch choose its oscillation smaller than any fixed d in (0,1); this is the admissibility condition in their Definition2.1. Bounded derivatives of s permit a uniform patch size. Multiplication by <xi>^s is an elliptic order-zero map from the s-twisted bundle to the ordinary scalar bundle. Smooth bounded e^(N Lambda) does not change ellipticity. The composition expansion loses at least 1-d orders per frequency derivative; derivatives of s introduce logarithms which can be absorbed by any smaller positive power.

For clarity, the global use of this local theorem involves no compactness of C. Cover C by uniformly sized patches of bounded overlap, with translated cutoffs whose derivatives have common bounds. Local symbol estimates, ellipticity radii and the finite number of seminorms in each mapping estimate are uniform. Proper support reduces every output patch to finitely many neighboring input patches. Sum their squared estimates. A global nonproper quantization differs from this one away from the diagonal. Repeated frequency integration by parts makes that difference a kernel of arbitrary negative order with arbitrarily summable decay in the distance between patches. The order function is bounded, so one chooses the number of integrations larger than its full oscillation and the required source and target orders. This gives the same global mapping and parametrix estimates.

Choose d=1/4. The elliptic parametrix B of A_v has principal symbol e^(-N Lambda)<xi>^(-s), with

 B A_v=I+K,   K:H^(s-epsilon)->H^s bounded.                 (4)

Indeed even a finite first correction leaves a remainder of relative order at most -3/4; further corrections, if used for a prescribed quantization, only improve this. The low-frequency error is smoothing, with uniform estimates. Also B:L2->H^s is bounded. Applying (4) gives the second inequality in (1), and the direct mapping theorem gives the first. This proof does not assert that I+K is invertible. A possible low-frequency kernel is harmless.

The composition <D>^(-r) A_v is of variable order s-r, with principal symbol e^(N Lambda)<xi>^(s-r). The same mapping theorem proves (2), including r=0. The cofactor assertions either follow from the constant-order case or from the same calculus. Bounded smooth multiplication by e^(N Lambda) and its inverse is allowed at every displayed order.

## The support correction

The supports of (1-psi) and u are separated by a fixed positive angular distance. The kernel of A_u is smooth away from the diagonal. Its derivatives of any fixed order have arbitrarily summable decay in the radial-cylinder separation by frequency integration by parts. This remains true after R, which has order zero. Therefore the two off-support operators in (3) map H^(25/4-epsilon) to H^K uniformly in radial translation. One may factor through an arbitrarily negative input order; the weaker displayed estimate suffices. A partition in t and Schur's test give the global estimate. There is no radial support assumption on u.

In particular, a bounded matrix field M which is at least mu I only on Q_2 satisfies

 <M R A_u u,R A_u u>
   >=mu||R A_u u||_2^2-C||h||_(X_(s-epsilon))||h||_(X_s),    (5)

if M has any bounded extension outside Q_2. To see this, split the integral over Q_2 and its complement, use positivity on Q_2, boundedness outside, and (3). The off-support square is bounded by the product in (5), since the lower norm embeds in the high norm. The identity ||Rw||_2^2=||w||_2^2-||w||_(H^-1)^2 is exact on the flat cylinder. Equation(2) controls the latter term. This proves the sector version of the matrix positivity step without an unsupported support assumption.

## Scope

These results repair input Q0 in the theory author's Proposition Hs and its sector positivity step. They do not prove the finite-regularity transport conjugation, the local coupling commutator, the transport graph-core assertion or the complete Hs estimate. Proof 143 already controls the logarithmic form remainder once (2) is used. Constants are qualitative; no value of N or an inverse constant is certified.
