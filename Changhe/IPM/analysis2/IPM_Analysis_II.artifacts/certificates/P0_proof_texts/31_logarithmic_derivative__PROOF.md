# Keeping the radial factor in the cylinder derivative

Status: analytical proof and two independent arithmetic implementations are complete. Exact rational basis, trace and cylinder identities have also been checked. Lead review was CORRECT at 2026-10-28T08:17Z; its independent interval computation is confirmed by V123. The result concerns the unweighted Route U norm and six fixed stationary branches.

## 1. Exact statement

For every n-dimensional span E of n distinct exponentials exp(-b_j tau), b_j>0, in L2(0,infinity;d tau),

    ||tau partial_tau f||2^2<=n(n^2+2)||f||2^2/6,
                                            f in E.       (1)

No separation or upper bound on the b_j is needed. This is an explicit sufficient constant; no optimal operator-norm claim is made.

Let a_1,...,a_n>-1/2 be distinct, w(u) in their power span on(0,1), u=(1+r^2)^-1, and s=log r. Put

    g(s)=sqrt(u(1-u))w(u).

Then

    ||partial_s g||2^2<=Q_n||g||2^2,
    Q_n=[2n(n^2+2)+1]/3.                                (2)

Both norms in(2) use ds. This improves the preceding sufficient bound by retaining1-u in the cylinder derivative.

Apply this to the exact potential family

    chi=sum_(0<=j<=5,0<=m<=59,m<=k<=K) a_(j,m,k)
         r^(2k)(1+r^2)^((3+gamma-jdelta)/2-k)cos(2m theta),

for K>=59, c=4076476460239181/2251799813685248, gamma=1/c, delta=1-gamma. Set rho=-partial_y Delta chi, U=(-chi_xyy,chi_xxy), F=(cX+U).D rho-rho. Impose the six fixed stationary leading potential branches determined by original state131, and the vanishing first descendants of branches j=0,1, exactly as in topics26 and30. All coefficients are real and unrestricted in magnitude; the center normalization is optional here. Put a_star=7delta/2-2,

    A_K={ell delta/2+k-2:1<=ell<=12,0<=k<=2K+4,
                                   ell delta/2+k-2>=a_star},
    n_K=12(2K+5)-8,
    D_K=(2a_star+1)^(-1/2)
                product_(a in A_K,a>a_star)(a-a_star)/(a+a_star+1).

Let e_m be the fixed coefficient of sin(m theta) in the residual sector r^(1-7delta), with positive odd m<=139. Then the actual homogeneous negative norm satisfies

    ||F||_(dot H^-1)>=D_K sqrt((pi/2)
                                   sum_m e_m^2/(m^2+Q_(n_K))).        (3)

The exact Route U norm N_U=E2(J^(2^-18).) consequently satisfies

    N_U(F)>=Bnew_K,
    Bnew_K=(1-34*2^-18)*512sqrt(20/21)
                  D_K sqrt((pi/2)sum_m e_m^2/(m^2+Q_(n_K))).          (4)

Bnew_K strictly decreases with K. A certified comparison Bnew_K>eta_U=1/1572864 excludes the current sufficient Route U residual threshold for the entire stated family. A value below eta_U makes this formula inconclusive there. It is not an existence or feasibility conclusion. Adding branch j=6 changes the problem and is not covered.

## 2. An orthonormal basis for the exponential span

Use the Laplace transform F(z)=int_0^infinity exp(-z tau)f(tau)d tau, with boundary norm

    ||f||2^2=(1/(2pi))int_R |F(i omega)|^2 d omega.

For each j=0,...,n-1 define

    Phi_j(z)=sqrt(2b_j)/(z+b_j)
                    product_(i<j)(z-b_i)/(z+b_i).        (5)

The simple poles show that Phi_j is the Laplace transform of a function phi_j in the span of exp(-b_i tau), i<=j. Its coefficient at the newly introduced pole-b_j is nonzero, since the b_i are distinct. Each boundary factor(z-b_i)/(z+b_i) has modulus1 at z=i omega, so

    |Phi_j(i omega)|^2=2b_j/(omega^2+b_j^2),
    ||phi_j||2=1.

For i<j, Phi_j(z)Phi_i(-z) has only left-half-plane poles and decays quadratically at infinity: all right-half-plane poles cancel with the factors in Phi_j. Closing the imaginary-axis contour in the right half-plane gives zero integral. Equivalently one may integrate its partial fractions directly. Thus <phi_j,phi_i>=0. The n triangularly independent vectors form an orthonormal basis of E. This argument establishes the basis used below, rather than assuming a named rational-function theorem.

## 3. The norm of tau partial_tau on each basis vector

Integration by parts and differentiation of the Laplace integral give

    Laplace(tau f')=-F-zF'.                              (6)

The constant boundary term f(0) in Laplace(f') disappears under z differentiation. The finite exponential functions justify every operation absolutely in the right half-plane and by L2 limits on its boundary.

At z=i omega set

    A_i(omega)=2b_i omega/(omega^2+b_i^2),
    P_b(omega)=b/[pi(omega^2+b^2)].

P_b is a probability density. Logarithmic differentiation of(5) shows that the multiplier in(6) is

    -b_j/(b_j+i omega)+i sum_(i<j) A_i(omega).

Its squared modulus is

    b_j^2/(b_j^2+omega^2)
       +A_j sum_(i<j)A_i+(sum_(i<j)A_i)^2.              (7)

All quantities in(7) are real. The imaginary part of-b_j/(b_j+i omega) is A_j/2, which accounts for the middle term.

Direct integration against P_(b_j) gives

    E[b_j^2/(b_j^2+omega^2)]=1/2,
    E[A_i^2]=2b_i b_j/(b_i+b_j)^2<=1/2.                 (8)

For example, E[1/(omega^2+a^2)]=1/[a(a+b_j)]. Differentiating this identity in a and subtracting gives E[omega^2/(omega^2+a^2)^2]=b_j/[2a(a+b_j)^2], proving the second formula. All poles lie off the real axis and all differentiated integrals are absolutely convergent. Cauchy-Schwarz now gives |E[A_i A_k]|<=1/2. Integrating(7), with exactly j preceding terms, yields

    ||tau phi_j'||2^2<=(j^2+j+1)/2.                     (9)

For f=sum c_j phi_j, Cauchy-Schwarz in the finite vector index gives

    ||tau f'||2^2<=(sum_j |c_j|^2)
                              sum_j ||tau phi_j'||2^2.

The last sum is at most n(n^2+2)/6. Orthogonality gives sum|c_j|^2=||f||2^2. This proves(1). It is a Hilbert-Schmidt estimate, which suffices here even though it need not give the smallest operator norm.

There is an independent exact formula for the sum before this bound:

    sum_j ||tau phi_j'||2^2
      =n/2+4sum_(i<j) b_i b_j/(b_i+b_j)^2
             +8sum_(i<j<k)
                 b_i b_j b_k/[(b_i+b_j)(b_i+b_k)(b_j+b_k)].          (10)

Indeed E_(b_j)[A_i A_k]=4b_i b_k b_j/[(b_i+b_k)(b_i+b_j)(b_k+b_j)]. Substitute this into(7) and group pairs and triples. Each normalized pair and triple summand in(10) is at most1 by arithmetic-geometric mean. This independently recovers the same upper bound. The formula is used only for small exact audit cases; evaluating its large triple sum is unnecessary.

## 4. Exact transformation to the radial cylinder

Set tau=-log u, t=1-u=1-exp(-tau), and

    f(tau)=exp(-tau/2)w(exp(-tau)).

Its exponents are b_j=a_j+1/2>0. This transformation is unitary from L2(0,1;du) to L2(0,infinity;d tau). Moreover

    g(s)=sqrt(t)f(tau), ds=d tau/(2t),
    ||g||2^2=(1/2)||f||2^2,
    ||partial_s g||2^2
       =(1/2)||exp(-tau)f+2(1-exp(-tau))f'||2^2.         (11)

These identities follow by differentiating r^2=exp(tau)-1. They include the derivative of the prefactor, which is essential.

Write u=exp(-tau). Expand the last square and integrate its mixed term by parts. The boundary term u(1-u)|f|^2 vanishes at both0 and infinity, since f is a finite sum of decaying exponentials. The exact result is

    ||u f+2(1-u)f'||2^2
       =4||(1-u)f'||2^2+int(2u-3u^2)|f|^2 d tau.       (12)

Since0<=1-exp(-tau)<=tau and2u-3u^2<=1/3 for0<=u<=1, equations(1),(11),(12) prove(2). This is the step that retains the radial cancellation lost when u partial_u is bounded first.

## 5. Full-plane consequence

Topic30 gives the exact residual representation with compactified degree2K+4. Its eight cancellations remove all exponents below a_star, and its u^a_star coefficient is the fixed e_m. Its exact monomial-distance identity gives ||w_m||2>=|e_m|D_K. The residual lies in the actual homogeneous negative space; its mode cylinder functions belong to H1 by the endpoint exponents and origin regularity.

For each m>=1 the Poisson inverse is(-partial_s^2+m^2)^-1 and

    <g_m,(-partial_s^2+m^2)^-1g_m>
      >=||g_m||2^4/(||partial_sg_m||2^2+m^2||g_m||2^2).

Apply(2), the measure factor1/2 in(11), and the monomial-distance bound. Multiplication bypi and summation over orthogonal sine modes prove(3). The previously verified Route U comparison gives(4). The vector e is fixed and nonzero, D_K decreases strictly and n_K increases strictly, proving the claimed monotonicity.

## Dependencies and scope

The standalone family, exact source data, radial degree count, eight cancellations, fixed sine vector and Route U comparison are specified in26_uniform_family_gap/PROOF.md and30_radial_degree_obstruction/PROOF.md. The present proof independently supplies the exponential derivative estimate, its exact trace formula, and the complete cylinder transformation. Its numerical constants were checked from the same source-bound exact sine vector using separate gamma-product and direct-product implementations at384 and512 bits. Every one of21 rows agrees. Four unrelated rational exponential sets independently verify all basis orthogonality, exact trace and complete cylinder identities.

The certified comparisons are Bnew_75/eta_U>1308, Bnew_779/eta_U>1.0035179 and Bnew_780/eta_U<0.9995471. Consequently every59<=K<=779 fails the present Route U sufficient residual threshold. TheK779 family has270180 coefficient slots before constraints. TheK780 result only makes this formula inconclusive. Numerical evidence is in verification/constant_bound.py,json,log and verification/audit_derivative.py,json,log.

No weighted norm lower bound, successful improved reference, or exact IPM profile is asserted. All positive conclusions are stated for the exact spaces and finite support above. The result gives a necessary change to the sufficient Route U program while keeping the six stationary branches fixed.
