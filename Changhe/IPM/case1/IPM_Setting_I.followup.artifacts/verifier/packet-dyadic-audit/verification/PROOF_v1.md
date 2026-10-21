# Frozen packets: direct dyadic estimates and all normalized axis traces

Date: 2026-10-20. This is an independent proof of a specified part of the frozen-packet statement in the lead's section6.4. It does not prove the full asymptotic expansion or any correction to the variable-coefficient equation.

## Exact statement and definitions

Let A>1, g>0, q=2(A-1), b=g/q and h=1+g. Choose a smooth complex function Phi compactly supported in R minus{0}, satisfying

    integral Phi(t)dt=0,
    Phi(-t)=-conjugate(Phi(t)).

The Fourier transform convention is fhat(xi,eta)=integral exp(-i(s xi+y eta))f(s,y)dsdy, with inverse factor(2pi)^-2. Define the tempered distribution Vhat by the limit of the following formula restricted to |eta|>epsilon:

    Vhat(xi,eta)=sgn(eta)|eta|^(-A-2)
       (1+xi^2/eta^2)^(-b) Phi(xi/|eta|^A).

The extension at zero frequency is part of this definition. Let v be its inverse transform. Define U_2[v] by the same limiting convention after multiplying the displayed expression by -xi^2/(xi^2+eta^2). Conclusions:

1. These limits exist. The density is the real continuous function

    v(s,y)=2i/(2pi)^2 integral_0^infinity sin(yr)r^-2
        integral Phi(t)exp(i s t r^A)(1+t^2 r^q)^(-b)dt dr.       (1)

   It is odd in y and satisfies the frozen equation

    A s v_s+y v_y-v+g U_2[v]=0                                (2)

   distributionally, with no additional distribution at zero frequency.
2. v is smooth off(0,0). If m is a nonnegative integer, 0<alpha<1 and(m+alpha)A<=h, then v belongs to C^(m,alpha)_loc. The noninteger endpoint in this statement is included.
3. For every integer j>=2, the trace d_y^j v(s,0) is smooth for s!=0 and satisfies

    |d_y^j v(s,0)| <= C_j times
       1,                         j<h,
       1+log(1/|s|),              j=h,
       1+|s|^((h-j)/A),           j>h,                         (3)

   for0<|s|<=1/2. Thus, for every odd j>=3,

    |s|^((j-1)/A) d_y^j v(s,0)/j! ->0.                     (4)

   Neither boundedness of all unweighted traces nor absence of smooth Taylor terms is asserted.
4. The mapping Phi to v is injective. If h/A>3, it gives an infinite-dimensional real space of frozen solutions in C^(2,alpha)_loc for every alpha<1, smooth off the source and satisfying(4) at every odd order.
5. Every such packet satisfies |v(X)|<=C(1+|X|)^(1/A). Every nonzero packet fails the global bound |grad v(X)|<=C(1+|X|)^(gamma-1) for every gamma<1. Hence these uncut packets do not satisfy that growth condition of the profile class.

There is no assertion that they solve the nonlinear or variable-coefficient IPM equation, that their cutoffs correct to kernel elements, or that they yield a family or either task endpoint. The full quasi-homogeneous expansion with possible resonant logarithms remains outside this proof.

## The distribution at low frequency and its equation

Set xi=t r^A, eta=plus or minus r. The Jacobian is r^A. For a Schwartz test function f, the pairing becomes

    integral_epsilon^infinity r^-2 integral Phi(t)(1+t^2r^q)^(-b)
           [f(t r^A,r)-f(t r^A,-r)] dt dr.                   (5)

For r<=1 and t in the fixed support,

    f(t r^A,r)-f(t r^A,-r)
       =2r f_eta(0,0)+O(r^(A+1)+r^3).

The amplitude is1+O(r^q), uniformly with t derivatives on this support. The zero moment of Phi cancels the leading term. The absolute value after the t integration is at most a fixed Schwartz seminorm times

    C(r^(q-1)+r^(A-1)+r),

which is integrable since A>1 and q>0. At infinity, the test function gives arbitrary polynomial decay and the integral converges. The same argument proves continuity with respect to finitely many Schwartz seminorms, hence defines a tempered distribution. Multiplication by the second-velocity symbol adds a factor O(r^q) at zero, so its pairing converges too.

Let D=A xi d_xi+eta d_eta. The quantity t=xi/|eta|^A is invariant under D and D r=r. Direct differentiation away from eta=0 gives

    D Vhat=(-A-2-g xi^2/(xi^2+eta^2))Vhat.

The Fourier transform of(2) is therefore zero away from eta=0. On the cutoff |eta|>epsilon, integration by parts leaves only the boundary from D crossing r=epsilon. Its pairing is epsilon times the radial integrand in(5), hence O(epsilon^q+epsilon^A+epsilon^2) after the same cancellation. It tends to zero. The support in t is away from zero and compact, so there is no separate boundary on xi=0 or at t infinity. This proves(2) as a distribution on the whole plane.

Grouping positive and negative eta in Fourier inversion gives(1). On bounded sets of(s,y), its low-r integrand is bounded by C(r^(A-1)+r^(q-1)): subtract the zero moment in the inner integral and use |sin(yr)|<=C r. For r>=1, the integrand is bounded by C r^(-2-g), since t stays away from zero. Both bounds are integrable and locally uniform, proving continuity and agreement with the distributional inverse. The reality condition makes the inner t integral purely imaginary for real s,r; thus v is real. Oddness in y follows from the sine. These statements also hold for U_2 with its inserted multiplier.

## Smooth low frequencies and uniformly Schwartz dyadic pieces

Choose a smooth partition of unity on r>0 consisting of one term supported in r<2 and terms chi(2^-n r), n>=0, with chi supported in a fixed compact subinterval of(0,infinity). Overlap is uniformly finite. The low-frequency part is smooth in(s,y). To check every derivative at r=0, write a for the number of s derivatives and c for y derivatives. If a>=1, the inner integral gains r^(Aa). For c=0 the sine gives an extra r; for c>=1 the derivative supplies r^c. All resulting powers are integrable since A>1. If a=0,c=0 or1, use the zero-moment cancellation O(r^A+r^q); if c>=2 the factor r^c alone suffices. This also justifies derivatives uniformly on compact sets.

For the n-th high-frequency piece substitute r=2^n u. Since qb=g, it has the exact form

    v_n(s,y)=2^(-hn) H_n(2^(An)s,2^n y).                  (6)

The inverse Fourier integrand defining H_n is supported where u lies in the fixed support of chi and t lies in the fixed support of Phi. On each sign of eta, the map(t,u) to(t u^A,plus or minus u) is a smooth diffeomorphism with nonzero Jacobian. Its amplitude includes

    (2^(-qn)+t^2u^q)^(-b),

whose derivatives of every fixed order are bounded uniformly for n>=0. This follows because |t| and u have fixed positive lower bounds. All other factors are fixed smooth functions on this compact support. Integration by parts in the two Fourier variables, with no boundary terms because the cutoff functions are smooth and compactly supported, proves H_n are uniformly Schwartz. Consequently, for every a,c,N>=0,

    |d_s^a d_y^c v_n(s,y)|
       <= C_(a,c,N) 2^((Aa+c-h)n)
          (1+2^(An)|s|+2^n|y|)^(-N).                  (7)

On any compact set separated from(0,0), choosing N sufficiently large makes the derivative series uniformly summable. Thus v is smooth there.

## Ordinary Holder regularity, including the noninteger endpoint

For a derivative of total order m, Aa+c<=mA. Its uniform norm at scale n is bounded by C 2^((mA-h)n). Its first derivative is bounded by C 2^(((m+1)A-h)n). The mean-value inequality and the uniform bound give, for delta=|X-X'|<=1,

    |D^m v_n(X)-D^m v_n(X')|
       <= C 2^((mA-h)n) min(1,2^(An)delta).             (8)

Put theta=h/A-m. The assumption gives theta>=alpha>0. If0<theta<1, splitting at2^(An)delta=1 sums two geometric series and gives C delta^theta. If theta=1, the low-scale part is at most C delta(1+log(1/delta)), bounded by C_alpha delta^alpha for every alpha<1. If theta>1, the derivative series of order m+1 is summable and gives a Lipschitz bound. Thus in every permitted case(8) sums to C delta^alpha. The derivatives of order m themselves are uniformly summable because theta>0; the smooth low-frequency term causes no difficulty on a compact set. This proves the asserted C^(m,alpha)_loc regularity without assuming any asymptotic expansion.

## Axis traces at every order

At y=0, inequality(7) gives

    |d_y^j v_n(s,0)|<=C_(j,N)2^((j-h)n)(1+2^(An)|s|)^(-N).

For0<|s|<=1/2 split the series at2^(An)|s|=1. Before the split, it is a bounded geometric series if j<h, a sum of O(1+log(1/|s|)) constants if j=h, and at most C|s|^((h-j)/A) if j>h. After the split, take AN>max(j-h,0); the geometric tail gives the same respective bound, with a bounded contribution from the smooth low frequencies. This proves(3). Multiplying by |s|^((j-1)/A) gives a vanishing bound: its exponent is(j-1)/A when j<h, with a logarithm if j=h, and g/A>0 when j>h. The conclusion(4) follows for every stated j. The constant may depend on j; no uniform all-orders estimate is claimed.

## Injectivity, dimension and far-field admissibility

If v is zero as a distribution, Vhat is zero. On eta>0 away from the origin its formula is a smooth function, with nonvanishing scalar factors multiplying Phi. Thus Phi is zero. The reality and moment conditions leave an infinite-dimensional real space: take Phi=i f, where f is any real even smooth compactly supported function away from zero with integral zero. Injectivity and the regularity and trace estimates prove conclusion4.

For growth, put S=|s| and Y=|y|. On0<r<1 subtract the zero moment to bound the inner integral in(1) by

    C(min(1,S r^A)+r^q).

The first term contributes at most C(1+S)^(1/A), even after replacing the sine by1, by splitting at r=S^(-1/A) when S>1. The second contributes at most

    C integral_0^1 min(1,Yr) r^(q-2)dr.

For q<1 this is bounded by C(1+Y)^(1-q), for q=1 by C(1+log(1+Y)), and for q>1 by a constant. Since1-q=3-2A<1/A for A>1, all cases are bounded by C(1+Y)^(1/A). The high-r part is uniformly bounded. This proves the isotropic growth bound.

A stronger fact follows from rescaling(1): as R tends to infinity,

    R^-1 v(R^A s,R y) -> V_0(s,y),                      (9)

locally uniformly, where V_0 is(1) with the amplitude(1+t^2r^q)^(-b) replaced by1. For the rescaled integral, the amplitude is(1+t^2r^q/R^q)^(-b). At r<=1 the same moment cancellation gives an integrable bound C(r^(A-1)+r^(q-1)), uniform for R>=1 and compact(s,y); at r>=1 use C r^-2. Dominated convergence, with the same bounds on compact sets, proves(9). The limiting Fourier distribution is given by the preceding construction with amplitude1 and is nonzero for nonzero Phi, again by its formula on eta>0. V_0 is continuous and odd in y.

Suppose the weighted gradient bound in conclusion5 held. On each compact set with |s| bounded away from zero,

    d_y[R^-1 v(R^A s,Ry)]=v_y(R^A s,Ry)
       =O(R^(A(gamma-1))) ->0.

Using the fundamental theorem of calculus between two finite y values and the locally uniform limit(9), V_0 is independent of y on s!=0. Oddness makes it zero there, and continuity makes it zero on s=0 as well. This contradicts its nonzero Fourier distribution. Thus no nonzero packet satisfies that weighted gradient condition. This is a failure of one admissibility condition for the uncut field, not a conclusion about a compact cutoff or its possible correction.

## Dependencies and scope

The proof uses Fourier inversion for tempered distributions, integration by parts, the mean-value inequality, geometric series, dominated convergence and elementary compactly supported Fourier decay. The needed estimates are supplied above. It does not use numerics, the full quasi-homogeneous expansion, a classification of all frozen solutions, or a variable-coefficient inverse. In particular it supplies no exact coupled profile, no smooth-center candidate and no endpoint. Review evidence and any finite exponent checks belong in verification/. The independent verifier must read and resolve a second-model review before attributing the proof as confirmed.
