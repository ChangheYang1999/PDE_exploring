# Exact supersolutions for sharper tuned-series radii

Status: PROVED. The independently derived rational supersolutions and all input and radius inequalities passed. This verifies the theory part's proposed sharper radii using the already independently reviewed positive-majorant argument.

## Statement and dependencies

Use the exact c=3 recurrence and the two sextic roots b1,b2 of topic119, with the unique compatible harmonic tuning. For nonzero real epsilon and initial profile epsilon(sin(theta)+bj sin(3theta)), the density, stream and potential series converge with every appropriately weighted derivative on r>=R whenever

    R > 26100000000000000 |epsilon|^(3/2), j=1,
    R >   475000000000000 |epsilon|^(3/2), j=2.

The potential has only the order3 and order6 logarithmic corrections described in121. These are local exterior stationary solutions; no global stationary extension is asserted. The dependencies are the proved TheoremT (119), the positive majorant equations and iteration argument of120, the potential theorem121, and certified response lower bounds.

## Exact certificate criterion

Let Y=(W,U,V,E) and Phi(z,Y) be the four polynomial right sides in119. Take kappa=28/3, and use

    a=12807/10000, sigma_*=38/1000000 for j=1,
    a=16464/10000, sigma_*=15/10000 for j=2.

The required input inequalities are 1+bj<=a and inf_(k>=2)|sigma_k(bj)|>=sigma_*. They follow from the root isolations and the all-index polynomial response comparison certificate of123; that arithmetic certificate, rather than any finite response scan, is checked again here. It is also permissible to use the theory part's separate all-index comparison at these weaker constants.

Set c=Phi(0,0), J=partial_Y Phi(0,Y). The verified J is constant, nonnegative and strictly lower triangular, so Q=(I-J)^(-1)=I+J+J^2+J^3 is nonnegative. The equation is equivalent to

    Y=G(z,Y):=Qc+Q[Phi(z,Y)-c-JY].

Every coefficient of G is nonnegative, and every term after Qc is divisible by z. If an exact positive rational vector Yhat satisfies Phi(z0,Yhat)<=Yhat, then

    (I-J)Yhat >= c+[Phi(z0,Yhat)-c-JYhat].

Multiplication by Q preserves this inequality and yields Yhat>=G(z0,Yhat). Iteration of G from zero is therefore bounded by Yhat at z0. Its nonnegative formal coefficients stabilize degree by degree, because each nonconstant iteration term has a positive factor of z. Monotone convergence of the sums at z0 proves absolute convergence of the unique formal majorant there. In particular all coefficients are bounded by a constant times z0^(-n).

The certificate uses z0=1138/10^14 for j=1 and z0=1644/10^13 for j=2. The exact vectors Yhat are retained in checks.json, with every rational component of Phi(z0,Yhat) and every positive margin. Approximate fixed-point iteration may propose Yhat, but is not used in the proof: only the final exact rational inequalities matter.

For the stated decimal radius bounds Rj, also check exactly that

    Rj^2 z0^3 > 1.

Thus Rj>z0^(-3/2), and R>Rj implies |z|=r^(-2/3)<z0. Finite angular bandwidth, polynomial derivative costs and the geometric coefficient bound give every weighted derivative on this strict exterior, by119/121. Multiplying the initial data by epsilon multiplies order n by epsilon^n, so the radius scales by |epsilon|^(3/2).

The numerical search for a fixed point or a critical z is not a certified location of the true singularity. The theorem states only sufficient exterior radii.
