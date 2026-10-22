# A joint local and leading-tail chart for the horizontal primitive

Status: complete informal construction written before implementation. Written actual Opus5.5 reviews182 (tail dependency) and183 (local and combined map) CONFIRMED the displayed construction; all independent implementation controls passed. It defines a trial family only. No profile, convergence or broad exclusion is claimed.

## Statement and exact variables

The convention is exactly that of PROMPT.md: grad_perp Psi=(-Psi_y,Psi_x), Omega=-DeltaPsi and curl V=-Omega. The canonical relative kernel is K(z)=(z2,-z1)/(2pi|z|²), used as K(X-Y)-K(-Y). No sign change of temperature or a0 is made. Independent Cartesian and inverse controls use this same convention.

Fix beta>2, a0 nonzero, s=1/beta, m=1-2s, R=sqrt(1+x²+y²), and t=R^-s. Let E be the finite-dimensional span of the smooth odd streams

    x R^(1-s-d) T_i(2t-1) T_j(y/R),

modulo their linear x term, with d in{0,1}, at least four radial and four angular basis functions. Impose Psi_xy(0)=1+beta/2 and (-DeltaPsi)_x(0)=4a0/beta on the E component. Add the three actual stream directions

    K4=xy³ R^-8, K50=x^5 R^-8, K52=xy^4 R^-8.

For any stream define Omega=-DeltaPsi, V=grad_perpPsi-grad_perpPsi(0), W=beta X+V, F=W.gradOmega+Omega, Theta=int_0^x F(u,y)du and RT=W.gradTheta-(beta-2)Theta. This temperature is defined by an exact integral. It satisfies the vorticity equation and Theta(0,y)=0. A quadrature approximation has to be differentiated independently before this identity can be claimed numerically.

There is an explicit smooth finite-parameter map into E+span{K4,K50,K52} that enforces all of the following exactly:

1. The two prescribed center conditions, hence Theta=a0x²+O(|X|³).
2. The two leading homogeneous angular-primitive moments C_plus=C_minus=0.
3. Every Taylor coefficient of RT through total degree4 is0.

Its image contains every stream in this augmented finite space satisfying these constraints. This is a surjectivity statement; no coefficient injectivity or absence of other basis kernels is claimed. The map is polynomial in its free coefficients for each fixed beta and smooth for beta>2. Its full derivative can be checked without differentiating a PDE solver.

## Leading-tail correction, stated explicitly

Write the first two stream tails as r^(2-s)cos(theta)p(z)+r^(2-2s)cos(theta)p1(z), z=sin(theta), modulo the relative linear gauge. The d=1 block begins at a smaller degree and does not change these two tails. Put

    Dp=(1-z²)p'-zp,
    L_k p=(k²-1)p-3zp'+(1-z²)p'', q=-L_(2-s)p,
    h=L_(2-2s)p1+s(Dp)q+(2-s)p(Dq).

For h=sum h_j z^j the two primitive moments are

    C_sigma=sum_j h_j sigma^j/(j-m), sigma=+1,-1.

Packet130 proves these formulas by direct polar differentiation and elementary one-dimensional antiderivatives. In particular h is linear in p1 and quadratic in p. Adding

    a H0+b H1,
    H0=x R^(1-2s)(1-t)², H1=xy R^-2s(1-t),

preserves the center and p, changes p1 to p1+a+bz, and changes the moments by

    delta C_plus=-(m+2)a-(m+3)b,
    delta C_minus=-(m+2)a+(m+3)b.

Thus choose a=(C_plus+C_minus)/(2(m+2)) and b=(C_plus-C_minus)/(2(m+3)). Both directions lie in E. Choose the affine complement whose coefficient positions (i,j,d)=(3,0,0),(2,1,0) vanish before this repair. Their direction entries1/32 and-1/8 make this a valid complement. Packet130's explicit rank calculation proves that every center- and moment-compatible E coefficient field is obtained this way. The repaired coefficient vector C(z) is polynomial of degree at most2 in the complement coordinates z.

## Local correction and noninterference

For Psi_C in E after that repair, read its Taylor coefficients through degree5:

    Psi_C=l x+cxy+p0 x³+q0 xy²+d0 x³y+e0 xy³
                         +f0 x^5+g0 x³y²+h0 xy^4+O(|X|^6).

Set lambda1=(beta-2)/2, lambda2=(3beta+2)/2 and b0=4a0/beta. Define

    b1=-6d0-6e0, b20=-20f0-2g0, b02=-6g0-12h0,
    a1=((2beta+1)b1-2q0 b0)/2,
    a20=((3lambda1+1)b20-d0 b0+3p0 b1)/4,
    a02=((lambda1+2lambda2+1)b02-q0 b1-3e0 b0)/2.

Direct differentiation, horizontal integration and multiplication give

    r21=lambda2 a1-4q0 a0,
    r40=2lambda1 a20-2d0 a0+3p0 a1,
    r22=2lambda2 a02-6e0 a0-3q0 a1.

These are all possibly nonzero coefficients of RT through degree4; the degree2 coefficient is already0. Add e K4 with

    e=r21/[3lambda2(2beta+1)].

Recompute r40,r22 after replacing e0 by e0+e, then add

    f K50+h K52,
    f=r40/[10lambda1(3lambda1+1)],
    h=r22/[12lambda2(lambda1+2lambda2+1)].

The direct coefficient calculation in packet132 proves this triangular system and its unique solution. The nonzero denominators require beta>2. The K4 jet starts at degree4 and then6; the other jets start at degree5 and then7. Consequently the additions preserve all the center data. Their complete derivatives decay: K4=O_symbol(r^-4) and K50,K52=O_symbol(r^-3). They cannot change p,p1 or either leading moment. Hence the local repair preserves the preceding tail repair, establishing properties1 to3.

To prove the stated surjectivity, take a stream in E+spanK satisfying all three constraints and choose a decomposition Psi_E+e_*K4+f_*K50+h_*K52. Since the K directions do not change the center or leading moments, Psi_E satisfies those constraints and is attained by the tail chart. For this fixed Psi_E, the triangular system has a unique triple giving RT flat through degree4, so the local repair returns (e_*,f_*,h_*). This proves coverage, even if the augmented coefficient representation has a redundancy.

## Derivatives, serialization and inverse

The jet coefficients are linear functions of C. On the fixed-center affine space e is linear in the jet, while f and h are polynomials of degree at most2 in it after the triangular substitution. Composing with C(z) gives a polynomial map of degree at most4. Its analytic derivative is the ordinary derivative of these displayed polynomial formulas. An implementation may compute its directional derivatives by complex-step polynomial evaluation, with separate real five-point controls. This method is applied to the finite coefficient map only, never through absolute values or residual normalizers. The primitive residual then uses the ordinary chain rule. A free-beta column must differentiate the complete map, basis powers and quadrature, for example by centered differences of the complete residual.

For rational beta, exact rational center projection and tail repair, followed by an ordinary rational Taylor expansion and this local repair, give exact serialized coefficients. The three K coefficients are stored as exact rational JSON entries next to the ordinary basis coefficients. Direct bivariate differentiation of these JSON values can independently verify the center, zero degree4 coefficients and any higher nonzero coefficient. Importing coefficients alone is not proof.

Each corrected stream is smooth on the entire plane and odd in x. The new directions have power-decaying vorticity and sublinear velocity, so their once-subtracted whole-plane Biot-Savart integral converges absolutely. The integral equals the differentiated relative stream velocity by the harmonic uniqueness argument of packets03 and132: the difference is entire, harmonic, sublinear and0 at the origin. There is no wall, exterior multipole or independently fitted drift. The exact primitive preserves even temperature and the prescribed axis normalization.

## Scope and planned checks

The theorem does not enforce the full thermal PDE, a regular higher far-field expansion, positivity or any error bound to a nearby solution. Beta remains an unknown in the free runs; the lambda1 denominator can be poorly conditioned near2. The finite angular span is a trial choice, not a restriction on the broad research target. Checks must include exact center and moment certificates, independent degree4 and higher Taylor residuals, manufactured fitting recovery, real finite-difference derivatives, actual primitive differentiation, an independent full-plane inverse and sampling outside the fit domain. Those numerical controls are not an existence proof.

Dependencies: the fully stated tail formulas and rank proof of130, local Taylor calculation of132, smooth Taylor algebra and whole-plane relative inverse uniqueness. None of these finite-constraint constructions provides a decisive B2 endpoint.

Written UTC: 2026-10-21T06:11:58.215349+00:00
