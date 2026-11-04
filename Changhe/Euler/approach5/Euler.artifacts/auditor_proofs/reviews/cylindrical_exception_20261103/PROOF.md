# Full Poisson obstruction at the cylindrical scalar exception

Status: CONFIRMED at the exact warped local and Euclidean circular prescribed-vorticity scopes, A744-A745. The full Poisson equation excludes the pair left by A743.

## 1. Local statement and notation

Let r>0,F>0 and G be C2 functions of h on an open interval. On coordinates(theta,h,z) use the metric r(h)^2 dtheta^2+dh^2+dz^2 and positive volume r dtheta dh dz. Let f be C2 and nonzero on a connected phase arc J. Suppose fixed real numbers lambda,eta,E satisfy eta E!=0 and

    f''=lambda f-eta f^3,
    (f')^2=lambda f^2-(eta/2)f^4+2E.                    (1)

Suppose J contains a compact subarc on which two regular branches take each f value in a nonempty open nonzero interval, with opposite derivative signs. Put chi=theta+G(h), w=F(h)f(chi), and take the contravariant field

    W=w partial_theta-z w_theta partial_z.

If a C2 field V near the central strip satisfies

    curl_g V=W, div_g V=0, <V,W>_g=0,                  (2)

then V^z(theta,h,0)=0 on J after a possible restriction of the h interval. In fact the associated scalar potential below is independent of its characteristic coordinate I near0. If additionally G' is nonzero at any h under consideration, no such V exists on the two-branch strip at all.

In the special Euclidean cylinder r=R+h,R>0, combining this local lemma with the independently reconstructed necessary-pair theorem yields: for every p>0,beta!=0 and every nonconstant C2 real periodic f, the exact field

    W=h^p f(theta+beta log h) partial_theta
                 -z h^p f'(theta+beta log h) partial_z

admits no C2 V satisfying (2) on a whole circular collar. This is a curl/divergence/helicity theorem, with no Euler equation or decay assumption. It does not reduce arbitrary Euler periodic tubes to this form.

## 2. The local potential and its common domain

The one-form alpha0=-r z w dh satisfies d alpha0=i_W(r dtheta dh dz). Its metric dual is V0=-r z w partial_h, with curl_g V0=W, <V0,W>=0 and

    div_g V0=-(z/r)partial_h(r^2 w).

On a simply connected phase strip (2) therefore gives a scalar q with

    V^flat=alpha0+dq,
    Delta_g q=(z/r)partial_h(r^2 w),
    w q_theta-z w_theta q_z=0.                         (3)

The potential is C3 because all components of its first differential are C2. The last equation has characteristic invariant I=z w, with h fixed. Choose a reference phase inside the compact two-branch arc. After restricting to a compact smaller h interval, F and |f| have positive lower bounds on this arc. Consequently, for all sufficiently small |I|, every characteristic segment between a phase of the arc and the reference stays inside the original coordinate strip: its z coordinate is I/w. There is one function Q, common to both branches, such that

    q(theta,h,z)=Q(h,I), I=z w.

Its regularity is C2, which is all that is used. The reference substitution involves the C2 functions F and G, so asserting Q is C3 would require an extra argument and is unnecessary. The identity V^z=q_z=w Q_I identifies the desired velocity component. Connected portions of J outside the compact arc can use smaller |I| domains but the same derivative Q_I(h,0).

## 3. Full Laplacian, including the inverse-square angular term

Write

    A=F'/F, T=f'/f, C0=(G')^2+r^-2>0,
    L1=2AG'+G''+(r'/r)G',
    L0=F''/F+(r'/r)A.

At fixed theta,z the derivatives of I are I_h=I(A+G'T), I_theta=I T and I_z=w. Applying

    Delta_g=partial_hh+(r'/r)partial_h+r^-2 partial_thetatheta+partial_zz

to Q(h,I), and then substituting (3), gives the exact identity

    0=Q_hh+(r'/r)Q_h
       +2I(A+G'T)Q_hI
       +Q_II{F^2 f^2+I^2[A^2+2AG'T+C0 T^2]}
       +I Q_I[C0(lambda-eta f^2)+L1 T+L0]
       -I[r(A+G'T)+2r'].                               (4)

All derivatives of Q are at the same(h,I). In particular its coefficient functions do not change when the phase is varied at fixed(h,I). Formula (4) uses no derivative beyond order2 of Q,F,G,r,f.

Equation (1) implies T^2=lambda-(eta/2)f^2+2E f^-2. Thus (4) is

    A_T T+A_2 f^2+A_m2 f^-2+A_const=0,                 (5)

where all coefficients depend only on(h,I), and

    A_m2=2E C0 I^2 Q_II,
    A_2=[F^2-(eta/2)C0 I^2]Q_II-eta C0 I Q_I.          (6)

For the optional stronger conclusion, the odd coefficient is

    A_T=2I G' Q_hI+2I^2 A G' Q_II+I L1 Q_I-I rG'.     (7)

These displayed coefficients follow directly from (4). There is no phase dependence hidden in A_const.

## 4. Separation by the two regular branches

Fix h and a small I!=0 in the common domain. Evaluate (5) at the paired phases for each f value in the shared open interval. Their T values are opposite and nonzero, with equal magnitude by (1). Subtracting the two equations gives A_T=0. Then

    A_2 f^2+A_m2 f^-2+A_const=0

on a nonzero open f interval. Multiplication by f^2 gives a polynomial in f^2 on an open interval. Its three coefficients vanish. By (6), E!=0,C0>0,I!=0 force Q_II=0. The other equation and eta!=0 then force Q_I=0. Continuity gives Q_I(h,0)=0. This argument works for every h and all sufficiently small nonzero I; hence Q is independent of I on a neighborhood of0. It proves V^z(theta,h,0)=0 throughout the connected phase interval by the characteristic identity.

For the extra local consequence, Q_I vanishes identically in this open(h,I) region, so Q_hI=0 too. Formula (7) now reduces to A_T=-I rG'. If G'!=0, this contradicts A_T=0. This strengthens the local lemma but is not needed for the earlier exceptional k contradiction. No division by f' at a turning point is made; only the adjacent regular branches enter.

## 5. Every exceptional periodic shape supplies the two branches

The preceding necessary-pair theorem, reconstructed in the team records, says that any hypothetical cylindrical solution must have

    p=1/2, beta^2=1/24, k(h)=(R+h)^2/5,
    V^z(theta,h,0)=k(h)w,
    f''=6f-eta_J f^3                                  (8)

on a nonzero phase interval J inside the component D of the complement of {f=f'=0} used in that theorem. The scalar eta_J is independent of h and phase. The coefficient identities have been compared on a nonempty h interval where k!=0. No matching of eta_J through degenerate endpoints is required.

If f has a zero, choose any nonzero component J inside D. It is a finite open arc with zero endpoint values. The polynomial ODE in (8) extends continuously to its endpoints because f is globally C2. Multiplication by f and integration over J gives

    eta_J integral_J f^4=integral_J (f')^2+6 integral_J f^2>0.

The boundary terms are f f' and vanish. Thus eta_J>0. At either endpoint f' cannot be0: uniqueness for the polynomial first-order system with data(f,f')=(0,0) would otherwise force the solution to be identically0 on J. The conserved energy

    E=(f')^2/2-3f^2+eta_J f^4/4

is therefore positive at the endpoints and constant on J. There is a nonzero interior extremum. Its second derivative cannot vanish, since its data would then be an equilibrium of the polynomial system, again forcing constancy by uniqueness. This strict extremum supplies a compact nonzero two-branch arc with opposite derivatives and eta_J E!=0.

If f has no zero, (8) has one eta on the whole periodic circle. The same integration gives eta>0. There are two different positive extrema of |f| because f is nonconstant and of one sign. If E=0, the energy identity at either extremum would give f^2=12/eta, so the extrema would agree. Hence E!=0. Polynomial uniqueness again gives a strict nonzero extremum and the required two branches.

These arguments cover arbitrary zero sets: only one nonzero component is needed, and no zero-set finiteness or finite vanishing order is imposed. The local lemma now forces V^z=0 on a nonzero subarc, contradicting k=(R+h)^2/5>0 in (8). Alternatively G'=beta/h!=0 contradicts (7) directly. The exceptional scalar pair is therefore excluded by the full Poisson equation.

## 6. Scope and verification

The first scalar coefficient test failed to exclude all positive p and correctly retained an exception. This additional argument uses the full I-dependent equation; it does not reinterpret that earlier computation as having passed. It requires no computation itself. The general warped local lemma uses an exact metric and exact W, and the cylindrical conclusion uses a whole periodic prescribed shape. A general Euler periodic orbit can have different metric cross terms, nonlinear transverse vorticity and no separated angular shape. The high-growth W2 alternative and the main conjecture remain OPEN.

Dependencies are the explicitly displayed metric identities, local exactness of a closed C2 one-form, C2 characteristics, the polynomial Duffing ODE and energy, uniqueness for its locally Lipschitz first-order system, elementary polynomial independence, and the full preceding necessary-pair theorem. They have all been used with their exact regularity and domain restrictions. The full source and independent reconstruction were reread at the final audit recorded in the team records. Continuing configured-model comparison uses the existing working files; no runtime attestation or new model request is claimed.
