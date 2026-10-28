# Flat conormal inputs do not give the proposed exterior singularity

## Claim audited

Theory author note26 and S2_L2_THEORY remark(7) propose a fixed input with a one-sided power at a straight cone boundary. The proposed argument says that the order-minus-one commutator creates a nonzero power on the other side of that boundary. This claim is false for the IPM multipliers. The unboundedness of the sharp-cone map proved in proof 116 remains true, by a different family of inputs that concentrates in both coordinates.

## Exact local theorem

Let u be signed distance to a straight line and z its tangential coordinate. Let m>-1, and let a(u,z) be smooth and compactly supported. Set

 h(u,z)=u_+^m a(u,z).

For either component of the canonical IPM velocity U, the restriction U[h] to u<0 extends smoothly to the closed half-plane u<=0, locally in z. Every derivative has a continuous one-sided trace at u=0. This assertion concerns smoothness from the zero-input side; it does not assert that the two-sided velocity is smooth.

To prove it, let the unit normal in the original coordinates be n=(a_0,b_0) and the unit tangent be (-b_0,a_0). For normal frequency xi and tangential frequency eta, the two symbols have the form

 sigma_j(xi,eta)=c_j+[A_j xi eta+B_j eta^2]/(xi^2+eta^2),

with

 (c_1,A_1,B_1)=(a_0 b_0,a_0^2-b_0^2,-2a_0 b_0),
 (c_2,A_2,B_2)=(-a_0^2,2a_0 b_0,a_0^2-b_0^2).

These identities follow by rotating the numerators xi_original eta_original and -xi_original^2. They are checked symbolically in the accompanying code.

For eta nonzero, the inverse normal Fourier transforms of eta^2/(xi^2+eta^2) and xi eta/(xi^2+eta^2) are constant multiples of |eta| exp(-|eta||u|) and i eta sign(u) exp(-|eta||u|), respectively. The constants have magnitude1/2 in the usual Fourier convention. For output u<0 and input v>0, the absolute difference is v-u. The local identity part vanishes. Thus the partial tangential Fourier transform of U_j[h] is

 C_j(eta) exp(|eta|u) integral_0^infinity exp(-|eta|v) v^m ahat(v,eta) dv,  (1)

where |C_j(eta)|<=C|eta| and ahat is the Fourier transform of a in z.

For every integer N, smooth compact support gives |ahat(v,eta)|<=C_N(1+|eta|)^(-N), uniformly in v. For |eta|>=1, the integral in (1) is bounded by

 C_N Gamma(m+1)|eta|^(-m-1)(1+|eta|)^(-N).

For |eta|<=1 it is bounded uniformly, because m>-1. Applying p normal and q tangential output derivatives introduces at most |eta|^(p+q). Since N is arbitrary, the differentiated expressions are integrable in eta, uniformly for u<=0. Dominated convergence gives continuous derivatives of every order up to u=0. This proves the theorem without a pseudodifferential transmission assumption.

## Why the proposed commutator argument fails

On the normal frequency line, the principal commutator symbol is a constant multiple of 1/xi, not 1/|xi|. It is odd. Its inverse is an ordinary antiderivative, up to a constant complex factor and a smooth low-frequency term. The local antiderivative of u_+^m is u_+^(m+1)/(m+1). It does not produce u_-^(m+1). Therefore the asserted generic nonzero exterior coefficient c_- is zero for this principal term. Formula(1) proves that higher terms do not restore the claimed exterior power for a fixed smooth tangential amplitude.

## Application and limitations

Away from the origin, (|cos(theta)|-epsilon)_+^m is u_+^m times a smooth positive factor to the m-th power. The radial and angular cutoffs in the proposed test are smooth compact amplitudes. Hence the theorem applies at the straight boundary ray. Reflection patches, the strain correction and the axis-row subtraction are smooth on a sufficiently small boundary patch that avoids the axes and the other supports. One may choose this patch in an analytic part of the background.

This refutes the proposed proof by a fixed conormal power. It does not establish boundedness of C_R on the sharp-cone space. The packet family in proof 116 has tangential derivatives growing with the concentration scale, so the constants C_N above are not uniform for that family. Its exact-kernel proof of unboundedness is unaffected. Likewise no conclusion about a smooth variable-order space follows from the present theorem.
