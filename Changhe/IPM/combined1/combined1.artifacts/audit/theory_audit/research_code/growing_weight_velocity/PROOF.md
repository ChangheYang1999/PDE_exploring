# Growing radial weights in the S1 velocity estimate

Status: new extension, OPEN pending an independent theory review. The proof uses the audited odd decreasing-weight Beurling estimate T4-054. It answers the S1 question in T2's the review of T4-094, addition A5.

## Exact statement

For R>0 and real p put w_p(X)=(1+|X|^2/R^2)^(p/2). The complex centrally odd space consists of functions f with f(-X)=-f(X). The Beurling operator B has Fourier symbol (xi1-i xi2)^2/|xi|^2. If |p|<2, its exact norm on this weighted space is

    ||B||_(L2(w_p^2),odd) = (2+|p|)/(2-|p|).             (1)

For real centrally odd h, including the real S1 subspace,

    ||w_p U[h]||_2 <= 2/(2-|p|) ||w_p h||_2.             (2)

The vector norm on the left sums both velocity components. On the real S1 space the existence of any finite constant in (2), not necessarily the displayed constant, is equivalent to |p|<2. The value in (2) is an upper bound; its sharpness on S1 is not claimed.

These are canonical operators extended from compact smooth odd functions. No new correction-space inverse or energy estimate follows merely from these velocity bounds.

## Proof for the growing weight

For p=-a with 0<a<2, (1) and (2) are the audited result T4-054. Multiplication by a radial positive weight preserves central oddness. Let J denote complex conjugation on physical-space functions. The Fourier multiplier of B is even. Consequently

    B*=J B J.

Indeed the Fourier transform of Jf at xi is conjugate(hat f(-xi)), and conjugating the even symbol of B gives its complex conjugate, the adjoint multiplier. J is an antiunitary isometry in every real radial weight, so B and B* have the same norm in each such weighted space.

For compact smooth odd f,g, unweighted duality gives

    <w_a B w_a^(-1) f,g>
      =<f,w_a^(-1) B* w_a g>.

The decreasing-weight estimate applies to the right-hand operator, with weight w_a^(-1)=w_-a, and gives its norm K=(2+a)/(2-a). Thus the left-hand operator extends with norm at most K. Conversely, its adjoint is exactly the bounded operator w_-a B* w_a. The equality follows first on the dense compact test class and then by continuity. Adjoint operator norms agree, and the latter norm is exactly K by T4-054 and conjugation. This proves (1) for p=a. For p=0 it is the ordinary unitary multiplier identity.

For real h the exact canonical identity is

    U2[h]+i U1[h]=-(I+B)h/2.

Its modulus is the Euclidean velocity magnitude. The triangle inequality and (1) give (2), including its identity-operator contribution. In particular the local/contact term has not been omitted.

## Necessity of the range on S1

Choose a nonzero, nonnegative, smooth radial function eta with compact support and let h(x,y)=y eta(x,y). This is S1 and belongs to every weighted input space. Its zeroth moment and x first moment vanish, while

    M=int y h(x,y) dxdy=int y^2 eta(x,y) dxdy>0.

Outside the support, the kernel of U2=R1^2 is

    K2(X)=(x^2-y^2)/(2pi |X|^4).

Taylor expansion in the compact source variable yields uniformly in angle

    U2[h](X)=-M partial_y K2(X)+O(|X|^-4)
             =M sin(3theta)/(pi |X|^3)+O(|X|^-4).        (3)

The local term vanishes there. On an open angular interval with sin(3theta) nonzero, (3) has size bounded below by a positive multiple of r^-3. Therefore its weighted squared integral diverges like int r^(2p-5)dr whenever p>=2. This rules out any finite velocity constant for p>=2.

For p<=-2, suppose a finite velocity bound existed. Then its U2 component would be bounded on real S1 L2(w_p^2). U2 is self-adjoint in the unweighted pairing and preserves S1. The preceding duality argument would make it bounded on S1 L2(w_-p^2), contradicting (3) because -p>=2. Thus p<=-2 is also excluded.

This proves the equivalence without invoking an unrestricted A2 theorem. In the full space, without the odd moment cancellation, the monopole r^-2 tail gives the familiar smaller interval. The parity assumption is substantive.

## Full-space comparison, proved by the same blocks

On the unrestricted complex space, the same angular reduction has n=m-1 in all integers. Its first positive index is n=1. The positive-square identity of T4-054 therefore gives the exact full-space Beurling norm (1+|p|)/(1-|p|) for |p|<1, with sharpness from the n=1 annular sequence and growing weights obtained by duality as above. Consequently a valid real full-space velocity bound is

    ||w_p U[h]||_2 <= 1/(1-|p|) ||w_p h||_2, |p|<1.

For necessity, choose a nonnegative radial compact smooth h of positive mass M0. Outside its support U2[h]=M0 K2+O(r^-3), with a nonzero r^-2 angular leading term. The weighted squared integral diverges for p>=1. Self-adjoint duality excludes p<=-1. Thus the full-space admissible interval is exactly |p|<1. This supplies the specific power-weight conclusion of T2 addition A5 directly, without invoking the general A2 characterization.

The identity in that addition has a sign typo. Since R1^2+R2^2=-I,

    R1^2=-I/2+(R1^2-R2^2)/2.

Its printed minus sign before the difference is incorrect. This typo does not change its conclusion about the full-space interval.

## Consequence for graded energy bookkeeping

A level whose differentiated unknown is centrally odd may use a growing weight with exponent1<=p<2 and the explicit constant in(2). A differentiated S1 function need not remain centrally odd: even total derivative orders preserve central oddness, and odd orders produce central evenness. Therefore (2) must not be applied indiscriminately to every row of a derivative hierarchy. A row acting on an even differentiated quantity needs its own parity or moment argument.

For example, this lemma permits p=3/2 on the undifferentiated S1 variable, with velocity constant4. It does not repair the independent divergence of w D2rho at p=3/2 for the case4 background, and does not repair a growing residual sector. Those are different hypotheses.

Dependencies: audited T4-054, density of compact smooth parity tests in radial weighted L2, Hilbert-space duality, and the displayed multipole Taylor calculation. No external sharp-constant theorem is imported.
