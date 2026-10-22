# Weighted residual growth of the higher-tail repair

Date: 2026-10-21. This is an immediate corollary of the already verified
and independently reviewed topics106 and108, not a new numerical run.
Read their PROOF.md files with all mandatory addenda.

## Statement

Let rho_T be exactly the topic106 higher-tail repair and epsilon_T its
canonical stationary residual at c0=1/k, with the admissible cutoff
T>=max(R_b,L,1). In the unitary Fourier convention of topics106 and108,

 liminf_(T->infinity) T^(-(2k+1)) ||r epsilon_T||_2
 >= C_D > 0.0022215507882.

C_D is the exact positive one-test constant in topic108 PROOF(10).
Every norm on the left is finite. There is no evaluated threshold T,
no global asymptotic equality, no monotonicity, and no upper norm bound.

## Proof

The residual is odd in y. For each radius its angular mean vanishes.
Let P be the mean-zero angular primitive, so d_theta P=epsilon_T and
||P(r,.)||_2 <= ||epsilon_T(r,.)||_2 by the integer-frequency Fourier
series. The vector field J=r P e_theta satisfies div J=epsilon_T in
distributions. The finite weighted L2 result of topic106 gives
||J||_2 <= ||r epsilon_T||_2 < infinity. For every compact smooth test,
integration by parts and Cauchy-Schwarz therefore give

 |<epsilon_T,phi>| <= ||r epsilon_T||_2 ||grad phi||_2.

The extension to the homogeneous completion follows by density. Hence
||epsilon_T||_(dot H^-1) <= ||r epsilon_T||_2 for every admissible T.
Multiply by the positive T^(-(2k+1)) and take liminf. The topic108
lower bound on the homogeneous norm gives the statement. Its two
independent computations strictly place C_D above the printed decimal.
This completes the proof.

## Scope and dependencies

This supplies the final weighted norm claim in the lead's V36(e').
The proof is only an implication between existing full scoped results;
no fresh floating estimate or new asymptotic remainder is used. All
pins of both dependencies are rechecked in evidence/verdict.json.
The actual Opus5.5 reviews of those dependencies cover the two used
lemmas. No stationary profile, inverse, nonlinear inequality or decisive
endpoint follows from this growing forcing norm.
