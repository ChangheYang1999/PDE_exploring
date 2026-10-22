# Finite axis-jet obstructions on the component containing the center

## Exact setting and statements

Let beta>=2. Let W,Theta,Omega be smooth real fields on R^2 satisfying

    div W=2beta, Omega=partial_y W1-partial_x W2,
    W(0)=0, W(X)=beta X+o(|X|) uniformly at infinity,
    W.gradTheta=(beta-2)Theta, W.gradOmega+Omega=Theta_x.

Assume W1,Omega odd in x and W2,Theta even in x, Theta(0,y)=0, and Theta(x,y)=a0*x^2+O(|X|^3) at0 with a0!=0. Put H(y)=Theta_xx(0,y), phi(y)=W2(0,y), and let J=(y_-,y_+) be the component of {H!=0} containing0. Put I_j=partial_x^(2j)Theta(0,y)/H(y)^j on J. No condition on H outside J is imposed.

(E) The finite endpoints of J are exactly the nearest additional zeros of phi on the corresponding half-axes. Thus J is unbounded if and only if phi has no zero on at least one open half-axis.

(B) If beta=2, I2 and I3 cannot both be constant on J.

(A) If beta>2, put N=2 floor(3beta/(2(beta-2))) and M=2N+4. Suppose J is unbounded and, at one infinite end of J, for every even j=N+2,N+4,...,2N+2,

    |partial_x^j W2(0,y)|<=D_j |y|^(1-1/beta-j)

for all sufficiently large |y| in J. It is impossible that every even derivative partial_x^j Theta(0,y), j=4,6,...,M, vanish identically on J. If in addition the temperature bounds

    |partial_x^ell Theta(0,y)|<=C_ell |y|^(1-2/beta-ell), ell=4,6,...,M,

hold at that infinite end, then at least one of I2,...,I_(N+2) is nonconstant on J. The previously independently verified class A symbol theorem supplies these hypotheses. Its hypotheses and implication are recorded in P229 Section9. The main conditional statements here do not require that theorem.

This full argument is written before new controls. It strengthens P230/P231 and independently audits the lead's z441 note. General B2, bounded J at beta>2, and varying ratios remain outside these exclusions.

## 1. Axis component and finite ends

For R(x,y)=(x,-y), Wnew(X)=R W(RX), Thetanew(X)=-Theta(RX), Omeganew(X)=-Omega(RX) preserve the equations and every hypothesis, including end bounds. This takes J to -J and I_j(y) to (-1)^(j+1)I_j(-y), preserving constancy and unboundedness while reversing a0. Assume A0=H(0)>0. Continuity gives H>0 on J. Define a=(A0/H)^(1/2), a(0)=1, A(y)=integral_0^y a, and L=1+3beta/2.

Twice differentiating temperature transport on the axis and using parity and divergence gives on all of R

    phi H'+(3beta+2-2phi')H=0.                    (1)

On J this is (a phi)'=L a. Since phi(0)=0, phi=L A/a, so phi has the sign of y on J and phi'(0)=L. If y_* is a finite endpoint, H(y_*)=0 by continuity and maximality. If phi(y_*)!=0, (1) is a regular homogeneous first-order linear ODE near y_*, whose zero initial value forces H=0 there, contradicting H>0 just inside J. Hence phi(y_*)=0 and a->infinity at every finite endpoint. No nonzero zero of phi lies inside J. Any nearest nonzero zero must therefore be an endpoint: if a preceding finite endpoint existed it would be a nearer zero, and an infinite J endpoint would contain the proposed zero in J. This proves(E).

At an infinite end, sublinearity gives phi(y)/y->beta. From A'=a and phi=L A/a, y A'/A->L/beta=3/2+1/beta. Integrating logarithmic derivative inequalities gives, for gamma=1/2+1/beta and every sufficiently small epsilon>0,

    c |y|^(gamma-epsilon)<=a(y)<=C |y|^(gamma+epsilon).   (2)

At a negative end use -A(-t), a(-t), t>0. No asymptotic derivative is taken. For beta>2, gamma<1 and a tends to infinity at that end.

## 2. Coordinates and the common coefficient's strict sign

Put k=x/a(y), S=Theta(ka(y),y), V=W2(ka(y),y), Q=W1(ka(y),y)-k a'(y)V. The exact identities are

    (Q/a)S_k+V S_y=(beta-2)S,
    Q_k+(aV)_y=2beta a.                         (3)

All remainders mean smooth divisibility by the stated power of k on sufficiently small strips over compact subintervals of J containing0. Integration from0 to y gives one common even germ C(k)=W2(k,0), C(0)=0.

In(A), vanishing derivatives and parity give S=A0 k^2/2+O(k^(M+2)); smooth division by S_k/k in(3) gives Q=a alpha k+O(k^(M+1)), alpha=(beta-2)/2, and aV=L A+C+O(k^M). In(B), constancy of the ratios gives S=A0 k^2/2+B0 k^4/4+D0 k^6/6+O(k^8), where B0,D0 are constants (the corresponding derivatives are6B0,120D0). Then S_y=O(k^8), Q=O(k^7), and aV=4A+C+O(k^6).

In both cases W2_xx(0,y)=2c2/a^3 exactly, where c2=C''(0)/2. Divergence and negative curl give eta:=Omega_x(0,y)=-phi''-2c2/a^3. The differentiated vorticity equation and r=a eta yield

    phi eta'+(2beta+1-phi')eta=A0/a^2,
    phi r'+(beta/2)r=A0/a.                       (4)

The backward orbit of y'=phi(y) through y0 in J remains between y0 and0 and tends to0. This compact interval is inside J. Boundedness of r and1/a and the integrating factor exp(beta*s/2) give

    r(y0)=A0 integral_-infinity^0 exp(beta*s/2)/a(y(s)) ds>0.

The endpoint term vanishes. At0, (beta/2)r(0)=A0. Thus eta>0 on J. If c2>=0 then phi''<0. If y_-=-infinity, phi'(y)>L for y<0 gives phi(y)/y>L>beta, contradicting sublinearity. If y_- is finite, phi is concave on(y_-,0), continuous on its closure, and zero at both endpoints, so phi>=0 above the zero chord. This contradicts phi<0 there. Hence

    c2<0                                                     (5)

for every J. The finite-end concavity alternative avoids assuming a negative infinite end.

## 3. Supercritical finite-jet reduction

Assume the forbidden vanishing in(A). The coordinate expansion gives partial_x^j W2(0,y)=C^(j)(0)/a^(j+1) for1<=j<M. For even j=N+2,...,2N+2, a nonzero C^(j)(0) conflicts with(2) and the velocity bound: the lower-power versus upper-power gap is j(1/2-1/beta)-3/2-(j+1)epsilon>0 for sufficiently small epsilon. The first two terms have positive sum by the definition of N. These derivatives therefore vanish. Odd derivatives vanish by parity. The Taylor polynomial P of C through degree N satisfies C-P=O(k^M); by(5) its highest nonzero degree n is even with2<=n<=N.

Put D=L A+P(k), Wtilde2=D/a, Wtilde1=a alpha k+k a'D/a, and Thetatilde=A0 k^2/2. Differences from W2,W1,Theta have orders M,M+1,M+2 respectively. Physical x differentiation is a^-1 partial_k and lowers the order once; physical y differentiation is partial_y|k-k(a'/a)partial_k and preserves it. Thus Omega-Omegatilde=O(k^(M-1)). Since both first velocity components are O(k), the vorticity residuals agree modulo O(k^(M-1)). Let B=a''/a-2(a'/a)^2. Direct differentiation gives

    Omegatilde=L k a'+kD B-(1+k^2 a'^2)P'/a^2,
    R=a alpha k Omegatilde_k+D Omegatilde_y|k+a Omegatilde-A0 k.

R is the comparison vorticity residual multiplied by a. It has degree at most2N+1 but order at least M-1=2N+3, hence is identically zero as a polynomial for each y in J. This is finite polynomial algebra, not analytic continuation or equality of the original and comparison fields off the axis.

For p=a'/a and P's leading coefficient p_n, the coefficient of k^(2n+1) in R is p_n^2[p''-2(n+1)p p']; only P times the derivative in y of the highest vorticity term contributes. It follows that p'-(n+1)p^2=K is constant on J. Therefore v=a^(-(n+1))>0 satisfies

    v''+(n+1)K v=0.                              (6)

If J has a finite endpoint y_*, then v=(H/A0)^((n+1)/2)->0 and

    v'=((n+1)/2)(H/A0)^((n-1)/2)H'/A0 ->0,

because n>=2 and H' is bounded near y_*. The solution of(6) through an interior point extends to R and equals v on J by uniqueness. Its value and derivative at y_* are zero, forcing it to vanish identically, contradiction. If J has no finite endpoint, J=R and(2) gives v->0 at both ends. The affine(K=0), trigonometric(K>0), or exponential(K<0) solution formula then forces v=0, again a contradiction. This proves(A).

For its ratio corollary, a constant I_(ell/2) means partial_x^ell Theta=h_ell/a^ell for constant h_ell. At the infinite end, (2) and the temperature symbol bound have strict exponent gap (ell/2-1)(1-2/beta)-ell*epsilon>0 for sufficiently small epsilon and every even ell>=4. Thus every h_ell must vanish. If all the stated ratios were constant, the forbidden derivatives would all vanish on J. A bounded J supplies no infinite-end reduction of C to P, so this argument gives no bounded-J theorem.

## 4. Critical finite-ratio reduction

Suppose beta=2 and I2,I3 constant. Write P=c2 k^2+c4 k^4, D=4A+P, and compare with Wtilde2=D/a, Wtilde1=k a'D/a, Thetatilde=A0 k^2/2+B0 k^4/4+D0 k^6/6. By Section2 the differences of W2,W1,Theta have orders6,7,8. The vorticity residuals therefore agree modulo O(k^5). Their k,k^3 coefficients vanish exactly; the k^5 coefficient is uncontrolled. With B=a''/a-2a'^2/a^2 the first coefficients of Omegatilde are

    o1=4a'+4AB-2c2/a^2,
    o3=c2B-4c4/a^2-2c2 a'^2/a^2.

Comparison transport is D/a times partial_y at fixed k. Hence, setting F1=4A o1'+a o1-A0 and F3=4A o3'+c2 o1'+a o3-B0, one has E1=-F1=0 and E3=-F3=0. The complete local elimination and smooth uniqueness argument is reproduced in the appendix. It uses only these identities, c2<0, A'=a, a(0)=1, A(0)=0, A0>0, and proves a=1 near0.

Away from0 in J, A!=0 and a>0. The coefficient of the third derivative of a in E1 is -16A^2/a, so E1 with A'=a is a regular smooth first-order system. Ordinary uniqueness extends agreement with(a,A)=(1,y) over every compact subinterval of either half of J. Thus a=1 and H=A0 throughout J. A finite endpoint contradicts continuity and H(y_*)=0. If neither endpoint is finite, J=R and phi=4y contradicts phi/y->2. This proves(B).

## 5. Dependencies and limits

The component and endpoint arguments are proved above. The appendix reproduces the verifier's own local calculation from P231, which had32 exact controls and a separately checked37-control lead review. The supercritical algebra is reproduced from the verifier's own P230 argument, which had81 controls and a separately checked64-control lead review. No lead or NUM code is executed; the lead's seven checks are not assumed correct. The class A corollary uses the exact symbol theorem dependency documented in P229 Section9. All other claims use only the explicitly stated differential equations and sublinearity.

No separated representation or analyticity is assumed. The inverse and gauge are never modified. Beta2 now permits zeros of H outside J. At beta>2 an infinite end is still a material hypothesis. General B2 is OPEN.

## Appendix: complete local critical elimination and smooth uniqueness

Write E1=-F1,E3=-F3. Direct expansion gives

    E1=-16A²a'''/a-36A a''+80A²a'a''/a²
       +40A a'^2/a-64A²a'^3/a³-4aa'
       +2c2/a-16c2A a'/a³+A0=0.              (7)

These are the same exact two identities used in P227, now derived from only finite temperature ratios. The following elimination and uniqueness argument is included to make the proof standalone. Its rational identities were independently checked in P227 and will be checked again as the specific dependency of this strengthening.

### Finite elimination forces a'(0)=0

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

### Smooth uniqueness, without analyticity

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


The appendix is entirely local near0. Its last conclusion is used on J in Section4.
