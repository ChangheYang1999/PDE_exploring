# Positive smoothing for the finite-regularity energy symbols

## Statement

Let C=R times S1 with its flat cylinder coordinates. Use left quantization, with any fixed smooth convention at frequency zero and the periodic quantization in the angular variable. Suppose a(X,xi) is a real symbol, smooth in xi and C^3 in X, and for every multi-index beta and |alpha|<=3,

 |partial_X^alpha partial_xi^beta a(X,xi)|
                       <=C_(alpha,beta)<xi>^(m-|beta|),              (1)

uniformly on C, where 0<=m<=1/8. Assume a>=0. Then

 Re <Op(a)w,w>>=-C ||w||_(H^(-1/32))^2,                            (2)

initially for smooth compactly supported cylinder functions, and by continuity whenever the quadratic form is defined. If m=0 and a>=mu for a constant mu, then

 Re <Op(a)w,w>>=mu ||w||_2^2-C ||w||_(H^(-1/32))^2.                 (3)

The constants use finitely many of the seminorms in (1). They are uniform under translation in t. Neither compact support nor integrability of the coefficients in t is required.

Consequently the actual order-zero symbols G_v,G_u of proof 142 obey (3), after smooth extension of the cofactor symbol from a slightly larger vertical sector. The actual nonnegative symbol

 (W.grad s)log<xi>

obeys (2), since it satisfies (1) with m=1/8. Thus the positivity steps Q3 and Q4 of the theory author's work/Hs.md require no unproved infinite regularity of the actual coefficients. This theorem alone does not prove the transport conjugation or H3.

## Two classical analytic inputs

We use the ordinary smooth-symbol sharp Garding theorem in its explicit form: if b>=0 is a scalar symbol in S^m_(1,d), 0<=d<1, then

 Re <Op(b)w,w>>=-C ||w||_(H^((m-1+d)/2))^2.                         (4)

This is the sharp Garding theorem for the (1,d) calculus, as in the sharp-inequality part of Section18.6 of L. Hormander, The Analysis of Linear Partial Differential Operators III. The real left form and the Weyl form differ by order m-1+d, so the same estimate applies to both. Its construction uses a positive Friedrichs quantization: average with even wave packets of frequency width <xi>^((1+d)/2) and spatial width <xi>^(-(1+d)/2). Positivity is exact before comparing quantizations. The first moments vanish. The second frequency and spatial Taylor terms both have order m-1+d, since their factors are respectively <xi>^(1+d)<xi>^(m-2) and <xi>^(-1-d)<xi>^(m+2d). Symbol differentiation preserves these orders; the L2 bound after conjugation by the indicated Bessel powers yields (4). We only apply this smooth theorem after the following positive smoothing.

For a finite-regularity remainder we use David Lannes, Sharp Estimates for Pseudo-Differential Operators with Symbols of Limited Smoothness and Commutators, arXiv:math/0508465, Theorem1, first estimate, printed page20 of the retained PDF. For a symbol r in Gamma^l_(s0), with d_space/2<t0<=s0 and -t0<v<t0, that estimate is

 ||Op(r)u||_(H^v)<=C ||u||_(H^(v+l)),                               (5)

with the coefficient norms n_(0,t0)+N_(2[d_space/2]+2,t0). Here d_space=2. We take t0=3/2, s0=2 and v=1/32. The source PDF and extracted text are retained in references/finite_regularity. On bounded patches uniform C^2 coefficient bounds imply the required H^2 bounds. The globalization for uniformly local coefficients is checked below.

## Smoothing that preserves the sign

Choose a nonnegative smooth compactly supported function J on R^2 with integral1, and periodize it in the angular coordinate. Put d=1/2, e(xi)=<xi>^(-1/2), and

 a_sharp(X,xi)=integral J(Y) a(X-e(xi)Y,xi) dY.                    (6)

Then a_sharp>=0, exactly. No subtraction or Fourier cutoff is used to obtain this positivity. Differentiation of (6), transferring any excess X derivatives to the smooth kernel, proves

 a_sharp in S^m_(1,1/2).                                          (7)

For example, each X derivative costs at most e^(-1)=<xi>^(1/2), and each xi derivative costs <xi>^(-1); derivatives of e times a transferred X derivative have this same cost. The estimate (1) is more than sufficient, since smoothness of the convolution kernel supplies every higher X derivative required in the smooth symbol class.

Apply (4) to (7). Since (m-1+1/2)/2<=-3/16, we obtain

 Re <Op(a_sharp)w,w>>=-C ||w||_(H^(-3/16))^2.                       (8)

## The finite-regularity difference

Let r=a-a_sharp. For |alpha|<=2, apply the fundamental theorem of calculus in (6) to partial_X^alpha a. Its third X derivatives are bounded by (1). Thus

 |partial_X^alpha r(X,xi)|<=C <xi>^(m-1/2).

Differentiating in xi any fixed number of times gives

 |partial_X^alpha partial_xi^beta r(X,xi)|
             <=C_(alpha,beta)<xi>^(m-1/2-|beta|), |alpha|<=2.      (9)

Indeed a derivative falling on e contributes e/<xi> and one spatial derivative; use integration by parts in Y if another spatial derivative would exceed those available. Equivalently differentiate the scaled convolution kernel first: its integral is zero for positive parameter derivatives, and subtract the value of partial_X^alpha partial_xi^gamma a at X before estimating. The Lipschitz bound in X then supplies the same factor e. This argument uses only the three X derivatives in (1), not a derivative for every beta.

On a bounded coordinate patch, (9) puts r in Gamma^(m-1/2)_2. By (5),

 ||Op(r)w||_(H^(1/32))<=C ||w||_(H^(1/32+m-1/2)).                  (10)

Since 1/32+m-1/2<=-11/32<-1/32, the right side is bounded by C||w||_(H^(-1/32)). Duality gives

 |<Op(r)w,w>|<=C ||w||_(H^(-1/32))^2.                              (11)

Combining (8) and (11), and H^(-1/32) continuously embedded in H^(-3/16), proves (2). Apply the result to a-mu when m=0 to obtain (3).

## Uniform cylinder globalization

Take a smooth partition of unity in t with bounded overlap, supported on intervals of fixed size, and finitely many angular charts. Use a second partition equal to one on a fixed enlargement of each support. The localized symbols satisfy (9) in H^2 with the same constant on every chart. The input and output cutoffs produce bounded multipliers on the Sobolev orders in (10).

The kernels from pairs of nonoverlapping enlarged charts are smoothing of every frequency order needed here. To verify uniform summability, integrate by parts in xi in the oscillatory kernel. Since (9) supplies every required xi derivative, the kernel and its X derivatives up to2 are bounded by C_M(1+dist(X,Y))^(-M) when the charts are separated. Choose M greater than the dimension plus4; the row and column sums over the fixed-size t intervals converge. Apply the local estimate (10) to the neighboring pairs and the kernel estimate to the remaining pairs. This proves (10)-(11) on the whole cylinder. The usual localization proof of the smooth theorem (4) gives the same uniform globalization for (8). There are no constants growing with the location of a chart.

The angular coordinate can instead be treated by the toroidal quantization directly. Periodization of the kernels in a finite angular atlas gives the same operator and bounds, up to lower-order smooth coordinate terms already covered by (10). The frequency-zero convention changes an operator with bounded frequency support and uniformly C^2 coefficients; the same estimate covers it.

## Application to the actual symbols

The actual W and scalar transport coefficients are W^(7,infinity), hence the entries of DW have at least six bounded weak derivatives. Their representatives are sufficiently classical for the three derivatives in (1). The coupling symbol has normalized coefficient regularity H^(51/8) on a two-dimensional annulus. Sobolev embedding gives C^r for every r<43/8, in particular C^3 with uniform bounds. The same normalized endpoint expansions and finite set of spline joins give these bounds uniformly on the cylinder. The smooth s and Lambda have all bounded derivatives. Products in G_v and G_u consequently satisfy (1) with m=0. The divided angular coefficients at the vertical axis have the stronger uniform regularity already checked in proof 126.

For the sector component, apply proof 142 on a closed sector larger than the support of the cofactor cutoff. Choose a smooth angular cutoff equal to one on a neighborhood of that support and supported strictly inside the larger sector. Blend G_u there with the constant mu outside, using this cutoff. Both entries in the convex combination are at least mu wherever the cutoff is nonzero, so the resulting global symbol is at least mu and agrees with G_u on the required neighborhood. Derivatives of the fixed cutoff preserve (1). Applying (3) globally to this extension is legitimate for localized sector functions; changes outside the larger sector have separated-support kernels, controlled as in the globalization paragraph.

Finally W.grad s>=0, log<xi>>=0, and log<xi> and all its derivatives satisfy symbol estimates of order1/8. Thus (2) applies to the logarithmic term. All these conclusions are form estimates with a strictly lower ordinary Sobolev remainder on the conjugated unknown. Comparing that remainder to the lower X norm is a separate order-reduction assertion, not presumed in this theorem.
