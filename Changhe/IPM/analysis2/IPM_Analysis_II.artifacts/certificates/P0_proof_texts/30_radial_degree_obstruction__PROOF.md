# Radial degree needed to escape the present unweighted residual obstruction

Status: CONFIRMED by the proof below, independent exact compression tests and384/512-bit arithmetic. Lead review was CORRECT at 2026-10-28T08:17Z; its independent interval computation is confirmed by V123. This concerns the same six stationary branches as topic26. Adding a seventh branch changes the fixed-sector problem and is outside this statement.

## 1. Exact family and conclusion

Set c=4076476460239181/2251799813685248, gamma=1/c, delta=1-gamma and a_star=7delta/2-2. For an integer K>=59 consider every real potential

    chi=sum_(0<=j<=5,0<=m<=59,m<=k<=K) a_(j,m,k)
          r^(2k)(1+r^2)^((3+gamma-jdelta)/2-k)cos(2m theta).

Put rho=-partial_y Delta chi, U=(-chi_xyy,chi_xxy), F=(cX+U).D rho-rho. Impose the six stationary leading potential branches and the two vanishing first descendants exactly as in topic26. The center normalization may be imposed but is not needed here. The potential coefficients have no size restriction. The canonical realization, parity and exact original leading profile are those in that topic.

Let e_m, positive odd m<=139, be the fixed sine coefficients of F at radial degree1-7delta. Define

    A_K={ell delta/2+k-2:1<=ell<=12,0<=k<=2K+4,
                                   ell delta/2+k-2>=a_star},
    S_K=sum_(a in A_K)(2a+1),
    C_K=sqrt(4 S_K^2/pi^2+1/4),
    D_K=(2a_star+1)^(-1/2)
                 product_(a in A_K,a>a_star)(a-a_star)/(a+a_star+1),
    B_K=(1-34*2^-18)*512sqrt(20/21)*D_K
              *sqrt((pi/2)sum_m e_m^2/[m^2+(1+2C_K)^2]).

Then

    ||F||_(dot H^-1)>=D_K
              *sqrt((pi/2)sum_m e_m^2/[m^2+(1+2C_K)^2]),
    N_U(F)>=B_K,

where N_U is precisely the Route U norm E2(J^(2^-18).) of topics09 and11. In particular, any integer K with B_K>eta_U=1/1572864 excludes the current sufficient Route U residual threshold for this whole family. If a subsequent K has B_K<eta_U, the displayed sufficient obstruction has ceased to decide the issue there. It does not establish feasibility or existence at that K.

The numbers B_K strictly decrease with K. Thus one pair of certified adjacent comparisons determines the last integer excluded by this formula. Independent384-bit direct products and512-bit gamma-ratio calculations give B_349/eta_U>1.0019782 and B_350/eta_U<0.9917770. Hence every59<=K<=349 is excluded by this formula. The formula does not decideK=350. At the existing supportK=75 its ratio is greater than233. The K=349 family contains115380 coefficient slots before affine constraints; the conclusion allows all their real values.

## 2. A dilation bound from compression of an integral operator

We first prove a statement for any finite strictly increasing real exponents a_0,...,a_(n-1)>-1/2. Let P be their power span in L2(0,1;du), and let B=u partial_u act on P. Put S=sum_i(2a_i+1). Then

    ||B||_(P->P)<=sqrt(4S^2/pi^2+1/4).                    (1)

Apply increasing-order Gram-Schmidt to the powers u^a_i. Choose its orthonormal basis p_i so that p_i(1)>0. The exact endpoint formula from topic26 gives p_i(1)^2=2a_i+1. Dilation preserves each preceding power span. Integration by parts, whose u=0 boundary term vanishes since all exponents exceed-1/2, gives

    <Bp_i,p_j>+<p_i,Bp_j>=p_i(1)p_j(1)-delta_ij.

The triangular matrix of B therefore has diagonal a_i and upper entries sqrt((2a_i+1)(2a_j+1)) for i<j, with all lower entries zero.

Partition the interval(0,S) into consecutive intervals I_i of lengths l_i=2a_i+1. Let P_step denote the orthogonal projection onto functions constant on these intervals, with orthonormal basis1_(I_i)/sqrt(l_i). Define

    (Tf)(x)=int_x^S f(y)dy.

Its compressed matrix P_step T P_step has diagonal l_i/2 and upper entries sqrt(l_i l_j). Hence the matrix of B is exactly that of P_step T P_step-I/2. For every function f in this step space,

    ||Bf||2^2=||P_step Tf||2^2-Re<Tf,f>+(1/4)||f||2^2.

Fubini gives Re<Tf,f>=(1/2)|int_0^S f|^2>=0, also for complex f. Moreover

    ||Tf||2<=(2S/pi)||f||2.                              (2)

For completeness, g=Tf satisfies g(S)=0 and g'=-f. Reflect g evenly across0 to(-S,S). The reflected function belongs to H1_0(-S,S), so its elementary first Dirichlet sine-mode inequality is ||g||2<=(2S/pi)||g'||2. The two reflected squared norms each acquire a factor2, which cancels. This proves(2). Orthogonal projection decreases norm. Substituting(2) into the preceding identity proves(1).

This proof is independent of a numerical singular value calculation. Compared with the Frobenius bound of topic26, its leading coefficient in S is2/pi instead of1/sqrt(2). We use(1) directly; no assertion about optimality on the finite power span is needed.

## 3. Compactified residual and the fixed coefficient

Set u=(1+r^2)^-1 and t=1-u. For each generator separately, the Cartesian derivative recurrence and its origin regularity give degree bounds K+1 after three derivatives and K+2 after four derivatives, after removing the same radial factor as in topic26. The nonlinear product therefore has degree at most2K+3. The linear terms have degree at mostK+2. For every sine mode one can write

    F_m(r)=sqrt(t)u^(-1/2)H_m(u),
    H_m=sum_(ell=1)^12 u^(ell delta/2)P_(ell,m)(t),
    deg P_(ell,m)<=2K+3.

Put w_m=t u^-2 H_m. Its integer degree bound is2K+4, so it is a sum of powers in A_K once the eight required sectors are removed. Exactly the same eight exponents precede a_star for every K>=59. Their triangular relation with the exterior expansion makes their coefficients zero. The coefficient of u^a_star is exactly e_m. Distinct exponent classes cannot resonate: their ell difference has magnitude at most11, smaller than the denominator needed for an integer relation with the exact delta.

The coefficient e_m only involves the six prescribed leading stationary branches. There is no branch j=6 supplying a linear term at degree1-7delta. Increasing the radial degree introduces descendants but no new leading branch, so it cannot change e_m.

The exact power-space distance of topic26 now gives

    ||w_m||_(L2(du))>=|e_m|D_K.                          (3)

The canonical fields are smooth at the origin and decay sufficiently at infinity after the eight cancellations. In particular g_m(s)=r^2F_m(r), s=log r, belongs to H1(R;ds). Its exact norm conversion is

    ||g_m||2^2=(1/2)||w_m||2^2,
    ||partial_s g_m||2<=(1+2||B||)||g_m||2.              (4)

To verify the second identity, g_m=sqrt(u(1-u))w_m and partial_s=-2u(1-u)partial_u. Differentiate the prefactor and use |2u-1|<=1 and1-u<=1. The same measure du/[2u(1-u)] as in topic26 removes the prefactor. Applying(1) to the space A_K proves(4) with C_K.

## 4. The actual negative norm and the threshold

For m>=1, the planar Poisson equation reduces in the log-radius coordinate to(-partial_s^2+m^2)phi_m=g_m. Its Dirichlet energy is pi times the corresponding cylinder energy. Positive self-adjoint spectral calculus and Cauchy-Schwarz give

    <g_m,(-partial_s^2+m^2)^-1g_m>
       >=||g_m||2^4/(||partial_s g_m||2^2+m^2||g_m||2^2).

Substitute(3)-(4), multiply bypi, and sum the orthogonal sine energies. Every omitted angular mode has nonnegative energy. This proves the first claimed bound. The established comparison

    N_U(F)>=(1-34*2^-18)E2(F),
    E2(F)>=512sqrt(20/21)||F||_(dot H^-1)

proves the bound B_K in the exact Route U norm. No weighted-to-unweighted replacement is made.

Finally A_K is strictly nested as K increases. Every new factor in D_K lies strictly between0 and1 because a_star>-1/2, while every summand2a+1 in S_K is positive. Thus D_K decreases strictly and C_K increases strictly. The vector e is fixed and nonzero. It follows that B_K strictly decreases. This proves the adjacent-comparison procedure.

## Dependencies and scope

26_uniform_family_gap/PROOF.md supplies the exact stationary affine constraints, original e_m, monomial-distance identity, endpoint formula and cylinder realization. Its two independent programs recover the original source and verify those constants. Topics09/11 provide the Route U reverse norm comparison. The present proof supplies the new dilation bound, general degree count and monotonicity.

This is a quantitative obstruction to one current sufficient unweighted threshold over six fixed stationary branches and bounded radial degree. It is neither a weighted obstruction nor nonexistence of full-plane profiles. It allows arbitrarily large coefficients within the specified finite support. A seventh stationary branch is not in the family and requires a separate audit.
