# Required clarifications and complete arithmetic obligations

Read this with the unchanged proof-first PROOF.md. The initial model review
was analytic only; it did not certify the numerical outputs.

## A1. Regularity and notation

The phrase importing C6 regularity in PROOF section1 means the existing
radial joins away from zero. At the center the trial is C4 locally, not
C6. Its finite angular degree-five terms need not be Cartesian polynomials.
For derivative order j<=4 they are O(r^(5-j)), and the faster terms have
continuous derivatives of these orders. Thus they extend continuously at
zero. The unchanged density near any fixed compact set is C4, and C3
already suffices for C2 convergence of u_T dot grad rho0. Neither the
cutoff construction nor any estimate here requires a fifth center derivative.

Every symbol (v)_j in the derivative estimates denotes the falling
factorial v(v-1)...(v-j+1), with (v)_0=1.

The reviewer incorrectly placed a1+1 in a negative interval. In fact
k+1 is in(1,5/4), a1+1=2k in(0,1/2), a2+1=3k-1 in(-1,-1/4), and
ad+1=k-1 in(-1,-3/4). These exact intervals give all positive denominators
used here. The engines used the correct exact exponents throughout.

## A2. Explicit cutoff and strain cancellation

Let b(s)=(s-1)^8(2-s)^8 on[1,2], extended by zero, and
B0=int_1^2 b(s)ds=(8!)^2/17!. Define chi(s)=B0^-1 int_1^s b
between1 and2, zero below1, one above2. Since b>=0, chi is monotone
and takes values in[0,1]. Symmetry about3/2 gives
Jb=int_1^2 s b(s)ds=3B0/2=1/145860; max b=2^-16.
All these statements can also be checked by exact polynomial integration.
For ai<1, Ji=int_1^infinity chi(s)s^(ai-2)ds obeys
0<Ji<=1/(1-ai).

The compensator for each row is
4 Ii Ji T^(ai-3) x^2 y b(r/T)/Jb, subtracted from its tail.
The raw strain of the tail is Ii Ji T^(ai-1); the raw strain of
x^2 y b(r/T) is T^2 Jb/4. Thus each difference has exactly zero
strain. Its interior n=1 stream is sigma xy, because
(Im z^2)/2=xy; zero strain removes the entire term. Interior higher
harmonics have zero strain at zero. The compensator has only density
sine frequencies1,3 and therefore changes no interior n>=2 term.

At the fixed original source P, h vanishes with all density derivatives
and its raw strain is zero. Directly differentiating
F(rho0+h,c0)-F(rho0,c0)=U[h] dot grad rho0 near P, using parity,
gives the change g partial_y U[h]_2(P)+g' U[h]_1(P).
There is no source-location assertion for the perturbed velocity.

## A3. Exact collected quotient inverse

Write H=cos^2(theta)sin(theta) sum_(m=0)^M q_m cos(2m theta),
and H=sum_(j=0)^(M+1) E_j sin((2j+1)theta). Missing q entries are zero.
Product-to-sum gives

 E0=(2q0-q2)/8,
 E1=(2q0+q1-q2-q3)/8,
 Ej=(q_(j-1)+q_j-q_(j+1)-q_(j+2))/8, j>=2.

The sequence c_l=(-1)^l(floor(l/2)+1) has formal power series
sum_(l>=0)c_l x^l=1/[(1+x)(1-x^2)]. This follows by multiplying
the geometric series sum(-x)^j and sum x^(2j). Equivalently its
convolution with(1,1,-1,-1) is(1,0,0,...). Substituting the displayed
Ej and collecting each q coefficient, using this convolution identity,
proves exactly

 q0=4 sum_(j>=1)c_(j-1) Ej,
 qm=8 sum_(j>=m+1)c_(j-m-1) Ej, m>=1.

The sums are finite. This proves the primary inversion independently
of a zero-containing remainder diagnostic. The secondary algorithm
divides the full Laurent polynomial by(w-1)(w+1)^2. Since
2i cos^2(theta)sin(theta)=(z-z^-1)(z+z^-1)^2/4, with w=z^2,
the three divisions give the same polynomial quotient. The exact finite
audit applies both inversion methods to every individual q basis vector
through degree781 and compares the whole quotient, not just E0.

## A4. Rigorous integer convolution

Let S=2^512. For each input interval[l,h], compute
L=floor(S l), H=ceil(S h). Then [l,h] is contained in
[(m-r)/(2S),(m+r)/(2S)] with m=L+H and r=H-L>=0.
For two such intervals centered at m/(2S),n/(2S), the product is
contained in midpoint mn/(4S^2), radius
(|m|s+r|n|+rs)/(4S^2). Summing these exact integer centers and
nonnegative radii over each convolution coefficient preserves inclusion.
The four polynomial multiplications in the implementation use exact
integers; final division and conversion to iv intervals are outward.
This argument covers sparse inputs, signed centers, intervals crossing
zero, and nonbinary endpoints. The finite tests supplement this proof.

## A5. Complete input and output audit

The audit compares all2600 original outer binary64 coefficients and all
1573 knots with their exact hexadecimal JSON export, the exact k,L,bo,
and the pinned normalization and leading-residual definitions. It checks
all four used sine rows by a third signed projection, every finite
Fourier support and ordered product coefficient formula, every quotient
basis vector, positivity of required Green denominators, all predecessor
file maps, and the inherited N1 and C1 ceilings against105's audited data.
Both engines are rerun completely and their exact endpoint arrays must
reproduce. All783 sine coefficients,782 quotient coefficients and22
scalar majorants are included. Overlap between engines is a diagnostic;
validity comes from the interval inclusions and complete finite formulas.

Public decimals are made by exact rational floor/ceiling arithmetic and
then tested strictly against both interval outputs. The local quantities
are upper-bound majorants for individual velocity components or Cartesian
derivatives, not measured jets. No bound for a full vector/tensor norm is
implied. The original hypothesis 2R0<=T and all cutoff conditions are
checked when a numerical radius is used. No global residual norm ceiling,
stationary solution, inverse, or decisive endpoint is claimed.
