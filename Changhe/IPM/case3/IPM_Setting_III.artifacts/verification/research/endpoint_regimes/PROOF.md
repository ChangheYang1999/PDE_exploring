# Conditional information at the parameter endpoints

Date: 2026-10-20. Status: independent analytic reconstruction of the lead's ENDPT(a)-(d), with the qualifications below. This is not a full-class exclusion near either endpoint.

## Notation and dependencies

An exact primary profile obeys W.grad rho=rho, W=ell X+U, div U=0, curl U=-rho_x, the prescribed parities, smoothness, strictly sublinear growth, and the canonical velocity law. Write D=ell-1>0, a=rho_y(0)!=0, A=2ell-1, h=rho-ay, and sigma=sup|sym DU|_op. The origin relation is DU(0)=diag(D,-D).

Our independently checked weighted identity and inverse estimates give, for every 2<m<4,

    (m-1)ell-1 <= m sigma + |a| Qsign(m).                 (1)

The constants are the upper spectral edges of Jacobi operators with diagonal plus or minus d_j, d_1=1/4 and d_j=1/2 for j>=2, and off-diagonal

    b_j(m)=(m^2+4j^2)/(4|4j^2-m^2|).

The positive-diagonal operator bounds both signs. These are results59 and62, research/weighted_quadratic_sharp/PROOF.md and research/weighted_center_defect/PROOF.md. At m=3 the sign-independent rational upper bound is Qsign<1633/1000. Finiteness of sigma for exact profiles follows from the separate exterior regularity result; the arguments below can instead take the displayed uniform derivative bounds as extra hypotheses.

## 1. An explicit near-one exclusion with two extra bounds

For 3<=m<4 define

    B_m=1/2+b_2(m)+max(b_1(m),b_3(m)).

Then Qsign(m)<=B_m. Indeed b_j decreases with j for j>=2. The first positive-diagonal row has sum 1/4+b_1, the second has sum 1/2+b_1+b_2, the third has sum 1/2+b_2+b_3, and every later row has no larger sum than the third. The first row is smaller than the second. For finite sequences the quadratic form bound follows from 2|z_j z_(j+1)|<=|z_j|^2+|z_(j+1)|^2. Density then gives the bound on the entire infinite operator, without replacing it by a finite matrix.

Let K>0 and 0<=s<1/2. Choose 3<=m<4 such that beta=m-2-ms>0. Suppose an exact profile also satisfies

    |a|<=KD,                 sigma<=s.                       (2)

Inserting ell=1+D in (1) yields

    beta <= [K B_m-(m-1)]D.                                  (3)

If the coefficient in brackets is nonpositive, (2) is impossible for every D>0. If it is positive, (2) is impossible for

    0<D<beta/[K B_m-(m-1)].                                  (4)

For K=1, s=2/5, m=11/3, exact rational arithmetic gives

    B_m=18342/4669,       beta=1/5,
    beta/[B_m-(m-1)] = 14007/88370.

The decimal B_m is approximately 3.92846434. The rational interval endpoint, approximately .15850402, agrees with the source.

For any exact sequence D_n->0 and a_n->0, (1) at each fixed m first gives liminf sigma_n >= (m-2)/m. Taking m->4 only afterwards gives liminf sigma_n>=1/2. This is a necessary strain lower bound. It supplies no near-one exclusion when sigma is unrestricted.

## 2. Large-ell compactness and its actual limiting class

For exact profiles with ell_n->infinity, define q_n=rho_n/ell_n and u_n=U_n/ell_n. These satisfy

    (X+u_n).grad q_n=q_n/ell_n,
    div u_n=0,               curl u_n=-q_(n,x).               (5)

Assume the EXTRA uniform bound sup_n(||grad q_n||_inf+||Du_n||_inf)<infinity. Spatial dilations preserve this bound and the values q_n(0)=u_n(0)=0. On each compact ball the fields are uniformly bounded and equicontinuous. Arzela-Ascoli and a diagonal extraction give local uniform convergence along a subsequence to globally Lipschitz q,u with the same parities and at most linear growth. Distributional derivatives converge weakly. Writing transport as

    div((X+u_n)q_n)=(2+1/ell_n)q_n

passes it to the limit using uniform convergence of both factors on each test function's support. Therefore

    (X+u).grad q=0,     div u=0,     curl u=-q_x               (6)

in distributions. The product has its usual almost-everywhere Lipschitz meaning. Local uniform convergence alone does not pass origin derivatives or a nonzero origin slope. A common local C1,alpha bound would permit that stronger conclusion.

There is no zero Liouville theorem in the class just obtained: for every smooth odd f with bounded derivative,

    q(x,y)=f(y),                 u(x,y)=(x,-y)

solves (6), since X+u=(2x,0). Choosing f=tanh gives a nonzero bounded density. The limiting velocity is linear. Individual canonical sublinearity does not pass through local uniform convergence without a uniform estimate at infinity, so these examples belong to the class actually inherited. They do not refute a theorem imposing the additional canonical sublinear law on the limit.

For completeness, two globally Lipschitz velocities with the same density and parities differ by b(x,-y). Their difference has harmonic components. Each derivative is a bounded entire harmonic function and hence constant by the interior harmonic derivative estimate on disks of increasing radius. The difference is affine; parity eliminates constants and off-diagonal terms, and zero divergence leaves exactly b(x,-y).

The structural counterexamples in source Section3.3 also check out. Fix a nonzero smooth radial bump zeta supported in 2<r<3 and J=int zeta dr/r>0. For ell>=2, p=1/ell, a=kappa ell, let

    B_ell = a y(1+r^2)^(-(1-p)/2)
             +(a/4-D)r sin(3theta)zeta(r)/J,
    f = r sin(5theta)zeta(r).

Both are smooth because the angular bumps vanish near zero. The exact canonical strain formula c=-a/4+int rho3 r^-2 dr gives c[B_ell]=-D and c[f]=0. The density outside the bump has nonzero r^p first angular mode. With ell_n=n and rho_n=B_n+n^2 f, the normalized slope is kappa while ||grad(rho_n/n)||_inf>=n||grad f||_inf-C tends to infinity. The normalized radial background and its velocity have bounded first derivatives uniformly in p in (0,1/2], directly from the radial inverse integral; the fixed bump has bounded coefficient after division by n. Thus the constant C is uniform.

These are nonprofiles for large n, not counterexample solutions. Put b_n=B_n/n, w_n=U[B_n]/n and v=U[f]. After division by n^2, the residual has leading term n^2 v.grad f, with tested lower terms O(n). For a compactly supported test equal to y on supp f,

    int test v.grad f = -int f v2 = ||v||_2^2>0.

Integration by parts uses div v=0. The last equality follows from the real Fourier multiplier v2=-xi1^2/|xi|^2 fhat and |vhat|^2=xi1^2/|xi|^2|fhat|^2. Strict positivity follows because a nonzero compactly supported f cannot be independent of x. Hence the full transport equation fails for sufficiently large n. This verifies only the advertised failure of an upper bound from structural assumptions alone.

## 3. The ell=1, zero-slope rigidity statement

Let rho,U be smooth solutions of

    (X+U).grad rho=rho,   div U=0,   curl U=-rho_x,

with the parities, bounded first derivatives, DU(0)=0, grad rho(0)=0, and the EXTRA cap sigma=s<1. Strictly sublinear growth is not needed here. Then rho=U=0.

Parity gives rho(0)=U(0)=0. The fundamental theorem of calculus along radial segments gives X.U>=-s r^2. W=X+U is globally Lipschitz and its trajectories are complete. Along a backward trajectory,

    |Phi_t X| <= exp((1-s)t)|X|,            t<=0.              (7)

If rho had a first nonzero Taylor term rho_j of degree j>=2, DU(0)=0 and U(0)=0 would make the degree-j equation j rho_j=rho_j, a contradiction. All jets vanish, so rho is flat. For any integer N with N(1-s)>1, transport and (7) give for sufficiently negative t

    exp(t)|rho(X)|=|rho(Phi_t X)|
                       <=C_(N,X) exp(N(1-s)t).

Letting t->-infinity yields rho(X)=0 for every X. The Lipschitz harmonic ambiguity just proved then gives U=b(x,-y), and DU(0)=0 gives b=0.

This result applies to a smooth limiting field only if the compactness argument preserves smoothness, the zero origin derivatives and a nonzero field. A bounded first-derivative sequence does not automatically provide any of those conclusions.

## 4. A uniformly controlled all-radius slow representation is impossible

For 0<D<=1/2 let s=D log(r/L). Assume an exact smooth canonical profile has the EXTRA representation and uniform bounds

    rho/r = D h(s)sin theta + D^2 sum_(j>=3 odd) H_j(s)sin(jtheta),
    ||h||_(C_b^3) + ||H_3||_L1
       +sum_(j>=3 odd)(1+j)^4 ||H_j||_(C_b^3) <= M,           (8)

with the same M along the family. These are all-radius assumptions, not an expansion on a finite annulus. They imply ||grad rho||_inf+||DU||_inf<=C M D, with a universal C, and therefore cannot hold for exact profiles with D->0.

Directly differentiating (8) bounds grad rho: a radial derivative is r^-1 D partial_s on a function of s, and an angular derivative is r^-1 partial_theta. The factor r in rho leaves terms controlled by D||h||_(C1) and D^2 sum(1+j)||H_j||_(C1), which are O(MD).

To control the inverse, write the second stream mode as D r^2 g(s)sin2theta. Differentiating the density modes in x and using the canonical endpoint at infinity gives the exact scalar equation

    D g'+4g=B(s),
    B=-h/2-D H_3/2+2 int_s^infinity H_3(t)dt.                (9)

For each fixed D the individual symbol bounds give the endpoint values used in that integration. The L1 term in (8) makes B bounded uniformly. Its first two derivatives are bounded by C M. The bounded solution at the origin is

    g(s)=int_0^infinity exp(-4t)B(s-Dt)dt.                   (10)

The alternative homogeneous coefficient exp(-4s/D) produces a singular r^-2 stream term and is excluded by smoothness at zero. Differentiation under (10) gives ||g||_(C_b^2)<=C M. The leading mode's velocity gradient is therefore O(MD); radial derivatives of g introduce only extra factors D.

For each even n>=4, if P_n(s) is the coefficient of r^2 sin(n theta) in the stream, the equation is

    [n^2-(D partial_s+2)^2]P_n = forcing_n.

The forcing is D^2 times neighboring H_(n-1),H_(n+1) and their first derivatives, with coefficients bounded by C(n+2). The two first-order factors have bounded half-line convolution inverses with respective L1 norms 1/(n-2) and 1/(n+2). Thus the full inverse has norm at most 1/(n^2-4), and commutes with s derivatives through order two. Its velocity gradient is controlled by C(n^2||P_n||+nD||P_n'||+D^2||P_n''||). Summing these bounds is justified by the weighted summability in (8), and gives O(MD^2) for all n>=4. Smoothness at zero and the canonical condition exclude all extra homogeneous modes. Combining this with (10) proves the claimed derivative bound.

Finally |a|<=||grad rho|| and sigma<=||DU||. At m=3, (1) gives

    1+2D <= 3 sigma +(1633/1000)|a| <= C' M D,

a contradiction for sufficiently small D with M fixed. At least one all-radius representation or uniform bound in (8) must fail in any exact small-D family. This proof does not determine where it fails, and does not justify assigning a particular inner-layer scale from sampled data.

## Audit scope

ENDPT(a)-(d) are CONFIRMED with their displayed extra hypotheses. The source's optional smooth structural perturbation in Section3.3 is also checked above. The additional H2 residual asymptotic in its Section5 is not part of this verdict; its H3 limit was independently verified earlier in result53. None of the results here excludes any interval of ell in the unrestricted primary class, or proves realization of the displayed limiting fields by exact profiles. All norm hypotheses used for the exclusions are invariant under the genuine spatial scaling.

## 5. Explicit constant for the slow representation, audited 2026-10-20

The universal constant in Section4 can be taken strictly smaller than11, with G_U measured in Frobenius norm. This independently checks the explicit constant added to the lead's A.3.49(d).

Write t=log r and rho=sum_j r a_j(t)sin(j theta), with a_1=D h and a_j=D^2 H_j for odd j>=3. The arguments of h,H_j are s=D(t-log L). By the triangle inequality for the radial and angular derivative,

    G_rho <= (2D+D^2)||h|| + sum_(j>=3)[(1+j)D^2+D^3]||H_j||
           <= (5/2)DM,                                      (9)

because D<=1/2 and (1+j)>=4. Here every C_b^3 norm bounds each derivative of order at most3 individually.

If psi_n=r^2 p_n(t) sin(N theta), N=2n, the Hessian in the orthonormal polar frame has diagonal entries (2p_n+3p_n'+p_n'')sin(N theta) and ((2-N^2)p_n+p_n')sin(N theta), and off-diagonal entry N(p_n+p_n')cos(N theta). The Frobenius triangle inequality and sqrt2<=2 give

    ||D^2 psi_n||_inf <= (N^2+2N)||p_n||
                              +(2N+4)||p_n'||+||p_n''||.      (10)

The source coefficient is F_n=[(2-2n)a_(2n-1)+a'_(2n-1)+(2n+2)a_(2n+1)+a'_(2n+1)]/2. At n1 set Q(t)=int_t^infinity F_1(tau)dtau. The decay h,H3 ->0 at positive infinity follows from the given sublinear density bound; ||H3||_L1 is a hypothesis. Thus

    Q(t)=D[-h(s)/2-D H3(s)/2+2 int_s^infinity H3(v)dv]=D B(s).

The canonical Green formula and integration by parts give p_1(t)=int_0^infinity exp(-4u)Q(t-u)du. Its lower endpoint contributes zero because Q is bounded. The stated norm bound in(8) implies ||B^(k)||_inf<=2M for k0,1,2, by direct differentiation. Therefore ||p_1^(k)||_inf<=D^(k+1)M/2. Inserting N2 into(10) bounds its contribution by

    M(8D+8D^2+D^3)/2 <= (49/8)DM.                            (11)

For N=2n>=4 the logarithmic Green kernel has L1 norm1/(N^2-4). Each of ||F_n||,||F_n'||,||F_n''|| is at most D^2(n+3/2)(||H_(2n-1)||+||H_(2n+1)||), using D<=1/2 and C_b^3 control. Equation(10) then gives the coefficient (N^2+4N+5)/(N^2-4). The exact polynomial factorization

    37(N^2-4)-12(N^2+4N+5)=(N-4)(25N+52)>=0

bounds this coefficient by37/12 on the entire infinite range N>=4. Each H_j occurs at most twice, with summed factors at most j+3<=3(1+j)/2. Consequently the sum of all N>=4 contributions is at most

    (37/8)D^2 sum_j(1+j)||H_j|| <= (37/16)DM.                  (12)

Uniform summability of these Hessian bounds justifies differentiation of the stream series. Combining(9),(11),(12), and |DU|_F=|D^2 psi|_F, proves

    G_rho+G_U <= (175/16)DM <11DM.

The independently proved general gradient gap G_rho+G_U >=sqrt2(2ell-1)/3 is strictly larger than47/100. Since47/1100>1/24, one obtains D>1/(24M). Thus the stated representation with a fixed M excludes 0<D<min(1/2,1/(24M)). The hypotheses of this representation have not been proved for all exact profiles. These constants do not make the exclusion unconditional.
