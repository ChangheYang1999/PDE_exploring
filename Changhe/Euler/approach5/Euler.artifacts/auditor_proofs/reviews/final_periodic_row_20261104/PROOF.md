# Final check of the complete periodic-orbit row

This is a recheck of the existing AppendixA row after its omega and compact-set qualifiers were repaired. It combines existing A014-A015 and A030 facts; no new profile exclusion is proposed.

## Exact statement

Let 0<c<1/2, omega be any finite real number, and U in C2(R3;R3), P in C1(R3) solve the full rotating Euler profile equation with div U=0. Assume U is uniformly sublinear at infinity. Set A=cI-omega J, B=Ay+U and Omega=curl U.

Here J(y1,y2,y3)=(-y2,y1,0), and the full equation is

    (1-c)U+B.grad U+omega JU+grad P=0, div U=0.

Uniform sublinearity means sup_(|y|>=R)|U(y)|/|y| tends to zero as R tends to infinity. Write Phi for the B flow and Gamma for the maximal Omega flow. A whole-Gamma-invariant compact set means that each of its trajectories exists for every real time and remains in the set. The equation makes grad P continuously differentiable, so its curl may be taken classically.

The following conclusions hold.

1. Every nonconstant periodic B orbit requires omega!=0 and every period T obeys T>=2pi/abs(omega).
2. A nonconstant periodic B orbit on which Omega is nonzero is a saddle: its monodromy multipliers are 1, exp((1+c)T), exp((2c-1)T).
3. Omega has no nonconstant periodic integral curve.
4. The time-one Omega map on every compact set invariant under the whole Omega flow has zero topological entropy.

The last statement is explicitly about compact invariant sets. No entropy for a noncompact domain is claimed. Items1-2 only need the equation in a neighborhood of the relevant orbit. Items3-4 use the global sublinearity assumption. The target uniform velocity decay implies that assumption.

## Period lower bound and saddle multipliers

For the one-form alpha=U dot dy, the exact momentum identity is

    L_B alpha=(2c-1)alpha+d(|U|^2/2-P).

Indeed the vector of coefficients of L_B alpha is B.grad U+(DB)^T U. Substituting momentum, DB=A+DU and A^T=cI+omega J cancels the rotation terms and gives the displayed formula. Integration around a material closed curve multiplies its circulation by exp((2c-1)s). A periodic B orbit is unchanged as an oriented closed curve by its own flow, so its U circulation vanishes since 2c-1!=0 and P is single valued.

Write the orbit Y(t), 0<=t<=T, with Y'=B(Y). Since U(Y)=Y'-cY+omega JY, integration of the derivative of |Y|^2 gives

    E+omega Q=0,
    E=integral_0^T |Y'|^2 dt>0,
    Q=integral_0^T JY dot Y' dt.

Thus omega!=0. Put Z=Y-(1/T)integral_0^T Y dt. Cauchy-Schwarz, |JZ|<=|Z| and the periodic Wirtinger inequality give

    |Q|<=||JZ||_2 ||Z'||_2<=||Z||_2 ||Z'||_2
         <=(T/(2pi))||Z'||_2^2=(T/(2pi))E.

The first conclusion follows. This argument does not cover c=1/2 because circulation need not vanish there.

The curl identity is [B,Omega]=-(1+c)Omega, hence

    Omega(Phi_s x)=exp(-(1+c)s)D Phi_s(x)Omega(x).

At a point of a nonconstant periodic B orbit, B is nonzero and D Phi_T B=B. If Omega is nonzero at one orbit point, transport makes it nonzero at all of them, and D Phi_T Omega=exp((1+c)T)Omega. These two vectors are independent because their multipliers differ. The determinant of D Phi_T is exp(3cT), by div B=3c. Therefore the third multiplier is exp((2c-1)T). For 0<c<1/2 one transverse multiplier exceeds one and the other is less than one. This proves precisely the saddle assertion in the row.

## Backward compact control and the Omega-flow conclusions

Uniform sublinearity makes B complete and radially outward outside a ball: for sufficiently large |y|, B(y) dot y/|y|>=c|y|/2. For any compact set K, choose a larger closed ball D containing it and with B strictly outward on the boundary. Then Phi_(-s)(K) stays in D for every s>=0. Put kappa=1+c>0 and M=sup_D ||D Omega||<infinity.

The transport identity implies the flow conjugacy

    Phi_s Gamma_t=Gamma_(exp(kappa s)t) Phi_s

whenever these trajectories are defined. On a periodic Gamma curve, or on a compact whole-Gamma-invariant set, the required trajectories exist for every t. Conjugacy transfers their completeness to their images under Phi_s; it does not require global completeness of Gamma outside those sets.

If a nonconstant periodic Gamma curve has period T, its image under Phi_(-n) is a nonconstant periodic Gamma curve in D of period exp(-kappa n)T. Every such curve Z has integral_0^Tprime Omega(Z)dt=0. For its time average zbar, Wirtinger and the Lipschitz bound in the convex ball D give

    ||Z'||_2=||Omega(Z)||_2
       <=||Omega(Z)-Omega(zbar)||_2
       <=M||Z-zbar||_2<=(M Tprime/(2pi))||Z'||_2.

The first inequality uses the mean-zero property, which makes subtraction of a constant increase its L2 norm. Nonconstancy therefore forces M Tprime>=2pi, contradicting the shrinking periods. This proves item3, including the case M=0 by immediate contradiction.

For item4, let K be a compact whole-Gamma-invariant set and Kn=Phi_(-n)(K). All Kn lie in D and are compact whole-Gamma-invariant. The conjugacy and the time-scaling law for entropy of a continuous flow on a compact invariant set give

    h_top(Gamma_1 on Kn)=exp(kappa n) h_top(Gamma_1 on K).

For any two trajectories in Kn, their joining segment lies in the ball D, so Gronwall gives distance at time j at most exp(Mj) times their initial distance. A three-dimensional grid covering D at spacing proportional to epsilon exp(-MN) is an (N,epsilon) spanning cover of Kn after choosing a point in each occupied cell. Thus h_top(Gamma_1 on Kn)<=3M for every n. Dividing by exp(kappa n) and letting n tend to infinity proves item4.

## Scope

Each conclusion holds for every fixed finite omega. The proof neither replaces omega by a small parameter nor promotes zero entropy on compact invariant sets to a statement on the entire noncompact phase space. It uses the actual curl relation and the exact Euler circulation identity, not an independently chosen transported vector field. It does not show that every B trajectory escapes or that periodic B orbits cannot exist in a hypothetical decaying rotating profile.

## Dependencies and audit record

This reconstruction combines the exact circulation and period argument of A030 with the transport and compact-flow arguments of A014-A015. Their captured sources and earlier full reread are recorded in the period source manifest and the compact-flow audit. It does not extend those results. The complete original 69-line combined check is retained in the submitted check. The complete existing C comparison is captured here. Its six derivations and three optional scope precisions agree after independent checking. No diagnostic or formal build is used.

Only the exact four conclusions and the zero-circulation step are covered by this recheck. It is not a fresh certificate for the entire report row, the report as a whole, or ancillary equality classifications. The independent ledger determines the verdict.
