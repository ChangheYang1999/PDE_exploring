# The e=2 necessary configuration: finite integer reduction

Result271. Written before the independent checker and enumeration on2026-10-21. This result audits the arithmetic claim in SPECv53 G45. The finite search is initially OPEN pending execution; the proof below establishes its complete search domain. No numerics code or external search code is read or reused.

## Statement, hypotheses and dependencies

Consider positive integers n,nu,mu with mu>nu+n. Put k=mu-nu-n>0, D=6nu+6n+4k+1=1+2nu+4mu+2n, r=D/(D-1), t=1/r. All the denominators below are positive. Result261, with253/258 as explicit dependencies, shows that any e=2 configuration in the necessary finite polynomial auxiliary axis system has A0=1, one real node a of weight2nu and a nonreal conjugate pair of weight2mu. Here

 a=-kr/n, S=-(1+2nu a)/(2mu), J=(1+2nu a^2+2mu S^2)/(4mu).

The monic node polynomial is pi(v)=(v-a)(v^2-Sv+J). The remaining necessary equation is E=pi'(r)=3r^2-2(S+a)r+J+aS=0. The hypotheses already ensure the first two moments and the weighted relation once the node formula is used. The polynomial equation is necessary for the configuration; excluding it suffices to exclude the configuration. We do not need a converse to any underlying polynomial H or profile problem.

We prove: every real zero with n,nu,k>0 has nu>4n and k>(4+2sqrt(6))n. Every integer zero satisfies the finite divisor construction below. There is no integer zero if n is a power of two. For fixed n all integer zeros obey nu<(17/4)n^4-2n^3. An exact exhaustive execution for1<=n<=1000 can therefore settle that finite n range without a nu or mu cutoff. No assertion for all integer n follows.

## Direct polynomial derivation

Use u=a/r=-k/n and s=S/r=-(t+2nu u)/(2mu). Then J/r^2=t^2/(4mu)+nu u^2/(2mu)+s^2/2, so

 Q=8mu^2 n^2 E/r^2=C+B t+A t^2,
 A=n^2(2nu+2n+2k+1),
 B=4n[k^2+3nk+2n(n+nu)],
 C=4(4n-nu)k^3+4n(14n+3nu)k^2+64n^2(n+nu)k+24n^2(n+nu)^2.

This is obtained by substituting s,u into 3-2(s+u)+J/r^2+us and clearing8mu^2n^2. Define the integer polynomial

 F=D^2 C+D(D-1)B+(D-1)^2 A.

The source's expanded polynomial P(n,nu,mu) equals F/4 after mu=nu+n+k: both equal8mu^2n^2(2mu+n+nu)^2 E. The independent checker will reconstruct E and verify every coefficient of the source polynomial, rather than accept its displayed expansion.

## The real inequalities

Expanding Q by powers of k gives

 Q=4(4n-nu)k^3+4n(14n+3nu+t)k^2
   +2n^2(32n+32nu+t^2+6t)k
   +n^2[24(n+nu)^2+(2n+2nu+1)t^2+8(n+nu)t].

If nu<=4n all terms are nonnegative and the final bracket is positive, so Q cannot vanish. Since0<t<1 and A,B>0, Q=0 requires C<0. The quadratic C in nu has positive leading coefficient24n^2 and discriminant

 16k^2(k+n)^2(k^2-8nk-8n^2).

A real quadratic taking a negative value with positive leading coefficient has positive discriminant. Thus k^2-8nk-8n^2>0. With k,n>0 this is exactly k>(4+2sqrt(6))n. The identities will be expanded independently; no numerical approximation of sqrt(6) is used in the proof or search.

## Arithmetic reduction without loss

Assume an integer zero. Reduction of F=0 modulo the odd integer D gives D|A. The identity3A=n^2(D+2k+2) then implies D|2n^2(k+1), hence D|n^2(k+1). This does not require3 coprime to D: we multiply a divisibility by3 and only cancel2, which is coprime to oddD.

With nu=(D-6n-4k-1)/6 the following exact polynomial identity holds:

 12P=2n^2D^4+(-2k^3+6nk^2+16n^2k+n^2)D^3
 +2(4k^4+18nk^3+k^3+18n^2k^2+3nk^2+3n^2k-3n^2)D^2
 -n(12k^2+24nk-n)D+2n^2(k+1).

Its identity with3F is checked as a rational polynomial, without assuming any divisibility by6. Let L=n^2(k+1)/D, an integer. Divide the displayed identity byD and reduce moduloD to obtain D|2L-n(12k^2+24nk-n).

Set g=gcd(D,n^2), d=D/g, N=n^2/g. Then g is an odd positive divisor of n^2 and gcd(d,N)=1. The first divisibility gives d|k+1, so k+1=hd for a positive integer h. The defining D relation becomes

 (g-4h)d=6nu+6n-3>0.

Thus1<=h<g/4, in particular g>4. A power-of-two n has no such odd divisor g and is excluded. Substitute k=hd-1 and L=Nh in the second divisibility. With

 K=n(25n-12)+2Nh

it becomes gd | K-12nh^2d^2-24nh(n-1)d. Therefore

 d|K,   g | K/d-12nh^2d-24nh(n-1).

Each step is necessary for an arbitrary putative zero. Conversely the enumeration below checks positivity/integrality and the original equation, so a reported zero could not arise from the congruences alone.

The integer K is positive for n>=1. Since h<g/4, K<(51/2)n^2-12n<26n^2. Every positive divisor d of K satisfies d<=K. Hence D=gd<=n^2K<(51/2)n^4-12n^3, and nu=(D-6n-4k-1)/6<D/6<(17/4)n^4-2n^3. There is no bound on n.

## Exhaustive computation protocol

For each integer1<=n<=1000 enumerate every odd divisor g>4 of n^2, each1<=h<g/4, and every positive odd divisor d of K. Require gcd(d,N)=1, k=hd-1>0, integral nu=(gd-6n-4k-1)/6>4n, and the second g congruence. Every candidate must be evaluated with arbitrary precision integers in both F and the independently reconstructed original P; require F=4P. Record every arithmetic candidate and every zero, per-n counts, timestamps and all input/code hashes. No additional real bound is used to discard candidates, so source count comparisons are meaningful but not the reason for exhaustiveness.

The separately written C++ enumeration uses a deterministic smallest-prime-factor sieve below26million, constructs all divisors by prime exponents and checks congruences with signed128-bit intermediates. At n<=1000, g<=10^6, h<250000, d<26million, k<6.5*10^12 and D<2.6*10^13. All machine-sized products in those congruences are below10^24, safely within signed128-bit range. Arbitrary precision cpp_int handles F and P, including all powers. These numerical bounds are part of the verification, not unchecked implementation assumptions. Local Python will independently trial-factor selected inputs, enumerate small cases without the sieve, and reevaluate every saved candidate using rational node formulas or the independently expanded polynomial. Each build input is exact JSON or a small deterministic derivative of it, registered by hash.

All output remains in this lane. No JavaScript/TypeScript/Node, servers/listeners/tunnels, RLSciencecluster or Lean/Lake. One heavy CPU job, nice19, single-threaded, RAM below16GB. The finite arithmetic result and actual-model review remain OPEN until the recorded gates pass. Full-plane SettingIII remains UNRESOLVED; no early-finish endpoint follows.
