# Independent closure check after the full review of the defect theorem

## Scope and reviewed sources

The original computed-defect theorem is audit record alternative_route, proof, SHA256 d347071a02ea22eef12b4d209886deb0118738338d27bd8c531bcc559dbc61fa. T2's independent complete review of sections2,3,4 is frozen in source/T2_REVIEW.md, with its code and output. That review checks the fixed-factor multiplication estimate, the maximal domain, the normalized hyperplane, the low contraction, uniqueness and both rational scalar boxes. It does not review the B11 leading-tail sentence. Thus the original theorem is AUDITED conditional within precisely that reviewed scope. The following checks concern the new remarks in T2's review, not a second self-review of the original theorem.

## Exact scalar feasibility

Let A>0, mu real, and m,B,epsilon>=0. The existence of r>0 satisfying beta=mu-Ar>0 and

    m+(epsilon+Br)/beta<=r                                (1)

is equivalent to

    mu-Am-B>0,
    epsilon<=((mu-Am-B)^2-4ABm)/(4A).                     (2)

To prove this, set x=r-m. Multiplication by positive beta transforms (1) into

    -Ax^2+(mu-Am-B)x-Bm-epsilon>=0, x>=0.                (3)

If the linear coefficient is nonpositive, (3) cannot hold at x>0. At x=0 it can hold only when Bm=epsilon=0; beta>0 and r=m>0 then force B=0 and mu-Am>0, also a contradiction. Thus the first inequality in (2) is necessary. The quadratic's maximum on x>=0 is its value at x*=(mu-Am-B)/(2A)>0, giving the second inequality. Conversely (2) and this vertex give r*=(mu+Am-B)/(2A)>0 and beta*=(mu-Am+B)/2>0, and (3) holds there. This proves the equivalence, including degenerate zero parameters.

The elementary strict statement B<beta in T2 remark R2 needs a qualification: (1) implies B<=beta, and strictness follows if m+epsilon>0. The equality case m=epsilon=0 is admissible when B=beta. This endpoint does not alter the feasibility formula or any numerical box.

## H-free defect theorem

Let X_(s,W) be the Hilbert norm

    X_(s,W)(h)^2=||omega D^2 J^s h||_2^2
                 +W1||D J^s h||_2^2+W2||J^s h||_2^2,
    omega=(1+4r^2)^(2/5), J=(1-Delta)^(1/2).

Assume exactly the background, domain, normalization and inverse hypotheses of the audited T4-019 and T2-R3 theorems, including (B-L2). For the two registered weight choices these supply, for normalized k with X_(s,W)(k)<=r,

    ||A_k^-1||_(X->X)<=1/beta_r,
    ||A_k^-1||_(L2->L2)<=1/2,
    beta_r=mu0-C's-(8/5)r/sqrt(s),

where (W1,W2,mu0,C') is either (2^14,2^18,259/1000,401) or (2^15,2^20,97/250,397), and 0<s<=2^-10. These inverse assumptions have their own audited sufficient background conditions; they are not deduced from a small matrix here.

Let g be smooth S1 in the maximal generator domain, c[g]=0. Define a1=||Dg||_infinity, a2=||D^2g||_infinity, d2=||omega D^2g||_infinity, d3=||omega D^3g||_infinity, with ordered Frobenius derivative norms. Let S2,S3,S4 be the component-sum weighted derivative bounds used in section2 of T4-004. This notation separates derivative constants d2,d3 from energy weights W1,W2. Set

    M = [[(9/5)a1, 2d2/sqrt(W1), d3/sqrt(W2)],
         [0, a1, a2 sqrt(W1/W2)], [0,0,a1]],
    K = 17 [[S2,2S3/sqrt(W1),S4/sqrt(W2)],
            [0,S2,S3 sqrt(W1/W2)], [0,0,S2]].

Dropping the negative-Sobolev component from the componentwise multiplication proof in T4-004 proves

    X_(s,W)(U[k].Dg)<=||M+sK||_2 X_(s,W)(k).             (4)

Indeed the top row before multiplying by the norm weights is (9/5)a1 P+2d2 a+d3 b plus 17s(S2P+2S3a+S4b). The derivative row is a1 a+a2 b+17s(S2a+S3b), and the bottom row a1 b+17sS2b. Multiplying by (1,sqrt(W1),sqrt(W2)) gives exactly the matrices above. The approximation proof in T4-004 involves no negative-Sobolev estimate in these three rows, and hence applies unchanged.

Suppose X(g)<=m, X(F+Lg)<=epsilon, ||M+sK||<=B and (1) holds with mu=mu0-C's and A=(8/5)/sqrt(s). Then there exists a unique normalized correction h with X(h)<=r and F(rho+h;c)=0. Define

    T(k)=g-A_k^-1(F+Lg+U[k].Dg).

Equation(4), the high inverse and(1) give a self-map. The domain identity A_k T(k)=-F follows since g belongs to the maximal A_k domain. The forcing's first y derivative at zero vanishes: (Lg)_y=a0 c[g]=0 and (U[k].Dg)_y=c[k]g_y=0. The normalized inverse preserves c[T(k)]=0. The difference equation is

    A_k(T(k)-T(l))=-U[k-l].DT(l).

The velocity contraction and the Fourier embedding ||Dh||_infinity<=c_s X(h), c_s=(4 pi s(1+s))^(-1/2), give the L2 Lipschitz constant at most c_s r/2. This is less than one whenever beta_r>0 in the stated parameter range: c_s r/2<mu0/(4sqrt(pi)(8/5))<1. The normalized high ball is complete in L2 by the already audited closed-ball argument. Banach's theorem proves existence. Any solution in that ball obeys the same inverse equation and is the same fixed point. No leading-tail assertion is added here.

Thus T2's H-free extension is a valid conditional theorem. It does not rescue a candidate already excluded by a necessary distance test. The sentence that (B-L2) fails for every current exact candidate is too broad: d2 satisfies the signed condition by T4-053; other conditions and the correction-distance tests still obstruct its closure.

## Universal distance budget

For any mu0,C,kappa>0, beta=mu0-Cs-kappa r/sqrt(s)>0 implies

    r<(mu0-Cs)sqrt(s)/kappa
      <=(2mu0/(3kappa))sqrt(mu0/(3C)).                 (5)

Differentiate the cubic mu0 t-Ct^3 in t=sqrt(s)>0; its unique positive maximum occurs at s=mu0/(3C). Restricting the allowed s can only decrease this upper bound. Since X(h)>=sqrt(W2)||h||_2, divide(5) by sqrt(W2) to obtain a universal L2 distance budget. The same argument applies to the original N_s norm with sqrt(W2)=512. T2's listed suprema and candidate exclusions follow from the existing point and weak-test bounds. A computed g cannot enlarge this total-correction ball.

## Sharper fixed-factor commutator constant

For 0<s<=smax<=1/2, concavity gives (1+2|z|)^(4/5)<=1+(8/5)|z|. The exact Bessel moments therefore bound the commutator's weighted first moment by

    s[(sqrt(pi)/2)Gamma((1-s)/2)/Gamma(1-s/2)+16/5]
    <=s[(sqrt(pi)/2)Gamma((1-smax)/2)+16/5].            (6)

Here Gamma(y)>=1 for 0<y<=1 follows from Jensen's inequality applied to the convex function t^(y-1) under the unit exponential probability law. Gamma is decreasing on(0,1]: log Gamma is convex by Holder's inequality and its derivative at1 is E(log T)<log E(T)=0. Thus its derivative is negative throughout that interval. These arguments justify both inequalities without a rounded gamma estimate. The script encloses the endpoint in(6) by Arb. If the smax=2^-10 endpoint is below24/5, every factor17 in K may be replaced by24/5. This is a quantitative improvement of the fixed-factor bound, not a new inverse theorem.

## Numerical checks and limitations

The code recomputes the scalar boxes with rational arithmetic, the general distance budgets and the gamma endpoints. It reads no T2 computed numbers as input. Rounded box tolerances must be rounded downward to remain sufficient. Completion is recorded in verification/ and the top-level ledger. No candidate g or certified linear defect is supplied by this result.
