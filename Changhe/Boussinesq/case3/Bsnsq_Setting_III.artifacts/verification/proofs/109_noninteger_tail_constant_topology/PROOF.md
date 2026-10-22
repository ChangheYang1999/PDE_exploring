# The inverse constant is not controlled by weak tail convergence for noninteger beta

Written 2026-10-21T02:23:59.031584+00:00. Standalone informal proof, with explicit scope. The timestamps of file creation and verification are registered in the evidence manifest. This is a source-topology result, not a B2 solution or nonexistence theorem.

## Statement and definitions

Fix a noninteger beta>2, s=1/beta, N=floor(beta), and m=1-2s. Let a smooth x-odd vorticity Omega have smooth homogeneous tails omega_k of degrees -ks, 1<=k<=N, and a remainder eta=Omega-sum omega_k with eta=O(r^{-(N+1)s}) at infinity. Homogeneous terms are defined on the punctured plane, without a cutoff. Near zero eta=O(r^{-Ns}). Since Ns<1<(N+1)s, the ordinary kernel integral

    U_eta(X)=int K(X-Y)eta(Y)dY,
    K(Z)=(Z2,-Z1)/(2pi|Z|²)

is absolutely convergent at X=0 and locally elsewhere, and continuous at0. Set C=-U_eta(0)=(0,C2). The canonical relative velocity is V(X)=int[K(X-Y)-K(-Y)]Omega(Y)dY. It equals the sum of homogeneous tail velocities, U_eta and C, by linearity of the convergent differences. This C is the constant in the noninteger tail decomposition. Inversion and its sublinear uniqueness use packet99, and the convergence assertions are also checked directly below.

For any fixed real D and any sufficiently large R, there is a smooth annular perturbation deltaOmega_R with its canonical relative velocity deltaV_R such that:

1. deltaOmega_R=deltaV_R=0 on |X|<=R. All center data and equations on that disk are unchanged. Every homogeneous tail coefficient is unchanged, and C2 changes by exactly D.
2. For every finite j, using ||f||_(a,j)=max_{|k|<=j}sup_X(1+|X|)^{a+|k|}|partial^k f|,

       ||deltaOmega_R||_(s,j)+||deltaV_R||_(s-1,j)
                    <=M_j |D| R^{s-1}->0.

3. If the background has finite symbol bounds for Omega,V,Theta of degrees -s,1-s,m, then the weighted absolute residual changes obey

       ||delta R_Theta||_(-m,j)<=M|D|/R,
       ||delta R_Omega||_(s,j)
          <=M[|D|R^{s-1}+|D|/R+D²R^{s-2}].

4. Under the additional positive exterior envelopes for F=Theta/x² and G=Omega/x,

       F>=b r^{m-2}, G>=a r^{-1-s},
       |F|+r|gradF|<=M r^{m-2},
       |G|+r|gradG|<=M r^{-1-s},
       |V1/x|<=M r^{-s}, |V2|<=M r^{1-s},

   the prompt's normalized residual functions change uniformly by the same rates as in item3. The positive source envelope is retained with a/2 for large R. Exact axis ratios are interpreted separately from their divided limits.

Thus C2 is discontinuous even in the weighted-field topology augmented by uniform convergence of normalized residual functions. These are changes of residuals about a background, not claims that residuals tend to zero. If a true profile with these hypotheses existed, the construction would give approximate fields with a shifted C; the argument does not assume or establish its existence. The perturbations need not belong to a finite spline space or satisfy the full PDE.

## Exact annular construction and full-plane inverse

Choose a nonzero nonnegative C-infinity function chi supported in [1,2], flat at both endpoints, and write I0=int_1^2 chi(t)dt>0, I2=int_1^2 t²chi(t)dt. In polar coordinates with x=r cos(theta), set

    q_R(r)=-2D chi(r/R)/(R I0),
    deltaOmega_R=q_R(r)cos(theta),
    p_R(r)=1/2[r^-1 int_0^r rho²q_R(rho)drho
                          -r int_0^r q_R(rho)drho],
    deltaPsi_R=p_R(r)cos(theta),
    deltaV_R=(-partial_y deltaPsi_R,partial_x deltaPsi_R).

Differentiating the displayed integrals gives -(p_R''+p_R'/r-p_R/r²)=q_R. The fields vanish for r<=R and are smooth everywhere. For r>=2R,

    p_R(r)=D r-D R²I2/(I0 r).

The velocity is bounded and centered. The relative kernel has the same divergence0 and curl -deltaOmega_R and is sublinear; the difference is an entire harmonic vector field of sublinear growth, hence constant by the derivative estimate on large balls. Centering sets it to0. This identifies the full-plane inverse, without an arbitrary harmonic addition. Directly,

    U_deltaOmega(0)=(0,1/2 int_0^infinity q_R(r)dr)=(0,-D).

All omega_k are unchanged, so delta eta=deltaOmega_R and deltaC=(0,D). Absolute convergence at0 follows from integrating |eta|dr: near0 the bound is r^{-Ns} with Ns<1, and at infinity it is r^{-(N+1)s} with (N+1)s>1. The kernel singularity at X!=0 is locally integrable because eta is locally bounded there. The usual near/far split gives continuity at0, with small-ball contribution O(epsilon^{1-Ns}).

## Weighted convergence and residual estimates

Under X=RZ, deltaOmega_R=(D/R)f(Z) for a fixed smooth compactly supported f, while deltaV_R=Dg(Z), with g=0 for |Z|<=1 and g=e2 plus a degree -2 field for |Z|>=2. The compact source derivative scales are |D|R^{-1-|k|}. The velocity derivatives are bounded by M|D|r^{-|k|} for r>=R; positive derivatives decay still faster outside2R. Multiplying by the stated weights proves item2 because s<1.

Keep Theta unchanged. The exact differences of the physical residuals are

    delta R_Theta=deltaV.gradTheta,
    delta R_Omega=(beta X+V).grad deltaOmega+deltaOmega
                  +deltaV.gradOmega+deltaV.grad deltaOmega.

All terms vanish belowR. The first has weighted size M|D|/R. For the second line, beta X.grad deltaOmega+deltaOmega has weighted size M|D|R^{s-1}; V.grad deltaOmega and deltaV.gradOmega give M|D|/R; the quadratic term gives MD²R^{s-2}. Leibniz's rule proves these estimates for every fixed derivative order. No estimate here uses beta<3.

For normalized ratios put A=beta+V1/x, B=beta y+V2. The divided residuals and grouped physical normalizers are

    R_F=A(2F+xF_x)+B F_y-(beta-2)F,
    N_F=|A(2F+xF_x)|+|B F_y|+(beta-2)|F|,
    R_G=A(G+xG_x)+B G_y+G-2F-xF_x,
    N_G=|A(G+xG_x)|+|B G_y|+|G|+|2F+xF_x|.

The lower bounds N_F>=(beta-2)b r^{m-2} and N_G>=a r^{-1-s} are genuine, with a/2 after perturbation, and no floor. The explicit dipole inverse gives deltaA=O(|D|/r), deltaB=O(|D|) on r>=R, and h=deltaG=q_R/r satisfies |h|+r|gradh|<=M|D|R^-2 on the annulus. In particular G+h retains the claimed lower bound once R^{1-s} is sufficiently large.

Subtraction gives deltaR_F=deltaA(2F+xF_x)+deltaB F_y, of size O(|D|r^{m-3}). For G, changes of the signed terms and of the sum of their absolute values are bounded by

    |(A+1)h|+|xA h_x|+|B h_y|
    +|deltaA G|+|x deltaA G_x|+|deltaB G_y|
    +|deltaA h|+|x deltaA h_x|+|deltaB h_y|.

Dividing by the perturbed lower normalizer gives the item3 rates. The same bound controls signed or absolute ratios, since for |R|<=N and N,N'>0,

    |R'/N'-R/N|<=(|R'-R|+|N'-N|)/N'.

Expanding grouped terms into individual absolute terms only increases the available lower bound; the same termwise argument works. Fields and derivatives agree belowR, so denominator zeros there cause no difference. At x=0 the physical ratios have0/0 and are defined as0 for both fields. Their divided expressions have the nonzero exterior bounds above. This proves item4.

## Scope for beta near3 and a sufficient stronger topology

The construction works for every fixed noninteger beta>2, including3<beta<4. It preserves all N prescribed tail coefficients. Consequently it directly prevents deducing C_n->0 merely from weak weighted-field or normalized-residual convergence to a hypothetical C=0 profile. It does not assert that the particular numerical homotopy exhibits these perturbations or fails to converge.

For a sufficient stronger condition, with beta and the homogeneous tails fixed, convergence int|eta_n(Y)-eta(Y)|/|Y|dY->0 implies C_n->C, since |K(-Y)|=1/(2pi|Y|). A uniform bound on a stronger exterior remainder and appropriate convergence on compact sets can supply dominated convergence. Such a condition must be established, not inferred from sampled small residuals. The annular source has weighted remainder size ||deltaOmega_R||_((N+1)s,0) proportional to |D|R^{(N+1)s-1}, which grows, so it violates that stronger uniform control.

At beta=3 the third stream exponent resonates with the first angular harmonic, and a logarithmic term replaces its homogeneous inverse. A decomposition into a homogeneous term and a constant is not uniform through that resonance without further estimates. This observation is not needed for the fixed-beta counterexample and no beta-dependent limiting theorem is asserted here.

## Dependencies and evidence

The source formulas and normalized estimates are rederived here; packets94 and96 contain earlier versions restricted to2<beta<3. The interpretation of C after N tails is packet99. No proof assistant source is claimed. Independent finite checks and actual model review are recorded under verification and do not replace the argument.
