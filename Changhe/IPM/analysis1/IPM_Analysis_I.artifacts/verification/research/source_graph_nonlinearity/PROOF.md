Written 2026-10-21T23:21:07.006687+00:00 before new code.

# Failure of quadratic continuity in the weak graph norm at a noncentral equilibrium

## Statement, hypotheses and scope

Fix L>0, 0<k<1 and 0<alpha<1. Write r=|X| and let X denote the space of functions with weak first derivatives and finite norm

    ||h||_X^2 = integral_R2 [h^2+r^2|grad h|^2] w(r) dX,
    w(r)=L^6 r^(-6)(1+r^2/L^2)^(3/2-k).

Let rho be an even-x, odd-y density whose canonical velocity U[rho] has the corresponding parity. Assume rho is C^{2,alpha} locally and V=c_l X+U[rho] is C1 locally. Assume, for finite A,D,

    |grad rho|<=A r^(1+alpha), |D2 rho|<=A r^alpha, 0<r<=1,
    |grad rho|<=D r^(k-1), |D2 rho|<=D r^(k-2), r>=1.

Assume V(0)=0 and V(P)=0 for P=(p,0) with p>4. Parity also gives V(-P)=0. For compact C5 perturbations use the unique decaying canonical velocity, defined by -Delta psi[h]=partial_x h and U[h]=(-psi_y,psi_x). Put Sigma(h)=psi[h]_xy(0), E=X dot grad, G=E rho, and

    Lh=V dot grad h-h+U[h] dot grad rho+(Sigma(h)/3)G,
    Q(h)=U[h] dot grad h+(Sigma(h)/3)E h.

On the algebraic domain of even-x, odd-y functions with h,Lh in X and a continuous even-even center factor h=x^2 y b, put J(h)=b(0) and ||h||_graph=||h||_X+||Lh||_X. This theorem does not assume that this domain or its constrained subspace is complete.

There is an explicit sequence of compact C5 perturbations with J(h_n)=Sigma(h_n)=0 such that h_n,Lh_n,Q(h_n) belong to X and

    ||h_n||_graph ->0,
    liminf ||Q(h_n)||_X^2 >= p^2 w(p) E_H >0,             (1)

where E_H is the positive, exactly computed unit energy in topic141. Consequently Q is not continuous at zero for this particular graph norm, and no estimate ||Q(h)||_X<=C||h||_graph^2 can hold on any positive-radius graph ball containing this sequence. The compact perturbations preserve every prescribed exterior coefficient. This result does not concern stronger Sobolev graph norms, the lead's full SPEC norms, restricted finite-dimensional families, weaker image norms, a continuous inverse, or an existence or nonexistence endpoint.

The canonical normalized modal_v2 trial is an instance only after the accepted topic138 growth and regularity theorem, topic89 exact equilibrium certificate, and topic169 discharge of its moment-archive premise have all been checked. The exact p is the unique root in topic89's rational bracket. It is not replaced by a numerical midpoint.

## Unit stream, translation and exact normalization

Use

    H(Z)=Z_1^2 Z_2 (1-|Z|^2)_+^6,
    H_delta(X)=x^2 y(1-r^2/delta^2)_+^6,
    g=-(56/3)(H_1-H_2).

The explicit canonical Green calculation in topics137 and141 gives J(H_delta)=1, Sigma(H_delta)=delta^2/56, hence J(g)=0 and Sigma(g)=1. The function g has support in r<=2 and satisfies g=84 x^2 y r^2+O(r^7), with differentiated polynomial remainders. For the unit stream, outside |Z|=1,

    psi_H(x,y)=-xy/[2016(x^2+y^2)^2]
               -xy(x^2-y^2)/[3360(x^2+y^2)^4].          (2)

It is polynomial inside. The stream and derivatives needed here match at the unit circle. Write W=U[H]. Direct differentiation gives

    |W(Z)|<=C min(|Z|,|Z|^(-3)),
    |DW(Z)|<=C min(1,|Z|^(-4)),                         (3)

interpreting the first branches for |Z|<=1 and the second for |Z|>=1. Also W=(-x/56,y/56)+O(|Z|^3), so

    q_H=W dot grad H=-x^2 y/56+O(|Z|^5).

Its gradient is a nonzero polynomial on the half-unit disk K. In particular

    E_H=integral_K |grad q_H|^2 dZ
       =pi*1552530047839457441465148479
           /23683970648207968389305777258496000 >0.     (4)

The exact rational is inherited from the two independent computations in141, not recomputed here unless stated in the evidence.

For epsilon=1/n^2, a=1/n and n>=2, define two translated packets

    P_n(X)=a[H((X-P)/epsilon)+H((X+P)/epsilon)].

They have even-x, odd-y parity. Their supports are disjoint from r<=2 and from one another. Each has a factor y because the packet centers lie on the x axis. On its support x is bounded away from zero. Division by x^2 gives a continuous even-even global center factor, extended by zero wherever the packets vanish. Thus J(P_n)=0.

Translation and dilation of the canonical stream give psi[a H((X-P)/epsilon)]=a epsilon psi_H((X-P)/epsilon). From (2), for t nonzero,

    partial_xy[xy/(x^2+y^2)^2]_(t,0)=-3 t^(-4),
    partial_xy[xy(x^2-y^2)/(x^2+y^2)^4]_(t,0)=-5 t^(-6),
    (psi_H)_xy(t,0)=(t^(-4)+t^(-6))/672.

Both signed centers have the same mixed derivative. Including the factor a/epsilon yields exactly

    sigma_n=Sigma(P_n)=(a/336)(epsilon^3/p^4+epsilon^5/p^6).

Set h_n=P_n-sigma_n g. Then J(h_n)=Sigma(h_n)=0 exactly and Q(h_n)=U[h_n] dot grad h_n. Moreover sigma_n=O(a epsilon^3), with constants depending on p. No approximate strain cancellation or per-packet quadratic normalization is used.

## Membership and the linear graph estimate

The estimates w(r)<=C r^(-6) near zero and w(r)<=C r^(-2k-3) at infinity give G in X: the squared radial integrals are bounded by multiples of integral_0^1 r^(-1+2alpha)dr and integral_1^infinity r^(-2)dr.

On a fixed compact annulus containing both packet supports, w and r are bounded above and below by positive constants. A change of variables gives ||P_n||_X<=C a. The fixed g belongs to X by its order-five zero at the center. The same argument as topic137 proves Lg in X. To make its use at radius2 explicit, on every compact annulus the C1 velocity and C2 density bounds are finite; near zero g=O(r^5) with two differentiated bounds and U[g]=O(r), DU[g]=O(1); outside its support U[g]=O(r^(-3)), DU[g]=O(r^(-4)). The product-rule integrals are respectively integrable at zero and bounded by integral_1^infinity r^(-10)dr at infinity. The rank-one term is G because Sigma(g)=1, with coefficient1/3. Hence ||sigma_n g||_graph<=C a epsilon^3.

Since V vanishes at each packet center and DV is uniformly bounded on their fixed neighborhoods, |V(X)|<=C epsilon on each support. There |P_n|<=C a, |grad P_n|<=C a/epsilon and |D2 P_n|<=C a/epsilon^2. Therefore the value of V dot grad P_n-P_n is O(a) and its first derivative is O(a/epsilon). Support area is O(epsilon^2). It follows that

    ||V dot grad P_n-P_n||_X<=C a.                     (5)

All these derivatives are weak derivatives of C1 functions; no interface measures occur.

It remains to bound F_n=U[P_n] dot grad rho globally. Choose fixed disjoint disks of radius d<1 around P and -P, separated from r<=1. In one such disk let q be the distance to its center. Bounds (3) give for its own packet

    |U|<=C a, |DU|<=C a/epsilon,          q<=epsilon,
    |U|<=C a epsilon^3 q^(-3),
    |DU|<=C a epsilon^3 q^(-4),           epsilon<=q<=d.

If epsilon>d, the estimates below still hold after increasing constants, or those finitely many n may simply be discarded. The other packet contributes O(a epsilon^3) to the velocity and its physical derivative throughout that disk. The background derivatives, weights and radius are bounded there. The squared X norm of F_n over q<=epsilon is at most C a^2. Over epsilon<=q<=d, its dominant derivative integral is bounded by

    C a^2 epsilon^6 integral_epsilon^d q^(-7)dq<=C a^2.

The lower derivative and value terms have smaller bounds; using d<1, their powers are dominated by this integrand. Thus both disks together contribute at most C a^2.

On the remaining fixed compact annulus separated from these disks and zero, U[P_n] and DU[P_n] are O(a epsilon^3). Near zero, parity gives U[P_n](0)=0, and the exterior formula gives DU[P_n]=O(a epsilon^3) uniformly for r<=1. Therefore U[P_n]=O(a epsilon^3 r), and

    |F_n|+r|grad F_n|<=C a epsilon^3 r^(2+alpha), r<=1.

Its squared X integral is bounded by C a^2 epsilon^6 integral_0^1 r^(-1+2alpha)dr. Finally, for r>=2p+4, (3) and the fixed centers give

    |F_n|+r|grad F_n|<=C a epsilon^3 r^(k-4).

Its squared X integral is bounded by C a^2 epsilon^6 integral_(2p+4)^infinity r^(-10)dr. These estimates prove F_n in X and ||F_n||_X<=C a. Including sigma_n G/3, (5) and the fixed compensator gives

    ||h_n||_X+||Lh_n||_X<=C a ->0.                     (6)

This proof bounds the full nonlocal linear expression on the entire plane, not only its values on the density support.

For each n, Q(h_n) is C1 and compactly supported. Near zero h_n=O(r^5), grad h_n=O(r^4), D2 h_n=O(r^3), while U[h_n]=O(r) and DU[h_n]=O(1). Thus Q(h_n)=O(r^5), grad Q(h_n)=O(r^4); its two squared weighted radial integrands are O(r^5). This proves Q(h_n) in X. The compact C5 densities and explicit canonical velocities also obey the perturbation regularity and sublinear-growth requirements of topic138's algebraic domain.

## A nonzero limiting quadratic image

On P+epsilon K only the packet centered at P is present in the density. Its velocity is a W(Z)+R_n(Z). The opposite packet and the compensator are uniformly separated from this patch. The rational exterior stream and the smooth fixed U[g] give

    ||R_n||_(C0(K))=O(a epsilon^3),
    ||grad_Z R_n||_(C0(K))=O(a epsilon^4).

Since a^2=epsilon, direct substitution yields

    Q(h_n)(P+epsilon Z)=q_H(Z)+E_n(Z),
    ||E_n||_(C1(K))=O(epsilon^3).

Indeed E_n=(a/epsilon)R_n dot grad H. Its differentiated terms have orders epsilon^4 and epsilon^3. Sigma(h_n)=0 eliminates the full quadratic rank-one term exactly.

Restricting the gradient part of the squared X norm to this patch and changing variables gives

    integral_K |P+epsilon Z|^2 w(|P+epsilon Z|)
                    |grad_Z(q_H+E_n)|^2 dZ.

This converges to p^2 w(p) E_H by uniform convergence on K. It is a nonnegative portion of ||Q(h_n)||_X^2. Positivity of (4) proves (1). Along the sequence the full residual difference F(rho+h_n)-F(rho)=Lh_n+Q(h_n), with c_l(h) normalized by Sigma, also cannot tend to zero in X by the reverse triangle inequality. This last statement concerns the difference expression, and does not assume that each background residual separately belongs to X.

## Application and verification requirements

Check all accepted pins of137,138,141,89 and169. Use their full statements, addenda and resolutions. In particular the moment-archive premise in89 must be discharged by169, while its other restrictions remain. The bracket endpoints a_0=4841405518533377/562949953421312 and b_0=4841405518533711/562949953421312 satisfy4<a_0<b_0, so their exact unique root supplies p>4. No new root enclosure is claimed.

Before any final acceptance, independently recompute the axis strain by symbolic differentiation and exact rational quotient-rule polynomial differentiation, verify the scaling coefficients and integrability exponents, and bind the inherited positive energy and parent verdicts. The analytic proof precedes code. Request actual Claude Opus5.5 review, record the actual model and complete response, and adjudicate it afterward with independent reasoning. Computation, a model reply, or a parent summary alone is insufficient. This weak graph-norm obstruction is not a decisive IPM endpoint.
