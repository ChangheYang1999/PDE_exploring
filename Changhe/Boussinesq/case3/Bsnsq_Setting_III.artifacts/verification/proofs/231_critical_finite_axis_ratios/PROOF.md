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
