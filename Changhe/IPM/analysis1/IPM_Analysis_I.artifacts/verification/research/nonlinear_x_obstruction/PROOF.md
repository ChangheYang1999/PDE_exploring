# The quadratic IPM remainder is not bounded from X times X to X

## Exact statement and space

Let L>0 and0<k<1 be fixed and define the weak weighted H1 norm

    ||h||X^2=int_(R2) (h^2+r^2|grad h|^2)w(r)dX,
    w(r)=L^6 r^-6(1+r^2/L^2)^(3/2-k).

For compact C5 densities let U[h] be the canonical decaying IPM velocity, with -Delta psi[h]=partial_x h and U[h]=(-psi_y,psi_x). Let Sigma(h)=psi_xy(0). On the parity class even in x and odd in y, write J(h)=a(0) whenever h=x^2 y a with continuous even-even factor. Consider

    Q(h)=U[h].grad h+(Sigma(h)/3)X.grad h.

There exists an explicitly specified sequence h_n of compact C5 densities with continuous even-even factors, J(h_n)=Sigma(h_n)=0, such that

    h_n in X, Q(h_n) in X,
    ||h_n||X ->0,  liminf ||Q(h_n)||X >0.                 (1)

Thus Q is not continuous at0 for the X topology on this exact constrained class, and no finite constant C can give ||Q(h)||X<=C||h||X^2 on an X ball of positive radius in this class. In particular a general nonlinear closing estimate of this form cannot be inferred from matrices using only X as the perturbation norm. This is not an assertion about stronger or graph norms, weighted spaces with more derivatives, a particular finite-dimensional family, an inverse, profile existence or nonexistence. It is not an IPM endpoint.

## Unit density and exact zero-strain compensation

Set

    H(Z)=Z_1^2 Z_2(1-|Z|^2)_+^6,
    H_delta(X)=x^2 y(1-r^2/delta^2)_+^6,
    g=-(56/3)(H_1-H_2).

The exact Green calculation gives Sigma(H_delta)=delta^2/56 and J(H_delta)=1. Hence J(g)=0, Sigma(g)=1 and g is C5 with support in r<=2. Near0,

    g=84 x^2 y r^2+O(r^7),

with differentiated polynomial remainders, so g belongs to X. Its factor is even-even and vanishes at0. Its canonical velocity is smooth off its support and locally C1 everywhere. The compact density is C5 and vanishes to the required orders at each support circle.

The canonical stream of H outside the unit disk is exactly

    psi_H=-(1/4032)r^-2 sin(2theta)-(1/13440)r^-4 sin(4theta)
         =-xy/[2016(x^2+y^2)^2]
          -xy(x^2-y^2)/[3360(x^2+y^2)^4].               (2)

Inside the disk it is a polynomial. Its quadratic term is xy/56. Consequently

    U[H]=(-x/56,y/56)+O(r^3),
    Q_H:=U[H].grad H=-(1/56)x^2 y+O(r^5).              (3)

In particular grad Q_H is not the zero polynomial. Formula(2), its first two derivatives, and the interior polynomial were independently verified in topic137; a fresh exact reconstruction will verify(2),(3) and the finite arithmetic used here.

## Four translated packets

Let epsilon=1/n^2, a=1/n, n>=2. For p_(s,t)=(4s,4t), s,t in{1,-1}, put

    P_n(X)=a sum_(s,t) H((X-p_(s,t))/epsilon).

All four coefficients have the same sign. Even x parity and odd y parity follow by relabeling the packet centers and using those parities of H. Each packet support is disjoint from both axes, the disk r<=2 and the other packet supports. Thus P_n has a continuous even-even factor and J(P_n)=0.

Translation invariance and the order-zero scaling of the canonical velocity give

    U[a H((X-p)/epsilon)]=a U[H]((X-p)/epsilon),
    psi[a H((X-p)/epsilon)]=a epsilon psi_H((X-p)/epsilon).

There is no extra affine strain: both sides give decaying canonical velocities. At X=0 the stream is in the exterior region. Differentiating(2) shows

    (psi_H)_xy(A,A)=-1/(2688 A^4).

The same value holds at the other three signed diagonal points by even-even parity of psi_xy; the mode4 contribution is zero on these diagonals. Take A=4/epsilon and include the scale a/epsilon from two physical derivatives of the stream. Summing the four packets yields the exact identity

    Sigma(P_n)=-a epsilon^3/172032.

Define

    h_n=P_n+(a epsilon^3/172032)g.                       (4)

Then J(h_n)=0 and Sigma(h_n)=0 exactly. Hence Q(h_n)=U[h_n].grad h_n, with the rank-one quadratic term absent. The definition uses exact rational n and coefficients; no fitted strain or approximate cancellation occurs.

## Vanishing X norm and membership of the quadratic image

All packet supports lie in a fixed compact annulus separated from0. On that annulus r,w and their reciprocals are bounded. Changing variables X=p+epsilon Z bounds the L2 part of one packet by C a epsilon and its gradient L2 part by C a. Summing four packets and the fixed g term gives

    ||h_n||X<=C a+(a epsilon^3/172032)||g||X ->0.          (5)

Here constants depend on fixed L,k and the chosen centers, never on n. The estimate uses exact weak derivatives; all functions are C5, so there are no jump measures.

For each n, Q(h_n) is C1 and compactly supported in the union of the five density support regions. The parity of h_n forces U[h_n](0)=0. Locally C1 velocity therefore gives U[h_n]=O(r), DU[h_n]=O(1) near0. From(4), h_n=O(r^5), grad h_n=O(r^4), D2 h_n=O(r^3) there. Thus Q(h_n)=O(r^5), grad Q(h_n)=O(r^4), and the two squared weighted radial integrands are O(r^5), which are integrable. On all remaining compact regions the integrands are bounded. Therefore Q(h_n) belongs to X. No uniform bound on its full norm is needed for the claim.

## A positive lower bound from one packet

Fix p=(4,4) and K={Z:|Z|<=1/2}. In p+epsilon K, the other three densities and g vanish identically. Thus

    h_n(p+epsilon Z)=a H(Z),
    U[h_n](p+epsilon Z)=a U[H](Z)+R_n(Z).

From(2), U[H](Y)=O(|Y|^-3), DU[H](Y)=O(|Y|^-4) for |Y|>=1. The other packet centers stay a fixed distance away. Their velocities are O(a epsilon^3) and their physical velocity derivatives O(a epsilon^3). The compensating term has coefficient a epsilon^3/172032 and U[g],DU[g] bounded on the fixed neighborhood of p. The chain rule therefore gives uniformly on K

    R_n=O(a epsilon^3),  grad_Z R_n=O(a epsilon^4).       (6)

All constants in(6) are independent of n. This is a direct far-field estimate for a fixed finite family, not an unproved general singular-integral L-infinity bound.

Since a^2=epsilon, substitution and differentiation yield

    Q(h_n)(p+epsilon Z)=Q_H(Z)+E_n(Z),
    ||E_n||_(C1(K))=O(epsilon^3).                        (7)

Indeed the correction is (a/epsilon)R_n.grad H; its size and Z derivative follow from(6), and a^2/epsilon=1. The derivative of R_n gives the still smaller O(epsilon^4) term. The rank-one term is zero by exact strain cancellation.

The gradient portion of the X norm restricted to this packet patch is

    int_K |p+epsilon Z|^2 w(|p+epsilon Z|)
          |grad_Z(Q_H+E_n)(Z)|^2 dZ.                   (8)

The factors epsilon^-2 from the squared physical derivative and epsilon^2 from area have canceled exactly. Uniform convergence of the weight on this compact patch and(7) show that(8) tends to

    |p|^2 w(|p|) int_K |grad Q_H|^2 dZ.                (9)

This number is positive. The polynomial grad Q_H is nonzero by(3), so it cannot vanish on the whole disk K. At a point where it is nonzero, continuity gives an open set of positive measure on which its squared norm is positive. The weight factor in(9) is finite and strictly positive. Since(8) is a nonnegative part of the full squared X norm, (9) proves the liminf assertion in(1). Equations(5) and(1) refute continuity and the quadratic bound.

## Verification and scope

The proof precedes new arithmetic. Reconstruct the unit Green polynomial and its quadratic product with one symbolic engine, and independently using rational radial ODE coefficients and Cartesian convolution. Check the nonzero degree3 coefficient and compute int_K |grad Q_H|^2/pi by two exact disk-moment formulas. Recompute the translated diagonal strain from the rational exterior stream and from a separate explicit derivative formula. Check all scaling factors and the coefficient172032. Exact JSON stores the finite coefficients and rational evidence. The positive integral is supporting evidence; the proof already follows from the explicit nonzero coefficient.

All h_n are exact constrained perturbations with strong center factorization. No exact stationary background is assumed or constructed. This local concentration obstruction concerns the broad X norm and the particular quadratic expression Q, not the stronger spaces in the lead's SPEC. It does not show small linearized residuals or that h_n are close in a graph norm. It cannot be used as a NO endpoint or to dismiss a correctly specified proof in stronger spaces.
