# A quantitative conditional injectivity criterion

## The operator and the certificate

Let R=L2_P(w dX), where w=|x|^(-17/2)max(1,r)^(29/4), and P denotes even-x, odd-y parity. Let rho be the exactly joined, exactly normalized modal background specified in proof 76. Put V=ell X+U[rho], T=V.grad-1 on its maximal distributional graph domain D_R, and A=T+C_R. The operator C_R is the complete axis-subtracted remainder coupling, including its normalization terms. The domain D_R carries the norm (||u||_R^2+||Tu||_R^2)^(1/2). All adjoints below use the R inner product. Use the convention that the inner product is conjugate-linear in its first entry.

Topics76 and90 establish that A is closed, densely defined and Fredholm of index zero. Its real transport energy is

 Re<Tu,u>_R=-integral kappa_w |u|^2 w dX.

Proof 82 gives the exact bound kappa_w-bplus>=m=5/2, where bplus=(|grad rho|-rho_y)/2. Define the bounded self-adjoint defect

 S=sym(C_R)-M_bplus.

The following statement is conditional on a finite certificate for this specified operator. None of the certificate inputs below is supplied merely by the Fredholm theorem.

**INJ-Q.** Suppose an orthogonal finite-rank projection P on R, Q=I-P, and epsilon>=0 have been certified to satisfy

 <SQu,Qu>_R<=epsilon ||Qu||_R^2  for all u in R.          (1)

Define the exact self-adjoint finite-rank operator

 S_F=P S+S P-P S P.                                     (2)

Suppose finite columns e_i,phi_i in R, i=1,...,N, and psi_i in D(A*) are specified. Let E,Phi,Psi be their synthesis maps from C^N to R, and let D=Phi-A*Psi. Assume certified constants delta_F,e,p,d>=0 satisfy

 ||S_F-E Phi*||<=delta_F,
 E*E<=e^2 I,  Psi*Psi<=p^2 I,  D*D<=d^2 I.              (3)

If

 a=m-epsilon-delta_F>e d,                               (4)

then A is bijective, and

 ||A^(-1)||_(R->R)<=k1=(1+e p)/(m-epsilon-delta_F-e d).  (5)

If ||C_R||_(R->R)<=M_C is also certified, then

 ||A^(-1)||_(R->D_R)<=sqrt(k1^2+(1+M_C k1)^2).           (6)

The finite columns need not be orthonormal. The three Gram inequalities in (3) refer to their actual Hilbert-space inner products, with every quadrature, truncation and input error included. Verifying a matrix of sampled values or a floating singular value is insufficient. A certified positive-definiteness test for e^2 I-E*E, and the analogous matrices, is one way to verify (3). The parameter e may be zero, in which case the formula still applies.

## Producing the high-frequency condition

Here is an explicit sufficient form of (1). It states precisely where the regular estimates, strip estimates and compact-kernel approximations enter. Choose finitely many bounded localization maps J_j:R->H_j, where H_j is an unweighted regular torus Hilbert space, and certify

 sum_j ||J_j u||^2<=c_loc^2||u||_R^2.                   (7)

On each H_j use either the principal operator of proof 94 or the full regular Mellin operator of proof 96. Let Hreg_j denote its symmetric coupling minus multiplication by its bplus_j. Choose a cutoff Lambda_j and enclose every moment needed in the corresponding bound

 <Hreg_j v,v><=E_j ||v||^2,  v=Q_(Lambda_j)v.            (8)

For the full Mellin family, this means certifying the coefficient suprema and Fourier moments in

 E_j=eta_j/2+[S2mat(B_j)+S2(b_eta_j)]/(2 Lambda_j^2)
       +G0_j[(sigma_j+1)^2/((Lambda_j-1)^2-(sigma_j+1)^2)
                    +1/((Lambda_j-1)^2-1)]
       +6 max(|sigma_j+1|,1)G1_j/(Lambda_j-2-|sigma_j+2|)^2,

with eta_j>0, Lambda_j>2+|sigma_j+2| and no low-frequency pole in the defined family. The simpler principal bound drops the last two terms. All these E_j are nonnegative.

Suppose bounded self-adjoint E_small,K_l on R satisfy the exact quadratic-form inequality

 S <= sum_j J_j* Hreg_j J_j+E_small+sum_l K_l,
 ||E_small||<=epsilon_small.                            (9)

For each l provide a finite-rank operator F_l=E_l Phi_l* with

 ||K_l-F_l||<=delta_l.                                  (10)

The approximants F_l need not themselves be self-adjoint. Choose ran P to contain every column of Phi_l and every vector J_j* v with v a low Fourier mode |p|<Lambda_j on H_j. Then every u in ran Q obeys F_l u=0 and J_j u=Q_(Lambda_j)J_j u. Equations (7)-(10) imply (1) with

 epsilon=c_loc^2 max_j E_j+epsilon_small+sum_l delta_l.  (11)

If there are no regular pieces, the first term is zero. One may improve (11) using separate certified bounds for the sum of E_j||J_j u||^2. The displayed choice requires no orthogonality between patches. An independent spanning set for P is not presumed: its actual Gram matrix, rank and orthogonal projection must be certified, or its closed finite-dimensional span used in an exact argument.

## Required global error bounds

Equation (9) is a substantive hypothesis. It must include every difference between the actual C_R and the regular torus models. In particular:

* Real nonnegative cutoffs with sum chi_j^2=1 have no transport energy error. Their coupling localization error is the paired double commutator of proof 99. On a compact regular extension of the weight its explicit kernel is Hilbert-Schmidt. The regular weight-conjugation defect is treated by proof 95. Finite-rank approximation uses proof 92 with actual kernel-tail and derivative bounds.
* For a vertical strip in a compact annulus, proof 97 permits the near-input bound A_ax s, where

 A_ax=sqrt(Wmax/Wmin)[39 M20+(25 s0/2)M21
                           +(39 s0^2/6)M40+(25 s0^3/24)M41].

  Here 0<s<=s0<=R0/2, the output lies in R0<=r<=R1 and |x|<d<=s, Wmax=max(1,R1)^(29/4), and Wmin is a proved lower bound for the input radial weight factor. Without radial input localization take Wmin=1. The quantities M20,M21 are the axis suprema of |rho_xx|,|rho_xxy| on the stated y interval; M40,M41 are suprema of |rho_xxxx|,|rho_xxxxy| on the Taylor rectangle |x|<=s0. These are exactly the sets and derivatives in proof 93. Their actual enclosures, the strip widths, partition factors and operator-to-form conversion factors enter epsilon_small explicitly. This one estimate does not cover separated inputs or the lift row.
* Radial tails, source/output separation, the difference between the full-plane canonical inverse and a periodized model, angular-axis subtraction, finite-rank normalization and cross-patch interactions must appear either in E_small or among the K_l. None is removed by calling it compact. A kernel approximation requires its complete input and output Hilbert-space weights, reflected parity distances and all exterior integrals.
* If coordinate changes or lifts are not unitary, their actual norm comparisons enter (7),(9),(10). A high-frequency condition before multiplication by a nonconstant factor does not imply the corresponding condition afterward. The vectors defining P must impose the constraints on the actual J_j in (7).

A proof of (9) may use domination rather than equality, but it must account for every term with the correct sign. The accepted qualitative compactness proof is not an enclosure for epsilon_small, delta_l or delta_F. An output finite section alone is not such an enclosure either.

## Proof of INJ-Q

Expand S into its four P,Q blocks. The three blocks involving P sum to S_F, leaving S=S_F+Q S Q. The range of S_F is contained in ran P+S(ran P), so it is finite-dimensional. By (1), the energy identity and the bound kappa_w-bplus>=m, every u in D_R satisfies

 (m-epsilon)||u||_R^2
 <=-Re<Au,u>_R+Re<S_F u,u>_R
 <=||Au||_R||u||_R+||S_F u||_R||u||_R.

Replace S_F by E Phi* using (3) and divide by ||u|| when u is nonzero. For each column, the adjoint identity gives

 <phi_i,u>=<psi_i,Au>+<D_i,u>.

Consequently Phi*u=Psi*Au+D*u and

 ||E Phi*u||<=e p||Au||_R+e d||u||_R.

After absorption this proves (5) as a lower bound on A. It implies injectivity, and the already proved Fredholm index zero implies surjectivity. Finally Tu=Au-C_Ru gives (6). The zero vector causes no division issue.

To prove (11), take u in ran Q. By the choice of P, <v,J_j u>=<J_j*v,u>=0 for every low mode, and Phi_l*u=0. Insert these facts in (8)-(10), use (7), and bound each remaining quadratic form by its operator norm. This yields (1).

## Scope and verification

The conclusion concerns the remainder operator S_1=A only. The jet system and scalar border of proof 90 still require their own inverse certificate to conclude invertibility of L_red. The actual finite certificate (1)-(4), an actual value of M_C, and the jet-system certificate are OPEN.

The accompanying exact-rational finite-dimensional check tests the P,Q decomposition, the adjoint reconstruction, nonorthonormal Gram bounds and the constant in (5) on a nonsymmetric example. It also checks that keeping only P S P misses the cross terms. The Hilbert-space proof above supplies the infinite-dimensional argument; the finite test is only an independent algebra check.
