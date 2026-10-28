# Small coupling tails and reduction to a compact core

## Statement

Use the actual modal trial, X_s, T and C_R of topics123 and137. The order is the actual order of proof 130. Let chi_-(t) be smooth, equal to one for t<=0 and zero for t>=1. Let chi_+(t)=chi_-(-t). Then

 lim_(R to infinity)||chi_-(t+R) C_R||_(Xs to Xs)=0,
 lim_(R to infinity)||chi_+(t-R) C_R||_(Xs to Xs)=0.      (1)

No rate is asserted for the full C_R. Its unprojected part C_ren has the quantitative qualitative-constant bounds

 ||chi_-(t+R) C_ren||_(Xs to Xhat_s)<=C exp(-(2-delta)R),
 ||chi_+(t-R) C_ren||_(Xs to Xhat_s)<=C exp(-(1-k)R).    (2)

Here Xhat_s has exactly the bulk and cofactor norms of X_s but omits the zero vertical trace. The constants in (2) depend on the fixed actual data and norm, and are not numerically evaluated. They are independent of R sufficiently large. The parameters are delta=9/5, gamma=-1/2 and the exact k of proof 123.

Let S=T+C_R on D_s={h in X_s:T h in X_s}. For every compact K contained in Re lambda>-m_x there exist a smooth compactly supported radial cutoff zeta and C_K<infinity such that

 ||h||_Xs<=C_K[||(S-lambda)h||_Xs+||zeta h||_Xs],
               h in D_s, lambda in K.                 (3)

The cutoff can equal one on a finite cylinder covering both principal end transitions. Its high-norm term has not been shown compact. Estimate (3) does not imply Fredholmness or an inverse without a further core estimate.

## Norms with the trace omitted

The norm of Xhat_s is

 ||h/b||_(H^{s(.)})^2+||chi_y h/(b p)||_Hsigma^2,

with the same physical parity, p, b, sigma and sector cutoff as in proof 123. It is a Hilbert graph space. Removing the trace condition does not change the norm of a member of X_s. Smooth radial cutoffs are uniformly bounded on Xhat_s under translation and converge strongly to zero when their support escapes either end. For the constant-order component this follows from density of compactly supported smooth functions and the uniform multiplier bound. The same density and bound hold in the variable-order component by its dyadic definition. Approximate both components simultaneously using the local graph description, or first use a growing radial cutoff and then the local cofactor/bulk partition. No axis trace needs to be restored in Xhat_s.

## Explicit Schur estimates for the unprojected coupling

Take dyadic annuli with output radius r=2^j and input radius s=2^l. Bounded overlaps and a fixed shift of the indices only change constants. Proof 123 proves the following six operator matrices, including the output cofactor norm:

 l<=j<=0:       2^(2j) 2^((delta+2)(l-j));
 j<=l<=0:       2^((2-delta)j+delta l);
 0<=l<=j:       2^((k-1)j) 2^((gamma+3)(l-j));
 0<=j<=l:       2^((k-1)j) 2^((gamma-1)(l-j));
 j<=0<=l:       2^((2-delta)j+(gamma-1)l);
 l<=0<=j:       2^((k-4-gamma)j+(delta+2)l).             (4)

The fixed constant C is suppressed. These are estimates for C_ren itself after the exact normalized linear-strain cancellation, not for U separately. They hold for the full Sobolev norms because separated annuli give smooth kernels with the same bounds after any required output derivative, and the comparable-annulus estimate includes the actual coefficient regularity.

Restrict first to j<=-N. In the first row of (4), the row sum is bounded by C2^(2j)<=C2^(-2N). For a fixed l<=-N, the column sum is

 2^((delta+2)l) sum_(j=l)^(-N) 2^(-delta j)
 <=C2^(2l)<=C2^(-2N).

In the second row its row sum is at most C2^((2-delta)j), while its column sum is

 2^(delta l) sum_(j<=min(l,-N)) 2^((2-delta)j).

For l>=-N this is at most C2^(-(2-delta)N); for l<-N it is at most C2^(2l), which is smaller. The mixed fifth row is a product of two decreasing geometric sums and has row and column sums at most C2^(-(2-delta)N). Thus Schur's test bounds the inner output operator by C2^(-(2-delta)N).

For j>=N, the third row has row sum at most C2^((k-1)j). Its column sum is

 2^((gamma+3)l) sum_(j>=max(l,N)) 2^((k-gamma-4)j),

bounded by C2^(-(1-k)N), since k-gamma-4<0 and gamma+3>0. In the fourth row, the row sum has the same bound, while the column sum for l>=N is

 2^((gamma-1)l) sum_(j=N)^l 2^((k-gamma)j)
 <=C2^((k-1)l)<=C2^(-(1-k)N),

using k-gamma>0. The mixed sixth row has row and column sums at most C2^((k-4-gamma)N), a faster decay. Hence the far output operator has norm at most C2^(-(1-k)N).

The needed signs are all strict for the exact data:

 2-delta=1/5>0, delta+2=19/5>0,
 gamma+3=5/2>0, 1-gamma=3/2>0,
 1-k>0, k-gamma=k+1/2>0, 4+gamma-k=7/2-k>0.

Uniform radial localization of the variable-order and cofactor norms transfers these dyadic matrix bounds to the global norms. The pieces separated from an output annulus by a fixed number of indices are already included in (4); enlarging the annuli and cutoffs therefore produces no additional tail. Putting R=N log2 and absorbing the bounded difference for arbitrary R proves (2).

## The subtracted axis term

Write

 C_R=C_ren-E Gamma_C,  E beta=x^2 y beta(log r).

Proof 123, using topics109,113 and115, proves that

 K:h -> Gamma_C[h]/a

is a compact map X_s -> H^sigma(R). The map J:f(t)->b(t)p(theta)f(t) is bounded H^sigma(R)->Xhat_s: the angular factors are smooth, and sigma is the largest bulk order. Thus E Gamma_C=JK is compact into Xhat_s. It need not take values in X_s because its axis trace is precisely the trace being subtracted.

If M_R is either escaping cutoff in (1), then M_R is uniformly bounded on Xhat_s and converges strongly to zero. Therefore ||M_R JK|| tends to zero. To verify the operator-norm conclusion, cover the compact closure of JK's unit-ball image by finitely many balls of radius epsilon. Strong convergence controls the finitely many centers, and the uniform bound controls each radius. Taking the supremum over the unit ball and then epsilon to zero proves the claim.

Combine this with (2). The exact axis identity guarantees M_R C_R h belongs to X_s and its X_s norm equals its Xhat_s norm. This proves (1). The compact argument supplies no numerical decay rate, which is why (1) and (2) have different quantitative statements.

## The far principal estimate

For completeness, proof 135 gives the actual far principal estimate in the same form as proof 137's inner estimate. Far enough right the order is identically sigma and b=e^(gamma t). Extend the small W7 coefficient errors to zero before the far end, preserving parity and axis tangency. The resulting full-cylinder operator has the selected inverse on X_infinity proved there.

For a far cutoff chi_f, the localized function belongs to the maximal X_infinity domain, and

 (T-lambda)(chi_f h)=chi_f(T-lambda)h+q chi_f' h.

Its second term is confined to a finite radial transition, with uniformly bounded multiplier norm. The X_infinity norm and the X_s norm of these far-supported functions are uniformly equivalent: both have order sigma on a larger neighborhood of the support, and the remaining off-support kernels are smoothing with uniform bounds. Equivalently use the local dyadic definition and a fixed larger cutoff. Low uniqueness identifies the localized solution with the selected inverse. Thus, uniformly for sufficiently far-right translated cutoffs,

 ||chi_f h||_Xs<=C_K[||chi_larger(T-lambda)h||_Xs
                              +||eta_f h||_Xs].        (5)

Here eta_f is a finite annular cutoff and chi_larger includes its transition. This is a high-norm annular error, exactly as at the inner end.

## Absorption and the remaining core

Put f=(S-lambda)h. Then (T-lambda)h=f-C_R h. Apply proof 137 at an inner end and (5) at a far end. Choose both ends so far out that (1), multiplied by the two fixed principal-estimate constants, contributes at most ||h||_Xs/4. This choice is possible because those principal constants are uniform under further end translation. The forcing localizations are bounded by C||f||_Xs.

Complete the two end cutoffs to a smooth radial partition of unity. Choose zeta compactly supported and equal to one on the middle partition and on both annular error supports. Bounded multiplication controls all middle and annular norms by C||zeta h||_Xs. The triangle inequality for the partition gives

 ||h||_Xs<=C_K||f||_Xs+C_K||zeta h||_Xs+(1/2)||h||_Xs.

Absorb the last term to obtain (3). Since C_R is bounded on X_s, D_s is also the exact maximal X_s domain of S; no unmentioned domain restriction is introduced in this substitution. The argument proves (3) for every member of that domain, not just for compactly supported test functions.

## The open implication

Multiplication by a compactly supported zeta is not compact on X_s. High-frequency packets supported where zeta=1 give a bounded sequence without a strongly convergent subsequence. A further estimate must control this core norm by the full equation and a compact or low norm. Neither the smallness of the coupling at the ends nor the finite size of the core proves that estimate. Global H3, low injectivity, numerical inverse constants and nonlinear closure remain separate.
