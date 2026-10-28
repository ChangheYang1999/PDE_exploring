# Two sufficient injectivity certificates and regular-cylinder errors

## Scope and exact Hilbert-space conventions

All Hilbert spaces below may be real or complex; adjoints use their
specified inner products. These are sufficient conditions. None of the
finite-rank or complement estimates below has been established for the
actual modal IPM operator by this note. In particular the positive
remainder margin of proof 68 is not automatically a coercivity constant
for a bounded, preconditioned realization on the full jet space.

## Finite adjoint witnesses

Let F:H->H be bounded and Fredholm of index zero. Let K:H->H0 be bounded
and suppose, for every u in H,

 m ||u|| <= ||Fu|| + ||Ku||,   m>0.

Suppose K=Ksmall+E Phi*, where ||Ksmall||<=delta, E:C^n->H0 is an
isometry and Phi:C^n->H is bounded. Suppose W:C^n->H satisfies

 ||W||<=Psi,   ||F* W-Phi||<=epsilon.

If d=m-delta-epsilon>0, then F is invertible and

 ||F^(-1)|| <= (1+Psi)/d.                                      (1)

Indeed the isometry gives ||E Phi*u||=||Phi*u||. Subtracting the small
part from the weak lower bound and inserting W*Fu yields

 (m-delta)||u|| <= ||Fu||+||Phi*u||
 <= (1+Psi)||Fu||+epsilon||u||.

Thus F is injective with closed range and lower bound d/(1+Psi).
Index zero makes its cokernel zero, proving (1). If r_i=F*psi_i-phi_i
are the columns of the residual, Cauchy-Schwarz gives

 epsilon <= (sum_i ||r_i||^2)^(1/2).

A direct residual Gram bound can be smaller. If T:Z->Y is the transport
isomorphism of proof 76 and F=L T^(-1):Y->Y, the conclusion is

 ||L^(-1)||_(Y->Z) <= ||T^(-1)||_(Y->Z) (1+Psi)/d.

Every constant must refer to these particular norms. For example, in
a single Hilbert space without jet coordinates, L=T+C and ||C||<=b,
a weak estimate m0||h||<=||Lh||+||K0h|| implies only

 [m0/(m0+b)] ||u|| <= ||L T^(-1)u||
                 +[b/(m0+b)] ||K0 T^(-1)u||,   u=Th.

This follows from ||u||<=||Lh||+b||h|| and substitution. It explains
why replacing m by the raw margin m0 is not justified.

## A finite block and a complement inverse

Let F:H->H be bounded and Fredholm of index zero. Let P be an orthogonal
finite-rank projection and Q=I-P. Suppose D=QFQ:QH->QH is bijective and

 ||D^(-1)||<=1/d,  ||PFQ||<=b,  ||QFP||<=c,
 ||PFP p||>=a||p|| for all p in PH,

where d>0 and a-bc/d=:s>0. Then F is invertible. Put

 p0=sqrt(1+(b/d)^2)/s.

A valid bound is

 ||F^(-1)|| <= sqrt(p0^2+((1+c p0)/d)^2).                       (2)

For Fu=f and u=p+q, the Q equation gives

 ||q|| <= (||Qf||+c||p||)/d.

Insert this into the P equation and use its lower bound to get

 s||p|| <= ||Pf||+(b/d)||Qf|| <= sqrt(1+(b/d)^2)||f||.

First apply these equations with f=0 to prove injectivity. Index zero
then gives existence for each f; the same inequalities and the
orthogonality of p,q give (2). The fact that D is bijective is essential.
A finite-section singular value, even with a small image tail, supplies
neither this fact nor either cross-block bound.

## Explicit regular-cylinder commutator

This section is on the periodic cylinder with periods ell and 2pi,
normalized area measure and lattice

 Gamma={(2pi j/ell,n):j,n integers}.

For a scalar coefficient a, let a_hat(q) be its Fourier coefficient and
S1(a)=sum_q |q||a_hat(q)|<infinity. Let M be a scalar or matrix multiplier
bounded by M0 on Gamma. Assume a continuously differentiable extension
satisfying ||grad M(p)||<=M1/|p| for |p|>=Lambda/2. Let Q_Lambda retain
lattice frequencies |p|>=Lambda>0. Then

 ||[a,M]Q_Lambda|| <= max(2M1,4M0) S1(a)/Lambda.                (3)

The entry from p to p+q is a_hat(q)(M(p)-M(p+q)). When |q|<=Lambda/2,
the line segment stays at radius at least |p|/2>=Lambda/2; integrating
the derivative bounds the difference by 2M1|q|/Lambda. For larger q,
it is at most 2M0<=4M0|q|/Lambda. Young's convolution inequality on the
lattice proves (3). A second valid bound is the SUM

 2M1 S1(a)/Lambda + 2M0 sum_(|q|>Lambda/2) |a_hat(q)|.           (4)

The two terms in (4) cannot be multiplied or concatenated. The latter
sum is at most (2/Lambda)^p Sp(a), with
Sp(a)=sum_q |q|^p|a_hat(q)|, when finite.

For derivative data Dij=||partial_t^i partial_theta^j a||_infinity,
put

 D3^2=D10^2+D01^2+2(D20^2+2D11^2+D02^2)
                         +D30^2+3D21^2+3D12^2+D03^2.

Cauchy-Schwarz and Parseval, using normalized measure, give

 S1(a)<=C_ell D3,   C_ell^2<=1+pi/2+3ell/4.                    (5)

In detail the first factor in Cauchy-Schwarz is the square root of
sum_q(1+|q|^2)^(-2); the other squared factor is
sum_q |q|^2(1+|q|^2)^2|a_hat(q)|^2, bounded by D3^2. With h=2pi/ell,
monotonicity bounds the sum over j, for each n, by

 (1+n^2)^(-2)+(pi/(2h))(1+n^2)^(-3/2).

The sums over n are at most 1+pi/2 and 3 respectively, yielding (5).

## Principal coupling estimate on that regular cylinder

Let g=(g1,g2) be a real smooth vector field. Let R_theta rotate radial
and angular coordinates to Cartesian coordinates, and set

 B=R_theta^T [[-g2,g1/2],[g1/2,0]] R_theta,
 bplus=(|g|-g2)/2, b_eta=(sqrt(|g|^2+eta^2)-g2)/2, eta>0.

The largest eigenvalue of B is bplus and
0<=b_eta-bplus<=eta/2. Let Sj have multiplier p_j/|p|, zero at p=0,
and Cpr=sum_ij B_ij Si Sj. For v=Q_Lambda v,

 Re<Cpr v,v> <= integral bplus |v|^2
   +[eta/2 + (4/Lambda)(sum_ij S1(B_ij)+2S1(b_eta))]||v||^2.    (6)

To prove (6), commute Si past B_ij. The error is at most
(4/Lambda)sum_ij S1(B_ij)||v||^2 by (3), since M0=M1=1 for Si.
The resulting quadratic form sum_ij<B_ij Sjv,Siv> is bounded by
sum_j<b_eta Sjv,Sjv>. Commute Sj back, using sum_j Sj^2v=v since v
has no zero frequency. Two further applications of (3) cost
(8/Lambda)S1(b_eta)||v||^2. Finally replace b_eta by bplus+eta/2.

This is a calculation in a regular periodic chart. It does not cover
the singular factor |cos(theta)|^(-17/4), the kink of a radial weight,
Taylor subtraction, local cutoffs, or the jet and normalization rows.
Their errors are additional terms and must be bounded separately.

## Rank and conformity

On this periodic cylinder, the real parity class has angular modes
sin(n theta), n positive and odd. A disk cutoff has real dimension

 N(Lambda,ell)=sum_(1<=n<=Lambda,n odd)
       [2 floor((ell/(2pi))sqrt(Lambda^2-n^2))+1]
       =ell Lambda^2/8+O(ell Lambda+Lambda).

The exact count follows by counting the radial Fourier modes for each
angular mode, including the real sine/cosine pair for each j>0. The
leading term is the quarter-disk area with density ell/(4pi), counting
both signs of the radial mode. This is a model finite-dimensional
count only. Band limiting on the whole real radial line has infinite
rank, so no finite-rank conclusion follows without localization.

Raw angular projection can destroy the order-four axis vanishing
required by the actual remainder weight. A conjugated projection
J^(-1) P J is bounded on the weighted L2 space when J is its exact
isometry, but its range must separately be proved to lie in the
transport domain. A bounded orthogonal L2 projection is not by itself
a conforming graph-domain section.

## Audit dependency

This note independently supplies the elementary arguments used in the
theory author's INJ_cap consultation. It corrects the missing plus sign in the
consultation's displayed sharper commutator bound. No actual compact
error, adjoint residual, complement inverse, cutoff, or inverse norm
has been certified here. Those are open numerical and analytic inputs.
