# Independent background seminorm calculation through the Laplacian

## Statement and exact data

Consider the finite real potential

chi=sum_(j,n) (1+r²)^p_j P_(j,n)(t) cos(n theta),
t=r²/(1+r²), u=1-t, p_j=(3+gamma-j delta)/2,
gamma=1/c in(0,1), delta=1-gamma,

with exact rational c and polynomials P. Assume that every branch extends smoothly through the origin and that the resulting density rho=-partial_y Delta chi is smooth, with |D^k rho|=O(r^(gamma-k)) for k<=3 at infinity. The exact state131 canonical JSON is the data for the accompanying calculation. This note proves a separate way to compute

||D²rho||_2², ||D³rho||_2², ||D rho_x||_2², ||D rho_y||_2².

All four norms use ordered Cartesian derivatives. Each squared norm is pi/2 times an exactly computed rational number. The method constructs the density directly from a radial Laplacian of chi, then uses integration by parts and beta integrals. It does not call the N4 Cartesian derivative recurrence or N4 norm integration routine. The canonical potential input is shared with the independently audited N4 source; this is a reproduction of the seminorm calculation, not a separate reconstruction of that input from the original optimizer.

## 1. Direct density construction

Let D=r partial_r. Acting on (1+r²)^p r^(-d)P(t), it gives the same prefactor times

A_(p,d)P=(2pt-d)P+2tu P'.

Since Delta=r^-2(D²+partial_theta²), the contribution of a potential mode to Delta chi is (1+r²)^p r^-2 B(t)cos(n theta), where

B=A_(p,0)(A_(p,0)P)-n²P.

Apply -partial_y using

partial_y[f(r)cos(n theta)]
=-(Df+nf)/(2r) sin((n-1)theta)+(Df-nf)/(2r) sin((n+1)theta).

Thus the two density numerator polynomials are (A_(p,2)B+nB)/2 and -(A_(p,2)B-nB)/2, at modes n-1 and n+1. Fold a negative sine mode with its sign and discard the zero sine mode. The code combines exact equal modes and checks divisibility by t². Dividing by t² gives

rho=r sum_(j,n) u^a_j R_(j,n)(t)sin(n theta), a_j=(j+1)delta/2,       (1)

because (1+r²)^p r^-3 t²=r u^(2-p) and 2-p=a_j. These polynomial checks also detect a failed smooth origin cancellation instead of silently ignoring it.

## 2. Laplacian and Hessian diagonal

On a term r u^a P(t), the radial operator D acts by

T_a P=(1-2at)P+2tu P'.

The Laplacian of the sine mode is therefore

Delta[r u^a P sin(n theta)]
=r u^(a+1) [(T_a²P-n²P)/t] sin(n theta).                   (2)

The numerator division is checked exactly. To compute the anisotropic columns without a Cartesian derivative tree, use

partial_x²-partial_y²=(1/2)[(partial_x+i partial_y)²+(partial_x-i partial_y)²].

The identities partial_x +/- i partial_y=exp(+/-i theta)r^-1(D +/- i partial_theta) give the following two sine-mode numerators after the same normalization as (2):

mode n-2: [(T_a+n-2)(T_a+n)P]/(2t),
mode n+2: [(T_a-n-2)(T_a-n)P]/(2t).                       (3)

Here each expression T_a+q means the operator T_a plus q times the identity. Negative modes are again folded with a sign. Now rho_xx is one half the sum of (2) and (3), and rho_yy is one half their difference. Their sum equals Delta rho as an exact polynomial identity.

## 3. Integration by parts identities

The derivative decay implies that all boundary terms in the following identities vanish on growing circles: their orders are at most R^(2gamma-2) for second derivatives and decay faster for third derivatives. Smoothness removes the shrinking-circle terms. Equivalently one may use smooth cutoffs and the same estimates. Integrating by parts twice gives

integral rho_xx rho_yy = integral rho_xy²,
||D²rho||_2²=||Delta rho||_2²,
||D rho_x||_2²=integral rho_xx Delta rho,
||D rho_y||_2²=integral rho_yy Delta rho.                  (4)

Apply the second identity to rho_x and rho_y and add. Their decaying first derivatives justify the same integrations, yielding

||D³rho||_2²=||D Delta rho||_2².                          (5)

In (4), the column integrands need not be pointwise positive; their exact integrals are positive by the proved identities. The implementation checks positivity at the end rather than dropping signed cross terms.

## 4. Exact beta integration

For two terms r u^b P(t)sin(n theta) and r u^c Q(t)sin(n theta), full-circle angular integration and r dr=dt/(2u²) give their inner product

(pi/2) integral_0^1 t u^(b+c-3)P(t)Q(t)dt.               (6)

Different positive sine modes are orthogonal. Expanding the polynomial P Q in t, each coefficient of t^k contributes Beta(k+2,b+c-2). All encountered b+c-2 are positive; this is checked exactly.

For the gradient inner product of the same two modes, the angular radial and tangential components give

(pi/2) integral_0^1 u^(b+c-2)
  [(T_b P)(T_c Q)+n²P Q]dt.                              (7)

Its monomials contribute Beta(k+1,b+c-1). The integrals converge at both endpoints under the stated positive exponents and polynomial regularity.

For positive rational v, Beta(m,v) is rational for positive integer m: Beta(1,v)=1/v and Beta(m+1,v)=m Beta(m,v)/(m+v). The code uses this recurrence directly, so all cancellations are exact. It sums all ordered pairs of branches, including their signs, then multiplies by pi/2 and takes an Arb square root. No spatial truncation, quadrature, decimal coefficient rounding or residual norm proxy is involved.

## 5. Verification and scope

The independent numerical comparison must check the exact rational quantities, not merely matching decimal endpoints. The four resulting rational energies are compared to N4's saved unweighted_rational_sum values. Equations (4)-(7) explain why those are the same normalization. The scalar Hilbert-Schmidt value then follows from the separately audited gradient-structured identity; its enclosure is a consequence of the two column energies. A positive L² inverse criterion still requires its own principal-sign and domain hypotheses. No nonlinear existence theorem follows from these seminorms alone.
