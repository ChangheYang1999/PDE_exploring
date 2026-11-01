# Necessary first-period common-potential logarithms for Q4, Q5 and Q6

Status: PROVED, V536, admitted 2026-10-31T18:55:09+00:00. The exact independent prefix, Euclidean and potential reconstruction checks pass, and the theory part reviewed the argument on2026-10-31 at18:54Z. All18 coefficients in its separate polar a_Q calculation agree exactly.

## Statement and hypotheses

Let Q be4,5 or6, delta=2/Q, c=Q/(Q-2), and let b be a real root of the exact first compatibility polynomial O_(2Q) of142,130 or154, respectively. For real epsilon nonzero, take the already proved tuned pure density and stream series with leading coefficient epsilon[sin(theta)+b sin(3theta)]. Let a_Q(b) be the sin(theta) coefficient of its unit-amplitude density coefficient f_Q.

If gcd(O_(2Q),a_Q)=1 in Q[b], then every one of the six real compatibility roots for this Q requires a nonzero first-period common-potential correction

    epsilon^Q r^2 log(r)[alpha_Q(b)+beta_Q(b)cos(2theta)].

The density and stream series stay pure, and their sufficient exterior radii are unchanged. This statement concerns finite cosine angular coefficients and the power/logarithm reconstruction of132. It does not restrict other representations of the same function, and it makes no assertion that the second permitted logarithmic coefficient is nonzero.

## Complete argument

Before orderQ the positive-even sine Poisson multipliers are nonzero. At orderQ the radial density exponent is-1 and the stream exponent is0; the excluded zero sine frequency again gives a unique stream. Thus f_Q is a rational polynomial in b of degree at mostQ, independently of every later free harmonic.

For a finite even cosine potential of radial degree2, direct differentiation gives

    -partial_y Delta[r^2 c_m cos(2m theta)]
      =4m(1-m^2)c_m r^-1
        [sin((2m+1)theta)+sin((2m-1)theta)].

Both m=0 and m=1 vanish. Every other column has frequencies at least3. Hence no pure degree-two potential can produce a nonzero sin(theta) density coefficient.

Starting with the highest density frequency, eliminate it using the corresponding column m>=2, then continue downward. This terminates because f_Q has finite support. The residual is a_Q sin(theta)+d_Q sin(3theta). The exact identities

    -partial_y Delta(r^2 log r)=-4r^-1 sin(theta),
    -partial_y Delta(r^2 log r cos(2theta))
        =4r^-1[sin(theta)+sin(3theta)],
    partial_x partial_y(r^2 log r)=sin(2theta),
    partial_x partial_y(r^2 log r cos(2theta))=-sin(4theta)/2

show that alpha_Q=(d_Q-a_Q)/4 and beta_Q=d_Q/4 complete the density reconstruction. Both reconstructed and prescribed streams solve the same Poisson equation at radial degree0, where all positive even sine multipliers are nonzero, so the streams agree. In particular beta_Q-alpha_Q=a_Q/4.

The rational Euclidean identity gcd(O_(2Q),a_Q)=1 implies that the two polynomials have no common complex root. Therefore a_Q is nonzero at each real compatibility root. At least one of alpha_Q,beta_Q must be nonzero, proving necessity of a logarithm for all six branches. Homogeneity gives the factor epsilon^Q. A single finite logarithmic term does not affect the exterior radius established by the reconstruction theorem132.

## Verification protocol and dependencies

Generate the positive-frequency polar prefix independently throughQ, with both signed product frequencies. Compare all signed coefficients with the existing exact Cartesian prefix, including radial exponents and antisymmetry. Extract a_Q, compute a rational Euclidean remainder chain against O_(2Q), and verify that its final nonzero term is constant. Construct alpha_Q,beta_Q and check the full density and stream using Cartesian differential operators and the four displayed log identities. Preserve the exact polynomials, remainder chains, source hashes and actual elapsed time.

Dependencies:01,121,130,132,142,154,258. The finite obstruction alone proves logarithmic necessity; the previously admitted convergence results identify actual exterior branches with that obstruction.
