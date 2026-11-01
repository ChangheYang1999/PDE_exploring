# Necessary radii for the automatically compatible single harmonics

Status: PROVED after directed verificationV508 and the independent review of17:52Z, admittedV512. The6/13 center now has an admitted convergent sequence by242/V528.

## Statement

Take one of the following three rows and let epsilon be nonzero and real. Consider any compatible pure density and stream sequence with f_1(theta)=epsilon sin(M theta), with only the prescribed resonant homogeneous stream modes.

| delta | c | M | B | a=2/(B-delta) | b=2M/(B-delta) | 4d=4delta/(1-delta) |
|---|---|---|---|---|---|---|
| 4/5 | 5 | 7 | 8 | 5/18 | 35/18 | 16 |
| 4/7 | 7/3 | 9 | 10 | 7/33 | 21/11 | 16/3 |
| 6/13 | 13/7 | 17 | 18 | 13/114 | 221/114 | 24/7 |

Define the positive constant

    R_H=4d [a Gamma(a) Gamma(b)/Gamma(a+b)]^(1/a).

If the density series and its first two angular derivatives converge term by term uniformly on r>=R, then necessarily

    R>R_H^(-1/delta) |epsilon|^(1/delta).

This condition is necessary only. Existence at the three stated centers is established separately in241,233 and242.

## Proof

The angular support is bounded by Bn-1 for the nth density coefficient and by Bn for the stream. A free stream harmonic at order n has frequency delta n-2, strictly smaller than Bn. In each advection product, only the two top input frequencies can produce the top output frequency. Thus free harmonics and their propagated lower-frequency changes never affect the top sector, as proved in170.

Writing the highest sine coefficient as A_n=(-1)^(n-1)epsilon^n h_n gives h_1=1 and

    4d(n-1) h_n = sum_(i+j=n) [2Bj/((B-delta)i+2)-1] h_i h_j.

The coefficient asymptotic theorem115, with normalization117, gives h_n>0 and

    h_n R_H^n ~ K n^(-1-1/b), K>0.

The exact substitutions in the table give 1-1/b equal to17/35,10/21 and107/221, respectively. At r=R_H^(-1/delta)|epsilon|^(1/delta), the top coefficient of the second angular derivative of the nth density term therefore has magnitude asymptotic to a positive constant times n^(1-1/b). It does not tend to zero. Uniform convergence of angular functions would force every individual Fourier coefficient of each term to tend to zero, since Fourier extraction has uniformly bounded norm. The necessary term test fails at the stated threshold. Below that threshold the undifferentiated top coefficient grows exponentially. This proves the strict inequality.

## Numerical verification plan

Evaluate the positive gamma expression at512 and1024 bits with fresh rational-to-ball conversions and verify overlap. Save exact dyadic ball encodings and directed decimal lower and upper bounds for each necessary radius. Independently generate the first four top coefficients with the exact Cartesian differential recurrence, and compare them with the scalar recurrence displayed above. No ratio fit or truncated tail estimate is used in the necessary-radius proof.

Dependencies:38,115,117,170. Sufficient convergence of all three profiles is proved separately in241,233 and242. This result does not locate a singularity of the full series or provide a sharp radius.
