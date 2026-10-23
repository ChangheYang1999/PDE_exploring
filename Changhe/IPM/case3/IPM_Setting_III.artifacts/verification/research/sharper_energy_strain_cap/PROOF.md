# Sharper gradient energy bounds and a conditional strain exclusion

Date: 2026-10-20. Status: independent audit of lead ener1 P3, P9-P11. These are necessary bounds and an exclusion under an additional uniform strain hypothesis, not a full-class NO result.

## 1. Hypotheses, notation and statements

Let ell>1 and let rho,U be an exact smooth full-plane IPM profile in the primary class:

    (ell X+U).grad rho=rho, div U=0, curl U=-rho_x,
    rho even in x and odd in y, U the canonical sublinear inverse,
    a=rho_y(0)!=0, DU(0)=diag(D,-D), D=ell-1.

Use the independently established symbol bounds |D^j rho|+|D^j U|<=C_j(1+r)^(p-j), p=1/ell<1, at infinity. Define Euclidean/Frobenius norms

    R=||grad rho||_infinity, V=||DU||_(infinity,Frob),
    S=(DU+DU^T)/2, sigma=||S||_(infinity,op),
    E_k=||D^k rho||_2², beta_k=||D^k U||_2/sqrt(E_k), k>=2.

D^k denotes the ordered full derivative tensor, not an unweighted list of multiindices. Then0<E_k<infinity and0<=beta_k<=1. The sharper necessary bounds are

    D<=2sigma+R beta_2,
    2ell-1<=3sigma+R beta_3+9sqrt(VR beta_3),               (1)
    R+V>=(2ell-1)/Lambda,
    Lambda=(1+3/sqrt(2)+sqrt((3/sqrt(2)-1)^2+81))/2.       (2)

Numerically Lambda is approximately6.0954523201. Additionally, under the extra hypothesis sigma<=D,

    R=|a|, V<=sqrt(2D²+a²/2),
    1-D<=|a|+9sqrt(|a|sqrt(2D²+a²/2)).                    (3)

In particular no profile in this subclass has0<D<=1/2 and0<|a|<=1/400. The strain cap has not been proved for the primary class and cannot be omitted.

## 2. Tensor energy and cancellation of the skew strain

For each ordered k-tuple I, differentiate transport and commute the derivatives through U.grad. Multiplying by D_I rho, summing and integrating with radial cutoffs yields

    ((k-1)ell-1)E_k=-integral D^k rho:[D^k,U.grad]rho.      (4)

The cutoff transport flux is bounded by C times the annular L² mass of D^k rho, and tends tozero because k>=2 and p<1. The symbol bounds make every commutator product integrable. The differentiated div-curl equations give the L² multiplier norm bound beta_k<=1. There is no zero-frequency harmonic ambiguity: a difference supported at Fourier frequency0 that lies in L² is zero. If E_k=0, rho is a polynomial of degree at mostk-1; sublinear growth makes it constant and odd parity makes it zero, contradicting a!=0. The complete cutoff proof is also supplied in ../small_gradient_exclusion/PROOF.md.

Fix one derivative slot in the term with exactly one derivative on U. Holding the other k-1 indices fixed gives the quadratic contraction v_i (partial_i U_j) v_j. Its skew part is zero because v_i v_j is symmetric. Its absolute value is bounded by sigma |v|². Summing each of the k slots gives k sigma E_k. This is pointwise algebra, so no angular-parity cancellation is assumed.

The term with all k derivatives on U is bounded by R beta_k E_k using tensor Cauchy-Schwarz and the multiplier bound. For k=2 these are the only terms, giving the first inequality in(1).

## 3. A vector-valued interpolation inequality with constant3

For v a finite-dimensional vector or tensor field with the decay of grad rho or DU, integrate one derivative in I=integral|Dv|^4:

    I=-integral (v.Delta v)|Dv|²
      -2 integral v_alpha (partial_i v_alpha)
                       (partial_j v_beta)(partial_ij v_beta).

The first term is at most ||v||_infinity ||Delta v||_2 I^(1/2). The second is at most2||v||_infinity ||D²v||_2 I^(1/2), by pointwise Cauchy-Schwarz followed by its integral form. The Fourier identity ||Delta v||_2=||D²v||_2 holds for the full ordered Hessian. It can alternatively be obtained by integration by parts with cutoffs; the symbol decay makes the derivative-cutoff terms vanish in L² even if v itself is not in L². The boundary term in the displayed fourth-power integration also vanishes by this decay. Thus

    ||Dv||_4²<=3||v||_infinity ||D²v||_2.                 (5)

This proof works for vector and matrix v with Euclidean/Frobenius pointwise norms. No componentwise constants are lost.

For k=3, the middle commutator has three terms. Its contraction in(4) is bounded by

    3 sqrt(E_3)||D²U||_4||D²rho||_4
    <=9 sqrt(VR beta_3) E_3,

using(5) with v=DU and v=grad rho. Together with Section2, this gives the second bound in(1).

## 4. Converting the strain norm and comparing origin restrictions

S is trace-free in two dimensions, so its eigenvalues are opposite and |S|_Frob²=2|S|_op². The skew part of DU has Frobenius square (curl U)²/2=rho_x²/2. Orthogonality of symmetric and skew matrices gives

    sigma<=V/sqrt(2), V<=sqrt(2sigma²+R²/2).              (6)

Discard beta_3<=1 in(1) and use sigma<=V/sqrt(2). The resulting quadratic form in (sqrt(R),sqrt(V)) has symmetric matrix

    [1,9/2;9/2,3/sqrt(2)].

Its largest eigenvalue is Lambda, which proves(2). This is an optimized bound for these estimates, not a claim of a sharp PDE constant.

The independent origin values imply R>=|a|, sigma>=D and V>=sqrt(2)D. Thus the k=2 bound is automatically satisfied just using sigma>=D; it gives no additional restriction on a profile with the known center strain. For the earlier coarser bound (2ell-1)<=C_*(R+V), C_*=6+3sqrt(2)/2, the origin already makes it automatic when

    D>=1/(C_*sqrt(2)-2),

or when |a|>=(2ell-1)/C_*. Therefore that coarser bound is informative only below these thresholds. The ell threshold is less than1.106; equality in a necessary bound is not an exclusion. The sharper Lambda improves the threshold but still does not give a full-class contradiction.

## 5. The uniform strain cap and the explicit excluded subclass

Assume sigma<=D. Since U(0)=0, the fundamental theorem of calculus along a radial line gives

    X.U(X)=integral_0^1 X.S(tX)X dt>=-D|X|²,
    X.(ell X+U)>=|X|².

The smooth globally Lipschitz field W=ell X+U has a complete flow. Along a backward orbit, its radius is at most e^t times its radius at time0, for t<=0, hence every backward orbit tends tozero. Differentiating transport gives, along the flow,

    d(grad rho)/dt=-(D I+DU^T)grad rho,
    d|grad rho|²/dt=-2D|grad rho|²-2(grad rho).S(grad rho)<=0.

For any fixed X, compare its gradient with the gradient at time t<0 and then let t tend to minus infinity. Smoothness and convergence to the origin give |grad rho(X)|<=|a|. Equality holds at the origin. Thus R=|a|, and(6) proves the V bound in(3). Substitution in(1), using3sigma<=3D and beta_3<=1, gives the final inequality in(3).

For0<D<=1/2,0<|a|<=1/400, its left side is at least1/2. Its right side is at most

    1/400+9sqrt((1/400)sqrt(1/2+1/320000))<1/2.

For an elementary rational check, sqrt(1/2+1/320000)<71/100, so the right side is below1/400+(9/200)sqrt(71), which is less than1/2 because9sqrt(71)<199/2; squaring gives5751<39601/4. Thus there is a strict contradiction. The weaker rational upper bound suffices, and no numerical root location is required.

## 6. Dependencies and open scope

This proof uses canonical inversion, symbol estimates, center relations and the independently verified tensor energy identity. The improved constant3 and symmetric-strain contraction are derived here independently. The strict cap sigma<=D is an added global condition, stronger than a local center value or absence of trapped trajectories. Nothing here establishes that cap. The high-order commutator remainder has not been shown to vanish after division by kE_k, so no limiting conclusion sigma>=ell is inferred.
