# Reconstructing a common potential from an exterior density and stream

Status: PROVED. The theory part independently reviewed and adopted this proof; the final transcription was checked in V207 and V208. This result constructs a potential for an already given exterior pair. It does not establish convergence of a potential series or bounds on its growth.

## Statement and notation

Let R>0, let s>=2 be an integer, and write Omega_R={x^2+y^2>R^2}. Suppose rho is C^(s-1) and psi is C^s on Omega_R, with

    rho(-x,y)=rho(x,y),       rho(x,-y)=-rho(x,y),
    psi(-x,y)=-psi(x,y),      psi(x,-y)=-psi(x,y),
    -Delta psi=partial_x rho.

For every R2>R there is a C^(s+1) function chi on the whole plane, even separately in x and y, such that on Omega_R2

    chi_xy=psi,
    -partial_y Delta chi=rho,
    (-chi_xyy,chi_xxy)=(-psi_y,psi_x).

The extension of chi inside Omega_R2's complement is only a construction device; the equations are asserted on Omega_R2. In particular, if the given pair solves the stationary IPM transport equation, then it also solves the original potential formulation on Omega_R2. For s>=3 the potential is at least C4, sufficient for the pointwise differentiated density equation.

On a fixed exterior domain, the difference between any two C3 potentials with these properties and these symmetries is exactly

    A(x)+b y^2,

where A is an even C3 function and b is a real constant. The constant term can be included in A. This describes the gauge freedom without imposing growth restrictions.

## Construction of the mixed primitive

Choose R1 with R<R1<R2. Let zeta be a smooth radial function that vanishes on r<=R1 and equals1 on r>=R2. Define psi_tilde=zeta psi on r>R and zero on r<=R1. Because the cutoff vanishes on a neighborhood of the interface, psi_tilde is a C^s function on the entire plane. It is odd separately in x and y and agrees with psi on Omega_R2.

Set

    chi_0(x,y)=integral_0^x integral_0^y psi_tilde(a,b) db da.

Then chi_0 is even separately in x and y, and (chi_0)_xy=psi_tilde. Moreover chi_0 is C^(s+1). A pure derivative of positive order m<=s+1 leaves one integral and differentiates psi_tilde at most m-1<=s times. A mixed derivative of total order m with both coordinate orders positive differentiates psi_tilde m-2<=s-1 times. These formulas also show continuity of all stated derivatives.

Define on Omega_R2

    F=-partial_y Delta chi_0-rho.

This is C^(s-2), is even in x and odd in y, and has a classical x derivative despite the lower overall regularity bound. Indeed the mixed-primitive formulas give

    partial_x F=-Delta psi_tilde-partial_x rho=0

on Omega_R2. Thus F is constant on each connected component of the horizontal section of Omega_R2 at a fixed y.

For |y|>R2 the section is connected. For |y|<=R2 there are two components, and x reflection carries one into the other. Since F is even in x, their constants are equal. Choose a fixed x_*>R2 and define A_0(y)=F(x_*,y). It follows that

    F(x,y)=A_0(y) on Omega_R2.

The function A_0 is C^(s-2) on the full real line and odd. This is the step where reflection symmetry removes the possible mismatch between the two horizontal components around the hole.

## Removing the density discrepancy

Define

    B(y)=(1/2) integral_0^y (y-b)^2 A_0(b) db.

Then B'''=A_0, B is C^(s+1), and B is even because A_0 is odd. Put chi=chi_0+B(y). Since B has no x dependence,

    chi_xy=psi_tilde,
    -partial_y Delta chi
       =-partial_y Delta chi_0-B'''
       =rho+A_0-A_0=rho

on Omega_R2. Differentiating chi_xy=psi gives the asserted velocity. This proves existence, regularity and symmetry.

The construction does not select the homogeneous radial powers of the formal series. It can add gauge terms with unrelated growth, so no quantitative potential asymptotics should be inferred from this existence statement alone.

## Gauge classification

Let h be the difference of two such C3 even potentials on a fixed Omega_R2. Then h_xy=0 and partial_y Delta h=0. At fixed x, h_x is constant on every connected component of the vertical section. Its evenness in y identifies the two constants whenever the section has two components. Consequently h_x=a(x) for a globally defined C2 function a. Since h is even in x, a is odd. Similarly h_y=b_0(y) for a globally defined odd C2 function b_0.

Choose even primitives A'(x)=a(x) and B_0'(y)=b_0(y). The gradient of h-A-B_0 vanishes on the connected exterior, so the difference is constant; absorb it in A. The density condition now gives B_0'''=0. Its evenness implies B_0(y)=b y^2+d, and d can again be absorbed in A. Conversely every A(x)+b y^2 with A even has zero mixed derivative and zero partial_y Delta, so it leaves both fields unchanged.

## Application and scope

The confirmed finite-truncation Theorem S gives rho in C^(k-2) and psi in C^(k-1), with k>=4. Taking s=k-1 in this proposition gives a C^k common potential on any slightly smaller exterior, by V204. This removes the potential-reconstruction gap from the physical-space conclusion. It does not give a convergent canonical series, a C-infinity solution on one fixed exterior, a common solution for every truncation, or a whole-plane stationary extension.

The proof uses only the Poisson compatibility, coordinate symmetries, a smooth radial cutoff, ordinary integration and connectedness of horizontal and vertical sections. No numerical computation or external theorem is required.
