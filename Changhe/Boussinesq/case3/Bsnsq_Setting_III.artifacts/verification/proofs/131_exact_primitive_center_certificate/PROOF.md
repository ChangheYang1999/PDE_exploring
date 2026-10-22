# Exact center certificate for a horizontal-primitive stream

Status: complete elementary certificate argument written before implementation; controls pending. This checks a serialized field, not proximity to any other profile.

Let beta>2 be rational. Let Psi be a finite rational linear combination of the smooth odd basis x R^(1-1/beta-shift) T_i(2R^(-1/beta)-1)T_j(y/R), R=sqrt(1+x^2+y^2), with integer indices i,j and shift in{0,1}. Remove its linear x Taylor monomial, which implements the relative velocity gauge without changing vorticity. Put Omega=-Delta Psi, W=beta X+(-Psi_y,Psi_x), F=W.grad Omega+Omega and Theta=int_0^x F(s,y)ds. Assume the prescribed center identities Psi_xy(0)=1+beta/2 and Omega_x(0)=4a0/beta. This primitive then has Theta=a0x^2+O(r^3).

Expand Psi through total degree8 by the generalized binomial series of R powers and the ordinary Chebyshev recurrence. All coefficients are rational. Apply Cartesian polynomial differentiation to compute Omega, W and F, keeping sufficient degree at each operation. F is odd in x; integrate each monomial c x^i y^j to c x^(i+1)y^j/(i+1). This gives the true Taylor coefficients of Theta through degree6. Apply the thermal operator W.grad Theta-(beta-2)Theta and retain its coefficients through degree4. The calculation uses no prescribed center or tail coefficient formula from the fitting chart.

The truncated coefficients are exact. The discarded stream Taylor remainder and its derivatives have their usual smooth Taylor orders; after at most three derivatives the omitted terms start above degree5, and multiplication by W, which vanishes at0, raises the order again. Integration in x raises it once. Thus discarded terms cannot contribute to a thermal coefficient of degree at most4. The linear stream term is removed before using W, so no hidden constant multiplies a discarded derivative. Generalized-binomial Taylor coefficients are exact for every rational exponent because R is strictly positive near0.

If any thermal coefficient through degree4 is nonzero, the exact serialized field fails the thermal equation on every neighborhood of0. The vorticity equation holds for the exact primitive by definition; a finite numerical quadrature must still be independently differentiated and checked. If every checked coefficient is zero the verdict is OPEN, since higher coefficients and the global equation have not been tested. A tiny nonzero rational coefficient still rejects exact identity but implies no lower bound on the distance to a different profile.

The field coefficients, rational exponent, code and proof are hashed as build inputs. Controls must include an exact polynomial B2 pair, a known nonprofile and direct symbolic differentiation of rational-exponent basis functions. No Lean formalization is claimed or run.

Written UTC: 2026-10-21T05:43:10.748882+00:00
