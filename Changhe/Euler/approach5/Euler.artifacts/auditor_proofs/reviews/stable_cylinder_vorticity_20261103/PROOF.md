# Transported vorticity on a stable cylinder

Status: CONFIRMED as A462 after independent reconstruction, full postwrite inspection and focused configured-model review. A449 already excludes the periodic negative-covector Euler orbit by a different proof. The elementary geometric lemma below gives a shorter independent route and makes its local helicity requirement explicit.

## 1. Geometric statement

Let B be C2 on a neighborhood of a nonstationary hyperbolic periodic orbit Gamma of period T in an oriented three-manifold. Its two nontrivial Poincare multipliers are assumed positive, with exponents lambda_s<0<lambda_u. Let kappa>0 and let W be C1 there with

    [B,W]=-kappa W, lambda_u>kappa.

Then W is tangent to a sufficiently small forward-stable cylinder Sigma of Gamma.

Suppose in addition that a C2 scalar H satisfies WH=0 nearby, H=h0 and W=0 on Gamma, dH is nonzero on its stable line, and DW is nonzero on every nonzero stable vector along Gamma. Then Sigma contains nonconstant closed W-orbits arbitrarily close to Gamma on both sides of that circle.

No incompressibility, Euler pressure, complete ambient flow or global invariant surface is assumed in this geometric statement. The strict inequality lambda_u>kappa and the nonzero stable derivative are explicit premises.

## 2. Stable cylinder and its defining function

Choose a transverse disk to B. Its first return map is a C2 local diffeomorphism with a hyperbolic fixed point, one stable eigenvalue and one unstable eigenvalue. The finite-dimensional C2 stable-manifold theorem supplies a C2 local stable curve. Its flow saturation gives an embedded C2 local stable surface, using the return map to identify overlapping section pieces rather than leaving a seam at one period. The positive stable multiplier orients its stable line around Gamma, so the surface is a cylinder. On this surface Gamma is attracting. A sufficiently small forward-invariant collar therefore has compact closure inside a larger stable cylinder. One can obtain it by a periodic change of scale in the stable coordinate so its linear radial rate is the negative constant lambda_s, and then shrinking the coordinate interval to preserve the negative rate. Smoothness of the collar boundary is not used; the defining function below is constructed on the larger C2 surface.

The stable return iterates converge geometrically. The C1 return-time function differs from T by at most a constant times the distance to the fixed point. Summing these errors yields a finite time correction. Hence every point of the stable cylinder approaches a fixed phase of Gamma in forward time. This uses neither a global stable foliation nor a stronger normal-hyperbolicity theorem.

The cylinder is orientable, and the ambient manifold is oriented. It therefore has a continuous coorientation. Local C2 defining functions can have their signs chosen consistently. A finite C2 partition of unity on a neighborhood of a smaller compact collar combines them into a C2 function f with Sigma={f=0} and df nonzero on Sigma, after shrinking the neighborhood. Indeed the derivatives of all signed defining functions on Sigma are positive scalar multiples of one common conormal; their weighted sum cannot vanish. The implicit function theorem excludes additional nearby zero sheets.

Since Bf=0 on Sigma, all tangential derivatives of Bf vanish there. Thus for a continuous scalar beta on Sigma,

    d(Bf)=beta df.                                          (1)

Only B C2 and f C2 are used. In particular no derivative of beta will be taken.

## 3. Exact normal transport forces tangency

Along Sigma the derivative of the pulled-back covector df is the pullback of d(Bf). Thus

    df(Phi_t x) D Phi_t(x)
      =exp(integral_0^t beta(Phi_s x) ds) df(x).             (2)

At x on Gamma and t=T, the scalar is the unstable multiplier: the kernel of df is exactly the stable-plus-flow tangent plane. Consequently the period mean of beta is lambda_u. Phase convergence and uniform continuity of beta on the compact stable collar imply for every x there

    lim_(t to infinity) (1/t) integral_0^t beta(Phi_s x) ds
      =lambda_u.                                          (3)

Set w=Wf on Sigma. It is C1, and the commutator identity and(1) give

    B w=W(Bf)+[B,W]f=(beta-kappa)w.                         (4)

This formula evaluates the full covector d(Bf) on W, even before W is known tangent. It does not replace W(Bf) by a derivative of an identity valid only on Sigma. Equation(1) is the necessary ambient first-derivative statement that makes the calculation legitimate.

If w(x) is nonzero, its scalar ODE and(3) make its magnitude grow with positive asymptotic exponent lambda_u-kappa. This contradicts boundedness of W and df on the compact forward orbit. Hence w=0 everywhere on the smaller stable cylinder, proving W tangent to Sigma. No pointwise sign of beta is needed.

## 4. The first integral yields nearby closed vortex circles

On Gamma, dH annihilates the orbit tangent and is nonzero on the stable line. Thus H restricted to Sigma is a C2 submersion near Gamma. Choose a C1 vector field Z tangent to Sigma with dH(Z)=1. Its local C1 flow, starting at Gamma, gives a C1 collar chi(theta,r) with H=h0+r. Compactness supplies one parameter interval for the whole circle, and uniqueness plus the local inverse theorem give an embedded collar. Each small level r is one compact C1 circle.

The vector Z on Gamma has a nonzero stable component. DW kills the orbit tangent because W=0 on Gamma. The assumed stable derivative is nonzero, so

    W(chi(theta,r))=r DW(Gamma(theta)) Z(Gamma(theta))+o(|r|) (5)

uniformly around Gamma. Its continuous leading coefficient has a positive minimum norm. Hence W is nonzero on every sufficiently small level with r!=0. By Section3 it is tangent to Sigma, and WH=0 makes it tangent to the level circle. A continuous nonvanishing tangent field on a compact C1 circle has a finite traversal period: its scalar speed in arclength coordinates has one sign and is bounded away from zero. Since W is C1, uniqueness identifies this traversal with its local integral curve. This proves the geometric statement.

## 5. Euler application with only local zero helicity

Let U in C2(R3;R3),P in C1 solve the full rotating incompressible Euler profile equation for 0<c<1/2 and any real omega, with uniform U=o(|y|). Put

    A=cI-omega J, B=Ay+U, W=curl U,
    a=1-2c, kappa=1+c, d=3c,
    H=P+|U|^2/2+(Ay).U, g=U.B.

Suppose Gamma is a nonstationary periodic carrier orbit on which

    W=0, U!=0, rank DW=1, image DW=R B, grad g=-kappa U,

and assume U.W=0 on some open neighborhood of Gamma. These hypotheses are inconsistent. Global zero helicity is sufficient, but this particular argument uses only the stated local neighborhood hypothesis and the explicit orbit data.

The full equation gives H in C2 and

    grad H=-aU+B cross W, BH=-ag, WH=-a U.W,
    [B,W]=-kappa W.                                       (6)

Differentiating the local zero-helicity identity on Gamma gives U^T DW=0. The image condition and U!=0 then give U.B=0. Hence H=h0 on Gamma, grad H=-aU!=0 there, and

    grad(BH)=-a grad g=-kappa grad H.                      (7)

The covector transport law from(7) makes grad H a nonzero left eigenvector of D Phi_T with multiplier exp(-kappa T). The flow gives eigenvalue1, and det D Phi_T=exp(dT) supplies the remaining multiplier exp((d+kappa)T). The multipliers are positive and distinct. The stable line is therefore transverse to the H-level; grad H annihilates the flow and unstable lines.

It remains to verify that DW is nonzero on the stable line without importing a separate spectral classification. On W=0 the differentiated Cauchy identity at one full period gives, with N=DW(p) and M=D Phi_T(p),

    N M=exp(-kappa T) M N.

The image of N is the flow line, on which M acts by1. Thus N M=exp(-kappa T)N. It follows that N kills the flow and unstable eigenlines; since rank N=1, it is nonzero on the stable line. All geometric hypotheses are verified, with lambda_u=d+kappa>kappa and WH=0 in the neighborhood. The resulting nonzero closed W-orbits contradict A014 for the global uniformly sublinear profile. This conclusion needs neither A413 nor Kelvin circulation.

## 6. Dependencies, scope and verification

The local invariant-manifold input is exactly the C2 stable-manifold theorem for a finite-dimensional hyperbolic fixed point of a C2 local diffeomorphism. The suspension, phase estimate, coorientation, normal scalar ODE, H collar and first-order nonvanishing argument have been supplied above. The source's Panageas-Piliouras citation is not needed as a replacement for these deductions, and its cited book is not claimed to have been read.

The Euler input is the exact Lamb and Cauchy identities, div U=0 and consequently div B=3c, and the confirmed global closed-vortex obstruction A014. A444 and A445 supply the orbit data for a periodic exceptional nonflat measure in the globally helicity-free class; their global hypotheses remain necessary when that corollary is invoked. The local-helicity strengthening does not derive those orbit data for a general profile.

No aperiodic measure, equilibrium, first-jet-flat point, nonzero local helicity or unrestricted decay-only conjecture is excluded here. The complete proof was written before any computation; none is needed or planned. The submitted LIT98 proof and the complete focused review are preserved in verification. The review independently checked the stronger local-helicity application. Its further observation that some orbit data are redundant is not needed to enlarge the statement here.
