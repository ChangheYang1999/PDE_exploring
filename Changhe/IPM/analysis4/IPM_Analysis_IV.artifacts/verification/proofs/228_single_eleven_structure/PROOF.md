# Necessary logarithm and radius for the eleventh-harmonic branch

Status: PROVED, independently reviewed by the theory part and verified by exact reconstruction and directed arithmetic in V492.

## Statement

Let delta=4/9, c=9/5, and f_1(theta)=epsilon sin(11 theta), with real epsilon!=0. Consider a compatible pure density and stream sequence on the prescribed exponent lattice, using only its resonant homogeneous stream modes. Then:

1. Its common potential necessarily contains the nonzero term epsilon^9 lambda log r at order9, modulo the irrelevant constant gauge. Here lambda=beta_pure-H_9, where beta_pure is the order9 stream amplitude forced by the pure degree-zero potential and H_9 is the unique amplitude that cancels the order18 obstruction. The exact rational values are defined and independently checked in topic36. For epsilon=1, lambda>0. A common potential containing only pure powers is obstructed at order18.
2. Define

       a=9/52, b=99/52,
       R_H=(16/5)[a Gamma(a) Gamma(b)/Gamma(a+b)]^(52/9).

   Uniform termwise convergence with two angular derivatives on a closed exterior r>=R requires

       R > (|epsilon|/R_H)^(9/4).

   This necessary bound is not a sufficient convergence radius. It applies even if the all-integer response hypothesis of topic227 has not been proved. The highest Fourier sector never terminates.

## Proof of the necessary logarithm

At order9 the density exponent is -3, the stream exponent is -2 and the potential exponent is zero. The first compatibility coefficient vanishes by the signed-support calculation in227. Let D_(2k) be the cosine coefficients of Delta chi at degree -2. The exact density identities are

    a_1=2D_0=0,
    a_(2k+1)=(k+1)D_(2k)+kD_(2k+2),  k>=1.

Starting above the finite support with D=0, backward substitution determines the remaining coefficients. A pure potential has coefficient -D_(2k)/(4k^2) for cos(2k theta). Direct differentiation gives its forced frequency-two stream amplitude beta_pure=D_4/8. Topic36 proves uniqueness up to a constant among smooth periodic S1 degree-zero potentials representing this density.

The order18 compatibility is R_1+sigma_1 H_9=0. Its exact slope is nonzero, so H_9=-R_1/sigma_1 is uniquely fixed. The exact calculation in36 gives H_9!=beta_pure and lambda=beta_pure-H_9>0 at unit amplitude. Since Delta log r=0 and partial_xy log r=-r^(-2)sin(2theta), adding lambda log r corrects precisely this stream amplitude without changing the density. The scalar identities determine the sign of lambda. Homogeneity of the order9 coefficients gives the factor epsilon^9. No constant gauge removes a nonzero logarithm.

The Cartesian code represents an odd sine polynomial as i times the physical polynomial. Its operators X and Y represent partial_x and -i partial_y. Consequently the encoded density is Y(X^2-Y^2)C and the encoded stream is -XYC; the apparent minus sign in the encoded Laplacian is due to this convention.

The reconstruction check below differentiates the complete finite potential, including its logarithm, and compares every coefficient of both the density and stream. It also recomputes beta_pure from the independent exact Cartesian prefix, rather than only subtracting stored decimals.

## Proof of the necessary radius

The highest density frequency is at most12n-1. At order9k every free stream frequency is4k-2<108k. As in170, a lower input cannot reach the highest output frequency in a later product, so all tuning is irrelevant to the top density coefficients A_n.

Set d=4/5 and eta=104/9. The exact scalar recurrence is

    A_n=(-1)^(n-1)epsilon^n h_n,  h_1=1,
    4d(n-1)h_n=sum_(i+j=n)[24j/(eta i+2)-1]h_i h_j.

Topics38 and115 prove h_n>0 and

    h_n R_H^n asymptotic to K n^(-1-52/99),  K>0.

At r=(|epsilon|/R_H)^(9/4), the magnitude of the highest Fourier coefficient in the second angular derivative of the nth density term is asymptotic to a positive constant times n^(47/99). It does not tend to zero. Fourier coefficient extraction is a continuous functional on continuous angular functions, so the uniform term test fails. At smaller radii the undifferentiated top coefficient grows exponentially. This proves the strict inequality. Positivity of every h_n also proves nontermination.

## Verification and scope

The exact program checks the degree-zero potential by Cartesian differentiation, compares the first nine top coefficients with the scalar recurrence, and encloses R_H and its necessary radius with directed arithmetic. Topic227 separately addresses sufficient convergence. Nothing here asserts a whole-plane canonical stationary extension, identifies the actual full-series radius or locates a singularity at a fixed angle.
