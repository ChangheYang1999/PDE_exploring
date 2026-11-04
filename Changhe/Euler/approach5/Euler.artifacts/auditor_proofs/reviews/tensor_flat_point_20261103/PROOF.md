# Sphere averages forbid a flat uniformly definite stress

## 1. Exact local theorem and dependency scope

Let x0 be an interior point of an open subset G of R3. Suppose V in C1(G;R3), P in C1(G), div V=0, and -Delta P=tr((DV)^2) in distributions. Write E=|V|^2, S=P-E/2 and H=-S. Assume on a ball B_r0(x0) that H>=0 and E<=Rstar H for one constant 0<=Rstar<2/3. Suppose H vanishes to infinite value order at x0: for every integer N>=1 there are constants C_N,r_N>0 such that H(x)<=C_N|x-x0|^N when |x-x0|<r_N. Then V=P=0 throughout B_r0(x0).

This is a local kinematic and Poisson theorem. It assumes no self-similarity, helicity, rank identity, value of c, rotation rate, potential, or derivative bound on E/H. Smooth common-flat tails satisfy the required flatness. If S<0 away from an orbit through x0, its conclusion contradicts that strict sign. Thus it excludes the proposed nontrivial common-flat branch for every omega, including the submitted CO63 case omega=0.

The proof uses only the elementary tensor lemma below and the distributional identity div div(V tensor V+P I)=0. All radius statements concern balls centered at x0; there is no boundary at spatial infinity or at the missing similarity origin.

## 2. A tensor lemma in arbitrary dimension

Let d>=2 and let T be a symmetric C1 matrix field on B_r0(0), positive semidefinite. Suppose div div T=0 in distributions and, for every unit vector n and every x,

    0<=tr T(x)-n.T(x)n<=(d-1) kappa n.T(x)n,             (1)

where kappa>=1 is finite. Assume T vanishes to infinite value order at0. Then T=0 on the ball.

For 0<r<r0 define unnormalized unit-sphere integrals

    A(r)=integral_S n.T(rn)n dn,
    B(r)=integral_S [tr T(rn)-n.T(rn)n] dn.

The radial component of div T, integrated over the unit sphere, is

    integral_S (div T)(rn).n dn=A'(r)+[(d-1)A(r)-B(r)]/r. (2)

To verify (2), extend n=x/|x|. The vector Tn has divergence (div T).n+[tr T-n.Tn]/r. Its normal component is n.Tn. Apply the usual polar divergence formula to Tn; the integral of the tangential divergence over the closed unit sphere is zero. This gives (2) with no derivative of a chosen frame.

The flux r^(d-1) times the left side of (2) is constant in r because div div T=0. This follows first distributionally by radial tests in each annulus. It then holds for every r because div T is continuous. That constant is zero: div T is bounded near0 and the sphere area factor r^(d-1) tends to0. Consequently

    A'(r)=[B(r)-(d-1)A(r)]/r<=K A(r)/r,
    K=(d-1)(kappa-1)>=0.                                (3)

No division by A is needed. The function r^(-K)A(r) is nonincreasing. For 0<r<r1<r0,

    A(r)>=(r/r1)^K A(r1).                               (4)

If A(r1)>0, (4) contradicts infinite-order flatness by choosing an integer N>K and letting r approach0. Hence A(r)=0 for every r. The nonnegative continuous integrand n.T(rn)n is then zero everywhere on each sphere; (1) makes tr T=0 there. A positive semidefinite matrix of trace zero is zero. Continuity gives T(0)=0 as well. This proves the lemma.

One sufficient condition for (1) is a nonnegative scalar h and constants 0<a<=b<infinity with a h I<=T<=b h I; then kappa=b/a. The scalar may vanish on an arbitrary set. Strict positivity away from a single point is unnecessary.

## 3. Application to the negative Euler stress

For a C1 divergence-free V,

    div div(V tensor V)=tr((DV)^2)

in distributions. For example, mollify V on a relatively compact open subset, use divergence freedom for the smooth fields, and pass to the limit in V and DV. The assumed Poisson equation therefore gives div div T=0 for

    T=-(V tensor V+P I)=(H-E/2)I-V tensor V.

Its eigenvalues are H-3E/2 in the V direction and H-E/2 on the two perpendicular directions, with the same formula at V=0. The pressure premise gives

    (1-3Rstar/2)H I<=T<=H I.                            (5)

Thus (1) holds with kappa=1/(1-3Rstar/2). Infinite value flatness of H and (5) imply the same flatness of T. The tensor lemma gives T=0. Its lower bound in (5) gives H=0, and E<=Rstar H gives V=0. Finally P=E/2-H=0. This proves Section1.

The slightly sharper pointwise eigenvalue ratio is (2-R)/(2-3R), so one can instead take kappa=(2-Rstar)/(2-3Rstar). The coarse constant in (5) already suffices. There is no dependence on the rotation rate in either argument.

## 4. Direct verification of the submitted spherical proof

For omega=0, p=(1-c)/c in (1,3/2), k=cx.V=0 implies V=r^(-p)w(n) with w tangent to the round unit sphere and div_gamma w=0. Write S=-r^(-2p)h, s=|w|^2 and u=s/2-h, so P=r^(-2p)u. The Poisson equation reads

    -(Delta_gamma+lambda)u=tr((nabla_gamma w)^2)+2p s,
    lambda=2p(2p-1).

The curvature commutator on the unit sphere gives

    div_gamma div_gamma(w tensor w)=tr((nabla_gamma w)^2)+s.

Hence for U=u gamma+w tensor w,

    div_gamma div_gamma U=lambda h-mu s,
    mu=(p+1)(2p-1).                                     (6)

For R=s/h<=Rstar<2/3, -U has eigenvalues h-3s/2 and h-s/2, and (6) gives div div(-U)<=-(lambda-mu Rstar)h<=0. Here lambda/mu=2p/(p+1)>1. Let A(rho),B(rho) be circle integrals of its two orthonormal polar components. Integration over a geodesic disc of radius rho<pi/2 gives

    A'+cot(rho)(A-B)<=0,
    B<=kappa A,
    kappa=(2-Rstar)/(2-3Rstar).

Therefore A'<= (kappa-1)cot(rho) A and

    A(rho)>=[sin(rho)/sin(rho1)]^(kappa-1) A(rho1).

Infinite flatness contradicts any positive A(rho1), exactly as in the tensor lemma. This verifies CO63 independently, including the polar divergence term and inequality direction. The spherical proof is valid at its submitted zero-rotation scope. Section3 proves a strictly broader version directly in physical coordinates.

## 5. The opposite pressure regime and ratio consequences

The same tensor lemma applies to T=V tensor V+P I when H>=0 and H<=E/Rlower for a constant Rlower>2, with E infinitely flat. Its eigenvalues are E/2-H and3E/2-H, so

    (1/2-1/Rlower)E I<=T<=3E I/2.

Thus T, V and P vanish locally. This is the positive-stress regime underlying the earlier LIT216 exclusion; no novelty is claimed. It also needs no k=0 or rotation restriction.

Consequently, if a nonzero smooth common-flat tail has S<0 off an orbit through x0, and has the divergence and Poisson equations on a full neighborhood, the ratio R=E/(-S), defined away from that orbit, must obey

    limsup_(x->x0, x off orbit) R>=2/3,
    liminf_(x->x0, x off orbit) R<=2.

Indeed, failure of either inequality supplies a uniform strict bound on some neighborhood; on the orbit the smooth flat-tail homogeneity gives V=S=0, so the corresponding tensor inequalities extend there continuously. More generally one may directly require that the uniform inequalities extend across all zeros of S. Values on the orbit cannot be omitted without this extension check.

The theorem does not treat equality at Rstar=2/3 or Rlower=2, where a positive eigenvalue lower bound is lost. It gives neither a universal upper or lower bound for R nor an exclusion when R oscillates through the remaining range. The main bare-decay Euler nonexistence question remains open.

## 6. Audit method and provenance

The complete coordinator CO63 note and its full nested question were read. Sections1-3 and5 are an independent strengthening supplied for comparison by the existing configured model theory agents; provider runtime is not attested. No nested answer is needed to verify the displayed spherical argument. No mathematical computation, formal build, numerical observation or new model call is used. The C1 tensor-flux proof explicitly handles the center and all characteristic-flow questions are absent from this local argument.
