# Dyadic energy for the variable-order reduction

## Statement

Use the cylinder C=R times S1, the order s, the escape Lambda and the fixed N of proof 144. Let sigma=25/4, s_min=41/20, and let psi_j, j>=0, be real smooth inhomogeneous dyadic Fourier cutoffs with sum_j psi_j(xi)^2=1. Their dilates have uniformly bounded derivatives and fixed finite overlap. Set

 A=Op(exp(N Lambda)<xi>^s), A_j=A psi_j(D),
 J_s v=(A_j v)_(j>=0), R=grad<D>^(-1).

The quantization here is global left quantization. The conclusions for the cofactor order sigma use the same definitions with s replaced by sigma. For every sufficiently small epsilon>0, in particular epsilon<=1/5120:

 ||J_s v||_(l2 L2)<=C||v||H^s,
 ||v||H^s<=C(||J_s v||_(l2 L2)+||v||H^(s-epsilon)),       (1)
 ||J_s v||_(l2 H^(-r))<=C_r||v||H^(s-r), 0<=r<=1.        (2)

Let P_0=W.grad+c_0 with the actual W^(7,infinity) background coefficients of proof 147. Write

 a_0=W.grad s,
 M_0=(div W/2-c_0+N W.grad Lambda) I-s sym DW.

For smooth v one has

 -Re sum_j <A_j P_0 v,A_j v>
 =sum_j <M_0 R A_j v,R A_j v>
   +Re sum_j <a_0 log<D>A_j v,A_j v>+E(v),              (3)

where for every eta>0,

 |E(v)|<=eta||v||H^s^2+C_eta||v||H^(s-epsilon)||v||H^s. (4)

The sums in (3) can equivalently be interpreted through finite partial sums and their limits. On the maximal domain, the logarithmic sum is discarded using its lower bound before passage to the limit. This statement does not require the logarithmic operator by itself to map that domain to L2.

The coupling-form estimate of proof 145, the penalty estimate of proof 146, and the off-sector estimates of proof 144 hold with every scalar L2 norm or inner product replaced by its square-summed dyadic counterpart. The compact map and constants can change, but remain independent of the input. These assertions concern the fixed background.

## Frequency-local estimates used in the proof

Put w_j=exp(N Lambda)2^(j s). Proof 156 proves the moderate-weight estimate

 w_j(X)/w_j(Y)<=C(1+2^j d(X,Y))^M.                       (5)

On a j-th annulus write A_j=w_j Q_j. The symbol of Q_j is (<xi>/2^j)^s psi_j and has uniform scaled order-zero bounds. Its kernel is bounded by C_L 2^(2j)(1+2^j d)^(-L). This gives the first estimate in (1) by Schur and finite overlap.

We will also use the following elementary annular composition observation. Suppose a composition or an adjoint expansion has a first omitted term with one frequency derivative. Each frequency derivative of an annular symbol gives 2^(-j), while each spatial derivative of w_j divided by w_j costs only C(1+j). Taylor's formula with integral remainder for the spatial argument in the kernel composition therefore bounds the omitted operator, between the corresponding weighted annular L2 spaces, by

 C_L (1+j)^L 2^(-j).                                    (6)

The number L is fixed by the finite number of derivatives used. The part with spatial separation larger than a fixed multiple of 2^(-j) is estimated by integrating in frequency sufficiently many times and (5); the arbitrarily high kernel decay absorbs the moderate-weight power. If a second frequency cutoff has index k, the same integrations give arbitrary decay in |j-k| when the two annuli are separated. The polynomial (1+j)^L is absorbed by 2^(j d) for any fixed d>0. Thus the square sum of a family of such relative-order-minus-one remainders is bounded by C||v||H^(s-epsilon) for every fixed epsilon<1, after choosing d<1-epsilon. A finite number of low-frequency terms has the same bound without a gain factor. This is also a direct kernel proof of the uniform annular version of the smooth calculus used in proof 144.

No spatial derivative of a rough coefficient is taken in this observation unless it is explicitly part of the relevant composition. Smooth coefficients use it directly. The actual W^(7,infinity) coefficient uses the finite Taylor argument below; rough coupling coefficients use approximation as in proof 145.

## Frame estimates and off-sector terms

On a slightly enlarged j-th annulus, Op((<xi>/2^j)^(-s)) is a left parametrix for Q_j without its final cutoff. The composition remainder obeys (6). Apply the same weighted Schur estimate to this inverse and sum in j. For all large j its remainder is absorbed. The finitely many remaining j are bounded by the lower norm in (1). This proves the second estimate in (1).

For (2), compose <D>^(-r) with A_j. Its leading term is the annular reduction of order s-r; the omitted terms obey (6) relative to that order. The first part of (1), applied to s-r, proves (2). Here s-r>=21/20>0, so the same kernel and dyadic norm arguments apply. In particular the negative norm comparison has no frequency-dependent constant.

If u is supported in the fixed smaller vertical sector, the kernels of (1-chi_wide) A_j u and (1-chi_wide) R A_j u have a fixed positive angular separation. Their frequency integrations give a bound C_K 2^(-jK)||u||H^(sigma-epsilon), for any prescribed K after increasing the number of integrations. The finite low-frequency terms are uniformly smoothing and obey the same weaker lower-norm estimate. The square sums therefore satisfy the off-sector bounds of proof 144. They do not retain exact support.

## The extra cutoff term in the background transport energy

Apply the kernel Taylor proof of proof 147 directly to each A_j. Its kernel obeys

 |K_(A_j)(X,Y)|<=C_L 2^(j(2+s(X)))(1+2^j d(X,Y))^(-L).

Taylor expansion of W_l(Y)-W_l(X) to degree6 has a C^(6,1/2) remainder. Schur's test therefore bounds the remainder operator on Dv by C 2^(-j/4)||Dv||_2, since max s-13/2=-1/4. The integral for d>=1 obeys the same bound after increasing L. This sequence is square summable, and ||Dv||_2 is controlled by the lower norm. The same expansion treats [A_j,c_0]v, with no input derivative. All its terms are lower order. Every polynomial Taylor term of degree at least2 in the transport commutator is the bounded coefficient partial^alpha W_l times Op(partial_xi^alpha a_j)partial_l v. It has exact input frequency support comparable to j and relative order at most minus1; (5)-(6) bound its square sum by the lower norm.

The first Taylor term is

 sum_(i,l) (partial_i W_l) Op(partial_(xi_i) a_j) partial_l v / i.

Differentiating a_j=exp(N Lambda)<xi>^s psi_j splits this into the usual term with s xi_i xi_l/<xi>^2 and the extra term with symbol

 e_j(X,xi)=exp(N Lambda)<xi>^s
              sum_(i,l) partial_(xi_i) psi_j partial_i W_l xi_l.

The usual term converts to s sym DW in the matrix form exactly as in proof 147, using a uniform smooth approximation of DW followed by (6). The extra quadratic sum is Re sum_j <Op(e_j)v,A_j v>. Its leading symbol is

 exp(2N Lambda)<xi>^(2s) psi_j
          sum_(i,l) partial_(xi_i) psi_j partial_i W_l xi_l.

It vanishes after summation because sum_j psi_j partial_(xi_i) psi_j=0. This cancellation is pointwise in (X,xi), including the inhomogeneous low-frequency cutoffs. For the form remainder, first approximate DW uniformly by a smooth bounded matrix. The replacement costs an arbitrarily small multiple of ||v||H^s^2, since both sequences are bounded annular order-zero operators after reduction. The smooth adjoint/composition error has one frequency derivative and obeys (6), hence has the lower-norm product bound in (4). Its constants may depend on the approximation, as allowed. This is the same order of choices used for the matrix form in proof 147.

Finally differentiation in X gives the exact terms -N(W.grad Lambda)A_j v and -(W.grad s)A_j log<D>v. The commutator of log<D> with A_j has relative order minus1 with finitely many logarithms, so (6) replaces the latter expression by -(W.grad s)log<D>A_j v with a lower square-summed error. Integration by parts gives div W/2. These observations prove (3)-(4).

There is no unaccounted endpoint term from a partial frequency sum. Each extra-cutoff quadratic term is absolutely summable by the bounded annular order-zero estimate and Cauchy-Schwarz. Alternatively its boundary principal term is supported on a fixed number of annuli at the last frequency and tends to zero because the high-norm square sum converges.

## Coupling and penalty

For clarity about the extension of proof 145, localize first to finitely many radial patches. A smooth local order-zero coupling has a smooth principal symbol p_0(X,xi). The difference between A_j C v and p_0(X,D) A_j v obeys (6); its high-frequency square-sum tail tends to zero as an operator from H^s. Its finitely many low-frequency pieces are compact after the fixed spatial localization. Consequently this difference is compact into l2(L2). The same assertion for the actual local coefficients follows by their H^(51/8) approximation from proof 145: the multiplication and order-zero mapping norms are uniform after applying J_s, by (1), and can be made arbitrarily small. The cofactor principal identity and the compact axis row are exactly those of topics141 and140. Finally proof 138's input and output tail estimates, followed by the bounded map J_s, remove the finite-patch restriction with an arbitrarily small high error. This proves the square-summed coupling estimate with a compact map plus the stated small and lower errors. A compact map into the sequence space is represented by a compact seminorm on X_s, as in proof 145.

For the penalty, apply the pre-equation estimate of proof 146 to each v_j. Commuting W.grad across psi_j costs order zero, so after measuring the transport input at order s-1 this is a lower-order square-summed term. The same finite Taylor argument supplies this assertion for W^(7,infinity). The result is

 (sum_j ||W.R A_j v||_2^2)^(1/2)
 <=C||W.grad v||H^(s-1)+eta||v||H^s+C_eta||v||H^(s-epsilon). (8)

The cofactor version is identical after adding its fixed cutoff forcing. Inserting the fixed equation and the lower-space bound for C_R gives the dyadic version of proof 146. All constants are fixed before any later small perturbation is chosen.

## Interpretation on a maximal domain

For each fixed j, A_j maps L2 into every finite ordinary Sobolev space: its input frequency is bounded, the symbol and its spatial derivatives are bounded, and the same kernel estimates apply to output derivatives. Thus A_j v is in H1 even if v is only in H^s. Integration by parts against a bounded Lipschitz field is legitimate, by truncation in t. The exact formulas extend distributionally. One first sums through a finite index, bounds or discards the logarithmic forms from below, and then takes the index to infinity. The square-sum bounds above control all other terms. This establishes the energy inequality without a graph-density assertion.

## Dependencies and scope

The proof uses the explicit kernel and moderate-weight arguments of proof 156, the finite Taylor expansion of proof 147, and the fixed-background coupling, penalty and support results in topics140-146. It verifies a dyadic formulation of those results. It does not itself supply positivity for a perturbed field or a perturbed inverse.
