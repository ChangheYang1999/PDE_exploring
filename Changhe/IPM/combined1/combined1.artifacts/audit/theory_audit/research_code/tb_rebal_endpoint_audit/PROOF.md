# TB-rebal: endpoint cutoffs at the exact family ceiling

Written UTC 2026-10-29T15:06:23.669232+00:00 before the finite checker.

## Statement and hypotheses

This audit concerns the replacement row of T2's FALSIFY revision3 note,
not the other unchanged rows. Fix c=4076476460239181/2251799813685248,
q=1/c-4, delta=1-1/c, D=5c-1 and alpha=-2q-2. In the fixed-c real
S1 charts the exact TB-rebal necessary L2 radius supremum is

 b=sqrt(323433/2621440000000000000),
 3.5125e-7 < b < 3.5126e-7.                              (1)

For each immutable reference007,013,014 use the exact endpoint coefficient
dictionaries in data/. Circle measure is dtheta on[0,2pi]. A real C1
stationary correction h has finite H_q(h), defined as the maximum of
sup(1+r)^(-q)|h| and sup(1+r)^(1-q)|grad h|. Velocity is canonical,
with the local/contact term retained. The complete endpoint expansion,
radial-error and stationary-normalization assumptions of the frozen
T4-443 proof remain required. In particular its endpoint equation
implies H_q(h)>=Phi>H0, with H0 respectively999775,999745,999748.

Write A(theta)=sum A_n sin(n theta), P(theta)=sum P_n sin(n theta),
Theta0(theta)=sum theta_n sin(n theta), and p=1/c+2. Define

 B=sqrt(pi*(sum A_n^2-(sum A_n P_n)^2/sum P_n^2))/(4c),
 g0=sum n theta_n,
 Phi=|q(AP'-A'P)|/[4c sqrt(q^2 P^2+(P')^2)],
 v0=|(p-1)sum n theta_n/(p^2-n^2)|,

where Phi is evaluated at the stored exact rational angle and its
denominator is positive. Set S=2delta^2/[alpha(alpha+delta)(alpha+2delta)].
All B,g0,H0,Phi,v0 are positive and S>0. The source coefficient
lower bound for every valid universal velocity coefficient is

 Emin=(-q-1)/[2(-q)(-q-3)]>0.7930365.                     (2)

This lower endpoint is not claimed to be a valid coefficient itself.
For H>=Phi and V>=v>=0, reaching a target radius beta with the selected
constant-coefficient endpoint CI certificate necessarily requires

 E<=K(beta;H,v)=D B/(sqrt(2pi)H g0)
          *(B sqrt(S)/beta)^(delta/(-q-1))-v/g0.         (3)

At every beta in[3.5125e-7,3.5126e-7] the three K(beta;Phi,0)
are at most0.6720590, and the K(beta;Phi,v0) lie in
[0.6372593,0.6372977]. At the exact b, these bounds improve to
0.6720573 and[0.6372611,0.6372960]. Hence this retained-shape test
fails for every admissible universal coefficient E>=Emin at b.
The crude cutoff replacing sqrt(S) by1/sqrt(alpha) is bounded above
by1.000026 over the bracket, and1.000024 at b; it is greater than
Emin for each candidate, so that test alone does not imply exclusion.
The old lower endpoint0.6372628 fails for candidate007 at b.

This is an obstruction to a particular certificate at a radius. It
proves no nonexistence of corrections, no attained family radius, no
upper bound on H_q over actual solutions, and no existence result.

## Derivation of the necessary cutoff and exact radius

Let R>=2 and let the chosen nonnegative radial-error majorant obey
 ehat(r)>=(H/D)(v+g0 E)r^(-delta), r>=R.
The CI lower witness chosen by the endpoint method is
 J^2=int_R^infinity[B-sqrt(2pi)ehat(r)]_+^2 r^(2q+1)dr.
Set r0=[sqrt(2pi)H(v+g0 E)/(D B)]^(1/delta). Extending the
nonnegative upper integrand to(0,infinity), and setting r=r0 u, gives

 J^2<=B^2 r0^(2q+2)*[1/alpha-2/(alpha+delta)+1/(alpha+2delta)]
      =B^2 r0^(2q+2)S.

Because q+1<0, the requirement J>=beta implies(3). Dropping the
shape terms gives the weaker factor1/sqrt(alpha). This is a necessary
condition only: passing it does not construct a coefficient or profile.
The majorant bounds an error from above; its lower bound is not a
lower bound on the actual correction error.

The TB-rebal high-rate requirement is
297/1000-4800s-5r/sqrt(s)>0, and its norm controls512||h||2.
For s>0, every allowed L2 radius is less than
(297/1000-4800s)sqrt(s)/(5*512). Maximizing this cubic in sqrt(s)
gives its squared supremum323433/2621440000000000000 and(1),
checked by positive exact rational squares. No attainability is used.

## Monotonicity and directed endpoint repair

Let e=delta/(-q-1)>0. Each cutoff has the form A beta^(-e)-B0,
with A>0,B0>=0, so it strictly decreases with beta. Therefore its
upper value on the new interval occurs at3.5125e-7 and its lower
value occurs at3.5126e-7. The old interval[3.5124e-7,3.5125e-7]
does not contain b. Its upper bounds remain conservative at b;
its lower bounds need not do so. The finite audit independently
reconstructs B,Phi,g0,v0 from exact JSON, computes b from its exact
square and checks all63 individual displayed endpoints from the old
bracket, new bracket and exact-radius rows. Every comparison is made
against a rational printed endpoint in its required direction.

For the exact-radius007 row, K(b;Phi,v0)<0.6372612<0.6372628,
so the old lower endpoint is refuted without relying on approximate
floating equality. The replacement common upper0.6720573 lies below
0.7930365<Emin. Thus the repaired exclusion follows strictly. The two
small Db targets and other proposed velocity estimates remain outside
this finite audit and retain their previously stated OPEN scope.

## Evidence and limits

The manifest freezes revision3, revision2, the peer17-check result and
program for inspection, all exact candidate endpoint inputs, the accepted
finite-radius and family-ceiling proofs and results, and a dated hash
observation of every direct peer input. Own code executes no peer program
and no new spatial integral. Arb enclosures use768bits; proofs precede
implementation. Passing the checker accepts the finite row repair and
its stated one-way implications, not every surrounding report sentence.
