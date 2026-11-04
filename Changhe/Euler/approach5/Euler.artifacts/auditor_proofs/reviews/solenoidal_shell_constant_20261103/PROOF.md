# A rigorous interval for the solenoidal shell constant

Status: CONFIRMED at the angular variational and profile-corollary scopes below. A single exact trial is certified. The optimal decimal value near1.712 is not proved.

## 1. Exact constants and hypotheses

For unit e,e' in R3 and0<alpha<=1, put

    M_alpha=e'e'^T-alpha ee^T,
    k_alpha(theta)=theta cross M_alpha theta,
    J_k(phi)=(3/(4pi)) integral_(S2)
                   sqrt(|k-grad_S phi|^2+4phi^2),
    D_alpha=sup_(e,e') inf_(phi in C1(S2)) J_(k_alpha)(phi).

All angular integrals use ordinary area measure and Euclidean norms. At alpha=1, D1 equals the infimum for M=diag(1,-1,0), because the eigenvalues of e'e'^T-ee^T are0 and plus/minus sin(beta), where beta is the angle between e and e'. Orthogonal changes of coordinates and scaling phi give the exact factor sin(beta).

Then

    1+alpha/2<=D_alpha<=D1+1-alpha,
    3/2<=D1<1.720646.                                    (1)

The upper certificate uses the exact rational a0=107/200 and phi=a0xyz on S2. It supplies a uniform angular estimate, not just an orientation-specific bound.

For the profile corollary, use the full exact C2 Euler equation and hypotheses of A1223: any finite omega,0<c<1, uniform U->0, |U|<=CU(1+r)^(-a),0<=a<=3/2. Put Gamma_a=min(c(1+a),1). The already confirmed C49/C50 transport proof, with the verified shell replacement below, gives

    limsup_(r->infinity)|curl U|<Gamma_a/1.720646
       implies DU->0 and |curl U|+||DU||=O(1/r).           (2)

For c>1/3 the natural derivative rate O(r^-1/c) follows. Under the campaign natural tail the threshold is1/1.720646>0.58117. Constants may depend on the profile and fixed omega. No helicity assumption is used, and no unrestricted nonexistence statement follows.

## 2. Fixed-test-function shell inequality

Let f=chi0 xi on the shell rho<|p-z|<1, with |xi|<=w, div xi=0, and chi0 equal to one near the inner ball. Assume the support of grad chi0 has distance at least1/2 from p, as in the verified C50 decomposition. Write theta=(p-z)/|p-z| and

    Phi(r theta)=r^-2 phi(theta),
    grad Phi=r^-3(grad_S phi-2phi theta).

Integration by parts changes the combined degree-minus-three strain kernel k into k-grad_S phi+2phi theta. Each spherical boundary costs at most4pi w||phi||infinity, since its area and r^-2 factor cancel. The volume term has div f=xi.grad chi0 at distance at least1/2, so it costs at most Cw||phi||infinity. All remainders are independent of rho.

As k and grad_S phi are tangent, the new angular norm is precisely the integrand defining J. Radial integration supplies J_k(phi)w log(1/rho), with a remainder O_phi(w). This estimate is valid for each fixed phi and both signs of the strain expression. It does not assume a minimizer exists.

For the optimized infimum, choose near-minimizers on a finite cover of the compact pair-orientation space. The inequality

    |J_k(phi)-J_l(phi)|<=(3/(4pi))integral|k-l|

is uniform in phi. Thus any coefficient D_alpha+epsilon can be used with one finite remainder constant, and strict exponent inequalities absorb epsilon. For the explicit trial below a simpler uniform family is available, so no optimized-minimizer regularity is needed.

## 3. Exact lower obstruction

For the orthogonal pair e'=e1,e=e2,

    k_alpha=(alpha yz,xz,-(1+alpha)xy).

Define almost everywhere

    g=sgn(x)(0,z,-y)/sqrt(1-x^2).

It is tangent and has norm one. To justify integration by parts without an interface assumption, use the smooth tangent fields

    g_epsilon=x(theta cross e1)/
               (sqrt(x^2+epsilon^2)sqrt(1-x^2+epsilon^2)).

Their norm is at most one, they converge to g almost everywhere, and they have zero surface divergence: theta cross e1 is the infinitesimal rotation about e1, and its scalar coefficient depends only on the preserved coordinate x.

For every C1 phi,

    integral g_epsilon.grad_S phi=0,
    g_epsilon.theta=0.

Pointwise norm duality and dominated convergence therefore give

    J_(k_alpha)(phi)>=(3/(4pi))integral k_alpha.g.

In coordinates x=t, y=sqrt(1-t^2)cos(v), z=sqrt(1-t^2)sin(v), the surface area element is dt dv. The last integral equals

    (3/(4pi)) 2pi(2+alpha) integral_0^1 t sqrt(1-t^2)dt
       =1+alpha/2.

Taking the infimum and then the orientation supremum proves the lower inequality in (1). In particular D1>=3/2. This is an analytic lower bound, independent of optimization trials.

The zero-homogeneous extension of each g_epsilon is divergence-free away from the origin. A smooth radial cutoff preserves zero divergence because the field is tangent. Cut it off away from the origin and outside a fixed ball, while keeping it unchanged on shells of arbitrarily large logarithmic aspect ratio. Their bounded solenoidal strain integrals have coefficient arbitrarily close to3/2. Consequently no universal coefficient-one shell inequality with a remainder independent of that aspect ratio holds for this class. These fields are test fields for a kernel inequality, not Euler profiles.

## 4. Variational interpretation and its exact limitation

Consider the linear operator Aphi=grad_S phi-2phi theta from C1(S2) into L1(S2;R3). The distance from k to the closure of its range equals the supremum of its pairing against unit L-infinity fields annihilating the range, by the Hahn-Banach distance formula. Integration by parts identifies that annihilator as

    div_S g_T+2g_R=0

in distributions. Therefore

    D1=(3/(4pi))sup integral k.g_T,

where the supremum is over measurable g with ||g||infinity<=1 satisfying this equation. This is exactly the divergence-free condition for its zero-homogeneous extension on punctured R3. Thus D1 is the sharp angular coefficient for bounded homogeneous solenoidal shell fields. The statement does not include additional Euler constraints or assert that every dual field extends smoothly through the origin. The explicit tangent family in Section3 already suffices for the coefficient-one obstruction.

## 5. Exact trial and independent upper certificate

For k=(yz,xz,-2xy), phi=a0xyz and x^2+y^2+z^2=1,

    P:=|k-grad_S phi|^2+4phi^2
      =(1-a0)^2 z^2(x^2+y^2)+(2+a0)^2x^2y^2
                                   -5a0^2x^2y^2z^2.     (3)

To verify it, grad_S(xyz)=(yz,xz,xy)-3xyz theta. Its squared norm is x^2y^2+x^2z^2+y^2z^2-9x^2y^2z^2, and k.grad_S(xyz)=y^2z^2+x^2z^2-2x^2y^2. Expanding gives (3).

Use equal-area coordinates z in[0,1], v in[0,pi/4]. Sign changes and interchange of x,y give symmetry factor16. Put s(v)=cos(v)^2 sin(v)^2. Then

    P=(1-a0)^2z^2(1-z^2)
          +[(2+a0)^2-5a0^2z^2](1-z^2)^2s(v).

Each rectangular cell has an exact integral determined by the antiderivatives

    z^3/3-z^5/5,
    z-2z^3/3+z^5/5,
    z^3/3-2z^5/5+z^7/7,
    v/8-sin(4v)/32.

Cauchy-Schwarz gives integral_cell sqrt(P)<=sqrt(area_cell integral_cell P). Summing is therefore a rigorous upper bound, with no quadrature-error assumption. The supplied independent script uses a128by128 partition, exact rational a0=107/200, and160-bit Arb ball arithmetic. Its question and strict PASS criterion were written before execution. The complete script was read before running it on one low-priority CPU55 with one thread.

The computed upper sum is

    [1.7206453391453974373606589359973327669054167
         +/-2.46e-44] < 1720646/1000000.

The strict comparison is between Arb balls and the exact rational threshold. All cell integrals had positive enclosures; no negative interval was clipped. The real start and end times,0.043seconds apart, are in the team records. This proves D1<1.720646. It does not certify the optimal value or reuse the source's floating-point optimization. The source also reports a finer240by240 upper bound; the present proof only needs and independently certifies the displayed bound.

## 6. Uniform pair estimate from the trial

For alpha=1, rotate and scale the same trial with the eigenspaces of M1. Its coefficient is at most1.720646 sin(beta), and its supremum norm is uniformly bounded by a fixed multiple of |a0|. No continuity in the eigenbasis choice is necessary: for each kernel inequality one chooses a basis, and all bounds are independent of that choice.

For alpha<1, M_alpha=M1+(1-alpha)ee^T. The triangle inequality adds at most1-alpha to the coefficient, because

    (3/(4pi))integral|theta cross ee^T theta|=1.

Thus the fixed-trial family yields the uniform coefficient

    C_alpha=min(1+alpha,1.720646+1-alpha).                  (4)

The first choice uses phi=0. Near alpha=1 this lies between1 and1+alpha, so0<=1+alpha-C_alpha<=alpha. Its remainder is uniform because the trial suprema are uniform. The same triangle inequality with near-minimizers proves D_alpha<=D1+1-alpha.

The combination of the kernel replacement, the original small and intermediate regions, and the original separation estimate is exactly the C50 pair inequality with C_alpha in place of its old angular coefficient. All other constants contribute to its already allowed O(w) remainder. This establishes the uniform input needed for the full profile proof, not just its formal variational expression.

## 7. Profile consequence and method ceiling

The confirmed C50 transport proof uses its coefficient only through the uniform shell inequality,1<=C_alpha<=1+alpha, and the strict exponent condition gamma>C_alpha W0/alpha. These are now verified by (4). In particular its separation condition gamma>W0 follows as before. The sign of the excess coefficient, small-pair scale, integrating-factor bound, finite-time Holder continuity and first-contact barrier are unchanged. No bound on an optimizing phi or new unproved regularity result enters.

For every gamma>1.720646 W0 choose alpha<1 close enough to one that gamma>C_alpha W0/alpha. The same theorem therefore proves the exterior logarithmic Holder bound with power gamma/c. If omega_inf<Gamma_a/1.720646, choose W0 between these quantities and gamma between1.720646 W0 and Gamma_a. A1223 applies and proves (2). The exact rational comparison gives1/1.720646>0.58117. One may likewise improve the old C50/A757 natural-tail gap to1/(2*1.720646)>0.29058, although A1223 gives the stronger current result.

The lower bound D1>=3/2 means the optimized version of this same angular shell method can at most approach natural-tail threshold2/3 in the TV argument, or1/3 in the older A757 argument. It does not show an obstruction for all divergence-free methods, and it does not prove that these ceilings are attained. The trials near1.712 give upper bounds only. Endpoints and unrestricted profile nonexistence remain open.

## 8. Reading coverage and collaboration

The revised source R2 addendum, the complete source check script and its log, and the whole added Section7 of the inner pair review were read. The older C50 proof is a previously completely audited dependency, A1171-A1177; the immutable inner whole proof is retained as provenance, not claimed freshly read in full. The above reconstruction verifies every new step used here. The independent certificate and source hashes are retained beside this proof.

The Theory Agent A author is an existing configured model agent, with runtime identity unattested. The inner the external referee (a second model) review records failed credential retrieval and no model response. It is not counted as a model consultation. A focused comparison is requested through existing working files for the lower-bound quantifiers and the uniform-trial replacement in the profile corollary. No new agent or client is launched.
