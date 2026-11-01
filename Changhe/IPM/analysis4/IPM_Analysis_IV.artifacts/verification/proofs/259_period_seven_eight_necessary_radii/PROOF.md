# Necessary exterior radii at periods seven and eight

Status: PROVED in V535. The independent theory-part derivation of18:42Z agrees, every exact highest-sector check passes, and all constants are enclosed twice in directed arithmetic.

## Statement

Let Q be 7 or 8, delta=2/Q and c=Q/(Q-2). Let b_i be any of the ten real compatibility roots isolated in253 or256, respectively. For real epsilon nonzero, consider the uniquely tuned pure density and stream series with

    f_1(theta)=epsilon[sin(theta)+b_i sin(3theta)].

Set

    a=Q/(2Q-1), beta=3Q/(2Q-1), d=2/(Q-2),
    R_H=4d [a Gamma(a) Gamma(beta)/Gamma(a+beta)]^(1/a).

If the density series and its second angular derivative converge uniformly term by term with their natural radial weight on the closed exterior r>=R, then

    R > (|b_i|/R_H)^(Q/2) |epsilon|^(Q/2).

These are necessary bounds only. They do not identify the true convergence threshold or improve the separately proved sufficient bounds. The conclusion about a given branch requires its convergence admission in253 or256.

## Exact highest sector

The density bandwidth at order n is4n-1. Write A_n for its coefficient at sin((4n-1)theta). Only the two highest participating input frequencies can generate this frequency in the stationary quadratic recurrence. A free stream harmonic has frequency delta n-2, strictly below4n, and neither it nor its propagated lower-frequency terms alters the highest sector. The top stream coefficient is

    -A_n/[2((4-delta)n+2)].

The stationary bracket therefore gives

    A_n=(-1)^(n-1)(epsilon b_i)^n h_n, h_1=1,
    4d(n-1)h_n = sum_(j=1)^(n-1)
        [8(n-j)/((4-delta)j+2)-1] h_j h_(n-j).

The general highest-sector theorem38, with the normalization117 and asymptotic theorem115, gives h_n>0 and

    h_n R_H^n ~ K n^(-1-1/beta), K>0.

Its parameters are a=2/(4-delta) and beta=6/(4-delta), which are precisely those displayed above. At Q7 they equal7/13 and21/13, with4d=8/5. At Q8 they equal8/15 and8/5, with4d=4/3.

## Failure at and below the necessary threshold

Every b_i is nonzero because its irreducible compatibility polynomial has degree2Q>1. At the displayed threshold, the highest Fourier coefficient of the weighted second angular derivative of the nth density term has modulus asymptotic to a fixed positive constant times

    n^(1-1/beta)=n^((Q+1)/(3Q)).

It does not tend to zero. Fourier extraction is a bounded linear functional on uniform angular functions, so uniform termwise convergence is impossible there. At any smaller r, the same coefficient also grows exponentially. This proves the strict necessary inequality. The argument uses absolute values and therefore includes both signs of b_i and epsilon.

## Verification protocol and dependencies

Compute every h_n through2Q exactly and compare its monomial coefficient with the separately generated Cartesian polynomial prefix. Evaluate R_H and every root-dependent bound twice, at512 and1024 bits, refining each exact root enclosure afresh. Retain directed decimal bounds, exact dyadic ball encodings, input hashes and actual elapsed time. No fitted tail growth is used.

Dependencies:38,115,117,170,253,256. The finite arithmetic of the necessary constants can be checked independently of all-order convergence; a convergence claim at the corresponding center uses the separate admitted certificates.

## Completed directed constants

All30 highest-sector coefficients through2Q agree with the exact Cartesian polynomials. Fresh512-bit and1024-bit root/gamma evaluations overlap. Every decimal lower bound in the independent18:42Z derivation lies strictly below the directed enclosure. The base radii are R_H=0.91368025953574548913... for Q7 and0.76889062508510007962... for Q8.

| Q | Increasing root | Certified necessary radius constant, rounded down |
|---|---:|---:|
| 7 | 1 | .3441017 |
| 7 | 2 | 5.956143e-5 |
| 7 | 3 | 5.740541e-7 |
| 7 | 4 | 6.838151e-6 |
| 7 | 5 | 1.009437e-4 |
| 7 | 6 | 4.448449e-4 |
| 7 | 7 | 1.261427e-3 |
| 7 | 8 | 3.379089e-3 |
| 7 | 9 | 1.098633e-2 |
| 7 | 10 | .1014339 |
| 8 | 1 | .7213489 |
| 8 | 2 | 1.110938e-4 |
| 8 | 3 | 5.257627e-7 |
| 8 | 4 | 1.962667e-5 |
| 8 | 5 | 9.601229e-5 |
| 8 | 6 | 2.893045e-4 |
| 8 | 7 | 7.775502e-4 |
| 8 | 8 | 2.179840e-3 |
| 8 | 9 | 8.234541e-3 |
| 8 | 10 | .1127887 |

Multiply each entry by |epsilon|^(Q/2). These lower constants are weaker than the exact strict thresholds in the statement. They do not determine a convergence boundary.
