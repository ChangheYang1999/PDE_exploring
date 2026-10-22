# A velocity interpolation defect at the moving center

Status: CONFIRMED structural defect of a specified interpolation rule, with an independent manufactured test. It refutes using that rule as an exactly incompressible smooth characteristic velocity at fixed resolution. It does not refute convergence of a repaired solver or any B2 profile.

## Exact statement and notation

Put x=r sin(phi), y=-r cos(phi). Let a smooth stream function have sine modes P_k(r)sin(k phi). With U=(-Psi_y,Psi_x), its polar components are U_r=-Psi_phi/r and U_phi=Psi_r. Suppose a numerical rule independently interpolates p_k=P_k/r^2 and d_k=P_k'/r as polynomials of a compactified coordinate t, then sets Ptilde_k=r^2 ptilde_k(t(r)) and Dtilde_k=r dtilde_k(t(r)). The resulting velocity need not be divergence free, even when every interpolation datum comes from an exact smooth compactly supported stream function. For the r2 map

    t(r)=1-(1+r^2/L^2)^(-1/(2 beta)), beta,L>0,

the same rule need not give a differentiable velocity at r=0. Decreasing the characteristic terminal radius at fixed interpolation resolution does not eliminate that structural defect.

## 1. Exact divergence formula

Direct polar differentiation of the represented velocity gives

    div Utilde=sum_k (k/r)[Dtilde_k-Ptilde_k']cos(k phi).

This is zero when Dtilde_k is obtained by differentiating Ptilde_k. Independent interpolation of P_k/r^2 and P_k'/r imposes no such identity. Knowing the true derivatives at the interpolation nodes is insufficient: differentiation and polynomial interpolation do not commute in general, and the factors r and r^2 also enter the identity.

## 2. A smooth canonical manufacture with unavoidable origin error

Fix the first interpolation interval [0,h] and any N distinct interior nodes 0<t_i<h. Choose a smooth radial cutoff eta equal to one throughout this interval in physical radius and compactly supported beyond it. Define the single-mode stream function

    Psi=r^2 sqrt(t(r)) sin(phi) eta(r).

The cutoff may be taken as a smooth function of r^2. Since sqrt(t(r))/r is a positive smooth function of r^2 near zero, Psi equals x r^2 times a smooth radial factor there. Hence Psi, Omega=-Delta Psi and U=(-Psi_y,Psi_x) are smooth on the plane and compactly supported. The ordinary full-plane inverse reproduces U: it has the prescribed curl and divergence, and the difference from the decaying Biot-Savart field is an entire decaying harmonic field, therefore zero. The manufacture has no artificial boundary or added harmonic strain.

On the first interval, P/r^2=sqrt(t). Let p be its degree N-1 interpolant through the positive nodes. Then p(0)>0, exactly. To see this, use

    sqrt(t)=(1/pi) integral_0^infinity [t/(t+s)] s^(-1/2) ds.

Interpolation is a finite linear operation. The interpolant of t/(t+s), evaluated at t=0, is

    product_i t_i/(s+t_i).

Indeed the usual polynomial interpolation remainder for 1/(t+s) gives this identity after multiplication by -s and addition of one. Equivalently, subtract the interpolating polynomial and multiply by t+s; the resulting degree N polynomial has roots t_i and its value at t=-s fixes its coefficient. The displayed integrals converge at both endpoints; finite linearity is legitimate. Thus

    p(0)=(1/pi) integral_0^infinity s^(-1/2) product_i[t_i/(s+t_i)] ds > 0.

Write p0=p(0), d0=d(0), where d is the separately interpolated P'/r. Since t=O(r^2), the represented single-mode velocity has leading terms

    Utilde_1=(p0-d0)xy/r+O(r^3),
    Utilde_2=(d0 x^2+p0 y^2)/r+O(r^3).

In particular Utilde_2(0,y)=p0|y|+O(|y|^3). It has no derivative at the origin because p0>0. This conclusion is independent of d0. The exact velocity is smooth and of order r^2; its interpolation has acquired a spurious degree-one term. At a fixed mesh, the leading velocity error divided by r does not tend to zero as r tends to zero. Nor does a smaller terminal radius repair the derivative used to transport the center jet.

This example need not meet the B2 center identities. A quadratic stream mode can be added to set the center strain, without removing the single-mode defect. The numerical manufacture below does meet both nontrivial center identities with a0=1, but satisfies neither coupled transport equation by design.

## 3. Independent numerical manufacture

The verifier code code_independent/interpolated_velocity_audit.py uses its own NumPy polynomial fits and five-point Cartesian differences. It neither imports nor runs the numerics lane's source. The field is

    Psi=sum_(k=1)^3 c_k r^(m_k) exp(-r^2) sin(k phi),
    (m1,m2,m3)=(3,2,3),
    (c1,c2,c3)=(-1/(2 beta),-(1+beta/2)/2,0.2).

Here r^3 sin(phi)=x r^2, r^2 sin(2phi)=-2xy and r^3 sin(3phi)=3x y^2-x^3. Consequently Psi_xy(0)=1+beta/2 and Omega_x(0)=4/beta. The third mode is harmonic to leading order. All fields decay, so the ordinary full-plane inverse is exact for this manufacture.

The first cell has width Nt^(-1.5), L=1.5 and seven interior Gauss-Legendre nodes. Both the independent p/d rule and the alternative P_k=r^(m_k) a_k(t), with D obtained by differentiating that same P, are tested at five off-axis angles and radii 1e-2,1e-3,1e-4,1e-5. All saved numbers are in verification/interpolated_velocity_audit.json; source SHA256 and actual times are included there.

At r=1e-5 the maximum absolute divergence for the separate p/d rule is:

| beta | Nt=32 | Nt=40 | Nt=64 |
|---:|---:|---:|---:|
| 2.5 | 0.01570635 | 0.01327386 | 0.00931974 |
| 3 | 0.01680320 | 0.01419822 | 0.00996641 |

For beta=3,Nt=40 the first physical node is approximately 0.036856. The velocity error divided by radius at 1e-5 is approximately 0.01924. The exact divergence formula agrees with the independent Cartesian difference to less than 1.5e-12 on these samples. The single regular-factor rule has algebraically zero divergence, sampled difference error below 2e-12, and velocity error divided by radius below 9e-15 at r=1e-5. These are floating-point manufactured checks, not rigorous global error bounds.

## 4. Application to the current numerical implementation

The read-only source snapshot candidate_snapshots/num_homotopy_20261020T1507 contains hashes and the current charnewton.py source. Its prepare method constructs nodal arrays (Psi/r^2,dPsi/r,ddPsi), and its velocity method interpolates their components separately. Its r2-map production runs use the same first-cell rule with Nt=40 and seven interior nodes. No inner smooth replacement occurs in the inspected method.

The manufactured values above are not residuals measured on the production coefficient states. They establish a defect of the actual rule, independently of an optimizer. Production-state errors still require evaluation of the published coefficients and reconstructed full-plane inverse. A repair must preserve modal center powers and derive the velocity and derivatives consistently from a single stream representation, or use a separately justified smooth inner patch with matching and cutoff refinement. Increasing Nt is a convergence experiment, not an identity restoring smoothness at each fixed Nt.

Dependencies: polar divergence, finite polynomial interpolation, the elementary integral for sqrt(t), smooth compactly supported Poisson inversion, and direct Cartesian Taylor expansion. No B2 existence or nonexistence claim follows from this packet.
