# Conditional convergence at every irrational parameter

Status: PROVED after the theory part's independent 07:44Z review and the verifier recheck recorded in V184 at 2026-10-31T07:45:21Z. The argument establishes an equivalence, not convergence at all irrational parameters.

## Exact statement

Fix any irrational delta in(0,1), c=(1-delta)^(-1), and a nonzero finite real odd-sine polynomial f_1 with largest frequency L. Let f_n,g_n,h_n be the unique pure stationary density, stream and common-potential coefficients, so

    rho_n=r^(1-n delta) f_n(theta),
    psi_n=r^(2-n delta) g_n(theta),
    chi_n=r^(4-n delta) h_n(theta).

There are no polynomial-log terms at irrational delta. Put B=L+1, M_n=||f_n||_l1 and N_n=||g_n||_l1, using real angular amplitudes, equivalently the complex Fourier Wiener norm for these parity classes. The following conditions are equivalent:

1. M_n is bounded geometrically in n.
2. N_n is bounded geometrically in n.
3. The density, stream and common-potential series converge on a sufficiently distant exterior, absolutely with every fixed weighted Cartesian derivative, and their sums solve the stationary IPM equation.
4. At some radius r_0>0, the individual density terms are pointwise bounded on a measurable set of angles of positive length.
5. The same assertion as4 holds for stream terms, radial-velocity terms, or common-potential terms. Each of these three assertions separately suffices.

No Diophantine, Brjuno or other quantitative arithmetic hypothesis is needed for these equivalences. They concern the generated stationary sequence with a fixed finite leading profile.

If these conditions fail, there is a single set Theta of angles of full Lebesgue measure, which is also a dense residual subset of the circle, such that for every theta in Theta and every r>0 the individual terms of all four stated fields are unbounded. Thus all four series diverge along every ray with angle in Theta. The set Theta is allowed to depend on the fixed parameter and leading profile. There is no assertion of a common set for uncountably many parameters.

## Formal input and the stationary equation

The independent recurrence in topic01 gives, for n>=2,

    (c-1)(n-1) f_n
       =sum_(i+j=n)[P_i g_i f_j' - p_j g_i' f_j],
    p_n=1-n delta, P_n=2-n delta.

All coefficients are finite because irrationality excludes every integer resonance. The support bounds are deg f_n<=Bn-1 and deg g_n<=Bn. The pure common potential exists at every order by the same finite angular inversion, since 4-n delta cannot be an integer. These are formal statements and do not presuppose convergence.

Write E=B(3-delta). The Wiener algebra property and the inequalities |P_i|<=(2-delta)i, |p_j|<=j give

    ||P_i g_i f_j' - p_j g_i' f_j||<=E i j N_i M_j.   (1)

The same estimate holds in any fixed exponential angular coefficient weight.

## Stream growth controls density growth

For n>=2, (1) and n/(n-1)<=2 imply

    n M_n <=D_0 sum_(i+j=n)i N_i j M_j,
    D_0=2E/(c-1).

If N_i<=H A_0^i, set Y_n=n M_n and K=D_0H. Let y_* be the smaller root in(0,1) of K y=(1-y)^2 and let A_1=A_0/y_*. Then

    K sum_(i>=1)i y_*^i=1.

Induction from Y_1=M_1 gives Y_n<=M_1 A_1^(n-1), exactly as in topic93. This proves2=>1 without using any Poisson multiplier estimate.

## Density growth controls stream growth

Write f_1=sum_(k<=L)a_k sin(k theta), with a_L!=0 and odd positive k. Choose a fixed rho>=4 such that

    S=sum_(k<L)|a_k|rho^k/(|a_L|rho^L)<=1/16.

Set T=|a_L|rho^L/2 and ||v||_rho=sum_m |v_m|rho^m. Since angular frequencies are at most Bn,

    X_n:=||f_n||_rho<=rho^(Bn) M_n,
    N_n<=Y_n:=||g_n||_rho.

For i delta>=16 define a=i delta-2>0, p=1-delta>0 and

    L_i g=-a g f_1' -p f_1 g'.

The same highest-harmonic estimate as topic98, now with no log derivative, gives

    ||L_i g||_rho>=T L delta i ||g||_rho/8.        (2)

Here is the estimate explicitly. Each coefficient g_m, m>=2 even, has an upper contribution at m+L of coefficient -a_L(La+pm)g_m/2. These output indices are distinct, so their total norm is T[La||g||_rho+p||g'||_rho]. Lower contributions have relative weight at most rho^(-2)<=1/16 and no larger modulus. Every lower leading harmonic k<L contributes in both branches at most |a_k|rho^k(1+rho^(-2))[La||g||_rho+p||g'||_rho]/2. Subtracting these bounds gives

    ||L_i g||_rho>=(223/256)T[La||g||_rho+p||g'||_rho].

Since a=i delta-2>=i delta/2 for i delta>=4, this is stronger than(2). The proof has no small denominator.

At density order i+1 the pair(i,1) is exactly L_i g_i. All other stream indices k are less than i. Thus (1), (2), and (c-1)i=c delta i imply, for i delta>=16,

    Y_i<=U X_(i+1)+V sum_(k+j=i+1,k<i)j Y_k X_j,
    alpha=8/(TLdelta), U=alpha c delta, V=alpha E.  (3)

We used k/i<=1. If M_n<=C A^n, put A_*=max(1,A rho^B) and K_*=V C A_*. Choose H_*>=U C A_* and H_*>=Y_i/A_*^i for the finitely many i with i delta<16. Then(3) becomes for every i>=1

    Y_i<=H_* A_*^i
         +K_* sum_(l=1)^(i-1)(l+1)A_*^l Y_(i-l).

For A_2=A_*max(4,8K_*), y=A_*/A_2<=1/4, the normalized convolution mass is

    K_* sum_(l>=1)(l+1)y^l
       =K_*y(2-y)/(1-y)^2<=4K_*y<=1/2.

Induction yields Y_i<=2H_* A_2^i. Therefore1=>2. The finite constants may be large and depend on delta and the leading profile. No uniform N_n/M_n bound or equality of limiting growth bases is claimed.

## Common-potential reconstruction without arithmetic loss

Suppose M_n,N_n<=C A^n after enlarging C,A if needed. The joint reconstruction in topic41 does not use rationality except to bound log degree. Here that degree is zero. We give the pure specialization to make this dependence explicit.

For X=n delta>=20, put q=4-X and write Y=partial_y chi_n=r^(q-1)V_n(theta). The identities Y_x=psi_n and -Delta Y=rho_n give the Euler identity

    (q-1)(q-2)V_n
       =cos(theta)P_n g_n+sin(theta)g_n'
          -sin(theta)^2 f_n.                    (4)

Both scalar factors on the left have modulus at least X/4. The angular factors have Wiener norm one, and ||g_n'||<=Bn N_n, |P_n|<=X. Hence

    ||V_n||<=16/X^2 [M_n+n(B+delta)N_n].          (5)

To recover h_n, solve partial_y(r^q h_n)=r^(q-1)V_n. If V_n=sum_(m>=0)v_m sin((2m+1)theta), h_n=sum_(m>=0)c_m cos(2m theta), and x=-q/2>=1/2, the descending equations are

    -v_0=2x c_0+(1-x)c_1,
    -v_m=(m+x)c_m+(m+1-x)c_(m+1), m>=1.

Since |m+1-x|<=m+x and |1-x|<=x, downward substitution yields

    |c_m|<=sum_(k>=m)|v_k|/(k+x), m>=1,
    sum_(m>=1)|c_m|<=sum_(k>=1)|v_k|,
    |c_0|<=|v_0|+one third sum_(k>=1)|v_k|.

The last estimate uses 2x>=1 and 1+x>=3/2. Thus ||h_n||<=3||V_n|| and its largest frequency is no greater than Bn. Equation(4) uniquely recovers the y derivative of the formal common potential, so this h_n generates the same density and stream. Combining with(5) gives

    ||h_n||<=48/X^2 [M_n+n(B+delta)N_n].          (6)

Finitely many earlier orders are harmless. Hence the potential coefficients are geometric too. For every sufficiently large R with A R^(-delta)<1, remove the respective leading radial powers from the three series. Their terms are geometrically summable uniformly on r>=R. Each fixed weighted Cartesian derivative costs only a polynomial in n, since radial exponents and angular frequencies are O(n). Its series is therefore summable too. Differentiation and the nonlinear Cauchy products are justified, and the formal equations pass to the sums. This proves1 or2=>3. The strict geometric margin also gives local real analyticity. Condition3 immediately implies bounded terms on a distant full circle.

## Recovering angular coefficients on one circle

Let u_n(r,theta)=r^(beta-n delta)v_n(theta), where beta is fixed, v_n is a trigonometric polynomial of frequency at most Bn, and its coefficient norm is Q_n. Suppose the terms are pointwise bounded at r=r_0 on a measurable angular set E of positive length. Extract a subset E_J of positive length eta on which |u_n(r_0,theta)|<=J for every n; the increasing union of these subsets is E.

The trigonometric interpolation lemma of topic94 gives

    Q_n<=J r_0^(-beta)
          [r_0^delta (16pi e/eta)^(2B)]^n.        (7)

This is geometric. The lemma follows by choosing 2M+1 separated nodes in a half-period retaining half the measure, interpolating z^M v_n at z=exp(i theta), and using coefficient numerator bound2^(2M), chord separation and (2M)!>=(2M/e)^(2M). Its complete proof and exact constants are in topic94.

For density take beta=1 and v_n=f_n, giving4=>1. For stream take beta=2 and v_n=g_n, giving its version of5=>2. For radial velocity take beta=1 and v_n=-g_n'; its coefficient norm is at least2N_n because the nonzero stream frequencies are even and at least2. For the potential take beta=4 and v_n=h_n. Two Cartesian derivatives yield N_n<=C n^2 Q_n for a fixed C at large n, which again implies a geometric N_n bound. This proves every stated equivalence.

## One angular exceptional set for all radii

Assume the equivalent conditions fail. For each positive integer radius k and each of the four fields, the boundedness set

    Z_(k,field)=union_(J>=1) intersection_(n>=1)
                         {theta: |u_(n,field)(k,theta)|<=J}

is a countable union of closed sets. By(7) and the equivalences it has measure zero. Every closed constituent has empty interior, so the set is meagre. Take Theta to be the complement of the union of these sets over the countably many k and four fields. Then Theta has full measure and is a dense residual subset of the circle.

Fix theta in Theta and r>0. Choose an integer k>=r. For every field with its corresponding constant beta,

    |u_n(r,theta)|=(r/k)^beta (k/r)^(n delta)
                                      |u_n(k,theta)|.

The first factor is a fixed positive number and the second is at least one. Since the terms at k are unbounded, those at r are unbounded. This proves the assertion simultaneously for every positive radius and all four fields.

In particular, each already established divergent irrational parameter for the single-sine profile, including the computable examples in topics31-32, has divergence of all these fields along almost every ray. The parameter may lie in the residual, measure-zero divergent set, while almost every parameter satisfies the Brjuno convergence theorem. These two quantifiers are distinct. The theorem does not select a single angular exceptional set uniformly in the parameter.

## Dependencies and limits

Topics01 and06 supply formal pure reconstruction and support. Topics93 and98 supply the two majorant patterns, reproduced here without logarithms. Topic41 supplies the Euler reconstruction, specialized and proved above without an arithmetic divisor. Topic94 supplies measurable angular interpolation. Topics31-32 supply the previously proved existence of divergent irrational parameters for the final application. The present proof makes no quantitative statement about the size of the resulting exterior radius and does not assert convergence at a non-Brjuno parameter without a geometric coefficient bound.
