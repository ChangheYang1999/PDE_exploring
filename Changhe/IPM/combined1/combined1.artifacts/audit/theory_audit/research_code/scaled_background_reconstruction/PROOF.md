# Independent exact gradient reconstruction for candidate 017

## Statement and scope

Fix the exact potential and c in data/017.json, whose SHA256 is
7dc30181e2d29c8c9706cf396a1be2334f53b2a19ca00e4fad756ff98ec59114.
Put delta=1-1/c, r=sqrt(x^2+y^2), t=r^2/(1+r^2), v=1-t,
w=v^(delta/2), z=cos(2 theta). Define rho=-partial_y Delta chi.
The exact sparse rational polynomials in the frozen N4 reconstruction
represent the whole-plane gradient, for r>0, by

    rho_x = sin(2 theta) / D(t) sum_(j=1)^8 w^j P_(x,j)(t,z),
    rho_y =                 1 / D(t) sum_(j=1)^8 w^j P_(y,j)(t,z),
    D(t)=(1+2499(1-t))^19.

The verification compares every nonzero rational coefficient with an
independent construction from the canonical input. The construction and
its identities are proved below. A successful exact comparison proves
that the frozen N4 polynomials represent these derivatives. It does not
prove a Bernstein cover, a uniform matrix bound, an inverse, or existence.
No interpolation or finite sample is used to justify coefficient equality.

## Dependencies and exact generator meaning

The accepted polar construction and rational arithmetic of T4-366 are in
scaled_hessian_audit, with PROOF.md and its input manifest. The raw
potential generators and branch powers are precisely those of that topic.
In more detail, a raw branch j has factor v^(-p_j), where
p_j=2-(j+1)delta/2. Its angular factor is cos(2m theta). For a generator
specification (legqs,w0,n,q,R), let L=1+(R^2-1)v. Its rational radial factor
is

    sum_(k=0)^n (-1)^(n+k) binom(n,k) binom(n+k,k)
       R^(2q) t^(m+w0+k) v^q / L^(w0+q+k).

This is the finite shifted-Legendre identity, applied to the compact
coordinate t/L. It also covers unscaled and monomial generators by the
corresponding n=0, q=0 and R=1 specializations. Coefficients are exact JSON
rationals, not parsed binary floats. Candidate 017 uses R=1 or R=50.

## Polar differentiation

For a rational radial function A, the radial Euler derivative of
v^(-p) A(t) is v^(-p) E_p A, where

    E_p A = 2t(1-t) A'(t) + 2pt A(t).

The polar Laplacian of a cos(n theta) branch is
r^(-2)v^(-p)(E_p^2-n^2)A cos(n theta). Applying -partial_y gives the
sine modes n-1 and n+1, using the elementary products of sin(theta),
cos(theta) and the mode n. In the exact raw input the resulting rational
numerators are divisible by t^2. Since r^(-3)t^2 v^(-p_j)
= r v^((j+1)delta/2), the density takes the form

    rho = r sum_(j,n) v^a_j A_(j,n)(t) sin(n theta),
    a_j=(j+1)delta/2.

The accepted T4-366 backend obtains these A directly by the displayed
polar Laplacian and differentiation, rather than the N4 Cartesian fourth
derivative recurrence. Exact division by t^2 is checked, never assumed.

For a branch r^d v^a A(t) times a sine or cosine, set

    B=(d-2at)A+2t(1-t)A'.

For d=1 and a=a_j, partial_x of a sine branch has coefficients
(B-nA)/2 at sine mode n+1 and (B+nA)/2 at sine mode n-1.
Partial_y has coefficients -(B-nA)/2 at cosine mode n+1 and
(B+nA)/2 at cosine mode n-1. Negative modes are folded using sine's odd
and cosine's even identities. These formulas follow by writing
partial_x=cos(theta)partial_r-sin(theta)r^(-1)partial_theta and
partial_y=sin(theta)partial_r+cos(theta)r^(-1)partial_theta.
There is no remaining r power in either gradient component. All resulting
modes are even. The x component has no zero sine mode.

## Denominator clearing and angular conversion

Every exact gradient coefficient A=P_A/D_A is held with an explicit
product of powers of 1+624v and 1+2499v. In this candidate the first power
is zero and the second is at most 19. Multiply P_A by D/D_A, using exact
polynomial division and checking

    (P_A D/D_A) D_A = P_A D.

D(t)>0 on [0,1], so this clearing introduces no singularities. Set
z=cos(2 theta). The polynomial identities

    cos(2k theta)=T_k(z),
    sin(2k theta)=sin(2 theta) U_(k-1)(z)

give the stated P_(y,j) and P_(x,j). To avoid sharing N4's three-term
recurrence, the independent checker uses closed coefficient formulas:

    T_0=1,
    T_k(z)=(k/2) sum_(a=0)^floor(k/2)
       (-1)^a (k-a-1)!/[a!(k-2a)!] (2z)^(k-2a), k>0,
    U_k(z)=sum_(a=0)^floor(k/2)
       (-1)^a binom(k-a,a) (2z)^(k-2a).

The usual recurrence, checked algebraically, or the exponential formulas
for cosine and sine prove these finite identities. Exact sparse addition
then gives all coefficients of every P. Vanishing coefficients are removed
only after exact addition. Equality of the resulting complete maps proves
the reconstruction globally for every r>0 and theta.

## Origin and infinity

The canonical potential is smooth at the origin. The gradient formula is
initially derived away from r=0, but its exact origin specialization has
sum_j P_(x,j)(0,z)=0 and sum_j P_(y,j)(0,z)=rho_y(0)D(0), independent of z.
Since w tends to 1 as r tends to 0, this proves continuous agreement there.
For an independent local check, expand the original generator in u=r^2.
For each m+w0<=2 and 0<=k<=min(n,2-m-w0), its coefficient of
u^2 cos(2m theta) is the exact coefficient multiplying

    (-1)^(n+k) binom(n,k) binom(n+k,k) R^(-2(w0+k))
    sum_(i=0)^(2-m-w0-k) binom(p_j-m,i)
       binom(-w0-q-k,2-m-w0-k-i) R^(-2(2-m-w0-k-i)).

This follows by expanding (1+u)^(p_j-m)(1+u/R^2)^(-w0-q-k).
Generators with m+w0>2 cannot contribute. Call the resulting three
coefficients b0,b1,b2. Since u^2, u^2 cos(2theta), u^2 cos(4theta)
equal (x^2+y^2)^2, x^4-y^4, and x^4-6x^2y^2+y^4, respectively,
the coefficients of x^2y^2 and y^4 are a22=2b0-6b2 and
a04=b0-b1+b2. Thus rho_y(0)=-4a22-24a04 and the origin strain is
4a22. These exact values are compared with the frozen N4 local jet,
and c+4a22=1 is also checked.
At infinity, t tends to 1 and w tends to 0, while D(1)=1. Thus each
polynomial representation has its proper continuous compactified limit.
This endpoint property does not bound the gradients at intermediate radii.

## Verification evidence and limitation

The checker binds the raw coefficient file, frozen compressed N4 polynomial
file and summary, this proof, and every executed independent backend.
It compares all coefficient maps and D exactly, then checks three point
pairs in Arb as secondary diagnostics. The point comparisons alone would
not prove the representation. The final record separates the exact
coefficient theorem from the still separate interval cover. No foreign
source code is executed. Computations use one low-priority CPU process.
