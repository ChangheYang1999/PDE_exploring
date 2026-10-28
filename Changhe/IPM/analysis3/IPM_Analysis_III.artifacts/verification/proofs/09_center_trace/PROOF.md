# The cubic center coefficient is not closed in the weak graph topology

## Exact statement

Let L0>0, 0<k<1, 0<alpha<1 and

    w(r)=L0^6 r^(-6)(1+r^2/L0^2)^(3/2-k),
    ||h||_X^2=integral (|h|^2+r^2|grad h|^2)w(r) dX.

All derivatives in this norm are weak derivatives. Let rho be a fixed density and V a C1 vector field near the closed unit disk with V(0)=0. Assume, with finite constants,

    |grad rho| <= C r^(1+alpha), |D2 rho| <= C r^alpha  (r<=1),
    |grad rho| <= C r^(k-1), |D2 rho| <= C r^(k-2)     (r>=1),
    |V|<=C r, |DV|<=C                                 (r<=1).

Assume rho is C2 locally off zero, with the displayed bounds there. Set G=X dot grad rho and

    Lh=V dot grad h-h+U[h] dot grad rho+gamma c[h]G,

where gamma is any fixed real number and U and c are the canonical full-plane IPM operators of proof 01. In particular gamma=1/3 is the normalized linearization. No exact solution identity is assumed.

For 0<delta<=min(1,L0)/2 define

    H_delta(X)=x^2 y (1-r^2/delta^2)_+^6,
    B_delta=(4 H_delta-H_(2delta))/3.

Then H_delta and B_delta are C5, compactly supported, have the required parity, and have continuous even-even center factors. They and their full images belong to X. Their exact center and strain values are

    J(H_delta)=J(B_delta)=1,
    c[H_delta]=delta^2/56,
    c[B_delta]=0.                                          (1)

Moreover

    ||H_delta||_X=O(delta),
    ||L H_delta||_X=O(delta)+O(delta^(2+alpha))+O(delta^2),
    ||B_delta||_X+||L B_delta||_X -> 0.                     (2)

Let D be any linear subspace on which the expression is defined, h and Lh belong to X, the pointwise factor coefficient J exists and is linear, and all B_delta belong to D. In the graph norm ||h||_X+||Lh||_X, every J level is dense within every nonempty fixed-c level of D. In particular J is not continuous, and its kernel is not closed relative to D. Adding the exact constraint c[h]=0 does not repair this defect.

For a fixed constant K, an estimate ||h||_X<=K||Lh||_X on {h in D: c[h]=0,J(h)=0} is equivalent to the same estimate on {h in D:c[h]=0}. Thus the unclosed center condition cannot create an estimate in this topology. This is not a claim about norms with an explicit J coordinate or a stronger center topology.

## Canonical velocity and exact strain of the bump

Write H=H_1. Its angular expansion is

    H(r,theta)=r^3(1-r^2)_+^6 (sin theta+sin 3theta)/4.

The strain formula therefore gives

    c[H]=(1/4) integral_0^1 r(1-r^2)^6 dr=1/56.

Degree-zero homogeneity of the canonical velocity gives U[H_delta](X)=delta^3 U[H](X/delta); the degree-one derivative c consequently scales as delta^2. This proves (1).

For completeness the velocity estimates do not require an unstated multiplier theorem. Put chi(v)=(1-v)^6 on [0,1]. The stream forcing is

    partial_x H = [r^2 chi(r^2)+(r^4/2)chi'(r^2)] sin 2theta
                  +(r^4/4)chi'(r^2) sin 4theta.

For angular frequency n=2,4, solve by the canonical Green formula

    psi_n(r)=[r^(-n) integral_0^r s^(n+1) f_n(s)ds
              +r^n integral_r^infinity s^(1-n)f_n(s)ds]/(2n).

The inner stream functions are finite Cartesian polynomials. There is no logarithmic term: the forcing for n=2 starts at degree two, and for n=4 at degree four. The outer stream functions are multiples of r^(-2)sin 2theta and r^(-4)sin 4theta. Matching follows directly from the integral formula. Hence W=U[H] has

    |W|<=C r, |DW|<=C                       (r<=1),
    |W|<=C r^(-3), |DW|<=C r^(-4)            (r>=1).

Scaling gives

    |U[H_delta]|+r|DU[H_delta]| <= C delta^2 r       (r<=delta),
    |U[H_delta]|+r|DU[H_delta]| <= C delta^6 r^(-3)  (r>=delta). (3)

No freely chosen affine velocity is present.

## Full-image membership and graph estimates

The weight satisfies w<=C r^(-6) for r<=1 and w<=C r^(-2k-3) for r>=1. The hypotheses give

    |G|+r|grad G| <= C r^(2+alpha)   (r<=1),
    |G|+r|grad G| <= C r^k           (r>=1).

Its squared norm is bounded by the integrals of r^(-1+2alpha) at zero and r^(-2) at infinity, so G belongs to X.

On its support H_delta and its first two derivatives are bounded by C r^3, C r^2, C r, respectively, with constants independent of delta. Polynomial expansion in r/delta proves these bounds. The same powers bound V dot grad H_delta-H_delta and its first derivative. Consequently the X norms of H_delta and this transport expression are O(delta). C5 matching at the support boundary excludes interface measures.

For Q_delta=U[H_delta] dot grad rho, the product rule and (3) bound |Q_delta|+r|grad Q_delta| by

    C delta^2 r^(2+alpha)   (0<r<=delta),
    C delta^6 r^(alpha-2)   (delta<=r<=1),
    C delta^6 r^(k-4)       (r>=1).

Squaring and inserting the weight and area element gives upper bounds

    C delta^4 integral_0^delta r^(-1+2alpha) dr,
    C delta^12 integral_delta^1 r^(2alpha-9) dr,
    C delta^12 integral_1^infinity r^(-10) dr.

Each is O(delta^(4+2alpha)), since 0<alpha<1 and delta<=1. Thus ||Q_delta||_X=O(delta^(2+alpha)). The rank-one term has norm |gamma|delta^2||G||_X/56. This proves all membership statements and (2), first for H_delta and then for B_delta by linearity. In B_delta the rank-one term vanishes exactly.

## Density, closedness, and the scaling caveat

For any h in D and real j set

    h_delta=h+(j-J(h))B_delta.

It has c[h_delta]=c[h], J(h_delta)=j and converges to h in graph norm. To see that ker J itself is not closed, choose any B_d with a fixed d, take j=0 in this construction and pass to the limit B_d, whose coefficient is one. This proves the claimed relative nonclosedness without making any assertion about completeness of D.

Apply a proposed estimate on c=J=0 to h-J(h)B_delta for any h in ker c and let delta go to zero. Continuity of the two graph-norm components gives the estimate on all of ker c. The reverse implication is immediate.

If a nonzero K in D also satisfies c[K]=0 and LK=0, then K-J(K)B_delta is a normalized approximate kernel and rules out such an estimate. For an exact smooth profile the scaling tangent may furnish K, but its domain membership must be checked separately. At a numerical trial the exact algebraic identity is LK=F-X dot grad F, so it need not be zero. No numerical trial is being promoted to an exact solution here.

## Relation to stronger center information

For any smooth cutoff chi equal to one on the unit disk and fixed 0<=s<4, the same density packets satisfy ||chi H_delta||_Hs ->0 and ||chi B_delta||_Hs ->0. Indeed H_delta=delta^3 H(X/delta), and a Fourier change of variables gives ||H_delta||_Hs<=C_s delta^(4-s)||H||_Hs for delta<=1. The fixed bump H belongs to Hs for these orders: its zero extension is C5 with compact support and bounded weak derivatives through order five. This shows that adding only such a local Hs norm of h to X does not make J continuous. It does not by itself prove convergence of L H_delta in a local Hs norm, and no such claim is needed above. At s>=4 this scaling estimate no longer gives convergence; no endpoint assertion is made.

## Dependencies

The canonical kernel and scaling are proved in proof 01. The present Green computation and all weight exponents are explicit. The supplied Analysis I graph_center_norm and FIXED_STRAIN proofs have been independently checked in deriving this statement. The code verifies the finite polynomial forcing, exact strain, exterior stream coefficients, and radial exponents. The exact modal density satisfies the displayed background hypotheses, as checked in proof 05. Application to raw X3 still requires its separate regularity audit.
