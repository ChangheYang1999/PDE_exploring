# Independent audit of the global matrix-cover method

## Statement and scope

Let chi be a smooth real potential even in each coordinate, with the finite rational generator representation in the frozen N4 target. Put rho=-chi_xxy-chi_yyy, u=(-chi_xyy,chi_xxy), V=cX+u, and

A=[[rho_y,-rho_x/2],[-rho_x/2,0]],
M=(2c+1)I+sym Du+A,
M_k=(1+c+V.grad log omega_k)I-k sym DV+A,
omega_1=(1+r²)^(-1/10), omega_2=(1+4r²)^(2/5).

The polynomial identities and interval-cover acceptance test in source/N4_PROOF.md imply M>=19I/5 and M_k>=I/2 for k=1,2 whenever every leaf of each complete cover passes that test. The test is mathematically valid. This note audits the method and identities; it does not independently reproduce the arithmetic of every saved d2 leaf.

The weighted matrix M_1 here is distinct from I-sym Du+A, the unweighted first-derivative matrix needed by some no-H frameworks. A certificate for this M_1 must not be silently substituted for that other matrix.

## Matrix identities

Direct differentiation gives

Du=[[-chi22,-chi13],[chi31,chi22]],
rho_x=-chi31-chi13, rho_y=-chi22-chi04.

Therefore M-19I/5 has equal constant diagonal part 2c+1-19/5, diagonal perturbations -2chi22-chi04 and chi22, and off-diagonal chi31.

Write t=r²/(1+r²) and e=(X.u)/r² for r>0. Since u is the perpendicular gradient of psi=chi_xy, X.u=-partial_theta psi, proving e=-partial_theta(chi_xy)/r². Also

V.grad log omega_1=-t(c+e)/5,
V.grad log omega_2=16t(c+e)/[5(1+3t)].

For k=1, subtract I/2. The constant scalar part is 1/2-ct/5, the diagonal perturbations are -chi04-te/5 and -chi22-te/5, and the off-diagonal is chi13.

For k=2, subtract I/2 and multiply by 1+3t>0. The constant scalar part is

1/2-c+(3/2+c/5)t.

The diagonal perturbations are (1+3t)(chi22-chi04)+(16/5)te and -2(1+3t)chi22+(16/5)te. The off-diagonal is (1+3t)(3chi13-chi31)/2. These are exactly the target formulas. Although e itself may have a directional limit at zero, te=(X.u)/(1+r²) is smooth there.

## Polynomial representation and ranges

Set z=cos(2theta) and w=(1-t)^(delta/2). The generator derivative identities give each fourth derivative as a finite polynomial in t,z,w, with every odd-odd derivative carrying a factor sin(2theta). This follows from cos(2m theta)=T_m(z) and sin(2m theta)=sin(2theta)U_(m-1)(z). Exact division by t² must be checked on the radial numerator before using the representation. The S1 reflections change only the off-diagonal sign, so eigenvalues are unchanged. Thus 0<=t<=1, -1<=z<=1 covers all radii and angular quadrants, including their limiting boundaries.

For a polynomial on a closed rectangle, affine restriction to [0,1] in each variable followed by the tensor Bernstein expansion encloses its range by the least and greatest coefficients. The basis polynomials are nonnegative and sum to one. The power-to-Bernstein identity is B_i=sum_(k<=i) a_k binom(i,k)/binom(d,k). Applying this in each coordinate proves the stated algorithm, provided the arithmetic encloses every transformed coefficient.

On a radial cell [a,b], treating w as an independent variable in [(1-b)^(delta/2),(1-a)^(delta/2)] enlarges the true set, so it gives a valid range bound. On a cell with b<1, expand each (1-t)^q at mu=(a+b)/2. Taylor's theorem gives remainder at most

|(q)_(N+1)| ((b-a)/2)^(N+1)/(N+1)!
 times max((1-a)^(q-N-1),(1-b)^(q-N-1)).

This is valid for either sign of q-N-1 because the endpoints are positive. Multiply by the maximum absolute Bernstein coefficient of the remaining branch polynomial and sum the resulting errors. The Bernstein product identity

B_(i,d) B_(j,N)=binom(d,i)binom(N,j)/binom(d+N,i+j) B_(i+j,d+N)

preserves the dependence on the common radial variable. The resulting correlated Taylor enclosure and the independent-w enclosure are both valid. Their intersection is valid; no independence of the underlying variables is asserted.

## Eigenvalue and coverage checks

Suppose the two diagonal functions are bounded below by real a,b and the off-diagonal magnitude is at most C. Pointwise subtraction of the diagonal lower-bound matrix is positive semidefinite. The least eigenvalue is therefore at least

(a+b-sqrt((a-b)²+4C²))/2.

The alternative bound min(a,b)-C follows from 2|xy|<=x²+y². Taking the larger of the two bounds is valid. If the off-diagonal is sin(2theta) times q(z,t), then C can be bounded by max|q| times sqrt(1-min_z |z|²) on that cell. Outward interval evaluation of these formulas is sufficient, including when a-b changes sign. A nonnegative lower bound certifies the desired shifted matrix.

A finite binary cover rooted at the full rectangle is complete if every internal node has exactly its two halves along one coordinate and every node is either a leaf or such an internal node. Check exact endpoints and prohibit duplicate and ancestor leaves. Induction on the finite tree then proves that the leaves cover the root. Merely matching total areas would not establish this.

## Dependencies and limitations

The dependencies are smooth profile reconstruction, exact rational derivative identities, elementary trigonometric recurrences, Taylor's theorem, Bernstein positivity, and outward interval arithmetic. The argument proves the soundness of the test. A certified candidate conclusion also needs successful arithmetic on all leaves for that candidate. It establishes only these three matrix inequalities, not higher derivative caps, residual smallness or nonlinear existence.
