# The first two source moments of a decaying solenoidal field

Status: proved conditional identities for exact fields. No numerical source table is assumed to satisfy these identities exactly.

## Statement and notation

Let U belong to C²(R³;R³), with div U=0. Let |U| be the Euclidean norm and |DU| the Frobenius norm, with (DU)ij=∂j Ui. Suppose there are constants C0,C1>0 and β>1 such that, for every x in R³,

|U(x)| ≤ C0(1+|x|)^(-β),
|DU(x)| ≤ C1(1+|x|)^(-β-1).

Define f=tr((DU)²). Then f and xk f are absolutely integrable for k=1,2,3, and

∫R³ f(x) dx=0,
∫R³ xk f(x) dx=0  for k=1,2,3.

The first identity alone requires only β>1/2 under the same bounds.

Suppose additionally that V belongs to C²(R³;R³), div V=0, and satisfies the same two bounds with constants C0',C1' and the same β>1. Define fp=2tr(DU DV). Then

∫R³ fp(x) dx=0,
∫R³ xk fp(x) dx=0  for k=1,2,3.

Here V may be the parameter derivative Up of a differentiable solenoidal family, provided the stated regularity and decay hold. No Euler momentum equation is assumed.

## Proof of the source identities

Write the components of the quadratic tensor B as Bij=Ui Uj. Twice differentiating and using div U=0 gives

∑i,j ∂i∂j(Ui Uj)
=∑i,j ∂i(Uj ∂j Ui)
=∑i,j (∂i Uj)(∂j Ui)
=tr((DU)²)=f.

The term ∑j Uj∂j(div U) vanishes since U is C². Put A_i=∑j ∂j Bij=∑j Uj∂j Ui, so f=div A. The pointwise bounds imply

|f| ≤ |DU|² ≤ C1²(1+|x|)^(-2β-2),
|A| ≤ |U||DU| ≤ C0 C1(1+|x|)^(-2β-1).

The first source bound proves absolute integrability of f for β>1/2 and of xk f for β>1. In the ball BR of radius R, the divergence theorem gives

∫BR f dx=∫∂BR A·n dS.

The absolute value of the boundary integral is at most

4π C0 C1 R²(1+R)^(-2β-1),

which tends to zero when β>1/2. Passing to the limit proves the zeroth moment.

For the first moment, integration by parts twice gives

∫BR xk f dx
=∫∂BR xk A·n dS - ∫BR A_k dx
=∫∂BR xk A·n dS - ∫∂BR Uk(U·n) dS.

The two absolute boundary bounds are respectively

4π C0 C1 R³(1+R)^(-2β-1),
4π C0² R²(1+R)^(-2β).

Both tend to zero for β>1. Absolute convergence permits the limit R→∞, proving all three first moments.

For the mixed source, set Bp,ij=Vi Uj+Ui Vj. Because both fields are solenoidal, the same component calculation gives

∑i,j ∂i∂j Bp,ij=2tr(DU DV)=fp.

Its single divergence is Ap=DV U+DU V. Thus

|fp| ≤ 2 C1 C1'(1+|x|)^(-2β-2),
|Ap| ≤ (C0 C1'+C0' C1)(1+|x|)^(-2β-1),
|Bp n| ≤ 2 C0 C0'(1+|x|)^(-2β).

The preceding boundary argument applies verbatim with these constants. This proves both mixed-source moment identities without interchanging a parameter derivative and an infinite integral.

## Consequence for radial Newton integrals

Use orthonormal spherical harmonics Y_lm and coefficients

f_lm(s)=∫S² f(sn) conjugate(Y_lm(n)) dS(n).

For ell=0,1, the solid harmonic s^ell Y_lm(n) is a constant or linear function. The identities above therefore imply the absolutely convergent radial moments

M_lm=∫0^∞ s^(ell+2) f_lm(s) ds=0,  ell=0,1.

For r>0 the usual decaying Newton coefficient is

P_lm(r)=[r^(-ell-1)∫0^r s^(ell+2)f_lm(s)ds
          +r^ell∫r^∞ s^(1-ell)f_lm(s)ds]/(2ell+1).

This formula and its uniqueness convention are proved in ../pressure_consistency/PROOF.md. Substituting M_lm=0, for ell=0,1 only, gives the exactly equal exterior-only formula

P_lm(r)=[-r^(-ell-1)∫r^∞ s^(ell+2)f_lm(s)ds
          +r^ell∫r^∞ s^(1-ell)f_lm(s)ds]/(2ell+1).

Differentiation in r cancels the two source endpoint terms and yields

P_lm'(r)=[(ell+1)r^(-ell-2)∫r^∞ s^(ell+2)f_lm(s)ds
           +ell r^(ell-1)∫r^∞ s^(1-ell)f_lm(s)ds]/(2ell+1).

The same formulas hold with f replaced by fp. These formulas impose neither a finite-radius pressure condition nor a freely chosen harmonic correction: their equality follows from the exact whole-space source moments. Their numerical use must still be checked against the unmodified integrals and increasing quadrature.

## Relation to this campaign and limits

The campaign has 2/5<c_l<1/2, so its leading exponent α=(1-c_l)/c_l is greater than one. For a parameter family whose spatial derivatives have the asserted r^(-α-j) tails up to logarithmic factors, any β strictly between one and the minimum local α gives the bounds needed here. Uniform control of that represented family, including its correction channels, remains a hypothesis unless verified separately. A finite coefficient file alone is not a proof of these bounds.

The identities apply to the exact differentiable velocity. A supplied Jacobian that is inconsistent with that velocity need not generate a source with these moments. Angular truncation, radial quadrature, and cancellation can also produce nonzero discrete moments. Such defects must be retained as diagnostics. Setting a computed moment to zero is a justified evaluation strategy only when the underlying exact-field hypotheses hold; it is not evidence that the unmodified source was accurate.

No ell≥2 moment is asserted. In particular, the given bounds need not make a second spatial moment absolutely integrable when β≤3/2. No claim about existence, nonexistence or approximation of a rotating Euler profile follows from these source identities.
