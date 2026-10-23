# Same-node inverse comparison for a fixed hydrostatic trial

Result304. Written before the candidate computation. This is an auxiliary hydrostatic audit, not an elliptic IPM profile test.

Fix the binary64 N=96, M=24, c=2 trial in result276. Let g be its exact finite local Chebyshev representation. At any physical point define
V1=-integral_y^infinity g_x(x,t) dt,
V2=integral_0^y t g_xx(x,t) dt + y integral_y^infinity g_xx(x,t) dt.
The finite representation has the vertical tail convergence established in result187. These are the prescribed full vertical inverse and its symmetry gauge. Their defining integrals, not a finite box, are the target.

For a fixed density jet J=(g,g_x,g_y), set R(J,V)=(cx+V1)g_x+(cy+V2)g_y-g. Define Nf=|(cx+V1)g_x|+|(cy+V2)g_y|+|g| and Nv=|g|+|xg_x+yg_y|+|V1g_x+V2g_y|. For two velocities and the same jet,
R(J,V)-R(J,W)=(V-W) dot grad g.
This follows by cancelling the three identical terms cxg_x, cyg_y and -g. All pointwise ratios below are recomputed with their own denominators. A ratio is undefined if its denominator is zero.

The producer's stored nodes_Fmax is a maximum of the absolute residual rows together with normalization rows, as the residual function concatenates R, a0-1 and K-1. It is not max |R|/Nf. This claim will be checked by static AST on the frozen solver sources. Hence comparing a reported 3.9e-8 nodes_Fmax directly with a normalized 5.0e-3 sample is not a dimensionally consistent error ratio. At a point with specified Nf, both absolute and normalized residuals can instead be displayed explicitly.

Our principal computation uses the existing separately implemented Cartesian analytic jets and physical dyadic Gauss panels with the power tail t=R/u^(1/(1-p)). At three refinement settings it covers the physical point (30,1), the independently reconstructed collocation point nearest (1998,65.4), and (1998,65.4) itself to distinguish rounded from reconstructed coordinates. Radial nodes are r=L sqrt((1+t)/2)/(1-t)^P from the saved t array; angles are (j+1/2) pi/(2M). This reconstructs the declared node recipe, not the exact GPU-produced floating point coordinates.

A diagnostic second inverse is written separately from the quadrature definition in the producer's static source: Gauss on [0,min(1,y)], equal log panels on [1,y], and a tail t=y+(1+y)(u/(1-u))^3. The baseline orders are 24, 8 and 80, with a common panel count ceil(4 log10(max(y_nodes,10))). This implements the stated rule using our own density evaluator, not a producer map matrix or producer code. Repeating it with analytic g_xx and with the centered difference of our g_x at h=1e-5(1+|x|) separates those two diagnostic approximations. It does not reproduce possible errors in the producer's map assembly or its interpolation and does not prove the producer maps equal this reconstruction.

For an explicit check take g=y(1+x^2+y^2)^(-1/4). Put A=1+x^2+y^2. Then g_x=-xy A^(-5/4)/2 and g_xx=-y A^(-5/4)/2+5x^2 y A^(-9/4)/4. Direct integration gives V1=x A^(-1/4); incompressibility and odd-y symmetry give V2=-integral_0^y [(1+x^2+t^2)^(-1/4)-x^2(1+x^2+t^2)^(-5/4)/2] dt. The latter compact integral is evaluated independently at high precision. Differentiating both formulas recovers the required derivatives and V2(x,0)=0. Test the principal inverse against these formulas at small and far points, and test the telescoping residual identity using exact rational arithmetic on stored binary64 operands.

The numerical error controls are empirical refinement and manufactured comparisons, not certified enclosures. The three principal rules share a binary64 integrand, so they do not control common integrand error. Independent 72/108-digit scalar differentiation checks the local jet at the candidate probes; it does not certify the complete inverse integrand. A discrepancy observed on these probes does not establish a global maximum, a cause for all residual plateaux, infinite-sequence convergence or nonconvergence, or optimizer uniqueness.

The claim that two improved quadrature solves either prove quadrature-induced nonconvergence or prove a discretization problem is logically invalid without further assumptions. For any two finite observed states there exist convergent and nonconvergent continuations, obtained respectively by keeping the subsequent state constant or alternating two distinct states. A solver also need not return a unique stationary point. Therefore finite matched experiments can support a causal hypothesis but cannot establish that dichotomy. The primary endpoint remains UNRESOLVED.

Dependencies: result187 independent Cartesian hydrostatic evaluator; result233 power-tail inverse manufactures and parent regression; result287 scalar differentiation and arithmetic safeguards; result276 frozen N96 state. No result from this audit is asserted before execution and review.
