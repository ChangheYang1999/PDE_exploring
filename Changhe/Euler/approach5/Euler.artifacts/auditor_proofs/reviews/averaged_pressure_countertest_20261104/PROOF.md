# Centered sphere means do not replace pointwise quarter pressure

Status: CONFIRMED A2696-A2697; scope OPEN A2698. Complete source and independent reconstruction read; existing coordinator comparison completed.

## 1. Exact claim and example

Write rho^2=x^2+y^2 and define the polynomial fields

    V=z(-y,x,0), E=rho^2 z^2,
    P=rho^4/240-rho^2 z^2/30+8z^4/45.

They are smooth on every ball B_R(0), are nonzero as fields on every such ball, and have V(0)=DV(0)=P(0)=0. They satisfy div V=0, -Delta P=tr((DV)^2) and P>=E/60 pointwise. On every centered sphere they satisfy <P>=<E>/4 and V.n=0. They therefore refute replacing the pointwise quarter-pressure inequality by just its centered spherical mean in that local kinematic Poisson class.

## 2. Polynomial equations and positive pressure

The Jacobian is

    DV=[0 -z -y; z 0 x; 0 0 0].

Its trace is zero and tr((DV)^2)=-2z^2. The identities

    Delta rho^4=16rho^2,
    Delta(rho^2 z^2)=2rho^2+4z^2,
    Delta z^4=12z^2

give Delta P=2z^2 exactly. Since these are polynomial identities, there are no axis or boundary distributions.

Completing the square gives

    P-E/60=(rho^2-6z^2)^2/240+z^4/36>=0.

The two terms can vanish simultaneously only at the origin, so P>0 elsewhere. This weaker pointwise positivity does not imply P>=E/4. When rho^2=z^2>0,

    P-E/4=-73z^4/720<0,

whereas on z=0 with rho>0 the quarter-pressure defect is positive.

## 3. Exact sphere means and failure of the L1 step

The normalized sphere moments are <z^4>=r^4/5 and <x^2z^2>=r^4/15, with the same values after coordinate permutations. They follow by integrating one coordinate on the unit sphere and using rotational symmetry and (x^2+y^2+z^2)^2=r^4. Thus

    <rho^4>=8r^4/15, <rho^2 z^2>=2r^4/15,
    <P>=r^4/30=<E>/4.

Also x.V=0 identically. In the stress notation A=<(V.n)^2>+<P>, one has

    A=r^4/30, v=0, 4<P>-<E>=0.

So (A/r^4)'=0, fully consistent with the endpoint stress identity. The nonzero limit 1/30 alone does not yield a contradiction.

By homogeneity, V_epsilon=epsilon^-2 V(epsilon x)=V and P_epsilon=epsilon^-4 P(epsilon x)=P. The continuous polynomial 4P-E changes sign and is nonzero on an open subset of every ball. Consequently its absolute integral on any ball is strictly positive and independent of epsilon, even though its signed integral is zero. The absolute-value estimate in the pointwise theorem is precisely the step lost under the averaged premise.

## 4. Failure of the full equations and scope

At (0,0,z) with z!=0, V=0, the acceleration is zero and

    grad P=(0,0,32z^3/45)!=0.

Thus this example does not solve stationary Euler with this P. On the same axis X=(cI-omega J)x=(0,0,cz), and DV X=0, so all velocity terms in the rotating similarity equation vanish while this pressure gradient remains. It fails that equation for every c and omega. A pressure constant cannot fix the defect, and its polynomial growth also violates decay.

The countertest concerns only averages on spheres centered at the double zero. It says nothing about inequalities on all translated spheres, and does not contradict any theorem retaining the full pointwise lower bound. No scalar-tail completion, global profile, numerical result or external theorem is used. Existing configured model comparison is completed in the final section; actual provider runtime remains independently unattested.

## 5. The coordinator's general tangential-quadratic remark R2

Let Q be a nonzero homogeneous quadratic vector field on R3 with div Q=0 and x.Q=0, and let R be any homogeneous quartic satisfying -Delta R=tr((DQ)^2). No sign assumption on R is made. Then on every centered sphere

    4<R>=<|Q|^2>,

and the continuous quartic 4R-|Q|^2 takes both signs on that sphere.

Proof. For any smooth divergence-free pair satisfying the Poisson equation, the divergence of T=Q tensor Q+R I has zero divergence. The flux of div T through a centered sphere is therefore zero. Multiplying by the radial position and integrating by parts, or differentiating the radial stress flux, gives rA'=e-3v with A=v+<R>, e=<|Q|^2> and v=<(Q.n)^2>. Here v=0 and A is homogeneous of degree four, so 4<R>=e.

If 4R-|Q|^2 vanished identically, the tangency identity differentiated in x and quadratic homogeneity would give x cross curl Q=-3Q. Since curl Q is linear, Q=x cross Mx for a constant matrix M. The divergence condition forces M symmetric. In an oriented orthonormal eigenbasis Q=(a yz,b xz,d xy), with a+b+d=0. Substitution of R=|Q|^2/4 in the Poisson equation gives a^2=-2bd, b^2=-2ad and d^2=-2ab. Multiplying yields (abd)^2=-8(abd)^2, hence abd=0, and the three equations force a=b=d=0. This contradicts Q nonzero. Thus the defect is not identically zero. Homogeneity makes its restriction nonzero on every positive-radius sphere. Its mean is zero, so continuity forces both signs there. This proves the remark without random sampling.

The centered average equality is therefore automatic for this particular tangential homogeneous class. The remark does not impose the positive-pressure lower bound of Section 2, does not treat translated spheres, and does not assert existence of an Euler profile.

## 6. Completed existing coordinator comparison

All eight coordinator items, the full R2 remark and wording point A1 were read, as was the complete shared check log. Items 1-8 agree with Sections 1-4. R2 is proved independently in Section 5; the random checks in the log are unnecessary for the proof. The precise interpretation is centered sphere averages of a kinematic Poisson pair. The source hash matches the pinned snapshot. No discrepancy was found. Existing configured model file collaboration is completed; actual provider runtime remains independently unattested.
