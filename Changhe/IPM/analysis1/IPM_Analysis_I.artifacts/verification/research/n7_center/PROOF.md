# N7 center regularity and its first nonpolynomial residual term

## Statement and scope

Write X=(x,y)=r(cos(theta),sin(theta)), t_-=the first stored knot, r_-=exp(t_-), M=260. The radius is defined by the knot, not by the separately stored floating approximation called rmin. Interpret all stored binary64 coefficients as exact rationals. On 0<r<r_- define

phi(X)=1+sum_{m=0}^{259}sum_{j=1}^{7} D[m,j-1](r/r_-)^{2j} cos(2m theta)
       +(r/r_-)^b sum_{m=0}^{259}sum_{i=0}^{6} E[m,i] log(r/r_-)^i cos(2m theta),
rho(X)=x^2 y phi(X).

The coefficients E are any finite real numbers. In particular this covers both the stored floating corrections and the exact corrections obtained from the triangular C^6 join equations. Assume b>49, D[m,j-1]=0 when 1<=j<=4 and m>j, and D[259,4] != 0. The exact data check below tests these hypotheses for data/trial_n7.npz without executing the producer.

Then phi has a C^9 extension across 0 and no C^10 extension; rho has a C^12 extension and no C^13 extension. The density is a polynomial through degree 11, followed by homogeneous terms of degrees 13,15,17 and a higher-order logarithmic remainder. Its first nonpolynomial homogeneous term has degree 13. These are local statements on a ball of radius strictly smaller than r_-. They do not assert C^8 or higher regularity across spline joins.

For the residual assertion additionally assume a global completion of this finite angular representation with the canonical regular inverse -Delta psi=partial_x rho, U=(-partial_y psi,partial_x psi), and exact normalization sigma=partial_xy psi(0)=3c_l-1, c_l=1/k, 0<k<1. Set V=c_l X+U and F=V dot grad rho-rho. Then F is C^12 but not C^13 at the center. Its first nonpolynomial homogeneity is exactly 13. If L=2*259+3=521, the coefficient of r^13 sin((L+2)theta) in that degree-13 residual is

  (2-6/k)(13-L) D[259,4] / (32 r_-^10).                 (1)

This coefficient is nonzero. No new global normalization certificate, inverse estimate, residual norm enclosure, trial-to-X3 placement, or decisive endpoint is asserted. The residual conclusion is conditional on the stated canonical normalization; the density conclusion is an exact conclusion about the inspected D and b.

## Homogeneous regularity lemma

For a smooth angular function f and positive integer d, H=r^d f(theta) on the punctured plane has derivatives of every order l bounded by C_l r^{d-l}. Extend H(0)=0. Inductively its derivatives of order l<d extend continuously with value zero: the next directional derivative at zero of a derivative of order l<d-1 is zero by the bound C r^{d-l}; the same bound proves continuity. Thus H is C^{d-1}. If H were C^d, Taylor's theorem at zero, applied to lambda X and divided by lambda^d, would show H(X) equals its degree-d homogeneous Taylor polynomial. Conversely a homogeneous polynomial is smooth. Hence H is C^d exactly when it is a homogeneous polynomial. The same derivative estimates show r^alpha log(r)^i f(theta) is C^n with zero jets through n whenever alpha>n. All sums here are finite, so no angular summability claim is needed.

A homogeneous polynomial of degree d restricted to the unit circle has frequencies at most d. Also

  r^{2j} cos(2m theta)=(x^2+y^2)^{j-m} Re((x+iy)^{2m})

is polynomial when m<=j. Consequently all j<=4 terms of phi are polynomials of degree at most 8. Terms j>=5 are homogeneous of degree at least 10, so phi is C^9. Its degree-10 part has nonzero frequency 518 from D[259,4]/r_-^10. No lower m contributes that frequency, and 518>10; it is not a polynomial. Terms of degree 12,14 and the b>49 remainder are o(r^10) with the required lower derivative bounds. Taylor rescaling therefore rules out C^10 for phi.

Since x^2 y=r^3(sin(theta)+sin(3theta))/4, the degree-13 part H of rho has highest angular frequency L=521 and its coefficient is D[259,4]/(8r_-^10). Lower modes cannot contribute frequency 521: their maxima are 2m+3<=519. This coefficient is nonzero and L>13. The degree-15 and degree-17 terms and the r^{b+3} logarithmic remainder are C^12 and o(r^13). The lemma proves rho is C^12, and Taylor rescaling proves it is not C^13. The degree-13 part can contain additional polynomial terms; those do not change the conclusion.

## Local form of the canonical velocity

This paragraph justifies why a remote completion cannot cancel the high angular frequency in (1). For a separated mode one has

  Delta[r^a sin(l theta)] = (a^2-l^2) r^{a-2} sin(l theta).

Differentiating this identity in a treats every logarithmic power. If a=l>0, a particular solution of r^{l-2} sin(l theta) is r^l log(r) sin(l theta)/(2l). For the equation with -Delta the particular solution has the opposite sign. Iteration solves any finite logarithmic polynomial; at a!=l the triangular coefficient system has nonzero diagonal a^2-l^2. The forcing partial_x rho has only finitely many even, positive angular frequencies because rho is even in x and odd in y. There is no zero mode. The homogeneous solutions of each radial equation are r^l and r^{-l}; the canonical regular branch excludes r^{-l}. A difference between two regular global completions near 0 is therefore a finite sum of regular harmonic polynomials r^l sin(l theta).

Every polynomial density term of degree d gives a polynomial forcing of degree d-1. Its frequencies are <=d-1, whereas a=d+1 for the Poisson solution, so no resonance occurs. Its particular stream function is polynomial of degree d+1 and its velocity is polynomial of degree d. The nonpolynomial degree-13 density gives a degree-12 forcing. Its particular stream function has degree 14, with at most one logarithm, and its velocity has degree 13, with at most one logarithm. Terms of degree 15,17 and b+3 give no lower orders. Thus U is a polynomial near 0 through degree 11 plus a remainder whose derivatives of order l are O(r^{13-l}(1+|log r|)^K); polynomial terms of higher degree may be retained in this remainder. Here K is a finite integer. The harmonic polynomial terms of degree below 13 are all included in the polynomial part. This argument uses only the local radial equation and regularity of the selected inverse, not a pseudolocal approximation.

Symmetry and the leading cubic density imply U has no constant term and has linear part (-sigma x,sigma y). Indeed the only degree-2 regular harmonic stream function consistent with the two odd symmetries is sigma xy; all particular stream functions start at degree 4. Exact normalization then gives

  DV(0)=diag(c_l-sigma,c_l+sigma)=diag(1-2c_l,4c_l-1).

## First nonpolynomial residual term

Write rho=P+H+R, where P is the polynomial of degrees 3 through 11, H is homogeneous of degree 13, and R and its derivatives of order l<=13 are O(r^{15-l}(1+|log r|)^6). Write V=V_1+V_pol,>=3+V_rem, with V_1=diag(lambda_x,lambda_y)X and V_rem of degree at least 13 with logarithms as above. Products of polynomial pieces give polynomials. Multiplying V_pol,>=3 by grad H has degree at least 15. Multiplying V_rem by grad P has degree at least 15, since P starts at degree 3. All terms involving R also have degree at least 15. It follows that the degree-13 part of F, modulo a polynomial of degree 13, is (V_1 dot grad-1)H.

For every d,L, direct polar differentiation gives

  (x partial_x-y partial_y)[r^d sin(L theta)]
    =r^d[(d-L)sin((L+2)theta)+(d+L)sin((L-2)theta)]/2.

Now V_1 dot grad=(lambda_x+lambda_y)r partial_r/2
 +(lambda_x-lambda_y)(x partial_x-y partial_y)/2, and lambda_x-lambda_y=2-6/k. Only H's highest frequency L can generate L+2. Its coefficient is therefore (1). Since 0<k<1, 2-6/k<0, and 13-L<0. The exact nonzero D implies a nonzero coefficient of frequency 523>13. No polynomial background can cancel it. All remaining nonpolynomial terms are of order at least 15 with finite logarithmic powers; their derivatives through order 12 extend continuously and they are o(r^13). The homogeneous lemma and Taylor rescaling prove the residual assertion.

## Exact data and arithmetic obligations

The producer claims to zero the mask {(m,j):1<=j<=4, j<m<260}. Its size is sum_{j=1}^4(259-j)=1026. Compare every exact D in the original and repaired files, not just a printed maximum. Test the mask and the unchanged complement, the highest nonzero mode, b>49 and 0<k<1. Test the now-vanishing degree-5 angular coefficient (D[2,0]+D[3,0]-D[4,0]-D[5,0])/8. Reconstruct the join matrix J[nu,i]=nu!/(nu-i)! b^{nu-i} for i<=nu, whose diagonal i! is nonzero. This establishes uniqueness and finiteness of the exact correction coefficients for finite spline jets; it does not certify the stored floating E satisfies the joins.

The input JSON contains exact rational D, b, k, t_- and SHA256 hashes of both full NPZ files. A second program must parse the NPY member headers and binary64 bytes independently using zipfile, ast.literal_eval and struct, and compare every rational input. It must not import producer modules or the primary checker. Primary Arb512 and mpmath.iv180 must enclose the physical coefficient (1), with an independent higher-precision formula. The small maximum of the scaled D[:,4] is not a bound for either the coefficient of r^13 in rho or the residual coefficient (1), because these contain r_-^{-10} and additional angular factors.

For the proposed numerical threshold a=6.45, s=3.07, the homogeneity inequality is 13>a+s-1=8.52 with margin 4.48. Checking this inequality only verifies the power threshold cited in the proposed class; it does not establish membership in that class or any global graph domain. No far-field or join condition is inferred from a center calculation.

## Dependencies and status

The representation and exactification convention are frozen from numerics' make_n7.py, modal_fit.py and cert_green.py in evidence/source. All analytic identities above are proved here. The exact input data are evidence/exact_inputs.json. This proof is written before the verification code. Final numerical and review status will be recorded in evidence/verdict.json; until then the actual-data arithmetic obligations are OPEN.
