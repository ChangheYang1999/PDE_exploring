# Complete reference contract for the exact d2 refit

## Statement and certificate conditions

Let chi be the exact potential nb_d2_exact, with canonical coefficient hash f1e761a9849e7c0af0fba2cc5ba2a9aa83c3f3230727737fe3196ef1b03e07fc. Put c=4076476460239181/2251799813685248, gamma=1/c, delta=1-gamma, rho=-partial_y Delta chi, u=(-chi_xyy,chi_xxy), V=cX+u, r=|X| and <r>=(1+r^2)^(1/2). Every derivative tensor has the full ordered Euclidean norm. All decimal values below, if any, denote exact rationals.

This result is conditional on the three complete matrix certificates and all four complete norm-group certificates in topic95, together with their independent checks. Until the registration record verifies every input, the consolidation is OPEN. Under those certificate conditions, this reference satisfies every reference hypothesis of the parameterized logarithmic theorem89, with

    R=2^31, d=4/9, U3=B3=2^191, B4=2^201,
    Astar=2^189, tau=2^-210, 1/2<beta<=1.

The remaining residual hypothesis of that existence theorem cannot hold. More precisely, set epsilon=2beta-1, Q=(1+tau log(1-Delta))^beta,

    omega1=(1+r^2)^(-1/10), omega2=(1+4r^2)^(2/5),
    w=(1+r^2/R^2)^(-11/10), L(h)=||wh||_(Hdot^-1),
    Mstar(h)^2=||omega2 D^2Qh||_2^2
                   +Astar^2||omega1 DQh||_2^2+Astar^2 2^31 L(h)^2,
    r0=2^-20 tau^beta sqrt(epsilon), eta=r0/32.

The spaces are the S1 compact smooth core completions in these norms, realized as canonical tempered distributions as in89. If F=V.Drho-rho, its finite high norm satisfies

    Mstar(F)>2^178 *1936535207,
    Mstar(F)/eta>2^243.

The membership theorem106 proves that this is the actual finite norm in the compact-core completion. No exact canonical stationary profile of any real exponent lies in the closed Mstar correction ball of radius 2^-15 tau^beta around this reference. In particular the theorem's entire ball of radius r0 is excluded. These are statements about the infinite dimensional correction space, not merely about the finite generator family.

## Verification of the reference hypotheses

The exact source audit19 proves the intended parity, smooth finite-potential form, c+c[rho]=1 and

    a0=rho_y(0)=47238706681952399067752453371665 /
                    4589704466829443526249565650944 >1.

The exponent obeys 9/5<c<37/20. The full leading homogeneous potential equals that of state131. Its nonzero leading density, established by the exact original tail audit05 and the refit audit19, is therefore unchanged. The finite branch expansion supplies uniform convergence T^(-gamma)rho(TX) to that continuous nonzero homogeneous density on compact annuli. All density and velocity derivatives have polynomial growth by the finite-generator proof91. These facts also specify the canonical velocity without an additional harmonic field.

Topic95 supplies

    M=(2c+1)I+sym Du+A >=19I/5,
    Mj=(1+c+V.Dlog omegaj)I-j sym DV+A >=I/2, j=1,2,
    A=[[rho_y,-rho_x/2],[-rho_x/2,0]].

For r<=R the low matrix hypothesis of89 requires only

    M >=[2/5+(11/5)c r^2/(R^2+r^2)] I.

The scalar on the right is at most 2/5+(11/10)c<=487/200<19/5, so the certified global M bound implies it.

The four norm-group certificates in95 give the five fixed caps

    |Du|<=14/5, |D rho|<=16, <r>|D2u|<=3,
    |D2rho|<=3, <r>|D2rho|<=8,

and the decay caps

    r^d|D rho|<=93, r^(1+d)|D2rho|<=93,
    r^(d-1)|u|<=22, r^d|Du|<=22, r^(1+d)|D2u|<=56.

Adding the first two decay bounds gives r^d(|D rho|+r|D2rho|)<=186. This is exactly the first decay hypothesis in89. The remaining three agree with its other decay hypotheses. These statements include the appropriate continuous limits at the origin; ordinary pointwise inequalities hold for every positive radius.

The independent coefficient certificate91 gives

    <r>|D3u|<=2^191,
    <r>^2|D3rho|<=2^191,
    <r>^2|D4rho|<=2^201.

These large but finite constants replace the original fixed higher-derivative requirements. They do not assert the false bound <r>^2|D4rho|<=512. The exact rational parameter audit in91 checks, with a=198+B3/24 and G3=a^2+352,

    Astar>=2048, 7Astar^2>=200G3,
    Kstar=max(525,432+(272U3+816B3)/Astar,
                    312+(1088/3)B3+(2176/(3Astar))B4),
    tau<=2^-20, 768 Kstar tau<=1.

This verifies the complete reference and parameter contract in89.

## Why the residual cannot close the theorem

The annular witness and parameter-uniform proof90 give

    Mstar(F)>(Astar/2048)1936535207.

Here Astar/2048=2^178, proving the asserted floor. Since eta<2^-35 and 1936535207>2^30, division gives Mstar(F)/eta>2^(178+30+35)=2^243. This argument uses the actual native low component of the norm, not an inference from a different high norm.

The same proof90 excludes the closed Mstar ball of radius 2^-15 tau^beta for every prospective exponent. Its radius divided by r0 is 32/sqrt(epsilon)>=32. Thus every correction allowed by the existence theorem's small ball is already excluded. The failure is a verified residual obstruction after all reference hypotheses have been met. It does not rule out a larger correction or a different asymptotic class.

## Dependencies and scope

Source normalization and leading moments:19, with original tail05. Exact global matrix, lower derivative and decay bounds:95. Higher derivative upper bounds and admissible parameters:91. Compatible function-space realization and conditional theorem:89. Native residual witness and exclusion:90. Actual forcing-space membership:106. Registration must bind these actual inputs and may not infer a complete contract from only point samples. This result concerns only nb_d2_exact, not nb_Mpen2_exact. It proves no nonlinear existence result.
