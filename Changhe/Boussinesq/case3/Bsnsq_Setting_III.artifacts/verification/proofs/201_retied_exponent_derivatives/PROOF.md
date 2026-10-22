# Differentiating a retied exponent and a projected coefficient map

## Exact statement and hypotheses

Fix L>0, a finite collection of cardinal splines B_j on [0,1] with fixed knots, and masked cosine coefficients z_(k,j). The masks and knots do not depend on b>0. Write X=(r sin phi,-r cos phi), ell=log(1+(r/L)^2)/2, zeta=exp(-ell/b), t=1-zeta, and rho_odd=r/sqrt(r^2+L^2). Let S_z(t,phi)=sum_(k,j) z_(k,j) B_j(t) cos(k phi), with the factor rho_odd multiplying odd k; rho_odd is independent of b. Define D_q=exp(-ell-q ell/b), and R_(q,b,z)=D_q S_z(t,phi), where q=1 gives the divided vorticity G, and q=2 gives the divided temperature F. R denotes the represented scalar field, never the nonlinear PDE residual. Even k have no additional radial factor. All formulas below apply also at r=0 by their smooth limits in the admissible masked representations. Indeed the mask removes j<floor(k/2). On the first clamped spline cell each remaining nonzero B_j vanishes to at least order floor(k/2) in t; indices past the first-cell degree vanish identically near0. Since t/r^2 is a positive smooth function of r^2, and rho_odd/r is smooth in r^2, the mode has r^k times a smooth function of r^2. The factor r^k cos(k phi)=Re(-y+ix)^k is a Cartesian polynomial. Thus the masked modes are smooth at the center. At knots use derivatives that exist; degree-five simple-knot splines have four continuous t derivatives, enough for the two derivatives used here.

At fixed coefficients, physical point and L,

 partial_b R = D_q ell/b^2 [q S-zeta S_t],
 partial_b^2 R = D_q {ell^2/b^4 [q^2 S-(2q+1)zeta S_t+zeta^2 S_tt]
                       -2ell/b^3 [q S-zeta S_t]}.

For a differentiable coefficient path z(b), add R_(q,b,z') to the first derivative. For a C2 path its second derivative is the fixed-coefficient second derivative plus2 partial_b R_(q,b,z')+R_(q,b,z''), where the partial derivative in the cross term holds z' fixed. There is no R_zz term because R is linear in z; nonlinear PDE residuals generally do have such a term. These are physical-field derivatives; a derivative of coefficients in a changing basis alone omits the displayed basis contribution. Multiplication by x or x^2 gives the corresponding derivatives of Omega or Theta.

## Derivation and strain projection

Since partial_b zeta=zeta ell/b^2, partial_b t=-zeta ell/b^2 and partial_b D_q=q ell D_q/b^2, the first formula follows by the product and chain rules. Differentiating its bracket gives ell/b^2[-(q+1)zeta S_t+zeta^2 S_tt]. A second product rule gives the second formula. Odd-mode factors remain fixed throughout.

For the canonical inverse of Omega=xG, the center strain is the linear functional

 c_b(z)=-(b L/4) sum_j integral_0^1 B_j(t)dt [z_(1,j)-z_(3,j)],

with inactive entries omitted. This follows from the angular identity and radial Jacobian proved in P200. In Euclidean coefficient coordinates let q_b=grad c_b=b q_1 and Q_b=||q_b||^2>0. Fix the native forcing source, its strain c_f, lambda, and a coefficient vector z0. The total-strain projection is

 p(b,lambda)=z0+q_b[1+b/2-c_b(z0)-lambda c_f]/Q_b.

It satisfies c_b(p)+lambda c_f=1+b/2. At fixed z0 and fixed native source,

 p_lambda=-c_f q_b/Q_b,
 p_b=(lambda c_f-1) q_b/(b Q_b),
 p_bb=-2 p_b/b,
 p_b_lambda=c_f q_b/(b Q_b).

To prove these formulas, substitute q_b=b q_1 and c_b=b c_1, so the correction is q_1/||q_1||^2 times [(1-lambda c_f)/b+1/2-c_1(z0)]. Direct differentiation proves all four formulas. Consequently c_b(p_b)=(lambda c_f-1)/b. The derivative of the total strain is c_b(p_b)+c_b(p)/b=1/2, as required. The partial b derivative does not preserve the input vorticity center coefficient4a0/b: this projection fixes only strain. A characteristic reconstruction with center boundary values4a0 x/b contributes their derivative -4a0 x/b^2 separately.

When beta=b and W_b=bX+V_b[Omega_(b,p)]+lambda V_f, the notation V_b means the same canonical linear physical inverse applied to a b-dependent source, not a b-dependent physical kernel. Its derivative is X+V[partial_b Omega_(b,p)], with the basis and coefficient contributions both retained. The center derivative of this response is diag(1/2,3/2), because DW_b(0)=diag(b/2-1,3b/2+1). The forcing source stays in its own fixed recorded basis; it contributes no b derivative. Differentiation under the relative whole-plane integral is justified for these finite spline families on any compact b interval in (0,infinity): their far-field bounds are uniform positive power decay times at most powers of log r, which remain integrable against the once-subtracted kernel, and the local kernels are locally integrable with uniform source bounds. The strain derivative also has the finite integral formula above.

## Reduced derivatives in a finite coefficient problem

Let T(z,b,lambda) be a C1 finite-dimensional map on an open neighborhood of the point, with a genuine fixed point z*=T(z*,b,lambda). Suppose A=D_z T-I is invertible. The finite-dimensional implicit function theorem gives a local differentiable branch and

 A z*_lambda=-T_lambda,   A z*_b=-T_b.

For the diagnostic m=c_b(z*)+lambda c_f-1-b/2,

 m_lambda=c_b(z*_lambda)+c_f,
 m_b=c_b(z*_b)+c_b(z*)/b-1/2.

These are chain-rule identities. They need not be zero: this fixed point may be the inner scalar-reconstruction iteration with a separate outer strain diagnostic. If the equations above are evaluated only at an approximate fixed point using finite differences for T, they are formal linear-response diagnostics. Matrix invertibility there is not a proof of a fixed point, of a nearby branch, or of a continuum solution. The numerical errors in the matrix, parameter columns and linear solve must be reported separately. No second derivative or nondegenerate fold follows from these first derivatives alone.

The C1 hypothesis cannot in general be weakened to mere differentiability. For a one-dimensional control, put f(0)=0 and f(x)=x+x^2 sin(1/x^2) for x!=0. Then f is differentiable with f'(0)=1. At x=(2pi n)^(-1/2), f'=1-2/x<0 for all large n, while at x=((2n+1)pi)^(-1/2), f'=1+2/x>0. Thus f is not increasing on any interval around0. Take T(z,b)=z-f(z)+b. At (0,0), T=z and D_zT-I=-1 is invertible. If a C1 fixed-point branch z(b) through0 existed, differentiating f(z(b))=b at0 would give z'(0)=1. Its C1 regularity would make z strictly increasing near0, with image an interval around0, and f its increasing inverse there, a contradiction. This control refutes the overly weak IFT hypothesis, not the corrected C1 statement.

## Logarithmic tails and the topology of exponent variation

Suppose sin(phi) S_z(1,phi) is nonzero in a tested direction. The temperature statements require sin^2(phi) S_z(1,phi)!=0 for the temperature coefficients in their direction. At fixed coefficients,

 Omega_b(r,phi)=r^(-1/b) a_b(phi)+O(r^(-2/b)),
 partial_b Omega_b(r,phi)=r^(-1/b)[a_b(phi) log(r/L)/b^2+o(log r)],

where a_b=L^(1+1/b) sin(phi) S_z(1,phi), with the limiting odd factors replaced by1. For temperature the additive expansion is Theta_b=r^(1-2/b) A_b(phi)+O(r^(1-2/b-min(1/b,2))), uniformly in angle, with A_b=L^(1+2/b) sin^2(phi) S_z(1,phi). The logarithmic multiplier in its b derivative is2/b^2. No relative error uniform through zeros of A_b is asserted. The displayed remainders only state a leading asymptotic; the next radial power can coincide with geometric correction powers at special b, without changing the leading logarithm. The vorticity remainder O(r^(-2/b)) as written requires b>=1/2; for general b>0 replace it by O(r^(-1/b-min(1/b,2))). The analogous relative correction for temperature is O(r^(-min(1/b,2))).

For b0>0 and a coefficient family whose endpoint amplitude varies continuously and is nonzero at some direction at b0, exponent changes are not continuous in the critical norm sup_X (1+|X|)^(1/b0)|Omega(X)|. For b>b0 arbitrarily close to b0, the weighted difference from the b0 field is infinite in that direction. For b<b0 the large-r weighted difference has the nonzero signed limit -a_b0(phi), of magnitude |a_b0(phi)|, so it cannot tend to zero with b. The temperature statement is the same in the critical norm sup_X (1+|X|)^(-(1-2/b0))|Theta(X)|. Pointwise and compact-set differentiability do not fix this obstruction.

With a strictly weaker fixed weight, for example vorticity weight (1+r)^(1/b0-eps) for eps>0, choose a neighborhood of b0 with |1/b-1/b0|<eps/2. The zeroth, first and second parameter derivatives are uniformly bounded in that weighted norm by C(1+r)^(-eps/2)(1+log^2(2+r)). Uniform tail control and ordinary compact-set differentiation show twice continuous differentiability in that weighted sup-C0 norm for a C2 coefficient path. Norms involving spatial derivatives or Holder seminorms require their own estimates and are not asserted here. For temperature use weight (1+r)^(-(1-2/b0+eps)) and |2/b-2/b0|<eps/2. These statements concern finite represented fields; no fitted branch has been established.

## Verification plan and scope

Independent exact algebra will check the chain rules, strain projection and reduced formulas. Native frozen archives will be read only through this lane's SciPy reader, evaluated with perturbed basis exponent and fixed coefficients on physical Cartesian points, and compared with the analytic derivatives at several steps. The code does not import the numerical lane's map or differentiation implementation. The formulas diagnose what a retied-beta column must include; they do not claim that the unpublished column is wrong. The B2 endpoint remains OPEN.
