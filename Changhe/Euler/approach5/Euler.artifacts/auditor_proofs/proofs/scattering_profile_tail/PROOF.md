# The vorticity and velocity tails in scattering coordinates

Audit A210. Written: 2026-11-02T21:59:03Z. Status: CONFIRMED, with the critical-flux supplement below.

## Exact hypotheses and conclusion

Assume a real C^2 Euler profile U on R3, a C^1 pressure P, and

    (1-c)U+(Ay+U).grad U+omega JU+grad P=0, div U=0,
    A=cI-omega J, 1/3<c<1, omega in R.

Assume U is bounded, U(R .)->0 in distributions as R->infinity, and the Dini derivative condition of A209. Put Omega=curl U. Let S and K be as in A209, Q_s=exp(omega sJ), sigma(z)=log|z|/c, pi(z)=exp(-sigma(z)A)z. Then

    W(Sx)=DS(x)Omega(x), x outside K,

is continuous away from zero, divergence free on all R3 in distributions, and

    W(exp(sA)z)=exp(-s)Q_s^T W(z).

It is locally integrable and |W(z)|<=C|z|^(-1/c). There is a continuous angular vector G=W restricted to S2, and

    Omega(y)=|y|^(-1/c)Q_sigma(y)^T G(pi(y))+o(|y|^(-1/c))

uniformly as |y|->infinity. Its absolutely convergent Biot-Savart field V=T W is continuous away from zero, divergence free, curl V=W on R3, and satisfies

    V(exp(sA)z)=exp(-(1-c)s)Q_s^T V(z).

With F=V restricted to S2,

    U(y)=|y|^(-(1-c)/c)Q_sigma(y)^T F(pi(y))+o(|y|^(-(1-c)/c))

uniformly. If U!=0 then both F and G are nonzero.

The continuous tangent field Y(w)=G(w)-(w.G(w))w+(omega/c)(w.G(w))Jw on S2 satisfies

    div_S2 Y=((1-2c)/c)(w.G(w))

in distributions. Its radial datum has zero integral even when c=1/2. Every zero of Y gives an escaping B orbit lying entirely in {B cross Omega=0}; its nonempty compact backward limit is contained in K and in that closed degenerate set.

## Proof of the tail statements

Curling the profile equation gives [B,Omega]=-(1+c)Omega, equivalently Omega(Phi_s x)=exp(-(1+c)s)D Phi_s(x)Omega(x). Differentiate S composed with Phi_s=exp(sA)S and combine the two identities. This proves the exact homogeneity of W. Continuity follows from the C^1 diffeomorphism in A209. Homogeneity gives the angular formula and local integrability because 1/c<3.

For f supported away from zero, change variables z=S(x), with det DS=1, to get integral W.grad f=integral Omega.grad(f composed with S)=0. To extend across zero, first use a test g equal to one near zero. Its composition with S is constant on an open neighbourhood of K, is C^1 there and off K, and is compactly supported because S is proper. The same calculation applies. For a general test phi subtract phi(0)g. The remainder psi vanishes at zero, so ||grad(chi_epsilon psi)|| is bounded independently of epsilon for the usual cutoff supported in the 2epsilon ball. The error is at most C integral_(|z|<2epsilon)|W|=O(epsilon^(3-1/c)), which tends to zero. Thus div W=0 on R3; no point source has been discarded.

A209 gives DS->I and |S(y)-y|<=M/c. Express W(S(y))-W(y) at unit scale using its exact homogeneity. Its two rescaled arguments differ by O(1/|y|), and W is uniformly continuous on a fixed compact annulus. Thus W(S(y))-W(y)=o(|y|^(-1/c)) uniformly. The exact identity Omega=DS^-1 W composed with S proves the vorticity expansion.

Put beta=1/c, so 1<beta<3. Both W and Omega have weak L^(3/beta) bounds, and are in L^p+L^q for some 1<p<3/beta<q<3. The Biot-Savart kernel has size C|x|^-2. Its integral against W is absolutely convergent off zero: W is bounded locally at such x, integrable near zero, and the infinity integral is bounded by C integral_R^infinity r^-beta dr. The usual divergence and curl identities extend from test fields to L^p+L^q by the Hardy-Littlewood-Sobolev and Riesz-transform bounds. For a globally distributionally divergence-free field they give div T W=0 and curl T W=W. Equivalently the possible harmonic polynomial in the Helmholtz identity vanishes in L^p+L^q. Continuity away from zero follows by splitting the locally integrable kernel singularity from the dominated far integral.

The same argument for Omega gives curl T Omega=Omega. U-T Omega is an entire distributionally harmonic field. The mean value bound for T Omega in the corresponding finite-exponent sum spaces, together with bounded U, makes this difference constant; the distributional blow-down assumption fixes the constant to zero. This is the Biot-Savart uniqueness lemma already proved in A166, whose hypotheses are now supplied by the vorticity tail.

Rotation covariance and the change of variables y=exp(sA)z in the absolutely convergent integral give the stated homogeneity of V=T W. Let f=Omega-W. It is locally integrable and f(y)=o(|y|^-beta). Given epsilon>0 choose R so |f(y)|<=epsilon|y|^-beta for |y|>R. For |x|>2R,

    |T f(x)| <= C |x|^-2 ||f||_(L1(B_R))
                 + C epsilon integral |y|^-beta |x-y|^-2 dy
              <= C_R |x|^-2+C_beta epsilon |x|^(1-beta).

The last integral is finite exactly for 1<beta<3. Since 1-beta>-2, this proves the uniform little-o velocity expansion. If G=0, Omega=0 outside K; since K is null and Omega continuous, Omega=0 everywhere. Bounded harmonic U is constant, then zero by its blow-down. If F=0 then V=0 and W=curl V=0, giving the same conclusion.

## Projection to the sphere and the critical-flux supplement

Direct differentiation gives D pi(w)v=v-(w.v/c)Aw. This proves the formula for Y, its tangency, and D pi(exp(sA)w)W(exp(sA)w)=exp(-(1+c)s)Y(w). In coordinates z=exp(sA)w the volume form is c exp(3cs)ds dA(w). Test div W=0 with a(s)phi(w), integrate a' by parts, and obtain

    c integral_S2 grad phi.Y=-(1-2c) integral_S2 phi (w.G(w)).

For c!=1/2, setting phi=1 gives zero radial mean. For c=1/2 this particular equation gives no information about the mean. Instead test the already proved global equation div W=0 with a smooth radial cutoff equal to one near zero. The flux through a radius-r sphere is r^(2-1/c) integral_S2 w.G(w); at c=1/2 this is the constant radial mean. Integrating against the cutoff derivative forces that constant to vanish. This repairs the omitted endpoint step in the submitted proof, without changing its conclusion.

The hairy-ball theorem gives a zero w0 of continuous Y. Its defining formula says G(w0) is proportional to Aw0. Exact homogeneity then makes W proportional to Az along the whole linear orbit exp(sA)w0. Applying DS^-1 and DS B=A S gives B cross Omega=0 along its inverse image. Every backward B orbit is bounded, since B is radially outward outside a ball. Its limit set is nonempty, compact and invariant, and full invariance plus boundedness puts it in K. Closedness of {B cross Omega=0} gives the final inclusion.

## Dependencies and limitations

Dependencies: A209; the exact vorticity transport identity; the Biot-Savart uniqueness and boundedness argument A166; elementary distributional cutoff arguments; hairy-ball theorem. The new proof does not use an energy identity. It verifies Theory Agent A SCATTERING_TAIL Theorem T and Corollary T.6 for their stated Dini hypothesis and full range 1/3<c<1. At c=1/2, later formulas dividing by 1-2c are not part of this theorem. It gives no tail theorem from velocity decay alone and no exclusion in the target range.
