# Directed values from nearly maximal disks and eight reflection moments

## Statement and scope

Use the scalar homogeneous Holder spaces and circular principal-value operators of ../PROOF.md. The analytic inputs are the accepted optimal-axis-disk theorem V224, the full even-moment theorem V223, the exact exterior series V222, and the sharp-deficiency cutoff inequality V205. All functions and norms have those precise conventions. The following procedure produces upper bounds for D_alpha at the stated rational exponents, and a linear remainder coefficient for all 0<alpha<=1/100. It does not assert optimality of the chosen radii or equality with the operator norm.

Let p(s)=2s^4-3s^2+4s-1, and isolate its unique root sigma in (0,1/3) by rational bisection. For an isolating interval [l,u] in this range put v(s)=1-2s+2s^3 and N(s)=(1-2s^2)^2. Both N and v are positive and decreasing there. Therefore

    N(u)/(2v(l)) <= c_* <= N(l)/(2v(u)).

Round this upper bound upward to a rational c on the grid 10^(-30), and put a=1-c. The program verifies 49/66<c<3/4. The disks with this center and radius are contained by V224, since c>=c_*. Every row satisfies 2as<1. For a cutoff row s=rho<1/2, the retained density is positive by V223.

Write B_m(c)=int_0^a t^m/(c+t)^2 dt. For n=1,...,8 subtract the positive saving

    A_n(alpha)s^(2n)B_(2n+1)(c),
    A_n(alpha)=2alpha prod_(k=1)^(2n-1)(k-alpha)/(n!)^2.

For cutoff rows replace B_m by B_m-rho^2 a^(m+1)/[(m+1)(1-rho)^2]. For the uniform coefficient on 0<alpha<=epsilon=1/100 subtract instead the same sum with A_n(epsilon)/epsilon and s=rho. This is a lower bound for the saving divided by alpha throughout the interval, because every positive factor k-alpha decreases as alpha increases. Omitting the positive terms n>=9 preserves the upper bound. The geometric majorant in V223 is recorded only to describe this truncation; no omitted saving is subtracted.

The unperturbed rows start from the original translation-cost bounds recorded in V220's inputs, before any reflection saving. Cutoff rows recompute J_D with the sharp deficiencies and exact exterior upper series S_64^+. Each saving is subtracted exactly once. The uniform row recomputes the corresponding K_D. All radii are explicitly selected rational numbers, rather than numerical minimizers asserted without proof.

## Independent moment enclosure

The logarithmic finite formula for B_m in V223 is evaluated with directed ball arithmetic. A separate positive series provides exact rational bounds. With u=t/(c+t), the endpoint is u=a because c+a=1, and

    B_m(c)=c^(m-1) int_0^a u^m/(1-u)^m du
          =c^(m-1) sum_(k>=0) binom(m+k-1,k) a^(m+k+1)/(m+k+1).

All terms are positive. For k>=N their successive ratio is at most q=a(m+N)/(N+1). If q<1, the remainder after k=N-1 is at most the first omitted term divided by 1-q. Thus a finite exact rational sum and that remainder enclose each B_m. The same enclosure remains valid after subtracting the exact rational removed-density moment. This provides an independent check on signs and cancellation in the logarithmic formula.

The computation uses 96 positive-series terms for each needed moment, rational root bisection, and 384-bit and 768-bit ball evaluations with different grouping of the moment formula. Every final upper endpoint is rounded upward to ten decimal places by exact rational arithmetic. All analytic acceptances, original numerical bases, code and this proof are hashed into the output record. No new quadrature, geometric grid test, or unverified transport plan is used.

This proof was written before execution. New decimal claims require the completed accepted.json record beside it.
