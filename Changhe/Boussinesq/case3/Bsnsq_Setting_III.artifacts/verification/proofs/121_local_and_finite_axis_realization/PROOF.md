# Local realization, finite-axis realization, and the compact-exterior obstruction

Written 2026-10-21T04:13:50.745939+00:00, before this packet's numerical or symbolic implementation. Independent audit of the lead's T1, T2 and T3 in astra/local428/answer.md. Status: CONFIRMED by the complete informal arguments and the independent symbolic controls; see verification/SUMMARY.md for model availability and numerical limitations. These results construct configurations satisfying only part of B2-P or exclude a restricted family. None gives a full YES or NO.

## Common hypotheses and base field

Fix beta>2 and a0>0. Put l=(beta-2)/2, mu=1+3beta/2, c=1+beta/2, q0=4a0/beta, Lambda=2mu=3beta+2 and M=2beta+1. Set

    p=(beta-1)/(2beta), L=3c sqrt(beta)/(4a0), h=sqrt(beta)L,
    S=L^2+x^2+(y-h)^2, S0=L^2+h^2,
    B=c/(2ph S0^(p-1)), Psi_e=-Bx S^p,
    Omega_e=4Bp x S^(p-2)[2L^2+(p+1)(x^2+(y-h)^2)].

The stream is odd in x; Omega_e/x is positive everywhere. The actual velocity is U_e=(-Psi_e,y,Psi_e,x); its relative value defines W_e=beta X+U_e-U_e(0). Packet119 proves, using the explicit field and the canonical whole-plane inverse, that W_e,1/x>=l, b_e'>=l for b_e=W_e,2(0,y), DU_e is bounded, and the whole plane is its backward basin. Its derivatives have the slow algebraic tails stated there. Let ell=Psi_e,x(0)=-B S0^p. Direct Taylor expansion gives

    (Psi_e)_(<=3)=ell x+cxy-q0 x^3/6.

In particular there is no xy^2 term. The latter identity follows from L^2+(2p-1)h^2=0.

We use the following consequence of the proof in packet119. If a smooth odd stream perturbation preserves the center 2-jet, keeps W1/x and b' bounded below by a positive constant, has bounded second stream derivatives, and its induced velocity is sublinear, then the backward flow is complete and tends to the origin. The integral construction xi=x exp[-int_0^infinity (W1/x-l)(phi_(-t)X)dt], first on a small backward-invariant neighborhood and then extended along trajectories, gives smooth odd xi with W.grad xi=l xi and xi=x+O(|X|^2). Its square Theta=a0 xi^2 is smooth, positive off x=0, has the correct center jet and solves (T). The proof controls every derivative of the backward flow near the source, so the integral is C-infinity. For any such field, sublinearity gives the polynomial temperature bound C(1+r)^[2(beta-2)/beta].

## T1: the full system on a small disk

There exists such a full-plane configuration, with Omega>0 on x>0 and unchanged base exterior, for which both defining transport equations hold on a disk about the origin.

Let P=ell x+cxy-q0 x^3/6. Then -Delta P=q0x and

    W_P=(l x,mu y-q0x^2/2), Theta_P=a0x^2.

Therefore W_P.grad Theta_P=2l Theta_P=(beta-2)Theta_P and W_P.grad(q0x)+q0x=(l+1)q0x=2a0x=Theta_P,x. These are exact identities. P alone is not admissible globally because its velocity grows quadratically.

Take an even radial smooth cutoff chi equal to one on the unit disk and zero outside radius two. Put delta_rho=chi(X/rho)(P-Psi_e), Psi=Psi_e+delta_rho. Since P is the cubic Taylor polynomial, Taylor's theorem and the product rule give ||delta_rho||_C^k <= C_k rho^(4-k) for 0<=k<=3 as rho tends to zero. On a fixed ball containing its support let m0=min Omega_e/x>0. Oddness and the fundamental theorem of calculus imply |Delta delta_rho/x|<=2||delta_rho||_C^3, so Omega/x remains positive for small rho. The same argument bounds the changes of W1/x and b' by ||delta_rho||_C^2, preserving their positive lower bounds. The perturbation is compact, vanishes through degree three at zero, and does not change U(0). Its perpendicular gradient is exactly the canonical relative inverse of -Delta delta_rho: the difference from that inverse is divergence-free, curl-free, sublinear and zero at zero, hence zero by componentwise harmonic Liouville. The tails, center relations and global basin follow.

On |X|<rho the stream equals P. Moreover

    X.W_P=l x^2+mu y^2-(q0/2)x^2y
          >=(l-q0rho/2)|X|^2.

Choose rho<=l/q0. The disk is backward invariant, and every backward trajectory inside it stays in the polynomial region. There W1/x=l, so the defining integral for xi is zero and xi=x. Thus the globally constructed Theta equals a0x^2 throughout the disk, and both equations hold there. This does not assert an exact solution on any fixed large disk or on the whole plane.

For completeness the naive large-cutoff limit loses positivity. Fix chi above and write F(Z)=z1^3 chi(Z). On the right half-plane, integration by parts twice gives int z1 Delta F=0: F and its first x derivative vanish at x=0, and it is compactly supported. Yet Delta F=6z1>0 near the origin, so it is negative somewhere with z1>0. For the same cutoff formula at radius rho tending to infinity, the cubic part dominates because Psi_e grows with degree 2-1/beta<2, whereas P has degree three. At a fixed such point Z,

    Omega_rho(rho Z)/rho -> (q0/6) Delta F(Z)<0.

This refutes only that fixed large-cutoff family, not arbitrary large-disk realization.

## Regular singular ODE lemma

Let b,d,f be smooth on an interval containing zero, b(0)=0, b'(0)=mu>0, yb(y)>0 for y!=0, and d0=d(0)>0. Then b u'+du=f has exactly one solution smooth and bounded at zero; it extends throughout the interval. Define

    z(y)=y exp(int_0^y [mu/b(s)-1/s]ds),
    H(y)=exp(int_0^y [d(s)-d0]/b(s)ds).

The integrands extend smoothly across zero. Also bz'=mu z and z'>0, so z is a smooth local coordinate throughout the interval. For v=Hu, F=Hf the equation is mu z v_z+d0 v=F. Its unique bounded solution is

    v(z)=int_0^infinity exp(-d0 t) F(exp(-mu t)z)dt.

On every compact z interval, differentiation under the integral is justified by exp[-(d0+jmu)t] for derivative order j. The formula is smooth, solves the equation by integration by parts in t, and its homogeneous alternatives are proportional to |z|^(-d0/mu), which are unbounded at zero. Positivity of f implies positivity of u by the displayed positive integral, or by continuing its positive solution along the outward flow of b. For the homogeneous case d0=0=f, the unique solution with assigned u(0) is u(0)/H.

## T2: all vorticity residual jets on any finite axis segment

For every finite Y0>0 there is a smooth full-plane configuration with all the base positivity, tail, gauge, center and global-basin properties, with (T) exact, and with every derivative of R_Omega zero at every (0,y) with |y|<=Y0. It may also be chosen to satisfy both equations exactly on a small disk. This is infinite-order vanishing on a segment, not vanishing on a neighborhood of that segment.

Here are the complete recurrences. Write formal x expansions with smooth y coefficients

    Psi=sum_(j>=0) x^(2j+1) g_(2j+1)(y),
    Omega=sum_(j>=0) x^(2j+1) w_(2j+1)(y),
    Theta=sum_(m>=1) x^(2m) a_(2m)(y),
    b=beta y+g1(y)-g1(0), A=beta-g1'=2beta-b',
    w_n=-g_n''-(n+1)(n+2)g_(n+2) (n odd).

The coefficient of x^(2m) in (T) is

    b a_(2m)'+(2mA-2l)a_(2m)
      +sum_(j=1)^(m-1)[(2j+1)g_(2j+1) a_(2m-2j)'
                       -(2m-2j)g_(2j+1)' a_(2m-2j)].             (1)

The coefficient of x^n in R_Omega for odd n is

    b w_n'+(nA+1)w_n-(n+1)a_(n+1)
      +sum_(j=1)^((n-1)/2)[(2j+1)g_(2j+1) w_(n-2j)'
                          -(n-2j)g_(2j+1)' w_(n-2j)].             (2)

Both formulas follow by multiplying the two components of W by the appropriate derivatives; every term of each degree is included.

First fix g1 equal to the base g1. Equation (1) for m=1 is b a2'=(2b'-Lambda)a2, with a2(0)=a0, hence a2=a0 exp int_0^y(2b'-Lambda)/b>0. The integrand is smooth. Solve bq'+(M-b')q=2a2 by the lemma: its center coefficient is M-mu=beta/2>0. Thus q is positive and q(0)=4a0/beta. Put g3=-(q+g1'')/6. Inductively, when g1 through g_(2k+1) are known, (1) for m=k+1 is an ODE for a_(2k+2) with center coefficient 2k l>0. Equation (2) for n=2k+1 then determines w_(2k+1) by an ODE with center coefficient (2k+1)l+1>0. Define g_(2k+3) from the elliptic identity. The lemma produces smooth coefficients on any fixed larger finite interval. No convergence in x is asserted.

It remains to realize these coefficients while preserving positivity. Choose Y2>Y1>Y0 and a smooth cutoff vartheta(y) supported in (-Y2,Y2) and equal to one on [-Y1,Y1]. Set h(y)=vartheta(y)(q(y)-q_e(y)). Then q_e+h is a convex combination of two positive functions. On this compact interval there is m0>0 below both q_e and q_e+h. Let eta be a smooth nonincreasing function equal to one at arguments <=0 and zero at arguments >=1. Define an even cutoff

    chi(x)=eta(1+log(|x|/eps)/L_c),

extended by one near zero. It is one for |x|<=eps exp(-L_c), zero for |x|>=eps, and satisfies |x chi'|+|x^2 chi''|<=C/L_c when L_c>=1. Add delta3=-h(y)x^3 chi(x)/6. Direct differentiation gives

    -Delta delta3/x=h[chi+x chi'+x^2 chi''/6]+(h''/6)x^2 chi.

Since Omega_e/x=q_e+O(x^2) uniformly on the compact y interval, the corrected quotient equals q_e+chi h plus an error at most C||h||/L_c+C'eps^2. The main term is at least m0. Choose L_c large and then eps small to make the error below m0/2. Also |delta3,y/x|<=||h'||eps^2/6, so W1/x retains a positive bound; g1 and b are unchanged. Outside this compact rectangle nothing changes.

Now for each odd n>=5 let d_n(y)=vartheta(y)(g_n-g_n^e), or subtract the coefficients of the already corrected reference; these are equal for n>=5 because chi is one near zero. Choose an even ordinary cutoff chi0 and eps_n tending to zero so that

    ||x^n d_n(y) chi0(x/eps_n)||_C^(n-1)<=2^(-n) tau.

This is possible by the product rule since n derivatives have not yet been taken, and d_n has compact y support. The sum over n>=5 converges in every C^k, is smooth and compactly supported, has the prescribed x Taylor coefficients, and is C^3-small. It leaves g1 and g3 unchanged. Its vorticity quotient changes by at most 2tau; its W1/x changes by at most tau. Choosing tau small preserves positivity and the basin estimates.

Construct the actual global temperature from xi. Its x Taylor coefficients obey (1), and smoothness across y=0 supplies the bounded solutions selected by the lemma. Induction and uniqueness identify them with the prescribed a_(2m) on [-Y1,Y1]. The actual vorticity Taylor coefficients are the prescribed w_n there. Equation (2) therefore vanishes for every odd n; even n vanish by parity. Since each coefficient vanishes on an open interval containing [-Y0,Y0], all mixed derivatives vanish there as well.

To combine with T1, start instead with the T1 reference stream. Its g1 gives b'>0 and equals the polynomial g1 near zero. The same ODEs then produce exactly the polynomial solution coefficients on that central interval, by uniqueness; the correction coefficients vanish there. All added terms are zero in a horizontal strip about y=0. A smaller disk of the T1 reference is unchanged, including its invariant backward trajectories and temperature. The finite-axis and local exact properties hold simultaneously.

## T3: a compact exterior perturbation cannot satisfy the full axis equation

The first axis vorticity equation already fails somewhere for any configuration with (T), a(y)>0 on the whole axis, and with vorticity equal to Omega_e outside a compact set, whose relative velocity is the canonical inverse. In particular T1 and T2 cannot be extended to the whole axis while keeping this exterior.

Let t=2p=1-1/beta, Q_e=4Bp(p+1)>0. Parameterize the lower axis by y=h-r, r tending to infinity. For the base velocity and vorticity,

    b_e=-beta r-B r^t+C+O(r^(t-2)),
    b_e'=beta+Bt r^(t-1)+O(r^(t-3)),
    q_e=Q_e r^(t-2)(1+O(r^-2)),
    q_e'=(2-t)Q_e r^(t-3)(1+O(r^-2)).

Consequently the nominal r^(t-2) terms cancel in H_e=b_e q_e'+(M-b_e')q_e, since beta(t-2)+beta+1=0. The first remaining term is

    H_e=-2B Q_e r^(2t-3)+O(r^(t-3))
       =-2B Q_e r^(-1-2/beta)(1+o(1))<0.            (3)

The coefficient -2 is the sum -(2-t)-t. If delta Omega is smooth compactly supported and odd in x, its total mass is zero. Taylor expansion of the full-plane Biot-Savart kernel outside the support gives delta U_abs=O(r^-2), Ddelta U_abs=O(r^-3). Passing to the relative inverse adds a constant. Thus b changes by a constant plus O(r^-2) and b' by O(r^-3); q_e is unchanged outside the support. The resulting error in H is O(r^(t-3)), of smaller order than (3). Hence H remains negative far down the axis, whereas the full axis equation would require H=2a>0, a contradiction.

If the actual velocity agrees with U_e outside a compact set but its center value changes, b differs from b_e there by a constant. Formula (3) still applies. However the particular formula F_e'(0) in packet119 must not be reused without accounting for this constant. For unchanged U(0), that packet also excludes vanishing of the axis residual on any exterior open interval. These are restricted obstructions for this base exterior, not obstructions for the broad B2 class.

## Dependencies and verification plan

Dependencies: explicit base field and global xi construction in packet119; elementary smooth cutoff/Borel construction, harmonic Liouville uniqueness for the declared canonical inverse, and the displayed regular singular ODE lemma. No lead or numerics code is used. Planned controls independently differentiate the full polynomial PDE and compare the all-axis recurrences, reproduce the base jet and F derivative at several exact beta, and check (3) at high precision. Such controls check formulas; the infinite-order realization is established by the informal argument above, not by truncation tests.
