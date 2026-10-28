# Audit of the quantitative compact-defect proposal

## Scope and accepted inputs

This note audits the answer in theory author/second-model referee/INJ_defect/answer.md, read in full on October 28, 2026. The spaces R, D_R, B, G, Z and Y, the actual background, bounded coupling and qualitative Garding estimate are precisely those of proof 76. Proof 82 supplies the actual margin 5/2. No assertion below certifies the still unknown compact-defect norm, its finite-rank approximation, an adjoint witness, injectivity, or a practical rank for the actual operator.

The consultation contains a useful conditional construction. The following elementary statements are proved independently. Its axis-strip constant can be supplied by proof 93. A sharper principal real-energy estimate is investigated separately in proof 94.

## Exact finite-rank construction

Let H be a Hilbert space. Let S0 and R0 be bounded self-adjoint operators, with ||R0|| <= delta, and let P be an orthogonal projection of rank N. Set Q=I-P. Suppose Q S0 Q <= epsilon Q, with epsilon >= 0. Then

 S0+R0 <= epsilon I+KF+R0,
 KF=P S0+S0 P-P S0 P,
 rank KF <= 2N.                                             (1)

Indeed expand S0 in its four P,Q blocks. The three blocks containing P sum to KF, while the fourth is Q S0 Q. If p1,...,pN is an orthonormal basis of ran P, the range of KF is contained in the span of p_i and S0 p_i. This proves (1), including self-adjointness. Keeping only P S0 P is unjustified: S0=[[0,1],[1,0]] and P=diag(1,0) have Q S0 Q=0 but S0 is not <=0. This exact two-dimensional example checks the cross terms.

For R=L2(w dX), the cylinder unitary is J h=e^t sqrt(w(e^t,theta)) h(e^t,theta), using dt dtheta on the cylinder. The Jacobian is dX=e^(2t)dt dtheta. With the actual weight its radial exponents are -13/4 at t<0 and 3/8 at t>0; the corresponding homogeneous density lines are sigma=13/4 and sigma=-3/8. These identities are exact, not approximations.

## Hilbert-Schmidt approximation and derivative bounds

For A:H1->H2 Hilbert-Schmidt, let e_m and f_n be orthonormal bases and a_nm=<A e_m,f_n>. Retain m<=M,n<=N. Orthogonality in the Hilbert-Schmidt space gives

 ||A-A_NM||^2 <= ||A||_HS^2-sum_(m<=M,n<=N)|a_nm|^2.        (2)

Every term omitted from the sum is nonnegative. In interval arithmetic a valid upper bound therefore uses an upper endpoint for the total squared norm and lower endpoints for the retained squared coefficients. Orthonormality refers to the actual input and output inner products. The cellwise weighted Legendre family is orthonormal in L2 of that weight, but is not a graph-space basis without a separate Gram construction.

Suppose, after unitary weight flattening, the kernel has square-integrable first derivatives on a rectangular core. Project onto constants on rectangular source and output cells. Orthogonality of the projections splits the error into an output projection error and the remaining input projection error. The one-dimensional interval inequality ||f-average f||_2 <= h ||f'||_2/pi, applied successively in each coordinate and integrated in the others, gives

 ||A-A_h||_HS^2 <= E_exterior^2
       +sum_source h_i^2 ||partial_i K||_2^2/pi^2
       +sum_output h_i^2 ||partial_i K||_2^2/pi^2.           (3)

E_exterior is the actual flattened kernel norm off the product core. This estimate requires the displayed derivative integrals, not just Hilbert-Schmidt membership. The interval inequality follows by the cosine-series expansion of f-average f on an interval; its first nonzero Neumann frequency is pi/h. Density extends it from smooth functions to H1.

For a degree-p Legendre projection on an interval I, the corresponding bound is

 ||(I-P_p)f||_2^2 <= |I|^2 ||f'||_2^2/[4(p+1)(p+2)].        (4)

To see this, map I to [-1,1]. The Legendre equation and integration by parts give sum n(n+1)|f_n|^2=integral (1-z^2)|f'(z)|^2 for the orthonormal expansion, first for polynomials and then by approximation. Bound the omitted eigenvalues below by (p+1)(p+2), use 1-z^2<=1, and rescale. No rate is inferred from compactness alone.

## Energy-to-preconditioned conversion

Suppose T_R:D_R->R is an isomorphism, C_R:R->R bounded with norm M_C, and

 m||h|| <= ||(T_R+C_R)h||+||KF h||, m>0.

Set q=T_R h, A_R=I+C_R T_R^(-1), a_R=m/(m+M_C), and K_R=M_C KF T_R^(-1)/(m+M_C). The triangle inequality ||q||<=||A_Rq||+M_C||h|| followed by the assumed estimate gives

 a_R||q|| <= ||A_Rq||+||K_Rq||.                            (5)

Thus the raw margin m is not the dimensionless lower constant of the preconditioned operator. If M_C=0, a_R=1 and K_R=0, so the same formula remains meaningful.

Suppose on an orthogonal product H1 direct-sum H2,

 F0=[[I,0],[B,A_R]]+J0,  ||B||<=b,

where J0 is compact. Put a=a_R, s=a^2+b^2+1 and

 mT=a sqrt(2/[s+sqrt(s^2-4a^2)]).                         (6)

This is the reciprocal of the Euclidean operator norm of [[1,0],[b/a,1/a]]. Applying (5) to the second coordinate gives

 mT||(p,q)|| <= ||F0(p,q)||+||K(p,q)||,
 K(p,q)=sqrt(2)(J0(p,q),(mT/a)K_Rq).                       (7)

For the proof, if y is the triangular output then |p|=|y1| and |q|<=(|y2|+b|y1|+|K_Rq|)/a. Take the Euclidean norm, use (6), and then F0 minus J0. The sum of the last two error norms is at most sqrt(2) times their Hilbert product norm. Their approximation errors combine as sqrt(2dJ^2+2(mT/a)^2 dR^2). Since a<=1, the weaker choice mT=a/(1+b) also works by the triangle inequality for the displayed matrix.

In the actual transport product, the lower triangular transport block cannot be discarded. If T=[[T_G,0],[T_E,T_R]], one possible principal B is -C_R T_R^(-1)T_E T_G^(-1), so b may be bounded by ||C_R||||T_R^(-1)|| ||T_E|| ||T_G^(-1)||. None of those uncomputed norms is supplied by the energy margin alone. Proof 90 offers an alternative reduction directly through S1 on R.

## Rank-one bordering

For any bounded F0 and a bounded vector-functional pair u,ell, the bordered map [[F0,u],[-ell,1]] is invertible if and only if F0+u ell is. This follows by solving its scalar row s=ell(x)+g and substituting into its first row. If F0 itself is invertible, the scalar denominator is d=1+ell(F0^(-1)u). For d!=0 direct multiplication proves

 (F0+u ell)^(-1)=F0^(-1)-F0^(-1)u ell F0^(-1)/d.           (8)

If d=0, F0^(-1)u is a nonzero kernel vector unless u=0; the latter would force d=1. Exact retention of this rank-one term therefore does not establish injectivity. A numerical enclosure of d needs a rigorous solve error.

## Localization and kernel cautions

For bounded H and real cutoffs with sum chi_j^2=I,

 H-sum chi_j H chi_j=-sum chi_j[H,chi_j].

For self-adjoint H this also equals (1/2)sum[chi_j,[chi_j,H]]. The latter kernel has the factor (chi_j(X)-chi_j(Y))^2. On a compact regular two-dimensional patch this cancels an order-zero |X-Y|^(-2) kernel to a bounded kernel, hence to a Hilbert-Schmidt operator. A single commutator only cancels one power, and its square has logarithmically divergent radial integral at the diagonal. It must not automatically be called Hilbert-Schmidt.

The dyadic input windows (2^(j-3),2^(j+3)) overlap six times almost everywhere. Their disjoint output annuli therefore give sqrt(6) times the largest localized norm. This proves the consultation's near-tail bound when the uniform dyadic coefficient is known. That coefficient and the separated-scale kernel tail remain separate inputs.

The separated strip integral defined using the exact parity-projected kernel is valid. Its pointwise derivative majorant must either sum over the reflected source points or work on a specified quadrant with a compatible output segment. Replacing every reflected distance by |X-Y| on the full plane is not generally valid. Jensen's inequality and invariance of w under reflections do give the corresponding integrated bound from an unprojected majorant on a reflection-invariant source region. This removes the convention ambiguity without claiming a false pointwise estimate.

Multiplication by a smooth function does not preserve a sharp high-frequency subspace. Thus the consultation correctly imposes both P_Lambda u=0 and P_Lambda(f^(-1)u)=0 when invoking an input high-frequency estimate after conjugation. Cutoffs create additional such constraints or require proved leakage bounds. A bounded weighted L2 projection is not automatically conforming in D_R.

The Fourier-moment estimate using three derivatives for S1, the explicit lattice sum, and the conjugation smoothing error (exp(2d)-1)||A_smoothed|| follow respectively from Cauchy-Schwarz/Parseval and expansion of r A_smoothed r^(-1)-A_smoothed with exp(-d)<=r<=exp(d). They apply only after the specified smooth regular extension and with its actual constants. A radial derivative jump need not have a finite first absolute Fourier moment.

## Verdict and remaining work

The algebraic constructions and conditional estimates in this note are CONFIRMED. The consultation does not certify a finite rank for the actual problem; its cost table is explicitly a scale illustration. The explicit compact strip constant is supplied in proof 93. Actual localization radii, coefficient bounds, kernel tails, Gram matrices and adjoint witnesses remain OPEN. No global inverse or nonlinear existence conclusion follows.
