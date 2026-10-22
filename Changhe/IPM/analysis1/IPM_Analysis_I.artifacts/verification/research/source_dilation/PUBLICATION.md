# Topic96: the isotropic dilation corollary is confirmed

Read PROOF.md and ADDENDUM.md together. The final authority is
evidence/verdict.json after its current-file and model gates pass.

For the source auxiliary operator of topics78/92 and every fixed
3.05<=s<=3.1, 0<ell<=1, put D_ell u(Y)=u(P+ell Y). Its conjugate
has w_ell=w(P+ell Y)/ell, q_ell=q(P+ell Y), the same Fourier
multipliers, and exactly the same E_s,a_s,d_s. Its maximal domain
corresponds in both directions. The theorem has no hidden support
radius assumption.

With N_lambda(u)^2=integral(lambda^2+|xi|^2)^s|uhat|^2,
||D_ell u||Hs=ell^(s-1)N_(1/ell)(u). Thus the original auxiliary
inverse has N_(1/ell) norm at most(1+R_ell/d_s)^s/a_s and Hs norm
at most ell^(-s)(1+R_ell/d_s)^s/a_s. Minimize the latter if reporting
an Hs bound. The exact continuous Hs bound attains a minimum; a
finite certified set of scales certifies only the best of those scales.

For f_ell=f(P+ell Y), W_r(f_ell)=(2pi)^(-1) integral
(1+ell^2|xi|^2)^(r/2)|fhat|, while ||f_ell||Hs equals ell^(-1)
times the corresponding weighted L2 Fourier norm. For w_ell add
one further ell^(-1). Anisotropic dilation changes the IPM symbols
and the Frobenius derivative bound; the same theorem does not apply
without a new analysis.

The independent check uses exact symbolic identities, Arb512,
mpmath.iv180, and a third exact-integer root plus Machin-pi method
on12 Fourier-annulus examples. This is an analytic corollary and
norm audit. The lead floating R values are not certified here. No
rank-one denominator, physical global inverse or endpoint follows.
