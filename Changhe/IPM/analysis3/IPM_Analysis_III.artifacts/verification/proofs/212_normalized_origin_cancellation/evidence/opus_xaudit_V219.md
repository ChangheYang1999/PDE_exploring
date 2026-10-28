# Independent cross-audit of V219 (proof 212): exact origin cancellation and the sharp quadratic normalized bound

Auditor: independent auditor. Done by hand, with no computation beyond trivial arithmetic and sha256sum. No file other than this one was created or modified. No git, no network.

Audited file: verification/proofs/212_normalized_origin_cancellation/PROOF.md

SHA256 (sha256sum): be13a724f3dfe02a9b31d38643c8712a70619467a1ea5c0acfc01bb766a89cbe

This hash matches the one recorded in V219 and in evidence/check.json. The six dependency hashes in check.json (topics 33 and 199 to 203) also match the current files byte for byte.

Context read: VERIFICATION_RECORD sections V203 to V207 and V219; verifier message 70; proofs 33 and 199 to 203; xaudit_V203_V204.md, xaudit_V205_V206.md and xaudit_V207_V208.md (for orientation only); S2_CALPHA_THEORY.md section 2(e).

## Verdict

**PASS WITH REMARKS.** I found no mathematical gap. The upper bound (1), ||chi_delta(U[h]+c[h]X/3).grad rho||_E2 <= C delta^2 ||h||_E2, holds. The matching operator lower bound c0 delta^2 also holds. Both are stated for fixed 0<alpha<1 and small delta, with qualitative constants, which is the correct scope. The four directional estimates (2), the strain series (8), the background division (17), every cutoff pair type and the compact sharpness packet all check out. The stated consequences are correct as upper bounds: frozen Neumann error O(delta^2), variable error O(delta^(2-alpha)). Every remark below is cosmetic or informational. Remark 12 records an optional sharpening of the variable error, which is not needed and not claimed.

## Checks

### 1. Algebra of the cancellation and the size of each norm component

Write R=U-c(-x,y)=(U1+cx, U2-cy)=(xZ, W), with Z=U1/x+c and W=U2-cy. With rho_x=x a1 and rho_y=x^2 a2, the following holds exactly:

 (U+cX/3).grad rho = R.grad rho + c[(-x+x/3)rho_x + (y+y/3)rho_y]
                   = x^2(a1 Z + a2 W) + c x^2[-(2/3)a1 + (4/3)y a2].

So the formula proposed in the audit request is correct. For P=x^2y we have a1=2y and a2=1, so the bracket is -(4/3)y+(4/3)y=0. The same fact can be seen invariantly: (-x,y).grad P=-P, and Euler's identity gives X.grad P=3P, so ((-x,y)+X/3).grad P=0. This holds for any multiple J0 x^2y, so the cancellation does not depend on the normalization of the cubic coefficient. With a1=2y+e1 and a2=1+e2 the bracket is exactly E=-(2/3)e1+(4/3)y e2, which agrees with (18).

As a consistency check, rho-P=O(r^5) (Check 3), so ((-x,y)+X/3).grad(rho-P)=O(r^5)=x^2 O(r^3). This agrees with |E|<=C r^3. Nothing else cancels. What remains is the velocity remainder against the full background, x^2(a1 Z+a2 W), plus c times the degree>=5 background remainder, x^2 cE.

The sizes of the pieces on the box R_delta={|x|<=delta, |y|<=2delta} are as follows. Here [.]_alpha is the y-Holder seminorm on [-2delta,2delta] at fixed x.

- a1 Z. On the box |a1|<=C delta and the y-Lipschitz constant of a1 is at most C, so [a1]_alpha<=C delta^(1-alpha). By (2), the supremum is at most C M delta^(2+alpha). The seminorm is at most C delta * C M delta + C delta^(1-alpha) * C M delta^(1+alpha) = C M delta^2.
- a2 W. The supremum is at most C M delta^(2+alpha). The seminorm is at most C * C M delta^2 + C delta^(1-alpha) * C M delta^(2+alpha), which is C M delta^2.
- cE. Here |c|<=(4/pi)M (proof 200 at p=2; see Remark 8), |E|<=C r^3 and |DE|<=C r^2. The supremum is C M delta^3 and the y-Lipschitz constant is C M delta^2. On an interval of length 4delta this gives a seminorm of at most C M delta^(3-alpha), which is at most C M delta^2 because alpha<1.

Next, the cutoff. Let G=a1 Z+a2 W+cE, so the coupling is x^2 chi_delta G. At fixed |x|<=delta I checked every pair type:

- Both y, y' in [-2delta,2delta]. Use chi_delta(y)(G(y)-G(y'))+(chi_delta(y)-chi_delta(y'))G(y'). The first term is at most C M delta^2 |y-y'|^alpha. The second is at most [chi_delta(x,.)]_alpha * sup|G|, which is C delta^(-alpha) * C M delta^(2+alpha) = C M delta^2.
- One point outside [-2delta,2delta], the other on the support (so |y|<=delta). The separation is at least delta, and the quotient is at most C M delta^(2+alpha)/delta^alpha.
- Both points off the support: the difference is zero.
- |x|>delta: the whole slice vanishes.

Since [x^2 F]_(y,2)=sup_x [F(x,.)]_alpha, the weighted y-seminorm of the image is at most C M delta^2. This holds uniformly down to x=0, where (2) is still uniform and the image slice is identically zero.

The supremum is at most C M delta^3 by the crude route in the proof. Through (18) it is in fact C M delta^(4+alpha).

For the x-seminorm, put Wv=chi_delta grad rho. Its supremum is at most C delta^2 and its Lipschitz constant at most C delta, so its Holder seminorm is at most C delta^(2-alpha). Evaluate the undifferenced velocity at the supported point. The two terms are then C M delta * C delta^(2-alpha) and [U]_(C^alpha(B1)) * C delta^2 <= C M delta^2 (proof 199 (11)). The column contributes |c| [chi_delta X.grad rho/3]_x <= C M delta^(3-alpha). So the x-seminorm is C M delta^2. The cancellation is not used here, and none is available (Check 4).

Parity and continuity of the image are correct. U1 rho_x and U2 rho_y are both even in x and odd in y, and both vanish on x=0. Hence (1) follows from (2) and (17).

### 2. Band-by-band strain subtraction and the four estimates (2)

(a) Compact reduction. Oddness gives |h(x,y)|<=M x^2|y|^alpha. Together with the product difference rule this yields ||g(x,.)||_inf+[g(x,.)]_alpha<=C M x^2.

The far velocity U[h-g] is smooth on a fixed disk, with derivatives of order >=1 bounded by C||h||_inf. Its parities admit only the monomial x in U1 and only y in U2 through degree 2. No quadratic monomial is odd in x and even in y, or even in x and odd in y. Divergence freedom then forces the Taylor polynomial c_far(-x,y). The cubic remainder gives sup C M delta^3 and seminorm C M delta^(3-alpha) for W_far. Taylor division in x gives sup C M delta^2 and seminorm C M delta^(2-alpha) for Z_far. All four bounds are stronger than (2).

(b) Band formulas.

- The symbol of U2 is -xi^2/(xi^2+eta^2) = -1+eta^2/(xi^2+eta^2), so U2[g_j]=-g_j+Q_j with Q_j=eta^2(-d_x^2+eta^2)^(-1)g_j. This is (3).
- The x-kernel of Q_j is (|eta|/2)e^{-|eta||z|}. With the band cutoff and k y-derivatives, its y-integrated absolute value is at most C_k lambda^(1+k) e^{-c lambda|z|}. This is the same integration by parts in omega=eta/lambda as proof 199 (7).
- The moment integral against |x'|^2 gives the factor (x^2+lambda^(-2)). Hence (4) holds, and (5) is Bernstein's inequality.
- (6) reads d_x^2 Q_j=-d_y^2 Q_j+d_y^2 g_j, with a continuous right side.
- Q_j is even in x and odd in y.

(c) Strain series (8).

- Because g(0,.)=0, every block satisfies g_j(0,.)=0. Hence d_y U2[g_j](0,y)=d_y Q_j(0,y).
- By (4) with k=1 at x=0, this is at most C M lambda^(-1-alpha), uniformly in y.
- The series of axis derivatives therefore converges uniformly, and sum_j |c_j| <= |c_0| + C M sum_(j>=1) 2^(-j(1+alpha)) < infinity.
- The low coefficient is bounded, |c_0|<=C M, by the H^1_eta kernel argument (proof 199, audited in xaudit_V203_V204).
- Parity makes the far-subtraction constants vanish for the compact g, so U[h]=U[g]+U[h-g] with consistent conventions.
- Proof 201 proves Frechet differentiability at 0 with DU(0)=c[h]diag(-1,1). In particular d_y U2[h](0,0)=c[h].

Therefore c[h]=c_far+sum_(j>=0) c_j is a genuine, absolutely convergent identity. It is not a formal regrouping, and the low block is treated correctly.

(d) Low bands, 1<=j<=N, where lambda delta<=1.

- (9). From (6), d_x^2 d_y Q_j=-d_y^3 Q_j+d_y^3 g_j. By (4) and (5) with k=3, on |x|<=delta this is at most C M lambda^(3-alpha)(delta^2+lambda^(-2)) + C M delta^2 lambda^(3-alpha), which is at most C M lambda^(1-alpha).
- (10), first line. The Taylor step in x uses d_x d_y Q_j(0,y)=0, by evenness, and the continuity of d_x^2 d_y Q_j. The Taylor step in y along the axis uses d_y^2 Q_j(0,0)=0, because d_y Q_j(0,.) is even.
- (10), second line. d_y^2 Q_j is odd in y.
- (11). d_y W_j=-d_y g_j+(d_y Q_j-c_j) is at most C M delta^2 lambda^(1-alpha). W_j is odd in y, so its supremum on |y|<=2delta is at most 2delta times that.
- Summation. sum_(j=1)^N 2^(j(1-alpha)) <= 2^(N(1-alpha))/(1-2^(alpha-1)) <= C_alpha delta^(alpha-1).
- This gives, for the low part of W, sup C M delta^(2+alpha) and y-Lipschitz constant C M delta^(1+alpha). The seminorm on [-2delta,2delta] is then C M delta^(1+alpha)(4delta)^(1-alpha) = C M delta^2.
- The j=0 block obeys the same bounds with lambda=1. They are smaller.
- (12). U1(0,y)=0 and d_x U1=-d_y U2, which holds pointwise because each band has a continuous x-derivative. This gives Z_j=-integral_0^1 d_y W_j(tx,y)dt, so ||Z_j||<=||d_y W_j||.
- d_y Z_j is bounded by sup|d_y^2 g_j|+sup|d_y^2 Q_j|, which is at most C M(delta^2 lambda^(2-alpha)+delta lambda^(1-alpha)) <= C M delta lambda^(1-alpha).
- Summing gives, for the low part of Z, sup C M delta^(1+alpha), y-Lipschitz constant C M delta^alpha and seminorm C M delta.
- The low bands never need d_x U1 directly. Only the derivatives Q_xxy and Q_yyy of the U2 band enter.

(e) High bands, j>N, where lambda>1/delta.

- (14). By (5) with k=0 and by (4), ||U2[g_j](x,.)|| <= C M lambda^(-alpha)(2delta^2+lambda^(-2)) <= C M delta^2 lambda^(-alpha), uniformly for |x|<=delta.
- Dyadic reconstruction (proof 199). Split the sum at 2^j about 1/d and use Bernstein's inequality. This bounds the global y-seminorm of the high sum by C_alpha M delta^2. Its supremum is at most C M delta^2 2^(-alpha(N+1)) <= C M delta^(2+alpha).
- (15). If lambda|x|<=1, integrating proof 199 (9) at p=2 gives at most 2C M lambda^(-1-alpha) <= 2C M delta lambda^(-alpha). If lambda|x|>=1, dividing directly gives C M lambda^(-alpha)(|x|+lambda^(-1)) <= 2C M delta lambda^(-alpha).
- At fixed x the quotient is band-limited in y. Reconstruction therefore gives seminorm C M delta and sup C M delta^(1+alpha).
- (16). sum_(j>N)|c_j| <= C M 2^(-(1+alpha)(N+1))/(1-2^(-1-alpha)) <= C M delta^(1+alpha).
- Its y-multiple costs sup C M delta^(2+alpha) and seminorm C M delta^(1+alpha)(4delta)^(1-alpha). As a constant, it adds nothing to the seminorm of Z.

(f) Assembly. W=W_far+sum_(j<=N)W_j+[sum_(j>N)U2[g_j]-(sum_(j>N)c_j)y], and Z decomposes in the same way. Both decompositions rest on (8). All four estimates in (2) hold with exactly the stated powers.

Consistency checks:

- Proof 201's isotropic remainder O(r^2(1+|log r|)) does not contradict the sup bound delta^(2+alpha). The quadratic Taylor terms vanish by parity, as already observed in xaudit_V205_V206 remark 3.
- The sharpness packet of Check 4 saturates the W supremum bound. There U2=P_xx, with sup eps^alpha <= delta^(2+alpha).

### 3. Background division and C^(4,1) regularity of the actual trial

Consider a monomial x^a y^b with a even and b odd. Its degree is odd, so the parities exclude all terms of degree 0, 2 and 4. The condition rho(0,y)=0 excludes y and y^3. The Taylor polynomial through degree 4 is therefore exactly x^2 y. Since D^4 rho is Lipschitz and vanishes at 0, D^k(rho-x^2y)=O(r^(5-k)) for k<=4.

Hence:

- rho_xx-2y=O(r^3) and D(rho_xx-2y)=O(r^2);
- rho_xxy-2=O(r^2) and D rho_xxy=O(r).

The division formulas are:

- a1=integral_0^1 rho_xx(tx,y)dt, using rho_x(0,y)=0;
- a2=integral_0^1(1-t)rho_xxy(tx,y)dt, using rho_y(0,y)=0 and d_x rho_y(0,y)=0.

Since integral_0^1(1-t)dt=1/2, we get a2=1+e2. All four bounds in (17) follow, uniformly on a fixed smaller disk.

The Lipschitz fourth derivatives are actually needed. With C^4 alone one only gets E=o(r^2) and DE=o(r). Then the column remainder would be only o(delta^(2-alpha)) in the weighted y-seminorm, not O(delta^2). The coefficient bounds behind the a1 Z and a2 W products need only C^4.

Regularity of the actual trial is established in proof 33 (proofs/33_modal_origin_regularity/PROOF.md, hash matches). On the inner disk r<exp(t_minus) the exact definition is rho=x^2y[1+sum D_mj e^(2j(t-t_minus))cos(2m theta)+e^(bi(t-t_minus)) sum E_mi (t-t_minus)^i cos(2m theta)], with finitely many terms. The degree-5 terms r^5 H(theta) have fourth derivatives that are homogeneous of degree 1 with smooth angular factors, hence Lipschitz. The higher-degree terms and the logarithmic terms of degree 3+bi>53 are smoother. So rho is C^(4,1) with the required parities, with rho(0,y)=0, and with cubic coefficient exactly 1, since the bracket tends to 1. Proof 33 also proves that rho is not C^5, so C^(4,1) is precisely the available regularity, and it suffices. I did not re-extract proof 33's dyadic coefficients. The C^(4,1) argument is elementary and I accept it.

### 4. Lower bound construction and its scaling

Geometry. Take q=delta/8 and b<1/8. The four disks are then disjoint and avoid the axes. They lie in B_(delta/2), because |Q|+b delta <= (sqrt2/8+b)delta < delta/2.

Velocity. With h=-Delta P we have hat h=|k|^2 hat P. Then m1 hat h = xi eta hat P, which is the symbol of -d_x d_y, and m2 hat h = -xi^2 hat P, which is the symbol of d_x^2. So U=(-P_xy,P_xx), which is (20). The input is compact and smooth with both parities, so no subtraction constant appears.

Normalization functionals. c=0, because U vanishes identically near 0 (by proof 201, or directly from the strain integral). J=0, because d_eps vanishes near 0.

Input norm. The proof does not state the cutoff scaling explicitly. I assume chiQ=phi((X-Q)/(b delta)) with phi fixed (see Remark 4). Put s=(x-q)/eps. Then

 d_eps = eps^alpha cos(s) chiQ + 2 eps^(1+alpha) sin(s) d_x chiQ - eps^(2+alpha) cos(s) Delta chiQ.

For eps<=delta:

- sup|d_eps| <= C eps^alpha.
- |d_x d_eps| <= C eps^(alpha-1). Splitting x-differences at length eps gives [d_eps]_x <= C.
- The y-dependence enters only through chiQ, so |d_y d_eps| <= C eps^alpha/delta and [d_eps(x,.)]_alpha <= C eps^alpha delta^(-alpha).
- Nonzero vertical lines have |x| >= (1/8-b)delta, so [d_eps]_(y,2) <= C eps^alpha delta^(-2-alpha). This is (21).

With eps^alpha <= delta^(2+alpha), the bound ||d_eps||_E2 <= C holds uniformly in delta. The two points stay on the plateau, because pi eps <= pi delta^(1+2/alpha), which is much smaller than b delta.

Image. On the plateau chi_delta=1, c=0, P_xy=0 and P_xx=-eps^alpha cos(s), so the image is -eps^alpha cos(s) rho_y. At s=0 and s=pi the values are -eps^alpha rho_y(X0) and +eps^alpha rho_y(X1). These have opposite signs, so the difference is at least eps^alpha(rho_y(X0)+rho_y(X1)).

By (17), rho_y=x^2(1+O(r^2)) >= (delta^2/64)(1-C delta^2) at both points. Dividing by (pi eps)^alpha gives an x-Holder quotient of at least (delta^2/(32 pi^alpha))(1-C delta^2). Hence ||B_norm||_(E2->E2) >= c0 delta^2, with c0 of order 1/(32 pi^alpha C). The scaling is correct.

The mechanism is simple. U2=-d_eps-P_yy, and P_yy=O(eps^(2+alpha)/delta^2) is negligible. So the image is essentially -d_eps rho_y: the local identity part of U2 multiplied by rho_y, which is of order x^2. No strain normalization can touch this term. This also explains why the x-seminorm was already O(delta^2) before normalization. The improvement over V207 comes entirely from the weighted y-seminorm. Before normalization, V207's delta^(1-alpha) is sharp: take h=x^2y chi(r) with c[h]>0, as in xaudit_V207_V208 A12. After normalization it is not sharp.

### 5. Consequences and scope

Frozen. kappa_2=1+2A0-alpha D0=D0(1-alpha) with D0=2A0+1. So K0=max(1,1/(D0(1-alpha))) is proof 25's bound for the maximal-domain inverse at p=2, since the x-factor 1/(1+A alpha) and the sup factor are at most 1. The factorization L_delta=(I+B_norm R0)T0 gives ||L_delta^(-1)|| <= K0/(1-C delta^2 K0) when C delta^2 K0<1. The strain bound |c[h]| <= (4/pi)||h||_E2 at p=2 then gives the stated control of c on solutions. Both are correct.

Variable. Use proof 202 at p=2, as verified in xaudit_V207_V208 A11. With E_delta=-m_delta+q_delta B_norm, the new bound is C_M delta^(2-alpha)+(q0+C_M delta^(2-alpha))C delta^2 = O(delta^(2-alpha)). The leading term is the reciprocal-transport multiplier of proof 202 (11), not the coupling. The domain is unchanged because the perturbation is bounded. The claim is correct as an upper bound. Remark 12 explains why it can probably be sharpened.

Scope.

- Constants are qualitative. No numerical C or delta0 is given.
- The operators are whole-plane extensions. They agree with the actual operator only on B_(delta/2).
- There is no full-plane inverse.
- E_2 does not see J.
- There is no nonlinear closure. Topics 204 and 207 still apply.

Both the proof and V219 state all of this. The second paragraph of team message 70 (a common space E2 intersect L2, and physical c near the source) is outside V219. I did not audit it.

## Remarks

1. Line 41: "They have y support in a fixed enlarged annulus of size lambda". This means y-frequency support; the blocks are not compactly supported in y. Cosmetic.

2. Line 24: "[U2[h](x,.)-c[h](.)]". This means the function y -> U2[h](x,y)-c[h]y. Cosmetic notation.

3. Line 151 uses, without saying so, the parity fact of Check 3: there are no Taylor terms of degree 2 or 4, so rho-x^2y=O(r^5). It would help to state it, and to note that the cancellation holds for any multiple of x^2y. Cosmetic.

4. Lines 180 to 194: the estimates in (21) need |D^k chiQ| <= C_k delta^(-k). That is, chiQ should be a fixed profile rescaled to radius b delta. This is implicit in "direct cutoff differentiation" and should be stated, because (21) depends on it. Cosmetic.

5. Line 72: the proof states uniform convergence of the derivative series along the axis. It should add one sentence on the function series. The bound |Q_j(0,.)| <= C M lambda^(-2-alpha) makes sum_j Q_j(0,y) absolutely convergent. Its value is U2[g](0,y), because the partial sums are U2 applied to the Littlewood-Paley partial sums of g, which converge to U2[g], and U2[g] is continuous. Cosmetic.

6. Line 39: "derivatives of every fixed positive order bounded by C M". In fact C||h||_inf suffices, since h-g vanishes on [-2,2]^2. Cosmetic.

7. V219 and team message 70 say that the low-band Taylor step "uses only Q_xx and Q_yyy". The proof actually uses d_x^2 d_y Q_j and d_y^3 Q_j, linked by (6): Q_xxy=-Q_yyy+g_yyy. This is a wording fix in the verdict text, not in the proof. Cosmetic.

8. Dependencies used at p=2. Proof 200 is stated for p<2 but is used at p=2 for |c| <= (4/pi)M. Proof 202 is used at p=2. Both were checked to apply verbatim in xaudit_V207_V208 (A9, A11 and issue 1). The bound |U| <= C M delta on B_delta, cited from proof 203, also follows directly from (2). Informational.

9. The constants are not uniform in alpha. The low sum costs 1/(1-2^(alpha-1)), the high reconstruction costs 1/(1-2^(-alpha)), K0 blows up as alpha->1, and c0 depends on alpha through pi^alpha and the input constant. This is harmless for fixed alpha, which is what is claimed. Informational.

10. The sharp component is the x-seminorm. The supremum is much smaller, O(M delta^(4+alpha)) by (18). The proof correctly limits sharpness to the full E2 norm. Whether the weighted y-seminorm part alone is also of exact order delta^2 is neither claimed nor checked here. Informational.

11. The lower-bound argument uses only rho_y >= c x^2 near Q_delta. It therefore applies to every background in the class with leading term x^2y, and equally to the unnormalized operator, since c[d_eps]=0. The phrase "on the actual modal background" is correct but narrower than the argument. Informational.

12. Optional sharpening of the variable error. This is my own observation, checked by hand. Proof 212 does not claim it, and it is not needed for V219. In proof 202 (11) the power delta^(2-alpha) comes only from the term ||h||_inf [m]_alpha in the x-seminorm. For h in E_p, however, |h(x,y)| <= [h]_(y,p)|x|^p|y|^alpha <= M delta^(p+alpha) on supp m, which lies in B_delta. If the undifferenced h is evaluated at the supported point, then [mh]_x <= C delta^2[h]_x + C delta^(2-alpha) M delta^(p+alpha). The sup and weighted-y parts were already O(delta^2) (xaudit_V205_V206 remark 10). So ||m_delta||_(E2->E2)=O(delta^2), and with the present result the variable Neumann error would also be O(delta^2). V219's O(delta^(2-alpha)) remains a correct upper bound. If this sharpening is adopted, it should be recorded as a separate amendment to proof 202 (11).

13. Statement of (1): delta0 must also satisfy delta<1/4, keep sqrt(5)delta inside the C^(4,1) disk and inside the disk where the far velocity is smooth, and depend on the fixed auxiliary cutoffs chi_x, chi_y and eta_0. "Depending on alpha, the fixed local C^(4,1) bound and chi" covers this loosely. Cosmetic.

14. Integrity: the proof hash and all six dependency hashes in evidence/check.json match the current files. Informational.
