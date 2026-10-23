# Localized pressure flux and the limits of characteristic geometry

Status: CONFIRMED by independent derivation and exact checks. Actual Opus5.5 review20 supplied a substantial but truncated audit; completed review21 confirmed the checked repairs, including the added multiplier parity restriction and the exceptional next flux term. Date: 2026-10-20.

## Hypotheses and statements

Let ell>1 and let a smooth exact primary profile satisfy the full equations and canonical law in PROMPT.md. Put d=ell-1, A=2ell-1, a=rho_y(0)!=0, W=ell X+U. Let P be any smooth pressure with grad P=-U-rho e2. On the origin basin B use the area preserving label diffeomorphism (xi,eta):B -> R^2 proved surjective in ../labels/PROOF.md, where rho=a eta and the label velocity is (A xi,eta). Define

    D_s={(x,y): |xi(x,y)|<s^A, |eta(x,y)|<s}, s>0,
    M(s)=integral_Ds y rho, E(s)=integral_Ds |U|^2,
    F(s)=integral_boundary_Ds P U.n.

Each D_s has compact closure in the basin, piecewise smooth boundary, and area 4s^(A+1). Then

    s M'(s)-(3ell+1)M(s)=-E(s)-F(s).             (1)

As s decreases to zero,

    M(s)=(4a/3)s^(A+3)+o(s^(A+3)),
    E(s)=(4d^2/3)s^(A+3)+o(s^(A+3)),
    F(s)=(4d(a-d)/3)s^(A+3)+o(s^(A+3)).         (2)

In particular the pressure flux cannot generally be omitted. Its displayed leading coefficient vanishes if a=d, so the phrase "same order" needs that exception. Bounds on P at infinity likewise do not prove a nonzero asymptotic pressure flux there.

For any smooth compactly supported real weight f, a weighted generalization is

    integral f|U|^2 = integral (P+y rho) U.grad f
       + integral [(3ell+1)f+ell X.grad f] y rho. (3)

These are identities, with no asserted sign for their right sides.

There are also smooth global fields satisfying the symmetries, source geometry, density transport, and sublinear density growth, with nonzero a of either sign and no other equilibrium, which fail the curl coupling. Thus those kinematic facts alone cannot give a NO theorem. A construction and its precise failure are given below.

## Pressure and moving-domain proof

The vector -U-rho e2 has zero curl because curl U=-rho_x. On the simply connected plane it is a gradient. Since div U=0, the divergence theorem gives, on every bounded piecewise smooth D,

    integral_D rho U2=-integral_D |U|^2-integral_boundary_D P U.n. (4)

Adding a constant to P changes no flux, since integral_boundary_D U.n=0.

The label diffeomorphism maps D_s to an ordinary rectangle, hence its closure is compact inside the basin. The flow of W sends D_s to D_(s exp(t)). Reynolds' formula, div W=2ell, and

    W.grad(y rho)=(ell+1)y rho+rho U2

give sM'=(3ell+1)M+integral_Ds rho U2. Equation (4) proves (1). Corners do not affect the boundary or volume identity; it also follows by smooth approximation to the label rectangle.

Parity and D(xi,eta)(0)=I give for the inverse chart

    x=xi[1+O(xi^2+eta^2)], y=eta[1+O(xi^2+eta^2)].

The volume element is exactly dxi deta. Since rho=a eta and

    U=(d x,-d y)+O(r^3),

integration gives the first line of (2). The y^2 term in the energy has integral (4/3)s^(A+3); the x^2 term has integral (4/3)s^(3A+1)=o(s^(A+3)) because A>1. The cubic remainders have higher powers. Also

    integral_Ds rho U2=-(4ad/3)s^(A+3)+o(s^(A+3)).

Using (4) proves the last line of (2), without differentiating an unspecified little-o remainder. Factored parities give U1=d*xi+O(|xi|(xi^2+eta^2)), U2=-d*eta+O(|eta|(xi^2+eta^2)) in these coordinates. Keeping the linear x-energy term therefore gives

    F(s)=(4d(a-d)/3)s^(A+3)-(4d^2/3)s^(3A+1)
                         +O(s^(A+5))+O(s^(3A+3)).

The omitted xi^4 term has exponent 5A+1>3A+3. When a=d and 1<A<2 the second term is the negative leading flux; for A>=2 cubic data can enter at the same or earlier order. This refinement is obtained directly from parity bounds, not from differentiation of remainders. The coefficients satisfy (1), since A+3-(3ell+1)=1-ell=-d. For a<0 the localized integral of rho U2 is positive to leading order and F is sufficiently negative to preserve (4); this is not a contradiction.

For (3), integrate the transport identity against f. It gives

    integral f rho U2=-integral y rho W.grad f-(3ell+1)integral f y rho.

The pressure identity gives integral f|U|^2=integral P U.grad f-integral f rho U2. Substitute W=ell X+U to obtain (3). All integrations have compact support.

## A smooth global kinematic example

Fix a smooth radial cutoff chi with 0<=chi<=1, chi=1 for r<=1, and chi=0 for r>=2. Set

    psi_k=-d*x*y*chi(r), U_k=(-partial_y psi_k,partial_x psi_k), W_k=ell X+U_k.

These fields are smooth, have the required component parities and div W_k=2ell, and U_k is compactly supported. Direct polar differentiation yields

    W_k.e_r=r[ell+d chi(r) cos(2theta)] >= r.     (5)

The derivative of the cutoff contributes only to the angular component in (5). Hence zero is the unique equilibrium. Every nonzero trajectory reaches infinity forwards and zero backwards; the growth is at most linear, so the flow is complete. Inside r<=1 it is exactly (A x,y).

Define eta_k(X)=exp(t)*y(flow_(-t)(X)) once the backward trajectory has entered r<1. The definition is independent of any further increase in t. For every compact set K, (5) gives |flow_(-t)(X)|<=exp(-t)|X|, uniformly on K. Choose T so the image of K lies inside the unit ball. Then eta_k=exp(T)*y composed with flow_(-T) on K, proving smoothness by smooth flow dependence. In the inner ball eta_k=y. Flow equivariance gives eta_k even in x and odd in y. The invariant axis y=0 and uniqueness of trajectories show that eta_k has the sign of y. Put rho_k=a eta_k for any a!=0. Then W_k.grad rho_k=rho_k and rho_k,y(0)=a.

Outside r>=2, W_k=ell X. Thus rho_k=r^p Theta(theta), p=1/ell, with a smooth angular function Theta determined on r=2. It is nonzero on each open half plane and has the required parities. Every derivative there has the corresponding homogeneous bound. The fields satisfy the prompt's density growth condition with gamma=p, and U_k=o(r).

They do not solve IPM. If curl U_k=-rho_k,x held on the whole plane, then rho_k,x=0 outside r=2. On the region x>2, independence of x gives rho_k=g(y). There the homogeneous transport equation gives ell*y*g'(y)=g(y), hence g(y)=C*y^p for y>0, with C nonzero by strict sign. At the fixed x=3 this fails to be C1 at y=0 because 0<p<1. Contradiction. Thus no velocity satisfying the curl coupling equals U_k. In particular the canonical velocity, whose existence follows from ../inverse/PROOF.md for this smooth density with growth exponent p, differs from U_k. The example establishes only the insufficiency of the listed kinematic conditions, not existence in a weaker coupled class.

## The limited variational obstruction in label coordinates

The curl equation for labels is

    E(xi,eta)=eta Delta xi-A xi Delta eta-(A-1)grad xi.grad eta+a eta_x=0,
    det D(xi,eta)=1.                           (6)

At identity labels take an infinitesimal area preserving variation xi=x+epsilon h_y, eta=y-epsilon h_x, with smooth compactly supported h odd in both coordinates. The determinant is 1+O(epsilon^2), and the derivative of E is

    Lh=(A x partial_x+y partial_y)Delta h
          +(A-1-a)h_xx-(A-1)h_yy.             (7)

This follows by direct differentiation of (6). Its nonzero third-order real principal part is skew under formal adjunction. Thus L is not formally self-adjoint on any nonempty open set. The defect can be detected within odd-odd functions: take two test functions supported inside a quadrant and extend by the required reflections. L preserves this parity.

For a precise variational conclusion, let Phi(h) be the time-one map of the compactly supported Hamiltonian field (h_y,-h_x), viewed as a label map. Then det D Phi(h)=1, Phi(0)=identity and D Phi(0)h=(h_y,-h_x). Let m be a smooth real scalar multiplier even in both coordinates; it may depend smoothly on the labels as well. Its value m0 at identity labels is required to be nonzero on some open set. There is no C2 scalar functional S, on a neighborhood of zero in the odd-odd test functions, whose usual L2 gradient is m E(Phi(h)) there. Indeed E(identity)=0, so its derivative is m0 L, whose real third-order principal symbol is skew and nonzero on that set. A Hessian in this pairing must be symmetric, a contradiction. Locality of S is not required for this necessary condition. Evenness of m ensures it preserves the parity space: for an arbitrary non-even multiplier the parity-projected operator could cancel, so that wider assertion is not made.

This excludes only the specified gradient in this pairing. Actions with additional fields, alternative constraints or differential preconditioning, and other metrics are not excluded. The fixed-eta weighted divergence equation alone is not the coupled variational problem.

## Verification and scope

The label construction is independently proved in ../labels/PROOF.md. The pressure law and canonical gauge are in ../darcy_energy/PROOF.md and ../inverse/PROOF.md. Exact symbolic coefficient, adjoint and compact polynomial checks are in verification/. The kinematic construction uses only standard smooth flow existence and elementary radial differentiation; no numerical trajectory fit enters its proof. None of these results settles the primary or secondary existence question.
