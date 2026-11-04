# Independent audit of the one-eighth quadratic pressure bound

Status: CONFIRMED at A2844-A2846 after independent reconstruction, exact finite certificate verification and the existing coordinator comparison. This is a homogeneous polynomial theorem, not a pressure premise for arbitrary Euler profiles.

## 1. Statement and sole cone dependency

Let Q:R3->R3 be real, homogeneous quadratic and divergence free. Let R:R3->R be real and homogeneous quartic. If

    -Delta R=tr((DQ)^2), R>=|Q|^2/8 everywhere,

then Q=R=0. Allow every harmonic quartic component of R. Define Gamma_2 as the supremum of feasible gamma>=0 under the normalization mean_S2 |Q|^2=1. The second assertion is that this supremum is finite, attained and satisfies2/17<=Gamma_2<1/8.

The only cone dependency for the upper bound is A2805: if B>0 and tr(B)tr(B^-1)<=49, then ell_B(F)=tr(B C_F)>=0 for every nonnegative homogeneous quartic F, with Delta F=x^T C_F x. It was proved by a positive finite evaluation representation, not a sampled test. No other pressure-bound result is imported for the upper bound.

## 2. Strict positivity

For a trace-one B>=I/15, set B0=B-I/300. Then B0>=19I/300, tr B0=99/100 and tr(B0^-1)<=900/19. Thus their product is at most891/19<49, and A2805 applies. The polar Laplacian for a quartic gives mean_S2 Delta F=20 mean_S2 F, whereas mean_S2 x^T C_F x=tr C_F/3. Hence ell_I(F)=60 mean F.

For F>=0 nonzero, its mean is strictly positive by continuity. Therefore ell_B(F)=ell_B0(F)+ell_I(F)/300>0. This includes B with an eigenvalue exactly1/15. For a feasible pair put F=R-gamma|Q|^2 and define C_gamma by

    x^T C_gamma(Q)x=-tr((DQ)^2)-gamma Delta|Q|^2.

We shall produce an allowed B with tr(B C_(1/8)(Q))<=0, then exclude equality.

## 3. The full velocity space

The solenoidal tangential quadratic space consists exactly of T=x cross Mx with M symmetric modulo scalar matrices. Indeed differentiating x.T=0 and using homogeneity yields x cross curl T=-3T. The curl is linear, so T has the stated form for some M. Since div(x cross Mx)=-x.curl(Mx), the divergence condition forces symmetry of M. The kernel consists of scalar M, since x cross Mx=0 for every x says every line is an eigenline. This is a five-dimensional space.

Project Q onto it in the sphere inner product, writing Q=T+N. For nonzero T choose an oriented orthonormal eigenframe of M; a sign change of one eigenvector permits orientation without losing diagonality. Then T=(a yz,b xz,d xy), a+b+d=0 and s=a^2+b^2+d^2>0.

Under coordinate reflections Q(x)->D Q(Dx), the eighteen coefficient monomials split into four characters. The xyz character has dimension3 and is automatically solenoidal. Each of the three single-coordinate characters has dimension5 with one independent divergence constraint. This retains all15 solenoidal dimensions. Distinct characters are orthogonal and the reflection-invariant quadratic functional tr(B C_gamma(Q)), for diagonal B, has no cross terms between them.

The xyz part of N is orthogonal to the coefficient plane a+b+d=0, whose three monomial sphere norms are equal. It is therefore (h yz,h xz,h xy). In the z character a solenoidal field is

    ((u+v)xz,(u-v)yz,d0 x^2+e0 y^2-u z^2).

Its tangential direction is (-xz,yz,x^2-y^2). The sphere moments1/5 and1/15 give orthogonality d0-e0=v. Writing w=(d0+e0)/2 leaves

    N_z=((u+v)xz,(u-v)yz,(w+v/2)x^2+(w-v/2)y^2-u z^2).

There are two cyclic copies, with independent parameters. The actual field in its chosen frame thus has xyz part ((a+h)yz,(b+h)xz,(d+h)xy) and these three normal parts. The eigenframe is part of the description; this is not a reduced fixed-frame search. If T=0, use an arbitrary frame and put a=b=d=0.

## 4. Adapted weights and first pairing

Let p=abd and r=p^2/s^3 when s>0. The relations a+b+d=0 imply sum a_i^4=s^2/2, sum a_i^3=3p and

    (a-b)^2(b-d)^2(d-a)^2=s^3/2-27p^2.

Thus0<=r<=1/54. Set tau=1/7-(144/35)r, mu=1-3tau and b_i=tau+mu a_i^2/s. Then1/15<=tau<=1/7 and4/7<=mu<=4/5, so B=diag(b_i) has trace1 and B>=I/15.

For Q_xyz=(A yz,B1 xz,D1 xy), the diagonal of C_gamma is the cyclic list -2B1D1-2gamma(B1^2+D1^2). Inserting a_i+h gives

    sum b_i(a_j+h)(a_k+h)=-tau s/2-3mu ph/s+h^2,
    sum (1-b_i)(a_i+h)^2=(1+tau)s/2-6mu ph/s+2h^2.

Combining them proves the full pairing

    [tau-gamma(1+tau)]s+6mu(1+2gamma)(p/s)h-2(1+2gamma)h^2.

At gamma1/8, the constant term is (7tau-1)s/8=-(18/5)sr. Completing the square gives

    -(5/2)(h-(3mu/2)p/s)^2+(45/8)sr(mu^2-16/25)<=0.

Equality occurs either at r=0,h=0, with (a,b,d) a permutation of(t,-t,0), or at r=1/54,mu4/5,h2t/5, with (a,b,d) a permutation of(2t,-t,-t). Here t!=0. These cases exhaust equality because both summands are nonpositive.

## 5. Every normal block and its determinants

For N_z above, the coefficients of tr((DN_z)^2) are

    x^2:4(u+v)(w+v/2), y^2:4(u-v)(w-v/2), z^2:6u^2+2v^2.

The coefficients of Delta|N_z|^2 are

    x^2:2u^2+2uv+4v^2+16w^2+12wv-4uw,
    y^2:2u^2-2uv+4v^2+16w^2-12wv-4uw,
    z^2:16u^2+4v^2-8uw.

Weighting these at gamma1/8 yields -8tr(B C)=(u,w,v)H(u,w,v)^T with

    H=[[2+62k,14-18k,9delta],
       [14-18k,16(1-k),22delta],
       [9delta,22delta,20]],

where k=b3 and delta=b1-b2. Cyclic covariance gives the same formula for the other two normal blocks. The first leading minor is positive. The second is4P, where P=-41+366k-329k^2. Expanding the determinant along the final row gives

    det H=80P-delta^2[(2+62k)484+(16-16k)81-2(14-18k)198]
         =80[P+(41-448k)delta^2]=80D.

For q=d^2/s, Cauchy gives0<=q<=2/3. Since ab=(2d^2-s)/2, we have r=q(1-2q)^2/4 and (a^2-b^2)^2/s^2=q(2-3q). Therefore

    tau=1/7-(36/35)q(1-2q)^2, mu=1-3tau,
    k=tau+mu q, delta^2=mu^2 q(2-3q).

The same relations hold for each cyclic distinguished coordinate. Section6 supplies P>0 and D>0 on the full interval. Sylvester's criterion then makes every H positive definite. If T=0, choose B=I/3. Then k1/3,delta0, P400/9>0; the xyz pairing is -(5/2)h^2. Thus the total pairing is strictly negative for every nonzero field with T=0.

## 6. Exact coefficient certificate and its logical role

Direct substitution gives

    k=(432q^4-576q^3+252q^2-16q+5)/35,
    delta^2=16q(2-3q)(108q^3-108q^2+27q+5)^2/1225.

Define P,D by Section5, without importing an expanded polynomial from data. Their degrees are8 and12. For F(l+(u-l)t)=sum c_j t^j of degree n, define beta_i=sum_(j<=i)c_j binom(i,j)/binom(n,j). The binomial theorem proves

    F(l+(u-l)t)=sum_(i=0)^n beta_i binom(n,i)t^i(1-t)^(n-i).

Indeed the coefficient identity for t^j follows by factoring t^j and expanding (t+(1-t))^(n-j). The basis functions are nonnegative and sum to1 on[0,1]. Consequently a positive minimum beta_i is a strict lower bound throughout the closed interval.

The exact rational lists are stored, not hardcoded here, in the team records. The proposed certificates use P on[0,1/6],[1/6,1/3],[1/3,2/3], with respective minima13948/11025,476/25,400/9; D on[0,1/3],[1/3,2/3], with minima8/33075,12112/441. Their intervals cover the entire parameter range, including endpoints. Every one of the53 coefficients must equal the rational transform of the defined P or D and be strictly positive. The independent standard-library rational check planned in the team records verifies these identities, degrees, coverage and minima. The independent check completed successfully: all53 coefficients equal the exact transform and are positive, with the stated minima and complete coverage. The argument combines those rational identities with the binomial identity above; a JSON import or earlier PASS label alone is not accepted as proof.

## 7. Equality exclusion

For a feasible nonzero Q, the case T=0 already contradicts ell_B(F)>=0. Otherwise all four group pairings are nonpositive; strict positivity from Section2 forces F=0, and hence C_(1/8)(Q)=0. All three normal blocks must vanish, and the xyz part is one of the two equality families in Section4.

For Q=t(yz,-xz,0), direct substitution gives C=t^2 diag(-1/4,-1/4,3/2). For Q=(t/5)(12yz,-3xz,-3xy), it gives C=t^2 diag(-9/10,27/20,27/20). Neither is zero. Permutations and orientation corrections merely conjugate the residual matrix, so this exhausts every eigenframe. The contradiction proves Q=0. R is then harmonic and nonnegative homogeneous quartic; its mean is zero by the polar Laplacian, so continuity gives R=0.

## 8. Explicit nonemptiness and attainment

Set rho^2=x^2+y^2 and k0=sqrt6. The explicit pair is

    Q0=(xz-k0 yz,yz+k0 xz,-rho^2-z^2),
    E0=|Q0|^2=rho^4+9rho^2 z^2+z^4,
    R0=(2/17)E0+z^4/34.

The divergence is z+z-2z=0. The Jacobian has diagonal(z,z,-2z) and opposite off-diagonal products -6z^2,-2x(x-k0y),-2y(y+k0x). Hence tr((DQ0)^2)=-4rho^2-6z^2. Since Delta rho^4=16rho^2, Delta(rho^2 z^2)=2rho^2+4z^2 and Delta z^4=12z^2, Delta R0=4rho^2+6z^2. Its energy mean is8/15+18/15+3/15=29/15. Scaling Q bysqrt(15/29), R by15/29 gives a normalized feasible pair at2/17.

On the normalized velocity sphere, coefficients of Q and its quadratic source are bounded in finite dimension. If -tr((DQ)^2)=x^T N_Q x, then mean R=tr N_Q/60 is bounded. For gamma>=0, R>=gamma|Q|^2>=0, so gamma<=mean R and the sphere L1 norm of R is bounded. This is a norm on homogeneous quartics; continuity and homogeneity show that zero norm implies the zero polynomial. Norm equivalence bounds every pressure coefficient. The feasible triples are closed, since coefficient convergence preserves normalization, the exact Poisson identity and pointwise nonnegativity. They are bounded and nonempty, hence compact. The maximum gamma is attained and positive. Section7 excludes every gamma>=1/8 by monotonicity of the inequality, so Gamma_2<1/8.

## 9. Scope and evidence

The theorem keeps the entire fifteen-dimensional solenoidal velocity class and every quartic pressure adjustment. Its Q-dependent B entails no interchange of infimum and supremum. It neither supplies a local Euler pressure lower bound nor relaxes center normalization. The previously proved sharp local threshold1/6 and the center-Holder threshold1/(4+2alpha) cannot improve by this quadratic theorem because their cubic and fractional swirl countertests remain. The exact Gamma_2 and the unrestricted decaying rotating Euler conjecture remain open.

All eight original source sections and all168 entries of its source check record were read. Those source checks were not rerun. The independent rational certificate audit completed all82 checks in0.021187581 actual seconds, from2026-11-04T03:16:19.038172+00:00 to03:16:19.059361+00:00, using only standard-library Fraction arithmetic. All82 result entries were read. The input hash is e99abf9033d0d489bd0082244094586d6cedbfe46227c28f1594c64d5e5d9a0b and the script hash is3cc3875e40fae0f616b76f72146ace4816c44d7d475f6e5f75130d50bb7549e7. The input, plan, script and full result are retained in verification. It ran on CPU55 at priority19 with one worker. The existing configured model comparison is completed in Section10; no new client or agent is used and actual provider execution is independently unattested.

## 10. Existing coordinator comparison and exact limits

The complete seven-item coordinator comparison of the original source f49b5940 was read with every entry of its final 39-check log. Its analytic reconstruction agrees with Sections1-8: the strict dual positivity, complete projection and four characters, discriminant-dependent weight, all three normal matrices, all53 Bernstein coefficients, the two residual matrices, and attainment. Its independent exact root isolation is additional evidence, not needed by the rational certificate used here. The sharper trace-product maximum it states is correct: at eigenvalues19/300,19/300,259/300, the product is159489/4921. Convexity of the reciprocal sum on that fixed-trace simplex puts its maximum at a vertex. The coarser bound891/19 already suffices.

The first coordinator run had two check-script errors, not proof errors. The full retained final log and the exact script diff were read. The roots of mu(r)^2=16/25 are -1/9 and1/54; the first script compared to a wrong root list. The corrected test filters to the admissible interval. Its use of Integer on a rational interval endpoint was replaced by Rational, preserving1/6 and1/3. Neither defect occurs in this agent's Fraction reconstruction. No coordinator script was rerun here.

Its floating composition diagnostic reports4000 fields, including3800 generic fields and100 perturbations of each equality type. The largest normalized generic pairing is about-0.5463. The absolute perturbed values range from2.38e-5 to3.27e-4 and from4.66e-6 to6.97e-5, respectively, with no positive pairing recorded. These statements describe the retained log only; they are not the proof or an optimization of Gamma_2.

The particular test is exactly tight at both equality types at gamma1/8. At Q=t(yz,-xz,0), B=diag(3,3,1)/7 gives ell_B(C_gamma)=(2-16gamma)t^2/7. Thus this unchanged weight cannot prove a lower endpoint there. This field is a multiple of the already audited axial swirl whose fixed-field optimum is(6-sqrt30)/24; tightness of this test is not sharpness of Gamma_2. The stronger previously confirmed lower bound g_star from A2718-A2719 may be combined with Section8 to give g_star<=Gamma_2<1/8. No new lower-bound proof is claimed here.

The comparison is through the existing configured model coordinator, with actual provider execution independently unattested. It resolves the pending model comparison without a new client, subagent or remote computation. Euler applicability and the exact value of Gamma_2 remain open.

## 11. Additional Theory Agent C  comparison and source status revision

The complete Theory Agent C  comparison stamped 2026-11-04T03:27Z and every line of its 42-check algebra log were read. Its independent decomposition, both cyclic normal groups, completed square, determinant polynomials, all 53 Bernstein coefficients, equality residuals and positive feasible pair agree with the reconstruction above. The log also reports an exact root count, but that independent computation is not needed for the already reconstructed Bernstein proof and was not rerun.

The second equality family has pairing -18t^2(8gamma-1)/25. This follows directly from the general xyz formula by inserting s=6t^2, p=2t^3, h=2t/5, tau=1/15 and mu=4/5. Together with the first family, the present test has two equality types. The older phrase that a test has one equality type must not be extended to this test. The Theory Agent C  grid values for the minima of P and D are sampled estimates, not certified global minimum values; neither those values nor its separate floating stress test supplies the proof. The stress-test log was not read or rerun here.

All changed source lines from the retained submission f49b5940 to the status revision f4c699a2764b9d3f0137feb2dbdc3638a84daedce229b9bfcb1e3d39d205d8e2 were read, with its confirmation manifest. Only the status and a ninth comparison section are added. The equations, homogeneous hypotheses, strict bound, harmonic freedom and open Euler application remain unchanged. The additional lower bound g_star is correctly attributed to A2718-A2719, and the sharp local thresholds remain unchanged. The reported repairs concern the coordinator's check script only. This is a source-preservation and analytic-comparison check, with no new mathematical computation.
