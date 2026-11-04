# Escaping sheet estimates and compatible finite jets

Status: A777-A779 CONFIRMED at their stated conditional and finite-jet scopes; the unsupported source extension remains OPEN in A780. Independent reconstruction of the remaining coordinator Note52 claims. The sharper escape estimate retains its supplied vorticity asymptotic. The finite-jet calculation below is not an exact profile.

## 1. Setting and distinction between assumptions

Let 0<c<1/2, omega be any finite real number, a=1-2c, kappa=1+c, A=cI-omega J, J(x1,x2,x3)=(-x2,x1,0). Let U in C2(R3;R3), P in C1(R3) solve the full divergence-free rotating Euler profile equation, with U.curl U=0 and uniform U(y)->0. Write B=Ay+U,W=curl U,H=P+|U|^2/2+(Ay).U. Let p be a vortical carrier equilibrium of covector rate rho<=-2a, and mu=-a-rho>0. The global surface theorem A770 gives M=W^u(p), with a globally defined scalar k satisfying

    B cross W=ak grad H, U=(k-1/a)grad H,
    k(Phi_t x)=exp(mu t)k(x),
    Phi_t^*dH=exp(rho t)dH, det DPhi_t=exp(3ct).

Its zero fiber L is the vortex line through p. A771 already supplies its connected fibers. Fix an escaping forward orbit starting at x in M outside L. The additional hypothesis for the sharp estimates is

    |W(Phi_t x)| |Phi_t x|^(1/c) -> ell in (0,infinity).   (1)

This is explicitly a supplied premise here. The cited predecessor hf_vortical_eq proves it only on escaping branches of L, where B=kappa sW and s(Phi_t x)=exp(kappa t)s(x). The successor question silently extends it to M outside L. That extension is not justified by the predecessor. It is not derived from velocity decay in this proof. The velocity scattering below uses only decay. Properness in Section3 does not use(1). The finite jets in Section5 require none of the global hypotheses.

## 2. Scattering and the conditional sharp area estimate

Bounded U and c>0 imply d|y|/dt>=c|y|/2 outside a large ball. Hence a forward-unbounded orbit eventually leaves every compact set. Variation of constants gives a finite vector v and

    y(t)-exp(At)v=-integral_t^infinity exp(A(t-s))U(y(s))ds.

The norm of this integral is at most c^(-1)sup_(s>=t)|U(y(s))|, hence tends to zero. If v=0, the orbit would tend to zero, a contradiction. Therefore |y(t)|exp(-ct)->|v|>0.

Under(1), |W(y(t))|exp(t)->ell|v|^(-1/c)>0. Since k(x)!=0 and mu>0,

    aU=(1-1/(ak)) B cross W

gives |U(y(t))|=O(exp(-(1-c)t)), using |B|=O(exp(ct)). Dividing U=(k-1/a)grad H then gives |grad H|=O(exp((rho-c)t)). A second substitution in the variation-of-constants integral sharpens its remainder to O(exp(-(1-c)t)). All constants here may depend on the chosen orbit.

For the ordinary surface area Jacobian, the cofactor formula and the ambient covector identity give exactly

    J_M(t,x)=exp((3c-rho)t)|grad H(Phi_t x)|/|grad H(x)|.

Thus J_M=O(exp(2ct)) on this orbit. The weighted area form nu=dA/|grad H| still expands by exp((3c-rho)t). These statements are compatible: the weight itself grows. No uniform bound over a noncompact surface patch has been proved. Replacing(1) by an unexplained consequence of bare velocity decay would strengthen this conditional statement without proof.

## 3. Properness if every noncentral orbit escapes

Assume every carrier orbit of M except p escapes forward; equivalently assume escape on M outside L and on both halves of L. Choose a small closed source disk D about p with B strictly outward along its boundary. A positive quadratic Lyapunov form for the restricted linear source, with its nonlinear error absorbed by shrinking D, supplies it. Every orbit in M except p crosses its boundary once: backward convergence supplies existence, and strict outward crossing prevents reentry.

Thus M outside the disk is parametrized by Phi_t x with x in its compact boundary and t>=0. For every sufficiently large outward-invariant ball, each boundary orbit eventually crosses it strictly. Continuous dependence provides the same strict crossing on a neighborhood of that boundary point. A finite cover provides one common crossing time, after which outward invariance and the radial inequality give uniform exponential escape. The inverse image in M of a compact ambient ball lies in D together with the image of a bounded time interval times the boundary. That is compact, and the inverse image is closed in it. Hence the inclusion M into R3 is proper.

Escape merely on M outside L gives uniform escape only on compact portions of the source boundary avoiding its two L intersections. No properness is inferred at those exceptional points. Properness itself supplies neither a lower bound for |grad H| nor a contradiction with the area law.

## 4. What the circulation calculation actually gives

U is normal to M, so any curve in M has zero velocity line integral. A small oriented disk transverse to a nonzero W has nonzero vorticity flux, hence a boundary C of nonzero circulation. The exact Kelvin identity is

    exp(-at)|integral_C U.dy|
      <=length(Phi_t C) sup_(Phi_t C)|U|.

The right side tending to zero is compatible with its left side tending to zero. A contradiction follows if one additionally proves both length(Phi_t C)=O(exp(ct)) and sup_(Phi_t C)|U|=o(exp(-(1-c)t)). Bare velocity decay supplies neither that rate nor the length bound. This is an exact limitation of the displayed inequality; no impossibility theorem for all circulation arguments is claimed.

## 5. Exact finite-jet statement

Now let 2/5<c<1/2 and omega be arbitrary. Set rho=-2a, mu=a, p=-(c,omega,0)/(c^2+omega^2), x=y-p, u0=e1, w0=e2. Define

    b=(8c^2-13c-4)/(4c+1),
    zeta=(48c^3-64c^2+27c-4)/a, alpha=-b-zeta,
    f=(b-20c^2+18c-4-zeta-4omega^2)/(2a),
    h=omega(2b+7c^2+15c+2)/(7c-2),
    D=[[3c-2,-omega,0],[-omega,1,0],[-1,0,1-3c]],
    Q1=[[alpha,(c+3)omega,-c],[(c+3)omega,2c-4,0],[-c,0,-4a(1-3c)]],
    Q2=[[h,b,0],[b,-(c+3)omega,c],[0,c,0]],
    Q3=[[f,omega,zeta],[omega,c-1,0],[zeta,0,0]].

All denominators are nonzero in the stated range. Define the polynomial U_i=delta_i1+(Dx)_i+x^T Qi x/2. It is exactly divergence-free, and at p one has B=0,U=e1,W=e2. Its carrier derivative is

    M=A+D=[[-2a,0,0],[-2omega,kappa,0],[-1,0,a]],

so its spectrum is {rho,kappa,mu}, M w0=kappa w0 and M^T u0=rho u0.

Let T=DW(p), with entries

    T=[[omega,-1,0],[-c-f,-omega,-4a(1-3c)-zeta],
       [h-(c+3)omega,b-2c+4,0]].

The identities D^T w0+T^T u0=0 and TM-MT+kappa T-R=0, where R_ij=(Qi)_(j2), express respectively the first helicity jet and the first vorticity-transport jet. Their possibly nonzero residuals reduce to the defining scalar equations

    alpha+b+zeta=0,
    (4c+1)b=8c^2-13c-4,
    (2c-1)zeta=-48c^3+64c^2-27c+4,
    2af=b-20c^2+18c-4-zeta-4omega^2,
    (7c-2)h=omega(2b+7c^2+15c+2).

In particular u0.Tw0=-1=-|w0|^2 is the forced curvature identity. These equations concern finite jets, not vorticity transport at neighboring points.

## 6. Pressure jet and rank jet

For this polynomial velocity let F=((1-c)I+omega J)U+DU(Ay+U), and let F_[<=2] be its polynomial terms of degree at most two in x. The exact divergence-free vector identity is curl F=[B,W]+kappa W. The previous zero constant and linear curl terms imply curl F_[<=2]=0. Consequently the explicit cubic polynomial

    P(x)=-integral_0^1 F_[<=2](t x).x dt

has grad P=-F_[<=2], and the full momentum residual has order O(|x|^3), meaning that precisely degrees zero through two vanish. This is not vanishing through degree three.

The associated H=P+|U|^2/2+(Ay).U has grad H(p)=-a e1 and Hess H(p)=E=-aD-[w0]_cross M. The matrix E is symmetric. For g=U.B,

    grad g(p)=rho e1, Hess g(p)=Q1+D^T M+M^T D,
    Hess g+(rho/a)E=lambda e1 e1^T,
    lambda=alpha+2a(2-3c)+4omega^2.

The last matrix equation says exactly that the constant and linear terms of dH wedge dg vanish. Thus the residual orders are

    div U=0,
    U.W=O(|x|^2), [B,W]+kappa W=O(|x|^2),
    F+grad P=O(|x|^3), dH wedge dg=O(|x|^2).

The actual quadratic coefficient of x2^2 in U.W is -omega(c+3)/2. In particular the displayed velocity is not an exact helicity-free germ for any nonzero omega. This does not obstruct a different higher-order completion, whose cubic velocity terms can change that helicity coefficient. This supplies consistent second-order velocity and cubic pressure jets for every stated c and omega. It gives no higher-order compatibility, formal series convergence, exact local Euler solution or global decaying profile.

## 7. Verification question and pass criterion

The theoretical question for the independent exact computation is whether direct differentiation of these full polynomial fields and the radial pressure construction gives precisely the asserted residual orders, without relying on separately assigned H or W jets. The pass criterion is that every rational coefficient below the stated degree vanishes identically in c and omega, and the displayed eigenvalue, covector and curvature identities hold. A nonzero higher coefficient is allowed and documents the distinction from an exact profile. No numerical sampling, optimization, formal build or external computation is used.
