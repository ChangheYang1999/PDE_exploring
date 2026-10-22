# Annular perturbations and the prompt's normalized residuals

Written 2026-10-21T00:39:44.867414+00:00. Complete informal argument before numerical checks. This strengthens packet94 under explicit positive far-field envelopes. It is a continuity statement for residual functions on an inverse-source class, not existence, nonexistence, or a residual lower-bound theorem for B2.

## 1. Hypotheses and exact claim

Fix2<beta<3, s=1/beta, m=1-2s. Let smooth fields Theta=x²F, Omega=xG have the prompt x-reflection parity and a canonical centered full-plane velocity V=(-Psi_y,Psi_x), -DeltaPsi=Omega. Suppose their first two homogeneous vorticity tails and inverse constant C=(0,C2) satisfy packet94's hypotheses. The quotients F,G and V1/x extend smoothly over x=0. Assume that for some r0>=1 and positive a,b,M, at every point with r>=r0,

    G>=a r^(-1-s),       F>=b r^(m-2),
    |F|+r|gradF|<=M r^(m-2),
    |G|+r|gradG|<=M r^(-1-s),
    |V1/x|<=M r^-s,      |V2|<=M r^(1-s).              (1)

The quotient bound on the axis is interpreted by continuity. These uniform positive envelopes are additional hypotheses, not consequences asserted for all profiles. No PDE is assumed.

Let chi be smooth on R, nonnegative and nonzero, supported in[1,2], and I0=integral chi>0. For fixed real D and R>=r0, add the packet94 source and its canonical relative inverse:

    deltaOmega=q_R(r)cos(theta),
    q_R=-2D/(R I0)chi(r/R),
    Omega_R=Omega+deltaOmega, V_R=V+deltaV, Theta_R=Theta. (2)

All fields agree on r<=R, both leading tails agree, and C2_R=C2+D. For R sufficiently large, G_R>=a r^(-1-s)/2 for r>=r0. The perturbation is zero belowR; the bound at r0<=r<R is unchanged.

Define the actual Cartesian residuals and normalizers from the prompt, using W=beta X+V:

    R_Theta=W1 Theta_x+W2 Theta_y-(beta-2)Theta,
    N_Theta=|W1 Theta_x|+|W2 Theta_y|+(beta-2)|Theta|,
    R_Omega=W1 Omega_x+W2 Omega_y+Omega-Theta_x,
    N_Omega=|W1 Omega_x|+|W2 Omega_y|+|Omega|+|Theta_x|.

Write rho_Theta=|R_Theta|/N_Theta and rho_Omega=|R_Omega|/N_Omega, with0 when both numerator and denominator vanish. Then there is M1 independent ofR,D such that, for all sufficiently largeR (depending onD),

    sup_X |rho_Theta,R-rho_Theta|<=M1 |D|/R,
    sup_X |rho_Omega,R-rho_Omega|
      <=M1[|D|R^(s-1)+|D|/R+D²R^(s-2)].               (3)

The same bounds hold for their desingularized ratios, including the exact axis limits, with either normalizers inherited from the original Cartesian terms or the fully expanded termwise normalizers defined in section2. No denominator floor is used. The signed residual ratios also obey these difference estimates.

Consequently the constant C2 is still discontinuous if the weighted field norms of94 are supplemented by uniform convergence of these pointwise normalized residual functions. This is a statement about changes of residual functions, not about their values tending to zero. Only if an exact background profile satisfying(1) existed would it yield nearby fields with arbitrarily small normalized residuals and a changed constant. No such background profile is constructed here.

## 2. Desingularization and a ratio inequality

Write

    A=beta+V1/x, B=beta y+V2, W=(xA,B).

In Cartesian variables F(x,y),G(x,y), rather than the variable x², the divided equations are exactly

    R_F=2AF+xA F_x+B F_y-(beta-2)F,
    R_G=AG+xA G_x+B G_y+G-2F-xF_x,                    (4)
    R_Theta=x²R_F, R_Omega=xR_G.

Dividing the original normalizers by x² or |x| gives, off the axis,

    N_F=|A(2F+xF_x)|+|B F_y|+(beta-2)|F|,
    N_G=|A(G+xG_x)|+|B G_y|+|G|+|2F+xF_x|.             (5)

Every expression on the right extends to x=0. Alternatively expand the first grouped term in each normalizer, and expand |2F+xF_x| into |2F|+|xF_x|. Denote those fully expanded sums by N_F^e,N_G^e. Both pairs bound the respective residual absolute values, and by(1)

    N_F,N_F^e >= (beta-2)b r^(m-2),
    N_G,N_G^e >= a r^(-1-s),                          (6)

with a/2 for the perturbed G. Thus all divided ratios have genuine, nonzero lower denominators on the exterior, even on the axis.

For any two residual/normalizer pairs with N,N'>0 and |R|<=N,

    |R'/N'-R/N| <= (|R'-R|+|N'-N|)/N'.                (7)

The same bound holds with absolute residual numerators. It follows by adding and subtracting R/N', then using |R|/N<=1; taking absolute values of the numerators can only reduce the numerator difference. A sum of absolute terms changes by at most the sum of the absolute changes of its signed terms. We will apply this termwise, so cancellations in a grouped normalizer create no hidden assumption.

## 3. Perturbation bounds and the proof of(3)

Let h=deltaG=q_R/r, a1=deltaA=deltaV1/x and b1=deltaB=deltaV2. Explicitly, writing deltaPsi=P_R(r)cos(theta), packet94 gives

    P_R(r)=(1/2)[r^-1 integral_0^r rho²q_R(rho)drho
                       -r integral_0^r q_R(rho)drho].

Both integrals run from0 to r. This is the centered inverse. Formula(7) of94 gives its velocity, and smooth parity or its explicit first-mode angular expression gives

    |a1|<=M2|D|/r, |b1|<=M2|D|       for r>=R,
    |h|+r|grad h|<=M2|D|/R²           for R<=r<=2R.    (8)

The three functions vanish on r<=R; h vanishes also on r>=2R. All estimates remain valid on x=0 by the smooth quotient extension. For instance deltaV1 is proportional to cos(theta)sin(theta), so dividing by x=r cos(theta) introduces exactly one power r^-1 and no angular singularity. Flatness of chi guarantees smoothness across both annular boundaries.

The positivity assertion follows from |h|<=M2|D|/R² and G>=a(2R)^(-1-s) on the annulus. It suffices to choose R^(1-s)>=2^(2+s)M2|D|/a. Outside the annulus G is unchanged. Fix such anR.

For temperature, subtraction in(4) gives

    deltaR_F=2a1F+x a1F_x+b1F_y.

The sum of the absolute changes of the normalizer terms is bounded by the sum of the same three magnitudes, whether the first term is grouped or expanded. By(1),(8), each is bounded by M3|D|r^(m-3). Dividing by the lower bound for N_F,R in(6) and using r>=R proves the first estimate of(3).

For vorticity, direct subtraction gives

    deltaR_G=(A+1)h+xA h_x+B h_y
              +a1G+x a1G_x+b1G_y
              +a1h+x a1h_x+b1h_y.                   (9)

The changes of all grouped or expanded normalizer terms are bounded by the sum of the absolute values of these products (with A and1 separated if necessary). On the annulus, |A|<=beta+M r^-s and |B|<=beta r+M r^(1-s). The linear terms involvingh therefore have size at most

    M4|D|[R^-2+R^(-2-s)].

The terms involving a1G,b1gradG are at most M4|D|r^(-2-s), throughout r>=R. The quadratic terms are supported on the annulus and bounded by M4D²R^-3. Divide by N_G,R>=a r^(-1-s)/2. On the annulus r andR are comparable, and outside it the only remaining change is O(|D|/r). This proves the second estimate of(3), using(7). The same reasoning works for signed ratios.

On r<R every field and derivative is exactly unchanged, so the ratio difference is zero regardless of any zeros of its denominator. On x=0 the original Cartesian ratios have0/0, declared0 for both fields. Off-axis bounds remain uniform up to the axis, and the desingularized ratios obey the continuous exterior estimates just proved. This handles exact axis values and their nontrivial limits separately and proves the global claim.

## 4. A nonempty test class with the exact center relations

The hypotheses can be met with all B2 center relations, without satisfying the global PDE. Let

    p=(1-s)/2, c=1+beta/2, a_c=p-1/(2beta),
    Theta=x²(1+r²)^(-1/2-s),
    Psi=-x[(1+r²)^p-1]+kappa(r)[cxy+a_c x r²],           (10)

where kappa is smooth radial, equals1 for r<=1 and0 for r>=2. Define Omega=-DeltaPsi and V=(-Psi_y,Psi_x). These are globally smooth and have the required parity. At0,

    Theta=x²+O(r^4),
    Psi=cxy-(1/(2beta))x r²+O(r^5),
    Omega=(4/beta)x+O(r^3), V(0)=0, Psi_xy(0)=c.

Thus a0=1, b0=4/beta and the required strain relation hold. The compact stream corrections are generated by their own compactly supported vorticity; they are not an added global harmonic strain. Their centered, bounded velocity is the canonical inverse by distributional div-curl uniqueness and sublinear growth.

For r>=2, the source and velocity equal the uncorrected first mode. Explicitly

    Omega=4p x(1+r²)^(p-2)[2+(p+1)r²],
    F=(1+r²)^(-1/2-s),
    V1=2p xy(1+r²)^(p-1),
    V2=1-(1+r²)^p-2p x²(1+r²)^(p-1).

These formulas give all positive envelope and derivative bounds in(1), with r0=2. The source has a nonzero degree -s leading tail and zero degree -2s second tail. The stream at infinity is -x r^(1-s)+x+O(r^-s), with differentiated remainder O(r^(-1-s)), so the inverse constant is C2=1. These fields need not solve the transport equations, and no such assertion is made. Applying(2) makes C2=1+D, with the exact center relations and core retained and all differences in(3) tending to zero. This is the promised explicit counterexample to continuity of C in the augmented topology. It does not turn the background's nonzero residual into zero.

## 5. Dependencies and verification scope

The source shift, full-plane inverse and weighted field convergence are the proved packet94 results. Sections2-3 supply the additional axis-safe normalized estimates, and section4 verifies that the hypotheses with correct center jets are nonempty. No positivity inside the fixed core is required, since the perturbations vanish there. Numerical checks supplement this proof and will be saved under verification after completion. No formal proof, interval certificate or full endpoint is claimed.
