# An explicit axis-strip constant for the actual remainder weight

## Statement

Fix a=17/4 and w(X)=|x|^(-2a) W(r), W(r)=max(1,r)^(29/4). Let R=L2(w dX) in the even-x, odd-y parity class. Let 0<R0<R1 and choose 0<s0<=R0/2. Define

 I={y:sqrt(3)R0/2<=|y|<=R1},
 K={|x|<=s0, y in I}, Wmax=max(1,R1)^(29/4).

Suppose rho is even in x, odd in y, vanishes to order x^2 at x=0, and has bounded continuous Cartesian derivatives through order five on K. Set

 M20=sup_I |rho_xx(0,y)|,
 M21=sup_I |rho_xxy(0,y)|,
 M40=sup_K |rho_xxxx|,
 M41=sup_K |rho_xxxxy|.

For 0<s<=s0 let h_s=1_(|x|<s) h, h in R. Let U be the canonical IPM velocity. Its axis traces T=U2[h_s](0,y) and T1=partial_x U1[h_s](0,y) mean the bounded extensions of proof 23. Set rho2(y)=rho_xx(0,y)/2 and

 Dvert h_s=U[h_s].grad rho-x^2(2rho2 T1+rho2' T).

For every 0<d<=s with d<=R0/2,

 ||1_(R0<=r<=R1, |x|<d) Dvert h_s||_R
       <= Aax s ||h||_R,                                  (1)

where the fully explicit constant is

 Aax=sqrt(Wmax)[C_a M20+(C_a s0/2)M21
                         +(D_a s0^2/6)M40+(D_a s0^3/24)M41]. (2)

C_a,D_a are the explicit universal strip constants of proof 23. In particular one may use C_a<593 and D_a<612, with exact rational integer upper bounds checked by directed ball arithmetic below. The actual modal rho satisfies the regularity hypotheses on K. Formula (2) reduces its numerical evaluation to four coefficient suprema and the two chosen radii. Their values have not been computed by this note.

This is an output estimate for the vertical-jet-subtracted operator and near-strip input. To bound the radial-jet operator, one must add the radial-versus-vertical lift and the separated input estimates. It is not by itself a global norm or a complement inverse.

## Proof

Since W>=1 globally,

 ||h_s||_(L2(|x|^(-2a)dX)) <= ||h||_R.

Thus h_s is in the strip space of proof 23 on the entire y line; no restriction of the input y coordinate is required. This also gives an unweighted L2 velocity. On the displayed output set, |y|>=sqrt(R0^2-d^2)>=sqrt(3)R0/2 and |y|<=R1, so its vertical Taylor segments lie in K. Also W(r)<=Wmax there.

Parity and Taylor's integral remainder give on K

 rho_x=2x rho2+x^3 r1,    |r1|<=M40/6,
 rho_y=x^2 rho2'+x^4 r2,  |r2|<=M41/24.                   (3)

For the first identity apply third-order Taylor expansion to rho_x: its constant and quadratic coefficients vanish by oddness in x. For the second use fourth-order Taylor expansion of rho_y: its constant term vanishes by the axis hypothesis and its odd coefficients vanish by evenness in x. The remainder constants are 1/3! and 1/4!, respectively. The trace coefficients satisfy 2|rho2|<=M20 and |rho2'|<=M21/2.

Proof 23, applied with strip radius s, gives the unweighted-in-y estimate

 ||Dvert h_s|| <= [C_a s M20+(C_a s^2/2)M21
                  +(D_a s^3/6)M40+(D_a s^4/24)M41]||h_s||.

Here the output can be restricted to y in I because the multiplication coefficients in its proof are only used on that output set. The Fourier strip bounds themselves hold on the whole line, so this restriction does not change their constants. Both input and output are converted from half-strip to full-strip norms by the same factor sqrt(2); it cancels. Restrict further to the desired output set and multiply by sqrt(Wmax). Since s<=s0, divide out s and obtain (1)-(2).

All operations first hold for smooth core inputs supported away from the axis. Density in R after strip truncation, the bounded trace extensions, and the inequality just proved extend the result to every h in R. This verifies the domain, image membership and canonical velocity interpretation.

## Explicit universal constants and sharper local comparisons

The constants used are

 B_a=max((2a+1)^(-1/2), sqrt(Gamma(2a+1)/2^(2a+1))),
 C_a=1+10*2^(a+1/2)+64*(1+1/(9/2-a))
       +2*(1/(a+1/2)+1/(a-1/2)+1/(a-3/2)+1/(a-5/2)),
 D_a=C_a+B_a/sqrt(9-2a).

They have already been proved in proof 23 by explicit Fourier kernels and Schur estimates. The code in this topic independently evaluates their exact expressions at 256 and 384 bits. It checks the proposed integer upper bounds without floating-point rounding of endpoints. There is no quadrature or mode truncation.

If the near-strip input is also restricted to a known radial set B where W>=Wmin>0, replace sqrt(Wmax) in (2) by sqrt(Wmax/Wmin). This follows from the same two norm conversions. For dyadically comparable radial sets it avoids the large absolute Wmax at large radii. Neither this improvement nor subdivision of I changes the Taylor argument.

Dependencies: topics23,48,50 and76. No external weighted singular-integral theorem is used.
