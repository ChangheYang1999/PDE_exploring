# Conditional reconstruction of the candidate017 norm totals

## Exact statement, hypotheses and notation

Fix the exact candidate C1-N1-017-legqs50-quot013 with source SHA256
7dc30181e2d29c8c9706cf396a1be2334f53b2a19ca00e4fad756ff98ec59114.
Use its canonical residual F=(cX+u).grad rho-rho with
rho=-partial_y Delta chi, u=(-chi_xyy,chi_xxy), and
c=4076476460239181/2251799813685248. The definitions of H,G0,G1,P2,E2
are those of N4-410: real whole-plane Lebesgue norms,
H(F)=sup{|int Fphi|:phi smooth and compactly supported,||grad phi||2<=1},
P2=||(1+4r^2)^(2/5)D2F||2, and
E2^2=P2^2+2^14G1^2+2^18G0^2+(20/21)2^18H^2.

Assume the following source premises, separately from the finite
arithmetic checked here.
C1. F is smooth, in L2, and has precisely the finite odd sine support
n=1,3,...,319 stated by the frozen Hardy record. The actual quantities
q_n=pi int_0^infinity r^3 f_n(r)^2dr lie in that record's rF_n_sq balls.
C2. Each dual trial in the frozen16-mode record is an admissible
homogeneous H1 test and its actual dual quotient is enclosed by its
LB ball. For each residual trial, grad_psi encloses ||grad psi_n||2
and residual_r_g encloses ||r(F_n+Delta psi_n)||2. Each such trial is
smooth with gradient and r Delta in L2 and admits radial cutoff
convergence in gradient norm. Its exact numerator/energy source
integrals are not established by a printed label or by this audit.
C3. The actual G0,G1,P2 are bounded below by the lower endpoints of
the norm_lower balls and above by the upper endpoints of norm_upper
in the frozen norm record, with the indicated identical definitions.

Under C1-C3, the outward displays follow:

 0.6144195987 < H(F) < 0.6165956396,
 605.4068697 < E2(F) < 605.9589546.

Consequently E2(007)-E2(017)>0.8591 under C1-C3 and the already
accepted007 lower bound. This is a conditional norm consequence,
not a conditional existence theorem or a new closure-matrix verdict.
The source premises are OPEN in this audit. They must not be replaced
by the nearby016 certificates. An independent017 replay is queued
separately; even if its16 duals and first two residuals pass, the
remaining source premises need their own evidence.

## Complete informal argument

For each mode, integration in the angular variable yields an L2
vector field with divergence F_n and norm sqrt(q_n)/n. Thus
H(F_n)<=sqrt(q_n)/n. Distinct sine frequencies are orthogonal in the
Dirichlet dual Hilbert norm. This can also be seen by rotating the
weak Poisson equation, or by expanding compact tests in angular
Fourier modes, applying Cauchy-Schwarz to their gradient energies,
and taking limits. Finite support removes any infinite sum issue.
Therefore H(F)^2=sum H(F_n)^2.

For each residual trial put g_n=F_n+Delta psi_n. The identity
H(Delta psi_n)=||grad psi_n||2 follows from integration by parts and
cutoff approximation. The triangle inequality and the angular
bound give H(F_n)<=||grad psi_n||2+||r g_n||2/n. Use this upper for
n<=31, or the smaller angular upper if available. Use q_n/n^2 for
every n>=33. This retains all144 other modes. Squaring and summing
positive upper endpoints gives an upper U2 for H^2. Separately,
each nonnegative lower endpoint l_n of a dual LB ball is a lower
bound on H(F_n). Thus L2=sum l_n^2 <= H(F)^2. These16 frequencies
are counted once each; the nine-beta and eight-beta trials are not
added as if they were different modes.

Insert lower or upper endpoints of C3 and L2 or U2 into the positive
E2 square. Exact squaring verifies the strict displayed H and E2
endpoints. Subtract605.9589546 from the accepted007 strict lower
606.818151 to obtain0.8591964>0.8591. This proves the conditional
consequences. None of these rational inequalities proves C1-C3.

## Finite checks, provenance and limitations

Bind the four frozen N3 data records, their manifest and current
program texts, the exact source, the own queued-replay proof and
its proof-first receipt, and accepted007 bounds. Read both program
texts, but do not execute or import them. Reconstruct sums and
bounds with exact decimal endpoint arithmetic. Use directed squares
to verify the coarse published endpoints. Check all160 mode labels,
the16 selected frequencies, the common source and the exact c/delta.
Check internal numeric consistency of stored total balls and primitive
per-mode balls, explicitly as consistency only. Short stored strings
cut off before their closing bracket are diagnostic labels and must
never be parsed as interval certificates. A long decimal string for
an upper endpoint is a proposed bound, not an outward ball by itself.

The frozen hres result records historical code1944bedcb3a59dd38633cf10507f4dfb530f06118c2ae82e65db87fee7cab0dd.
The current copied program has hash615478fe9ebdff3b07f0d74b061a2c5c7933ffc1ae2f84ea8a9349dbe55afdef.
Their unequal identities are recorded, not silently merged. The
historical program is unobserved. This finite arithmetic is independent
of either executable. Source-integral validity and exact historical
execution remain separate from the arithmetic consequence proved here.
