# Audit of the sharp global negative spherical-source coefficient

## 1. Exact statement and status

This reconstruction audits LIT397, captured as in the team records, SHA256 c79dfa89498691210323cc5bdc85abcb6449e4f53a320feb6db5b57724012588. It concerns a kinematic inequality, not an unconditional Euler nonexistence theorem. The independent comparison with the existing C agent is recorded in Section 8. The finite algebra verification is exact integer arithmetic; no sampled eigenvalue is a premise.

Let U belong to C1(R3;R3), be real and divergence free, and suppose

    E(R) = integral_(|y|<R) |U|^2,     E(R)/(L R^beta) -> 1,
    L > 0,     0 < beta < 1.

Set

    t=(beta-3)/2, k=(beta+1)/2, m=2-beta, D=k^2+2,
    H=t^2(k^2+4)/D, C_s=mt^2/D, x_1=k^2/D.

For a fixed center a, r_a=|y-a|, define

    F_a(R)=integral_(1<r_a<R) r_a^-beta |U|^2,
    G_a(R)=integral_(1<r_a<R) r_a^(2-beta)|DU|_F^2,
    Q_a(r)=integral_S2 tr((DU(a+rn))^2) dn,
    K_a^-(R)=integral_1^R r^(4-beta)[-Q_a(r)]_+ dr,
    J_a(R)=integral_1^R r^(4-beta)[Q_a(r)]_+ dr.

The measure dn has total area 4pi. The negative part is after the sphere integral. Assume additionally

    M=limsup G_0(R)/(beta L log R) < infinity.

Then the same M occurs at every fixed center, M>=H, and, with delta=M-H and u(M)=min(1,x_1+delta/(2beta)),

    limsup K_a^-/(beta L log R) <= delta/m,                    (1)
    limsup J_a/(beta L log R)
       <= min(M, m[1-beta+beta u(M)]+delta/m)
       <= min(M, C_s+(m/2+1/m)delta).                         (2)

The least constant C such that the right side of (1) can be replaced by C delta for every field in this class is 1/m at each beta. The least constant that works for all beta in (0,1) is 1. This statement does not give the best coefficient in (2), the best nonlinear function at fixed delta, or an optimal constant among actual Euler profiles.

## 2. Modal identities and regularity

The audited dependencies are A3186 and A3215-A3216 for the modal formulas and Hardy defect, A3153 for the tangential bound, A3203-A3204 for the oscillatory sharpness family, and A3053 for the conditional Euler application. The relevant modal identities are restated here so that the new implication is checkable.

At center zero put z=log r and U(rn)=r^t v(z,n). Solenoidality becomes

    (partial_z+k)(v.n)+div_S v_T=0.

The degree-zero radial harmonic vanishes: flux across each sphere is zero by the divergence theorem on its ball, and U is regular at the center. In an orthonormal real spherical harmonic basis, each degree ell>=1 has lambda=ell(ell+1), and its poloidal and toroidal fields are

    fY n + (f'+kf)grad_S Y/lambda,
    h n cross grad_S Y.

Write p=f' and w=f''. The solenoidal relation and C1 regularity imply f is C2; h is C1. Modal velocity energies are K_pol=f^2+(p+kf)^2/lambda and K_tor=lambda h^2. Define

    b_lambda=2+(k^2+t^2-H)/lambda,
    d_lambda=(t^2-H)(1+k^2/lambda)+lambda+t^2-2,
    Z_pol=w^2/lambda+b_lambda p^2+d_lambda f^2,
    Z_tor=lambda[h'^2+(t^2+lambda-H)h^2].

They are nonnegative: b_lambda>=1, d_2=0, d_lambda>=4lambda/9 for lambda>=6, and t^2+lambda-H>0. At lambda=2,

    b_2=D/2+2beta/D,     b_2-t^2/2=beta+2beta/D>0.

For a smooth compactly supported nonnegative eta(z), the summed identity is

    integral eta Z = G_eta-HF_eta
                  +O_beta(integral (|eta'|+|eta''|)|v|^2).    (3)

Here F_eta=integral eta|v|^2 and G_eta is its critical gradient counterpart. The exact poloidal integration-by-parts errors are

    -(k+t)/lambda integral eta' p^2
    -[2t+((k+t)tk-Hk)/lambda] integral eta' f^2
    +tk/lambda integral eta'' f^2;

the toroidal error is -t lambda integral eta' h^2. In particular

    p^2/lambda <= 2(p+kf)^2/lambda + 2k^2 f^2/lambda          (4)

bounds the errors by velocity energy, with constants independent of ell. No gradient trace on cutoff spheres is assumed.

The sphere-integrated source Qflat(z)=r^(5-beta)Q_0(r) is the sum of

    Q_pol=s_lambda f^2+A_lambda fp+B_lambda fw
                         +C_lambda p^2-2pw/lambda,
    Q_tor=m lambda h^2-2lambda hh',
    s_lambda=m(1-beta+k^2/lambda),
    A_lambda=8k-10+6k(1-k)/lambda,
    B_lambda=2(1-k/lambda), C_lambda=2+(3-4k)/lambda.         (5)

These identities hold first for finite angular sums. Such sums converge in the velocity and Cartesian-gradient L2 spaces on compact annuli by the vector harmonic Parseval decomposition. Thus their sources converge in L1 there, since

    |tr(M_1^2)-tr(M_2^2)|
       <= |M_1-M_2|_F (|M_1|_F+|M_2|_F).

This passage concerns the sphere integral of the quadratic source, not a termwise pointwise identity on the sphere.

## 3. Nonnegative corrected defect

For poloidal modes define

    R_pol=Z_pol/m+a_lambda fp+bhat_lambda pw
                                      +dhat_lambda(fw+p^2).

For lambda=2 use a_2=dhat_2=0 and bhat_2=t/m. For every lambda>=6 use

    a_lambda=1/2,
    bhat_lambda=-(lambda+1)/(2lambda^2),
    dhat_lambda=-1+1/lambda+1/(2lambda^2).                    (6)

Set R_tor=Z_tor/m. The required two inequalities are R_mode>=0 and Q_mode+R_mode>=0. At degree one they follow from the exact identities

    Q_pol=(mt^2/2)[f+((5-3k)p-w)/(mt)]^2-(tp+w)^2/(2m),
    R_pol=(tp+w)^2/(2m)+(b_2-t^2/2)p^2/m.

For toroidal modes the second inequality follows from

    Q_tor+R_tor=m lambda(h-h'/m)^2
                           +(lambda/m)(t^2+lambda-H)h^2.

These calculations use t!=0 and m>0, both automatic here. Higher degrees are settled by the finite certificate in Section 4. It follows that for every finite partial sum

    [-Qflat_partial]_+ <= sum R_modes.                      (7)

There is no assertion that R_pol is a fixed multiple of Z_pol at an individual jet. The extra terms in (6) matter before radial integration.

## 4. Independent exact verification in the higher degrees

In coordinates (f,p,w), form the symmetric matrices of Q_pol and R_pol from (5)-(6). Write B=beta, l=lambda, V=B^2+2B+9, k0=(B+1)^2, t0=(B-3)^2 and S=8(2-B)l^2V. The positive scalar S clears denominators. My independently constructed scaled R has entries

    R00=2l[-8lt0-2t0k0+4l^2V+lVt0-8lV],
    R11=2l(8lV+k0V-8t0)+4(2-B)V(-2l^2+2l+1),
    R22=8lV, R01=2(2-B)l^2V,
    R02=2(2-B)V(-2l^2+2l+1), R12=-2(2-B)V(l+1).

My scaled Q has entries

    Q00=2(2-B)^2lV[4l(1-B)+k0],
    Q01=4(2-B)l^2V(4B-6)+6(2-B)lV(1-B^2),
    Q02=4(2-B)lV(2l-B-1),
    Q11=8(2-B)lV(2l+1-2B), Q12=-8(2-B)lV, Q22=0.

Symmetry gives the remaining entries. Direct substitution gives these formulas; in particular t^2-H=-2t0/V. The independent program `check_integer_certificate.py (accompanying artifacts)` represents a polynomial by its integer coefficients indexed by the powers of B and l. It constructs the matrices above, takes their leading minors by the explicit determinant formulas of orders 1, 2 and 3, and applies the following transformation to each resulting polynomial P:

    T(x,y)=(1+x)^N P(x/(1+x),6+y),     N=degree_B(P).

For a coefficient p_ij of B^i l^j, its contribution to x^a y^b is

    p_ij binom(N-i,a-i) binom(j,b) 6^(j-b).

Binomial coefficients outside their range are zero. This is a finite identity from the binomial theorem. Thus the program uses only arbitrary-precision integer operations, without a symbolic algebra engine, approximate roots or floating point. The complete input and output coefficients are in the team records.

The six independently computed transformed minors have these summaries:

| Matrix | Order | N | Nonzero coefficients | Least nonzero coefficient | Constant |
| --- | ---: | ---: | ---: | ---: | ---: |
| SR | 1 | 4 | 20 | 72 | 10800 |
| SR | 2 | 8 | 52 | 2916 | 264384 |
| SR | 3 | 10 | 73 | 46656 | 3685824 |
| S(Q+R) | 1 | 6 | 28 | 72 | 21600 |
| S(Q+R) | 2 | 9 | 60 | 20736 | 61321536 |
| S(Q+R) | 3 | 12 | 89 | 373248 | 593790912 |

All 322 nonzero coefficients were additionally displayed and read; omitted coefficients are zero. Every row is positive for x,y>=0 because its coefficients are nonnegative and its constant is positive. For 0<=B<1 and l>=6 take x=B/(1-B), y=l-6. Then P=T/(1+x)^N>0. S>0, so each unscaled leading minor is positive. Sylvester's criterion proves R and Q+R positive definite throughout this continuum, and in particular at every integer angular degree ell>=2.

The source uses reduced minors N_j/D_j, with

    D_1=4lmV, D_2=16l^3m^2V^2, D_3=64l^6m^3V^2.

A second independent check verifies, coefficient by coefficient, that each scaled minor times D_j equals S^j N_j, that the complete source binomial transform is correct, and that its degree, all coefficient signs, count, minimum and constant agree. The source's 263 nonzero coefficients refer to these reduced numerators; they are not the 322 unreduced coefficients above. The source JSON SHA256 is 5ce9e0e45ffb4f0a5a60f484e10818fd155511a4fb7462b489c227a9a2d6f881. Each deliberately altered numerator is rejected, as is a negated leading entry. The extended independent run completed at 2026-11-04T11:47:29.873832+00:00 with six positive-minor rows and 61 ancillary checks PASS.

This is an exact finite algebra certificate with the preceding analytic soundness argument. It is not a Lean proof, a numerical Euler simulation or a claim based only on certificate summaries.

## 5. Infinite sums and radial cutoffs

For compactly supported eta, integration of the correction is exact:

    integral eta(R_pol-Z_pol/m)
      =-a_lambda/2 integral eta' f^2
       -bhat_lambda/2 integral eta' p^2
       +dhat_lambda/2 integral eta'' f^2.                    (8)

Indeed fp=(f^2)'/2, pw=(p^2)'/2, fw+p^2=(f^2)''/2. The stated regularity suffices for these integrations. No endpoints survive. At lambda>=6, |a_lambda|<=1/2, |dhat_lambda|<=1 and lambda|bhat_lambda|<=7/12. The degree-one value lambda|bhat_2|=2|t|/m is finite. Equation (4) therefore bounds the summed error by C_beta integral(|eta'|+|eta''|)|v|^2.

Each R_mode is nonnegative. For a nonnegative eta, (3) and (8) bound the partial sums of their eta integrals uniformly by the finite local velocity and gradient energies and the displayed error. Monotone convergence gives a locally integrable R_total. The L1 source convergence in Section 2 admits an almost-everywhere convergent subsequence in z. Equation (7) then gives [-Qflat]_+<=R_total almost everywhere. Parseval convergence of both energy integrals and the absolutely bounded correction errors yields

    integral eta R_total=(G_eta-HF_eta)/m
                 +O_beta(integral(|eta'|+|eta''|)|v|^2).     (9)

Consequently no finite angular truncation or weighted angular trace premise remains.

Integration by parts in the Stieltjes integral F_0(R)=integral_1^R r^-beta dE(r) gives

    F_0(R)=beta L log R+o(log R).

The energy ratio also bounds each fixed-width distant logarithmic strip's velocity integral uniformly: on R<r<cR, r^-beta<=R^-beta and E(cR)=O(R^beta). Choose 0<=eta_R<=1 equal to one on [0,log R], supported in (-log 2,log(2R)), with two uniformly bounded derivatives. The inner strip has fixed finite energies. The derivative errors of (9) are O(1). Since H>0, G_eta<=G_0(2R)+O(1) and F_eta>=F_0(R). Thus

    K_0^-(R)<=[G_0(2R)-HF_0(R)]/m+O(1).                    (10)

The outer gradient strip is retained in G_0(2R). We never replace it by O(1). Divide by beta L log R and use log(2R)/log R->1 to prove (1). Applying the same procedure to the nonnegative Z in (3) gives M>=H. Also |tr(DU^2)|<=|DU|_F^2 implies J_0,K_0^-<=G_0; this proves the elementary M bound.

For J, the signed source identity with the same cutoffs is

    integral eta_R Qflat=m(1-beta)F_eta+m beta T_eta+O(1),

where T_eta is the weighted tangential velocity energy. Explicitly, test the distributional identity q=div div(U tensor U) against psi(r)=r^m eta(log r). Its Hessian is

    D^2 psi=r^-beta[(m eta+eta')I
                  +(-m beta eta+(2m-2)eta'+eta'') n tensor n].

The terms containing eta' or eta'' are bounded by velocity strip energy; the remaining contraction is precisely the displayed signed identity. Thus no source derivative or unbounded gradient trace enters. Moreover T_eta=T_0(R)+O(1) for these cutoffs because the additional strips have bounded velocity energy. A3153 therefore supplies

    limsup T_eta/(beta L log R)<=u(M).

Using [Qflat]_+=Qflat+[-Qflat]_+, (9), the exact limit F_eta/(beta L log R)->1, and (10) proves the first bound in (2). Since u(M)<=x_1+delta/(2beta) and m(1-beta+beta x_1)=C_s, its second bound follows. In particular m/2+1/m<=3/2 for 1<m<2, since (m-1)(m-2)<=0. This last coefficient is an upper bound, not a sharpness assertion.

## 6. Every fixed center

Ball inclusion between radii R-|a| and R+|a| proves E_a(R)/(LR^beta)->1. Outside a sufficiently large fixed ball the ratio of r_a^(2-beta) and |y|^(2-beta) lies between 1-epsilon and 1+epsilon. The domains defining G_a(R) and G_0(R) differ by a fixed inner part and by replacing R with R+O(1). Positive-integrand comparison, division by log R, and log(R+O(1))/log R->1 give both inequalities between the limsups, up to these factors. Let epsilon tend to zero. Thus every center has exactly M, and the proof of Sections 2-5 applies there. This is a translated kinematic estimate, without an assertion that the Euler equation is translation invariant.

## 7. Optimality and Euler scope

A3203-A3204 establish smooth whole-space solenoidal fields with all derivatives decaying, the required energy asymptotic and M=H+delta, whose negative-source coefficient approaches

    F_beta(delta)=(sqrt(C_s^2+4C_s delta/m)-C_s)/2.

Here C_s>0, and rationalization gives F_beta(delta)/delta->1/m as delta decreases to zero. If C<1/m were valid for every field at the fixed beta, choose delta>0 sufficiently small that F_beta(delta)>C delta. A smooth member sufficiently near the family supremum would violate that proposed bound. Hence (1) is sharp. Taking the supremum of 1/(2-beta) over 0<beta<1 gives the uniform sharp value 1. Attainment of the supremum by a single smooth field is neither needed nor claimed.

These sharpness fields are not Euler profiles: their core pressure-free momentum curl is nonzero for every c and omega, as checked in A3203. Their role is exclusively kinematic.

A3053 gives E(R)/(LR^beta)->1 with L>0 and beta=5-2/c for a nonzero bounded C1 velocity and C1 pressure solving the full rotating profile equation, with distributional U(R.)->0 and 2/5<c<1/2. Thus (1)-(2) apply to each such profile for every finite omega if finite M is also assumed. Smooth uniform decay supplies boundedness and that blow-down condition; it does not supply finite M. No axisymmetry, restriction on angular modes, or restriction on the value of omega enters the kinematic proof.

The global linear K coefficient question of A3205/A3217 is thereby settled, conditional on the stated kinematic premises. Automatic finite M, optimal J bounds, a sharp nonlinear envelope at fixed delta, profile-specific sharpness, eventual source sign, pointwise negative parts before sphere integration, and unconditional rotating nonexistence remain open. At delta=0 the conclusion is K_a^-=o(log R), which does not imply eventual nonnegativity of Q_a.

## 8. Comparison and verification boundary

The six source proof sections and all 42 manual obligations have been read. The source verifier was inspected, but the decisive finite arithmetic here is the separately constructed integer program and recorded output. The analytic steps above explicitly resolve regularity, missing radial zero mode, pressure independence of the kinematic result, the infinite angular limit, cutoff boundary terms, all-center transfer, exact sharpness quantifiers and arbitrary-omega scope. No characteristic-flow argument is used by this lemma.

The existing C agent compared both complete proofs at 2026-11-04T11:53:24Z. Its six-item comparison is retained as in the team records, SHA256 0e40151446d80ce89ad5a3aacef9ce77b01303a67eca9b65da029a5d263513a7, and has been read in full. Items 1-2 reproduce the integration-by-parts errors, degree-one square completions and toroidal positivity. Item 3 independently reconstructs all six reduced minors and their binomial transforms, agreeing with the exact certificate. Items 4-5 check the infinite sum, retained outer gradient term, positive-source implication and sharpness quantifiers. Item 6 correctly separates the optimal pointwise modal coefficient from the better global logarithmic coefficient: the latter uses total derivatives, so the two results do not conflict. No substantive disagreement remains.

C explicitly did not inspect the source's 42 manual obligations or source checker; I inspected those separately. Its sampled eigenvalues, reduced-model numerical observation and extra wrong-variant tests are not premises of this proof and are not certified by this audit. The independent integer certificate above and analytic argument suffice. Collaboration is with the existing agent configured as model; its actual provider execution is not independently attested. No new model client or remote computation was used. The conclusion is the exact kinematic bound and sharp K coefficient, with the remaining limits in Section 7.
