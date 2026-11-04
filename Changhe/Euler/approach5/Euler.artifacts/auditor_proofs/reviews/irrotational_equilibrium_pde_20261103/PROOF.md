# Irrotational carrier equilibria: exact regularity and local rate restrictions

Status: independently CONFIRMED at A563-A566 after complete source and proof postreads and exact coefficient checks. No general C2 separating-germ exclusion or local Euler construction is asserted.

## 1. Setting and local level geometry

Let 0<c<1/2, a=1-2c, kappa=1+c, d=3c, D0=1+4c and omega be finite. Use a full global C2 velocity/C1 pressure profile with div U=0, U.curl U=0, U=o(|y|), B=(cI-omega J)y+U. At a carrier equilibrium p in the closure of {W!=0}, assume B(p)=W(p)=0 and u=U(p)!=0. Put M=DU(p), F=DB(p), K=DW(p). The confirmed identities give

    M=M transpose, tr M=0,
    grad H(p)=-a u, Hess H(p)=-a M,
    grad g(p)=F transpose u=rho u.

Every use of a global input below can instead be replaced by its explicit local identity or inequality as a hypothesis. In particular F1 is dg wedge dH=0 on {W!=0}; the zero-g inequality lambda>=1 is A521, not a purely local Euler theorem.

If K!=0, one component of W has nonzero differential on a small box. Its zero set is a C1 surface, and {W=0} is contained in that surface. Thus {W!=0} is dense in the box. F1 extends by continuity. H is a C2 submersion, so connected H-coordinate fibers give

    g=G(H), G in C2, G(H(p))=0, G'(H(p))=-rho/a.

Let S be the small regular level H=H(p). Then g=0 on all S and B,W are tangent to S. If W is zero on S, shrink the box so S is exactly the scalar-component zero surface; then {W=0}=S. The normal-form scalar G is only local, not globally single-valued.

On S, write N=grad H. The exact identities give

    B cross W=f N, aU=(f-1)N,
    Bf=mu f, Wf=0, mu=-a-rho.                     (1)

These extend across W=0 within this box. They follow from the full identities and G, or from A536 on the dense vortical part followed by continuity. The regularity of f is at least that supplied by B,W,N. For U in Ck, H,S are Ck and W restricted to S is C^(k-1).

## 2. Flat K: pointwise derivatives and conditional quadratic support

Suppose K=0. The C1 tensor dg wedge dH vanishes together with its first derivative at p: approach p through the open vortical set, where both vanish. Differentiating once and using the displayed gradients yields

    Hess g(p)=rho M+tau u u transpose.

Since Delta U(p)=-curl W(p)=0, tracing direct derivatives of g=U.B gives

    tau |u|^2=2|M|_F^2.                            (2)

With n=u/|u|, F transpose u=rho u gives M n=(rho-c)n-omega Jn. Split the symmetric matrix into n and n-perp. Its normal entry is rho-c, the off-diagonal vector is -omega Jn, and the tangential block has trace -(rho-c). Minimizing the squared norm of that block gives

    2|M|_F^2>=3(rho-c)^2+4omega^2|Jn|^2.            (3)

Neither (2) nor (3) by itself restricts the sign of rho.

Add explicitly W(p+X)=Q(X,X)/2+o(|X|^2), where Q is a symmetric vector-valued bilinear map. Finite-time Cauchy transport and the derivative of the flow at p give

    Q(exp(tF)X,exp(tF)Y)=exp(-kappa t)exp(tF)Q(X,Y),
    FQ(X,Y)-Q(FX,Y)-Q(X,FY)=kappa Q(X,Y).           (4)

Helicity gives u.Q=0. Scaling div W=0 in distributions gives sum_i Q_i(e_i,Y)=0, without differentiating a Peano remainder. For real diagonalizable F, choose a transverse rho eigenvector and tangent eigenvectors of eigenvalues s,t, s+t=d-rho. Each nonzero coefficient obeys

    output eigenvalue = input1+input2+kappa.        (5)

Normal-squared terms require tangent eigenvalue 2rho+kappa and spectrum {rho,2rho+kappa,-a-3rho}. A normal-times-tangent coefficient L has tr L=0 and [T,L]=(rho+kappa)L. If rho!=-kappa its two tangent exponents are {-a/2-rho,D0/2}; if rho=-kappa a traceless commuting L is possible with no further spectral condition. A pure tangent divergence-free quadratic is the rotated gradient of a cubic. The monomial x_s^i x_t^(3-i) requires (i-1)s+(2-i)t=-kappa. For i=0,3 this gives {q,2q+kappa}, q=(-a-rho)/3; for i=1,2 it gives {-kappa,D0-rho}. These alternatives can overlap. Use (4), not this list, for Jordan blocks or nonreal spectra.

If W is C2 on a neighborhood and Q!=0, some continuous second partial derivative stays nonzero nearby. An open zero set of W there is impossible, so the vortical set is dense and the local G argument applies. A nonzero purely tangential quadratic forces actual vortical points on S; A521 then gives rho<=-a. In the full target natural-decay class A536 sharpens this to rho=-a or rho<=-2(1-c). Under U in C2 alone no quadratic W expansion, neighborhood density or indiscriminate application of A521 on S is supplied. Different vortical level components accumulating at p need not each have g=0 unless the local G argument is justified.

## 3. Family I in the lower range, and the differentiability threshold

Now assume K!=0, 2/5<c<1/2 and rho<=-2(1-c). The two first-jet spectral alternatives are confirmed A469. In family I,

    s=rho+kappa, t=-a-2rho>0, mu=-a-rho>=1.

A nonzero tangent K arrow would require t-s=+/-kappa, giving rho=-1 or rho=-a/3. Neither is in this lower range, so K kills T_pS and W|S=o(|X|). The tangent dynamics is a source if rho>-kappa, has a zero exponent at rho=-kappa, and is a saddle if rho<-kappa. In particular family I is not always hyperbolic.

In the source case every sufficiently near point of S converges backward to p, stays in the box, and obeys |Phi_(-t)q-p|<=C_q exp(-(s-epsilon)t), for any fixed small epsilon>0. This follows by diagonalizing its two positive distinct tangent exponents and applying the usual differential inequality in an adapted norm.

If U is C3, then W|S=O(|X|^2) and f=O(|X|^3), since K kills the tangent plane, S is C2 and B=O(|X|). Comparing this bound with f(Phi_(-t)q)=exp(-mu t)f(q) gives f(q)=0 whenever mu<3s. For such a point W=bB because B cross W=0. Cauchy and the push-forward law of B give W(Phi_(-t)q)=b exp(kappa t)B(Phi_(-t)q). Since |B| is comparable to distance in this source box but W=o(distance), b must be0. Hence W=0 on a whole neighborhood of p in S, excluding the nearby-vortical-level case there.

The strict inequality is rho>-1-c/4. Its intersection with the lower range is

    -1-c/4<rho<=-2(1-c),                           (6)

which is nonempty exactly when c>4/9. At equality, x_s^2 e_t has the correct exponent, and the cubic f rate is mu=3s. No equality exclusion is obtained.

If U is smooth and a first nonzero W Taylor term on S has degree m>=2, tangent output e_s is impossible because every input exponent is positive and kappa>0. Output e_t cannot contain an x_t input for the same reason. Thus the only possible term is C x_s^m e_t and

    t-kappa=m s,
    rho=-1-(m-1)c/(m+2), m>=2.                     (7)

If all tangent jets vanish, uniform polynomial bounds of arbitrary order on the small surface, backward source convergence and the Cauchy conorm estimate force W=0 on its source neighborhood. Explicitly, if ||DB||<=L along the orbit, |W(Phi_(-t)q)|>=exp(-(kappa+L)t)|W(q)|, while flatness gives C_N exp(-N(s-epsilon)t); choose N(s-epsilon)>kappa+L. Consequently smooth nearby-vortical-level cases in the source interval can occur only at (7). This is a necessary resonance, not a solution or nonlinear solvability claim.

The quadratic tangent resonances in the entire lower family-I range are rho=-1-c/4 and rho=-2kappa. At the latter, the possible divergence-free polynomial C(x_s^2 e_s-2x_s x_t e_t) has cubic cross-product exponent 2s+t=mu. For rho<-kappa only the local unstable curve is controlled by backward convergence; W is zero on that curve by the same f and parallel-vector comparison, but other orbits leave the box. The zero exponent rho=-kappa requires a different argument.

## 4. Family II and what rate agreement actually means

In family II the tangent exponents are s=mu/2>0 and t=s+kappa. The only possible nonzero K arrow in this lower range sends e_s to a nonzero multiple of e_t. The leading terms near a slow direction have B of order x_s, W of order x_s e_t and B cross W of order x_s^2. Thus f has order2 with rate 2s=mu, exactly consistent with Cauchy transport. This is a coefficient/rate consistency assertion, not existence of a profile realizing those coefficients.

On the strong fast curve, f=O(distance^2) and mu<2t force f=0. The leading K kills e_t, hence W=o(distance) there, and the parallel-vector Cauchy comparison forces W=0 on that curve. It does not remove nearby slow directions.

If further derivatives exist, the degree-two coefficient equation is forced:

    DR2(TX)-T R2+kappa R2=DC2(LX)-L C2,

where B|S=TX+C2+..., W|S=LX+R2+.... Matching exponents neither solves the resonant equations nor validates their compatibility. The same warning applies to family-I surviving terms.

## 5. A separating first-integral model does not solve the curl equation

For omega0, define on ordinary coordinates

    B0=(rho x,(rho+kappa)y,(-a-2rho)z), W0=k x e_y,
    psi0=z |x|^(2+a/rho), f0=(k rho/a)|x|^(-a/rho).

For rho>=a/2 or rho<=-2a, psi0 is C1 across x0, constant on that plane and nonconstant elsewhere. On either half box B0 psi0=W0 psi0=0 and

    f0 dpsi0=(k/a)[(2rho+a)xz dx+rho x^2 dz]
              =(B0 cross W0)^flat/a.

The product is smooth even if f0 diverges. The bracket is -kappa W0, div B0=3c and div W0=0, and there are no closed W0 lines. However curl(B0-Ay) is not W0, so this is only a reduced-identity model. It refutes the proposed inference from a singular factor to failure of the first integral, not the Euler conjecture.

## 6. Generic cubic compatibility jets, with the actual curl equation

This construction uses omega0, 0<c<1/2 and a real r with r t (3r+2-c)(4r+3)!=0, where s=r+kappa and t=-a-2r. Take carrier p=-e_x/c, u=e_x and coordinates X=y-p. Let F=diag(r,s,t), M=F-cI, m_i=M_ii and k!=0. Define

    n2=(r-2s)m2, n3=(r-2t)m3, n1=-n2-n3,
    b=-k(r+a)(2r+a)/(4a(3r+2-c)),
    U2=((n1 x^2+n2 y^2+n3 z^2)/2,
        n2 xy+b yz, -k x^2/2+n3 xz+b(y^2-z^2)/2),
    W1=k x e_y,
    W2=(-k m2 xy,
        k[(n2-n1/2)x^2/r+b xz/t+m2 y^2/2+m3 z^2/2],
        k b xy/(2s-t)).                            (11)

Since 2s-t=4r+3, the displayed denominators are nonzero. Direct differentiation and the generic rational coefficient check give

    div U2=0, curl U2=W1, div W2=0,
    DW2(FX)-F W2+kappa W2=DU2 W1-DW1 U2,
    e_x.W2+(MX).W1=0.                              (12)

Set H1=-ax, H2=-a X.MX/2, H3=X.(-aU2+FX cross W1)/3 and gamma2=sum m_i^2/a^2. For an undetermined gamma3 put

    N3=-(r/a)H3+2gamma2 H1H2+gamma3 H1^3
                          -(MX).U2-U2.(FX).        (13)

The y coefficient of Delta N3+(curl W2)_x is zero. Its z coefficient is -4(3r+2-c)b-k(r+a)(2r+a)/a, which vanishes. Its x coefficient has nonzero gamma3 coefficient -6a^3. Thus a unique gamma3 makes this polynomial zero. These rational identities were checked symbolically for general c,r,k, not inferred from sampled parameter values.

Define (U3)_x=N3 and

    (U3)_y=integral_0^x [partial_y N3+(W2)_z](xi,y,z)dxi+T_y,
    (U3)_z=integral_0^x [partial_z N3-(W2)_y](xi,y,z)dxi+T_z,

where T is a quartic polynomial satisfying Delta_(y,z)T=-partial_x N3(0,y,z). Integrating the three quadratic monomials supplies such T, with the two harmonic quartic freedoms available. The x and y curl relations follow by differentiation; the remaining one follows from div W2=0 and (W2)_x at x0 being zero. The derivative in x of div U3 vanishes by(13), and its value at x0 vanishes by the equation for T. Hence curl U3=W2 and div U3=0.

For Ujet=e_x+MX+U2+U3, Bjet=FX+U2+U3 and Wjet=W1+W2, (12) makes the vector -aUjet+Bjet cross Wjet curl-free through degree3. Its homogeneous radial primitive gives Hjet=H1+H2+H3+H4. Then

    grad Hjet+aUjet-Bjet cross Wjet=O(|X|^4),
    div Ujet=0 exactly,
    Ujet.Wjet=O(|X|^3),
    gjet-[-(r/a)Hjet+gamma2 Hjet^2+gamma3 Hjet^3]=O(|X|^4). (14)

Define Pjet=Hjet-|Ujet|^2/2-(Ay).Ujet. The first line is exactly the profile residual through degree3. The third line is helicity only through degree2, and the final line gives rank residual O(|X|^3). On the formal surface Hjet0, x=-(m2 y^2+m3 z^2)/2+O(|(y,z)|^3), and W1+W2 cancels through degree2 by(11). It need not vanish exactly on that surface. The exact checks also reconstructed all of(14) at c9/20,r=1/10,-3/10,-1 with symbolic k. These are finite jets, not Euler germs.

## 7. An analytic exact-zero-set realization, still with finite momentum residual

Specialize r=-1, so s=c, t=1+2c. For any0<c<1/2 and k!=0 put

    chi=-k z/a^3+k^2 x^2/[2a^3(2c+3)]
        -k kappa(4c^2+2c-1)xz/a^3
        -c k^2[(1+2c)y^2+z^2]/[4a^4 kappa].        (15)

Choose analytic q(H)=1+q1 H+q2 H^2 with q1=-2kappa^2. Since gamma2=2kappa^2/a^2, choose q2=(a+1)q1^2/(2a)-a^2 gamma3/2. Then

    Hq/(a q+H q')=H/a+gamma2 H^2+gamma3 H^3+O(H^4).

For an unknown analytic H define

    U=-grad H/a+q(H)[(2-a)H chi grad H+H^2 grad chi]. (16)

The exact generic-c check in check_analytic_geometry.py (accompanying artifacts) verifies all twelve coefficients through degree3 of

    q(H)[(2-a)H chi grad H+H^2 grad chi]
        -[FX cross W1+FX cross W2+U2 cross W1]/a

are zero, using H=H1+H2 where those coefficients suffice. Thus (16) agrees with the cubic jet of Section6 whenever H agrees through degree4 with Hjet. This agreement is independent of its harmonic quartic freedom because the displayed beta depends only on B1,B2,W1,W2.

The analytic equation div U=0 is noncharacteristic for x at the origin: its coefficient of H_xx is -1/a because H0=chi0=0. Prescribe analytic H and H_x on x0 matching the chosen Hjet restrictions through degree4. The classical analytic Cauchy-Kowalevski theorem gives a local analytic solution. Its recursion fixes the same full degree4 jet, since substitution of Hjet already satisfies div U through degree2 by Section6. This invokes that standard local analytic PDE theorem, not an elliptic boundary-value existence statement for arbitrary smooth data.

Exterior differentiation of(16) gives exactly

    W=H[a q(H)+H q'(H)] grad H cross grad chi.        (17)

At0, grad H=-a e_x and grad chi=-k e_z/a^3. The bracket and cross product are nonzero on a small box. Consequently {W=0}={H=0} exactly, div U=0 exactly and U.W=0 exactly. With P=H-|U|^2/2-(Ay).U the momentum and rank residuals still have only the finite orders in(14). This analytic field does not solve the profile equation or full rank exactly. It realizes the geometric zero set and the checked cubic jet only.

## 8. Unrestricted coefficient obstructions at additional regularity

The exceptional nonextension claims concern the separating case with K!=0 and the local rank equation g=G(H). At omega0, symmetry of M and separation allow an orthonormal frame with u along e_x and K=k x e_y. Positive amplitude rescaling U_lambda(y)=lambda U(y/lambda), P_lambda=lambda^2 P(y/lambda) normalizes |u|=1 while preserving F and rescaling the nonzero k. It preserves the profile equation and rank. Thus the frame and amplitude in Section6 lose no such first jet.

The independent script constructs every vector homogeneous polynomial U_n with all3(n+1)(n+2)/2 coefficients. At each n it imposes div U_n0, the degree n relation g=G(H), the degree n-1 helicity equation and the degree n-1 bracket equation. At n2 it instead prescribes the complete W1=k x e_y. The degree n part of H is the radial primitive of the already determined lower-degree force, which is integrable by the previous bracket equations. All free coefficients from preceding stages stay among the next unknowns; no selected cubic representative is substituted prematurely.

For U in C3 these equations through n3 are necessary by Taylor expansion. The gradient terms multiplying B=O(|X|) have remainders of the correct order; no derivative of an unqualified Peano remainder is taken. For U in C4 the n4 equations are necessary in the same way. At each inconsistent stage the script stores the exact coefficient equations, unknowns, rational weights and weighted nonzero right-hand side. Multiplying these weights by the entire unknown coefficient matrix gives exactly zero.

At r=(c-2)/3, n3 yields

    -k(4c+1)(5c-1)(7c+4)/[54(2c-1)]=0.             (18)

At r=-3/4, n3 yields

    -k^2(8c-1)/[8(2c-1)]=0.                        (19)

For2/5<c<1/2 and k!=0 both are impossible: their denominators are nonzero and all displayed c-factors in the numerators are strictly positive. Thus these separating first jets cannot extend to C3 profiles with rank, at omega0.

At c9/20,r=-1, n4 yields

    3819(58590000 k^2+44752133)/841000000=0,          (20)

impossible for every real k. Two arbitrary harmonic freedoms remained after n3, and both were retained among the48 unknowns at n4. This rules out a C4 profile with that separating first jet and rank. One independently generated positive certificate suffices; no claim relies on the second coefficient relation in the source. These restrictions do not rule out C2 profiles or justify extrapolating a jet to an exact solution.

## 9. Verification, sources and limitations

The full actual coordinator CO30 check, external referee (a second model), standalone referee proof and question were read. The outer configured-model coordinator reviewed the dynamic argument and quadratic formulas. Its inner model credential failure is explicitly reported and is not counted as a successful consultation. The completed local checks ran on the assigned core55 at nice19 with OMP1 and a2GB memory cap: the generic construction and three unrestricted systems from2026-11-03T08:07:28.337654+00:00 to08:08:25.980375+00:00, elapsed57.64273012895137 seconds; the analytic-geometry coefficients from08:09:46.121091+00:00 to08:09:58.890045+00:00, elapsed recorded in its JSON. All exact checks passed. No numerical approximation was used.

 General C2 separating and flat cases remain open. The arbitrary-omega conclusions are the tensor and dynamic results; the explicit jets and nonextension certificates use omega0. The original question's conditional CO27 warning is superseded only by the exact already confirmed A536 scope, not by a blanket assumption of full global coverage.
