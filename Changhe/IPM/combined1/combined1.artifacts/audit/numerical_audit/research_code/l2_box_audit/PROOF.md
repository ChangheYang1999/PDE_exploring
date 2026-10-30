# Independent arithmetic audit of the no-negative-norm closure box

## Statement and scope

The target is the scalar parameter certificate in lane T4's l2_closure/PROOF.md, with s=2^-17, r=2^-14 and eta=1/163840. The high energy is E²=P²+2^14 a²+2^18 b². The proposed background decay is1/4, smooth fractional loss4800s and rough loss5r/sqrt(s). This audit proves only the finite algebra and inequalities below. It does not independently prove the analytic energy identities, maximal domains or existence theorem; those remain assigned to an Opus theory lane.

## Positive base quadratic form

For the proposed first, second and zeroth order estimates, subtracting(1/4)E² gives the symmetric matrix

G=[[1/4,-347/10,-5],[-347/10,53048/5,-49152],[-5,-49152,458752]].

Its three leading principal determinants are evaluated exactly as rational numbers. Positivity of all three implies positive definiteness by completing successive squares, equivalently Sylvester's criterion. The commutator matrix has diagonal(4708,4290,3882) and upper entries(85/2,68,340). Its symmetric part has row sums19053/4,17925/4,4086, each less than4800. The quadratic form of a symmetric matrix is bounded by its maximum absolute row sum times the Euclidean norm squared. Finally A_s+B_s=127/50+(653/5)s+(9/5)(1+44s) is increasing in s; at s=1/1024 it equals116349/25600<5.

## Radius, self-map and contraction arithmetic

Define beta=1/4-4800s-5r/sqrt(s), d=r/[2sqrt(pi s(1+s))]. The required strict inequalities are beta>1/10, eta/beta<r and d/2<0.00312. The Fourier gradient bound d also gives d<0.006234. These follow from outward rational interval evaluation: exact rational operations, integer-square-root enclosures at70 decimal places, and Machin's formula pi=16 atan(1/5)-4 atan(1/239), with alternating-series remainder bounds. Each interval endpoint is saved as an exact rational. The independent intervals are compared against the frozen T4 Arb output.

The signed background value c+1-1/20-kappa, with kappa independently confirmed for state131, can additionally be evaluated and compared with2. This scalar check cannot replace the global condition theta<=1/20, which comes from its separate background certificate.

## Dependencies

The code depends on exact rational arithmetic and elementary real inequalities. Its pi enclosure and square-root implementation are the independent ones used in ../graded_box_audit/code/check.py. The frozen target proof and JSON are hashed. Numerical agreement is not used as a proof of the analytic theorem.

## Candidate point exclusions for the proposed radius

The no-H energy still dominates the H^(2+s) norm because omega>=1 and xi^4+2^14 xi²+2^18>=(1+xi²)². Hence the already audited fixed-exponent pointwise necessary condition applies with R=r:

|F(X)| <= [C1 |V(X)|+C0(1+|D rho(X)|)]r+C0 C1 r²,
C0=[4pi(1+s)]^-1/2, C1=[8pi s(1+s)]^-1/2.

The scalar gradient functional in any fixed direction has the same C1 norm by rotation; taking the supremum in the direction of the gradient gives the vector gradient bound. The velocity multiplier has vector norm at most one and gives the displayed C0 bound. The inequality follows by expanding F(rho+h;c)=F+V.Dh-h+U[h].D rho+U[h].Dh. The three independently confirmed Cartesian field triples in ../point_witness/verification/cartesian_witnesses.json therefore decide whether d2, Mpen2 and b6 can lie within this particular ball of an exact profile. This test is independent of the sufficient theorem's background assumptions. The arithmetic is postprocessing of those field intervals, not a new field evaluation.

## T2-R3 sharp weighted variants

The same finite audit applies to the two parameter sets proposed in T2-R3: (w1,w2,mu,Cprime,s,R,eta)=(16384,262144,259/1000,401,1/7744,147/200000,76219/10^9) and (32768,1048576,97/250,397,1/5184,1351/10^6,4207/(2*10^7)). The unrelaxed base matrix is

G=[[1/2-mu,-347/10,-5],[-347/10,w1(9/10-mu)-40,-3w1],[-5,-3w1,w2(2-mu)]].

Check all three leading minors over exact rationals. For the sharp commutator use the kernel values and formulas of T2-R2 as restated in T2-R3, with C,U1,U2,U3,R1,R2,R3,R4=(2,6,24,160,22,32,80,2048). Interval evaluation of the complete symmetric row sums, not rounded displayed entries, checks the respective bounds 401 and397. The same sharp rough estimate is bounded by8/5. Thus beta=mu-Cprime*s-(8/5)R/sqrt(s) is an exact rational in these two cases. Check beta>=1037/10000 or1557/10000, eta<=beta_lower*R, the L2 contraction c_s*R/2<1, and the slope margin7/10-c_s*R>0. These are arithmetic checks conditional on the analytic T2-R3 theorem, whose proof remains assigned to the theory lanes.

For raw residual data, T2-R3's weighted commutator estimate implies P(J^s F)>=(1-(48/25)s)P(F), while Plancherel gives ||D J^s F||2>=||DF||2 and ||J^s F||2>=||F||2. Therefore a valid lower bound on X(F) is the square root of the weighted sum of these three squared lower bounds. A valid upper conversion is

E^(1-s)(2 Q3^2+Cw E^2)^(s/2)+(48/25)s E,
Cw=max(1+32/25+w1,1+w2/w1),

with E formed from upper component bounds. These comparisons are conditional on the already stated analytic commutator and interpolation estimates, not new Fourier computations.

For a four-branch family of fixed radial degree K in ../l2_family_floor/PROOF.md, its proven full-plane G0 floor directly gives X>=sqrt(w2)G0. No additional factor1-34s is needed for this zeroth-order component. The exact distance decreases as K increases because every additional factor |a-b|/(a+b+1) is less than one for the distinct square-integrable powers. A binary search followed by explicit checks at the two consecutive integers therefore identifies the last K excluded by this particular lower bound. It does not prove that any higher degree is attainable or sufficient.
