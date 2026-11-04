# Primary Beltrami and pressure statements: exact scope audit

## 1. Sources actually checked

The source submission is LIT251, whose complete five sections were read. Immutable copies are in the team records. The actual primary texts checked here are Chae and Constantin, arXiv 1407.7303v1, printed pages 2-4; Chae and Wolf, arXiv 1506.04361v2, printed pages 1-4 and 8-9; and Chae, arXiv 0809.0743v5 and v6, their weak definitions, Theorem 1.1 and the exact cutoff passages using a stronger time norm. CC14 pages 3-4 and CW16 pages 4 and 9 were also visually inspected. The manifest records hashes and honest reading coverage. This is an offline audit of the actual retained manuscripts, not an abstract-based assessment or a claim to have inspected an unretained online revision.

## 2. The literal bounded endpoint in CC14

In R3 let a be a fixed nonzero vector, v(x)=a, lambda(x)=0 and P(x)=-|a|²/2. All fields are smooth. Then div v=0, curl v=lambda v and (v.grad)v+grad P=0. Thus this is a Beltrami solution under CC14's printed definition. It belongs to the literal q=infinity endpoint of Theorem 1.2: v is bounded and lambda belongs to L^(6/5). It is not zero.

The claimed endpoint therefore needs a hypothesis removing constants, such as decay or the appropriate homogeneous Sobolev representative. The source step ||v||2<=C||grad v||_(6/5) cannot be used on this constant field. This countertest leaves the finite-energy theorem and finite-q conclusions intact. It does not refute a separately normalized bounded theorem. The pressure equation (1.5) has P-constant=-|v|²/2; the proof's initial plus sign is a transcription error, since the following integral uses the minus sign.

## 3. CW16's Morrey radius and tangential-vector notation

Let u(x)=(sin x3,cos x3,0) and P=-1/2. Direct differentiation gives div u=0, curl u=u, |u|²=1 and (u.grad)u=0. It is a smooth weak Beltrami flow with exactly the pressure normalization of Definition 1.2. However

    R^(-1) integral_(B_R) |u|²=(4pi/3)R².

The supremum over all R>0 is infinite. This disproves the literal all-radius formula printed immediately before Theorem 1.6. It does not disprove local Morrey regularity: the actual proof controls 0<R<=1 by monotonicity of its sphere-energy function. More generally the same example has a finite bound on every bounded radius interval.

The text also defines u_T=u cross n but writes u=u_N+u_T. For n=e3 and u=e1 the right side is -e2, not e1. The tangential projection is n cross(u cross n). The identity |u_T|²=|u|²-|u_N|² and all scalar norm bounds survive. No failure of the intended norm-based Liouville argument follows from this vector-notation error.

## 4. A finite-energy stress identity without a pressure representation

Let N>=2, v in L2(RN;RN), P in L1(RN) and assume

    div div(v tensor v+P I)=0 in distributions.

Then, for every i,j,

    integral v_i v_j=-delta_ij integral P.                (1)

To prove this, each component of the symmetric tensor T=v tensor v+P I is in L1. Its Fourier transform is continuous. The distributional equation says xi^T T_hat(xi) xi=0, and this continuous function is zero at every xi. For a fixed unit e and t!=0, divide by t² at xi=te to obtain e^T T_hat(te)e=0. Continuity at zero gives e^T M e=0, where M=integral T. Coordinate vectors show M_ii=0; normalized sums of two different coordinate vectors give M_ij=0. Thus M=0, proving (1).

Taking the trace gives integral |v|²=-N integral P. If integral P>=0, v=0 almost everywhere. In R3 the normalized Beltrami pressure P=-|v|²/2 instead gives E=(3/2)E, hence E=0. No Riesz-transform normalization, pressure derivative or boundary term is needed. An arbitrary pressure constant is not permitted by P in L1 on the whole space.

This Fourier proof is already explicit in CC14's proof of its pressure theorem under the stated representation. No novelty is claimed for it; the point here is the precise stress formulation and its use for time slices.

## 5. Time-slice repair of the Chae2008 proof mismatch

Let I be an open time interval, v in L1_loc(I;L2(RN)), P in L1_loc(I;L1(RN)), div v=0 and v_i v_j in L1_loc(RN times I). Assume the usual distributional incompressible Euler or Navier-Stokes momentum equation, with any constant viscosity nu>=0. Then (1) holds for almost every time.

Indeed insert a compact test field grad psi(x) eta(t). The time term and viscosity term vanish by divergence freedom; the remaining identity is

    integral_I eta(t) integral_RN [v_i v_j partial_ij psi+P Delta psi] dx dt=0.

For each psi the inner function is locally time integrable by the explicit local product and pressure assumptions, so it vanishes almost everywhere. Choose a countable collection of smooth scalar tests dense in the C2 norm on each member of a countable compact exhaustion. Intersect their full-measure time sets and the sets on which v(t) is L2 and P(t) is L1. At every retained time, continuity of the spatial pairing extends the identity to all smooth compact tests. Thus the spatial stress equation holds, and Section 4 applies.

Both inspected versions print an L1_t L2_x velocity class in Definition 1.1 but invoke L-infinity_t L2_x in the cutoff proof. The latter norm is not a consequence of the former. The time-slice proof repairs the L1-pressure conclusion without assuming global time integrability of the kinetic energy. It explicitly retains the local integrability of the quadratic products required to form the weak momentum equation; that integrability is not inferred from L1_t L2_x alone.

## 6. Limits of the audit

The v6 Hardy-pressure extension for exponents below one is not certified by this L1 Fourier argument, since such a pressure need not be an L1 function. Its separate distributional pairing proof requires its own audit. No counterexample to that extension has been produced.

The constant field and plane wave are stationary and nondecaying, and do not solve the target similarity equation with their displayed pressures. The spatial identity needs finite energy and globally integrable pressure, neither supplied by bare decay in the target c-range. No global Beltrami condition or pressure-integral sign is derived for a rotating profile. Therefore these source qualifications do not close the campaign's main conjecture or its common-flat-point problem.
