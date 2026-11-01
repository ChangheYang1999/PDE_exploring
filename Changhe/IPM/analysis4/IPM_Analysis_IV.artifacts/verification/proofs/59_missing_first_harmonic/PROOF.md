# Resonance tests without a first sine harmonic

Status: CONFIRMED for the exact finite decisions below. No all-prime incompatibility theorem is asserted for these inputs.

## Exact question

At a prime p>=5 and an even numerator 4<=a<p, let delta=a/p. The first stream resonance occurs at order p, with stream frequency a-2. Its compatibility coefficient is the sine amplitude at frequency a-3 of the density f_p. Denote it by kappa.

For the input f_1=sin(theta), the confirmed prime theorem gives kappa=(-1)^((a-4)/2) modulo p. For f_1=sin(M theta), with odd M>=3, that proof only implies kappa=0 modulo p when its integrality hypotheses hold. Divisibility by p does not imply exact compatibility. The present calculation recomputes the exact rational kappa and its p-adic valuation for fixed higher harmonics.

## Method and proof of each finite decision

Use the independent Laurent-Cartesian recursion from topic24 with exact rational arithmetic. At every order below p, solve Poisson by dividing the independently differentiated density coefficients by their nonzero exact multipliers. Form the next density from the ordered Cartesian velocity-gradient products. At order p, retain the complete density and evaluate the resonant Poisson forcing. Its exact value must be -(a-2)kappa.

If the exact rational numerator of kappa is nonzero, the first pure stream resonance is incompatible for this particular parameter and input. If it is zero, the first resonance is compatible; later resonances and the pure potential gauge require separate investigation.

For a nonzero reduced rational kappa=u/v, repeatedly remove factors of p from u and v. The difference in counts is its exact p-adic valuation. Reducing the remaining units modulo p gives the normalized residue. These are integer arithmetic decisions. Every completed case retains the full terminal density, exact kappa, code hashes, and real elapsed time.

The scan is evidence about its exact listed finite cases. It does not prove incompatibility for all rational parameters, all primes, or all profiles lacking a first harmonic. The support-selection examples in topic25 already show that some sufficiently high harmonics have a compatible first resonance.

## Completed results

All103 prescribed cases were completed. The scan used every even numerator4<=a<p and the indicated primes.

| Leading harmonic | Prime range | Cases | First incompatibilities | First compatibilities |
|---|---|---:|---:|---:|
| sin3theta | 5<=p<=31 | 64 | 64 | 0 |
| sin5theta | 5<=p<=19 | 27 | 27 | 0 |
| sin7theta | 5<=p<=13 | 12 | 11 | 1 |

All nonzero coefficients have p-adic valuation1 except the sin3 cases (p,a)=(7,4),(17,6),(31,22), which have valuation2 and normalized unit residues6,13,7 respectively. In particular, the assertion that all higher-harmonic obstructions are nonzero modulo p squared is false. The explicit first counterexample is

    kappa(sin3,delta4/7)
      = 4269138803176105369138355721
          /319955931723614529404272640000.

The unique first-compatible scanned case is sin7theta at delta4/5. Topic25's support rule proves this without computation: at n5 every signed density frequency has absolute value at least7-4=3, whereas the tested frequency is1.

## Exact continuation of the compatible case

At delta4/5, c5 and f_1=sin7theta, the first stream resonance is n5, p_5=-3, P_5=-2. Let beta denote its free stream amplitude at sin2theta. The next resonance is n10, at stream frequency6 and density frequency5. Its coefficient kappa_10(beta) is affine in beta. Indeed each occurrence of the free stream costs order5 and any density term has at least one leading-density leaf, so a term quadratic in beta has order at least11.

Four separate exact Cartesian runs compute beta0, beta1, the affine root beta_star, and the beta forced by a pure potential at order5. The retained exact rational results show:

- kappa_10(0) is nonzero and its affine slope is nonzero;
- beta_star is approximately0.0008438508931344587 and cancels the second stream obstruction exactly;
- a pure even degree-zero potential at n5 forces beta_pure approximately-5.010395324102969e-7;
- beta_pure differs from beta_star and gives kappa_10 approximately-1.6439655973893495e-8, which is exactly nonzero.

The pure-potential condition is obtained independently. Write Delta chi=r^(-2) sum D_k cos2k theta. At p=-3 the downward relation is a_(2k+1)=(k+1)D_k+kD_(k+1). Set the absent top coefficient to zero and solve downward. Then chi has cosine coefficient -D_k/(4k squared), up to an irrelevant constant, and its sin2theta stream amplitude is D_2/8. Direct differentiation checks both rho and psi against this potential. The first compatibility a_1=0 is necessary and holds here.

The tuned beta_star can be realized by adding a multiple of log r to the potential, as in topic36. It only cancels the next stream obstruction. This calculation asserts neither later compatibility nor convergence. In the strictly pure-potential ansatz, the first free stream amplitude is already fixed and the second resonance is obstructed.

## Evidence and actual computation time

Each scan case retains its full terminal density and exact compatibility coefficient under verification/. The complete scan took154.14784931577742 actual seconds, with153.9256272651255 seconds inside the case calculations. The four continuation runs took0.22309318277984858 seconds. These finite computations are independent of the numerical experiments. Sources and their hashes are retained alongside the results.
