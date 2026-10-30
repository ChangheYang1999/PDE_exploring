# Reciprocal Opus reviews of the dual and improved Hardy bounds

## Exact statement and mathematical scope

Let F be real and locally integrable on R2, with finitely many positive
angular sine modes and rF in L2. Let psi be smooth, in the gradient
completion of compact smooth functions, with finitely many positive
sine modes, grad psi and r Delta psi in L2. Define H(F) as the dual
norm against compact smooth real tests of gradient norm at most1.
Set A_F=-e_theta r sum f_n cos(n theta)/n, Z=A_(Delta psi)-grad psi,
M2=||A_F||2^2, a=||Z||2^2 and b=<A_F,Z>. Then for a>0,

 H(F)^2<=M2-b^2/a,
 H(F)^2>=sum p_n^2/d_n

for any finite set of distinct-frequency admissible gradient tests with
p_n=int Fpsi_n and d_n=||grad psi_n||2^2>0. In the upper bound,
distinct-frequency corrections add; same-frequency tests require their
Gram matrix or selection. Every M2 includes the complete source.
R1-048 and R1-049, read in full with both scripts and output logs,
confirm these assertions under the stated hypotheses. This audit
accepts their general arguments and independently checks their finite
fixture and candidate-source compositions. Numerical quadrature and
unaccepted modal displays remain explicitly outside the certificate.

## Complete informal argument

Angular integration by parts gives div A_F=F against compact smooth
tests. L2 of A_F and local integrability justify the origin limit,
with no radial flux or contact distribution. The same identity for
Delta psi and integration by parts against a compact test imply
div Z=0. Cauchy-Schwarz bounds the dual norm by ||A_F+tZ||2.
Expand the square and minimize at t=-b/a. Different frequencies are
orthogonal in both polar components, proving the sum rule.

With psi=u(r)sin(n theta), y=log r and v(y)=u(exp y), direct polar
differentiation gives Z_r=-v'/r sin(n theta),Z_theta=-v''/(nr)cos(n theta).
Thus a/pi=int(v'^2+v''^2/n^2)dy and
b/pi=n^-2 int r f_n(r)v''(log r)dr. These are precisely the accepted
own404 formulas. For admissible psi, angular Hardy and Cauchy-Schwarz
give Fpsi in L1. The Riesz representative Phi of F exists since
H(F)<=sqrt(M2); Phi-psi represents g=F+Delta psi. Expanding its
squared gradient proves H(F)^2=2p-d+H(g)^2. Linearity of A also gives
M2+2b+a=2p-d+||A_g||2^2. Completing the same scalar quadratic yields
the exact gain (a+b)^2/a from optimizing over its t=1 value.

For the lower inequality, smooth radial cutoffs converge in gradient
norm for each declared exact beta>3/2 trial; their squared error is
O(R^(6-4beta_min)). Origin regularity follows from3+2k>=n and even
difference. Absolute integrability passes the pairings to the limit.
Orthogonality shows that the gradient norm squared of sum(p_n/d_n)psi_n
and its pairing both equal sum p_n^2/d_n, proving the lower bound.
This step would remain valid even if H(F) were infinite.

## Exact finite verification

The own rational polynomial integrator uses u=r w^bP(t),
t=r^2/(1+r^2),w=1-t,D_bP=(1-2bt)P+2twP'. It reconstructs the two
manufactured fixtures and the residual identities by exact polynomial
moments. Independently verify the differential shift for each supplied
label: with a0=3+2k,s=beta+k,m=r^a0(1+r^2)^-s and L=r d/dr,
Lm=a0 m-2s m(a0+2,s+1) and
L2m=a0^2m-4s(a0+1)m(a0+2,s+1)+4s(s+1)m(a0+4,s+2).
This follows by applying the first derivative twice. Its polynomial
form also covers the k=-1 constant term. The fixture fractions are
d/pi=3/8,6/35; a/pi=3/8,2/63;M2/pi=3/4,64/315.
Their full exact H2/pi=153/280, one-test upper1457/2520 and gap2/63.

Parse the peer scripts' literal source maps without execution and bind
every input to the own accepted396/398/392/252 sources. All663 labels
are checked for smoothness and decay. Compare exact candidate d/pi and
a/pi records and use the repaired650digit399 pairing archive for the
strict dual/cross composition; the old200digit strings are insufficient.
Use accepted392 component endpoints to recheck the same E2 square,
the strict lower608.392385921614,007 upper606.820219 and exact gap
1.572166921614. Retain own402/404/406/407 dependencies and the complete
finite source of016. No expensive candidate double sum or source
moment is repeated by this reciprocal finite checker.

The reviewed positive-pole FLOAT example uses the literal exponent
7/5 in its script, while R1-049 V6 describes7/10. Check the literal AST
assignment and record this attribution repair. It changes no analytic
formula or candidate integral. The claim of containment in R1-048 V5
was originally checked only as overlap; recheck actual directed
containment here, while using the own399 archive as the proof premise.
No accuracy conclusion follows from an interval merely containing zero.

## Domains, collaboration and remaining gates

The general divergence-free theorem is now reviewed by both existing
Opus5.5 lanes. Configured identity is us.anthropic.claude-opus-5-5;
actual provider response is unobservable. No model substitute or remote
client is used. T1's separate R1-050 on the prefix-tail proof is still
pending in its announced scope. Own403/407 already verify the finite
tail inequality and its arithmetic; a later whole-field upper acceptance
will bind the final prefix and trial choices explicitly. This result
accepts neither an N3 narrower display nor an exactH, inverse, contraction,
stationary solution, trial completeness or correction-distance ordering.
Exact JSON, frozen reviews and proof hashes precede the own code.
No peer code, JavaScript/TypeScript, server or cluster is executed.
