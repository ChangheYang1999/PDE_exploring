# The S1 Hessian velocity bound and a balanced Young estimate

## Statement

Let h be a real smooth compactly supported function on R2, even in x and odd in y. Put U[h]=(-R1R2h,R1^2h), with Rj the Fourier multiplier -i xi_j/|xi|. Let D2 be the full ordered Cartesian Hessian, with scalar squared norm |h_xx|^2+2|h_xy|^2+|h_yy|^2 and an additional sum over both velocity components. For any fixed R>0 set w2=1+r^2/R^2. Then

    ||w2 D2 U[h]||2^2 <= (185/96)||w2 D2 h||2^2.          (1)

The same bound holds in the completion of the stated test class in the weighted input Hessian norm, interpreted on the limiting derivative tensor. This strengthens the independently proposed bound63/32 in T2 the review of T4-242 R2. The proof below independently verifies R2, and the185/96 refinement is a new T4 claim awaiting Opus review. No sharpness is claimed. Neither bound supplies a transport estimate, inverse, normalization trace or nonlinear closure.

## 1. Exact Mellin representation

Let B have multiplier (xi1-i xi2)^2/|xi|^2. The real IPM symbols give

    U2+iU1=-(h+Bh)/2.                                  (2)

For real h, the squared complex Hessian norm on the right is the sum of the two real velocity component norms. Put d=(partial_x-i partial_y)/2, dbar=(partial_x+i partial_y)/2. Direct differentiation gives

    |D2v|^2=4(|d^2v|^2+2|d dbar v|^2+|dbar^2v|^2).

If h=f_m(r)e^(im theta), the three radial factors are r^(-2)(D+m-2)(D+m)f_m/4, r^(-2)(D-m)(D+m)f_m/4 and r^(-2)(D-m-2)(D-m)f_m/4, with D=r partial_r and angular shifts -2,0,2. In t=log r coordinates, put F_m(t)=e^t f_m(e^t). The moment r^4 and measure r dr cancel the radial powers. After unitary Fourier transform in t, D on f_m is -1+i tau on F_m. The input moment energy is

    ||r^2D2h||2^2=(pi/2) sum_m int Q_m(tau^2)|Fhat_m(tau)|^2 d tau,
    Q_m(u)=4[m^4+10m^2+5+(2m^2+6)u+u^2].              (3)

Distinct modes remain orthogonal for each Hessian component. Since dbar B=d, the multiplier from input mode m to output mode m-2 is

    mu_m(tau)=(m-1+i tau)/(1-m+i tau), |mu_m|=1.         (4)

For m=1 the value is identically1, including its removable value at tau=0. This is the canonical L2 Beurling operator: the extra homogeneous solution of the radial equation cannot belong to L2 at both endpoints. The compact smooth input has finite energy in (3), and the per-mode canonical outputs do also by the polynomial estimates below. These facts justify the transform and its extension by truncation.

## 2. Parity and output groups

S1 parity gives only positive odd sine modes. At each tau, write A_n=Fhat_n for n=1,3,...; then Fhat_(-n)=-A_n. This relation follows from the sine expansion and remains true after Fourier transform in t. The input energy at this tau is2(a+b), where

    a=Q_1|A_1|^2, b=sum_(n>=3, odd)Q_n|A_n|^2.

The mode -1 of h+Bh vanishes because -A_1+mu_1 A_1=0. All other output modes split into

    P=sum_(k>=1, odd)Q_k|A_k+mu_(k+2)A_(k+2)|^2,
    N=sum_(k>=3, odd)Q_k|A_k+mu_(2-k)A_(k-2)|^2.         (5)

Zero coefficients outside a finite initial truncation are understood. No mode is discarded at its upper boundary: N includes the outgoing last mode as well.

Write q_m=Q_m/4. For real u>=0,

    q_M-q_(M-2)=4(M-1)[M^2+(M-2)^2+10+2u]>=0, M>=1,
    11q_1-q_3=64u+10u^2>=0,
    5q_M-q_(M+2)
      =4(M-3)(M^3+M^2+7M+3)+(8M^2-8M+16)u+4u^2>=0,
                                                        M>=3.   (6)

Each identity is obtained by expanding the polynomial in (3); every displayed coefficient is nonnegative in its specified range. Thus the two vector energies in P are a+b and at most b. The two in N are b and at most11a+5b. This is the only estimate on infinitely many angular modes.

## 3. Young's inequality and constants

For any lambda>0, |z+w|^2<=(1+lambda)|z|^2+(1+1/lambda)|w|^2, because the difference is |sqrt(lambda)z-w/sqrt(lambda)|^2. Applied to P and N with parameters lambda and kappa, respectively, this yields

    P+N <= (12+lambda+11/kappa)a
         +(8+lambda+1/lambda+kappa+5/kappa)b.             (7)

The peer's choice lambda=1,kappa=4 gives(63/4)a+(61/4)b. Dividing by the input2(a+b) and by4 from (2) proves its bound63/32.

The balanced choice lambda=2/3,kappa=4 gives185/12 for both coefficients in (7). Dividing in the same way proves

    ||r^2 D2 U[h]||2^2 <= (185/96)||r^2 D2 h||2^2.       (8)

No optimization over the Young parameters or over the Mellin frequencies is needed. The estimate is strict as an improvement of63/32 because185<189.

## 4. Inhomogeneous weight and completion

The unweighted Fourier multiplier gives ||D2U[h]||2<=||D2h||2. The previously audited first-moment bound, T4-206 and its accepted review, gives ||rD2U[h]||2^2<=(5/3)||rD2h||2^2 for this test class. Since

    w2^2=1+2r^2/R^2+r^4/R^4, 1<5/3<185/96,

the sum of these three squared inequalities proves (1). Fourier truncations in theta converge in each input moment norm by (3) and the corresponding lower moments. The estimates make the outputs Cauchy in the weighted norm. Unweighted multiplier continuity identifies their limit with the canonical velocity acting on D2h. The same argument applies to any Cauchy sequence in the stated completion. It does not assert the existence of an independently normalized scalar representative in a homogeneous completion.

## 5. Why the parity hypothesis matters

For h=r^(-1)b((log r-T)/L)cos(theta), with b a nonzero smooth compactly supported real bump, the input modes have equal signs. At tau=0 the output -1 doubles rather than cancels. As L tends to infinity the squared velocity moment ratio tends to(5Q_1(0)+Q_3(0))/(8Q_1(0))=2. Thus the S1 bound cannot be extended to all centrally odd functions.

For the analogous radial bump, the input is mode0 and B moves it to mode-2. Its squared moment ratio tends to Q_2(0)/Q_0(0)=61/5; the velocity ratio tends to(1+61/5)/4=33/10. This exceeds((1+sqrt6)/2)^2, so even the earlier centrally odd bound fails without parity. The limits follow by Fourier scaling in t and dominated convergence against the Schwartz transform of b. Dilation to large physical radius makes the inhomogeneous weighted ratio approach the homogeneous moment ratio. These are explicit counterexamples, not conclusions drawn from numerical scans.

Dependencies: the audited Mellin tensor computation in ../weighted_hessian_second_moment/PROOF.md, the canonical multiplier, the audited first-moment estimate, finite sums, Young's inequality and Plancherel. The copied Opus numerical grids are illustrative and are not used in any proof here.
