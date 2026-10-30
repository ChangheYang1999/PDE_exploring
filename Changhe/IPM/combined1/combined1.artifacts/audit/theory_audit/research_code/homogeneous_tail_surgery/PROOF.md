# Removing a finite homogeneous residual tail at arbitrarily small L2 cost

This extends the cutoff construction of T4-314 and responds to the new
forced(9,0)tail in Opus the review of T4-294 R2. It is a reference-design theorem,
not an existence theorem. The proof precedes all coefficient calculations.

## 1. Inverting density on finite angular polynomials

Let q<-1, a=q+3, M>=0, and suppose

    a not in {0, plus or minus2, ..., plus or minus2M}.             (1)

For every real odd-sine polynomial B(theta)=sum_(l=0)^M b_l
sin((2l+1)theta), there is a unique even-cosine polynomial
P(theta)=sum_(m=0)^M p_m cos(2m theta) such that

    -partial_y Delta[r^a P(theta)]=r^q B(theta), r>0.              (2)

Here unique means within this finite angular space and fixed radial
homogeneity. Define

    H_0=-a^2(a-2),
    H_m=-(a^2-4m^2)(a-2-2m)/2, m>=1,
    J_m= (a^2-4m^2)(a-2+2m)/2, m>=1.

Then p_M=b_M/H_M and, in descending order,

    p_l=(b_l-J_(l+1)p_(l+1))/H_l, l=M-1,...,0.                  (3)

For M=0 this reads p_0=b_0/H_0. To prove the formulas, use
Delta(r^a cos(n theta))=(a^2-n^2)r^(a-2)cos(n theta), then

    -partial_y[r^d cos(n theta)]
      =r^(d-1)[-(d-n)sin((n+1)theta)
                          +(d+n)sin((n-1)theta)]/2.             (4)

In applying(4) to the Laplacian, d=a-2. This gives the displayed
coefficients H_m and J_m, including H_0 after folding sin(-theta).
The two radial derivatives taken by Delta must be included in this shift.
Under a<2 and(1), every H_m is nonzero: the extra root a=2+2m is excluded
by a<2. The resulting
upper bidiagonal system is invertible by descending substitution.
This proves(2), with no elliptic solvability or mode-range assumption
left implicit.

## 2. Smooth realization outside a large disk

Choose the fixed smooth cutoff zeta(r) that is0for r<=1 and1for r>=2:
write b(s)=exp(-1/s)for s>0 and0otherwise, and put
zeta(r)=b(r-1)/(b(r-1)+b(2-r)). Define

    chi_1(X)=zeta(r) r^a P(theta),
    h_1=-partial_y Delta chi_1,
    v_1=grad_perp partial_xy chi_1,
    chi_L(X)=L^a chi_1(X/L), L>=1.

All functions extend smoothly by zero at the origin, and chi_1 is even
in x and y. Thus h_1 is S1 and v_1 has the canonical S1 velocity parity.
With h_L=-partial_y Delta chi_L and v_L=grad_perp partial_xy chi_L,

    h_L(X)=L^q h_1(X/L),  v_L(X)=L^q v_1(X/L).                  (6)

For r<=L both fields vanish, including every derivative at the origin.
For r>=2L, h_L=r^q B(theta), independent of L. Both h_L and v_L lie in
L2 because q<-1. They have the same divergence and curl as the canonical
velocity U[h_L], including its contact contribution. Their difference
is an L2 entire harmonic vector field, hence zero by the Fourier
transform or the mean-value property. Therefore v_L=U[h_L]; no extra
dipole or unspecified harmonic field has been added.

For the full ordered derivative tensor D^k, any real beta and
q+1+beta-k<0, exact scaling gives

    ||r^beta D^k h_L||_2
       =L^(q+1+beta-k)||r^beta D^k h_1||_2.                     (7)

The unit constant is finite: the field vanishes near zero and its kth
exterior derivatives are O(r^(q-k)). The same formula holds for v_L.
In particular ||h_L||_2 tends to zero as L tends to infinity, while its
prescribed homogeneous exterior density remains fixed.

For q<-3 the first moments of h_L are absolutely convergent and both
vanish. The x moment vanishes by parity. For the y moment, integration
by parts on a large disk gives int y h_L=int Delta chi_L, with boundary
errors O(r^(q+3)); the last integral is the boundary flux of chi_L,
again O(r^(q+3)). These terms tend to zero because q+3<0. The origin
has no boundary contribution. Thus the absence of an r^-3 velocity
dipole in(6) agrees with the canonical moment identity. The cutoff
annulus supplies the necessary moment cancellation.

## 3. Cancellation of a reference residual

Fix c>1, gamma=1/c, delta=1-gamma. Let R be a smooth S1 reference with
canonical velocity. Suppose for r>=R0>=2 that

    |U[R]|<=V r^gamma, |grad R|<=G r^(gamma-1),
    F(R)=r^q A(theta)+E_0(X), |E_0(X)|<=E r^(q-epsilon),
    F(R)=cX.grad R-R+U[R].grad R,

where epsilon>0, A is a finite odd-sine polynomial and q satisfies
section1. Choose B=A/(1-cq), solve(3), and use section2 with L>=R0.
For r>=2L, cX.grad h_L-h_L=(cq-1)h_L=-r^q A, so

    F(R+h_L)=E_0+U[R].grad h_L+U[h_L].grad R+U[h_L].grad h_L.

If h_L=r^q B and v_L=r^q W in this exterior region, let B1 bound the
angular factor in r^(1-q)grad h_L and let W0=max|W|. Then

    |F(R+h_L)| <= E r^(q-epsilon)
        +(V B1+G W0)r^(q-delta)+W0 B1 r^(2q-1).                 (8)

Thus the leading homogeneous residual has been removed, with remainder
O(r^(q-min(epsilon,delta,1-q))). This conclusion is about the exterior
residual; it does not assert that its full-plane norm is small.

The change of the full-plane residual does tend to zero in L2. Set the
finite unit constants

    C_lin=||cZ.grad h_1-h_1||_2,
    C_grad=|| |Z|^gamma grad h_1||_2,
    C_vel=|| |Z|^(gamma-1) v_1||_2,
    C_quad=||v_1.grad h_1||_2.

The support condition r>=L>=R0 and a change of variables give

    ||F(R+h_L)-F(R)||_2 <= L^(q+1)C_lin
        +L^(q+gamma)(V C_grad+G C_vel)+L^(2q)C_quad.              (9)

All exponents are negative since q<-1 and gamma<1. Every unit constant
is finite by the exterior powers and vanishing near zero. The theorem
therefore removes a prescribed far tail while preserving the interior
and changing both the density and residual by arbitrarily small L2
amounts. It does not drive a fixed nonzero residual norm to zero.

## 4. Two consecutive campaign sectors

For007,013,014 the exact first two nonzero residual exponents are

    q1=-1-4delta, q2=1-9delta,

followed by q3=-1-5delta. Each q_i satisfies q_i<-1, and a_i=q_i+3
satisfies(1)for the relevant finite angular supports. The source tables
bind all coefficients exactly. At q1, formula(3) recovers the negative
of the original potential first-descendant coefficients A1_m. This is
an independent check of the sign and the shifted radial coefficients.
At q2 it gives90 exact potential coefficients for the90 odd density
modes1,...,179.

First remove q1 with a cutoff radius L1. Since q1-delta=q3<q2 and
2q1-1<q2, this leaves the original coefficient F_(9,0) unchanged.
The remaining residual is r^q2 F_(9,0)+O(r^q3). Next apply the same
theorem at q2 with L2 large enough that its exterior lies beyond both
the first cutoff and R0. Since q2-delta<q3, the result is O(r^q3) at
infinity. Given any eta>0, choose L1 and then L2 so each correction
has L2 norm below eta/2. Their sum has norm below eta, vanishes on the
original interior disk, preserves every origin normalization, and
removes both prescribed residual sectors exactly outside2L2.

The same choices make any finite collection of norms(7)small when all
its exponents are negative. They preserve a preexisting distance
exclusion if eta is below its margin, by the triangle inequality.
This is compatible with the weighted-tail obstructions: the correction
has a nonzero q1 tail and does not belong to the stricter weighted
affine classes that forbid that tail.

## 5. Scope and verification

Only the finite homogeneous sector maps are solved. No solution of
the nonlinear stationary equation, whole-plane inverse, or convergent
infinite sector iteration is asserted. No claim is made at the excluded
resonant homogeneities, where logarithmic terms may be needed.
The explicit cutoff radii depend on finite unit norm constants; their
existence is proved, but numerical radii are not selected here.

The independent exact checker solves the triangular system, applies a
second direct differentiation formula to all outputs, compares q1 with
the accepted potential repair, and stores q2 in exact JSON. The proof
and these new design data await independent Opus review.
