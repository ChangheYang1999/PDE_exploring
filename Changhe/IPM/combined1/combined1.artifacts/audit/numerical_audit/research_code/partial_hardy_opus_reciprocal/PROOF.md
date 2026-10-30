# Independent reciprocal audit of the complete angular prefix bound

Written UTC 2026-10-29T16:50:56.873790+00:00 before the checker. This result compares the two existing Opus theory reviews with an independent argument and exact compositions. It makes no existence or inverse claim.

## Statement, spaces and notation

Let F be a real locally integrable function on R^2, even in x and odd in y. Put r=|(x,y)| and assume rF belongs to L^2(R^2). For positive odd n set f_n(r)=pi^(-1) integral_0^(2pi) F(r,theta)sin(n theta)dtheta, S_n=pi integral_0^infty r^3 f_n(r)^2 dr, and S=||rF||_2^2. Define H(F) as the supremum of |integral F phi| over phi in C_c^infty(R^2) with ||grad phi||_2<=1. Then S=sum S_n and

 H(F)^2 <= M^2 := sum S_n/n^2 <= B_N := S/N^2 + sum_(odd n<N)(n^(-2)-N^(-2)) S_n

for every positive odd N. Every lower mode must be included or proved zero. Moreover B_N decreases to M^2, and

 0 <= B_N-M^2 = sum_(n>N)(N^(-2)-n^(-2))S_n <= N^(-2)sum_(n>N)S_n.

For enclosing data L_n<=S_n<=U_n and U>=S, the positive expression P=U/N^2+sum_(n<N)(n^(-2)-N^(-2))U_n is an upper. The split upper Q=sum_(n<N)U_n/n^2+(U-sum_(n<N)L_n)/N^2 satisfies Q-P=sum_(n<N)(U_n-L_n)/N^2. Equality requires precisely zero included interval widths; U need not equal S.

If finitely many tests of distinct positive odd frequencies give L^2 divergence-free fields Z_j with a_j=||Z_j||_2^2>0, b_j=<A_F,Z_j>, then H(F)^2<=P-sum b_j^2/a_j. Positive lower bounds for b_j^2/a_j may replace these terms. Same-frequency tests cannot be added as if orthogonal: use their Gram matrix or select one improvement.

## Complete argument

The symmetry removes cosines, the constant, and even sines. Polar Fubini and Parseval give S=sum S_n. Define A_F=-e_theta r sum f_n(r)cos(n theta)/n. Its series converges in L^2 with squared norm M^2<=S. For almost every r, the angular antiderivative has derivative rF in the circle distribution sense. For compact smooth phi, angular integration by parts and Fubini therefore give integral A_F dot grad phi=-integral F phi on the entire plane. Both integrals are absolutely integrable: the first by Cauchy-Schwarz and the second by local integrability. Equivalently, annular radial cutoffs introduce no derivative term because A_F is tangential. Thus there is no unverified origin contact term. Cauchy-Schwarz proves the H bound.

The coefficient of S_n in B_N is max(n^(-2),N^(-2)). Subtracting n^(-2) proves the displayed loss formula and bound. Subtracting adjacent B values gives ((N+2)^(-2)-N^(-2))sum_(n>N)S_n<=0; the loss tends to zero. Positivity of all included coefficients proves P. Direct subtraction proves Q-P, including its equality condition. These statements also hold for finite spectra.

Every A_F+sum t_j Z_j has distributional divergence F. Orthogonality of distinct frequencies gives its squared norm M^2+sum(2t_j b_j+t_j^2 a_j). Minimizing each quadratic gives t_j=-b_j/a_j and the improved bound. The exact radial test identities and cutoff admissibility are the separately accepted general469 result, bound through N4-404 and N4-408. Local integrability of F is a genuine extra hypothesis: F=sgn(y)/(r^2 |log r|) on 0<r<1/2 has ||rF||_2^2=2pi/log2 but integral |F|=infinity.

## Exact independent fixtures

For F=(1+r^2)^(-3)sgn(y), the sine coefficients are 4(1+r^2)^(-3)/(pi n). Its continuous periodic angular antiderivative g(theta)=(pi-2|theta|)/2 on [-pi,pi] has g'=-sgn(theta), so A_F=-e_theta r(1+r^2)^(-3)g. It gives S=pi/20 and M^2=pi^3/240. Here integral r^3(1+r^2)^(-6)dr=1/40; direct polynomial integration of g^2 gives pi^3/6. For phi=P(x,y)(1+r^2)^(-4), pairings follow by monomial integration. If i is odd or j even, integral F x^i y^j(1+r^2)^(-4)=0. Otherwise it equals B((j+1)/2,(i+1)/2) B((i+j+2)/2,7-(i+j+2)/2), where B is the beta integral. Half-integer gamma values give the exact rational multiples of pi listed in the source JSON, with a minus sign for integral A_F dot grad phi. These tests decay and the preceding identity extends by cutoffs, since both required integrals converge.

For psi=r(1+r^2)^(-3/2)sin(theta), the cross b=-256/1155 and a=3pi/8. To calculate b directly, put t=r^2/(1+r^2): b=2 integral_0^1 t^(1/2)(1-t)^2(1-12t+15t^2)dt. This is an exact rational beta sum, not quadrature. The peer's Green-function quadrature is retained solely as a numerical observation.

For psi_1=r(1+r^2)^(-3/2)sin(theta), psi_3=r^3(1+r^2)^(-3)sin(3theta), F=-Delta(psi_1+psi_3), define t as above and D_b A=(1-2bt)A+2t(1-t)A'. A radial profile r(1-t)^b A(t) has radial Euler derivative r(1-t)^b D_b A. The existing own exact polynomial integration code therefore independently reconstructs S_1/pi=3/4, S_3/pi=64/35, d_1/pi=3/8, d_3/pi=6/35, a_1/pi=3/8, a_3/pi=2/63 and b_j=-a_j. Consequently M^2/pi=1201/1260 and subtracting both a terms gives H(F)^2/pi=153/280. The exact H equality follows from F=-Delta(psi_1+psi_3) and density of radial cutoffs in the gradient norm, not from approximate comparisons.

## Source-bound candidate composition and scope

For candidate016, bind the exact whole-plane component certificates N4-392, deep dual/cross396/398, own prefix7 and prefix31 results, reviewed upper410, and the peer T4-480 prefix31 replay. For each prefix, recompute P from the full rF upper squared and every included q_n upper. Subtract the accepted distinct-frequency cross floor and recompute E2^2=P2^2+2^14 G1^2+2^18 G0^2+(20/21)2^18 H^2. The full 160-mode source and all omitted modes remain covered by the accepted full rF component. This reciprocal arithmetic repeats no source integrals and cannot improve any unbound field.

The original R1-050 V7 text printed 1.129995949, 1.063012676 and .944106346 as if directed. Direct comparison with the exact saved prefix7 upper, and exact squaring for the latter two, shows all three are too small as representations of that particular upper. Replacements 1.129995950,1.063012677,.944106347 are safe. The coarse endpoints1.063013,.944107,722.968760 remain valid. This refutes the displayed rounding attribution, not an upper inequality that a later stronger certificate can separately imply. Its repeated51.061045287604983 is approximate, not an interval; safe endpoints are in JSON.

Bind both complete primary review texts, programs as inert text, logs, and the reciprocal T4 acceptance. The configured peer model is us.anthropic.claude-opus-5-5; actual provider-response identity is unobservable here. No remote model call or substitute model is used. All source files remain read-only; this checker executes only own code. No JavaScript/TypeScript, servers, cluster, Lean builds or additional busy workers are used. General analytic statements are proved above; finite tests validate formulas and recorded compositions, not all hypotheses of a PDE existence theorem.
