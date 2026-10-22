# The cubic axis equation and its finite-part coefficient

Topic59. Independent audit of the lead's pinf_B3 note. This proof precedes executable checks. It gives conditional identities and a smoothness criterion. It does not evaluate the coefficient of an exact profile, exclude a P2 profile, or turn a trial defect into an error bound.

## 1. Hypotheses and the axis equations

Let rho be even in x, odd in y, and let V=c X+U, U=(-psi_y,psi_x), -Delta psi=rho_x, with the canonical inverse and c=(1+psi_xy(0))/3. Write c for c_l in this note. At the normalized center rho=x²y a, a(0)=1. Suppose V is C3 near the segment [0,L] on the x-axis, rho is C3 near the open segment and P=(L,0), and the indicated center expansions hold. Put

    G1=rho_y(x,0), G3=rho_yyy(x,0)/6,
    w=V1(x,0), w2=V1_yy(x,0)/2,
    v1=V2_y(x,0), v3=V2_yyy(x,0)/6.

From div V=2c and curl V=partial_x V2-partial_y V1=-rho_x, comparison of the even and odd transverse coefficients gives

    w'+v1=2c, w2'+3v3=0, 2w2=G1'-w''.                     (1)

For example differentiating the curl once in y gives v1'-2w2=-G1'; differentiating the first divergence identity gives v1'=-w''. These identities hold for a density and its own velocity without requiring the profile equation.

Now assume V.grad rho=rho. The first axis equation is

    w G1'+(v1-1)G1=0.                                      (2)

The cubic equation is valid in distributions in x even when G3 is only continuous:

    w G3'+(3v1-1)G3=f, f=-(w2 G1'+v3 G1).                 (3)

Here is a derivation that does not assume a fourth derivative of rho. The conservative equation is div(V rho)=(2c+1)rho. The C3 Peano expansions are

    V1 rho = wG1 y+(wG3+w2G1)y³+o(y³),
    V2 rho = v1G1 y²+(v1G3+v3G1)y4+o(y4).

On each compact x interval their remainders are uniform. Integrate the conservative equation from zero to y in the transverse coordinate, and test against a compactly supported smooth function of x. Comparing the y² and y4 coefficients gives

    (wG1)'+2v1G1=(2c+1)G1,
    (wG3+w2G1)'+4(v1G3+v3G1)=(2c+1)G3.

Substitution of (1) gives (2),(3). This argument is distributional only for the x derivative of G3. Where w is nonzero, its continuous right side implies that G3 is C1 and obeys (3) classically.

C2,alpha regularity with 0<alpha<1 does not provide G3. The odd one-variable function y|y|^(1+alpha) is C2,alpha but has no finite cubic Peano coefficient. At a point P away from the center, a stronger example is

    F(s,y)=y³ |s|^(-lambda) chi(y/s), s=x-L,
    F(0,y)=0, 0<lambda<1,                                 (4)

where chi is a smooth even function supported in a bounded interval and equal to one near zero. It is smooth away from (0,0), including along s=0 at y nonzero, and homogeneous of degree 3-lambda near (0,0). Derivatives of order k<=2 are bounded by C r^(3-lambda-k). The second derivatives extend by zero and are Hoelder of order 1-lambda: if two points have separation comparable to either radius, use the size bound; otherwise the segment stays at comparable radius and the third derivative bound C r^(-lambda) gives |D²F(X)-D²F(Y)|<=C |X-Y| r^(-lambda)<=C |X-Y|^(1-lambda). Thus (4) is C2,alpha for alpha<=1-lambda, whereas its cubic trace for s nonzero is |s|^-lambda. Cutoffs near P and its reflected point produce the required x parity if desired. These are regularity examples, not PDE solutions.

## 2. Endpoint geometry and the corrected integrating factor

Assume w has simple zeros at 0,L, w<0 on (0,L), and

    w'(0)=-A, A=2c-1>0, D=4c-1=2A+1.

Assume G1/x²->1 at zero. If G1(L) is nonzero, equation (2) gives v1(L)=1. Consequently w'(L)=A. This is the exact constraint w'(L)=-w'(0). The trial's small defect in this equality cannot be set to zero in a certificate.

Parity and C3 give w=-Ax+O(x³), v1=D+O(x²). Define

    p=(3D-1)/A=6+2/A,
    q=(3v1-1)/w=-p/x+O(x),
    E(x)=-integral_0^x (q(t)+p/t) dt,
    H(x)=x^(-p) exp(-E(x))
        =x^(-p) exp(+integral_0^x(q(t)+p/t)dt).             (5)

Then H'/H=q. The sign in the exponent of H in A4 of the lead's revision1 is wrong. For example if q=-p/x+x, the printed expression has H'/H=-p/x-x, whereas (5) gives -p/x+x. Formula (5), rather than the printed negative-integral expression, is required for

    (H G3)'=H f/w.                                         (6)

Near L the exact-profile condition v1(L)=1 gives q=2/[A(x-L)]+O(1), so

    H(x)=C_P(L-x)^(2/A)(1+O(L-x)), C_P>0.                 (7)

If f is continuous at L, H f/w is integrable there because 2/A>0. The unique bounded solution of (3) is

    G3(x)=H(x)^(-1) integral_L^x H(t)f(t)/w(t) dt.           (8)

The difference of two solutions is C/H, which diverges at L unless C=0. For the endpoint value, divide the integral asymptotic by (7). Since w=-A(L-x)+O((L-x)²), its leading term is (C_P f(L)/2)(L-x)^(2/A); hence G3(L)=f(L)/2. This does not require G3' to have a finite limit at P.

The normalized first trace is

    G1=x² exp integral_0^x ((1-v1)/w-2/t)dt.                (9)

Under the stated geometry its exponent is integrable at zero and at L, so G1 has a positive finite value at L. Thus a sufficiently regular w with the endpoint slope constraint reconstructs c,A,p,v1,G1,w2,v3,f by (1),(9), and reconstructs the bounded G3 by (8). It reconstructs axis data only. Such a w need not arise from a full-plane density and its canonical velocity, and the higher-order assumptions in the next section do not follow merely from C3.

## 3. Finite part, remainder and cutoff error

Assume 6<p<8. Define Q=x exp(-E) f/w, so Hf/w=x^(-p-1)Q. Suppose for some r0<=L,

    Q(x)=q2 x²+q4 x4+q6 x6+R(x), |R(x)|<=K x8,
    0<x<=r0.                                               (10)

Also assume the endpoint integrability proved above. Define

    B3=-lim_(delta->0) [integral_delta^L x^(-p-1)Q(x)dx
                       +sum_(j=2,4,6) qj delta^(j-p)/(j-p)].(11)

The limit exists: the displayed subtractions integrate each polynomial term exactly, while x^(-p-1)R is integrable at zero since p<8. Integrating (6) and using (11) gives the exact local expansion

    G3=e^E sum_(j=2,4,6) qj x^j/(j-p)+B3 x^p e^E
           +x^p e^E integral_0^x t^(-p-1)R(t)dt.           (12)

The last term has absolute value at most K e^E x8/(8-p). The dimensionless coefficient used here is beta3=L^(p-2)B3.

For 0<delta<=r0 put

    Phi_delta=-integral_delta^L x^(-p-1)Q(x)dx
                       -sum_(j=2,4,6) qj delta^(j-p)/(j-p).

The exact error is

    B3-Phi_delta=-integral_0^delta x^(-p-1)R(x)dx,
    |B3-Phi_delta|<=K delta^(8-p)/(8-p).                    (13)

This verifies the subtraction signs and identifies the remainder that must be enclosed. Neither a floating polynomial fit nor a small pointwise residual provides K. If p ranges in [p_-,p_+] inside (6,8), delta<=1, then the error is at most K delta^(8-p_+)/(8-p_+); the expression increases with p because its logarithmic derivative is -log(delta)+1/(8-p)>0.

## 4. When a smooth center forces B3=0

For this section assume 6<p<7, and (10). A sufficient regularity hypothesis is that the center factor a is C6,alpha for p-6<alpha<1, and the canonical velocity is locally C6,alpha. The second condition follows from the first under the usual canonical full-plane growth hypothesis of the prompt, as justified below. With these assumptions B3=0.

First, w is odd C6,alpha and w=-Ax+O(x³). Set F=-w/(Ax). Then F is even C5,alpha, F(0)=1, and is positive near zero. Formula (5) can be written without a singular quotient:

    E=3 log F-(p-3) integral_0^x (F(t)-1)/(t F(t))dt.         (14)

Indeed differentiating gives -q-p/x. Since F-1 vanishes to second order, division by t leaves a C4,alpha function; (14) is C5,alpha and even. In particular e^-E is C4,alpha.

On the x-axis, rho=x²y a gives G3/x²=a_yy(x,0)/2. Therefore e^-E G3/x² is even C4,alpha. Dividing (12) by x² e^E gives

    e^-E G3/x² = sum_(j=2,4,6) qj x^(j-2)/(j-p)
                             +B3 x^(p-2)+O(x6).            (15)

The polynomial is its degree4 Taylor polynomial, because p-2>4. The C4,alpha remainder is O(x^(4+alpha)). If B3 were nonzero, dividing (15) minus its polynomial by x^(p-2) would give a nonzero limit, whereas the C4,alpha estimate tends to zero because 4+alpha>p-2. This contradiction proves B3=0. A C7 factor supplies the regularity needed in this argument by choosing alpha in (p-6,1), still conditional on (10). Neither C6,alpha nor C7 alone is asserted to produce the eighth-order remainder in (10). The restriction p<7 is needed for this C7 implication.

For completeness, the local regularity used here follows from an elementary kernel estimate. Localize rho by a smooth even cutoff equal to one on a smaller disk. Its compact part is C6,alpha on the plane. Write T for the principal-value convolution with K; the kernel has zero integral on circles, |K(z)|<=C|z|^-2 and |grad K(z)|<=C|z|^-3. The local term -rho e2/2 has the required regularity directly.

Here are the details of the Hoelder estimate for a compactly supported C0,alpha function f. Set h=|X-Y|>0 and B=B(X,2h). In the difference Tf(X)-Tf(Y), subtract the same constant f(X) from both integrands. This is valid in principal value with circular truncations because K has zero annular integrals; differences of the large truncation boundaries tend to zero, bounded by C h/R. In B, the K(X-Z) integral is bounded by C[f]_alpha h^alpha. For the K(Y-Z) integral first subtract f(Y). Its absolutely convergent part is bounded by C[f]_alpha integral_0^(3h) r^(alpha-1)dr. The remaining constant is (f(Y)-f(X)) times PV integral_B K(Y-Z)dZ. Since B(Y,h) is contained in B and B is contained in B(Y,3h), the inner centered-ball integral is zero and the remaining absolute integral is bounded by C integral_h^(3h) dr/r=C log3. This gives another C[f]_alpha h^alpha. Outside B, the kernel difference is bounded by C h |X-Z|^-3 and |f(Z)-f(X)|<=[f]_alpha |X-Z|^alpha. Its absolute integral is at most C[f]_alpha h integral_(2h)^infinity r^(alpha-2)dr=C_alpha[f]_alpha h^alpha, since alpha<1. These estimates prove the local C0,alpha bound without any unproved boundary-cancellation assertion. Local boundedness follows by the same near subtraction and the finite compact far integral.

Distributional differentiation commutes with this convolution. Apply the proved estimate to every derivative of the compact density through order6. The resulting continuous functions are its velocity's weak derivatives; successive integration along coordinate lines, or mollification followed by the fundamental theorem of calculus, identifies them as classical derivatives. This proves local C6,alpha regularity. The separated tail is smooth: its density is locally measurable and bounded, as in the prompt, and grows like r^gamma with gamma<1. First and higher kernel derivatives integrate absolutely, since their radial bounds are integral r^(gamma-q-1)dr for q>=1. The zeroth difference K(X-Z)-K(-Z) is O(r^-3) and is also integrable. Parity cancels the constant velocity on concentric truncations. Thus the canonical tail is smooth locally, and no derivative gain has been claimed.

The regularity threshold cannot be weakened to C6 alone. With an even compactly supported smooth angular cutoff chi equal to one near zero, set

    a_*(x,y)=|x|^(p-2) y² chi(y/x), x nonzero,
    a_*(0,y)=0.                                            (16)

It is homogeneous of degree p, smooth away from the origin, and its angular support stays away from the y-axis. Derivatives of order6 are O(r^(p-6)); the same two-region difference argument as for (4) makes them Hoelder of order p-6. Lower derivatives extend continuously. Thus a_* is C6,p-6. Its cubic trace is G3=|x|^p. If desired add the constant1 to the factor to retain a(0)=1. This is a counterexample to a regularity implication, not an exact IPM solution.

For a P_infty profile the factor is smooth at the center. The same kernel argument gives smooth local w and hence an even smooth Q with Q=O(x²); (10) then follows by Taylor's theorem. Global C3 regularity near the axis and the endpoint geometry are still needed for (3),(8). In the P2 class even G3 need not exist. Consequently a nonzero certified B3 under stronger trace hypotheses would not by itself exclude the full P2 class.

## 5. A precise pullback continuity estimate

A norm for B3 must control the subtracted integrand near zero. The phrase 'continuous in low norms' is false. Fix p in (6,8), a nonzero nonnegative smooth phi supported in (1,2), and epsilon<L/2. Let

    Q_epsilon(x)=epsilon^p phi(x/epsilon).

All center Taylor coefficients vanish, while ||Q_epsilon||_Cj=O(epsilon^(p-j)) tends to zero for integer j<=6. Yet its contribution to (11) is the nonzero constant

    -integral_1^2 t^(-p-1)phi(t)dt.                         (17)

This is an exact change of variables, not a numerical conditioning argument.

Here is an explicit metric that also treats changing L. Pull back x=L t to (0,1), and define

    Qhat(t)=L^-2 Q(Lt), qhat_j=L^(j-2)qj,
    Rhat(t)=Qhat(t)-sum qhat_j t^j.

Then

    beta3=-sum qhat_j/(j-p)-integral_0^1 t^(-p-1)Rhat(t)dt. (18)

Fix t0 in (0,1). Assume BOTH members of the comparison class satisfy p in [p_-,p_+] inside (6,8), |qhat_j|<=Q_j, |Rhat(t)|<=Khat t8 for0<t<=t0, and integral_t0^1 |Rhat(t)|dt<=J. The endpoint is allowed to be unbounded but integrable. In fact (7) usually gives Qhat(t) comparable to (1-t)^(2/A-1), which is unbounded when p<7 and f(L) is nonzero. A global bound Khat t8 would therefore be inappropriate for the intended class. Put d_j=p_--j>0 and

    d_* = |p-pbar|+sum |qhat_j-qbar_j|
              +integral_0^1 t^(-p_+-1)|Rhat-Rbar|dt,
    M_* = max(1, max_j 1/d_j,
                    sum_j Q_j/d_j²+Khat/(8-p_+)²
                            +|log t0| t0^(-p_+-1) J).       (19)

Then |beta3-betabar3|<=M_* d_*. For the polynomial terms use the identity for the difference of reciprocals, which gives the two bounds 1/d_j and Q_j/d_j². For the integral, the change of R is bounded by the weighted term in d_*. The mean-value theorem in p gives

    |t^-p-t^-pbar|<=|p-pbar| |log t| t^-p_+,
    integral_0^1 t^(7-p_+)|log t|dt=1/(8-p_+)².

The near part is bounded using the displayed integral over(0,1), which is a valid enlargement of(0,t0). On[t0,1), |log t| t^(-p_+-1)<=|log t0|t0^(-p_+-1), so its contribution is at most |p-pbar| |log t0|t0^(-p_+-1)J. These prove (19). The uniform local remainder bound and the endpoint L1 bound, or a substitute uniform logarithmic moment, are needed when p varies. A bare weighted L1 bound does not imply it. For instance R(t)=t^p_+/log²(e/t) has finite integral against t^-p_+-1 but infinite logarithmic moment, so the one-sided p derivative of its integral is unbounded at p_+.

Thus B5 can be made precise with (19); it is not a numeric Lipschitz certificate for the trial class. The required map from the full density norm into d_* is not supplied here.

## 6. Conditional exclusion and what remains open

In a specified ball of exact profiles that satisfy the smoothness and axis hypotheses, B3=0. Suppose a reference cutoff functional has |Phi_delta,0|>=b_delta>0, and on that ball |Phi_delta-Phi_delta,0|<=M_delta C_N r. Suppose also a uniform (10) with constant K, p<=p_+<8 and delta<=min(1,r0). If

    M_delta C_N r+K delta^(8-p_+)/(8-p_+)<b_delta,

then (13) contradicts B3=0 throughout the ball. This is a valid conditional exclusion. No value of b_delta, map constant C_N, uniform K, radius containing the numerical uncertainty, or complete endpoint geometry has been verified for this task. The decisive NO endpoint is therefore not reached.

The lead's statements concerning the present modal trial require a separate check. Its density axis trace has no noninteger x^p term by its finite inner representation, but canonical Green inversion can create logarithmic terms at resonant integer powers. This note does not assume a plain Taylor finite-part expansion for its reconstructed Q. A small trial residual or a numerical equality between two trial expressions is not an estimate of B3 for a neighboring exact profile.

## 7. Executable evidence planned

Check (1)-(3) by exact polynomial coefficient extraction, the sign in (5), normalized reconstruction (9), the rational model from topic58, (12)-(13) on a finite polynomial Q, the exponent identities and both metric integrals. Recompute every numerical cutoff illustration using independent Arb and mpmath.iv expressions. Keep actual source hashes, complete outputs and an actual Opus5.5 review. These checks support the analytic proof and do not replace its hypotheses.
