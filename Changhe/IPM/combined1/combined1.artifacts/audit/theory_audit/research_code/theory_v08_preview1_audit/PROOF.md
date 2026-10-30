# Independent audit of theory_v08 preview 1

## Object, statement and scope

This audit concerns all 769 lines of the frozen preview generated at
2026-10-29T13:29:19Z, SHA256
d8c8e8ba4d36e281381c0f7c55447c9636fc39977e6350a00d805c765725cf06.
It is a draft, not a published exchange version. The sources are copied
locally. This proof precedes the checker for this topic.

The corrected 24-row factor table is valid with the separate scopes in
its section 1.1. The endpoint obstruction in its section 5 is valid for
the four named targets, under the inherited endpoint and majorant
hypotheses. The current-list integral bounds and the two open small-radius
questions are correctly distinguished in section 2(g). The remaining
scope and status repairs below are required before publication. No
existence theorem, high inverse, or unrestricted nonexistence result is
established by this audit.

The reference exponent is
c=4076476460239181/2251799813685248. S1 functions are real, even in x and
odd in y. Every correction claim here fixes c and the leading far-field
profile. The canonical velocity is U=(partial_xy,-partial_xx)Delta^(-1),
including its local term (0,-h/2). In the expression DK(X)M(h), DK denotes
the derivative of the kernel, not multiplication by the scalar D below.
The moment is M(h)=integral X h(X)dX when it converges. The endpoint norm is

 H_q(h)=max(sup_X (1+|X|)^(-q)|h(X)|,
            sup_X (1+|X|)^(1-q)|grad h(X)|),
 q=1/c-4, delta=1-1/c, kappa=1-q, D=c*kappa=5c-1.

All closure statements keep their operator domain, normalization,
reference regularity and inverse hypotheses from the accepted theory_v07
and draft38 audits. In particular the X_(s,w) chart is the completion
with norm E_w((1-Delta)^(s/2)h), where
E_w(g)^2=||omega D^2 g||_2^2+w1||Dg||_2^2+w2||g||_2^2 and
omega=(1+4|X|^2)^(2/5). A fixed-c tangent has c[h]=0. The L2 chart does
not contain the nonintegrable scaling or leading angular modes.

## Factor table

For each row let Q be its specified nonnegative quantity and T>0 its
specified threshold. If p<=Q and T<=t with t>0, then Q/T>=p/t. If k is
the displayed precision, floor(10^k*p/t)/10^k is therefore a lower bound.
A displayed factor greater than one contradicts Q<T and also Q<=T.
This elementary implication does not make a sufficient norm test a
necessary condition for existence.

The accepted T4-437 record supplies the separate outward comparisons for
all 24 rows. The new text and revision-2 source must match those exact
numerators and thresholds. In particular S2 uses the sharp norm
XSW[1/7744,2^14,2^18], with
516.9717852723<X(F)<517.5527701453 and threshold 76219/10^9.
Its downward factor is 6782715.40. S1 uses the different sharpw norm
XSW[1/5184,2^15,2^20] and numerator 756.5312630768.

The D rows exclude only the specified L2-dominated balls by a certified
lower distance. The S rows fail specified sufficient norm tests. O1 is
conditional on every origin-inverse hypothesis. U rows concern all
coefficients in a particular universal norm class. P1 and P3-P5 compare
chosen proved upper coefficients; P2 concerns the complete angular span.
R and A compare chosen upper error majorants with their available room.
K compares the bracket of the present remainder formula with a necessary
threshold of the deliberately optimistic model. None excludes an
unlisted stationary estimate or another framework.

## Endpoint arithmetic and majorant argument

The accepted universal-class lower bound is
Emin=(-q-1)/(2*(-q)*(-q-3)). The positive bracket lower bound is
lambda=1/2+5*2^(1-q)>109.6024. For a coefficient e(s), define
T[e](r)=kappa*r^kappa*integral_r^infinity e(s)*s^(-kappa-1)ds.
The T4-335 tail list gives the positive term
C_delta*r^(q-delta), C_delta=H*(V+E*G)/D, with H=H_q(h)>0,
V>=0, G>=g0>0 and universal E>=Emin. Under exactly this list and the
T4-410 construction, its remainder coefficients have the floor
min(Emin,lambda*(5/s)^delta). T is positive. Splitting the elementary
integral at u=5*(lambda/Emin)^(1/delta) gives, for r<=u,

 T[e](r)>=Emin*(1-delta/(kappa+delta)*(r/u)^kappa).

At every named r_beta this exceeds 0.79303, while the necessary
positivity threshold is less than 0.785064. The outer-only floor from
T4-432 gives the separate lower bound 0.79303648. Thus all allowed
starting radii and these variable coefficients fail the four-target
certificate. This is a lower bound on an upper error estimate, not on
the actual error. The no-fallback factor above 4.34 must remain separate.

The kernel thresholds 13.27,14.41,8.647,7.287 are checked against all
three candidate records, not merely the factor table at 007. They are
upper bounds for the optimistic necessary thresholds and do not assert
that a smaller bracket suffices. The profile coefficient 93/250 leaves
no room at the graded target even with zero remainder.

For the additional small targets use the audited T4-443 theorem. Let
alpha=-2q-2, S=2*delta^2/[alpha*(alpha+delta)*(alpha+2*delta)],
f(s)=min(Ef,lambda*(5/s)^delta), E1=T[f](M),
r0=[sqrt(2*pi)*Hmin*(vmin+g0*E1)/(D*B)]^(1/delta).
For the radial certificate
J^2=integral_R^infinity [B-sqrt(2*pi)*ehat(r)]_+^2*r^(2q+1)dr,
where ehat(r)>=(Hmin/D)*(vmin+g0*T[e](r))*r^(-delta) and e>=f,

 J^2 <= B^2*r0^(2q+2)*S+B^2*M^(2q+2)/alpha.

Indeed T[f] is nonincreasing, so the inner integral through M is bounded
by the full constant-E1 integral. Beyond M discard the nonnegative error.
This also holds for M<R. For Ef=Emin, Hmin=Phi and vmin=v0, M=122000
gives J<1.14141e-7<2^-23. For the particular selected list with
Ef=1.747261, Hmin=H0 and vmin=0, M=108000 gives
J<2.66323e-8<2^-25. A valid but smaller universal coefficient is not
excluded from the two smallest targets by the supplied arguments.
Emin is not asserted admissible. The 13 tested radii are exact printed
targets; unprinted exact family ceilings need their own formula binding.
The constant universal-coefficient bound J<1.421e-7 and the more general
variable-coefficient bound are distinct, consistent statements.

## Remaining repairs to the preview

1. Section 0 item 0 says 023-025 are excluded in every registered ball.
   Section 3.2 repeats that wording for 022. Section 6 item 2 uses the
   same phrase to dismiss the possible effect of remaining dyadic tests.
   Replace each unrestricted phrase by 'registered scalar balls and
   original graded boxes'. The separate dyadic status must remain
   explicit. A scalar exclusion alone does not prove a dyadic exclusion.
2. Section 4 starts the 025 item with OPEN and ends the same item with
   the v130 RULED OUT conclusion, already supported by independent
   T4-438 to441. The opening status must be RULED OUT in the named
   scalar and original graded families.
3. Section 6 item 2 says the two-projection test completes the remaining
   dyadic rows and cannot change a closure question. The test is a
   sufficient way to refute the necessary inequality when every gap is
   positive. Failure of that test is inconclusive. The existing 009
   example already distinguishes a failing two-mode diagnostic from an
   exclusion by all modes. State that it tests the remaining rows and
   does not establish a closure. Do not promise a verdict in advance or
   infer the dyadic status from the scalar status.
4. Section 6 item 5 and section 0 item 4 should tie their ceiling
   comparison to the scalar and original graded families. The stated
   factor 1257.36 is not a universal radius ceiling for an untested
   dyadic or localized framework. Section 6 item 5 also says a candidate
   still needs rows S and N1: those are requirements of the specified
   sharp/sharpw certificates, not of every possible framework.
5. Section 7 still says T2's new Arb claims await review. T4-443 has
   reviewed the finite arithmetic and the split-integral theorem. Name
   the remaining logical repairs rather than mark those computations
   unreviewed. The frozen T2 source itself remains revision 1; its broad
   'falsified' language is not accepted by this preview or this audit.
6. The sentence after errata 67-72 that none changes a number is false
   as a literal summary: item 70 repairs displayed digits. Say that
   those errata change no candidate exclusion. Item 74 correctly
   distinguishes the false projected lower inference from the unknown
   full projected-plus-other-modes norm.
7. Explain DK as the kernel derivative on first use, since D is also
   the scalar 5c-1. No replacement by scalar multiplication is valid.

These repairs leave the corrected factors and endpoint majorant
obstructions intact. They prevent a transfer between different domains,
classes of estimates, or reference statuses.

## Verification and dependencies

The checker parses the copied revision-2 source as data, never imports or
executes it, compares the actual Markdown table to all T4-437 exact rows,
and recalculates the 24 quotients. It checks all three kernel-threshold
rows and the new integral caps against their accepted containing Arb
records. It binds the exact 025 distance and its displayed factors.
The 026 results and N4-v13 audit are reported as N4's own records pending
separate independent reproduction, not newly certified by this text.

Appendix H is checked against current read-only paths as a provenance
observation. A mutable source may have changed after generation; that
observation alone neither refutes its past hash nor certifies its past
contents. The stored observation identifies any such case. All actual
arithmetic inputs are frozen with their hashes. No candidate integral is
repeated and no foreign code is executed. There is no server, JavaScript,
cluster, remote model call or Lean build. Opus collaboration continues
through the existing theory-lane files; provider runtime identity remains
unobservable from this lane.
