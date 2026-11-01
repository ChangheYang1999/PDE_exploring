# Enclosure induction for the delta3/5 tuned producer

Status: PROVED after independent theory-part review, V440; all four source checkpoints pass the artifact hypotheses V430. The final untuned stream harmonic remains excluded.

## Statement and hypotheses

Fix delta=3/5, c=5/2, and one of the four exact real roots b of the degree-ten first-obstruction polynomial in200. Let f_1=sin(theta)+b sin(3theta). The all-index response certificate in200 gives the unique formal tuned branch and a uniformly nonzero response sequence. Assume the numerical initial coefficient intervals contain f_1, the parameter intervals contain delta and c, and the retained TunedGeneral producer uses outward-rounded arithmetic throughout. Require every nonresonant denominator interval and every tuning-response interval used in division to exclude zero. No coefficient interval may be replaced by its midpoint or narrowed without an exact identity.

Then each completed numerical block encloses the uniquely tuned coefficients of that branch. If the checkpoint stops at a resonant order n before H_n is chosen, the density and the nonkernel stream coordinates remain enclosed, but the provisional kernel value0 need not enclose the tuned stream. A full stream norm at that order must be excluded or completed with a certified harmonic.

## Definitions and exact block argument

Put p_n=1-3n/5 and lambda_n=3(n-1)/2. For angular functions define

    T_(i,j)(g,f)=(p_i+1)g f' - p_j g' f.

Resonances occur at n=10k, k>=1, at stream frequency6k-2. Write e_n=sin((6k-2)theta) and g_n=g_n^part+H_n e_n. Coefficients of smaller order and f_n are independent of H_n.

For1<=i<=10, let phi_i be the change in f_(n+i) per unit change of H_n. Its exact recurrence is

    lambda_(n+i) phi_i = T_(n,i)(e_n,f_i)
      + sum_(m=1)^(i-1) [T_(n+m,i-m)(Pi_(n+m)phi_m,f_(i-m))
                         + T_(i-m,n+m)(g_(i-m),phi_m)],

where Pi is the nonresonant stream inverse. All n+m with1<=m<10 are nonresonant. The first changed density is f_(n+1), and the first changed stream is g_n. Thus a product containing two changed factors has order at least2n+1>n+10 for every n>=10. The exact coefficients through n+10 are affine in H_n. Collecting the terms with exactly one changed factor gives the displayed recurrence, with both possible positions included once.

Compute a provisional continuation with H_n=0, denoting its density by f^0. Let R_k be the coefficient of sin((6k+3)theta) in f^0_(n+10), and let sigma_k be that coefficient in phi_10. Then

    f_(n+i)=f^0_(n+i)+H_n phi_i,
    H_n=-R_k/sigma_k.

The quotient is defined by the nonzero-response theorem. It makes the next obstruction vanish exactly. The first obstruction at10 vanishes because b is a root of the independently certified polynomial. Induction therefore supplies an exact branch and justifies every compatibility identity used when the producer sets a resonant coordinate to H_n. Merely observing that a computed ball contains zero would not supply this justification.

## Interval induction

The initial coefficient and parameter intervals contain their exact values by hypothesis. Suppose a completed prefix does so. Directed finite sums, derivatives and polynomial products enclose the provisional continuation and each response coefficient. Nonresonant divisions are valid because their denominator intervals exclude zero. The directed response quotient encloses the exact H_n. Substituting it into the affine correction encloses the corrected densities; possible dependence among intervals only enlarges the resulting bounds. Recomputing each stream inverse then encloses every nonkernel coordinate. At a resonance the exact compatibility identity already proved allows the kernel coordinate to be filled with H_n's enclosure. This completes the block induction.

The reviewed producer retains all coefficients of each polynomial product, uses both sum and difference frequencies with their factors1/2, and trims only intervals that are exactly zero. Statistical midpoint conversions do not update the recurrence arrays. The variable marking a provisional block permits a temporary zero kernel; that value is subsequently corrected as specified above. The final untuned kernel exception follows directly from the loop order.

## Source and artifact scope

The algorithmic induction uses the same outward-arithmetic operations inspected in194, with the general rational resonance index specialized to numerator3 and denominator5. Artifact checks must separately verify the actual parameter and root containment, agreement with the independent prefix archive, every stored nonresonant denominator, and the nonzero recorded responses. Source hashes identify the inspected versions but do not prove that a checkpoint was produced by those versions. Independent Cartesian prefixes and equation checks provide additional evidence, not a formal proof of the interpreter or interval library.

This result may justify source-bound finite norm enclosures when its artifact hypotheses pass. It does not convert a finite root test into an optimal convergence radius. The separate theorem200 establishes existence of an exterior radius; explicit bounds are supplied in204 and205.
