# Candidate 017 residual identity: acceptance of both Opus reviews

## Exact statement and hypotheses

Use the real plane with Lebesgue measure. For a real distribution G define
H(G)=sup{|<G,phi>|: phi real C_c^infinity(R2), ||grad phi||2<=1}.
Fix an odd positive integer n and F_n=f(r)sin(n theta) locally integrable,
with Q=||rF_n||2^2 finite. Let
u(r)=sum_i x_i r^3(1+r^2)^(-beta_i)(r^2/(1+r^2))^k_i,
where the sum is finite, x_i real, beta_i>3/2, k_i>=-1 integer,
and 3+2k_i-n is even and nonnegative. Put psi=u(r)sin(n theta),
y=log r and
A=-r f(r)cos(n theta)e_theta/n,
Z=-u_r sin(n theta)e_r-u_yy cos(n theta)e_theta/(nr),
d=||grad psi||2^2, a=||Z||2^2, p=int F_n psi, b=<A,Z>.
For d>0 the following identities and bounds hold:

 ||r Delta psi||2^2=n^2(a+d),
 int r^2 F_n Delta psi=n^2(b-p),
 R^2:=||r(F_n+Delta psi)||2^2=Q+2n^2(b-p)+n^2(a+d),
 max(0,sqrt(d)-R/n,|p|/sqrt(d))<=H(F_n)<=sqrt(d)+R/n.   (1)

Absolute convergence follows from
 |b|<=sqrt(Qa)/n, |p|<=sqrt(Qd)/n,
 |int r^2 F_n Delta psi|<=n sqrt(Q(a+d)).               (2)
The last factor n is necessary. T2 review at its frozen 18:07 version
omits it in R2. That displayed bound is false for n>1; the review's
identity, cutoff argument and finiteness conclusions survive the repair.

For finitely many trials at distinct frequencies with absolutely
convergent pairings, H(F)^2>=sum p_n^2/d_n. These statements do not assume
complete candidate Hardy or E2 data. The candidate017 dual lower and
n1/n3 residual endpoints remain exactly the already accepted T4-495
values. The other14 residual modes, remaining158 complete Hardy inputs,
G0/G1/P2, full H upper, E2 and its ordering with007 remain OPEN.

## Standalone analytic argument

At zero r^(3+2k)sin(n theta) is a harmonic polynomial times an even
nonnegative radial power, so psi is smooth. At infinity u,u_y,u_yy
are O(r^(3-2beta_min)), with beta_min>3/2. These orders imply
u,u_y,u_yy in L2(dy), grad psi and r Delta psi in L2(dx), and
u u_y tends to zero at both ends. The squared gradient error from
multiplying psi by a smooth radial cutoff on r<=2R is
O(R^(6-4beta_min)), tending to zero. At beta=3/2 the boundary term
can still vanish: u=r^3(1+r^2)^(-3/2) tends to1, u_y tends to0,
but the n1 angular contribution integral u^2dy diverges. Thus the
strict beta hypothesis guarantees finite energies, not merely a
vanishing boundary term. Cancellation among leading trial terms can
improve decay, so no necessity of beta_min>3/2 for every finite sum is
asserted.

Angular integration gives
 d=pi int (u_y^2+n^2u^2)dy,
 a=(pi/n^2)int(n^2u_y^2+u_yy^2)dy,
 p=pi int f u r dr, b=(pi/n^2)int f u_yy r dr.
Since r^2Delta psi=(u_yy-n^2u)sin(n theta), integration by parts
of -2n^2 u u_yy gives
 ||rDelta psi||2^2=pi int(u_yy^2+2n^2u_y^2+n^4u^2)dy
                  -2pi n^2[u u_y]=n^2(a+d).
The pointwise cross term is n^2(b-p). Expanding the norm square
proves the residual identity. Cauchy-Schwarz gives all three
inequalities (2); for p use ||psi/r||2<=sqrt(d)/n. The n factor
in the cross estimate is ||rDelta psi||2=n sqrt(a+d).

Angular differentiation gives div A=F_n on annuli. Local integrability
of F_n permits angular integration by parts through the origin; A has
no radial flux and is L2 by Q<infinity. Hence div A=F_n in distributions,
with no point mass, and H(F_n)<=sqrt(Q)/n. The same argument applies
to F_n+Delta psi. Integration by parts and the cutoff convergence
give H(Delta psi)=sqrt(d). The two triangle inequalities and the test
psi/sqrt(d) give (1). Distinct angular frequencies have orthogonal
gradients. Cut off sum(p_n/d_n)psi_n to obtain the multimode lower
bound, including H(F)=infinity. Repeating a frequency would require
the actual Gram matrix.

Q<infinity alone need not imply local integrability: near zero,
f(r)=r^-2/log(1/r) on0<r<exp(-1) has finite int r^3 f^2dr,
but infinite int r|f|dr. Thus T2's source qualification is legitimate.
For the accepted017 finite potential it is discharged without any
new integral: each generator in the frozen projection proof is a
Cartesian harmonic polynomial times (1+r^2) to a real power, times
polynomials and rational factors in r^2/(R^2+r^2), R>0. Every denominator
is strictly positive near0; every generator is smooth there. The
finite Cartesian derivatives forming rho, U and F are smooth. Their
sine projections, being rotation averages, are smooth and locally
integrable. The actual017 structural identity remains the previously
accepted T4-495 source/projection premise, not a newly reconstructed
field in this review acceptance.

## Exact counterexample to the omitted n

Take n=3,k=0,beta=3, u=r^3(1+r^2)^(-3), psi=u sin(3theta),
and F_n=Delta psi. Direct differentiation gives
 f(r)=-48r^3(1+r^2)^(-5).
The exact beta integral int_0^infinity r^m(1+r^2)^(-s)dr
=Gamma((m+1)/2)Gamma(s-(m+1)/2)/(2Gamma(s)) for positive
arguments evaluates, after dividing all squares/pairings by pi,
 d=6/35, a=2/63, p=-6/35, b=2/63,
 Q=64/35, a+d=64/315, int r^2F_nDelta psi=64/35.
The erroneous proposed right side sqrt(Q(a+d)) is64/105,
exactly one third of the cross term. The corrected n sqrt(Q(a+d))
is64/35 and gives equality. R^2/pi=256/35. All hypotheses hold;
this is a smooth rapidly decaying source, with no origin or infinity
exception. The beta integral follows by t=r^2/(1+r^2) and the defining
Euler beta integral. The checker independently differentiates finite
sums of r^m(1+r^2)^(-s), expands products, and integrates their
convergent monomials with exact Fraction beta recurrences. It does not
call a symbolic integrator, peer program or candidate moment engine.

## Radial formulas and finite review composition

With t=r^2/(1+r^2), v=1-t and u=r sum_b v^b P_b(t),
dt/dy=2tv and
u_y=r sum_b v^b D_bP_b, D_bP=(1-2bt)P+2t(1-t)P'.
Applying this twice and using r dr=dt/(2v^2),r^2=t/v
proves the five radial formulas in the frozen N4 proof. Equal powers
must be collected before integrating signed monomials. The accepted
source group convergence and positive poles are retained. T1's FLOAT
quadratures are useful observations, not certificates or new premises.

Read T1 R1-053 and T2's complete note, source checkers as text and their
79/18-check logs. Reconstruct T2's three exact examples and its known
Riesz representative with the independent finite monomial integrator.
For F=-Delta(w sin theta), w=r(1+r^2)^(-2), the exact H2/pi=4/15,
residual H2/pi=9/280 and R2/pi=1959/20020 check the triangle and Hardy
bounds. Inspect the six endpoint-order fixtures algebraically from
the leading exponent alpha=3-2beta: the d,a,Laplacian-square radial
coefficients are alpha^2+n^2,alpha^2+alpha^4/n^2,(alpha^2-n^2)^2.

T1's exact extract is compared field by field and by source hashes
with the own495 frozen result and two mode records. Sixteen positive
distinct floors sum to the accepted exact lower square. Exact squares,
differences and divisions prove all stated coarse intervals, widths,
relative width and approximate gap statements. No source group is
reintegrated. The complete H lower is a lower bound, so its location
inside an earlier conditional interval is only consistency, never a
proof of that interval's upper premise.

## Dependencies and verdict scope

Standalone predecessors: ../candidate017_conditional_acceptance/PROOF.md
(T4-484 analytic identity), ../candidate017_partial_replay_audit/PROOF.md
(T4-495 actual frozen groups), the general dual/Hardy arguments and
accepted Opus reviews identified there. This acceptance CONFIRMS both
reviews' identities and admissibility arguments after correcting T2 R2;
it REFUTES only the omitted-n display and preserves all OPEN candidate
components. No inverse, distance, stationarity or existence follows.
