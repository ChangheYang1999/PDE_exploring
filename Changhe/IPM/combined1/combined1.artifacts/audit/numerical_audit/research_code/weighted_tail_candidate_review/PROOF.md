# Independent exact weighted-tail comparison for six candidates

## Exact statement and correction class

Fix c=4076476460239181/2251799813685248, gamma=1/c and delta=1-gamma.
Let rho be one of the immutable candidates006,008,009,012,013,014 listed
by full ID and raw hash in the verification record. Every input is the
smooth finite potential family in ../generator_sector_audit/PROOF.md,
with canonical u=(-chi_xyy,chi_xxy) and rho=-chi_xxy-chi_yyy. Set

    E_a=L2(R2,(1+r^2)^(-a)dX),  -2<a<=1+gamma.

Under the canonical weighted-velocity convention and distributional
stationary equation in the frozen T4 weighted-forced-tail theorem, a
correction h in E_a can exist only if every residual coefficient at an
exponent q>=a-1 vanishes. The theorem includes equality. Its weighted
velocity extension retains the local identity term, and on real S1
inputs satisfies ||U[h]||_E_a<=2/(2-|a|)||h||_E_a. This audit applies
that separately audited theorem. It independently checks the complete
candidate coefficients and the threshold, rather than re-proving the
weighted multiplier theorem.

For each of the six candidates the proposed result is that the genuine
first nonzero residual sector is (K,L)=(4,1), with

    q_*=1-4delta-2=4gamma-5
       =-11375183046454913/4076476460239181.

If the exact checks succeed, its affine E_a class contains no stationary
S1 solution for -2<a<=q_*+1=4gamma-4. Above this exact rational threshold,
up to1+gamma, this necessary tail test gives no obstruction. It does
not prove existence. No rounded decimal enlarges the excluded interval.

The six complete density and stream profiles of exponents e_j=gamma-jdelta,
j=0,1,2,3, are also compared with candidate007. Their equality, and the
strictly lower omitted exponents, imply equality of the affine L2 classes.
This does not identify distances from the different reference points.

## Independent raw-generator expansion

For each raw generator extract its exact first two radial coefficients
at infinity using ../multiscale_generators/PROOF.md. In the unscaled
case these agree with P(1) and pP(1)-P'(1), but the own implementation
starts directly from its generator indices and rational coefficients.
It differentiates the homogeneous cosine potential with the Cartesian
frequency recurrences dx and dy. This gives full density, stream,
velocity and density-gradient coefficients, with exact negative-mode
signs and no angular quadrature.

Use the own index(h,l)=(K-1,L), whose density exponent is
alpha(h,l)=gamma-hdelta-2l. For every h=0,...,8 and l=0,1 retain the
linear term(c alpha-1)Theta and all Cartesian products
u1_i (rho_x)_j+u2_i (rho_y)_j with i+j=h-1 and descendant indices
summing to l. Compare the complete resulting rational angular map
coefficientwise with the independently derived T4 polar map. Compare
all density and stream maps as well, and check every angular Poisson
identity

    [partial_theta^2+(alpha+1)^2]Psi
              =-alpha cos(theta)Theta+sin(theta)Theta'.

Thus agreement includes every coefficient, zero or nonzero, in all18
retained sectors. The full first nonzero-sector set and exact exponent
are compared, and its squared full-circle norm is pi times the sum of
squared sine coefficients. An Arb norm overlap is an additional check;
it does not replace the rational identities.

## Completeness and theorem application

An omitted K>=10 term has exponent at most1-10delta<-3. An omitted
L>=2 term has exponent at mostgamma-4<-3. The finite rational radial
factors are analytic in r^-2 for all sufficiently large r, and can be
differentiated through every fixed order there. Their remainder and
the retained nonlinear products are therefore uniformly of order
O(r^(-3-epsilon)) for a positive exact epsilon. This remainder is in
E_a for every a>-2. Distinct labels in the retained prefix have distinct
rational exponents. A largest nonzero term has positive angular L2 norm
and cannot cancel against the lower terms. The prefix consequently
contains every residual sector at or above a-1 for the entire stated
range, with an independently checked omitted-exponent bound.

To see why this is a correction obstruction rather than merely a test
of residual membership, test the correction equation on the annulus
L<r<2L with L^-1 eta(r/L) times the leading residual angular profile.
Its reference pairing is L^(q_*+1)(A+o(1)), A>0. With m_L and n_L the
weighted annular L2 norms of h and U[h], respectively, the four
correction terms are O(L^a m_L), O(L^(a+gamma-1)m_L),
O(L^(a+gamma-1)n_L), O(L^(2a-2)m_L n_L). Both norms tend to zero.
When q_*+1>=a, division by the reference power makes every correction
vanish because gamma<1 and a<2. This contradicts A>0, including the
equality endpoint. These are exactly the hypotheses and bounds of the
frozen audited theorem and its Opus review.

## Source and verification scope

The T4 exact sector files are frozen losslessly with gzip; canonical
inputs reuse byte-identical files already retained in this lane. Both
decoded and retained hashes must equal the peer's original hashes before
parsing. Each canonical map must equal the independently
verified own map and share its raw-source identity. Every own snapshot
hash is rechecked. The peer code and proofs are copied and inspected
as data; no foreign code is imported or executed. The output binds
this proof, both prior analytic proofs, the Opus review, all immediate
candidate inputs, and all executed own code. Failure aborts without
an acceptance. No inverse, quantitative smallness or existence result
is inferred from these exact sector identities.
