# Exact endpoint expansion of finite radial Chebyshev amplitudes

Status: proved algebraic identity. This does not bound floating-point evaluation errors.

## Statement

Let R>0, q>=0, s=sqrt(q+R^2), x=q/(s+R)^2 and t=2x-1. Fix any integer N>=0 and real coefficients a_0,...,a_N. Let T_k denote the Chebyshev polynomials of the first kind, defined by T_0(t)=1, T_1(t)=t and T_{k+1}(t)=2tT_k(t)-T_{k-1}(t). Define integer polynomials C_k(z)=T_k(1-z), and let c_kj be the coefficient of z^j in C_k. Put b_j=sum_{k=j}^N a_k c_kj and z=4R/(s+R). Then

sum_{k=0}^N a_k T_k(t)=sum_{j=0}^N b_j z^j.

For q>0, both sides and all their q derivatives agree. Equality also extends with all right derivatives at q=0. The identity applies independently to every harmonic column and each finite correction-channel amplitude. Multiplication by a common smooth envelope or damping factor preserves it.

## Proof

The factorization q=(s-R)(s+R) gives x=(s-R)/(s+R), including q=0. Hence 1-t=2(1-x)=4R/(s+R)=z. By definition C_0=1, C_1=1-z and C_{k+1}=2(1-z)C_k-C_{k-1}. Induction proves that C_k has integer coefficients and degree k. Substituting t=1-z into the finite Chebyshev sum and collecting powers gives the stated formula for b_j. All rearrangements are finite. The function q maps to z smoothly on the open interval (-R^2,infinity), so ordinary differentiation proves equality of all derivatives, including at q=0. Multiplication by any common smooth factor preserves equality and its differentiated forms.

## Numerical scope

At large radius, computing z by 4R/(sqrt(q+R^2)+R) avoids subtracting t from one. Evaluating the polynomial in z can also avoid cancellations among the endpoint derivatives of separate T_k terms. Forming b_j exactly from the represented binary coefficients and integer c_kj, then rounding once, preserves the intended finite polynomial up to the recorded rounding. This is a change of evaluation formula, not a change of basis or a projection of coefficients onto extra constraints.

The expansion can be poorly conditioned away from z=0. An implementation may select the original recurrence near the origin and this expansion for r>=256R. In exact arithmetic the two formulas agree. At the numerical switch, continuity and derivative consistency still require numerical checks. No error bound follows solely from this algebraic identity.

## Dependencies

Finite polynomial algebra, the positive square root and elementary differentiation. No formal proof or PDE claim is made.
