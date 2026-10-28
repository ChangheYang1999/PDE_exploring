# A fixed order whose monotonicity survives small perturbations

## Statement

Choose the smooth order constructed in proof 130 by the repeller-block, exit-time and fixed-scale smoothing method. There is a constant kappa_s>0 such that, everywhere on the cylinder,

 W.grad s >= kappa_s |grad s|.                         (1)

In particular every bounded real perturbation B with ||B||infinity<=kappa_s/2 satisfies

 (W+B).grad s >= (kappa_s/2)|grad s|>=0.                (2)

The same fixed order works for the entire such ball. Constants are qualitative; no numerical kappa_s is claimed. The theorem concerns the explicit proof 130 order. Mere nonnegativity W.grad s>=0 for an arbitrary order does not imply (1).

For the same fixed order and escape Lambda, the pointwise matrix inequality of proof 142 also persists under small C1 perturbations of the field and small bounded perturbations of the scalar coefficients, with an explicitly described loss. These facts settle two sign conditions needed in a uniform high estimate. They do not settle the rough-coefficient transport commutator or a uniform nonlinear inverse.

## Proof of robust monotonicity

Use precisely the notation of proof 130. The C1 exit-time cutoff g has ||grad g||infinity<=L<infinity. After convolution by the fixed radius e, its smooth version g_e obeys

 ||grad g_e||infinity<=L,
 W.grad g_e>=m:=kappa_1-e||DW||infinity L>0
                  wherever 1/3<=g_e<=2/3.             (3)

The second inequality is proved there by ensuring the whole convolution ball lies in 1/4<g<3/4. Choose that fixed e with m>0. The final order is

 s=s_0+(sigma-s_0)F(g_e),

where F is smooth, nondecreasing, constant below1/3 and above2/3. If F'(g_e)=0, both sides of (1) are zero. Otherwise (3) gives

 W.grad s >= (sigma-s_0)F'(g_e)m,
 |grad s| <= (sigma-s_0)F'(g_e)L.

Taking kappa_s=m/(L+1)>0 proves (1), including L=0 without division by zero. Since the constructed order is nonconstant, L is in fact positive. Cauchy-Schwarz then gives

 (W+B).grad s >= (kappa_s-||B||infinity)|grad s|,

which proves (2). The estimate is uniform at both ends. It does not require the support of grad s to be compact, and does not infer a positive lower bound for F' near its flat endpoints.

## Perturbation of the finite matrix margin

Write the fixed unperturbed bulk or cofactor energy matrix as

 M=(div W/2-c+N W.grad Lambda)I-s_* sym DW-P+L_0 W W^T,

where s_* is respectively s or sigma. The same expression with W'=W+B and c'=c+d has difference

 M'-M=[div B/2-d+N B.grad Lambda]I-s_* sym DB
                         +L_0(W B^T+B W^T+B B^T).      (4)

The coupling matrix P is unchanged in the quasilinear formulation with fixed background coupling. In dimension2, with the Euclidean matrix operator norm, |div B|/2<=||DB||op and ||sym DB||op<=||DB||op. Consequently, pointwise,

 ||M'-M||op
 <=(1+sigma)||DB||infinity+||d||infinity
   +N||grad Lambda||infinity||B||infinity
   +L_0[2||W||infinity||B||infinity+||B||infinity^2].    (5)

Thus M>=mu I implies M'>=(mu-E)I, with E the right side of (5). On the cofactor sector the same formula holds with its scalar d and the same fixed constants. If the coupling also changes by Delta P, add ||Delta P||infinity to E. This is an exact elementary matrix estimate; it does not need a new compactness choice of N or L_0.

For an axis-tangent perturbation the divided cofactor scalar is controlled by C1. On a fixed vertical sector, B_theta vanishes at the vertical axis. The mean value formula bounds B_theta/cos theta by a fixed sector constant times ||partial_theta B_theta||infinity. The remaining cot theta term is smooth and bounded there. Hence d=beta B_t+(p'/p)B_theta has a bounded continuous extension and obeys a bound by C||B||C1. This statement is only a supremum bound; it asserts no surplus Sobolev regularity of the divided coefficient.

## Dependencies and scope

Proof 130 proves the exit-time construction, the global gradient bound for g, the strict inequality on the convolution transition strip and all specified constant-order regions. Proof 142 proves the original matrix margin for finite N,L_0. The present argument uses these exact constructions, so it supplies a fixed order for small perturbations of the actual field. To deduce a uniform high Fredholm or inverse estimate one must still prove the rough-coefficient commutator, the corresponding maximal-domain and semigroup facts, and uniform control of the compact and lower-order terms. The false full Kato-Ponce estimate identified in proof 151 cannot replace these obligations.
