# A necessary radius for the Candidate-shaped compatible profiles

Status: PROVED in V501 after independent review and the directed constant checks V489. The result is a necessary radius only.

## Statement

Let delta=4/9 and c=9/5. Let a_1,...,a_19 be the exact odd sine coefficients extracted from Candidate007 in02. Set alpha=a_19/a_1>0. Consider any of the seven compatible profiles of156, normalized by the original a_1, with only its third-harmonic coefficient replaced by the indexed compatibility root. Multiply the whole profile by a nonzero real epsilon.

Set

    a=9/88, b=171/88,
    R_H=(16/5)[a Gamma(a) Gamma(b)/Gamma(a+b)]^(88/9).

Uniform termwise convergence with two angular derivatives on a closed exterior r>=R requires

    R>(alpha |epsilon|/R_H)^(9/4).                  (1)

This necessary condition is common to all seven roots. It is not a sufficient radius or a claim that the complete series is singular at its boundary.

## Proof

Each leading profile has maximum frequency19 and identical coefficient epsilon alpha there. The Fourier bandwidth bound is20n-1 at density order n. Only the two highest input frequencies can reach this highest output frequency in a nonlinear product. Lower initial harmonics cannot contribute to it. A tuned stream harmonic at order9k has frequency4k-2, strictly below the highest possible stream frequency180k, and likewise cannot affect any subsequent highest density coefficient. These are the triangular highest-frequency identities established in38 and170.

The normalized highest density coefficient is therefore

    A_n=(-1)^(n-1)(epsilon alpha)^n h_n,

where h_n is the universal positive scalar sequence with B=20, eta=B-delta=176/9 and d=delta/(1-delta)=4/5. The admitted asymptotic theorem115, with its corrected normalization117, gives

    h_n R_H^n ~ K n^(-1-88/171), K>0.

At r=(alpha |epsilon|/R_H)^(9/4), the magnitude of the highest Fourier coefficient in the second angular derivative of the nth density term is asymptotic to a positive constant times n^(83/171). It fails to tend to zero. Fourier coefficient extraction is a bounded functional on continuous angular functions, so uniform termwise convergence of these derivatives fails there. Below this radius even the undifferentiated highest coefficient grows exponentially. This proves the strict necessary bound (1).

The exact ratio alpha is fixed by the authoritative coefficient extraction. A separate directed-arithmetic calculation will enclose the gamma expression and the radius and check the displayed approximate numbers. Changing only the third harmonic does not change alpha. The normalization of epsilon is essential: epsilon multiplies the profile after division by a_1.

Dependencies:02,38,115,117,156,170. No numerical fit is used in the proof.
