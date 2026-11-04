# Recurrent points of a unique continuous sphere flow

Auditor verdict: CONFIRMED (A389), 2026-11-03T01:52:02Z. The complete argument below has been independently checked at its exact written scope.

## 1. Exact statement and scope

Let Y be a continuous tangent vector field on the two-dimensional sphere. Assume that its integral curves generate a unique continuous complete flow

    Phi : R x S2 -> S2.

Thus each Phi_t is a homeomorphism, Phi_(s+t)=Phi_s composed with Phi_t, and each orbit is C1 in time with derivative Y. Let p be positively recurrent: there are times t_n tending to positive infinity with Phi_(t_n)(p) tending to p. Then either Y(p)=0 and p is fixed, or p belongs to a nonconstant periodic orbit.

The assertion also holds on the plane, for a recurrent point whose full orbit and the local transverse arc considered below exist for all required times. Compactness of the sphere is not the source of the argument. The required topological fact is that an embedded circle separates the surface into two components. We prove only the sphere case here.

Continuity of Y is enough. No derivative of Y, invariant measure, finiteness of its zero set, smoothness of its orbit foliation, or classification of limit sets is assumed. The uniqueness and complete-flow premises are explicit. This statement does not cover arbitrary nonunique continuous ODEs or noninvertible semiflows on arbitrary compact subsets.

## 2. A local transverse flow box

Suppose Y(p) is nonzero. Choose a smooth coordinate chart centered at p in which one coordinate component of Y is positive at p. On a smaller coordinate rectangle it is bounded below by b>0. The corresponding coordinate is strictly increasing along any orbit segment contained in that rectangle.

Choose a small segment through p in the coordinate hyperplane where that increasing coordinate is zero. Parameterize it by sigma, with p at sigma=0. Continuity of the flow, its group law, and the lower bound b give, after shrinking the segment and a positive time interval, a homeomorphism

    F : (-2,2) x (-epsilon,epsilon) -> an open neighborhood of p,
    F(sigma,t)=Phi_t(F(sigma,0)).                     (1)

Here is the local inverse justification. For a point sufficiently close to the central segment, its orbit has negative increasing coordinate at a fixed small negative time and positive increasing coordinate at a fixed small positive time. It therefore meets the segment in exactly one intermediate time. The meeting time is continuous: uniform continuity of the flow and the lower bound b force the zero times of nearby strictly increasing coordinate functions to converge. The meeting position is also continuous. These two functions are the inverse coordinates in (1). Shrinking again keeps the meeting position in the chosen segment. Injectivity follows from uniqueness and strict increase. This constructs the claimed box without differentiating Y or the flow in its initial point.

We refer to t in (1) as the vertical coordinate. Forward trajectories cross the horizontal section from negative to positive vertical coordinate.

For a compact subsegment strictly inside (-2,2), there is a uniform positive separation between distinct successive orbit visits to that subsegment. Indeed, a trajectory beginning there remains in the box for a uniform short time; (1) prevents a second visit to the horizontal section during that time. Consequently the visit times of any one orbit to such a segment form a discrete, hence countable, subset of R.

Recurrence of p gives recurrent visits to the section. Write

    Phi_(t_n)(p)=F(sigma_n,s_n)

for all sufficiently large n. Continuity of the inverse box gives sigma_n ->0 and s_n ->0. The flow law gives

    Phi_(t_n-s_n)(p)=F(sigma_n,0).                   (2)

The times t_n-s_n still tend to positive infinity. This step is necessary: visits near p need not themselves lie on the transverse arc.

## 3. A first return gives a Jordan curve

Assume, for contradiction, that p is not periodic. Its orbit is injective in time. Otherwise Phi_t(p)=Phi_s(p) for t>s would imply Phi_(t-s)(p)=p by invertibility.

Choose a compact transverse subarc

    Sigma={F(sigma,0): -u <= sigma <= v},
    0<u<1, 0<v<1,

whose endpoints do not lie on the orbit of p. Such endpoints exist because the orbit meets the larger compact horizontal section at only countably many points. Equation (2) supplies arbitrarily late returns to the interior of Sigma. The first positive return time T exists: all return times are separated from zero, the return set is closed because Sigma is compact, and it is nonempty. Set q=Phi_T(p). The endpoint choice makes q an interior point, and nonperiodicity gives q different from p. Reverse the parameter sigma if necessary so that q=F(q_sigma,0), with 0<q_sigma<v.

Let C be the orbit segment from p to q, followed by the section segment from q back to p. The orbit segment is injective and its interior misses all of Sigma by the first-return choice. Therefore C is an embedded circle. By the Jordan curve theorem, S2 minus C has exactly two connected components.

Label them C_minus and C_plus as follows. Along the interior of the section interval from p to q, sufficiently small points of negative vertical coordinate lie in C_minus, and points of positive vertical coordinate lie in C_plus. These labels are consistent along the entire interval: the interval is connected, the orbit part of C is disjoint from its interior, and the two local sides vary continuously. Forward flow crosses this part of C only from C_minus to C_plus.

Two endpoint facts will be used. They can be read directly in the flow-box coordinates, which straighten the orbit near each endpoint.

* Near p, the orbit part of C leaves p vertically upward, while the section part lies to its right. The horizontal section immediately to the left of p belongs to C_minus. Since the entire subarc with -u<=sigma<0 misses C and is connected, it all belongs to C_minus.
* Near q, the orbit part of C arrives vertically from below, while the section part lies to its left. The forward orbit immediately after q belongs to C_plus. The horizontal section immediately to the right of q also belongs to C_plus.

For clarity, the first local corner consists of the upward vertical ray and the rightward horizontal ray. Its upper-right sector is the positive side of the horizontal interval, and its connected complementary sector contains the leftward horizontal ray and the negative side. At the second corner the rays point downward and leftward, giving the asserted reversed corner arrangement. No differentiability of the transverse foliation is used in these side identifications.

## 4. Later returns cannot approach p

The future orbit after time T stays in C_plus. It starts there by the preceding corner calculation. It can never meet the orbit portion of C again, since that would contradict injectivity of the orbit. It cannot meet the section portion either: at every interior point of that portion its immediately preceding positions lie in C_minus and its immediately following positions lie in C_plus. Thus a first departure from C_plus through this portion is impossible. The endpoints p and q already belong to the forbidden orbit portion. These facts exclude every possible first boundary contact after any sufficiently small time greater than T, and prove that the whole later orbit stays in C_plus.

All points of Sigma with negative parameter belong to C_minus, and those with parameter between 0 and q_sigma belong to C. It follows that every visit to Sigma at time greater than T has parameter strictly greater than q_sigma. But (2) gives visits at arbitrarily late times with parameter tending to zero. This is a contradiction.

Thus a recurrent point with Y(p) nonzero is periodic. If Y(p)=0, the constant curve is an integral curve through p, and uniqueness makes p fixed. This proves the statement.

## 5. Application to the angular tail in A360

Under the exact Dini scattering hypotheses retained in A360, let G be the continuous tail vorticity on S2 and set

    A=cI-omega J,
    G_r(w)=w dot G(w),
    Y(w)=G(w)-(G_r(w)/c) A w.

The vector field is tangent because w dot A w=c. The previously established A274 flow construction supplies precisely a unique continuous complete flow for this Y. A360 already uses that flow and its time-one nonsingular area transformation; no new smoothness premise is introduced here.

Positive recurrence for the angular time-one map implies positive recurrence for this continuous flow. Sections 1-4 therefore identify every such point as fixed or periodic. This is exactly the planar input in Section 1 of A360. Its subsequent radial-cocycle, closed-vortex-line, Hopf-decomposition and rational-saturation arguments are unchanged and retain their original hypotheses.

If independently confirmed, this argument removes the need to use Bochi-Morris Theorem3.1, its Bebutov path-space construction, or the older unavailable Ciesielski manuscript for this particular Euler application. It does not prove the stronger compact-subset or noninvertible-semiflow statements in that literature. The only topological dependency used here is the Jordan curve theorem on S2; the local flow box was constructed above.

## 6. Verification and limits

This is a standalone mathematical proof; no numerical calculation is involved. The exact A360 dependency and its source file hash are recorded in the adjacent verification folder. The source repair LIT77 remains a separate manuscript audit and is not a premise of this proof.

The result classifies recurrent points, not all alpha-limit or omega-limit sets. It does not prove that all angular or actual vortex orbits are recurrent. In the Euler application the almost-everywhere recurrence comes from the conservative part of a separate nonsingular Hopf decomposition. It does not remove the Dini condition, prove C2 basin coverage, or exclude a sign-changing essential basin.


## Independent audit checks

A compact central transverse arc has a uniform no-return time, so its orbit intersections are countable on every bounded time interval. The chosen endpoints therefore avoid the entire orbit. The first positive return exists by compactness of the section and continuity of the orbit; nonperiodicity makes the orbit arc injective and its return endpoint different from its start. At the starting corner the upward and rightward rays place the left section in the negative side. At the returning corner the downward and leftward rays place the outgoing orbit in the positive side. The future cannot first leave this side across the old orbit arc by uniqueness, nor across the section because that crossing direction is always negative to positive. Recurrence gives section visits tending to the start and contradicts this separation. This is a statement about recurrent points only, not all limit sets. No invariant measure is assumed. The stronger noninvertible compact-subset semiflow theorem is outside this proof.

The adjacent verification manifest identifies the exact full input read. This record makes no numerical or formal verification claim.
