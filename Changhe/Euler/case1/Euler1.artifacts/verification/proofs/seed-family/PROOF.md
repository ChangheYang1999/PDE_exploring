# Affine calibration and the localized potential seed

Status: proved informal identities for the specified family; the localized field is an initialization, not a solved profile. Dependencies: the product rule for curl, elementary matrix multiplication, and asymptotic expansion of (1+s)^p. Notation follows profile-identities/PROOF.md. All parameters and coordinates here are real, and c>0.

Let

    M=[[a,b,0],[b_2,-1-a,0],[0,0,1]],
    s=|y|^2, q=y.M y, chi=(1+s)^(-1/(2c)),
    A_0=-(y cross M y)/3,
    A=chi A_0,
    U=curl A,
    P=-(chi^2/2)y.(M+M^2)y.

## Exact affine calibration

The trace of M is zero. Its transverse block B has trace -1, so Cayley-Hamilton gives B^2+B=-det(B)I. The third diagonal entry of M+M^2 is 2. Consequently S=M+M^2 is symmetric, even when b differs from b_2.

The vector identity curl(F cross G)=F div G-G div F+(G.grad)F-(F.grad)G with F=y and G=M y gives curl(y cross M y)=-3M y: div G=tr M=0, div F=3, and the last two terms both equal M y and cancel. Hence curl A_0=M y.

For U_aff=M y and P_aff=-y.Sy/2, grad U_aff=M and grad P_aff=-S y. Substituting into stationary momentum gives

    (1-c)M y+cM y+M^2y-Sy=0.

Divergence vanishes. This holds for every c; therefore zero residual and nonzero n=2 content do not identify c or establish a valid decaying profile. A nonzero M produces an affine field that grows at infinity and is inadmissible for the target.

## Localized seed and its exact properties

Since grad chi=-chi y/[c(1+s)], the product rule and vector triple product give

    U=chi [(1-s/(3c(1+s)))M y+q y/(3c(1+s))].

This formula is a convenient independent forward evaluator. A and P are smooth at every finite point. Divergence of curl A is identically zero. M commutes with Q. Because Q is a proper rotation and chi is rotationally invariant, A(Qy)=Q A(y); the curl transformation proves U(Qy)=Q U(y). Pressure is Q-invariant as well.

Near zero, chi=1+O(s), the correction term is O(|y|^3), and U=M y+O(|y|^3). At infinity chi has degree -1/c; both leading velocity terms therefore have degree d=1-1/c, while pressure has degree 2-2/c=2d. The leading coefficient may vanish along individual directions. These are generic field powers, not directionwise positive lower bounds.

At z=0, the affine transverse strain includes a cylindrical n=2 term unless its symmetric trace-free part vanishes. That part vanishes only when a=-1/2 and b+b_2=0. The seed inherits this nonzero n=2 content near zero for generic parameters. It is non-affine after localization but retains extra inversion and z-parity properties from this particular construction; a final search must release them.

## A necessary warning about the seed's subleading tail

The localized seed has an expansion U=R^d A_0(n)+R^{d-2}A_2(n)+O(R^{d-4}). To avoid confusion, these A_k are angular velocity coefficients and are unrelated to the vector potential above. Put k=1/(3c), p=1/(2c), q_n=n.Mn. Expanding chi and 1/(1+R^2) yields

    A_0(n)=(1-k)M n+k q_n n,
    A_2(n)=[k-p(1-k)]M n-k(1+p)q_n n.

For the general nonzero M this A_2 is nonzero. The linear similarity operator annihilates R^d A_0 and maps the next term to -2c R^{d-2}A_2. In the target interval c<1/2, d<-1, so d-2 is greater than 2d-1. Thus the seed's linear correction decays more slowly than its convection and pressure gradient, whose scale is R^{2d-1}. Unless its angular coefficient vanishes specially, the seed cannot balance the stationary equation at that next order.

In particular, a residual normalized by the large linear terms can decay as R^{-2}, while the same residual normalized at the nonlinear scale grows as R^{-d-1}=R^{1/c-2}. This does not invalidate the seed as an initializer. It proves that a favorable linear-relative tail residual alone cannot certify it as a profile. The exponent collision at c=1/2 makes this particular comparison different, but does not make that localized seed an exact solution.
