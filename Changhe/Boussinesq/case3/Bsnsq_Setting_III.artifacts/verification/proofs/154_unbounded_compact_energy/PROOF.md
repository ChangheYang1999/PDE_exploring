# Compact twists make the finite-part energy unbounded above

Status: CONFIRMED independent proof, controls and actual Opus5.5 review completed 2026-10-21T10:23:59.814382+00:00. No B2 existence or nonexistence endpoint.

## 1. Statement and hypotheses

Let beta>2 and let smooth whole-plane Psi,Theta satisfy the assumptions of152: Psi is odd and Theta even under S(x,y)=(-x,y), V=J gradPsi with J(a,b)=(-b,a), V(0)=0, V=o(r), Omega=-DeltaPsi, W=beta X+V, the canonical relative inverse ofOmega exists and equalsV, and

    W.gradTheta=(beta-2)Theta.

Suppose the disk energy

    E_R=int_(|X|<R) (|V|²/2+yTheta)

has a finite power/log expansion with constant coefficient E_fp and remainder o(1). Put f=W.gradOmega+Omega-Theta_x.

Fix a closed disk B_R0(c) contained in x>0 and separated from the material center and every region to be held fixed. Its reflected disk is disjoint. There is a one-parameter family of smooth compact area-preserving conjugacies, identical outside these two disks, for which the transformed fields retain every hypothesis, the complete exterior fields, the center data and the exact thermal equation, and

    E_fp(epsilon)=a epsilon²+O(1+|epsilon|), a>0.       (1)

Here a, the implicit constant, the disks and the base fields are fixed. In particular the finite-part energy tends to positive infinity in both parameter directions. If f is compact, it remains compact and all three affine moments int f, int x f, int y f are unchanged.

Only the temperature's signs are retained globally. No vorticity sign, bound uniform inepsilon on interior derivatives, or decreasing residual norm is asserted.

## 2. An explicit smooth compact flow

Choose a smooth real function kappa(r) compactly supported in an annulus 0<r_-<r<r_+<R0, with kappa' not identically zero. Put

    h_c(X)=-int_(|X-c|)^R0 t kappa(t)dt

inside the right disk and0 outside it, and define h(X)=h_c(X)-h_c(SX). The radial integral is constant nearc and zero near the disk boundary; hence h is smooth, compact and odd. H=J grad h equals kappa(r)Jz on the right disk, where z=X-c and r=|z|. Its flow there is exactly

    Phi_epsilon(c+z)=c+R_(epsilon kappa(r)) z,         (2)

where R_alpha is rotation byalpha. The radius is unchanged, so the inverse is obtained by replacingepsilon with-epsilon. The flow is the identity outside the two disks and commutes with S. On the left disk the angle is the reflected angle with reversed sign. The determinant is1, either by the polar map (r,theta)->(r,theta+epsilon kappa(r)) or divH=0.

Define

    W_epsilon=(Phi_epsilon)_*W,
    Theta_epsilon=Theta o Phi_epsilon^(-1),
    V_epsilon=W_epsilon-beta X.

Packet152 gives the explicit stream

    Psi_epsilon=Psi+int_0^epsilon (W_t.grad h-2beta h)dt,

so Psi_epsilon-Psi is compact in the same two disks. In particular all fields outside them, and all center derivatives, are fixed. Its compact Poisson correction has canonical velocity J grad(Psi_epsilon-Psi), with zero velocity near the material center0; thus the canonical relative inverse is retained. Exact thermal transport follows by the chain rule for the pushforward. All signs and values ofTheta are retained by composition. This proof uses the smooth complete flow for every finiteepsilon, not a small-parameter approximation. The centers of the twist disks are c andSc, distinct from the material center0. In each disk's hole r<r_-, the flow and velocity are unchanged but the stream correction can be a nonzero constant: on the right it equals-2beta epsilon h_c(c), with opposite sign on the left. This is part of the compact stream correction and must be retained in any stream-weighted residual integral. No stream invariance in these two holes is claimed.

## 3. Exact kinetic-energy transformation

Work first on the right disk, and use Y=c+z as its integration variable. Set

    alpha=epsilon kappa(r),
    A(Y)=W(Y)-beta z,
    B(Y)=(kappa'(r)/r) Jz (z.W(Y)).

Differentiating(2) in the directionW gives

    D Phi_epsilon(Y) W(Y)
                    =R_alpha[W(Y)+epsilon B(Y)],
    V_epsilon(Phi_epsilon(Y))
                    =R_alpha[A(Y)+epsilon B(Y)]-beta c.    (3)

The formula extends smoothly throughr=0, because kappa'=0 there. Area preservation lets us compute the transformed kinetic energy on the same disk inY. Expanding the square in(3), subtracting its epsilon0 value, and using orthogonality ofR_alpha gives the exact identity

    Delta K_right
      =epsilon²/2 int |B|² + epsilon int A.B
        -beta int c.[(R_alpha-I)A+epsilon R_alpha B].       (4)

All integrals here and below are over the right disk unless specified. The last two terms are bounded in absolute value by

    |epsilon| int (|A||B|+beta|c||B|)
                                +2beta|c| int |A|.         (5)

The bound uses only |R_alpha|=1 and compactness. The reflected disk contributes the same kinetic-energy difference: the base W obeys W(SY)=S W(Y), and the constructed flow commutes withS. Thus the coefficient ofepsilon² for the two disks together is

    a=int_(right disk) |B|².                              (6)

No oscillatory averaging or approximation is needed.

## 4. Positivity of the quadratic coefficient

For any circle |z|=r within the right disk, the divergence theorem and divW=2beta give

    int_0^(2pi) z.W(c+r e(theta)) dtheta =2pi beta r².     (7)

Indeed z.Wdtheta=W.n ds on this circle. Cauchy-Schwarz therefore gives

    int_0^(2pi) (z.W)² dtheta >=2pi beta² r^4.             (8)

Since |Jz|=r, formula(6) becomes

    a=int_0^R0 kappa'(r)² r
                     int_0^(2pi)(z.W)² dtheta dr
       >=2pi beta² int_0^R0 kappa'(r)² r^5 dr >0.          (9)

The strict inequality follows from beta>0 and the nonzero smooth derivative ofkappa. It does not require W to be nonzero pointwise, radial, or transverse to each of these circles.

## 5. Temperature and finite parts

The potential-energy difference on the right disk is exactly

    Delta P_right=int [Phi_epsilon(Y)_2-Y_2]Theta(Y)dY.

The displacement is (R_alpha-I)z, so its absolute value is bounded by2R0. Hence

    |Delta P_right|<=2R0 int |Theta|,                     (10)

uniformly inepsilon. The reflected disk obeys the same bound. Equations(4)-(10) prove(1) for the ordinary difference of the two energies on any disk containing both support disks.

Every exterior field is exactly unchanged. The divergent terms of the original E_R expansion are therefore unchanged, and the finite part changes by this compact ordinary energy difference. This proves existence of each new E_fp and the claimed asymptotic. No individual infinite integral has been split or discarded. For completeness the affine-moment identity can be checked directly. Write chi=Psi_epsilon-Psi and deltaTheta=Theta_epsilon-Theta. Both are compact. Oddness makes int deltaf=int y deltaf=0. Compact integration by parts in the remaining moment gives

    int x deltaf= (1-3beta)int x(-Delta chi)
                -int delta(V_1 Omega)+int deltaTheta
              =int deltaTheta.

The first integral is0 because x is harmonic. The second is0 because

    V_1 Omega=partial_x(Psi_x Psi_y)
                    +partial_y((Psi_y²-Psi_x²)/2),

whose difference is a compact divergence. Finally the two support disks are preserved by the area-preserving map, so change of variables on their union gives int deltaTheta=0. This proves all three affine-moment invariances without requiring separate integrability of the baseTheta orV. It is the same compact-difference identity as142/152.

## 6. Application and scope

Take a zero-affine-moment compact-residual configuration from148 with a polynomial B2 core larger than a prescribed protected disk. Choose the right twist disk and its reflection inside that core and outside the protected disk. All hypotheses above hold by150 and151. The annulus where the vorticity residual is known to be nonzero is outside the twists and unchanged. The negative-vorticity point retained by148 is also outside the polynomial core and remains unchanged. Thus for every finiteepsilon these are nonprofiles with the original prescribed center/core disk, exact thermal transport, nonnegative nontrivialTheta, canonical full-plane inverse, a nonzero compact f and all three affine moments zero, while E_fp is unbounded above along the family.

For beta outside Z_crit={M/N>2: M,N coprime positive integers,N<=3}, their common exterior dipoleD is0 by148-150. For beta outside Z_E={M/N>2: M,N coprime positive integers,N<=4}, an exact classA profile would require E_fp=0 by151; the twist family shows that the other retained conditions do not bound E_fp from above or imply that necessary equality.

This does not provide an energy of both signs, a zero crossing, a prescribed finite energy, residual repair, a positive-vorticity family, or any exact B2 profile. The existence of the base configuration in this application uses the precise conditional construction and dependencies in148, not a new gluing proof. The elementary unboundedness result itself needs only the hypotheses in section1 and packet152's compact inverse identity, which has been restated in section2.

Written UTC 2026-10-21T10:13:38.313696+00:00. This initial draft preceded the independent controls and actualOpus5.5 review.

Review237 refinements UTC 2026-10-21T10:17:10.363551+00:00: explicitly distinguish the material center0 from the twist centersc,Sc and retain their constant stream corrections; include a direct compact affine-moment proof. Its final remark about nonzero first variation for every twist is not assumed: a sign-changingkappa may have int xh=0. The positive quadratic coefficient remains strict independently of this first moment.

Final audit UTC 2026-10-21T10:23:59.814382+00:00: nine exact controls and nine numerical manufactured cases (72 finite twists) passed, elapsed5.124596327s. The first controls used the pre-refinement proof snapshot retained in verification/proof_before_review237_refinements.md; the refinements add the explicit compact affine-moment calculation and clarify the constant stream values in the two holes. No formula tested by the controls changed. ActualOpus237 returned a complete written confirmation with these refinements; request238 returned no written audit and is not an endorsement. Focused239 returned a complete written answer agreeing that a vanishing first variation invalidates the universal inference, without proving absence of a two-sided higher-order change. Indeed int_disk h_c=-pi int t^3 kappa and int xh=2c_x int_disk h_c. Two disjoint positive bumps with a compensating negative coefficient make this moment0 while kappa' is nonzero. A deliberately nonnegative nonzero kappa instead gives a nonzero derivative on the polynomial patch and changes energy on both sides of its base value. Neither statement implies both absolute signs or a zero crossing.
