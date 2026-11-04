# Equivariant densities, angular multipliers and exterior Bernoulli signs

## Setting

Use B=cy-omega Jy+U, X=cy+U, Omega=curl U, a=1-2c and the exact residual
R=(1-c)U+(B.grad)U+omega JU+grad P. Unless an identity specifies otherwise,
U is C^2, P is C^1, div U=0. The equation makes P C^2. All compactly supported
weights below are C^1 and axisymmetric. There are no boundary terms at infinity.

## Equivariant-density lemma (C04)

Let Q(U)(y)=q(y,U,DU,...,D^k U), with q C^1, U C^{k+1}. Assume precisely

    Q(R_alpha U(R_-alpha .))(y)=Q(U)(R_-alpha y).

Let L U=(Jy.grad)U-JU and DQ(U)[V] denote differentiation of Q with respect to
its field argument. Differentiation in alpha at zero gives

    DQ(U)[LU]=(Jy.grad)Q(U).

For a solution E0(U,P)=omega LU, where E0 is the nonrotating residual, it follows
that DQ(U)[E0]=div(omega Q Jy). Integration with an axisymmetric compact weight
phi gives zero: div Jy=0 and Jy.grad phi=0. This proves the exact submitted
lemma. A general pressure-dependent functional is not Q(U) as defined here;
its transformation and linearization must be checked separately. Nor does
absence of an explicit omega in a budget make its unknown solutions independent
of omega.

## Angular multiplier and mode identity (C05)

Since U.LU=(Jy.grad)(|U|^2/2), its phi-weighted integral vanishes. Pairing
E0=omega LU with phi LU therefore proves

    omega int phi|LU|^2 = int phi LU.[c(y.grad)U+(U.grad)U+grad P].

For a fixed cylindrical Fourier mode u_m=(a_m,b_m,w_m), D=r d_r+z d_z,
N_m the exact mode of (U.grad)U, and dmu=r dr dz, take the imaginary part of
the mode equation paired with phi conjugate(u_m). The pressure term is

    int phi conjugate(u_m).grad_m p_m dmu
       =-int p_m conjugate(u_m).(d_r phi,0,d_z phi) dmu,

by the mode divergence constraint. There is no axis contribution: smooth
Cartesian U,P imply bounded cylindrical coefficients and the boundary term
has the factor r. Thus

    m omega int phi |u_m|^2 dmu
      = c Im int phi conjugate(u_m).D u_m dmu
        - Im int p_m conjugate(u_m).grad_rz phi dmu
        + Im int phi conjugate(u_m).N_m dmu.

This uses the actual infinite mode system from in the team records. It
neither truncates the nonlinearity nor asserts a sign for its imaginary part.
The real part similarly gives the submitted mode energy identity, since
int phi Df dmu=-int(3phi+Dphi)f dmu. The coefficient of a tail weight R^-s
vanishes at s=5-2/c. No infinite integral is taken without convergence.

## Absolute-vorticity form (C06)

Assume c>0 and set kappa=a omega/c,

    H'=H-a omega^2 r^2/(2c).

Starting with R=aX+Omega x B+grad H, use X=B+omega Jy and
JB=cJy+omega y_h+JU. Direct rearrangement yields

    R=aB+(Omega+kappa e_3) x B+grad H'-kappa JU.

Dotting with B, and observing B.JU=-c Gamma-omega y_h.U, gives

    B.grad H'=-a|B|^2-kappa(c Gamma+omega y_h.U)+B.R,
    Gamma=Jy.U.

For a solution with 0<c<1/2,

    B.grad H' <= -a|B|(|B|-|omega||U|/c).

If U tends to zero, the closed exceptional set
{|B|<=|omega||U|/c} is compact because |B|>=c|y|-|U|.
The original H strictly decreases where X.B>0; its exceptional set is

    |X-(omega/2)Jy| <= |omega|r/2.

Its compactness follows without an unproved sign estimate. Put w=omega Jy and
use the distance from cy to the closed ball centered at w/2 of radius |w|/2:

    |U| >= sqrt(c^2|y|^2+omega^2 r^2/4)-|omega|r/2
         = c^2|y|^2 /
           (sqrt(c^2|y|^2+omega^2r^2/4)+|omega|r/2)
         >= c^2|y|/(c+|omega|).

Both exceptional sets contain all B-zeros. The conclusion is exterior
monotonicity only. Every backward limit set can lie inside the exceptional
region, so no global Lyapunov argument follows.

## Scope

C04, C05 and C06, precisely as stated above, are confirmed. Claims that all
possible weighted or quadratic identities fall into these forms are not
included. Pressure torque may persist pointwise even when its particular
axisymmetric integral vanishes. The result is uniform in finite omega, with
no uniform bound asserted for the sizes of the exceptional compact sets.

Audit recorded: 2026-11-02T18:42:51Z
