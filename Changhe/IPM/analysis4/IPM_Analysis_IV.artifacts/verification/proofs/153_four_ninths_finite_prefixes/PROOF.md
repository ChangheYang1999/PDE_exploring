# Independent finite tuned prefixes at delta=4/9

Status: all five finite constructions and fifteen independent response comparisons CONFIRMED in V298. No new infinite-series conclusion is inferred from these prefixes.

## Exact statement

For delta=4/9 and each exact real root b_i of the degree-nine obstruction polynomial in146, set f_1=sin(theta)+b_i sin(3theta). Construct the pure density and stream coefficients through order27. At each resonance n=9,18,27, choose the free stream coefficient H_n by enforcing the next density compatibility at n+9. The desired finite certificate checks the original Cartesian recurrence, support, symmetry and compatibility, together with the Q-step response values already computed independently in149.

The frequency support is at most4n-1 for density and4n for stream. The resonant stream frequencies at9,18,27 are2,6,10. The corresponding density obstructions are sin(theta), sin(5theta), sin(9theta). Determining H27 uses a provisional continuation through36, but the final reported prefix ends at27.

## Argument for the finite construction

Represent each sine polynomial by the signed Laurent polynomial sum_m a_m(z^m-z^(-m))/2. For radial degree p, its Cartesian derivative operators are

    Xz^m=(p+m)z^(m-1)/2+(p-m)z^(m+1)/2,
    Yz^m=(p+m)z^(m-1)/2-(p-m)z^(m+1)/2.

The physical derivative in y contributes an additional factor i, so the stream equation is -XXg+YYg=Xf. The transport coefficient is XgYf-YgXf. These formulas independently determine the finite recurrence without sine-product convolution identities.

At a resonant order n, form two separate provisional continuations with H_n=0 and H_n=1. The difference S of their next obstruction values is the exact response. The obstruction depends affinely on H_n because two factors depending on that harmonic first contribute at order2n+1>n+9. Thus H_n=-R/S, where R is the zero-harmonic obstruction. Every S is nonzero by146. After inserting this H_n, recompute the main coefficients from their fixed lower orders. The first obstruction vanishes by the exact algebraic identity for b_i. Each later obstruction then vanishes by the preceding affine correction. This inductively establishes the unique finite compatible prefix.

Exact rational bisection encloses each root. Outward-rounded interval arithmetic encloses every Cartesian sum, product and nonresonant inverse. Dividing by an interval separated from zero encloses the exact harmonic. Projection of a known structural zero is justified by the exact identities above, and its incoming interval must contain zero. Support and reflection projections are checked coefficientwise. The independently defined linear response in149 must overlap each two-continuation response at k=1,2,3.

## Evidence and limits

Save the exact root intervals, all norm and harmonic enclosures, interval check counts, independent response comparisons, source hashes and actual elapsed time. The finite root tests describe only these exact prefixes. Infinite convergence requires145 and its separate all-index response hypothesis; finite decreasing or increasing norms do not replace that argument. No whole-plane extension is asserted.

## Completed verification

On 2026-10-31T11:35:53+00:00, the retained run completed in27.042990491259843 seconds. For each of the five profiles, all13274 support checks,6478 symmetry checks,3 compatibility projections,12933 Poisson coefficient checks and1539 ordered products passed, using6 provisional continuations. The density norm roots at order27, in increasing root order, are approximately0.2323291984,0.3114084823,0.7144001659,1.3221176290,7.1213105866. Exact outward enclosures are in verification/checks.json. These finite root tests are not convergence-radius estimates.
