# Independent proof and entry audit of report 4.41

## Exact statement and status

Let beta>0, and let W,Theta,Omega be smooth real fields on R2 with divW=2beta, Omega=partial_y W1-partial_x W2, W(0)=0, W(X)=beta X+o(|X|) uniformly at infinity, and

    W.gradTheta=(beta-2)Theta, W.gradOmega+Omega=Theta_x.

Assume Theta and W2 even in x, Omega and W1 odd in x, Theta(0,y)=0 on the entire axis, and Theta=a0*x^2+O(|X|^3) at0 with a0!=0. Assume Theta_xx(0,y)!=0 for every real y. Define I_j=partial_x^(2j)Theta(0,y)/Theta_xx(0,y)^j for j>=2.

(a) If beta>2, let N be the greatest even integer<=3beta/(beta-2), M=2N+4. Under the axis bounds |partial_x^j W2(0,y)|<=D_j |y|^(1-1/beta-j) for every even j=N+2,...,2N+2 at large |y|, at least one even temperature derivative of order4,...,M is not identically zero on the axis. If additionally the full class A spatial symbol estimates hold, at least one of I_2,...,I_(N+2) is nonconstant. Every class A profile has those estimates, as separately checked in P229 and P233 through report4.37(5).

(b) If beta=2, I_2 and I_3 cannot both be constant. This assumes full smoothness, even though only derivatives through order six are constrained. No symbol estimates, separated representation, or analyticity are assumed in (b).

These are restricted necessary conditions. General B2 remains OPEN. The complete independent proofs below were written and checked as P230/P231 before this entry audit. They are reproduced so this packet is standalone; their historical status paragraphs retain their dates. The literal proposed4.41 entry and complete preview are CONFIRMED on 2026-10-22T00:37:08.713566+00:00. Actual insertion remains OPEN until a fresh read.

## Part A. Complete supercritical argument

# A finite axis-derivative obstruction at beta greater than two

## Exact statement and status

Fix beta>2, set

    alpha=(beta-2)/2, L=1+3beta/2,
    N=2 floor(3beta/(2(beta-2))), M=2N+4.

Thus N is the greatest even integer no larger than 3beta/(beta-2), and N>=2. Let W,Theta,Omega be smooth real fields on R2 with

    div W=2beta, Omega=partial_y W1-partial_x W2,
    W(0)=0, W(X)=beta X+o(|X|) uniformly at infinity,
    W.grad Theta=(beta-2)Theta, W.grad Omega+Omega=Theta_x.

Assume W1,Omega odd and W2,Theta even under x reflection, Theta(0,y)=0 for all y, and Theta(x,y)=a0 x²+O(|X|³) at0 with a0!=0. Assume the following finite family of velocity bounds on the axis, each with its own constant and sufficiently large radius:

    |partial_x^j W2(0,y)|<=C_j |y|^(1-1/beta-j),
    j=N+2,N+4,...,2N+2.                                 (S_f)

Then it is impossible to have both

    Theta_xx(0,y)!=0 for every y in R,                    (J1)
    partial_x^j Theta(0,y)=0 for every y in R,
    j=4,6,...,M.                                         (J2)

No separable formula, convergent Taylor series, or temperature condition off the axis is assumed. The smoothness hypotheses are convenient and are not claimed minimal. This is a restricted necessary-condition theorem, not a full B2 exclusion. Status: CONFIRMED by the verifier on 2026-10-22T00:13:11.191127+00:00. The complete proof preceded 81 successful exact controls. Actual Opus5.5 returned no written audit, so external mathematical review remains unavailable and separate lead-lane review is pending. The proof below was written before those controls.

Corollary in the broad polynomial-vorticity B2 target. Assume the same B2 conditions and |Omega|<=C(1+|X|)^k for some finite k>=0. If(J1) holds, then at least one of the functions

    y -> partial_x^(2j) Theta(0,y) / Theta_xx(0,y)^j,
    j=2,3,...,N+2,                                      (I_j)

is nonconstant. The all-order symbol estimates proved in P36 after P40/P33 apply here, as explicitly checked in P229 Section9. They supply(S_f), and they will also be used for the scalar part of the corollary. The main theorem with(S_f) is self-contained.

## 1. The positive scale and its two ends

By(J1), the continuous function Theta_xx(0,y) has a constant sign. If needed apply S(x,y)=(x,-y), Wnew(X)=S W(SX), Thetanew(X)=-Theta(SX), Omeganew(X)=-Omega(SX). These preserve all equations, parity, sublinearity and the derivative hypotheses while reversing the sign. Hence assume A0=Theta_xx(0,0)=2a0>0. Define

    a(y)=sqrt(A0/Theta_xx(0,y)), a(0)=1,
    A(y)=integral_0^y a(s)ds, phi(y)=W2(0,y).

This is a smooth positive global scale. Differentiate temperature transport twice in x on the axis and use div W=2beta there. The terms containing Theta or Theta_x vanish on the axis. The remaining equation is

    phi (Theta_xx)' + [2(2beta-phi')-(beta-2)]Theta_xx=0.

Substitute Theta_xx=A0/a² to obtain phi'+phi a'/a=L, or (a phi)'=L a. Since phi(0)=0, it follows that

    phi=L A/a.                                          (1)

In particular phi has the sign of y and its only zero is0, with phi'(0)=L. At either end, sublinearity gives phi(y)/y->beta. Write gamma=1/2+1/beta in(1/2,1). On y>0,

    A'/A=L/phi, y A'/A->L/beta=1+gamma.

For every sufficiently small epsilon>0, integrate the resulting two inequalities for the logarithmic derivative, then use a=L A/phi. This gives positive constants c,C, depending on epsilon, such that

    c |y|^(gamma-epsilon)<=a(y)<=C |y|^(gamma+epsilon)    (2)

at both ends. At the negative end apply the same argument to a(-t), -A(-t) and -phi(-t), t>0. Thus a tends to infinity at both ends and a=o(|y|). No derivative of an asymptotic identity was taken.

## 2. Finite Taylor remainders and transport coordinates

Write k=x/a(y), V(k,y)=W2(ka(y),y), Q(k,y)=W1(ka(y),y)-k a'(y)V(k,y), and S(k,y)=Theta(ka(y),y). Since M is even, parity and(J2), together with S_kk(0,y)=A0, give

    S(k,y)=A0 k²/2+k^(M+2) E(k,y),                     (3)

where E is smooth on R2. To justify a global smooth remainder, divide the smooth function S-A0 k²/2 successively by k using its vanishing derivatives on k=0, or use the integral Taylor remainder. This also proves the asserted order after any number of y derivatives, on every compact y interval. No uniform remainder bound as |y| tends to infinity is needed.

The exact coordinate identities are

    W.grad Theta=(Q/a)S_k+V S_y,
    Q_k+(aV)_y=2beta a.                                 (4)

Since S_k=A0 k+O(k^(M+1)), division of the first equation by S_k, initially for nonzero k and then smoothly across0, gives

    Q=a alpha k+k^(M+1) R1(k,y).                        (5)

Indeed [(beta-2)S-alpha k S_k-V S_y] is divisible by k^(M+2), while S_k/k is smooth and nonzero near each point(0,y). This establishes(5) locally near the whole axis. It includes every mixed y derivative. The constants controlling these local divisions may depend on the compact axis segment.

Substitute(5) into the second identity of(4), and integrate from0 to y along a sufficiently small common k strip over that compact segment. With C(k)=W2(k,0), a(0)=1, obtain

    aV=L A+C(k)+k^M R2(k,y).                            (6)

The same smooth even germ C is used for every compact axis segment. It has C(0)=0. Every derivative in k below therefore holds for every real y with common coefficients, although the strip width may shrink with the segment.

## 3. The finite velocity jet becomes a polynomial

For j<M, equation(6) implies

    partial_x^j W2(0,y)=C^(j)(0)/a(y)^(j+1), j>=1.       (7)

If some C^(j)(0) were nonzero for an even j=N+2,...,2N+2=M-2, then(2) and(S_f) would give the incompatible lower and upper powers with difference

    j(1/2-1/beta)-3/2-(j+1)epsilon.

The first two terms have positive sum because j>N and N is the greatest even integer <=3beta/(beta-2). Choose epsilon smaller than that positive sum divided by j+1. The lower bound would then grow relative to the upper bound at infinity. Hence all these derivatives vanish. Odd derivatives of C vanish by parity. Therefore the even polynomial

    P(k)=sum_{j=0}^N C^(j)(0) k^j/j!

satisfies C-P=O(k^M) as a smooth remainder near0. P(0)=0. Combining with(5)-(6) gives a global polynomial comparison field

    D(k,y)=L A(y)+P(k),
    Wtilde2(ka,y)=D/a,
    Wtilde1(ka,y)=a alpha k+k a'D/a,
    Thetatilde(ka,y)=A0 k²/2,

such that, locally near each compact axis segment,

    W2-Wtilde2=O(k^M), W1-Wtilde1=O(k^(M+1)),
    Theta-Thetatilde=O(k^(M+2)).                         (8)

All orders in(8) mean a smooth divisible remainder, including mixed y derivatives. The comparison field need not be sublinear and is not claimed to be an admissible B2 profile.

## 4. The polynomial is nonzero

Let c2=C''(0)/2. Since M>=8, equation(6) determines the second x derivative of W2 without remainder. On the axis, differentiating div W gives W1_xy=-phi''. Thus

    eta(y):=Omega_x(0,y)=-phi''(y)-2c2/a(y)^3.            (9)

Differentiate the vorticity equation once in x there, using parity:

    phi eta'+(2beta+1-phi')eta=A0/a².

Using phi'=L-phi a'/a, set r=a eta to obtain

    phi r'+(beta/2)r=A0/a.                              (10)

Every backward orbit of y'=phi(y) remains in the compact interval between its starting point and0 and tends to0. Positivity of a on that interval and boundedness of r justify integrating(10) with the factor exp(beta s/2) from negative infinity. The endpoint term vanishes, and

    r(y0)=A0 integral_-infinity^0 exp(beta s/2)/a(y(s))ds>0.

Hence eta>0. If c2>=0, (9) gives phi''<0. For y<0 it follows that phi'(y)>phi'(0)=L, whence phi(y)<L y and phi(y)/y>L>beta. This contradicts the negative-end limit phi(y)/y->beta. Therefore c2<0, so P has a highest nonzero even degree n with 2<=n<=N.

## 5. The residual polynomial is zero from finitely many jets

Physical x differentiation lowers the k order by one. Physical y differentiation is partial_y|k-k(a'/a)partial_k and preserves a smooth divisibility order. Since Omega=-curl W, (8) implies

    Omega-Omegatilde=O(k^(M-1)),                         (11)

where Omegatilde is the negative physical curl of Wtilde. Both W1 and Wtilde1 are O(k). Thus differentiating(11) in x and multiplying by either first velocity component preserves order M-1; differentiating in physical y also preserves it. The terms containing the differences of the velocity fields times derivatives of Omegatilde have order at least M, and the temperature-source difference has order M+1. Consequently the vorticity residual of the comparison field, multiplied by a, is O(k^(M-1)). The original residual is exactly zero.

Let B=a''/a-2(a'/a)². Direct physical differentiation gives

    Omegatilde(ka,y)=L k a'+k D B-(1+k²a'^2)P'/a².       (12)

The comparison vorticity residual multiplied by a is the finite polynomial

    R(k,y)=a alpha k Omegatilde_k+D Omegatilde_y|k
                           +a Omegatilde-A0 k.          (13)

Its degree is at most 2N+1, while it is O(k^(M-1))=O(k^(2N+3)). Thus for each real y all its coefficients vanish: R is identically zero as a polynomial. This is finite Taylor algebra, not analytic continuation, and it does not make the original fields equal to their comparison fields off the axis.

## 6. Highest degree and final contradiction

Let p_n!=0 be the leading coefficient of P, and put p=a'/a, so B=p'-p². The coefficient of k^(n+1) in(12) is p_n(B-n p²). In(13), the unique contribution of degree2n+1 comes from P Omegatilde_y|k, since n>=2 and all the other terms have degree at most n+1. Its coefficient is

    p_n² [B'-n(p²)']=p_n² [p''-2(n+1)p p'].

Since it vanishes, p'-(n+1)p²=K for a real constant K on R. The positive smooth function v=a^(-(n+1)) satisfies

    v''+(n+1)K v=0,

and tends to zero at both ends by(2). If K=0, v is affine and cannot satisfy both end conditions unless zero. If K>0, it is a sine/cosine combination and a limit of zero at infinity forces both coefficients to vanish. If K<0, the two end conditions separately kill the positive and negative exponential solutions. Each case contradicts v>0. This proves the main theorem.

## 7. Proof of the corollary and scope

In the broad polynomial-vorticity target, the previously proved all-order symbol bounds give(S_f) and

    |partial_x^j Theta(0,y)|<=C_j |y|^(1-2/beta-j).

Suppose(J1) holds and all the finitely many functions(I_j) are constant. The scale in Section1 still obeys(1)-(2), because that section used only the second temperature derivative. For each even ell=4,...,M, constancy of the corresponding(I_j) implies

    partial_x^ell Theta(0,y)=h_ell/a(y)^ell

for a fixed constant h_ell. If h_ell!=0, comparison with its symbol bound and the upper scale bound has exponent difference

    (ell/2-1)(1-2/beta)-ell epsilon>0

for sufficiently small epsilon. This is impossible. Hence every h_ell=0, giving(J2), contrary to the main theorem. At least one(I_j) must therefore vary with y.

For beta=3, N=8 and M=20; beta=4 gives N=6,M=16; beta=5 gives N=4,M=12; beta>8 gives N=2,M=8. These are sufficient derivative orders, not claimed optimal. Beta=2 is not included because the strict exponent gaps disappear. Profiles with a zero of Theta_xx somewhere on the axis are not excluded. The result imposes only a necessary variation of a finite derivative ratio, and does not exclude general nonseparable profiles or provide a numerical candidate.

The main proof uses elementary smooth division, scalar ODEs and exact polynomial algebra. It is an independent finite-order strengthening of P229. The corollary additionally depends on the precise symbol theorem, including its polynomial-vorticity and canonical-relative-inverse hypotheses, frozen and checked in P229 Section9. No numerical state or optimizer output enters this proof.


## Part B. Complete critical argument

# A finite axis-ratio obstruction at beta equal to two

## Statement and scope

Let W,Theta,Omega be smooth real fields on the full plane with

    div W=4, Omega=partial_y W1-partial_x W2,
    W(0)=0, W(X)=2X+o(|X|) uniformly at infinity,
    W.grad Theta=0, W.grad Omega+Omega=Theta_x.

Assume W1,Omega are odd in x and W2,Theta even in x. Suppose Theta(0,y)=0 for all y and Theta(x,y)=a0 x²+O(|X|³) at the origin, a0!=0. Suppose also Theta_xx(0,y)!=0 for every real y. Then the two functions

    I2(y)=Theta_xxxx(0,y)/Theta_xx(0,y)²,
    I3(y)=partial_x^6 Theta(0,y)/Theta_xx(0,y)³

cannot both be constant on R.

This theorem requires no exact separated representation on any open set, no all-order symbol bound, and no assumption on the canonical inverse beyond the stated div-curl and velocity behavior. It is a necessary-condition theorem for smooth B2, not a full exclusion. Zeros of Theta_xx on the axis are outside its conclusion. Status: CONFIRMED by the verifier on 2026-10-22T00:18:08.987142+00:00. All 32 own controls passed. Actual Opus5.5 returned no written audit, so a separate lead review is pending. This full informal argument preceded those controls.

## 1. Scale, axis equation, and positivity

Assume for contradiction that I2 and I3 are both constant. Reflection in y with simultaneous sign reversal of Theta and Omega preserves the equations and x parity, and changes the sign of Theta_xx. Explicitly, for R(x,y)=(x,-y), use Wnew(X)=R W(RX), Thetanew(X)=-Theta(RX), Omeganew(X)=-Omega(RX). Thus assume A0=Theta_xx(0,0)>0. Define

    a(y)=sqrt(A0/Theta_xx(0,y)), a(0)=1,
    A(y)=integral_0^y a(t)dt, phi(y)=W2(0,y).

Continuity and the nowhere-zero hypothesis make a smooth and positive. Twice differentiating temperature transport on the axis and using parity and divergence gives

    phi (Theta_xx)' + (8-2phi')Theta_xx=0,
    (a phi)'=4a, phi=4A/a.                         (1)

The last identity uses W(0)=0. Therefore phi has exactly one zero at0, its sign is that of y, and phi'(0)=4. Sublinearity on the axis gives phi(y)/y->2 at both ends. No asymptotic derivative is taken.

## 2. Only six temperature derivatives are needed

Set k=x/a(y), S(k,y)=Theta(ka(y),y), V(k,y)=W2(ka(y),y), Q(k,y)=W1(ka(y),y)-k a'(y)V(k,y). The exact coordinate identities are

    (Q/a)S_k+V S_y=0, Q_k+(aV)_y=4a.             (2)

Constancy of I2,I3 means S_kkkk(0,y) and partial_k^6 S(0,y) are constants, because S_kk(0,y)=A0. Hence there are real constants B0,D0 and a smooth remainder E such that

    S=A0 k²/2+B0 k4/4+D0 k6/6+k8 E(k,y).        (3)

This follows by smooth division using evenness and the first six derivatives, including the vanishing odd seventh derivative. It holds with all mixed y derivatives, locally uniformly on compact y intervals. The coefficients obey S_kkkk=6B0 and partial_k^6 S=120D0.

In particular S_y=k8 E_y. The function S_k/k is nonzero near each axis point. The first identity of(2) therefore gives Q=k7 R1 with smooth R1 on such neighbourhoods. Substitute into the second identity and integrate from0 to y on a common small k strip containing the chosen compact axis segment. It gives

    aV=4A+C(k)+k6 R2(k,y), C(k)=W2(k,0).        (4)

There is one common smooth even germ C, with C(0)=0. This germ does not depend on the segment because every integration starts at0. Let

    c2=C''(0)/2, c4=C''''(0)/24,
    P(k)=c2 k²+c4 k4, D=4A+P.

Then C-P is smoothly divisible by k6. Define comparison fields in these coordinates by

    Vtilde=D/a, Wtilde1=k a'D/a,
    Stilde=A0 k²/2+B0 k4/4+D0 k6/6.

On each compact axis segment the differences satisfy

    W2-Wtilde2=O(k6), W1-Wtilde1=O(k7),
    Theta-Thetatilde=O(k8),                    (5)

with smooth divisible remainders. These comparison fields are not assumed sublinear or equal to the originals off the axis.

Physical derivatives are partial_x=a^-1 partial_k and partial_y|x=partial_y|k-k(a'/a)partial_k. Thus physical x differentiation lowers a remainder order by one while physical y differentiation preserves it. The curl difference is O(k5). Since W1 and Wtilde1 are O(k), their vorticity transport residuals differ by O(k5): the possibly order4 x derivative of the curl remainder is multiplied by O(k); all velocity-difference terms have at least order6; the temperature-source difference has order7. In particular the coefficients of k and k³ in the comparison vorticity residual are exactly zero. No condition on the coefficient of k5 is used, so the constant D0 will not enter the proof.

## 3. The common quadratic coefficient has a strict sign

Differentiating divergence gives W1_xy(0,y)=-phi''(y). Equation(4) fixes W2_xx(0,y)=2c2/a³. Hence eta=Omega_x(0,y)=-phi''-2c2/a³. Once differentiating the vorticity equation on the axis gives

    phi eta'+(5-phi')eta=A0/a².

With r=a eta and(1), this is phi r'+r=A0/a. Every backward trajectory y'=phi(y) stays in the compact interval between its starting point and0 and tends to0. Smoothness, positivity of a and boundedness of r on that interval justify

    r(y0)=A0 integral_-infinity^0 exp(s)/a(y(s)) ds>0.

The integrating-factor endpoint term vanishes by boundedness. Thus eta>0. If c2>=0, then phi''<0, so for y<0, phi'(y)>4 and phi(y)/y>4. This contradicts phi(y)/y->2 at the negative end. Therefore c2<0.

## 4. The two exact identities

Put B=a''/a-2a'^2/a². Differentiation of the comparison field gives

    Omegatilde=4k a'+k D B-(1+k²a'^2)P'/a².

Its first two coefficients are

    o1=4a'+4AB-2c2/a²,
    o3=c2B-4c4/a²-2c2 a'^2/a².

The comparison transport direction is D/a times partial_y at fixed k. By Section2, the k and k³ coefficients of its vorticity equation multiplied by a vanish, giving

    F1=4A o1'+a o1-A0=0,
    F3=4A o3'+c2 o1'+a o3-B0=0.               (6)

Write E1=-F1,E3=-F3. Direct expansion gives

    E1=-16A²a'''/a-36A a''+80A²a'a''/a²
       +40A a'^2/a-64A²a'^3/a³-4aa'
       +2c2/a-16c2A a'/a³+A0=0.              (7)

These are the same exact two identities used in P227, now derived from only finite temperature ratios. The following elimination and uniqueness argument is included to make the proof standalone. Its rational identities were independently checked in P227 and will be checked again as the specific dependency of this strengthening.

## 5. Finite elimination forces a'(0)=0

Write the smooth Taylor jet a(y)=1+r1 y+r2 y²+..., and put r=r1. In E1's coefficient of y^n the coefficient of the new r_(n+1) is -4(n+1)²(4n+1). This follows from the three terms -16A²a'''/a,-36Aa'',-4aa'; all other occurrences of r_(n+1) have higher order. It never vanishes. The constant term fixes A0=4r-2c2. In particular 2r-c2=A0/2>0. Solving the next coefficients gives

    r2=9r(2r-c2)/40,
    r3=r(128r-51c2)(2r-c2)/2160,
    r4=r(2r-c2)(6375c2²-60562c2r+44704r²)/4492800,
    r5=r(2r-c2)(-70125c2³+2822036c2²r-2726484c2r²+1392064r³)/1272960000.

The constant term of E3 fixes B0=-(c2²r+78c2r²+80c4)/20. Its y coefficient is

    -r(219c2³+6026c2²r+32c2r²+12960c4)/360.

If r!=0, this determines c4. After that substitution the y²,y³ coefficients of E3 are

    -c2 r³(2r-c2)P(c2/r)/1123200,
     c2 r4(2r-c2)Q(c2/r)/15466464000,

where

    P(t)=-130509t²+4496958t+12320,
    Q(t)=-405889875t³+30302578176t²+58633849676t+1213256384.

Their resultant is the nonzero integer

    Res(P,Q)=-50076093926441217209396936743211581440.

Therefore P,Q have no common root. Since c2<0, r!=0 and 2r-c2>0, the two zero coefficients would require a common root, a contradiction. Hence r=0 and c2=-A0/2.

## 6. Smooth uniqueness, without analyticity

The constant a=1,A=y solves E1 with c2=-A0/2. Its nonzero recursive coefficients imply every derivative of a-1 vanishes at0. This is only flatness. To prove local equality define for y!=0

    Z=(a,ya',y²a'',A/y), Z*=(1,0,0,1).

The fourth entry extends smoothly to0 as integral_0^1 a(ty)dt. Thus Z-Z* is smooth and flat. Multiplying(7) by y gives yZ'=F(y,Z), where

    N(y,Z)=-36z4z3+80z4²z2z3/z1²+40z4z2²/z1
       -64z4²z2³/z1³-4z1z2
       +y(2c2/z1-16c2z4z2/z1³+A0),
    F=(z2,z2+z3,2z3+z1 N/(16z4²),z1-z4).

This is smooth near Z*, and F(y,Z*)=0 for every small y because 2c2+A0=0. The mean value formula therefore yields yD'=M(y)D for D=Z-Z*, with M bounded by K on a small two-sided interval. If D(y1)!=0 at y1>0, linear uniqueness away from0 and integration of |d log||D||/dy|<=K/y imply

    ||D(y)||>=||D(y1)||(y/y1)^K, 0<y<=y1.

Flatness gives an upper bound C_m y^m for every integer m>K, a contradiction as y tends to0. The same argument after y=-t treats negative y. Consequently a=1 near0.

For every nonzero y, A has the sign of y, so the coefficient -16A²/a of a''' in E1 is nonzero. Together with A'=a, the equation is a regular smooth first-order system on A!=0,a>0. Ordinary uniqueness and continuation of the agreement set across finite points on each half-line now give a=1 everywhere. It follows that phi=4A/a=4y, contrary to phi(y)/y->2. The contradiction proves the theorem.

## Dependencies and limits

The new implication from constant finite ratios to the two vorticity identities is proved in Sections1-4 with exact remainder orders. The finite elimination and regular singular uniqueness are given completely in Sections5-6; P227 supplies an independently generated arithmetic record for the same identities. No theorem about asymptotic symbol bounds, inverse-tail integrals, analyticity, or global physical evolution is used. The all-plane inverse and gauge are not altered. The theorem does not assert the existence or nonexistence of a profile with varying ratios or an additional zero of Theta_xx.


## Entry-specific derivation and scope audit

The proposed common header contains all required smooth B2 identities. The assumption on Theta_xx permits the positive scale rho=sqrt(A/Theta_xx), after the reflection changes the sign of A if necessary. It does not impose a velocity value U(0)=0: W is the material relative transport field and W(0)=0 is required by the moving center. There is no reflection in y and no boundary at y=0.

In (a) the negation of the conclusion is exactly simultaneous vanishing of all specified even derivatives. Part A proves that this is impossible. For the class A statement, assuming all finitely many I_j constant and using the upper bound on rho forces each constant higher Taylor coefficient to vanish by a strict exponent gap. The main finite-symbol statement and the class A ratio corollary must not be conflated: only the latter uses the temperature symbol bounds.

In (b), assuming both ratios constant gives S=A*k^2/2+B*k^4/4+D*k^6/6+O(k^8). All O terms mean smooth divisibility, including all mixed y derivatives on each compact axis interval. The constant sixth-order temperature coefficient contributes to S_k only in degree five. Since Q=O(k^7), the true velocity differs from its quartic comparison by orders6 and7, its vorticity by order5, and its residual by order5. Thus the first and third coefficients of rho*(W.gradOmega+Omega) agree with those of the comparison field. The fourth and sixth temperature derivatives determine B and D, but D cannot enter E1 or E3. The expansion cited in4.7(xxiv) is therefore valid modulo O(k^5), exactly as the entry says. No fifth-order equation is asserted.

The counterexample W=(0,4y+c(x)), Theta=-c(x), Omega=-c'(x) for an even polynomial c with c(0)=0 and c''(0)<0 has divW=4 and Omega=-curlW. Both scalar fields depend only on x, so W.gradTheta=W.gradOmega=0 and Omega=Theta_x. Parity, the center, the nonzero quadratic jet and nonvanishing axis Theta_xx all hold; the ratios are constants. However W2(0,y)/y=4 rather than2, so it violates the required sublinearity. The earlier independent nine-control polynomial instance in P231 confirms these identities. It is not an admissible profile.

If Theta=H(x/rho(y)) on an open neighbourhood of the entire axis with arbitrary initially unregular rho>0 and H, the y=0 slice gives a smooth germ of H at0. At every y, differentiation in x gives Theta_xx=H''(0)/rho^2!=0 and I_j=H^(2j)(0)/H''(0)^j, constant. Hence (a)'s class A corollary contains4.40(b), and (b) contains4.7(xxiv). No uniform neighbourhood width or analyticity is needed. A zero of Theta_xx or variable ratios is not excluded by these results.

For the entry controls, freeze the actual report after4.40 and its timeline. Independently insert the full Z1 text after4.40, perform exactly the five Z2-Z6 replacements, add the stated table row, and insert the new timeline entry in chronological order. Compare the entire normalized text and preserve every older timeline entry. The future lead apply.py is static reference data and must not be executed. The chained preview retains placeholders for4.40 and is not the final submitted base.

The source P230 proof was written00:09, its81 exact controls ran00:10, and confirmation occurred00:13. P231 was written00:14, its32 controls ran00:15 to00:16, and confirmation occurred00:18. Lead A149/A150 report VALID with64/37 separate checks. Their attempted Opus credential retrieval failed before inference; actual verifier Opus453/454 returned no written audit. Neither is an Opus endorsement.

## Entry verdict

CONFIRMED. All92 independent controls pass, including an exact complete normalized assembly of the eight changes and preservation of all137 older timeline entries plus one new entry. The full text SHA256 is 52ec7c79f0e6a07889737d18254ebab0c40e0b51b67dee28288566b0d1ba8e91; the complete preview SHA256 is 1ebac043e7bb0b5ab4fd3eb79b02d54281addcf78c50ac1d3bfcfd6e1f88a3b9. Verification interval: 00:35 to 00:37 UTC on2026-10-22. No source repair is required. The sufficient-order wording is accurate and does not claim optimality. Actual insertion is pending.
