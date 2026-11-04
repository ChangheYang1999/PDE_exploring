# Fixed-target ambient inverse-radius counterexamples

## 1. Exact claim and dependencies

For every integer k>=1 and every real C>1/4 there exist R>0 and a map u in C-infinity(B_R in C^k;C^(2k)) which is nonzero at each point except zero, has every real derivative zero at zero, and obeys

    |partial_bar u(z)| <= C |u(z)|/|z|,  0<|z|<R.

Here partial_bar_j=(partial_xj+i partial_yj)/2, and the norm on the left is the Euclidean norm of all target and source components. Appending zero coordinates gives every prescribed finite target N>=2k. This statement makes no assertion for smaller targets. The proof uses a smooth step, finite-sum Holder and Jensen inequalities, and differentiation. It does not use the pending finite-cover construction LIT356. The sharpness comparison in Section6 separately imports confirmed LIT354.

## 2. Cutoffs and power vectors

Choose a smooth nondecreasing step chi which is zero for s<=1/4 and one for s>=3/4. Integrate and normalize a nonnegative smooth bump positive on (1/4,3/4) to obtain it. Let Mchi=max chi', D=3pi Mchi/2, and for 0<=tau<=1 define

    theta(tau)=(pi/2)chi(3tau-1),
    nu(tau)=(1/2)chi(4tau)+(1/2)chi(4tau-3).

Both vanish near zero; near one they are pi/2 and one respectively. The first term of nu transitions on (1/16,3/16), and the second on (13/16,15/16). Hence nu=1/2 throughout [1/4,3/4]. The angle transitions on (5/12,7/12), contained strictly in that interval. In particular theta=0 on [0,1/3], theta=pi/2 on [2/3,1], and 0<=theta'<=D. Before tau=1/4, theta=0 and 0<=nu<=1/2; after tau=3/4, theta=pi/2 and 1/2<=nu<=1.

Fix L>0 large enough that 1/4+sqrt(k)D/(2L)<C. Put R=exp(-L). For n>=1 let P_n(z)=(z_1^n,...,z_k^n), Q_n(z)=|z|^(-n)P_n(z). For a unit direction zeta define a_n=|P_n(zeta)|, x_j=|zeta_j|^2 and S_n=sum_j x_j^n. Since sum_j x_j=1, Jensen gives S_n>=k^(1-n), and x_j^n<=x_j gives S_n<=1. Holder gives

    S_n <= S_(n+1)^(n/(n+1)) k^(1/(n+1)).

Thus S_(n+1)/S_n>=k^(-1/n) S_n^(1/n)>=1/k. The same ratio is at most one because each x_j is in [0,1]. Therefore

    k^((1-n)/2)<=a_n<=1,
    1/sqrt(k)<=a_(n+1)/a_n<=1.

No vector P_n vanishes in a punctured direction, and the ratio estimates are uniform in n and direction. The target consists of two copies of this fixed k-dimensional space.

## 3. Envelope and exact residual

For t in [nL,(n+1)L], set tau=(t-nL)/L, theta_n(t)=theta(tau), nu_n(t)=nu(tau), and define F(L)=0, F'=n+nu_n. On a neighborhood of a join both slopes equal n+1, so the continuous primitive is smooth. Higher derivatives of F are bounded uniformly in n; F'=O(1+t). Integrating t/L-1<=F'<=t/L+1 gives

    F(t)>=(t^2-L^2)/(2L)-(t-L).

Let iota_0 and iota_1 be the orthogonal inclusions C^k into C^(2k), and j_n the parity of n. For r=|z| and t=-log r, define on the nth interval

    Z=cos(theta_n)iota_(j_n)Q_n+sin(theta_n)iota_(j_(n+1))Q_(n+1),
    u(z)=exp(-F(t)) Z.

Its squared norm is exp(-2F)(cos^2(theta_n)a_n^2+sin^2(theta_n)a_(n+1)^2)>0.

Since Q_n=exp(nt)P_n and P_n is holomorphic, direct differentiation gives partial_bar u as the outer product of partial_bar t with exp(-F) times

    A=(-nu_n cos(theta_n)-dot(theta_n)sin(theta_n))iota_(j_n)Q_n
       +((1-nu_n)sin(theta_n)+dot(theta_n)cos(theta_n))iota_(j_(n+1))Q_(n+1).

The dot is a t derivative. The full radial source norm is exact:

    partial_bar_j t=-z_j/(2r^2),
    sum_j |partial_bar_j t|^2=1/(4r^2),
    |partial_bar u|=exp(-F)|A|/(2r).

Thus no extra dimension factor enters the derivative array. This is an ambient-radius estimate, rather than a bound involving only one coordinate modulus.

## 4. Estimate on all parts of every annulus

On [1/4,3/4], nu_n=1/2. Decompose A=A0+dot(theta_n)W, where A0 has the two coefficients -cos(theta_n)/2 and sin(theta_n)/2, and W has coefficients -sin(theta_n) and cos(theta_n). Orthogonality gives |A0|=|Z|/2 exactly. With q=a_(n+1)/a_n,

    |W|^2/|Z|^2
      =[sin^2(theta_n)+q^2 cos^2(theta_n)]
        /[cos^2(theta_n)+q^2 sin^2(theta_n)] <= k.

Indeed the numerator is at most one and the denominator at least q^2>=1/k. The triangle inequality yields |A|<=(1/2+sqrt(k)D/L)|Z|. Before tau=1/4 the angle and its derivative vanish, so A=-nu_n iota_(j_n)Q_n and |A|<=|Z|/2. After tau=3/4 only the next block remains, and |A|=(1-nu_n)|Z|<=|Z|/2. These three closed or adjoining intervals cover every case, including the cutoff plateaus. Hence everywhere off zero

    |partial_bar u|/|u| <= [1/4+sqrt(k)D/(2L)]/r < C/r.

The constant 1/4 comes from the fixed half-slope while both blocks mix. Only the angle-speed error involves their unequal norms. A larger fixed L controls this error without changing the target dimension.

## 5. Joins and all-order flatness

Near t=(n+1)L both formulas have F=(n+1)t+d_n for one common constant d_n. The old angle is pi/2 and the new one zero. Both expressions for u reduce on a full annular neighborhood to exp(-d_n)iota_(j_(n+1))P_(n+1)(z). Thus every derivative matches at the interface, and the displayed differential inequality also holds there.

For every fixed real derivative order m, repeated differentiation of the radial power gives |D^a r^(-n)|<=K_(a,k)(n+1)^a r^(-n-a). A derivative of order b of z_j^n either vanishes or is bounded by (n+1)^b r^(n-b), up to a constant depending only on b. Leibniz and the k target components therefore give, for |alpha|=m,

    |D^alpha Q_n(z)|<=K_(m,k)sqrt(k)(n+1)^m r^(-m).

Derivatives of t of positive order j are bounded by K_(j,k)r^(-j); all t derivatives of the cutoffs are uniformly bounded. The chain and product rules, F'=O(1+t), bounded higher F derivatives and n<=t/L now imply

    |D^alpha u(z)|<=A_m(1+t)^B_m exp(-F(t)+mt).

The constants depend on the fixed k,C,L,cutoffs,m, but not n or direction. Dividing by r^p for any fixed p>0 adds only pt to the exponent. The quadratic lower bound for F shows every such quotient tends to zero uniformly. This proves derivative flatness, not merely smallness of |u|.

Set u(0)=0 and extend each punctured derivative by zero. These extensions are continuous. Each is o(|z|), so it is Frechet differentiable at zero with zero derivative. Induction identifies the extensions as the actual derivatives of u, since away from zero their derivatives already agree. Thus u is smooth and flat at zero. The same uniform estimates imply infinite-order vanishing in every finite-power local integral norm.

## 6. Coefficient class, imported sharpness and scope

Let d=2k and v_d be the Euclidean unit-ball volume in R^d. Define b(z)=C/|z| for z!=0 and b(0)=0. Its distribution on B_R is

    measure{b>lambda}=v_d min(R,C/lambda)^d.

Consequently sup_(lambda>0) lambda measure{b>lambda}^(1/d)=C v_d^(1/d), and the limiting high tail is v_d C^d. This is a finite weak-L^d coefficient; the inequality at zero holds with this assigned value because u and its first derivatives vanish. Finiteness of the weak norm alone cannot imply vector continuation for these fixed targets. The construction does not give arbitrarily small weak norm.

Confirmed LIT354, A2977, gives continuation at C=1/4 for the local distributional L1 equation, full-array norm and infinite-order L1 integral flatness. The constructed map satisfies that theorem's regularity and flatness premises, but has a strictly larger coefficient. Combining the two statements gives sharp inverse-radius threshold1/4 for each fixed source dimension k and each prescribed finite target N>=2k. The positive assertion is an explicit separate dependency. No statement for N<2k, sharp logarithmic correction in higher dimensions, scalar counterexample, Euler carrier majorant or Euler profile follows. The Euler conjecture remains open.

## 7. Reading and comparison status

The complete submitted proof cae5e42939c01fe799afba301fe53588e4868dab7082a1f1764657d3871ec8c2, its five sections and fourteen estimates, and all35manual checks were read. The argument above is an independent reconstruction. The existing configured model comparison has now arrived and is audited in Section 8. Actual provider execution is independently unattested.


## 8. Completed C comparison and diagnostic qualification

The full Theory Agent C  comparison of 2026-11-04T06:06:10Z, all eight mathematical items and diagnostic paragraphs, was read. Its exact transition intervals, Holder calculation, half-slope residual, array norm, all-order extension and sharpness scope agree with Sections 1-6. The factor k in the uniform bound for |W|^2/|Z|^2 cannot be decreased for this family: use equal coordinate moduli and theta=pi/2. This observation concerns that bound, not optimality of every estimate in the construction.

The entire final script and all three retained logs were read without rerunning them. The final log records 23 passing checks: seven symbolic, three exact cutoff checks, one finite collection of rational tests, four negative controls and eight numerical samples. Three negative controls are exact and one is numerical. The rational collection tests at most 180 directions and twelve degrees per direction; it is not a proof for all inputs. The sampled cutoff derivative maximum multiplied by 1.02 is not a certified supremum. The general construction uses the actual maximum and does not depend on that grid.

The first log records fourteen passes before dividing by a zero derivative norm on a plateau. The final code uses the nonzero scale |u|/r instead. The second log has 23 passes but its displayed nonvanishing diagnostic uses the weaker factor k^((n+1)/2) while the label states k^(n/2). The final code and log use the claimed factor k^(n/2). Earlier scripts were not separately retained, so a complete source-diff account of those edits is unavailable. The retained first-run traceback was normalized to relative environment references for this audit, with both original and retained hashes recorded. These diagnostic qualifications do not affect the analytic proof or establish any Euler assertion.

The same C note checks the preceding report update 7cbff5a2 against a6e71745. Its description agrees with A3003, including the approval scope and unchanged mathematical sections; it is not a fresh review of every theorem in those reports.


## 9. Confirmed source-status revision

The source revision 522e7b6cdce62d46d9e8480de92607368f84f307132187d735d720f9f0903572 changes only its status, replaces the prospective sharpness sentence by the confirmed conclusion, and appends confirmation Section 6. Every changed passage was read. A3005 supports the construction and fixed-target sharpness; A3006 supports only the qualified comparison, and A3007 retains the stronger-scope exclusions. The source accurately attributes diagnostic reading to the auditor rather than claiming that the literature agent read or reran those scripts. The construction is byte-unchanged. The positive endpoint A2977 remains a separate explicit dependency of sharpness. No Euler consequence is added.
