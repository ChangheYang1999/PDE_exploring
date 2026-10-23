# A global derivative residual obstruction

Date: 2026-10-20. Status: independently reconstructed from the residual equation after reading the proposed diagnostic in the lead's rep4 audit. This is a necessary quantitative test on a candidate, not a distance-to-solution or existence theorem.

## 1. Hypotheses, notation and statement

Let ell>1 and let rho be a nonzero smooth density on the plane, even in x and odd in y. Let U be its canonical full-plane IPM inverse, with no added harmonic strain. Assume, for some q<1, the symbol bounds

    |D^j rho(X)|+|D^j U(X)| <= C_j (1+|X|)^(q-j), 0<=j<=4.

No transport equation is assumed. Define

    W=ell X+U, F=W.grad rho-rho,
    R=||grad rho||_infinity, V=||DU||_(infinity,Frob),
    sigma=||(DU+DU^T)/2||_(infinity,op),
    E=||D^3 rho||_2^2, beta=||D^3 U||_2/sqrt(E),
    eta3=||D^3 F||_2/sqrt(E), A=2ell-1.

Here D^j is the ordered full derivative tensor with its Euclidean contraction. Then0<E<infinity, D^3 F belongs to L2, and0<=beta<=1. The following bounds hold, where [z]_+=max(z,0):

    eta3 >= [A-3V-R-3(2+sqrt(2))sqrt(VR)]_+,               (1)
    eta3 >= [A-3sigma-R beta-9sqrt(VR beta)]_+,            (2)
    eta3 >= [A-Lambda(R+V)]_+,                            (3)
    Lambda=(1+3/sqrt(2)+sqrt((3/sqrt(2)-1)^2+81))/2.

All these tests are invariant under positive spatial scaling rho_lambda(X)=lambda rho(X/lambda), with ell fixed. In particular a canonical family with ell=1+D and R+V=O(D) has liminf_(D->0) eta3>=1, even if its pointwise normalized residuals tend tozero.

## 2. Finiteness and the canonical multiplier

The exterior bound D^3 rho=O(r^(q-3)) is square integrable because q<1. The same holds for U. If D^3 rho were zero, rho would be a polynomial of degree at most2. Strictly sublinear growth and the odd-y parity force that polynomial to be zero, contrary to the hypothesis. Thus E>0.

Differentiating F three times uses derivatives of rho through4 and U through3. Its linear terms have order O(r^(q-3)), and its nonlinear terms have order O(r^(2q-4)). These are in L2, so eta3 is finite. The differentiated canonical div-curl system has Fourier multipliers whose vector squared modulus is xi_x^2/|xi|^2<=1, yielding beta<=1. Any zero-frequency distributional difference lying in L2 is zero. No Fourier multiplier acting ambiguously on an undifferentiated growing density is needed.

## 3. Energy identity with a residual

Write T=D^3 rho. Differentiation gives

    W.grad T+(3ell-1)T+[D^3,U.grad]rho=D^3 F.

Pair with a smooth radial cutoff times T and integrate. Since div W=2ell, integration by parts gives the limit

    A E+<T,[D^3,U.grad]rho>=<T,D^3 F>.                    (4)

The cutoff error is bounded by a constant times the annular L2 mass of T because W=O(r). It tends tozero. Every commutator integral converges absolutely: its exterior integrand is O(r^(3q-7)), which is integrable for q<1. Smoothness handles the interior.

The terms with exactly one derivative on U have three slots. Their bound is3VE, or3sigma E after contracting the symmetric tensor in the differentiated slot: the skew part of DU has zero quadratic contraction. The term with three derivatives on U is bounded by R beta E. The three middle terms are bounded by

    3 ||D^2 U||_4 ||D^2 rho||_4 sqrt(E).

For any smooth vector or tensor field v with the relevant finite norms, integration by parts gives

    ||Dv||_4^2 <= 3 ||v||_infinity ||D^2 v||_2.

For completeness, integration of one derivative in I=integral |Dv|^4 gives

    I=-integral(v.Delta v)|Dv|^2
      -2 integral v_a (partial_i v_a)(partial_j v_b)(partial_ij v_b).

The second term is bounded by2 ||v||_infinity ||D^2 v||_2 sqrt(I). The first is bounded by ||v||_infinity ||Delta v||_2 sqrt(I). The full ordered Hessian satisfies ||Delta v||_2=||D^2 v||_2, by the L2 Fourier identity applied to its derivatives, or by two integrations by parts. The derivative decay controls the cutoff errors even when v is not in L2. Their sum proves the constant3. Bounding the Laplacian pointwise by sqrt(2)|D^2 v| instead gives the coarser constant2+sqrt(2). This is the same cutoff argument independently recorded in ../sharper_energy_strain_cap/PROOF.md, Section3. Applying it to v=DU and v=grad rho yields

    ||D^2 U||_4 ||D^2 rho||_4 <= 3 sqrt(VR beta) sqrt(E).

The coarser constant similarly yields(2+sqrt(2))sqrt(VR) sqrt(E). Insert these estimates in(4), use |<T,D^3 F>|<=sqrt(E)||D^3 F||_2, and divide by E. This proves(1)-(2). Orthogonality of the symmetric and skew parts of the trace-free DU gives sigma<=V/sqrt(2). Discarding beta<=1, the quadratic form in(sqrt(R),sqrt(V)) has matrix[1,9/2;9/2,3/sqrt(2)]. Its largest eigenvalue is Lambda, proving(3).

## 4. Scaling and two misleading small-residual mechanisms

For rho_lambda=lambda rho(X/lambda), the canonical inverse is U_lambda=lambda U(X/lambda). Hence W_lambda=lambda W(X/lambda) and F_lambda=lambda F(X/lambda). Both third derivatives have amplitude lambda^(-2), while two-dimensional L2 integration contributes lambda. Their L2 norms therefore both scale by lambda^(-1). The quantities R,V,sigma,beta,eta3 are unchanged.

The compact remote-strain family in ../near_one_noncompact_limits/PROOF.md has rho_L=L rho_1(X/L) at fixed ell. It has identically zero residual on B_L, but eta3 is independent of L. It is strictly positive: if D^3 F_1=0 then F_1 is a polynomial of degree at most2; compact support of the density makes F_1 compactly supported, forcing F_1=0. A nonzero bounded density cannot solve transport for a complete field, since rho(Phi_t X)=e^t rho(X) contradicts boundedness as t tends toinfinity. This excludes eta3=0 for this particular family, without evaluating its size.

The explicit family in ../vanishing_approximate_family/PROOF.md has ell=1+D and R+V<8D. Thus(3) gives eta3>=[1+2D-8Lambda D]_+. In particular liminf eta3>=1 as D tends tozero. The family is smooth and satisfies symbol bounds for each D>0, so the present hypotheses apply. This statement neither makes the constants in every symbol derivative uniform in D nor asserts convergence of eta3.

## 5. Scope and numerical use

The global L2 integrals in eta3 are essential. A value obtained on a finite box or sampled grid without a tail bound is not this quantity. The diagnostic requires differentiating the residual three times, so small sampled pointwise ratios and a small center defect do not determine it. It proves a residual obstruction only: it does not bound the distance to the unknown exact solution set. For an exact profile eta3=0, and these inequalities reduce to the already proved global energy restrictions. Neither a candidate nor a full-class contradiction follows.
