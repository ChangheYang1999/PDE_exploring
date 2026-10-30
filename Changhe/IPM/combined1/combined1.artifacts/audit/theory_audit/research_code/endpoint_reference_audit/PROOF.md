# Endpoint bookkeeping, next forcing term and a fourth cutoff

## Hypotheses and notation

This audits R2-R4 of the frozen Opus the review of T4-338. Use the campaign c, gamma=1/c and delta=1-gamma, and the exact three-times repaired references R3 of the audited finite-tail theorem for007,013,014. Put q=gamma-4=e(1,2), p=e(10,0), e(K,L)=1-Kdelta-2L, epsilon=q-p=9delta-4>0 and epsilon'=q-e(6,1)>epsilon. Let Theta be the leading density profile, A the residual coefficient at q, B the residual coefficient at p, and P=gamma cos2theta Theta+sin2theta Theta'. All norms and projections below use arc length on the full circle. Canonical velocity and the smooth cutoff construction are those in the cited audited proofs.

## 1. Exterior dipole bookkeeping

If an exterior velocity expansion is changed by d(cos3theta,sin3theta)/(pi r^3), the change paired with the leading density gradient is (d/pi)r^q P. All pairings with subsequent density-gradient sectors have strictly lower exponents. Thus A changes within A+span P and dist(A,span P) is unchanged. This is an exterior expansion identity. It does not permit adding a singular harmonic dipole to a globally smooth fixed canonical velocity. An actual global reference change realizing such a dipole must separately satisfy the canonical-velocity requirements.

## 2. A two-term conditional stationary expansion

Let k be a real S1 C1 stationary correction of R3 with H_q(k)<infinity, and let m=integral yk. The endpoint theorem and its moment-resolved velocity estimate apply. The exact reference expansion is

    F(R3)=r^q A+r^p B+O(r^(q-epsilon')).

The density leading-gradient error has a gap at least delta. The velocity-remainder and reference transport terms also have gap at least delta, while the moment self-transport and the remaining nonlinear term have still larger gaps. Here delta>epsilon'. Consequently radial integration of the exact stationary equation gives

    r^-q k = (A+(m/pi)P)/(4c)
               +r^-epsilon B/(1-cp)+O(r^-epsilon').

The O constant depends on H_q(k), m and the complete reference bounds. This statement is uniform in angle at sufficiently large radius. Its derivation is the same integrating-factor proof as the audited endpoint theorem, now retaining the second forcing term. Neither the expansion nor its O constant is a global finite-radius estimate by itself.

Let Pi be orthogonal projection onto the complement of span P, a=Pi A/(4c) and b=Pi B/(1-cp). Exact rational angular coefficients determine a.b up to the positive factor pi. If a.b>=0, then for every s>=0,

    ||a+s b||^2=||a||^2+2s(a.b)+s^2||b||^2>=||a||^2.

Thus the retained two-term projection never lowers the limiting norm. For the actual correction this gives ||r^-q k||>=||a+r^-epsilon b||-C r^-epsilon'. The sign does not remove the remainder. In particular a few listed lower sectors cannot certify C or prove that a given velocity constant, rather than the forcing remainder, limits a finite-radius closure inequality.

## 3. Fourth cutoff and its first moment

The endpoint exponent has a=q+3=-delta in(-2,0), so the audited finite angular inverse is nonresonant. Let B4=A/(1-cq)=A/(4c) and choose the finite even-cosine potential r^(q+3)Q with -partial_y Delta(r^(q+3)Q)=r^q B4. For a smooth radial cutoff zeta_L equal0 on r<L and1 on r>2L, set chi_L=zeta_L r^(q+3)Q and h4=-partial_y Delta chi_L. The canonical velocity is the corresponding local third derivative field. It is zero on the interior disk and homogeneous of degree q outside2L.

The linear residual of h4 cancels r^q A. Its mixed terms with R3 have exponent at most q+gamma-1=e(2,2)<q and its self term has exponent2q-1<q. Therefore R4=R3+h4 has zero residual coefficient at q. The previously retained p term may remain, and p<q. The leading Theta and P are unchanged. Dilation gives ||h4||2=L^(q+1)||h1||2, which tends to zero since q<-1.

Moreover integral yh4=0. The density and its first moment are integrable because h4=O(r^q) with q<-3. Write g=Delta chi_L=O(r^(q+1)). Integrating -y partial_y g over a disk gives integral g minus a boundary term of size O(R^(q+3)), tending to zero because q+3<0. The integral of g is a flux of grad chi_L, also O(R^(q+3)), hence zero. The inner boundary contributes nothing because chi_L vanishes near the origin. S1 gives integral xh4=0 as well. This argument proves actual global moment cancellation, not only cancellation of a formal sector.

Thus rebasing a stationary correction by k'=k-h4 preserves its first moment. The endpoint theorem for R4 has A=0. Any faster weighted stationary correction must satisfy mP=0; the campaign P is nonzero, so m=0. This is a necessary condition. It does not assert the existence of such a correction. The nonzero endpoint obstruction for R3 belongs to that reference and weighted class; it never excluded arbitrary nearby L2 states.

## Dependencies and verification

The complete endpoint estimate, finite cutoff theorem and angular inverse are already independently audited. Frozen exact sector maps and endpoint maps are copied from the accepted own calculations. The checker rebuilds B from the complete convolution after the first two repairs, tests the exact projection sign against the independent Opus result, solves the fourth finite angular inverse and checks it by the forward density map. Large coefficients remain in exact JSON. The new code is executed only after this proof is written and checked. The claims here are audits of the named Opus extensions; the finite-radius remainder conclusion is explicitly left OPEN.
