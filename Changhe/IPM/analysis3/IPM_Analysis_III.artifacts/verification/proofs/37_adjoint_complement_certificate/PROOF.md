# A finite-rank and adjoint certificate for a global inverse

Let H be a real or complex Hilbert space. All pairings below use a consistent inner-product convention; the norm estimates are independent of which slot is linear. Let L:D(L)->H be closed and densely defined. Suppose

    m ||g|| <= ||Lg||+||Kg||,  g in D(L), m>0,                     (G)

where K is bounded on H. Suppose e1,...,en are orthonormal and

    K=K_S+sum_i e_i <g,phi_i>,  ||K_S||<=delta.

Assume psi_i in D(L*) and ||L*psi_i-phi_i||<=epsilon_i. Set

    Psi=(sum_i ||psi_i||^2)^1/2,
    epsilon=(sum_i epsilon_i^2)^1/2.

## 1. The inverse certificate

For g in D(L), adjoint duality gives

    |<g,phi_i>| <= ||psi_i|| ||Lg||+epsilon_i ||g||.

Minkowski's inequality in Euclidean n-space yields

    (sum_i |<g,phi_i>|^2)^1/2 <= Psi ||Lg||+epsilon ||g||.

Orthonormality of the e_i therefore gives

    ||Kg|| <= (delta+epsilon)||g||+Psi||Lg||.

Insert this in(G). If delta+epsilon<m, then

    ||g|| <= (1+Psi)/(m-delta-epsilon) ||Lg||.                      (1)

Thus L is injective with closed range. If L is additionally Fredholm of index0, it is surjective, and(1) is its inverse bound. Neither closedness, dense definition nor(G) alone implies surjectivity. This is precisely the submitted Lemma IV.1.

For a nonorthonormal finite output family, write K_fin=U Phi with U:l2_n->H and use a certified upper bound M_U for ||U||. Then replace delta+epsilon by delta+M_U epsilon and1+Psi by1+M_U Psi. An exact Gram bound can improve both this and Psi; the Hilbert-Schmidt bounds above are sufficient.

## 2. Explicit stability under changes of transport

This paragraph supplies a conditional version of the theory author's uniformity argument, with its domains stated. Let H=L2(w dX), where w>0 off the invariant axes, log w has the weak derivatives used below, and W is a globally Lipschitz real vector field with W(0)=0. Suppose A=L+W.grad is a closed densely defined realization and each chosen psi_i belongs to both adjoint domains. Suppose also that

    m_W ||g|| <= ||Ag||+||Kg||,  g in D(A),                         (G_W)

with the same K and m_W>0. These are hypotheses, not consequences of a small finite matrix.

For smooth psi supported away from the singular axes, integration by parts gives

    (A*-L*)psi=-W.grad psi-[div W+W.grad log w]psi.                 (2)

The same identity holds on any larger common adjoint domain for which the products are in H and the integration-by-parts formula is valid. Let dW=||DW||_infinity, using the Euclidean operator norm. Since W(0)=0, |W(X)|<=dW |X|.

For the angular weight in the S2 proposal,

    log w=mu(log r)-2a log|cos theta|,
    M=ess sup|mu'|,

and an x-tangent W, one has

    |W.grad log w| <= (M+4a)dW.                                   (3)

Indeed |W|/r<=dW and |W1/x|<=dW. The identity

    tan(theta)W.grad(theta)
      =sin(theta)W2/r-sin^2(theta)W1/x

bounds the angular term by2dW. If div W is the constant2c/3, equations(2)-(3) give

    ||(A*-L*)psi_i||
      <= dW ||r grad psi_i||+[2|c|/3+(M+4a)dW]||psi_i|| =: p_i.

Consequently the adjoint defect vector is bounded by epsilon+p, with p=(sum_i p_i^2)^1/2, and

    ||g|| <= (1+Psi)/(m_W-delta-epsilon-p) ||Ag||                   (4)

whenever the denominator is positive. If A is Fredholm of index0, this is an inverse bound. For a family of fields, any common lower bound on the denominator makes(4) uniform.

The extra r in ||r grad psi|| is essential on an unbounded domain. A bare unweighted derivative norm does not bound W.grad psi when only DW and W(0) are known. Smooth compactly supported psi_i away from the axes automatically make these weighted derivatives finite. In a jet-plus-remainder Hilbert space, the corresponding adjoint formula must also include its jet rows and couplings; the plain L2 formula above must not be substituted for them without proof.

## 3. What must be computed or proved

To apply this to the radial Fredholm theorem V023/V031, one must first certify its global margin, then produce the actual K and a quantitative finite-rank split, then certify the complete adjoint defects. A generic statement that a commutator gains one derivative does not give delta: the low frequencies, the two spatial ends, the weight conjugation, and every cutoff term must all be included. A finite positive singular value of QLP is not a substitute for these adjoint defects.

CONFIRMED: Lemma IV.1 and the explicit conditional transport perturbation bound. OPEN: the actual S2 finite-rank split, adjoint solutions, and the resulting global numerical inverse bound. The moving-tail nonlinear formulation changes more than the fixed-background transport, as explained in V038, so its uniformity requires additional parameter estimates.
