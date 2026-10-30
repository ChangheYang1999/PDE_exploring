# Independent Cartesian-gradient audit of angular parity compression

## Statement

Use the exact S1 density rho of C1-N1-008-d2w-j7-x3bal, with canonical
SHA-256 13fe3fb1d9204b61e08599da7c4f5d6584034666040305bd01e4dde1783677f1.
For a=rho_x, b=rho_y and R_j=partial_j(-Delta)^(-1/2), set
K=[R1,[R1,b]]/2-[R1,[R2,a]]/2. The audited gradient identity gives

    ||K||HS²=kappa²
      =((log2-1/2)||D a||2²+(3log2-2)||D b||2²)/(16pi).

The domain here is real L2(R²), with full-plane Lebesgue measure.
For each parity p in {even-even,odd-even,odd-odd}, choose a finite
linearly independent family of smooth tests h_i of that parity.
Let G_p=(<h_j,h_i>) and B_p=(<K h_j,h_i>). Then

    T=sum_p tr(G_p^-1 B_p G_p^-1 B_p),
    0<=T<=kappa²,
    ||K restricted to S1||op<=sqrt(kappa²-T).              (1)

This numerical audit reconstructs the matrices from Cartesian
rho-gradient pairings and exact Fourier Gram formulas, and compares
them entry by entry against the independent T4 density-pairing
calculation. No sampled integrals or numerical Riesz transform enter.
The signed low-generator and nonlinear hypotheses remain separate.

## Proof of the budget

Coordinate reflections commute with K, as follows by expanding the
double commutators: a is odd in both coordinates, b is even in both,
and R_j reverses only its jth coordinate parity. Thus the four parity
spaces reduce the self-adjoint Hilbert-Schmidt operator K. In an
orthonormal basis adapted to these spaces, the full sum of squared
matrix entries contains the entire S1 block and the three chosen
finite compression blocks as disjoint nonnegative sums. The latter
sums are exactly tr(G_p^-1 B_p G_p^-1 B_p), because the map from
coefficients into the span becomes isometric after multiplication
by G_p^-1/2. This proves (1), including nonnegativity of its radicand.

## Test family and independent Gram formula

Let f_n=partial_z^n(z²+r²)^(-1/2)|_(z=1). Define
C_m=Re(partial_x+i partial_y)^m and S_m=Im(partial_x+i partial_y)^m.
Take f_{m,n}=C_m f_n or S_m f_n and h_{m,n}=-Delta f_{m,n}.
All cosine families lie in a complementary parity space. A sine
family is complementary precisely when m is positive and even.
No odd sine family is subtracted from the S1 budget.

The radial functions are constructed from the explicit Legendre
identity proved in ../parity_budget_audit/PROOF.md:

    f_n(t)=(-1)^n n! (1+t)^(-(n+1)/2) P_n((1+t)^(-1/2)).

For a radial f(t), t=r², the harmonic derivatives satisfy

    (partial_x+i partial_y)^m f(t)
                  =2^m(x+iy)^m f^(m)(t).

Induction proves this because (partial_x+i partial_y)(x+iy)=0.
Taking real or imaginary parts gives exact Cartesian monomials
x^u y^v(1+r²)^(-p), with rational coefficients and half-integer p.
All subsequent derivatives use the ordinary product rule.

With Fourier convention hat f=integral exp(-i X.xi)f(X)dX, the tests
have transform 2pi i^m(-1)^n |xi|^(m+n+1)exp(-|xi|) times their angular
sine or cosine. Distinct angular harmonics are orthogonal. If the
kind and m agree for tests i,j, their Gram entry is

    G_ij/pi = a_m (-1)^(n_i+n_j)
      (2m+n_i+n_j+3)! / 2^(2m+n_i+n_j+4),
    a_0=2, a_m=1 for m>0.

Otherwise it is zero. Independence follows from the distinct angular
harmonics and distinct powers of |xi| within each harmonic. Hence
G is positive definite. Exact LDL pivots provide an arithmetic check.

## Direct gradient pairing

The Poisson identity (-Delta)^(1/2)f_n=-f_(n+1) gives

    U1[h_i]=-partial_xy f_i, U2[h_i]=partial_xx f_i,
    R_j h_i=-partial_j D_m f_(n+1).

Write v_{ji}=R_jh_i. Expanding the symmetric coupling and the signed
principal operator gives

    A_ij=(h_i U1[h_j]+h_j U1[h_i]-v_{1i}v_{2j}-v_{2i}v_{1j})/2,
    D_ij=(h_i U2[h_j]+h_j U2[h_i])/2+v_{1i}v_{1j},
    B_ij=integral(a A_ij+b D_ij)dX.                       (2)

The signs of the v terms use R_j*=-R_j. This directly pairs the exact
Cartesian background gradients with rational test products. Unlike
the peer calculation, it does not integrate by parts onto rho.

## Exact gradient moments

The independently differentiated canonical potential gives

    a=sum_(j,n) (1+r²)^(-alpha_j) Q^a_(j,n)(u) sin(n theta),
    b=sum_(j,n) (1+r²)^(-alpha_j) Q^b_(j,n)(u) cos(n theta),
    u=r²/(1+r²), alpha_j=(j+1)(1-1/c)/2.

The stored fourth-derivative numerator is divisible by u²; divide
exactly to obtain Q. The gradient modes are even. For a monomial
x^v y^w(1+r²)^(-p) of even total degree2d, its contribution in (2),
divided by pi, is

    angular(kind,n,v,w)/2
      *sum_l Q_l Beta(d+l+1,p+alpha_j-d-1),              (3)

where angular is the full-circle integral of cos(theta)^v
sin(theta)^w times sin(n theta) or cos(n theta), divided by pi.
The binomial expansion of (cos(theta)+i sin(theta))^n computes this
coefficient exactly. An even monomial has integral divided by pi

    2(2a)!(2b)!/[4^(a+b)a!b!(a+b)!],

and any odd exponent gives zero. Fourier orthogonality makes the
angular factor zero when n>v+w, so a finite exact mode list suffices.
Equation (3) follows from r dr=dt/2 and u=t/(1+t). Every second beta
parameter is checked positive. The first parameter is a positive
integer, so all beta values are exact rational products.

## Verification and scope

Read and hash the exact peer inputs. Recompute every relevant entry
of G/pi and B/pi, all positive LDL pivots and all exact traces, then
compare the final outward scalar bounds. A selected smaller matrix
can be checked first without implying that a larger matrix is checked.
Record N, M, test labels and dimensions with each result. The four
parity-block argument uses the complete gradient-commutator identity;
the residual, high inverse, strain trace and theta are not supplied
by these matrices. A bound below c-1 still requires the separate
inequality theta<=c-1-bound to certify signed rate two.
