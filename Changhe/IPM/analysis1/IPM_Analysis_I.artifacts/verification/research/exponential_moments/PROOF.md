# Certified exponential-polynomial cell moments

Status: exact identity and remainder bound. This is an integration primitive, not a residual or inverse certificate.

## Statement

Let lambda,a,b and c_0,...,c_d be real numbers, with a<b, and p(t)=sum_j c_j t^j. Put h=b-a and write p(a+h u)=sum_{j=0}^d d_j u^j. Then

integral_a^b exp(lambda t)p(t) dt
= h exp(lambda a) sum_{j=0}^d d_j Phi_j(lambda h),

Phi_j(z)=sum_{n=0}^infty z^n/[n!(j+n+1)].

For any integer N>=0 with |z|<N+1, truncation before n=N has remainder bounded by

|z|^N/[N!(j+N+1)(1-|z|/(N+1))].

These statements remain valid for interval inputs when every operation and the added symmetric error use outward arithmetic. A wide interval is not a sharp certificate; no precision claim is inferred solely from a formal formula.

## Proof

Substitute t=a+h u and expand the exponential. Absolute uniform convergence on u in [0,1] allows termwise integration, giving integral u^{j+n}=1/(j+n+1). The ratio of successive absolute series terms for n>=N is

|z|/(n+1) times (j+n+1)/(j+n+2) <= |z|/(N+1)<1.

Comparison with the geometric series bounds the complete tail. The coefficients d_j equal h^j sum_{l=j}^d binom(l,j)c_l a^{l-j}, by the binomial theorem. These identities also hold when lambda=0, with Phi_j(0)=1/(j+1), without division by lambda.

If |lambda|h is large, partition [a,b] into finitely many equal cells for which the product of the absolute lambda bound and the cell width is at most one. Apply the same formula on each subcell and sum the outward balls. This avoids alternating exponential-series cancellation on a large argument. The number of cells is chosen with a certified upper bound, and all cells together cover the original interval exactly when rational endpoints are used.

## Contrast with primitive subtraction

The finite antiderivative formula involving inverse powers of lambda is also algebraically correct. On a small cell it subtracts large nearly equal numbers and can lose the entire positive integral in ordinary floating point. The scaled moment expansion evaluates a quantity of the size of the cell integral, with an explicit tail. It also handles lambda=0 continuously. Its role is to provide an independently written alternative for checking a future modal Green certificate; it does not make the surrounding fitted coefficients, matching conditions or PDE residual exact.
