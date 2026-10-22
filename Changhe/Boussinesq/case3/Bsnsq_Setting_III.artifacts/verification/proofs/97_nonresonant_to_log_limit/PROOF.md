# The source-inverse constant as the basis exponent approaches three

Written 2026-10-21T00:45:11.786364+00:00. Complete informal proof before computation. This compares the canonical source inverses of packets93 and95. It is not a statement that any source solves a B2 transport equation.

## 1. Definitions and claims

Fix L>0 and a real C³ function S on[0,1], piecewise polynomial on a finite partition and polynomial near1. For2<b<=3 define

    z_b=(1+r²/L²)^(-1/(2b)),
    q_b(r)=r z_b^(b+1) S(1-z_b), Omega_b=q_b(r)cos(theta).

The same conclusions for the vertical constant hold if q_b is the first cosine coefficient of the finite angular source of93/95. Use the prompt canonical centered inverse. Put f(z)=S(1-z), f0=f(0), f1=f'(0), f2=f''(0)/2 and alpha=L² f2. For2<b<3 let C_b be the constant after subtracting the first two homogeneous velocity terms, as in93. Let C_3 be the constant at b=3 with logarithm log r and angular correction specified in95. Define

    delta=3-b, epsilon=delta/b,
    H_b=integral_0^1 z^-b [f(z)-f0-f1z-f2z²]dz,
    J_3=H_3-f0/2-f1.

The precise parameter-limit identities are

    C_b=-b alpha/(2 delta)
         -(b L²/2)[H_b+f0/(1-b)+f1/(2-b)],             (1)
    lim_(b up to3)[C_b+b alpha/(2 delta)]
           =-(3L²/2)J_3,
    C_3=lim_(b up to3)[C_b+b alpha/(2 delta)]
                      +alpha[1/4+(log L)/2].          (2)

The pole in C_b cancels the pole in its third homogeneous inverse at every fixed exterior point. More precisely, let e2=(0,1), c=cos(theta), d=sin(theta), and

    u_(2,b)=alpha (L/r)^epsilon/[epsilon(2-epsilon)] e2
             +alpha (L/r)^epsilon/(2-epsilon)(cd,-c²).

Then, uniformly on every compact radial annulus and with any fixed spatial derivative,

    C_b e2+u_(2,b)
       -> -(alpha/2)log(r)e2+(alpha/2)(cd,-c²)+C_3 e2. (3)

The comparison is not uniform over the whole exterior r>=r0 when alpha!=0. Thus a large separate C_b near b=3 need not mean that the centered velocity is large at fixed spatial points.

## 2. Finite-part derivation and parameter continuity

Packet93 proves the convergent ordinary-moment identity

    C_b=-(b L²/2)[integral_0^1 z^-b(f-f0-f1z)dz
                           +f0/(1-b)+f1/(2-b)].

Subtract f2z² inside the integral and integrate it exactly: its integral is f2/(3-b). This gives(1) without rearranging divergent improper integrals. Taylor's theorem gives |f-f0-f1z-f2z²|<=M z³. Thus for b in any fixed interval[b_*,3], b_*>2, the integrands of H_b are dominated by M, and dominated convergence gives H_b->H_3. In fact H_b-H_3=O(3-b), since |d(z^-b)/db|=|log z|z^-b and the remainder bound makes its integral uniformly finite. The other denominators stay away from0. Taking the limit in(1) proves the first limit in(2).

Packet95 gives C_3=alpha/4-(3L²/2)J_3+(alpha/2)log L. This is exactly(2). For completeness, the alpha/4 is from the mean of the angular velocity correction, which is -alpha e2/4; the log L is from the change between z and the physical radius. Omitting either changes the canonical log-r normalization.

## 3. Cancellation with the third homogeneous inverse

The third first-cosine source coefficient is B_(2,b)=L^(1+3/b) f2=alpha L^epsilon, with source B_(2,b)r^(-1-epsilon)cos(theta). Its homogeneous stream is

    Psi_(2,b)=B_(2,b) x r^-epsilon/[epsilon(2-epsilon)].

Indeed Delta(r^k cos(theta))=(k²-1)r^(k-2)cos(theta), and k=1-epsilon. Applying V=(-Psi_y,Psi_x) yields the displayed formula for u_(2,b). This homogeneous stream is an exterior term; its singular source at0 is not assigned an ordinary centered velocity there.

Since b/(3-b)=1/epsilon, the pole in(1) is -alpha/(2epsilon). At every fixed r>0,

    (L/r)^epsilon=1+epsilon log(L/r)+O(epsilon²),
    1/(2-epsilon)=1/2+epsilon/4+O(epsilon²).

Consequently

    alpha (L/r)^epsilon/[epsilon(2-epsilon)]
        -alpha/(2epsilon)
       ->alpha[1/4+(log L-log r)/2],

and the second vector term tends to alpha(cd,-c²)/2. Combining this with(2) proves(3). The Taylor expansions and any fixed number of spatial derivatives are uniform on compact annuli. A more explicit remainder there is O(epsilon), with constants depending on the annulus and S. No uniform statement as r tends to infinity is implied: for each fixed epsilon>0, u_(2,b)->0 while the right-hand side of(3) has the unbounded term -(alpha/2)log(r)e2 if alpha!=0. Their difference is therefore unbounded over the full exterior. The scale |epsilon log(r/L)|~1 identifies why interchanging the two limits fails.

The complete centered velocity of Omega_b also converges to that of Omega_3 at every fixed X. To justify this independently of the tail expansion, write the canonical relative kernel integral. Uniformly for b near3 the source is O(r) near0 and O(r^-1/3) at infinity; at fixed X the relative kernel is O(r^-2) in the far field. These give an integrable dominating function there. Near the two locally integrable kernel singularities use local boundedness, uniformly inb, and continuity inb of q_b. Dominated convergence applies, uniformly on compact X-sets by the same local split and bounded source envelopes. This reinforces that the divergent tail constant alone is not a local-field divergence.

## 4. Families satisfying C_b=0 and a useful exact example

Let S_b vary with b and converge to S_3 in C³([0,1]) as b increases to3, with L fixed. The estimates in section2 remain uniform, since the Taylor remainders have uniformly bounded C³ coefficients. If C_b=0 for all suchb, (1) gives

    alpha_b=O(3-b), hence alpha_3=0.                  (4)

It does not force C_3=0. Explicitly, take

    S_b(t)=1+[(3-b)/(b-1)](1-t)²,  2<b<3,
    S_3(t)=1.

The exact manufacture formula of93 gives

    C_b=bL²/[2(b-1)]
          -[(3-b)/(b-1)] bL²/[2(3-b)]=0.

Here alpha_b=L²(3-b)/(b-1), so alpha_3=0, whereas95 gives C_3=3L²/4, nonzero. Each Omega_b is a smooth strictly positive first-cosine source on x>0, but has center strain0. Therefore these are not B2 profiles. The example proves only that the nonresonant C=0 constraint can limit to the resonant alpha=0 constraint without also imposing C_3=0.

## 5. Dependencies and scope

The convergent canonical moment identities of93 and95 are used explicitly and reconnected by the displayed calculations. All parameter limits, signs and cancellation are proved here. No global PDE, positive-profile existence, interval bound or formal verification is asserted. Numerical checks will be placed in verification after this proof. Full B2 remains OPEN.
