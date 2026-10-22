# Independent audit of the lead's local vorticity route

## Exact statement, status and dependencies

Consider a smooth B2 profile at beta=2 on the full plane, W=2X+U-U(0), with div U=0, U=o(|X|) globally at infinity, Omega=-curl U, W.grad Theta=0 and W.grad Omega+Omega=Theta_x. The B2 reflection symmetry is explicitly assumed: W1 is odd in x, W2 is even in x, Omega is odd in x, and Theta is even in x. Suppose Theta(0,y)=0 and Theta=a0 x²+O(|X|³) near zero, a0!=0. All small-o conditions here are limits at spatial infinity. A representation Theta(x,y)=H(x/rho(y)) for all x,y with arbitrary functions H:R->R and rho:R->(0,infinity) is impossible.

This statement follows already from the complete P225 theorem after the regularity argument below. This packet additionally audits the different lead route in work/sepV/NOTES.md. Its finite elimination identities in Section5 have been independently recomputed by exact arithmetic; no finite-jet identity is inferred from floating-point samples. The controls are distinct from the mathematical uniqueness argument. No formal build is attempted. General B2 temperatures need not have the representation and remain outside this result.

## 1. Smoothness, parity and normalization

Put rho0=rho(0)>0. Evaluation at y=0 gives H(k)=Theta(k rho0,0); hence H is smooth and even and H''(0)=2a0 rho0²!=0. At every fixed y, differentiation in x is legitimate without initial regularity in y of rho, since rho(y) is a fixed positive number. It gives Theta_xx(0,y)=H''(0)/rho(y)². Therefore rho(y)=sqrt(H''(0)/Theta_xx(0,y)) is smooth and positive on the entire real line. The ratio is positive even if both numerator and denominator are negative. This argument also works without parity if the specified quadratic jet is retained.

To make rho(0)=1 set a(y)=rho(y)/rho0 and h(k)=H(k/rho0). Then h(x/a(y))=H(x/rho(y)), h''(0)=2a0. The lead's original Step0 writes H(k rho0); that rescaling is incorrect unless rho0=1 or H has exceptional scale invariance. The inverse factor is necessary. In what follows rename h as H, with A0=H''(0)=2a0.

One can arrange A0>0 using the legitimate B2 reflection. For S(x,y)=(x,-y), define Wnew(X)=S W(SX), Thetanew(X)=-Theta(SX), Omeganew(X)=-Omega(SX). Direct chain differentiation gives div Wnew=4, negative curl Wnew=Omeganew, and both profile equations, with the vorticity source -Theta_x(SX) matching. Also Wnew(0)=0 and Wnew=2X+o(|X|). The representation transforms by anew(y)=a(-y), Hnew=-H. Thus a0 changes sign, and no center velocity is artificially set to zero. Assume henceforth A0>0.

## 2. Regular strip and axis positivity

Set k=x/a(y) and A(y)=integral_0^y a. Define V(k,y)=W2(ka(y),y), Q=W1(ka(y),y)-k a'(y)V. Since H'(k)=A0 k+O(k³), H'!=0 for 0<|k|<epsilon. The exact coordinate identities are

    W.grad Theta=H'Q/a,  Q_k+(aV)_y=4a.

Thus Q=0 on the punctured strip and, by smoothness, on the whole strip. Since a(0)=1,

    C(k)=W2(k,0),  D(k,y)=4A(y)+C(k),
    W2(ka,y)=D/a,  W1(ka,y)=k a'D/a.

B2 parity makes C even and W(0)=0 gives C(0)=0. Write C(k)=c2 k²+c4 k4+O(k6). Set phi(y)=W2(0,y)=4A/a. Since a>0, phi has exactly one zero at0, has the sign of y, and phi'(0)=4. On the axis, div W gives W1_x=4-phi'. Consequently

    q(y)=Omega_x(0,y)=-2c2/a³-phi''.

Differentiate the vorticity equation in x at x=0, using W1=0 and Omega=0 there. One obtains

    phi q'+(5-phi')q=A0/a².                        (2.1)

This can also be checked directly from the strip formula. Let r=a q and p=a'phi/a. Since phi'=4-p, (2.1) becomes

    phi r'+r=A0/a.                                (2.2)

For any initial y0, the backward trajectory y'=phi(y) remains in the compact interval between0 and y0 and tends to0 as time goes to negative infinity. Local uniqueness and the sign of phi justify compactness and prevent crossing0; boundedness on this interval prevents finite backward blowup. Multiplying (2.2) along it by exp(s), integrating and using boundedness of r on the compact interval gives

    r(y0)=A0 integral_{-infinity}^0 exp(s)/a(y(s)) ds>0.

The integral converges because a has a positive minimum on that interval. At y0=0 this includes the constant trajectory. Thus q>0 globally. This supplies an independent proof of the lead's invocation of 4.13(i), including its infinite endpoint case.

## 3. The sign c2>=0 is impossible

If c2>=0, q>0 gives phi''=-q-2c2/a³<0. For y<0, phi'(y)>phi'(0)=4, so phi(y)=-integral_y^0 phi'(t)dt<4y and phi(y)/y>4. The global velocity asymptotic on the axis instead gives phi(y)/y->2 as y->-infinity. Hence c2<0.

## 4. Independent derivation of the vorticity identities

At fixed (k,y), let B=a''/a-2a'^2/a². Physical derivatives are partial_x=a^-1 partial_k and partial_y|x=partial_y|k-(ka'/a)partial_k. Applying them to the strip field gives

    Omega(ka,y)=4k a'+k D B-(1+k²a'^2)C'/a².       (4.1)

Since Q=0, the vorticity equation multiplied by a is

    D partial_y|k Omega+a Omega=H'(k).             (4.2)

For comparison with the lead, set a1=a^-2, a2=a'^2/a², a3=-4AB-4a'=a phi'', a4=-B and L(f)=4A f'+a f. Equation(4.1) is -C'a1-k²C'a2-k a3-k C a4. Substitution in (4.2) yields the lead structural expression with its overall minus sign:

    a(W.grad Omega+Omega)
     =-[C'L(a1)+k²C'L(a2)+k L(a3)+k C(L(a4)+a3')
         +CC'a1'+k²CC'a2'+k C²a4'].

No field or residual is sampled to derive this identity. To implement independent coefficient controls, use (4.1) directly instead of the lead's a_i decomposition. Its first two odd coefficients are

    o1=4a'+4AB-2c2/a²,
    o3=c2 B-4c4/a²-2c2 a'^2/a².

Write H'(k)=A0 k+B0 k³+O(k5). Then

    F1=4A o1'+a o1-A0=0,
    F3=4A o3'+c2 o1'+a o3-B0=0.                   (4.3)

The lead quantities E1,E3 are -F1,-F3 respectively. Expansion gives

    E1=-16A²a'''/a-36A a''+80A²a'a''/a²
       +40A a'^2/a-64A²a'^3/a³-4aa'
       +2c2/a-16c2A a'/a³+A0=0.                 (4.4)

The relation to the axis equation is E1=-a²[phi q'+(5-phi')q-A0/a²], since o1=a q and 4A=a phi. These identities check the sign and powers of a independently.

## 5. Finite-jet elimination, independently checked

The following lead coefficients were recomputed from (4.3) with independently implemented truncated polynomial convolution and reciprocal recurrence. For a(y)=1+r1 y+r2 y²+..., the coefficient multiplying r_(n+1) in E1_n is

    -4(n+1)²(4n+1).

Indeed the only terms of (4.4) involving that highest new derivative at order y^n are -16A²a''', -36A a'' and -4aa'. For m=n+1 their contributions sum to -16m(m-1)(m-2)-36m(m-1)-4m=-4m²(4m-3). All other terms with r_m have higher y order, because A has a simple zero and a(0)=1. This coefficient is nonzero for every integer n>=0. Thus E1_0 fixes A0=4r1-2c2 and all higher jets are recursively determined by r1,c2.

The independently recovered low coefficients are r2=9r1(2r1-c2)/40 and r3=r1(128r1-51c2)(2r1-c2)/2160. E3_0 determines B0. E3_1 is exactly

    -r1(219c2³+6026c2²r1+32c2r1²+12960c4)/360.

If r1!=0 it fixes c4. With t=c2/r1, the next coefficients are

    E3_2=-c2 r1³(2r1-c2)P(t)/1123200,
    E3_3= c2 r1⁴(2r1-c2)Q(t)/15466464000,
    P(t)=-130509t²+4496958t+12320,
    Q(t)=-405889875t³+30302578176t²+58633849676t+1213256384.

The independently computed resultant Res(P,Q) is -50076093926441217209396936743211581440. An exact rational Bezout identity is recorded in verification/checks.json and independently simplified to 1. Thus the resultant is nonzero and P,Q have no common complex root. Here c2<0 and 2r1-c2=A0/2>0. Consequently these two identities prohibit r1!=0. The conclusion is r1=0, c2=-A0/2. No analyticity of a is assumed or inferred from these finite jets.

## 6. Complete singular uniqueness argument after elimination

Assume the preceding exact identities hold and r1=0. Then a=1,A=y solves E1 with c2=-A0/2. The nonzero recursive coefficients show that every derivative of a-1 at0 vanishes. This proves flatness, not local equality. Equality follows by the following regular singular argument, supplied explicitly to avoid an unjustified analytic-series step.

For y!=0 define Z=(z1,z2,z3,z4)=(a,y a',y²a'',A/y). The fourth component extends smoothly to y=0 by A(y)/y=integral_0^1 a(ty)dt; hence Z(0)=Z*=(1,0,0,1). Define

    N(y,Z)=-36z4z3+80z4²z2z3/z1²+40z4z2²/z1
           -64z4²z2³/z1³-4z1z2
           +y(2c2/z1-16c2z4z2/z1³+A0).

Multiplying E1 by y gives y³a'''=z1 N/(16z4²). Therefore

    yZ'=F(y,Z)=(z2,z2+z3,2z3+z1 N/(16z4²),z1-z4).

This F is smooth for z1,z4 near1. Crucially F(y,Z*)=0 for every small y, since 2c2+A0=0, not merely at y=0. By the integral mean value formula D=Z-Z* satisfies yD'=M(y)D, with

    M(y)=integral_0^1 partial_Z F(y,Z*+tD(y))dt

bounded in norm by some K on a small two-sided interval. All components of D are flat; this includes A/y-1 by its integral formula.

Fix a small y1>0. If D(y1)!=0, ordinary uniqueness for this linear equation away from0 gives D(y)!=0 for0<y<=y1. Differentiating its Euclidean norm yields |d log||D||/dy|<=K/y. Integrating from y to y1 gives ||D(y)||>=||D(y1)||(y/y1)^K. Flatness gives ||D(y)||<=C_N y^N for any integer N>K and sufficiently small y. The two estimates contradict each other as y->0. Thus D is zero near0 on the positive side. The negative side follows by replacing y by -t, obtaining t dD(-t)/dt=M(-t)D(-t) and the identical estimate. Hence a=1 and A=y near0.

Finally, for every nonzero y the positivity of a implies A has the sign of y, so the coefficient -16A²/a of a''' in E1 is nonzero. Together with A'=a, E1 is a regular first-order system for (A,a,a',a'') on A!=0,a>0 with smooth right-hand side. The existing solution and the constant-scale solution agree on an interval in each half-line. Uniqueness extends agreement through every finite point of either half-line: the agreement set is open by local uniqueness and closed by continuity, within each connected half-line. Thus a=1 on all R. But phi=4A/a=4y, contrary to phi=2y+o(|y|). This proves the candidate by the local route with Section5 arithmetic checked exactly.

## 7. Independent application of the established foliation theorems

Independently of the local elimination, Section1's regularity argument proves that any smooth B2 field with a nonzero quadratic jet and an arbitrary global representation has smooth positive scale and smooth nonconstant H. At beta2 these meet every assumption of P225. At beta>2 they meet P226: H(0)=H'(0)=0, H''(0)!=0, W(0)=0, div W=2beta and W=betaX+o(|X|). Hence the combination P225/P226 excludes such globally separated representations for every beta>=2. This application assumes the exact hypotheses of the respective standalone theorems; it asserts nothing about a general even Theta=x²F(x²,y) with independent x² and y dependence.

No numerical profile is used as proof. No statement about finite-box roots, canonical inverse cancellation, or the unrestricted slow-tail endpoint follows from this restricted representation result.

## Verification completion

The independent checker completed 2026-10-21T23:41:57.083393+00:00 to 2026-10-21T23:42:03.325545+00:00 in 6.242174 seconds with all 53 controls passing. It used no lead or numerics code. The pre-check proof is retained in verification/PROOF_before_arithmetic_completion.md. The exact further jets are

    r4=r*(-c2 + 2*r)*(6375*c2**2 - 60562*c2*r + 44704*r**2)/4492800,
    r5=r*(-c2 + 2*r)*(-70125*c2**3 + 2822036*c2**2*r - 2726484*c2*r**2 + 1392064*r**3)/1272960000,

where r denotes r1. The coefficient B0 is -(c2**2*r + 78*c2*r**2 + 80*c4)/20. The c4 formula is used only in the r1!=0 branch; no constraint on c4 is inferred from E3_1 when r1=0. The proof's status change was recorded 2026-10-21T23:42:50.637005+00:00.


## 8. Strengthening to an arbitrary neighbourhood of the entire axis

Assume now only that N is an open neighbourhood of {x=0}, rho:R->(0,infinity), H is defined on an interval about0 containing every value x/rho(y) for (x,y) in N, and Theta(x,y)=H(x/rho(y)) at every point of N. Keep the smooth B2 hypotheses of the opening statement. This is impossible at beta2. The following argument explains why Sections1-6 still apply even though there need not be a globally uniform strip width.

First choose a small interval on the slice y=0 contained in N. There H(k)=Theta(k rho0,0) proves H is smooth and even near0 with H''0=2a0rho0²!=0. At each fixed y, openness of N supplies an interval of x about0 on which the representation holds. Differentiating only in x at that fixed y gives Theta_xx(0,y)=H''0/rho(y)². Hence rho is smooth everywhere by exactly the positive-ratio formula of Section1. Normalize rho0 by the corrected inverse-factor rescaling and, if needed, reflect y and Theta. The rescaling changes only the representing functions and leaves the physical neighbourhood N unchanged. The reflection maps N to S N, another open neighbourhood of the entire axis, and preserves the B2 parities and the global velocity asymptotic, as verified in Section1. No uniform initial neighbourhood width or continuity of rho was assumed in this bootstrap.

Now let a denote the normalized rho and let Phi(k,y)=(ka(y),y), a smooth global coordinate map. The preimage Phi^{-1}(N) is open and contains {0} times R. For any finite Y>0, the segment {0} times [-Y,Y] is compact and disjoint from the closed complement. It has positive distance from that complement, unless the complement is empty, in which case any small distance works. Choose epsilon_Y>0 less than half that distance, less than the common interval on which H is defined and smooth, and within the punctured interval where H'!=0. Then all points with |k|<=epsilon_Y and |y|<=Y belong to Phi^{-1}(N). Choosing a smaller width if necessary leaves an open neighbourhood of this closed rectangle, so derivative identities at its horizontal edges are also legitimate.

On this rectangle, the temperature equation gives Q=0 for nonzero k and continuity gives Q=0 at k=0. The divergence identity gives (aV)_y=4a. Integrating from y=0 to any y in [-Y,Y] remains inside the rectangle. Thus aV=4A+C(k), with the SAME C(k)=a(0)W2(ka(0),0)=W2(k,0) for every Y. It is not an independently adjustable constant on successive compact intervals. Consequently all its derivatives at k=0, including c2 and c4, are the same at every height.

For any fixed y choose Y>|y|. Physical derivatives and k derivatives of the field identities at that y are valid in an open strip. The axis formula, positivity equation, exact E1,E3 and every coefficient used in Sections2-6 therefore hold at this y. Since y was arbitrary they hold along the entire axis. Those sections use no horizontal limit: their asymptotic inputs are solely phi(y)/y->2 on the two axis ends. Thus the same exact elimination and singular/ordinary uniqueness argument gives a=1 globally and phi=4y, the same contradiction.

This proves the neighbourhood statement. An arbitrary neighbourhood of only a bounded axis segment is not enough: compact choices there give E1/E3 only over that segment, and there is no access to the negative-axis asymptotic or global ordinary uniqueness. The statement uses the exact representation near the entire axis, not merely a matching finite jet. P225 is an independent proof of the GLOBAL representation corollary only; its horizontal-infinity argument is not a proof of this neighbourhood strengthening. P226 also remains in its global-representation scope.

For the lead's entry text, M1 follows from the preceding compact argument, M2 from Section1 and its local bootstrap here, M3 from Sections2-3, M4 from Sections4-6 and the exact53 controls, and M5 from the exact neighbourhood/global distinction above. The missing explicit identity F(y,Z*)=0 in the short proof outline is justified in full in Section6; adding it would make the outline easier to audit. The original wrong rescaling is corrected in entry v1.
