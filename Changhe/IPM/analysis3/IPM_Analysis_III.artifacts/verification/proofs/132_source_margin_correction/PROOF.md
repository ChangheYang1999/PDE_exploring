# The slow-direction source margin at order 41/20

## Statement

Let A, mu and g be the exact source coefficients of the normalized modal trial at its positive source point, as enclosed by the whole source interval in proof 15. Thus the frozen operator, in centered Cartesian coordinates, is

 L=A x partial_x+mu y partial_y-1-g M,
 Mhat(xi,eta)=xi^2/(xi^2+eta^2),
 b=1+(A+mu)/2.

Give L the maximal domain in ordinary isotropic H^s(R^2), with s=41/20. The sharp constant in the negative real energy estimate

 -Re <Lh,h>_Hs >= d_s ||h||_Hs^2

is

 d_s=min(b-s mu,b+g-s A)=b-s mu.

The independently certified interval for this constant, and for the other endpoint, is computed by exact rational interval arithmetic in evidence/check.json. In particular d_s is between4.5253 and4.5255. The fast endpoint is between15.5157 and15.5161. A joint margin of14.8 at this order is false. Positivity of the joint margin, the admissibility of order41/20, and the source regularization window below the fast threshold are unaffected.

For the less precise rectangular box 10<=A<=51/5, 99/100<=mu<=101/100, 29<=g<=30, valid uniform lower bounds are

 b-s mu >= 8869/2000=4.4345,
 b+g-s A >= 2937/200=14.685.

Their minimum is4.4345, not14.685.

## Energy calculation

Put F=(1+xi^2+eta^2)^(s/2) hhat. The exact Fourier calculation in proof 08 gives

 -Re <Lh,h>_Hs
 = integral [b+g xi^2/(xi^2+eta^2)
             -s(A xi^2+mu eta^2)/(1+xi^2+eta^2)] |F|^2.

Since s>=0 and A>=mu>0, this integrand is bounded below by

 (b-s mu)(1-m)+(b+g-s A)m,
 m=xi^2/(xi^2+eta^2).

The difference between its two endpoints is g-s(A-mu). The whole-source certificate gives a strictly positive lower bound for this difference. Hence the slow endpoint b-s mu is the smaller one. Formulae remain valid on the maximal domain by the logarithmic-frequency core argument in proof 08.

## Sharpness and the claimed larger constant

Choose a nonzero real smooth compactly supported function phi, even in both coordinates. Let h_N(x,y)=phi(x,y)sin(Ny). These functions are even in x and odd in y and belong to the maximal domain. Their Fourier transforms concentrate, after H^s normalization, at the two frequency directions (0,1) and (0,-1), with frequency tending to infinity. More explicitly each term is a translate of the Schwartz function phihat, and dominated convergence after division by N^(2s) gives

 -Re <Lh_N,h_N>_Hs / ||h_N||_Hs^2 -> b-s mu.

The two translated terms have vanishing cross products by Schwartz decay. Thus no larger energy constant holds even on the required parity class. The example is a failure of the number14.8 as an all-direction energy constant. It is not a failure of an inverse or of the positive source estimate.

## Exact arithmetic and dependencies

Write certified endpoint intervals as A in[A0,A1], mu in[mu0,mu1], g in[g0,g1]. Since1/2-s=-31/20, rational interval propagation gives

 d_s in[1+A0/2-(31/20)mu1, 1+A1/2-(31/20)mu0],
 d_fast in[1+g0+mu0/2-(31/20)A1, 1+g1+mu1/2-(31/20)A0],
 g-s(A-mu) >= g0-s(A1-mu0).

No endpoint-only source evaluation is substituted for the whole source interval. The source certificate is independently established in proof 15 from the read-only original, and its hash is recorded again here. This result corrects the number in remark5 and item4 of the theory author's H3 draft as read at09:21Z on2026-10-28. It does not prove the variable-coefficient H3 assembly.
