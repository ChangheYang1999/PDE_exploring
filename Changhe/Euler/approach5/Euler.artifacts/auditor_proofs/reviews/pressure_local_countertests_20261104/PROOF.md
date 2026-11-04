# Exact local countertests for pressure rigidity

## 1. Statements and scope

Let 0<c<1/2, omega be any finite real number, J(x_1,x_2,z)=(-x_2,x_1,0), A=cI-omega J and B=Ay+U. We check the full profile equation

    (1-c)U+(B.grad)U+omega JU+grad P=0,   div U=0.

Two explicit families show that local regularity and momentum alone do not supply two proposed rigidity inputs. For every alpha in (0,1), a global C^{1,alpha}_loc zero-swirl solution with smooth axisymmetric pressure has zero axis vorticity but unbounded Omega_theta/r near the axis. A smooth affine solution has negative Gamma partial_theta P, in fact partial_theta P/Gamma=-1 at specified points. Here Omega=curl U, Gamma=(Jy).U and partial_theta P=(Jy).grad P.

Both families grow at infinity. They do not refute the global uniformly sublinear or decaying results, do not settle their lowest possible regularity, and do not provide a counterexample to the campaign conjecture. All claims are established by exact differentiation below; no formal build or computation is used.

## 2. A Holder-regular profile and its full residual

Fix kappa nonzero and alpha in (0,1), and put

    a=(1+alpha c)/(1-alpha),
    U=(a x_1,a x_2,-2a z+kappa r^(1+alpha)),
    P=-a(1+a)r^2/2-a(2a-1)z^2,
    r=(x_1^2+x_2^2)^(1/2).

The gradient of r^(1+alpha) is (1+alpha)r^(alpha-1)(x_1,x_2) away from zero and tends to zero at zero. To verify its alpha-Holder regularity, take two horizontal points, let R be the larger radius and d their separation. If d>=R/2, the difference of their gradients is bounded by C R^alpha<=C' d^alpha. If d<R/2, their segment has radius at least R/2, so its Hessian bound C R^(alpha-1) gives a gradient difference at most C R^(alpha-1)d<=C d^alpha. This proves C^{1,alpha}_loc in all three variables. The radial second derivative kappa alpha(1+alpha)r^(alpha-1) is unbounded at the axis, so the velocity is not C2 there.

Divergence is a+a-2a=0. Rotational covariance gives (Jy).grad U=JU, so the omega terms in full momentum cancel. The radial carrier component is (c+a)r, and its vertical component is (c-2a)z+kappa r^(1+alpha). The radial residual before pressure is a(1+a)r. The vertical residual is

    2a(2a-1)z
      +kappa r^(1+alpha)[1-c-2a+(c+a)(1+alpha)].

The bracket equals 1-a+alpha(c+a)=0 by the definition of a. The gradient of the displayed pressure cancels both remaining components, and the azimuthal component is zero. The identity extends from r>0 to the axis by continuity. Thus these are classical C1 solutions for every finite omega, with the stated pressure.

## 3. The quotient, source and growth

The horizontal gradient of U_z vanishes on the axis. Direct curl computation gives

    Omega_theta=-kappa(1+alpha)r^alpha,
    Omega_theta/r=-kappa(1+alpha)r^(alpha-1).

All vorticity components tend to zero at the axis, but the displayed quotient is unbounded on every punctured axis neighborhood. This refutes the inference from local C^{1,alpha} regularity, zero swirl, zero axis vorticity and full momentum to a locally bounded quotient. It does not refute such an inference with additional global sublinearity.

The matrix DU is lower triangular with diagonal (a,a,-2a); hence tr((DU)^2)=6a^2. Also -Delta P=2a(1+a)+2a(2a-1)=6a^2. The pressure-source identity agrees exactly. The term kappa r^(1+alpha) is superlinear along horizontal rays. Its square integrates to a positive constant times R^(5+2alpha) on B_R. The remaining squares have order R^5, and the cross term with z has zero integral by oddness. The energy therefore has order R^(5+2alpha). Neither the sublinear nor the small-energy hypothesis holds.

## 4. Affine negative angular work

Fix s nonzero, let M=diag(s,-s,0), and put

    U=My,
    P=-[(s+s^2)x_1^2+(-s+s^2)x_2^2+4omega s x_1x_2]/2.

For any constant trace-free matrix M the pressure-free full residual is

    [M+M^2+omega(JM-MJ)]y.

Indeed the cM contributions from (1-c)U and the carrier cancel. Here JM-MJ has horizontal off-diagonal entries 2s, so the displayed matrix is symmetric and is exactly minus the Hessian of P. Divergence is zero, and full momentum holds for every c and omega. The velocity is irrotational because M is symmetric.

Nonetheless

    Gamma=-2s x_1x_2,
    partial_theta P=2s x_1x_2+2omega s(x_2^2-x_1^2).

At x_1=x_2=t nonzero, Gamma=-2s t^2 and partial_theta P=2s t^2. Thus Gamma partial_theta P=-Gamma^2<0 and partial_theta P/Gamma=-1, independently of omega. This profile has linear growth and energy of order R^5. Irrotationality alone is not zero swirl, and this example fails the required global sublinearity.

## 5. The conditional torque implication and its limit

Differentiating Gamma and using full momentum gives

    B.grad Gamma+(1-2c)Gamma=-partial_theta P.

For detail, (JB).U=c Gamma-omega(J^2y).U, and (Jy).JU=-(J^2y).U; these cancel the two rotation contributions. Let epsilon>0. On a compact region containing a complete backward trajectory, suppose

    Gamma partial_theta P>=-(1-2c-epsilon)Gamma^2.

Then B.grad Gamma^2<=-2epsilon Gamma^2. If Gamma at the terminal point were nonzero, integrating this differential inequality backward gives Gamma(Phi_t y)^2>=exp(-2epsilon t)Gamma(y)^2 for t<0. Continuity on the compact trajectory closure contradicts this as t tends to minus infinity. Hence Gamma vanishes at the terminal point. If every point of a region has such a trajectory and the inequality holds there, Gamma vanishes throughout that region.

At the affine points in Section 4 the premise would require -1>=-(1-2c-epsilon), or 0>=2c+epsilon, which is false. Thus full smooth momentum does not supply either nonnegative angular work or this strict inequality as an automatic local identity or inequality. A derivation using global decay remains a different, unresolved question. The sufficient torque condition by itself does not perform the later vorticity and harmonic steps of the absorbing-ball theorem.

## 6. Verification and dependencies

All six source sections, the fourteen author manual checks and their supporting plan were read in full. This reconstruction checks the regularity, all components of full momentum, pressure source, energy growth, exact angular ratio, and the direction of the backward differential inequality. No external theorem beyond elementary differentiability, ODE integration and compact boundedness is used. No numerical or symbolic computation was needed or performed. Existing configured model comparison is pending; actual provider execution is independently unattested.

## 7. Complete existing-agent comparison and disposition

The full C comparison dated 2026-11-04T07:11:50Z, including items14-17 on these examples, was read. The exact residuals, Holder estimate, source, energy powers and affine ratio agree with Sections2-5. The identity a-1=alpha(1+c)/(1-alpha)>0 also makes the failure of large-ball radial trapping explicit. The torque inequality has the stated backward growth direction.

This confirms only the local inferences refuted by the displayed exact examples and the explicitly conditional torque implication. It does not refute any theorem that includes uniform sublinearity or decay, and does not show that C2 is the sharp regularity for pressure rigidity. Indeed the separate C1 integrable-quotient proof avoids the locally false bounded-quotient inference. The described symbolic checks, random sample and numerical flow check were not read or rerun here and are not certified. Existing collaboration is with the configured model C agent, actual provider execution independently unattested.
