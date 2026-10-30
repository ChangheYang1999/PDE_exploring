# Audit of a sharper universal compensated-velocity upper bound

## Statement, scope and current status

Let -5<q<-3. Let h be real, centrally odd and C1 on R2, with

 H=H_q(h)=max(sup (1+|X|)^(-q)|h(X)|,
                 sup (1+|X|)^(1-q)|grad h(X)|)<infinity.

Use the complete canonical operator

 U[h](X)=(0,-h(X)/2)+PV integral K(X-Y)h(Y)dY,
 K(Z)=(-z1 z2,(z1^2-z2^2)/2)/(pi |Z|^4),
 M[h]=integral Yh(Y)dY.

The moment is absolutely convergent. The claim being audited is that at
q=2251799813685248/4076476460239181-4, one may use E=1749109/1000000 in

 |U[h](X)+DK(X)M[h]| <= E H |X|^q, X!=0.                  (1)

The proof below gives a sufficient integral certificate for (1). Its
numerical inequality remains OPEN until this lane's independent complete
cell calculation passes. The target was proposed in T2's frozen note
and part B of its frozen checker. Parts C-E contain separate diagnostics
and are not accepted by this audit. No stationary equation, normalization
at the origin, inverse or nonlinear closure is being asserted.

## 1. Scaling, folding and the local term

The case H=0 is immediate. Otherwise, for X=r e, scale
f(Z)=h(rZ)/(H r^q). Then |grad f(Z)|<=|Z|^(q-1) for Z!=0.
The amplitude tends to zero along each ray, so integration of this
radial derivative from infinity gives |f(Z)|<=|Z|^q/(-q).
The canonical scaling gives

 [U[h](r e)+DK(r e)M[h]]/(H r^q)
  =(0,-f(e)/2)+PV integral [K(e-Z)+DK(e)Z]f(Z)dZ.

The oddness of f permits folding the kernel about the origin. Identify
a physical vector (v1,v2) with v2+i v1. At e=1 in complex coordinates
w=z1+i z2, K(w)=1/(2pi w^2) and DK(1)Z=-w/pi. Fix 0<rho<1 and define

 k(w)=[chi1(w)/(1-w)^2-chi2(w)/(1+w)^2]/(4pi)-w/pi,
 chi1=1{|w-1|>rho}, chi2=1{|w+1|>rho}.

The two omitted singular disks have disjoint interiors. In each disk
subtract the corresponding constant f(1) or f(-1), which contributes
zero because the angular mean of the singular kernel vanishes. For
|W|=s<rho, integration along the segment from 1 to 1+W gives

 |f(1+W)-f(1)| <= integral_0^s (1-u)^(q-1)du
                 =[(1-s)^q-1]/(-q).

For any unit output direction, the absolute angular integral of its
projection of K(W) is 2/(pi s^2). The factors one half in the two folded
disks sum to one. Thus their total directional contribution is at most

 (2/pi) N(rho),
 N(rho)=1/(-q) integral_0^rho [(1-s)^q-1] ds/s.

The nonlocal far contribution in output direction beta is at most
F_beta/(-q), where

 F_beta=integral_R2 |Re(exp(-i beta)k(w))| |w|^q dA.

The local contact term is at most1/(2(-q)). At a general position
angle theta the nonlocal vector rotates by exp(-2i theta), while its
contact term remains in the physical second component. Taking the
supremum over beta and bounding the contact term separately therefore
gives the valid direction-independent sufficient constant

 E(rho)=(2/pi)N(rho)+(sup_beta F_beta+1/2)/(-q).             (2)

The integral F is absolutely convergent: k(w)=O(|w|^3) at zero,
k(w)=O(|w|) at infinity, and both singular disks have been removed.
These use q>-5 and q<-3, respectively. This derivation retains the
contact term and does not assume a zero moment or S1 beyond central
oddness.

## 2. Exact exterior bounds for the integral certificate

The checker fixes rho=3/20, t0=1/20 and T=2000. For |w|<t0 the cutoffs
are both one and

 k(w)=sum_(n odd>=3) (n+1)w^n/(2pi)
     =2w^3/pi+w^5(3-2w^2)/(pi(1-w^2)^2).

Use the exact absolute angular projection integral4 for the cubic,
and the coefficient majorant for the remainder. Uniformly in beta,

 integral_(|w|<t0) |Re(exp(-i beta)k(w))| |w|^q dA
 <= (8/pi)t0^(q+5)/(q+5)
      +6 t0^(q+7)/[(1-t0^2)^2(q+7)].                       (3)

For |w|>T, both cutoffs again equal one. The term-w/pi integrates
directionally to (4/pi)T^(q+3)/(-q-3). The remaining two kernels have
sum of magnitudes at most1/[2pi(t-1)^2]. Therefore

 integral_(|w|>T) |Re(exp(-i beta)k(w))| |w|^q dA
 <= (4/pi)T^(q+3)/(-q-3)+(T/(T-1))^2 T^q/(-q).             (4)

Also a=-q>1 gives

 N(rho)=(1/a)sum_(j>=1) (a)_j rho^j/(j j!).

After term J, each successive term ratio is at most
z=rho(a+J)/(J+1)<1. Thus the omitted sum is at most the last retained
term times z/(1-z). The checker uses positive Arb arithmetic and an
explicit geometric tail, not an unbounded truncated series.

## 3. Complete polar cells and their analytic errors

Because k(-w)=-k(w) and k(conj w)=conj k(w), the remaining annular
integral equals twice the first-quadrant integral of the sum of the
projections at beta and-beta. Partition t0<=t<=T into the exact rational
radial endpoints stored in data/mesh.json. Partition0<=phi<=pi/2 at
j pi/(2Nphi). A cell C has radial endpoints ta,tb, angular endpoints
pa,pb, center wc=tm exp(i pm), and enclosing complex-disk radius

 d=(tb-ta)/2+tb(pb-pa)/2.

The triangle inequality and |exp(iu)-exp(iv)|<=|u-v| prove this disk
containment. Its exact positive radial weight is

 W_C=(pb-pa)(tb^(q+2)-ta^(q+2))/(q+2).

Only the cutoff around+1 can change in the first quadrant. For each
branch that can occur in C, use one of the analytic functions

 k1(w)=[(1-w)^(-2)-(1+w)^(-2)]/(4pi)-w/pi,
 k0(w)=-(1+w)^(-2)/(4pi)-w/pi.

Possible branches are determined conservatively by |1-wc|+/-d and
rho. Every denominator disk is checked to avoid its singular point.
For k1 the second derivative magnitude on the disk is at most

 M2=3[(|1-wc|-d)^(-4)+(|1+wc|-d)^(-4)]/(2pi),

and for k0 only the second term is needed. Taylor's integral remainder
therefore gives, for every w in C,

 |k_b(w)-k_b(wc)|<=d |k_b'(wc)|+(d^2/2)M2=:s_b.             (5)

For each projection use the largest of
|Re(exp(-i beta)k_b(wc))|+s_b over possible branches. Multiplying by
W_C, summing all cells and their reflected projections and adding
(3)-(4) gives a rigorous U(beta)>=F_beta. Cells meeting the cutoff
circle are replaced by their complete8 by8 subdivision; no cells are
discarded. Thus neither the cutoff jump nor the polar partition creates
a missing region. The union and every positive denominator are checked.

## 4. Direction maximization and acceptance rule

Each projected center term is Lipschitz in beta with constant|k_b(wc)|.
The branch maximum is Lipschitz with the largest such constant. The
slack terms and (3)-(4) are independent of beta. The same weighted sum
therefore supplies a finite L for U. Reflection gives U(beta)=U(-beta)
and pi-periodicity, so0<=beta<=pi/2 suffices.

For an interval [a,b], endpoint upper bounds ua,ub give

 sup_[a,b] U <= (ua+ub)/2+L(b-a)/2.                         (6)

This follows by using the smaller of ua+L(t-a) and ub+L(b-t).
An adaptive dyadic partition of[0,pi/2] is accepted only after its
exact rational endpoints are sorted, meet consecutively and have total
length one in units of pi/2. Each interval's (6) bound is evaluated in
Arb. Its upper endpoint is converted to an exact dyadic rational, so
no float comparison or nearest-rounded decimal determines the final
upper bound. Floats may choose where to subdivide but cannot validate
an interval. Every completed interval is retained in the certificate.

Let Fup be the largest exact dyadic upper endpoint in this complete
partition. The independent certificate passes only if Arb proves

 (2/pi)N(3/20)+(Fup+1/2)/(-q) < 1749109/1000000.

A successful check confirms the numerical claim(1) under precisely
the hypotheses stated here. The stored result must give the complete
cell count, crossing-cell count, directional partition and real run
times. It does not imply that this E is optimal, that a stationary
correction has bounded H_q, or that CI closes. Those are separate
questions. T4-381/384/397 supply a universal lower constant; they do
not prove this upper constant.
