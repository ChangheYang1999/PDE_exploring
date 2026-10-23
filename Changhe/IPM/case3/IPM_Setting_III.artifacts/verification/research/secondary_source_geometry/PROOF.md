# Finite-order secondary source geometry and a cubic-axis search

Date: 2026-10-20. Status: independent derivation, external review pending. This concerns the secondary branch only.

## 1. Hypotheses and conclusions

Assume the full smooth coupled PDE, parities, canonical inverse and sublinear density/gradient growth in PROMPT, with ell>1. Suppose rho(0,y)=e_m y^m+O(y^(m+2)), where m>=3 is odd and e_m!=0. Set p=1/ell and lambda_x=2ell-1/m. Result12 proves

    c=1/m-ell, DW(0)=diag(lambda_x,1/m),
    rho=e_m y^m+O(r^(m+2)),
    rho(0,y)~K y^p, K/e_m>0.

Then rho is divisible by y^m in a neighborhood of zero, in the smooth sense, with rho/y^m tending to e_m there. The following conditions are equivalent:

(a) Hdyn: zero is the only equilibrium and every nonzero orbit comes from zero backward and escapes forward.
(b) W1(x,0)>0 for every x>0.
(c) rho/e_m>0 on the upper half-plane.

Under these conditions rho/y^m is smooth on the entire plane and has the sign of e_m, including its extension to the x-axis. Its far-field trace vanishes to exactly order m at the endpoints and

    c1(1+r)^(p-m) <= rho/(e_m y^m) <= C1(1+r)^(p-m)       (1)

with positive constants depending on the profile. This does not prove that any secondary profile exists, that its dynamics satisfies these conditions, or that all secondary profiles have a finite nonzero axis jet. Flat axis traces remain outside this statement.

## 2. Vanishing of lower transverse jets

Let w(x)=W1(x,0), v1(x)=partial_y W2(x,0)=2ell-w'(x), and g_j(x)=partial_y^j rho(x,0) for odd j. Near zero w(x)=lambda_x x+O(x^3), v1(x)=1/m+O(x^2). Differentiate transport j times in y. If all lower odd g_i are identically zero on an axis interval, every lower Leibniz term vanishes and

    w g_j'=(1-j v1)g_j.                                 (2)

For j<m, division on x>0 close to zero gives

    g_j'/g_j=s_j/x+O(x), s_j=(1-j/m)/lambda_x in (0,1),

on any nonzero solution. The general solution of the linear equation is C x^s_j exp(O(x^2)). Such a function cannot be C1 at zero unless C=0. Starting with j=1 and inducting through the odd j<m proves g_j identically zero near zero. Even transverse derivatives vanish by parity. Repeated smooth division by y, or Taylor's formula with integral remainder in y, therefore gives rho=y^m G near zero with smooth G and G(0)=e_m. In a smaller disk G/e_m>0, so the nodal set there is exactly the x-axis.

For j=m the same equation propagates nonzero g_m along any axis interval without a zero of w. In particular, if(b) holds, all lower g_j remain zero globally, while g_m/(m! e_m)>0. Smooth division then holds globally.

## 3. Dynamics and strict sign

The sublinear velocity gives W.X>0 outside a large disk. The set K of forward-bounded points is the intersection of its nested backward-flow images. These are compact connected disks, so K is compact and connected. Exact transport makes rho vanish on K, since rho(Phi_t X)=e^t rho(X) and the forward orbit is bounded. These arguments use only completeness, sublinear growth, positive divergence 2ell and transport, and do not use a nonzero first derivative of rho.

If(b) holds, every nonzero x-axis point escapes forward. Near zero the only nodal points are on that axis by Section2. Therefore zero is isolated in K. Connectedness gives K={0}. To conclude backward convergence, note that backward trajectories stay bounded. Their density tends to zero. A smooth potential P exists with grad P=W+rho e2; it is proper, and along a trajectory

    dP/dt=|W|^2+rho W2.

On a bounded backward trajectory the last term is integrable, since rho=O(e^t). The boundedness of P gives integrability of |W|^2 backward, and uniform continuity then gives W->0. Every backward limit point is an equilibrium and thus belongs to K={0}. This proves(a). Conversely(a) forbids any positive zero of w; positivity near zero then proves(b).

Condition(a) gives(c): every upper-half-plane trajectory enters the small source neighborhood backward, where rho/e_m>0, and transport preserves its sign.

To prove(c) implies(b), suppose w has a first positive zero x1. At Q=(x1,0), w'(x1)<=0 and the vertical eigenvalue of DW is lambda_v=2ell-w'(x1)>1. Reflection symmetry makes this eigenvector vertical. The positive-eigenvalue strong unstable manifold theorem supplies a nonstationary trajectory in the upper half-plane tending to Q backward with distance O(e^(lambda' t)), for some lambda'>1 as t->-infinity. Since rho(Q)=0 and rho is C1, rho on that trajectory is O(e^(lambda' t)). Exact transport also gives rho(Phi_t X)=e^t rho(X); multiplying by e^(-t) and taking t->-infinity forces rho(X)=0. This contradicts(c). This covers a degenerate first zero w'=0 as well as a saddle; no hyperbolicity of the other eigenvalue is assumed.

## 4. Far-field order and two-sided bound

The all-order exterior symbol argument in result32 applies without changing any step: its local evolution theorem does not use a center slope, its physical rescaling depends only on ell, and the prerequisite order-p value bound follows from the canonical inverse, exact exterior transport and the nonzero axis amplitude already supplied by result12. Thus rho and U have order-p symbol bounds and a smooth angular trace with Ck error O(r^(p-1)) for every k. This explicitly extends that regularity implication to the finite-order secondary branch; it does not transplant any primary center condition.

Under(b), equation(2) for j=m and the exterior bounds give

    g_m'/g_m=(p-m)/x+O(x^(p-2)).

The integrable error shows g_m(x)=G_m x^(p-m)(1+O(x^(p-1))), with G_m/(m! e_m)>0. Since all lower transverse jets vanish, differentiating the polar trace m times at theta=0 gives

    partial_theta^m[r^(-p)rho(r cos(theta),r sin(theta))]_(theta=0)
       =r^(m-p)g_m(r) -> Theta0^(m)(0)=G_m.

There are no lower-jet chain-rule terms: every term with fewer than m y derivatives differentiates an identically zero axis jet. The derivatives of Theta0 below m vanish. Reflection gives the corresponding endpoint at pi. Interior strict positivity of Theta0/e_m follows by exterior scattering along individual nonzero-density trajectories, not by taking a limit of positive functions. Therefore Theta0/(e_m sin^m(theta)) is positive and continuous on the closed upper semicircle.

The difference of the scaled density and Theta0 has zero derivatives of order below m at both endpoints, and its Cm norm is O(r^(p-1)). Taylor's integral remainder bounds its quotient by sin^m(theta) uniformly by the same error. This proves(1) outside a disk. Inside, smooth division, g_m sign and(c) give a positive minimum and a finite maximum, completing the proof.

## 5. An explicit restricted cubic-axis representation

For an independent m=3 search take L>0, 0<p<1, a=(1-p)/2 and

    w=(1+r^2/L^2)^(-a), sigma=r^2/(L^2+r^2), t=1-2w,
    rho=y w [y^2/(L^2+r^2)] sum_(k=0)^(M-1) sigma^k B_k(t)cos(2k theta).  (3)

This is smooth on the whole plane and has a global y^3 factor, not an x^2 factor. It is a restricted representation compatible with the dynamics subclass above, not an exhaustive parameterization of all secondary profiles. It has a0=0, e_3=B0(-1)/L^2 and K=L^(1-p) sum_k(-1)^k B_k(1). For a nondegenerate cubic-axis profile the scale L3=(K/e_3)^(1/(3-p)) is positive and transforms by L3->lambda L3. The slice K=e_3 fixes L3=1 without fixing ell or silently discarding the sign of e_3. The value e_3 is not a scaling invariant.

Let d_nk denote the sin(n theta) coefficient of sin^3(theta)cos(2k theta). Direct product-to-sum gives

    d_3k=(-1/4,3/8,-3/8,1/8,0,...),
    d_5k=(0,-1/8,3/8,-3/8,1/8,0,...).

With u=w and sigma=1-u^(1/a), the exact linear strain and quartic harmonic functionals are

    c=(1/(2a)) sum_k d_3k integral_0^1 sigma^k B_k(1-2u) du,
    H=e_3/8+(2/(a L^2)) sum_(k>=1) d_5k
                       integral_0^1 u^(1/a) sigma^(k-1) B_k(1-2u) du.   (4)

Here H=q1-q2 for psi=cxy+q1 x^3y+q2 xy^3+O(r^6). The first formula is the absolutely convergent sin3 density moment since a0=0. For the second, the local sin3 coefficient is -e_3/4, so its contribution -rho3_coefficient/2 equals e_3/8, while the remaining term is4 integral rho5 r^(-4)dr. These identities follow by radial substitution, without adding a harmonic field.

Finally let rho=e_3 y^3+f x^2y^3+g y^5+O(r^7). Exact Poisson gives q1+q2=0, and degree-five transport gives the necessary identities

    2 lambda_x f+(9/2)e_3 H=0,
    (2/3)g-(3/2)e_3 H=0.                               (5)

Indeed q1=H/2, U2 at degree3 equals (3H/2)x^2y-(H/2)y^3, and its product with3e_3 y^2 supplies these two nonlinear coefficients. A cubic-axis generator must use c=1/3-ell and(5), not the primary c=1-ell or its cubic identities. Formula(3) is only a finite smooth approximation; finite-angular nonexistence prevents interpreting any finite coefficient array as an exact solution.

Dependencies: results1,2,7,12,29,32 and the strong unstable manifold theorem in the explicit spectral-gap setting. All identities have been derived here before implementing the secondary experiment. Independent exact tests and a team model review are pending.
