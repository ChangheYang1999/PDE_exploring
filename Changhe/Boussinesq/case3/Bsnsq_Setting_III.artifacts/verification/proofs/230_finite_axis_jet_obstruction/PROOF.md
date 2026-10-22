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
