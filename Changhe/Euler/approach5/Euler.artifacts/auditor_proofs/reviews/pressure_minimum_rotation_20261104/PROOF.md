# A central pressure minimum and the sharp rotation threshold

Status: CONFIRMED A2747-A2749, with applicability OPEN A2750. Independent reconstruction and existing coordinator comparison complete. The pressure minimum and velocity zero are additional hypotheses.

## 1. Exact statement

Let c>0 and omega be real. Set J(x,y,z)=(-y,x,0). Suppose U is in C2(R3;R3), P is in C1(R3;R), and

    (1-c)U+DU[(cI-omega J)x+U]+omega JU+grad P=0,
    div U=0.                                                (1)

Assume U(0)=0 and P(x)>=P(0) for all |x|<r for some r>0. Then:

1. If |omega|<=sqrt(2), U=0 everywhere and P is constant.
2. For every omega the same conclusion follows if DU(0)=0.
3. If U is nonzero, W=curl U(0) is nonzero and

       omega^2|JW|^2>2|W|^2.                                (2)

For every omega with omega^2>2 and every real c there is a nonzero linear U and positive definite quadratic P satisfying (1) and the center hypotheses. These fields grow and do not meet the campaign's decay assumption. They prove sharpness only in the stated unrestricted global class.

The proof also establishes this propagation lemma: if c>0 and a global solution of (1) vanishes on any ball centered at zero, it vanishes on R3. The lemma requires no pressure sign, decay, global derivative bound or completeness of all characteristic trajectories.

## 2. Pressure regularity and the center identities

Write B=(cI-omega J)x+U and M=DU(0). The right side of

    grad P=-(1-c)U-DU B-omega JU

is C1, so the assumed C1 pressure is actually C2. Differentiation is therefore justified pointwise. Because B(0)=U(0)=0, differentiating at zero eliminates the derivative of DU multiplied by B and gives

    H:=D2P(0)=-M-M^2-omega(JM-MJ).                           (3)

The c terms cancel. Incompressibility gives tr M=0, and taking traces yields

    tr H=-tr(M^2).                                          (4)

The local minimum makes H symmetric positive semidefinite.

For completeness, divergence of (1) gives the full pointwise identity

    Delta P=-tr((DU)^2).                                    (5)

Indeed div(DU B)=tr(DU DB), DB=cI-omega J+DU, and div(omega JU)=omega tr(J DU). The trace containing c is zero and the two rotation traces cancel. No sign is assigned to tr((DU)^2) unless DU is symmetric.

Let Omega=curl U. Curling (1), using incompressibility and constant J, gives

    Omega+B.grad Omega+omega JOmega-DU Omega=0.              (6)

Here Omega is C1 and each term is continuous. At zero this becomes

    MW=W+omega JW,  W=Omega(0).                              (7)

Apply (3) to W. Substituting (7) into M W, M^2 W and J M W cancels the M J W terms and leaves

    HW=-2W-3omega JW-omega^2J^2W.                            (8)

Since J is skew and J^2 is minus the horizontal projection,

    W.HW=-2|W|^2+omega^2|JW|^2,
    (JW).HW=-3omega|JW|^2.                                  (9)

These identities use the full momentum equation at a carrier equilibrium. They are not consequences of Poisson and divergence alone.

## 3. Strictness at the angular-speed endpoint

Suppose W is nonzero. Positive semidefiniteness and the first equation in (9) imply the weak form of (2). If equality held, diagonalizing H would imply HW=0. The same equality forces omega!=0 and JW!=0, because W is nonzero. The second equation in (9) then contradicts HW=0. This proves the strict inequality (2).

If |omega|<=sqrt(2), the bound |JW|<=|W| rules out every nonzero W. Thus W=0. A matrix with zero curl is symmetric, so (4) now says

    0<=tr H=-|M|_F^2.

It follows that M=0. The rest of the proof shows that a double velocity zero with a local pressure minimum gives a zero ball and then a zero global field. Conversely, if a nonzero solution had W=0, the same reasoning would force this double zero and global vanishing, a contradiction.

## 4. A double zero gives local irrotationality

Assume U(0)=DU(0)=0. Choose 0<epsilon<min(c,1)/2 and a closed ball contained in the domain on which the operator norm of DU is at most epsilon. Integration on radial segments gives |U(x)|<=epsilon|x|. Hence

    x.B(x)>= (c-epsilon)|x|^2.                              (10)

For the backward characteristic x'=-B(x) starting in the interior of this ball, (10) gives

    d|x|^2/dt<=-2(c-epsilon)|x|^2,
    |x(t)|<=exp(-(c-epsilon)t)|x(0)|.

The trajectory stays in a compact smaller concentric ball. Local existence, uniqueness and the usual continuation argument for a C1 vector field therefore give existence for all t>=0 along this trajectory. This is a local trapping argument, not an assumption of global completeness of B.

Along it, (6) becomes

    d Omega(x(t))/dt=(I+omega J-DU(x(t)))Omega(x(t)).

Since J is skew,

    d|Omega(x(t))|^2/dt
      =2|Omega|^2-2 Omega.DU Omega
      >=2(1-epsilon)|Omega|^2.                              (11)

The continuous vorticity is bounded on the compact ball. The exponential lower bound from (11), with 1-epsilon>0, is possible only if Omega(x(0))=0. Every initial point in the smaller ball is allowed, so curl U vanishes on an open neighborhood of zero.

## 5. The local pressure minimum turns irrotationality into a zero ball

Shrink the ball so the pressure minimum inequality holds throughout it. There DU is symmetric, and (5) reduces to

    Delta P=-|DU|_F^2<=0.                                   (12)

Let pbar(s) denote normalized spherical means centered at zero. Since P is C2, the divergence theorem and differentiation of spherical means give

    (s^2 pbar'(s))'=s^2 <Delta P(s n)>, 
    lim_(s->0) s^2 pbar'(s)=0.

Equation (12) implies pbar'(s)<=0 and pbar(s)<=P(0). The local minimum gives the reverse inequality for each point on each sphere. A continuous nonnegative function on a sphere with zero mean is zero, so P=P(0) throughout this ball. Equation (12) forces DU=0 there, and U(0)=0 implies U=0.

This step needs the local minimum on a neighborhood. Positive semidefiniteness of H alone would not imply the pointwise pressure comparison used here.

## 6. Propagation of a centered zero ball

Suppose U vanishes on one centered ball. Define R as the supremum of the radii of all such balls. If R is infinite, there is nothing to prove. Otherwise R>0 is finite, and continuity gives U=0 and Omega=0 on the closed ball of radius R.

On its boundary B has radial component cR, because U=0 and Jx is tangent. Compactness of the sphere and continuity give delta>0 such that throughout the closed annulus R<=|x|<=R+delta,

    B(x).x/|x|>=cR/2.                                      (13)

For an initial point in the open annulus, the backward flow has radial derivative at most -cR/2 until it hits the inner sphere. It cannot exit across the outer boundary. A C1 field has bounded coefficients and derivatives on this compact annulus, so continuation is possible until the hit. The hit must occur by time 2delta/(cR); otherwise integrating the radial inequality would put the trajectory below R while it remained in the annulus.

At the hit, Omega=0. Equation (6) is a linear homogeneous ODE with continuous bounded coefficients on this finite trajectory. Uniqueness, used backwards from the hit time, implies Omega=0 at the original annulus point. Consequently div U=curl U=0 on the larger ball B_(R+delta). The vector identity

    Delta U=grad(div U)-curl(curl U)

shows that every component of U is harmonic there.

A harmonic function on a connected ball which is zero on an open subball is identically zero. One direct proof uses the interior derivative bounds to obtain its convergent Taylor expansion on each sufficiently small ball. Vanishing on one open ball forces all derivatives zero at any point there, hence vanishing on the next overlapping ball; a finite chain along any compact path reaches every chosen point. This uses local harmonic regularity, not analyticity of an arbitrary Euler profile.

Thus U=0 on B_(R+delta), contradicting the definition of R. We conclude U=0 on R3, and (1) then gives grad P=0. All characteristic arguments above were either locally trapped or of explicitly bounded finite duration.

## 7. Exact full-profile examples for omega squared greater than two

Fix omega^2>2 and set

    K=3omega^2+9omega^2/(omega^2-2)+1,
    w=2sqrt(K-1/4),
    M=[[1,omega,0],[omega,-1/2,-w/2],[0,w/2,-1/2]],
    H=[[omega^2-2,-3omega,0],
       [-3omega,K-3omega^2,0],[0,0,K]].

The radicand is positive. The trace of M is zero, and the curl of U(x)=Mx is (w,0,0). Multiplication, using w^2/4+1/4=K, gives

    M+M^2+omega(JM-MJ)
      =[[2-omega^2,3omega,0],
        [3omega,3omega^2-K,0],[0,0,-K]]
      =-H.

For P=x.Hx/2 this is exactly the entire momentum residual in (1), because the two c-dependent linear terms cancel for a degree-one velocity. Thus the pair solves (1) for every real c, not just c>0.

The leading principal minors of H are

    d1=omega^2-2,
    d2=(omega^2-2)(K-3omega^2)-9omega^2=omega^2-2,
    d3=K(omega^2-2).

All are strictly positive, so H is positive definite. Hence P has a strict global minimum at zero. The velocity is nonzero and homogeneous linear, so it grows along some ray and fails decay.

For omega=2 this construction gives K=31, w=sqrt(123), and

    H=[[2,-6,0],[-6,19,0],[0,0,31]],

with minors 2,2,62. The alternative choice w=12 and K=145/4, retaining the same form for M and H, has positive minors 2,25/2,3625/8 and again solves (1). Its nonzero commutator with J confirms that it is not equivariant about the designated rotation axis.

## 8. Scope, dependencies and verification

The pressure minimum is invariant under addition of a pressure constant. No gauge choice creates it. Decay has not been shown to give U(0)=0 or a pressure minimum at zero. The small-rotation conclusion holds on the closed interval |omega|<=sqrt(2), and only the double-zero conclusion holds for arbitrary omega. A velocity zero away from the origin generally has B nonzero, so the center proof cannot be transferred there.

The local trapping and finite-annulus continuation proofs are supplied in full above. The needed elementary harmonic derivative estimates were checked in the retained Hunter source as part of the LIT323 audit; this result does not use a unique-continuation assertion for general nonlinear profiles. No numerical estimate, global helicity statement, pressure normalization at infinity, or characteristic completeness assumption is a dependency.

All eight LIT324 source sections at the pinned hash were read. The proof above was checked independently without running mathematical computation. Existing configured model file comparison is complete; actual provider execution is independently unattested. The unrestricted decaying-profile conjecture remains OPEN.

## 9. Existing comparison and affine-family clarification

All eight coordinator items and W1-W3 in the team records were read and compared with Sections 2-8. All agree: pressure becomes C2; the center curl and derivative equations give the strict inequality; local trapping supplies the required backward existence; the pressure minimum yields a zero ball; and the finite-annulus continuation does not assume global completeness. The complete nineteen-check log was also read, without rerunning it. The separate source seventeen-check summary was read earlier; neither log replaces the analytic proof.

W1 is a useful clarification. In Section 7's displayed M and H one can take any w and K=(1+w^2)/4. The full matrix equation still holds. Positive definiteness is equivalent to omega^2>2 and K>3omega^2+9omega^2/(omega^2-2), by the first two minors and K>0. The prescribed K is one above this lower bound; the rational w=12 example is another member of this larger family, rather than another evaluation of that prescribed K. W2 is harmless: linear velocities are affine. W3 is essential for the report label: the local minimum and U(0)=0 are added hypotheses, so nonexistence is conditional in the campaign class.

## 10. Confirmed-source clarification

The complete three-hunk change from the original ae98625b source to 9b5364edfaafa0a7965add5a9d4f2702189bef4f2946d8fd2b5fd6867b1bbd48 was read. It updates status, records the free-w clarification from the existing comparison, and adds the precise verification record. The new mathematical sentence says that the same M,H solve the equation for any real w with K=(1+w^2)/4, and that H is positive definite exactly when omega^2>2 and K>3omega^2+9omega^2/(omega^2-2). This follows from the leading minors already computed in Sections7 and9: a=omega^2-2, a(K-3omega^2)-9omega^2 and K times that second minor. The stated conditions imply K>0, so they are necessary and sufficient. The rational w=12 example at omega=2 is a separate member of this family, not the K-one-above-threshold choice. No theorem hypothesis or conclusion changes.
