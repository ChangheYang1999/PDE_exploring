# Excluding a zero-velocity equilibrium from the exceptional support

Status: CONFIRMED as A464 after independent reconstruction, full postwrite inspection and focused configured-model challenge. This is a necessary restriction on an exceptional measure in the global helicity-free class, not a general exclusion theorem.

## 1. Statement and dependencies

Let 0<c<1/2 and omega be any real number. Let U in C2(R3;R3), P in C1 solve

    (1-c)U+(B.grad)U+omega JU+grad P=0, div U=0,
    A=cI-omega J, B=Ay+U, W=curl U,
    a=1-2c, kappa=1+c, d=3c.

Assume uniform U=o(|y|) and U.W=0 everywhere. Let mu be a compactly supported probability invariant and ergodic for the whole carrier flow, with

    B!=0, W=0, DW!=0, D(B cross W)=0  mu-almost everywhere.

Then U has no zero in S=supp mu. In particular S contains no equilibrium at the spatial origin. A regular support point at coordinate zero with U(0)!=0 is not excluded.

The dependencies are A444 and A445, which give on S, with H=P+|U|^2/2+(Ay).U and g=U.B:

    W=0, H=h, g=0;
    a zero of U can only be the origin, where B=0;
    grad g=-kappa U where U!=0;
    Hess g+kappa DU=tau U tensor U where U!=0.           (1)

Here tau is a point-dependent real scalar. Its boundedness is not assumed. The carrier is complete and S is invariant in both directions by the growth assumption. No pressure normalization, derivative decay, source theorem about singular flows or finite-jet nonflatness at the origin is required.

## 2. Limit of the second covector identity

Suppose U(p)=0 for some p in S. By (1), p=0 and B(0)=0. Set M=DU(0). Since W(0)=0, M is symmetric; incompressibility gives tr M=0. Differentiating g=U.B twice at a simultaneous zero of U and B gives

    G:=Hess g(0)=M(A+M)+(A+M)^T M
               =2M^2+2cM+omega(JM-MJ).

Thus, with beta=2c+kappa=1+3c,

    R:=G+kappa M=2M^2+beta M+omega(JM-MJ),
    tr R=2 tr(M^2).                                    (2)

This formula uses no third derivatives: g is C2 and the terms involving second derivatives of U or B are multiplied by U or B at the origin.

If M=0, then B(y)=Ay+o(|y|), and the radial estimate of Section4 follows directly. Suppose henceforth M!=0. Then rank M>=2, since a nonzero real symmetric rank-one matrix cannot have trace zero, and t:=2tr(M^2)>0.

The origin is not isolated in S: otherwise its positive support mass would contradict mu({B=0})=0. At every nonzero point y of S, U(y)!=0 by (1). The continuous matrix

    R(y)=Hess g(y)+kappa DU(y)

has rank at most one there. Its limit at zero therefore has rank at most one. Since R is symmetric and has positive trace t, there is a unit vector v such that

    R=t v tensor v.                                    (3)

This passage uses boundedness of R(y), which follows from continuity; it never bounds tau separately.

## 3. Tangent directions and the pseudoinverse trace

Consider any y_j in S minus {0} tending to zero with x_j=y_j/|y_j| tending to a unit vector x. Taylor expansion of grad g+kappa U, which vanishes on these points and at zero, gives Rx=0. By (3),

    v.x=0.                                            (4)

Furthermore tr R(y_j)->t>0. The rank-one identity in (1) implies, for large j,

    R(y_j)/tr R(y_j)
        =U(y_j) tensor U(y_j)/|U(y_j)|^2
        ->v tensor v.

Together with U(y_j)/|y_j|->Mx, this shows Mx is a scalar multiple s v; if Mx=0 this statement is already true. One can see the implication without choosing signs of normalized velocities by applying the perpendicular projection to both sides of the rank-one convergence.

For z in ker M, formula (2) gives z.Rz=0, since every term contains M on at least one side. Formula (3) then gives v.z=0. Hence v belongs to range M.

Let Mdagger be the symmetric spectral pseudoinverse, and Q=Mdagger M=MMdagger the orthogonal projection onto range M. Cyclicity of trace yields

    tr(Mdagger R)
      =2 tr M+beta tr Q
          +omega[tr(Mdagger J M)-tr(Mdagger M J)]
      =beta rank M>0.                                 (5)

Indeed the two commutator terms are both tr(QJ). Substitution of (3) gives t v.Mdagger v=beta rank M>0.

The equation Mx=s v is equivalent to x=s Mdagger v+z with z in ker M. Taking its scalar product with v, using (4), v perpendicular to ker M and (5), gives s=0. Consequently

    every unit limiting direction of S at zero lies in ker M. (6)

If M is invertible this already contradicts the existence of a unit limiting direction. No invertibility is needed in the next step.

## 4. A support-relative radial estimate

There exists epsilon>0 such that

    y.B(y)>=(c/2)|y|^2
    for all y in S with 0<|y|<epsilon.                 (7)

Otherwise choose a sequence violating (7), tending to zero, and a convergent subsequence of its unit directions. By (6) the limit x satisfies Mx=0. Since B(y)=(A+M)y+o(|y|) and J is skew,

    y_j.B(y_j)/|y_j|^2 -> x.(A+M)x=c,

a contradiction. If M=0 the same calculation is uniform in all ambient directions and proves (7) directly.

Estimate (7) is only on S. No smoothness of S, lower bound for |U|, or radial inequality outside S has been inserted.

## 5. Invariance and recurrence

The relative set S intersect B_(epsilon/2) has positive mu measure because zero lies in S. A backward trajectory starting there remains in S. Until a hypothetical exit from B_epsilon, (7) implies

    d/dt |Psi_t y|^2<=-c|Psi_t y|^2.

It cannot exit, since its radius decreases. Thus it tends to zero exponentially as t tends to infinity. Its continuous-time empirical probability is delta_0.

For almost every starting point under the whole-flow-ergodic mu, the same empirical probability is mu. This uses whole-flow ergodicity and continuous-time averages, not ergodicity of the time-one map. The positive-measure relative ball forces mu=delta_0, contradicting mu({B=0})=0. Equivalently one may use recurrence of a positive-measure annulus away from zero. This contradiction proves the theorem.

## 6. Scope and verification

All arguments use C2 velocity and the full second covector identity of A444. The origin is not assumed vortically dense, DW(0) is not assumed nonzero, and tau need not remain bounded. The conclusion supplies a positive minimum of |U| on this compact S, but does not exclude carrier equilibria with U=-Ay!=0 at nonzero positions. A separate surface argument is required to exclude the measure itself. Flat first-vorticity measures, vortical equilibrium atoms, general sign-changing helicity and the unrestricted C2 growth question remain outside this result.

The submitted source is pinned in the team records, and the complete focused review is in the team records. No computation was needed. The review independently redid all steps before and after reading this reconstruction and found no gap. The existing agent's the primary model configuration is distinguished from independent provider attestation.
