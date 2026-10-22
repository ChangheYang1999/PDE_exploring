# Audit of the trial flow certificate

Date: 2026-10-20. Status: OPEN. This is topic69. This record states the identities and the conditions needed to accept the revised finite-cell and tail implementation. It does not yet accept its complete output. The explicitly reconstructed modal trial, with c_l=1/k, is the object. Its exact normalization and canonical velocity are the subjects of the modal-repair and modal-Green topics.

## Statement and scope

Put V=c_l X+U, U=(-psi_y,psi_x), r=|X|, and work on the first quadrant with continuous axis limits. Write psi=sum_(n=1)^N psi_n(r) sin(2n theta), N=261. Define s=X.V/r², v1=V1/x, v2=V2/y. The conic transport rate uses a=129/20,b=307/100,gamma=1129/1000,Rm=6,p=4,S=a+b and mu=gamma+(S-gamma)/(1+(r/Rm)^p). Let T0=-(1+c_l)+a(v1-s)+b(v2-s)+mu s.

The implementation tests the box with the EXACT binary64 dyadics x1=float(4.8),x2=float(6.82),y2=float(2.85), interpreted as rational numbers, not the corresponding decimal rationals. Call this closed box B. Both on-box and off-box statements must use this same B. Its width is slightly larger than the rational2.02. A box-cost calculation must include that difference. The exact rational interpretation avoids an unsupported transfer of the off-box bound across thin boundary strips.

Conditional target: if the completed numerical certificate and full coverage pass, it gives lower bounds for v2 on the quadrant, for s where r>=20, axis signs apart from the independently certified exact crossing cell, and upper bounds T0 on/off B and V1 on B. Those feed only the transport results in ../global_flow and ../box_transport. They do not invert the nonlocal linearization or prove profile existence.

## Exact polar and angular identities

Polar differentiation gives U_r=-r^-1 psi_theta and U_theta=psi_r. Hence

 s=c_l-sum P_n cos(2n theta),
 v2=s+sum R_n C_n(theta), v1=s-sum R_n S_n(theta),
 P_n=2n psi_n/r², R_n=psi_r,n/r,
 C_n=cos(theta)sin(2n theta)/sin(theta),
 S_n=sin(theta)sin(2n theta)/cos(theta).

The quotients have finite polynomial extensions to the closed quadrant. Multiplying the geometric series in exp(i theta), or telescoping sine addition, gives

 C_n=2cos(theta)sum_(j=0)^(n-1)cos((2j+1)theta),
 S_n=2sin(theta)sum_(j=0)^(n-1)(-1)^(n-1-j)sin((2j+1)theta).

In particular C_n(0)=2n,S_n(0)=0,C_n(pi/2)=0,S_n(pi/2)=2n(-1)^(n-1). The sign in the last formula is essential. The product rule and the exact sums of odd powers give

 ||C_n'''||,||S_n'''|| <= 4n^4+8n^3+4n² <= 2n+6n²+8n³+4n^4.

Also ||partial_theta³ cos(2n theta)||<=8n³. Taylor expansion to degree2 about the exact cell center therefore has remainder bounded by the corresponding constant times d³/6. Ball coefficients enclose the coefficients at that center; the half-width d is rounded upward.

For q(eta)=q0+q1 eta+q2 eta², |eta|<=d, the three Bernstein coefficients on that interval are q0-q1d+q2d², q0-q2d², q0+q1d+q2d². Substituting eta=d(2z-1) and expanding in (1-z)²,2z(1-z),z² proves this identity. All basis functions are nonnegative and sum to1. Each coefficient is still a radial polynomial. A second Bernstein conversion after exact polynomial translation bounds the tensor polynomial. Separate radial and angular truncation remainders must be added.

## Radial models and tail algebra

Write A_n=r^-2n integral_0^r u^(2n+1)f_n(u)du and B_n=r^2n integral_r^infinity u^(1-2n)f_n(u)du. Then in t=log r,

 A_n'=-2n A_n+exp(2t)f_n(exp t),
 B_n'= 2n B_n-exp(2t)f_n(exp t),
 psi_n=(A_n+B_n)/(4n), psi_r,n=(B_n-A_n)/(2r).

These follow directly by Leibniz differentiation and give the code's P,R formulas. On a closed cell, Taylor's integral remainder and bounds for derivatives of the polynomial-exponential forcing give complete radial enclosures. The code's e^x<=1+x+x² bound is valid for0<=x<=1: sum_(j>=2)x^j/j!<=x²(e-2)<x², using e<3 from its positive series. The required2Nh<=1 is an explicit assertion.

A normalized exterior particular term is exp(alpha tau)tau^j. Its absolute majorant decreases for tau>=T if alpha<0 and j/T<=-alpha. An exterior homogeneous A transient decreases after division by r². At the inner endpoint write x=-tau>=T. Each term x^j exp(-alpha x) decreases if alpha>0 and j/T<=alpha. The n=1 B transient is the constant strain c; higher n transients decrease as r tends to0. Near resonance, the integral expansion remainder is bounded by |mu|x exp(|mu|x) times the integral of the absolute forcing polynomial. Its normalized majorants decrease under the two inequalities checked in the implementation.

With Ds=sum2n|psi_n|/r² and Dv=sum2n|psi_r,n|/r, the exterior bounds |s-c_l|<=Ds and |v_i-c_l|<=Ds+Dv follow from |C_n|,|S_n|<=2n. Since gamma<=mu<=S and mu decreases, a valid outer rate bound is -(1+c_l)+mu(T)c_l+mu(T)Ds+S Dv. The implementation's larger bound replaces mu(T)Ds by(2S-mu(T))Ds; it is conservative. This proof requires S>=mu(T)>=0, c_l>0, and monotone majorants.

For the inner tail, write v1=c_l-c+e1,v2=c_l+c+e2,s=c_l-c cos(2theta)+es with all errors bounded by D. Then

 T0 <= -(1+c_l)+a(c_l-c+D)+b(c_l+c+D)
       +max(0,(mu(r_T)-S)(c_l-|c|-D)).

Indeed T0=-(1+c_l)+a v1+b v2+(mu-S)s, mu-S lies between mu(r_T)-S and0, and s>=c_l-|c|-D. This proves the stated upper bound for either sign of that lower bound.

## Coverage, arithmetic and remaining obligations

Adjacent finite cells and the infinite tails must meet at the same exact log endpoints. Rounded printed radii are outer hulls, not substitutes for the actual polynomial domain; topic64 established that distinction. The tail formulas, evaluated with endpoint balls and the coherent canonical moments at those endpoints, apply from the shared actual endpoint. Their weaker statements r>=R_T_hi and r<=r_T_lo alone would leave a possible tiny gap unless finite coverage were separately enlarged. The exact shared endpoint argument must be checked against the data generator.

For r>=20, every cell whose upper radius reaches20 must be included; filtering only r_lo>=20 misses the crossing cell. cert_flow.py's glob uses the conservative first rule; flow_summary.py uses the insufficient second rule. A final aggregate must use the first rule.

Raw middle aggregate extrema are exact binary64 bounds. They give safe decimal statements Tin<=1.2780, Tout<=-0.2399,V1<=-12.834,v2>=0.98845,s_far>=3.4957, and above-source-axis v1>=0.0077249, subject to certificate acceptance. Printed1.2779,-0.2400 and0.007725 are unsafe in their respective directions. Exact rational comparison proves these rounding objections; they do not prove the true extrema violate those tighter numbers.

OPEN: complete source arithmetic, source/input provenance, exact coverage, remaining outer/inner cells, tail recomputation, and a final independently reviewed verdict. The assertions here do not upgrade a partial certificate to a global bound.

## Independent scalar and geometry checks planned before execution

The middle partition is reconstructed from the exact rational parent endpoints and integer subdivision counts in the already audited partition_exact.json. Every exported boundary ball must contain its assigned exact point. Direct Arb exponential enclosures at both exact endpoints check the printed radius hulls; this verifies the hull direction without relying on the floating expression1+h+h². It does not extend the Taylor domain to the entire printed hull. The source's exact2Nh<=1 guard is checked separately on every rounded h_up.

For the box-cost instance use C=exp((Tin+kappa)(x2-x1)/v)/kappa with Tin=639/500,v=6417/500,kappa=1/5 or11/50 and the dyadic width. This formula is the conditional transport bound of ../box_transport/PROOF.md. Compare an Arb exponential with a positive interval Taylor series. For0<=z<=zmax and N+2>zmax, the omitted exponential series is at most [zmax^(N+1)/(N+1)!]/[1-zmax/(N+2)]; successive positive omitted terms have ratio at most zmax/(N+2). This supplies an independent enclosure rather than agreement of rounded decimals.

## Exact finite modal-map audit

The first source review raised three arithmetic objections, but its follow-up withdrew them as whole-map counterexamples. Its replacement proof contains unquantified second-order rounding terms and is not accepted as a universal proof. A finite-data audit can instead check the exact image of each actual input box. At fixed polynomial degree q, write missing a_m as zero. The independent closed modal map is

 R_0=(2a_0-a_2)/8,
 R_1=(2a_0+a_1-a_2-a_3)/8,
 R_j=(a_(j-1)+a_j-a_(j+1)-a_(j+2))/8 for j>=2.

These follow by expanding cos²(theta)sin(theta)cos(2m theta) into sine frequencies. The first source accumulator contains five terms, of which the first two are an exact doubling; its 'four terms' comment is inaccurate. For exponent alpha,

 dR_(q,j)=(alpha+3)R_(q,j)+(q+1)R_(q+1,j),
 F_(q,n)=((alpha+4-2n)R_(q,n-1)+(alpha+4+2n)R_(q,n)
          +(q+1)(R_(q+1,n-1)+R_(q+1,n)))/2.

Thus each output is a sparse rational linear functional of the independent T input intervals when alpha is fixed. The exact output hull is sum w_i m_i +/- sum |w_i|r_i, with every binary64 input interpreted as its exact dyadic value. Correlations between occurrences of one T entry are retained by combining their weights before taking absolute values. If alpha is itself an interval, extrema of this multiaffine expression occur at its two endpoints; take the hull of the two fixed-alpha images. Compare these exact rational bounds with the exact binary64 output midpoint plus or minus radius. This proves containment for every point of each audited input box, without assuming the source map has a valid universal contract. Finite stress tests of other input boxes are diagnostics, not a proof for all floating inputs. The actual-data audit must state precisely which cells, regions, exponents and source hashes it covers.

For middle cells alpha=0 and every combined modal-map coefficient is an integer divided by16. Every finite binary64 value is an exact integer times eta=2^(-1074). Thus the same box-image calculation can use signed integers only: scale all input midpoints and radii by2^1074, all modal weights by16, and compare the resulting endpoint integers with16 times the scaled output midpoint plus or minus radius. There is no numerical rounding in this check. This provides a different implementation from rational sparse-map evaluation and makes exhaustive validation feasible. The integer method applies only to the alpha=0 middle case unless its weight denominator is explicitly enlarged.
