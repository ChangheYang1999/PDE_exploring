# The energy inequality on the maximal transport domain

## Statement

Use the scalar transport P=B.grad+c, smooth variable-order reduction A and matrix M_B of proof 147. Assume additionally a=B.grad s>=0. Let v belong to H^s(C) and suppose Pv belongs to H^s(C) in the distributional sense. Then, for every eta>0 and 0<epsilon<=1/32,

 -Re<APv,Av>
 >=<M_B RAv,RAv>-eta||v||H^s^2
                         -C_eta||v||H^(s-epsilon)||v||H^s.       (1)

The same result holds for the constant-order cofactor transport; then a=0. No density of a smooth normalized core in a transport graph norm is assumed. This supplies the maximal-domain version of Q1 needed by the high-frequency estimate.

## The conjugated distributional equation

Put w=Av. Proof 147 proved the identity

 APv=B.grad w-a log<D>w+Qw+Ev,                           (2)

where Q is an L2-bounded operator consisting of the scalar c-N B.grad Lambda and the left order-zero principal operator, and

 ||Ev||_2<=C||v||H^(s-epsilon).                          (3)

Equation(2) extends as a distributional identity from smooth v to every v in H^s. Indeed Pv belongs at least to H^(s-1), A maps that space into H^-1, and all the terms on the right have continuous maps into H^-1. Multiplication by the finite-regularity coefficients is legitimate on that space. Approximate v in its ordinary H^s norm to identify the distributions. Under the additional hypothesis Pv in H^s, equations(2)-(3) imply

 F:=B.grad w-a log<D>w in L2.                           (4)

We regularize w in this equation, rather than presuming that an approximation of v preserves a nonlinear-looking axis constraint or the transport graph.

## Two Friedrichs commutators

Let J_n be a real even smooth Fourier cutoff equal to one near zero and supported in frequencies |xi|<=2n. It converges strongly to the identity on every fixed Sobolev space and commutes with log<D>. Its convolution kernel is K_n; on the cylinder use its periodization in the angular variable.

For a bounded Lipschitz vector field B,

 [J_n,B.grad]:L2->L2

is uniformly bounded and converges strongly to zero. To prove the bound, integration by parts in the input variable writes its kernel as a sum of

 grad K_n(X-Y).(B(Y)-B(X)),  and  -K_n(X-Y) div B(Y).

Their row and column integrals are bounded by the Lipschitz norm of B, since the first kernel has the factor |X-Y| and the derivative of K_n has scale n. Convergence on smooth H1 functions follows directly from J_n->I and multiplication by B. Density and the uniform bound give strong convergence on L2. The same proof works on the whole cylinder, without integrable coefficients.

For a bounded Lipschitz scalar a,

 [J_n,a]log<D>:L2->L2

is also uniformly bounded and converges strongly to zero. Here is a bound which avoids applying log<D> as a bounded L2 operator. First

 [J_n,a]:H^-1->L2                                      (5)

has a uniform bound. Every f in H^-1 can be written f=f_0+div F with f_0,F in L2 and total norm bounded by C||f||H^-1, by taking f_0=<D>^-2 f and F=-grad<D>^-2 f. Apply the commutator kernel K_n(X-Y)(a(Y)-a(X)) to this decomposition and integrate by parts on F. The resulting differentiated kernel has the same two Schur bounds as above. The undifferentiated kernel has a bounded, in fact O(1/n), L1 norm. This proves (5). Since log<D>:L2->H^-1 is bounded, the desired uniform L2 bound follows. On smooth functions log<D>w belongs to L2 and [J_n,a] tends strongly to zero. Density again completes the proof.

## Regularized energy and the limit

Set w_n=J_n w. By (4) and the two commutator results,

 B.grad w_n-a log<D>w_n=J_n F+o_(L2)(1).                 (6)

Each w_n belongs to every fixed Sobolev space. Integration by parts in B.grad w_n is valid on the infinite cylinder: first insert a smooth radial cutoff of radius R, then let R grow. The boundary error is bounded by C/R times ||w_n||_2^2 and tends to zero. All other terms are integrable.

Insert (2) into (6), take the real inner product with w_n, and pass to the limit in the bounded order-zero terms and in Ev. For the logarithmic term use proof 143, which gives

 Re<a log<D>w_n,w_n>>=-C||w_n||H^(-1/32)^2.              (7)

Its hypotheses hold because a>=0 and a has at least three bounded derivatives. There is no need to assert that the logarithmic quadratic form of the limiting w is finite or converges. Discard its nonnegative part using (7), and use strong convergence of w_n in H^(-1/32). The order-reduction estimate in proof 144 bounds ||w||H^(-1/32) by ||v||H^(s-1/32). Since epsilon<=1/32, its square is bounded by C||v||H^(s-epsilon)||v||H^s.

The remaining left principal form is converted to the matrix form exactly as in proof 147. The conversion contributes eta||v||H^s^2 plus C_eta times the product of lower and high norms. Equation(3) contributes the same product. This proves (1).

## Application to the coupled X_s domain

Let h belong to D_s={h in X_s:T h in X_s}, which is the maximal domain verified in proof 126. Then v=h/b satisfies P_v v=(Th)/b in H^s. For u=chi h/(bp),

 P_u u=chi(Th)/(bp)+(W.grad chi)h/(bp).

The extra term is supported in the fixed overlap where p is nonzero and s=sigma. Its H^sigma norm is bounded by the high bulk norm. Thus the scalar hypotheses above hold for both components. The cofactor can be extended outside a larger angular sector with finite-regularity coefficients; its equation outside the support has no new term, and the off-sector order-reduction tails are controlled by proof 144. Neither independent regularization of the components nor the argument on w_n is claimed to preserve the zero-axis trace. It does not need to: the final inequality is proved for the original h on its exact closed domain.

This removes the graph-density gap in the high-frequency energy argument. The final assembly with coupling, penalty and compact terms is a separate algebraic step.
