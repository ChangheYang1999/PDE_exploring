# Final finite reciprocal acceptance: candidate016 and the candidate017 review repair

## Exact statements and dependencies

Let F16 be the canonical whole-plane residual of candidate016, raw SHA256
a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42,
at c=4076476460239181/2251799813685248. Its exact source and accepted
whole-plane hypotheses are stated in candidate016_multimode_complete_bounds/PROOF.md
(N4-431). Write F16=sum f_n(r)sin(n theta), n odd through319,
q_n=pi integral r^3 f_n^2 dr, S=||rF16||2^2, and
H=||F16||_(dot H^-1). This dual norm uses real compactly supported smooth
tests of gradient norm at most1. Put
E2^2=P2^2+2^14 G1^2+2^18 G0^2+(20/21)2^18 H^2,
with G0=||F16||2, G1=||DF16||2 and
P2=||(1+4r^2)^(2/5)D2F16||2, using the full Euclidean Hessian.
The complete source certificates and general cutoff, Hardy and solenoidal
arguments have already been independently accepted in N4-430/431 and their
listed dependencies. This finite result accepts T4-502's reciprocal arithmetic
and the corrected T2 auxiliary estimate, not a new source integration.

Under precisely those accepted hypotheses, the final complete bounds are

 308366750368225240013184170643/(5*10^29) < H
 < 308948684181969723952067879861/(5*10^29),
 628580088526341/10^12 < E2 < 39304086799647/62500000000.

For the identical007 norm definitions, H007-H16>0.017627007636152781
and E2016-E2007>21.759869526341. The earlier upper bounds remain valid.

For candidate017 and its admissible single-mode trial psi=u(r)sin(n theta),
retain all exact spaces and hypotheses in candidate017_opus_residual_review/PROOF.md
(N4-432): positive odd n, smooth trial with beta_i>3/2 and the stated integer
parity condition, source locally integrable, Q=||rF_n||2^2 finite,
a=||Z||2^2 and d=||grad psi||2^2 finite. The corrected Cauchy estimate is

 |integral r^2 F_n Delta psi dx| <= n sqrt(Q(a+d)).

The corrected T2 review is accepted for this literal repair. Its main residual
identity, gradient completion and triangle estimates, and source-origin
integrability of all2174generators, were already proved and accepted in N4-432.
No new017 upper norm or candidate comparison is asserted.

## Complete finite argument for candidate016

Let [l_n,u_n] be the producer's exact containing intervals for q_n, n<=63,
and let S_U be the accepted complete upper square of ||rF16||2. Every omitted
frequency is at least65, and q_n is nonnegative. Thus

 V=S_U/65^2+sum_(odd n<=63)(1/n^2-1/65^2)u_n

bounds the squared norm of the angular primitive. This includes all128omitted
modes of the complete160-mode residual. Let [v_n,w_n] be T4's containing
replay endpoints. Exact comparisons l_n<=v_n<=w_n<=u_n imply
V0<=V, with

 V-V0=sum_(odd n<=63)(1/n^2-1/65^2)(u_n-w_n)>=0.

The finite checker repeats these32 exact interval comparisons and the two
complete positive sums. The source integrations and all920signed source groups
are accepted in N4-430 and independently resummed in T4-502. Rehashing their
bindings is not called a repeated integration. T4's proof has one stale136
omitted-mode sentence, explicitly corrected to128 by its retained ERRATA_v01;
the original statement, code and exact counts are correct.

For the16selected distinct-frequency trials let L=sum ell_n^2 be the strict
dual square lower bound and J=sum j_n the strict solenoidal improvement.
N4-431 supplies these exact positive floors with all2130trial-group premises.
The general theorem gives L<H^2<V0-J<=V-J. The replay verifies the same L,J
and all endpoints, and that the difference of the two E2 upper squares is
exactly (20/21)2^18(V-V0). The lower E2 square is identical. Squaring positive
rational endpoints establishes every stated strict H and E2 bound.
Subtracting the accepted007 E2 upper606.820219 from the016 lower gives exactly
21.759869526341. Subtracting the016 upper H from the accepted containing007
H lower gives a gap strictly larger than0.017627007636152781. No assertion
about unknown correction-distance ordering is inferred from these norms.

## Complete finite argument for the corrected estimate

The accepted integration by parts gives ||r Delta psi||2^2=n^2(a+d).
Cauchy-Schwarz applied to rF_n and r Delta psi proves the corrected estimate.
Its constant n is necessary: for F_n=Delta psi and any nonzero trial,
Q=C=n^2(a+d), whereas sqrt(Q(a+d))=n(a+d). At n=3 and
u=r^3(1+r^2)^(-3), exact integration from N4-432 gives, after division bypi,
d=6/35, a=2/63, Q=C=64/35 and the old RHS64/105. The repaired RHS64/35
holds with equality. The peer's new example data are compared with the
independently integrated N4-432 fixtures; cross=n^2(b-p) and
||r Delta psi||2^2=n^2(a+d) recover the two extra fields without integration.
The corrected three Cauchy estimates follow by exact rational squaring in
allfourfixtures. The main residual identity and every accepted017endpoint
are unchanged.

## Verification scope and preservation

Freeze peer proofs, erratum, results, manifest, complete source-binding list,
checker text and note as inert local bytes. Freeze the corrected T2 review,
erratum program, results and log separately from the earlier review already
retained in N4-432. Read both complete proofs and peer programs; never execute
them. Rehash the57declared T4 manifest bindings as read-only provenance,
the361producer bindings in own lane, and all own432inputs. Compare exact
candidate identities, check counts, mode coverage, lower squares, upper-square
differences, directed endpoints and repair examples. Preserve any failure.

The code follows this standalone argument. It provides finite reciprocal
acceptance under already accepted analytic and source-specific integration
premises. It does not promote hashes to mathematical proofs. Full017 H upper,
E2 and017<007 remain OPEN. There is no inverse, stationary correction or
existence certificate. Opus collaboration used the existing T1/T2 files,
configuredus.anthropic.claude-opus-5-5; actual provider response is unobservable.
