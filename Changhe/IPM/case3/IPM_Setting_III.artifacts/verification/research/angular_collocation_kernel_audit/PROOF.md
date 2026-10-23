# A smooth kernel of midpoint angular sampling

Written UTC 2026-10-22T03:07:18.922784+00:00 before the finite checker. This is an audit of a sampling mechanism mentioned in numerics note165. It does not authenticate that note's numerical results.

## Statement and notation

Fix an integer M>=1 and midpoint angles theta_j=(j+1/2)pi/(2M), j=0,...,M-1, in the positive quadrant. There exists a real, nonzero C-infinity function E on R^2, even in x and odd in y, with E and all its derivatives rapidly decaying, such that E(r cos(theta_j),r sin(theta_j))=0 for every r>=0 and every j. Thus samples on these rays alone give no finite bound on the supremum of an otherwise unrestricted smooth function with these parities and decay. This is a statement about sampling functions. It does not claim that E is the transport residual of an admissible IPM solution or of a density in a prescribed finite basis.

Let P_M(x,y)=Re((x+i y)^(2M)), an exact real homogeneous polynomial. For any nonzero real K, put

    E_K(x,y)=K y P_M(x,y) exp(-(x^2+y^2)).

The binomial expansion gives

    P_M(x,y)=sum_{k=0}^M (-1)^k binom(2M,2k) x^(2M-2k)y^(2k).

## Complete argument

Every monomial of P_M has even powers of both variables. Hence E_K is even in x and odd in y. Being a polynomial times a Gaussian, it is smooth on the entire plane, including the origin and both axes. Any derivative is again a polynomial times the Gaussian and tends to zero faster than any power at infinity. This justifies all regularity and decay claims without polar-coordinate assumptions at r=0.

In polar coordinates P_M=r^(2M)cos(2M theta), so

    E_K(r,theta)=K r^(2M+1) exp(-r^2) sin(theta) cos(2M theta).

At theta_j, 2M theta_j=(j+1/2)pi, and the cosine is exactly zero. For M>=2, at theta=pi/(2M) the cosine is -1 and the sine is nonzero. For M=1, theta=pi/6 has nonzero sine and cosine(2theta)=1/2. At any r>0 these provide a nonzero value. Scaling K changes that value without changing any nodal sample. Therefore no bound of the form sup|E| <= C max_sample|E| can hold for all such functions, even if every radius on every fitting ray is sampled. The zero right hand side and nonzero left hand side already contradict it for K=1.

Writing z=cos(2theta), the same missed factor is the Chebyshev polynomial T_M(z), since T_M(cos u)=cos(Mu). Its defining recurrence is T_0=1, T_1=z, T_{m+1}=2zT_m-T_{m-1}; the identity follows by the cosine addition formula and induction. At the midpoint angles, the values z_j are its M distinct roots in (-1,1). A polynomial q(z) of degree<M that vanishes at all z_j is identically zero by the elementary bound on the number of roots. Thus the linear span sin(theta)q(cos2theta), deg q<M, has injective sampling on these M angles. The counterexample has degree M in z, just outside that span. These two facts must be stated together: collocation is not defective for every restricted linear space, but a nonlinear residual may have higher angular degree than the sampled density. This last possibility is not a claim about any actual computed field.

If the grid is changed to J=3M midpoint angles theta'_j=(j+1/2)pi/(2J), T_M(cos2theta) cannot vanish at all J angles. The J distinct z values exceed its degree M. Oversampling therefore detects this specific function somewhere; it does not by itself prove a residual bound, convergence, or lack of other errors.

## Finite diagnostic and dependencies

Implement the recurrence independently with integer coefficient lists. Compare its substitution z=(x^2-y^2)/(x^2+y^2), after multiplication by (x^2+y^2)^M, against the binomial formula for P_M at exact integer points, and also compare coefficients symbolically. This tests the formula for selected M only; the induction above proves it for all M. Verify exact normalized values at rational z via recurrence against independent angle-free complex polynomial arithmetic at rational x,y. A floating-point plot is unnecessary and no finite diagnostic proves the exact trigonometric zero.

This elementary result needs no external numerical result. Its relevance to the actual128x32 state remains OPEN until independent evaluation identifies its residual angular content with sufficient precision and a separately implemented inverse. No claim that the standard inverse attenuates high modes is made. Numerics note165 states that its earlier filtering claim was withdrawn; that withdrawal is context, not proof of a physical mechanism.

No JavaScript/TypeScript, servers/listeners/tunnels, RLScience, Lean/Lake, producer-code execution, other-lane writes, posting or contact with people. Primary full-plane IPM remains UNRESOLVED.
