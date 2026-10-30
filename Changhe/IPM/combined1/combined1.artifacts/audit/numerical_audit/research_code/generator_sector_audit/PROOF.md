# Exact origin and residual-sector audit from scaled generators

## Statement, hypotheses and notation

Fix a rational c>1, gamma=1/c and delta=1-gamma. Let J be a nonnegative integer and p_j=(3+gamma-j delta)/2. For finitely many tuples (j,m,w,n,Q,R) with 0<=j<=J, nonnegative integers m,w,n,Q and positive rational R, take rational coefficients a. Set s=x^2+y^2, H_m=Re(x+iy)^(2m) and

    chi=sum a H_m (1+s)^(p_j-m)
            [s/(R^2+s)]^w [R^2/(R^2+s)]^Q
            P_n((s-R^2)/(s+R^2)).                                    (1)

Here P_n is the ordinary Legendre polynomial, P_n(1)=1. Define

    rho=-partial_y Delta chi,
    U1=-chi_xyy, U2=chi_xxy,
    F=(c x+U1)rho_x+(c y+U2)rho_y-rho.

These functions are smooth on the real plane and have the required parity: chi is even in each coordinate, rho even in x and odd in y, U1 odd in x and even in y, and U2 even in x and odd in y.

The algorithm below computes the exact rational density slope a0=rho_y(0), strain=partial_y U2(0), and every residual far-field coefficient with exponent at least -2. It also computes any larger finite rectangular table of formal sectors. No conversion to a basis with the sole denominator 1+s is required. The finite table alone establishes no whole-plane norm or residual smallness.

## Exact origin coefficients

Define the polynomial

    A_n(v)=(1+v)^n P_n((1-v)/(1+v)).

It is a polynomial of degree at most n by expansion of P_n. Parity P_n(-t)=(-1)^n P_n(t) gives the following exact radial factor at the origin:

    (-1)^n R^(-2w) s^w (1+s)^(p_j-m)
           A_n(s/R^2)(1+s/R^2)^(-w-Q-n).                            (2)

This is analytic for |s|<min(1,R^2). Its coefficient of s^l is rational and follows from two binomial series and the finite A_n. Only l<=2-m is needed for fourth Cartesian derivatives. In particular generators with m+w>2 do not contribute to the strain or a0.

Write b22=[x^2 y^2]chi and b04=[y^4]chi. Since differentiation at zero selects precisely the fourth-degree homogeneous terms,

    strain=4 b22,   a0=-4 b22-24 b04.                              (3)

To obtain each b, multiply the needed coefficient in (2) by

    H_m=sum_(k=0)^m (-1)^k binom(2m,2k) x^(2m-2k)y^(2k),
    s^l=sum_(t=0)^l binom(l,t)x^(2l-2t)y^(2t).

All sums are finite rational arithmetic. Formula (3) has no polar singularity or numerical limiting operation.

## Potential moments and differentiated homogeneous terms

For z=r^-2, each summand in (1) is a r^(2p_j) cos(2m theta) times

    R^(2Q) z^Q (1+z)^(p_j-m)
       A_n(R^2 z)(1+R^2 z)^(-w-Q-n).                              (4)

This identity and its rational Taylor coefficients M_q are proved independently in ../multiscale_generators/PROOF.md. Summing a M_q within each (j,m) gives cosine polynomials C_(j,q), with

    chi=sum_(j,q>=0) r^(alpha_(j,q)+3) C_(j,q)(theta),
    alpha_(j,q)=gamma-j delta-2q.                                (5)

The series and all fixed finite Cartesian derivatives converge on every closed exterior r>=r0>max(1,R_i), by analytic power-series convergence away from the polar origin. Hence differentiation and the finite products below are valid there.

For a homogeneous angular term r^s cos(n theta), its x derivative has cosine coefficients (s+n)/2 at n-1 and (s-n)/2 at n+1. Its y derivative has sine coefficients -(s+n)/2 at n-1 and (s-n)/2 at n+1. For r^s sin(n theta), the x formula has the same coefficients and sine parity; the y derivative has cosine coefficients (s+n)/2 at n-1 and -(s-n)/2 at n+1. Negative frequencies are reduced by cosine-even and sine-odd parity; sin(0 theta) is zero. Finally,

    Delta[r^s C(theta)]=r^(s-2) sum_n (s^2-n^2) C_n cos(n theta).

These identities follow by partial_x=cos(theta)partial_r-sin(theta)partial_theta/r and partial_y=sin(theta)partial_r+cos(theta)partial_theta/r. Three applications therefore compute exact angular polynomials G_(j,q), V1_(j,q), V2_(j,q) of rho,U1,U2, all with radial exponent alpha_(j,q). One more derivative computes X_(j,q),Y_(j,q) of rho_x,rho_y, with exponent alpha_(j,q)-1.

## Residual sectors and completeness of the forbidden table

The linear residual at (h,q) is (c alpha_(h,q)-1)G_(h,q), with G zero if h>J. Products satisfy

    alpha_(i,u)+alpha_(j,v)-1=alpha_(i+j+1,u+v).

Consequently the complete residual sector is

    E_(h,q)=(c alpha_(h,q)-1)G_(h,q)
      +sum_(i+j+1=h, u+v=q)
         [V1_(i,u) X_(j,v)+V2_(i,u) Y_(j,v)].                    (6)

Products of angular polynomials use the exact sine-cosine product identity. No background mode may be omitted merely because the output frequency is small. There are no branches with h>2J+1. Since 0<gamma<1, every q>=2 has alpha_(h,q)<=gamma-4<-3, so q=0,1 and h=0,...,2J+1 contain every exponent at least -2.

If two pairs (h,q) yield the same exponent, their angular polynomials must be added before deciding whether that exponent vanishes. The implementation does so. All computed exponents and the threshold -2 are rational, without floating comparisons. A rectangular prefix h<=hmax, q<=qmax omits only terms with exponent at most

    max(gamma-(hmax+1)delta, gamma-2(qmax+1)),

where the first entry is discarded if hmax>=2J+1. This follows from delta>0 and nonnegative indices. The prefix contains every forbidden exponent when this upper bound is strictly below -2. A first surviving term can be called the leading residual term only when its exponent strictly exceeds this omitted upper bound. Otherwise the implementation explicitly leaves that conclusion open. These strict inequalities also ensure that an omitted formal sector cannot cancel a retained forbidden or leading coefficient through an exponent coincidence.

Thus exact vanishing of all aggregated E with exponent >=-2 establishes the required far-field exclusions for the finite smooth family. Membership in a particular forcing space additionally uses that space's decay and derivative requirements. No interval containing zero is treated as an exact cancellation.

## Verification, dependencies and scope

The implementation compares the direct moments and origin coefficients against independently converted canonical sources for existing single-scale snapshots. It compares every potential, density and residual coefficient in a specified finite table with the previous canonical sector algorithm. The direct moment formula has separate finite-grid and analytic audits in the preceding topic. Mixed-scale synthetic data are also checked against direct Cartesian origin jets and an independent expansion of the radial scalar expression.

The angular differentiation implementation is reused from the established sector audit; this is a new independent route for generator reduction and origin data, not a wholly independent differential algebra. Each output records hashes of the exact input, code and dependencies. Future scaled candidates require their own exact manifest and coefficient checks. This proof neither certifies their full-plane norms nor extends the existing beta-integral method to a second denominator.
