# The translation mode in material-center dynamic rescaling

Status: complete informal verification of the lead's instability mechanism, with the convergence claim restricted to what the linearized identity proves.

## Statement and notation

Let P=(Theta,Omega) be a smooth nontrivial whole-plane B2 stationary profile, with a0=1, c=Psi_xy(0)=1+beta/2, and U=o(r). Let the relative inverse be translation covariant, as the unique sublinear div-curl inverse modulo constants is. Consider the dynamic equations

    d_s P = E_beta(P),
    E_beta(P) = ((beta-2)Theta-W.grad Theta,
                 -Omega+Theta_x-W.grad Omega),
    W=beta X+U-U(0).

Let L be their pointwise linearization at the stationary profile with beta fixed. Set

    T = d_y P,
    D = (Theta-X.grad Theta, -X.grad Omega),
    mu = beta+c = 1+3 beta/2,
    a1 = (1/2)Theta_xxy(0).

Then LT=mu T and LD=0. For the adaptive prescription beta(P)=2c(P)-2, the linearized operator L_ad has the nonzero, normalization-preserving eigenvector

    H=T+a1 D,        L_ad H=mu H,
    delta a0[H]=0.

In particular mu>0. This is an exact linear instability direction in any function-space formulation that contains these smooth translation and scaling tangent vectors and for which the displayed linearization is valid. It is not by itself a nonlinear instability theorem in an unspecified norm.

## 1. Translate the full material-center operator

For h near zero, set P_h(X)=P(X+h e_y). The velocity representative can be chosen as U_h(X)=U(X+h e_y). Its relative velocity is U(X+h e_y)-U(h e_y), independently of additive gauge constants. At the shifted point, the original W differs from the newly centered one by

    d(h)=beta h e_y+U(h e_y)-U(0).

The reflection symmetry gives U_1(0,y)=0, so d(h) is vertical. Since E_beta(P)=0, direct substitution, with all reaction and forcing terms translated too, gives

    E_beta(P_h)(X)=d(h).grad P(X+h e_y).

Differentiate at h=0. Here d'(0)=beta e_y+U_y(0)=(beta+c)e_y. It follows that LT=mu T. A spatial translate is therefore generally not another stationary solution of this material-center equation with the computational origin fixed.

## 2. The dilation tangent and the normalized translation

The exact scaling family is

    Theta_lambda(X)=lambda Theta(X/lambda),
    Omega_lambda(X)=Omega(X/lambda).

It consists of stationary profiles at the same beta. Its derivative at lambda=1 is D, so LD=0. Under this scaling a0 becomes a0/lambda, while c is unchanged. Consequently

    delta a0[D]=-1,   delta c[D]=0,
    delta a0[T]=a1,   delta c[T]=c_y,

where c_y=Psi_xyy(0).

To relate a1 and c_y, write Theta=x^2 f(y)+O(x^4) and h(y)=Psi_x(0,y). The x^2 coefficient of the temperature equation is

    [beta y+h(y)-h(0)] f'(y) = [2h'(y)-beta-2] f(y).

At y=0, f(0)=1 and h'(0)=c. Differentiate this identity at zero. The right coefficient 2c-beta-2 vanishes, and the derivative of the bracket on the left is mu. Thus

    mu a1=2c_y.                                             (1)

At fixed fields, differentiation of E_beta in beta gives exactly D. The adaptive linearization is therefore

    L_ad V = L V + 2 delta c[V] D.

Use LT=mu T, LD=0, (1), and delta c[D]=0 to obtain

    L_ad(T+a1D)=mu T+2c_y D=mu(T+a1D).

Also delta a0[T+a1D]=a1-a1=0. Thus fixing a0 does not remove this mode.

## 3. The normalized mode is nonzero

If a1!=0 and H=0, its temperature component says

    (X-(0,1/a1)).grad Theta = Theta.

Along every ray about the point (0,1/a1), Theta is homogeneous of degree one. Smoothness at that point implies Theta is globally linear: divide Theta(center+rZ) by r and let r decrease to zero. A globally linear function even in x and vanishing on x=0 is zero. This contradicts a0=1.

If a1=0 and H=0, then Theta_y=0 everywhere. Hence Theta=f(x), with f'(x)!=0 for sufficiently small nonzero x. On such a vertical strip the temperature equation determines W_1=(beta-2)f/f', independently of y. Thus U_1 is independent of y there. Incompressibility then makes U_2,y=-U_1,x independent of y. The sublinear bound as |y| tends to infinity forces this slope to vanish for each such x. Continuity at x=0 gives U_1,x(0)=0, contrary to U_1,x(0)=-c and c=1+beta/2>0. This includes beta=2. Therefore H is nonzero.

## Numerical interpretation and scope

A time evolution that follows the material point at the computational origin has a positive translation direction, even after the a0 normalization. A projection or an additional frame-position condition can remove that direction. Special initial data on a stable set might also converge. The unqualified assertion that the method cannot converge is therefore stronger than this calculation proves.

A stationary Newton equation sees a nonzero eigenvalue mu in this direction; it is not a translation null direction. The dilation direction D remains a null direction until a normalization removes it. These statements do not establish good conditioning of the full Newton matrix or convergence of a discretized solver.

This proof uses the B2 equations, symmetry, center identities, the relative inverse's covariance, and the exact scaling from research/07_reconstruction_scaling. No far-field series, numerical pilot, or unpublished candidate is used.
