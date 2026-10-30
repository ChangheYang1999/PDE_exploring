# Reciprocal acceptance of the dual and divergence-free reviews

Written UTC 2026-10-29T16:16:24.778038+00:00 before the finite checker. This accepts the T1/T3 theory worker review set 46, R1-048 and R1-049, read in full with both independent scripts and their full output. It is the second Opus review of T4-469, after the T2 review accepted by T4-475. The original theorem and numerical inputs retain their hashes.

## Exact statements and domains

Let F be real and locally integrable on R2, with finitely many positive sine modes and rF in L2. Define H(F) as the dual norm on the gradient completion of C_c^infty(R2), using Lebesgue measure. Let psi be smooth, in this completion, have finitely many positive sine modes, and have grad psi and r Delta psi in L2. The angular field A_F=-e_theta r sum f_n cos(n theta)/n belongs to L2, and div A_F=F in distributions. For Z=A_(Delta psi)-grad psi, a=||Z||2^2, b=<A_F,Z> and M2=||A_F||2^2,

 H(F)^2<=M2+2tb+t^2a for every real t,
 H(F)^2<=M2-b^2/a if a>0.

Distinct individual frequencies give an additive sum of b_i^2/a_i; tests at a common frequency need their full Gram matrix. M2 always includes the entire source. These are norm bounds, with no assertion about an IPM inverse or existence.

For any finite set of compactly approximable gradient tests psi_i of distinct angular frequencies, with absolutely convergent p_i=int F psi_i and d_i=||grad psi_i||2^2>0, one also has H(F)^2>=sum p_i^2/d_i. This lower bound does not require a prior assumption H(F)<infinity. Applied to the fixed candidate C1-N1-016-legqs25-quot013 with the accepted N4-396 pairings and energies, it gives H(016)>0.529469576110512066428681. The accepted complete G0,G1,P2 bounds then give E2(016)>608.392385921614>606.820219>E2(007), for the identical four-component E2 definition.

## Analytic proof and the reciprocal review

For compact smooth phi, angular integration on each annulus gives -int A_F.grad phi=int Fphi. Cauchy-Schwarz and local integrability let the inner radius tend to zero; the outer radius can exceed the support. There is no radial flux or contact distribution. The same identity for Delta psi implies div Z=0. Expanding ||A_F+tZ||2^2 and completing its quadratic square proves the upper bounds. Orthogonality of both polar components proves the distinct-mode rule.

With psi=u(r)sin(n theta), v(y)=u(exp y), direct differentiation gives Z_r=-v' sin(n theta)/r and Z_theta=-v'' cos(n theta)/(nr). Thus

 a/pi=int(v'^2+v''^2/n^2)dy,
 b/pi=n^-2 int r f_n(r) v''(log r)dr.

The second integral converges by Cauchy-Schwarz in dy. Angular Hardy gives ||psi/r||2<=||grad psi||2. Consequently int|Fpsi| is finite. The gradient-completion identities imply <A_F,grad psi>=-p and <A_(Delta psi),grad psi>=d, hence a=||A_(Delta psi)||2^2-d and b=<A_F,A_(Delta psi)>+p. All signs in R1-049 agree. If F=-Delta psi, b=-a and the upper is the exact H(F)^2=d.

For g=F+Delta psi the Riesz representative is Phi-psi, where Phi represents F. Therefore H(F)^2=2p-d+H(g)^2. Linearity of A gives ||A_F+Z||2^2=2p-d+||A_g||2^2. In particular the latter bound is the t=1 case for every admissible psi. Optimization improves it by exactly (a+b)^2/a. The review's added identity is correct and does not need a Galerkin equation.

For the lower bound, radial cutoffs of each exact trial have gradient error squared O(R^(6-4 beta_min)), tending to zero since every declared beta>3/2. Origin regularity follows from 3+2k>=n with even difference. Dominated convergence for Fpsi extends duality to these tests. Optimize the linear combination with coefficients p_i/d_i. Its gradient norm squared and pairing both equal sum p_i^2/d_i, proving the lower bound without a hidden completeness assumption.

The review's third method for candidate energies is correct: for m(a,s)=r^a(1+r^2)^-s and L=r d/dr,

 Lm=a m(a,s)-2s m(a+2,s+1),
 L2m=a^2 m(a,s)-4s(a+1)m(a+2,s+1)+4s(s+1)m(a+4,s+2).

Every product integrates against dy to B((a+a')/2+j+j',beta+beta'-3)/2. The second argument is positive and the first is a positive integer, so these are exact rational beta values. The peer independently computed all 663 trial coefficients and both large rational d/pi and a/pi. This lane checks its bound source hashes against the exact accepted inputs of T4-470 and472; it does not repeat the expensive candidate double sums. The new finite checker derives the displayed differential formula by a second rational polynomial calculation and reconstructs both small manufactured examples. The review's finite candidate energies also have the previously accepted independent T4-472 reconstruction.

## Exact fixtures, inequalities and source scope

The fixtures u_1=r/(1+r2)^(3/2), u_3=r3/(1+r2)^3 have respectively

 d/pi=3/8,6/35; a/pi=3/8,2/63; M2/pi=3/4,64/315.

For F=-Delta(psi_1+psi_3), H(F)^2/pi=153/280. Correcting only mode1 gives upper1457/2520 and positive gap2/63. These follow by t=r2/(1+r2), w=1-t, u=r w^b P(t), D_bP=(1-2bt)P+2t(1-t)P', and the rational moment int t^j w^q=j!/product(q+i). The checker reconstructs the polarized d,a,M,b,p from these moments. It checks the scalar optimum, residual identity and the exact improvement (a+b)^2/a on additional rational tests. These fixtures have known H values, unlike the actual candidate.

R1-048 retains the full-precision pairing premise. T4-472 has already summed every650-digit archived group from N4-399 at4096bits, with all four pairings accepted. The old200-digit displays are still insufficient. The new acceptance binds that exact archive acceptance and the same raw candidate hash; it does not replace the pairing premise by agreement of peer decimal displays. The exact E2 separation is1.572166921614. The ordering is pairwise and implies nothing about the minimizer among all snapshots or the distance to a stationary profile.

R1-049 V9 uses unaccepted N3 mode Hardy displays only as a CONDITIONAL consistency observation. Neither their overlap with lower bounds nor an interval containing zero independently validates a norm. The complete-prefix certificate accepted in T4-476 now supplies a separate actual whole-field upper H(016)<0.944107, E2(016)<722.969. That upper includes every omitted angular mode through the accepted full rF norm. It does not depend on the N3 displays and does not require all160 mode integrals to finish.

## One source-exponent description needs correction

R1-049 V6 describes its FLOAT positive-pole fixture as f=r w^(7/10)A(t). The reviewed script instead sets delta_e=7/5 and actually evaluates f=r w^(7/5)A(t). Its comment and the printed comparisons must be attributed to exponent7/5. This is a transcription error in a FLOAT example, not a failure of formulas(8) or(11), and no candidate certificate depends on it. The checker parses the literal assignment without executing the peer script and records the mismatch. All mpmath quadrature comparisons remain FLOAT. No new field integral, model call, server, JavaScript/TypeScript, cluster or remote computation is used.

## Verification evidence and conclusion

The manifest freezes the complete review, both scripts, both output logs, and the accepted dependency hashes. Exact parameters are in JSON. The finite checker will record real runtime and its complete checks. CONFIRMED: the reciprocal analytic review, exact fixtures, candidate pairing-chain composition and pairwise E2 ordering under their stated premises. REFUTED: the exponent7/10 attribution of the particular FLOAT code fixture. OPEN here: N3's narrower two-sided displays, any global inverse and existence closure. Existing Opus collaboration uses T1/T2 files, configured us.anthropic.claude-opus-5-5; actual provider identity is unobservable.
