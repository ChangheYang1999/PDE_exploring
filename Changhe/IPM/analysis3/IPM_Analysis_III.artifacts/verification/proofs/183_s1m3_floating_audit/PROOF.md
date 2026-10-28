# Accounting and interpretation of the S1M3 floating section

## Claim and scope

S1M3 is the numerics team's completed full-angular, two-remainder-mode finite section of S_1=T_R+C_R in the original remainder norm R=L2(w_a), a=17/4. It has84 columns:42 radial functions for each of the angular factors

 p(theta)(cos(2theta)+1), p(theta)(cos(4theta)-1),
 p(theta)=cos(theta)^2 sin(theta).

All assertions here concern the stored floating quadrature matrices and their accounting. A generalized singular value of those matrices is not a certified singular value of the exact differential operator. It also does not prove infinite-dimensional injectivity or any complement inverse. This audit independently reconstructs the matrix sums, verifies exact cell IDs, compares the one-mode restriction with the earlier S1 run and inspects the better-conditioned spline subspace.

## Correct assembly and the defect

Every worker's final part contains its cumulative matrix contribution for its processed cells. The legacy final parts here do not themselves store cell IDs. Their IDs are reconstructed from the recorded full1569-cell run, the original four-worker round-robin assignment, all four completed worker counts and their stored checkpoint prefixes. New parts written after the repair store their IDs directly. Its last checkpoint is a prefix of the same contribution. Therefore a never-resumed run with disjoint final parts covering the expected cell set is assembled by summing those parts exactly once. Adding their retained checkpoints counts those cells twice and changes the quadrature functional. Unless every cell is duplicated with the same multiplicity, this is not even a uniform scaling of the two Gram matrices.

This is the same exact accounting issue proved in proof 176. The unchanged default assembler used for the12:31 S1M3 result sums parts, bases and checkpoints indiscriminately. Its output does not represent the intended section. The separate parts-only robustness script has correct accounting for this never-resumed run once the stated coverage is checked. Generic resumed-run correctness remains subject to proof 176's base accounting repair.

## Matrix comparison and subspace interpretation

For a fixed coefficient vector x, the computed Rayleigh quotient is sqrt(x^T B x/(x^T G x)) when both quadratic forms are positive. If rigorous absolute errors e_B,e_G are known and g>e_G, then its exact squared quotient is bounded above by(b+e_B)/(g-e_G), and bounded below by max(0,b-e_B)/(g+e_G). An unproved accumulation estimate is only a sensitivity model. A lower bound for one fixed vector's quotient is not a lower bound for the ordered minimum over all coefficient vectors. Nor does solving the stored double matrix eigenproblem at50 digits remove quadrature, truncation or earlier accumulation errors.

Restricting S1M3 to m=1 should reproduce the independently run S1 matrix up to floating assembly differences, since its radial basis and every image mode are unchanged. This is a useful consistency check with a separate worker run. It does not supply rigorous integration errors.

The two angular factors span different concentration patterns. In exact elementary algebra,

 (cos(2theta)+1)+(cos(4theta)-1)/4=2cos(theta)^4.

Thus the combined subspace contains p(theta)cos(theta)^4 as well as the m=1 profile p(theta)cos(theta)^2. A substantial change after adding m=2 is mathematically possible. It cannot be dismissed solely because the m=1 bulk section had a larger quotient. Locating the sampled minimizing vector and checking the conditioning are separate numerical diagnostics.

Dependencies: proof 176 for checkpoint accounting, topics115 and116 for the scope of finite-section bounds, and the immutable numerical snapshots listed in evidence/check.json. Numerical outcomes will be appended after the independent computation.

## Independent outcome

The final parts account for all1569 cells once, by the legacy assignment reconstruction described above. The retained checkpoints account for1544 of those same cells. The old default assembler therefore duplicates1544 contributions. The parts-only floating recomputation gives, for the full84-column pair, smallest double generalized values2.34428348,2.92071852,3.50111790,3.82825577. Its normalized input Gram condition is approximately6.92e14 and the weakest numerator is below the accumulation sensitivity model. These weak ordered values remain unresolved.

The52-column pure-spline block gives floating values3.455656825,4.247679001,5.460413172,6.941941714. Its normalized Gram condition is approximately4.42e4. Its sampled weakest vector has its largest radial coefficients on sp25,sp23,sp24 andsp22. This is a useful numerical observation, not a certified lower bound.

An additional numerical error was independently identified. The angular helper uses numpy.linalg.pinv for division by cos(theta)^4, including the exact-known low-mode input templates. The exact quotients for m=1 and2 are2sin(theta) and-6sin(theta)+2sin(3theta). With padding lengths531 and533, the computed m=1 quotient differs from2sin(theta) in coefficient l2 norm by3.92434e-8 and1.18335e-7 respectively. The corresponding m=2 errors are2.01925e-7 and2.58254e-7. These error norms were enclosed by interpreting each stored binary coefficient as an exact rational and comparing it with the exact polynomial quotient. The small residual of the least-squares solve does not bound this forward division error without an inverse condition estimate.

This explains the apparent run-to-run mismatch. Let

 I_p=integral_0^(2pi) sin(theta)^(2p)|cos(theta)|^(-1/2)dtheta
     =2 Beta(p+1/2,1/4).

The exact two-template angular Gram has entries4I_1,-16I_2,64I_3. In particular its first diagonal is8 Beta(3/2,1/4). The computed first angular diagonal changes relatively by9.31420509609e-8 when padding531 is changed to533. This predicts the observed relative Frobenius change9.31420500161e-8 between the separately run m=1 input Grams, to better than1e-12. The corresponding output Gram changes by7.40421e-8. Thus the1.3e-12 accumulation-only sensitivity model omits a larger division error. It cannot be read as a total error certificate or used to certify the displayed quotient intervals.

The exact low-degree templates can be inserted directly in future computations. Images require their own controlled division error, even when no angular mode is truncated. The repaired accounting code is audited separately; this evidence snapshots the old computation and does not modify the numerics team.
