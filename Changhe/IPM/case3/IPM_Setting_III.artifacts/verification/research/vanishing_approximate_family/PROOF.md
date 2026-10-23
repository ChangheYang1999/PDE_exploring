# Uniformly small relative residuals along a smooth family converging to zero

Date: 2026-10-20. Status: independently derived explicit non-profile family. It demonstrates a failure of inference from small residuals near the excluded parameter endpoint. It is neither an exact solution nor a nonexistence theorem for the primary class.

## 1. Statement, normalization and limits

For 0<D<=1 put ell=1+D, eta=D/(1+D), p=1-eta=1/ell and a=4D. Define, on the whole plane,

    f(r)=(1+r^2)^(-eta/2), rho_D(x,y)=a y f(r),
    H(r)=integral_0^1 t^3 f(rt)dt,
    psi_D(x,y)=-a x y H(r), U_D=(-psi_y,psi_x).             (1)

All these fields are smooth at every finite point. They have the required parities and strict sublinear density and gradient growth, and U_D is their canonical full-plane IPM inverse. The center and reporting normalization are exact:

    rho_y(0)=a!=0, c=psi_xy(0)=-a/4=-D,
    ell+c=1, K=a, L_can=(K/a)^(1/eta)=1.                  (2)

Nevertheless they are not exact profiles for any D>0. Their unforced residual satisfies, at every point with y!=0,

    |R|/N_f <=4D, |R|/N_v <=4D.                           (3)

On the horizontal axis the residual and both denominators vanish by parity; no value is assigned to a zero-over-zero ratio there. The same bound holds for every limiting ratio from off the axis. On a disk of radius M,

    sup |R| <=16D^2 M.                                   (4)

As D decreases to zero, rho_D and U_D converge to zero in C-infinity on every compact set, while ell decreases to1 and the reporting length remains1. Thus, for every finite collection of boxes and every strictly positive absolute and relative tolerances, some member passes those tolerances and the exact center and scale tests, but it is not a nontrivial converged exact profile. The correct limit of this explicit normalized sequence is zero.

There is also a representative with K=1, obtained for a<1 by the genuine dilation lambda_D=a^(-1/eta):

    rho_D^K(x,y)=a y(1+r^2/lambda_D^2)^(-eta/2).            (5)

Here lambda_D tends to infinity, and the fields still converge to zero locally. The bound (3) is unchanged under this dilation. A fixed far-axis amplitude alone therefore does not prevent this local vanishing when the global reporting length diverges.

## 2. Smooth canonical inversion

The integral defining H is a smooth function of r^2. For r>0, equivalently

    H(r)=r^(-4) integral_0^r s^3 f(s)ds,
    r H'(r)=f(r)-4H(r).                                  (6)

Differentiation gives H''+5H'/r=f'/r. Since Delta(xyH)=xy(H''+5H'/r), equation (1) satisfies

    -Delta psi=a xy f'/r=partial_x rho.

The stream parities and smoothness are exact. Since f(r) is asymptotic to r^(-eta), elementary integration of (6) gives H(r) asymptotic to r^(-eta)/(4-eta). Thus U=O(r^(1-eta))=o(r), and grad rho=O(r^(-eta)). This verifies the defining growth and canonical gauge. Any other smooth sublinear velocity with the same div-curl equations differs by an entire harmonic sublinear vector field. Its derivatives vanish by the interior disk estimate as the disk radius tends to infinity, so it is constant; parity removes the constant. Consequently (1) is the unique prescribed velocity, not a fitted strain.

At zero, H(0)=1/4, giving c=-a/4 and (2). The axis tail is rho(0,y) asymptotic to a y^p. These identities hold exactly for every D, not as a small-D expansion.

## 3. Exact residual and uniform bound

For r>0 write q=r^2/(1+r^2), tau=H/f and J=rH'/f. Since f decreases and its logarithmic derivative lies between -eta and0, for0<s<r,

    f(r)<=f(s)<=f(r)(r/s)^eta.

Using (6) gives

    1/4<=tau<=1/(4-eta), J=1-4tau,
    -eta/(4-eta)<=J<=0.                                  (7)

Write ctheta=x/r and stheta=y/r. Direct differentiation of (1) gives

    U_1=a x f(tau+stheta^2 J),
    U_2=-a y f(tau+ctheta^2 J),
    X.grad rho/rho=1-eta q,
    U.grad rho/rho=-a f[tau+ctheta^2 J+eta q tau cos(2theta)].

The last identity follows either by multiplication or from U.X/r^2=a f tau cos(2theta). Because ell eta=D and a=4D, the exact residual quotient is

    R/rho=D[(1-q)-4f(tau+ctheta^2 J+eta q tau cos(2theta))]. (8)

The same expression extends continuously to zero. For eta<=1/2, (7), f<=1 and q<=1 imply

    |R/rho| <=D[1+4(1+2eta)/(4-eta)] <=(23/7)D<4D.

Both N_f and N_v contain |rho| as a nonnegative summand, which proves (3). Since |rho|<=a|y|=4D|y|, (4) follows. No lower bound on a denominator away from the axis or a finite-grid argument is used.

On the positive vertical axis, (8) reduces to

    R/rho=D(1-q)-a f tau(1-eta q).

As y tends to infinity, the first term is O(y^-2), while the second is asymptotic to -a p y^-eta/(4-eta). It is therefore nonzero for all sufficiently large y. In absolute form,

    R(0,y) ~ -a^2 p/(4-eta) y^(1-2eta).                   (9)

For0<D<1 this actually grows in magnitude at infinity, even though the relative bound is uniformly small. AtD=1 its limit is a nonzero constant. Thus this family fails the defining transport equation at every parameter, and a fixed set of finite-box absolute checks cannot replace the full-plane far-field check.

## 4. Compact convergence and higher-jet diagnostics

The functions f(r) and H(r) depend smoothly on eta on each compact set of r^2>=0, including eta=0, where f=1 and H=1/4. Since a=4D tends tozero, all compact derivatives of rho and U tend tozero. Their first rescaled limits are rho_D/(4D)->y and U_D/D->(x,-y), but the unrescaled limit is the zero field. This distinction is necessary when describing an affine shape after amplitude renormalization.

For the K=1 representative (5), lambda_D tends toinfinity because log lambda_D=-log(4D)/eta tends toinfinity. On each fixed compact set, r/lambda_D tends uniformly tozero. Differentiation of (5) and its scaled canonical stream again gives convergence tozero in every compact C^k norm. The a and ell parameters are invariant under this dilation; setting K=1 did not keep the local amplitude nonzero.

The center cubic density coefficients are

    b=e=-a eta/2, H_4=0,

where H_4 is the difference of the x^3y and xy^3 stream coefficients used in the independent T2 relation. Indeed, H(r)=1/4-eta r^2/12+O(r^4), so those two stream coefficients agree. With A=2ell-1, the two necessary unforced jet defects are

    T1=(a-2A)b-6e=16D^2/(1+D),
    T2=(a-4A)b-3aH_4=8D^2.                               (10)

They both tend tozero in absolute value but are nonzero for every D>0. In the reporting representative L_can=1,

    T1/a^2=1/(1+D), T2/a^2=1/2.

For a different dilation the invariant versions are T1 L_can^2/a^2 and T2 L_can^2/a^2. These defects do not disappear under the proposed normalizations. They give an explicit check that shrinking absolute higher-jet errors are insufficient when the amplitude shrinks simultaneously.

## 5. Relation to the global energy obstruction

Let R_g=sup|grad rho_D| and V_g=sup|DU_D|_Frob. Directly,

    |grad rho|^2=a^2 f^2[1-eta q(2-eta q)sin^2(theta)]<=a^2,

with equality atzero, so R_g=a=4D. To bound V_g, use H(r)=integral_0^1 t^3 f(rt)dt. The logarithmic derivative bound gives |rH'|<=eta H. Also

    r^2 f''/f=eta(eta+2)q^2-eta q,

so |r^2H''|<=eta(eta+3)H. From the product Hessian of xyH, the Frobenius bounds |D^2(xy)|=sqrt(2), |grad(xy)|=r and |xy|<=r^2/2 give

    |D^2(xyH)|_Frob <= [sqrt(2)+4eta+eta^2/2]H.

Since H<=1/4 and rotating a Hessian preserves its Frobenius norm,

    V_g <=D[sqrt(2)+4eta+eta^2/2], R_g+V_g<8D.             (11)

Thus both global gradients vanish, consistently violating the independently proved nonzero-exact-profile bound 2ell-1<=C_*(R_g+V_g) for all sufficiently small D. This does not need a numerical maximum estimate. It explains why very small residuals along the explicit vanishing family cannot certify a genuine solution.

## 6. Dependencies and scope

All formulas above are elementary differentiations and a one-dimensional integral. Canonicity uses the already proved sublinear div-curl uniqueness. Section5 compares with ../small_gradient_exclusion/PROOF.md, but neither the residual estimate nor the proof of nonexactness depends on that theorem. The family supplies a rigorous manufactured failure test for continuation and convergence diagnostics. It makes no assertion that a particular numerical sequence converges to this family, to an affine field, or to zero. Those are separate questions requiring its actual data and a specified normalization.
