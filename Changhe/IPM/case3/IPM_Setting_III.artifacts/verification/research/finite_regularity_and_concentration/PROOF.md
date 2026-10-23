# Finite regularity, local homogeneous modes, and concentration limits

Date: 2026-10-20. Status: independent audit of the lead's weak1 proof. Status CONFIRMED for the conditional statements proved here. The independent algebra checks passed at2026-10-20T16:25:11Z; the endpoint-series, compactness and matching arguments were reread and audited at 2026-10-20T16:27:51.432373+00:00. Every existence statement in Sections 3-4 concerns the frozen linear local equation, not the nonlinear full-plane profile equation.

## 1. Classes, inverse, and first-order identities

Fix ell>1, A=2ell-1, B=A-1 and p=1/ell. Densities are even in x and odd in y. For 0<alpha<1 let P_(1,alpha) be the exact profile class with rho in C1,alpha_loc on the plane, a=rho_y(0)!=0, and

    |rho|+(1+r)|grad rho| <= C(1+r)^gamma, 0<gamma<1.

Let P_Lip^circ(K) instead require rho in W1,infty_loc on the plane and C1,alpha_loc off zero, the same growth bound almost everywhere, exact transport distributionally on the plane, and a nonzero axis tail K. No derivative at zero is required in this latter class. Neither class is the smooth primary class.

For both classes the canonical inverse is

    U=-rho e2/2+PV_disk integral K(X-Y)rho(Y)dY,
    K(z)=(-z1 z2/pi,(z1^2-z2^2)/(2pi))/|z|^4.             (1)

The disk at infinity is centered at zero. At the query subtract rho(X) on a small query-centered disk; Lipschitz regularity makes the resulting integral absolutely convergent. In the far exterior subtract K(-Y), whose integral against the centrally odd density vanishes on every centered annulus. The tail is bounded by C|X| integral_R^infty s^(gamma-2)ds. Splitting at distances comparable to |X| gives U=O((1+r)^gamma). Div U=0 and curl U=-rho_x hold distributionally from the kernel multipliers.

A compactly supported Lipschitz density gives a velocity modulus C h(1+|log h|): compare the query-centered subtracted integrals, splitting displacements at h and at one. Separated input has bounded derivatives. A compact C^alpha density instead gives the modulus C h^alpha by a kernel-difference estimate on the region larger than h. Localize and commute derivatives to obtain U in C1,alpha_loc when rho has that regularity, and an odd-odd stream psi in C2,alpha_loc. No Linfty singular-integral estimate is used.

Any two sublinear velocities with these div-curl equations differ by an entire harmonic vector field. The interior gradient estimate on disks of radius R and o(R) growth forces that difference to be constant; parity removes the constant. Thus (1) has the prescribed gauge at these regularities too.

For rho in P_(1,alpha), write rho=ay+O(r^(1+alpha)) and let rho_j=(1/pi) integral rho(r,theta)sin(j theta)dtheta. Then rho_3=O(r^(1+alpha)) at zero. The exact strain identity and transport give

    c=psi_xy(0)=-a/4+integral_0^infty rho_3(r)r^(-2)dr,
    ell+c=1,  DW(0)=diag(A,1).                            (2)

The integral is absolutely convergent. For completeness, the sin2theta coefficient f of rho_x is

    f=(rho_1'-rho_1/r+rho_3'+3rho_3/r)/2.

The canonical radial Poisson solution implies c=(1/2) integral f/r. Integration by parts uses rho_1/r -> a at zero and ->0 at infinity, and rho_3/r ->0 at both endpoints, giving (2). Expansion of W.grad rho-rho to order r gives a(ell+c-1)y+o(r); division by nonzero a proves the center relation without a second derivative of rho.

The earlier radial-scattering proofs need only C1 control on compact annuli, the sublinear gradient bound, and these equations. They therefore give a continuous nonzero leading tail, all C^beta angular bounds for beta<1, and canonical U=O(r^p) for P_(1,alpha). The primary axis proof gives K!=0. In P_Lip^circ(K) the prescribed nonzero K supplies nontriviality; the far-field argument remains an annular argument. The genuine scaling sends K to lambda^(1-p)K and a cubic coefficient b, if it exists, to lambda^(-2)b. Thus b |K|^(2/(1-p)) is invariant. A cubic coefficient is not part of either finite-regularity definition.

## 2. A local homogeneous inverse of degree between one and two

Let H be homogeneous of degree d with 1<d<2, even in x and odd in y, and C1,alpha on compact annuli. Define

    V[H](X)=-H(X)e2/2
       +PV integral [K(X-Y)-K(-Y)-DK(-Y)X]H(Y)dY.         (3)

The subtractions here are over the whole plane. At Y=0 their worst term has radial majorant s^(d-2)ds and is integrable because d>1. At infinity the bracket is O_X(|Y|^-4), with radial majorant s^(d-3)ds and d<2. At Y=X use the local Holder subtraction for K(X-Y)H(Y). Consequently (3) is well defined. A change of variables proves homogeneity of degree d. It solves div V=0, curl V=-H_x; the removed terms are a value and a linear Taylor term in X and do not change the local div-curl equations, as is also seen by applying the same Taylor subtraction to finite-domain canonical fields before taking limits.

For clarity, the linear subtraction has the div-curl compatibility of the original kernel at X=0. It is not an arbitrary linear velocity. Any two degree-d homogeneous div-curl inverses regular at zero differ by an entire harmonic vector. Growth O(r^d), d<2, makes the difference a polynomial of degree at most one, and homogeneity with noninteger d eliminates it. The corresponding odd-odd stream has degree d+1 and is unique.

This is a renormalized local inverse of a superlinear homogeneous field. It is not the full-plane sublinear velocity law applied to a degree-d candidate. Confusing these domains would invalidate the indicial argument.

Suppose an actual P_(1,alpha) profile has a leading expansion, in C1 on compact annuli,

    t^(-d)[rho(tZ)-a t Z2] -> H(Z),                        (4)

with uniform local remainder bounds O(r^d), O(r^(d-1)). Subtract the linear Taylor part of its velocity. Scaling the kernel as in (3) gives the limit V[H]. To justify the nonlocal limit, first restrict rescaled Y to a fixed bounded region; (4) gives convergence there. The outer local region is dominated by the Taylor-subtracted bound O(|Y|^(d-4)), and the fixed physical exterior has a velocity Taylor remainder O(t^2), which becomes o(t^d). Let the intermediate rescaled radius tend to infinity after the first limit. Thus the leading equation is

    (Ax partial_x+y partial_y-1)H+a V[H]_2=0.             (5)

The assumption (4) is additional. A function can be C1,alpha and fail C2 without having a nonzero homogeneous leading term. For example, with alpha<s<1, a smooth cutoff times y r^s/log(e/r) has this behavior. No indicial classification can be applied to every such failure of C2 without proving an expansion.

## 3. A sufficient interval of genuine finite-regularity linear modes

Fix 0<alpha<1, q0=1+alpha, and suppose

    a>A q0-1.

The interval

    I=(q0,min(2,a+1-B q0))                               (6)

is nonempty. For every d in I for which

    kappa_x=(A d-1)/B, kappa_y=(a-d+1)/B                 (7)

are nonintegers, there is a nonzero real homogeneous pair

    H=r^d Theta(theta), chi=r^(d+1)Phi(theta)

solving (5) and -Delta chi=H_x, with H in C1,alpha_loc and chi in C2,alpha_loc on the entire plane, and the required parity. At most finitely many degrees in I are excluded by the noninteger conditions. This is a sufficient interval, not a sharp classification for every regularity or every exceptional exponent.

Here is a direct construction. On 0<theta<pi/2 put c=cos theta, s=sin theta, and q=A c^2+s^2. The equations are

    (d q-1)Theta-B s c Theta'
                    +a[(d+1)c Phi-s Phi']=0,
    Phi''=s Theta'-d c Theta-(d+1)^2 Phi.                 (8)

They form a real analytic first-order system for Y=(Theta,Phi,Phi') of dimension three on the open quadrant.

At theta=t=0, the system is tY'=(R_x+analytic terms vanishing at zero)Y, with

    R_x = [[kappa_x, a(d+1)/B, 0],
           [0,       0,       0],
           [0,       0,       0]].                       (9)

At theta=pi/2-t use Y=(Theta,Phi,Phi_t). Its residue is

    R_y = [[-(d-1)/B, 0, -a/B],
           [0,        0,  0],
           [(d-1)/B,  0,  a/B]].                         (10)

Each residue is diagonalizable with eigenvalues 0,0,kappa and kappa>q0. The latter inequalities follow from d>q0, kappa_x-d=(d-1)/B>0, and the upper bound in (6).

We spell out the local existence fact needed here. For a system tY'=(R0+sum_(j>=1) R_j t^j)Y with the displayed eigenvalues and positive noninteger kappa, each vector in ker R0 gives an analytic solution with coefficients determined by

    (jI-R0)Y_j=sum_(l=1)^j R_l Y_(j-l), j>=1.

The matrices are invertible. A kappa-eigenvector likewise gives a solution t^kappa times an analytic series, replacing j by j+kappa in the recurrence. The inverses have norm at most C/j for all sufficiently large j. Since analytic coefficients satisfy ||R_j||<=C M^j, a geometric majorant bounds the solution coefficients: choose a larger base L so that sum ||R_j||L^(-j) is small enough; the finitely many small denominators are absorbed into the initial majorant. Thus both series converge. This proves the required three independent local solutions without merely counting formal exponents.

At the x-axis, imposing analytic oddness of Theta and Phi leaves exactly the one-dimensional analytic initial data Y0=(0,0,z0). Reflection invariance and uniqueness of its analytic series give the stated parity. The fractional solution has Theta~t^kappa_x, Phi'=O(t^(kappa_x+1)), Phi=O(t^(kappa_x+2)); the last two orders also follow directly from the second equation in (8). Its odd reflection gives H in C1,alpha and chi in C2,alpha because kappa_x>q0. These two solutions span a two-dimensional admissible data space at any interior angle.

At the y-axis, analytic evenness of Theta and oddness of Phi impose Phi(0)=0 and

    (d-1)Theta(0)+a Phi_t(0)=0.

This leaves one analytic parameter. Reflection invariance gives the parity of its analytic solution. A kappa_y-eigenvector of (10) is (1,0,-1); hence the fractional solution has Theta~t^kappa_y, Phi_t~-t^kappa_y and Phi~ -t^(kappa_y+1)/(kappa_y+1). Evenly reflecting Theta and oddly reflecting Phi gives the same required regularity. This supplies a second two-dimensional admissible data space.

Transport each space to one interior angle by the nonsingular first-order fundamental matrix. Two two-dimensional real subspaces of a three-dimensional space intersect in dimension at least one. Choose a nonzero intersection vector. It gives a solution satisfying both endpoint conditions and the required axis regularity. Reflection extends it to the plane minus zero. The regularities C1,alpha and C2,alpha ensure the two equations extend distributionally across the axes with no delta terms. Homogeneity and d>1+alpha give the same regularity at zero: on comparable-radius pairs use the annular Holder bound multiplied by r^(d-1-alpha); on noncomparable pairs use the homogeneous derivative bound. Set the value and first derivative of H, and derivatives through order two of chi, to zero at zero.

If H were zero, (5) would force chi_x=0 since a>0. Oddness in x would then force chi=0, contradicting the nonzero intersection vector. Finally uniqueness of the homogeneous inverse in Section 2 identifies its velocity with (3). This completes the construction.

The dimension argument is applied after constructing compatible endpoint spaces for the actual coupled system. It does not assign a dimension to a nonlinear full-plane solution set. Smooth angular modes obey the separate lattice theorem already proved in ../indicial_fourier/PROOF.md. Finite-regularity angular modes constructed here need not be smooth across the axes.

## 4. Superpositions and the limitation of a single indicial ansatz

On a subinterval where the two endpoint data spaces have constant intersection dimension and kappa_x,kappa_y avoid integers, their bases and the matching matrix depend smoothly on d. A fixed nonzero minor and elementary linear elimination give a smooth nonzero choice (Theta_d,Phi_d), after shrinking the subinterval. Strict margins d>1+alpha and kappa_x,kappa_y>1+alpha keep degree derivatives, which insert logarithms, in C1,alpha and C2,alpha respectively.

For a compact interval [d0,d1] in such a subinterval and smooth b, linearity therefore gives a further exact frozen solution

    H(r,theta)=integral_(d0)^(d1) b(d)r^d Theta_d(theta)dd.

If b(d0)Theta_(d0) is nonzero, integration by parts in d, or the elementary Laplace endpoint estimate with s=-log r, gives

    H(r,theta)=r^d0 [b(d0)Theta_(d0)(theta)/|log r|
                               +O(|log r|^(-2))]

in the relevant angular norm as r tends to zero. Thus even the frozen linear equation has non-pure-power leading behaviors. Distinct degrees in (1,2) are linearly independent modulo C2 germs, since a nonzero smallest degree cannot be C2 and the parity class has no nonzero homogeneous quadratic Taylor term. None of this constructs a nonlinear profile or proves a Fredholm property in an unspecified space.

## 5. A conditional concentrated-forcing compactness theorem

Suppose epsilon_j decreases to zero and smooth canonical forced pairs at a fixed ell satisfy

    W_j.grad rho_j-rho_j
         =mu_j y(1+r^2/epsilon_j^2)^(-2),
    a_j=rho_(j),y(0) bounded,
    Delta_j=ell+c_j-1 ->0,
    mu_j=a_j Delta_j.                                    (11)

Assume common value and gradient growth bounds with one exponent gamma<1, and common C1,alpha bounds on every compact set separated from zero. Assume also one common nonzero axis tail K_j=K. These are uniform compactness hypotheses, not conclusions of a finite scan or of small residuals.

There is a subsequence with rho_j converging locally uniformly on the whole plane, in C1,beta on compact punctured sets for every beta<alpha, and weak-star in W1,infty on compact sets. The limit belongs to P_Lip^circ(K), with the punctured exponent beta. In particular it is a nontrivial exact weak profile, but its derivative at zero and membership in P_(1,alpha) are not established.

Proof: common local Lipschitz bounds and compactness give the asserted density subsequence, with one diagonal extraction. The canonical velocities converge locally uniformly as well: on small query disks use the common Lipschitz estimate, on the remainder of a bounded region use uniform density convergence, and in the exterior use the uniform tail estimate in (1). Local C1,beta convergence off zero follows by localizing the density and using the same Holder kernel bound after differentiation; separated contributions have convergent derivatives.

The source in (11) has sup norm at most C|mu_j|epsilon_j and gradient at most C|mu_j|. Since mu_j->0, it vanishes. The conservative equation is

    div(rho_j W_j)=(2ell+1)rho_j+source_j.

Uniform convergence of its local products passes it distributionally to the limit. The div-curl equations pass by canonicity. There is no residual point source at zero. Alternatively the small-circle transport flux tends to zero, since rho=O(r) and W is locally bounded.

It remains to retain K, which local convergence by itself would not do. On the positive y-axis choose one large R so that

    v_j(y)=ell y+U_(j),2(0,y)>=ell y/2, y>=R

for all j, using the common sublinear velocity bound. Put

    H_j(y)=integral_R^y [1/v_j(s)-p/s]ds.

The integrand is O(s^(gamma-2)) uniformly. It follows that H_j(infinity) converges to the analogous H(infinity), and its tail beyond a large radius is uniformly small. The exact axis integrating-factor formula is

    K=exp(H_j(infinity)) [R^(-p)rho_j(0,R)
      +mu_j integral_R^infinity s^(1-p)exp(-H_j(s))
                    (1+s^2/epsilon_j^2)^(-2)/v_j(s) ds]. (12)

The integral is O(epsilon_j^4 R^(-p-3)). Passing to the limit in (12) gives K=exp(H(infinity))R^(-p)rho(0,R). The limit solves the unforced axis equation, so this is its nonzero axis tail. This proves nontriviality and the stated class.

## 6. A possible defect of the center strain moment

Continue with (11), take a subsequence a_j->a_*, and assume additionally that the limiting density is C1,eta at zero for some eta>0, with slope a and canonical strain c. For fixed delta>0, convergence away from zero and the common tail bound give

    lim_j integral_delta^infinity rho_(j),3(r)r^(-2)dr
             =integral_delta^infinity rho_3(r)r^(-2)dr.

Using (2) for every j, c_j->1-ell=-D, and then (2) for the limit gives the exact iterated defect

    lim_(delta->0) lim_j integral_0^delta rho_(j),3(r)r^(-2)dr
         =-D-c+(a_*-a)/4.                                (13)

If the limiting slope is nonzero, exact first-order transport forces c=-D and (13) reduces to (a_*-a)/4. If a=0, that division is unavailable and the first expression must be retained.

Uniform Lipschitz and punctured smooth convergence do not force a_*=a. An explicit nonprofile countertest is

    h_epsilon(X)=epsilon da [z2+(3z1^2 z2-z2^3)/2]
                               exp(-|z|^2), z=X/epsilon.

It has slope da, canonical strain zero, uniform Lipschitz norm, and converges to zero in every Ck norm away from zero and uniformly on the plane. Its x^2 y coefficient is da/(2epsilon^2). The strain follows either from (2) or direct angular integration: the sin3theta moment cancels -da/4 exactly. This countertest does not solve (11); it identifies why a separate PDE regularity argument is needed. Common C1,eta bounds at zero, or a common Dini modulus of the gradients, would make the small-radius integrals uniformly small and remove this defect.

## 7. Conditional inner matching and a measurable invariant

Let 0<s<1, C!=0, and suppose a smooth forced sequence has the stronger inner expansions, with errors tending to zero in C3 for density and C4 for stream on compact inner sets,

    rho_epsilon(epsilon Z)=a epsilon Z2+C epsilon^(1+s)F(Z)
                                                +o(epsilon^(1+s)),
    psi_epsilon(epsilon Z)=c epsilon^2 Z1Z2+C epsilon^(2+s)G(Z)
                                                +o(epsilon^(2+s)),
    c=1-ell, a!=0.                                      (14)

Put a_F=F_y(0), c_F=G_xy(0), b_F=[x^2y]F, H_F=[x^3y]G-[xy^3]G. Then

    a_epsilon=a+C epsilon^s a_F+o(epsilon^s),
    Delta_epsilon=C epsilon^s c_F+o(epsilon^s),
    mu_epsilon=a C epsilon^s c_F+o(epsilon^s),
    b_epsilon=C epsilon^(s-2)b_F+o(epsilon^(s-2)),
    H_epsilon=C epsilon^(s-2)H_F+o(epsilon^(s-2)).         (15)

Substitution into the exact equations shows

    (Ax partial_x+y partial_y-1)F+a G_x
                   =a c_F Z2/(1+|Z|^2)^2,
    -Delta G=F_x.                                       (16)

The leading cubic identity is

    (a-4A)b_F=3a H_F+4a c_F.                             (17)

It follows either by expanding (16) through degree three or by dividing the exact forced identity by C epsilon^(s-2). If b_F c_F!=0, then

    epsilon^2 b_epsilon/Delta_epsilon -> b_F/c_F.         (18)

These are implications of the uniform derivative expansions (14). The expansions, their matching to an outer finite-regularity profile, and nonvanishing of b_F,c_F have not been proved for the computed branch. Logarithms, cancellation of a leading coefficient, and multiple inner scales can change the diagnostic. Large finite jets alone are not proof of a limiting exponent or absence of a smooth limit.

## 8. Scope of the verification

This audit confirms the local finite-regularity inverse, first-order identities, the sufficient noninteger mode interval, and the conditional concentration and matching implications after independent reconstruction. It does not establish the full sharpness or necessity claims of a general indicial regularity threshold, a nonlinear finite-regularity family, a smooth primary profile, or nonexistence in the low-slope class.

Dependencies: the explicit canonical kernel, elementary homogeneous and Fourier facts stated above, the separately proved axis and radial-scattering identities, elementary regular-singular series with its majorant argument, finite-dimensional linear algebra, compactness, and the exact forced cubic relation. The numerical lane's implementation was not imported. Lead proof reviewed: ../analysis/referee/weak1/PROOF.md, read in full in this shift. Exact independently implemented checks passed and are recorded in verification/exact_checks.json. They check the formulas, while the proof supplies the regularity and compactness arguments.
