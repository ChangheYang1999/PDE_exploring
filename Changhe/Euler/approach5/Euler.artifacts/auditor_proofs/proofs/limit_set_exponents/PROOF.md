# A large forward exponent on every vortical backward limit set

## Statement

Let U be a C2 uniformly sublinear Euler profile, c>0, omega arbitrary, and let x satisfy Omega(x)!=0. Its compact backward limit set K supports a probability mu that is invariant and ergodic for the full B-flow and whose largest forward Lyapunov exponent chi is at least b=1+c. In particular this holds when K is entirely irrotational. If 0<c<1/2 and mu({B=0})=0, its spectrum is

    {chi,0,3c-chi},  chi>=1+c,  3c-chi<=2c-1<0,

and integral lambda_max(S) dmu>=1. The statement is a necessary condition, not an exclusion of such a limit set.

## Direct proof on the unit tangent sphere bundle

The complete B-flow has a compact set containing the entire negative orbit of x. Compactify the vector field outside a neighborhood of that set, preserving that orbit and K. The normalized derivative flow on the unit tangent sphere bundle is

    F_t(y,v)=(Phi_t y, D Phi_t(y)v/|D Phi_t(y)v|).

It is a continuous complete flow on a compact space. Its continuous instantaneous logarithmic growth is

    f(y,v)=v^T DB(y)v=c+v^T S(y)v.

For positive integer n, put x_n=Phi_-n x and v_n=Omega(x_n)/|Omega(x_n)|. Transport never vanishes on this orbit, and gives

    log|D Phi_n(x_n)v_n|
       =bn+log|Omega(x)|-log|Omega(x_n)|.

The final logarithm is bounded above, since the orbit lies in a compact set. Hence the time average of f along the length-n lifted segment is at least b-o(1). Let eta be a weak limit of its empirical probabilities. Shifting by any fixed time changes only two bounded-length pieces, so eta is invariant under the full normalized derivative flow. The base projections of those long segments spend asymptotically full time in every neighborhood of K, so eta is supported over K. Also integral f d eta>=b.

An ergodic component eta0 has integral f d eta0>=b. Its projection mu is full-flow ergodic on K. Birkhoff's theorem on the lift and Oseledets' theorem on the base imply that the logarithmic derivative growth in eta0-typical vector directions equals integral f d eta0 and cannot exceed mu's largest exponent. Thus chi>=b. This proof directly supplies an attained ergodic exponent and avoids replacing an unproved supremum by a maximum.

If B is nonzero almost everywhere for mu, its invariant tangent direction has exponent zero. Indeed D Phi_t B=B o Phi_t, and recurrence to a set where |B| is bounded below, together with compact upper boundedness and existence of the Oseledets exponent, forces that exponent to be zero. The determinant identity gives the sum 3c. The remaining exponent is therefore 3c-chi. Finally d log|D Phi_t v|/dt<=c+lambda_max S(Phi_t y), so ergodic averaging yields chi<=c+integral lambda_max S dmu.

## Audit of the cited subadditive route

The actual Schreiber 1998 manuscript, Theorem 1 on printed page 336, gives equality with a supremum over ergodic probabilities for a continuous subadditive function over a compact semiflow. It does not state that the supremum is attained. Morris, arXiv:1109.4615, Theorem A.3 on printed page 24 and Proposition A.5 on page 25, supplies attainment for a discrete compact system. A full-flow passage or the direct lift above is needed when the conclusion asks for a flow-ergodic measure. With that repair, the block-neighborhood argument in THEORY_B is valid.

Schreiber's printed page 342 contains the false sentence that every flow-ergodic measure is time-one ergodic. This particular step is repairable by ergodic decomposition and flow averaging; it should not be repeated. in the team records records the detail. The source files and retrieval checksums are in sources/subadditive.

## Other B11 claims

At Omega=0, DU=S is symmetric and DB=cI+S-omega J. The isometric change v(t)=exp(omega Jt)w(t) changes the variational equation to v'=(cI+exp(omega Jt)S(Phi_t y)exp(-omega Jt))v. This preserves the exponents of this particular cocycle, and proves the bounds between c+integral lambda_min S and c+integral lambda_max S. It does not say the exponents are independent of omega: the conjugated symmetric coefficient still depends on omega.

For an exact H0 counterexample to that matrix inference, U=(x,-y,0) has Omega=0 and solves the profile equation with P=-x^2-2omega xy for every omega. DB has eigenvalues c, c plus and minus sqrt(1-omega^2). Its largest exponent is c+1 at omega=0 and c at |omega|>1. This example is affine, not uniformly sublinear; it refutes the claimed algebraic implication, not the main decaying-profile conjecture.

The nilpotency statement DOmega^3=0 on the irrotational set is already A025. Its valid proof uses the transported derivative there (obtainable by differentiating the C1 flow identity), not an unjustified global third derivative of U. B11(b) and the precise conjugacy and bounds in B11(c) are CONFIRMED. Rotation-independence is REFUTED as a matrix inference.
