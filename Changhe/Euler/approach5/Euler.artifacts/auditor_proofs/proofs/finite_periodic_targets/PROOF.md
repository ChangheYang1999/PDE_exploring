# Finite periodic targets for an expanding interval map

Auditor verdict: CONFIRMED (A386), 2026-11-03T01:52:02Z. The complete argument below has been independently checked at its exact written scope.

## 1. Exact statement

Let I=[b_0,b_m] be a nondegenerate compact interval of length L. Let D be a finite set containing its endpoints, and let I_1,...,I_m be the nonempty connected components of I minus D, ordered along I. Let f:I minus D -> I have a C1 restriction to each I_j, with

    |f'(x)| >= sigma > 2

at every point in its domain. No upper derivative bound, distortion bound, transitivity or endpoint extension is assumed. Every iterate below is restricted to an open interval on which all intermediate iterates avoid D.

Then:

(i) For every delta in(0,L] there is an integer N(delta) such that every nonempty open interval J contained in I minus D with length at least delta contains an open subinterval K for which f^n:K->I_j is a diffeomorphism, for some j and 0<=n<=N(delta).

(ii) There is a finite nonempty set of periodic orbits P_1,...,P_q, each entirely in I minus D, such that every nonempty open interval J contained in the domain has an open subinterval K whose image under a suitable iterate is an open neighborhood of a point of some P_i. Consequently the union of the backward orbits of the P_i is dense in I. The assertion is about this finite family, not about every periodic orbit separately.

One may take any integer N(delta)>=1 with (sigma/2)^N(delta) delta>L in(i). Adding redundant periodic orbits is harmless.

## 2. Grow an interval until a whole branch is covered

Write rho=sigma/2>1. Each branch restriction is strictly monotone, because its continuous derivative never vanishes, and its image of an open interval of length ell has length at least sigma ell.

Start with J_0=J, retaining an inverse branch from J_0 to a subinterval of the original J. At a stage with J_r contained in one domain branch, inspect f(J_r). If it contains a full domain branch I_j, restrict to the inverse image of I_j and compose the previously retained inverse branches. This gives the required diffeomorphism onto I_j at time r+1.

Otherwise f(J_r) intersects at most two domain branches. Indeed, if it intersected three in their order along I, it would contain the whole middle branch. Removing the finitely many points D changes no interval length. Therefore one component J_(r+1) of f(J_r) minus D has length at least |f(J_r)|/2, hence at least rho |J_r|. Restrict to its inverse image and retain the new inverse branch. All intermediate iterates stay in open domain branches.

If this did not stop within N(delta) steps, we would have an interval of length at least rho^N(delta) delta>L contained in I, a contradiction. Stopping at time0 is also allowed when the original interval itself is a full branch. This proves(i).

## 3. Use interior branch intervals to construct actual periodic points

For each j choose a nonempty open interval J_j with closure contained in I_j. Part(i), applied to J_j, gives an integer n_j>=1, an index e(j), and an open K_j contained in J_j such that

    F_j=f^(n_j): K_j -> I_(e(j))

is a diffeomorphism. The inverse branch G_j=F_j^(-1) is sigma^(-n_j)-Lipschitz by the chain rule and the lower derivative bound. It extends continuously to the closed target branch, with image in closure K_j, a compact subset of I_j. These strict interior inclusions prevent a supposed periodic point from being merely a removed endpoint.

The directed finite graph j->e(j), with one outgoing edge per vertex, has at least one directed cycle, and every vertex reaches a cycle. For a cycle j_0->j_1->...->j_(r-1)->j_0 form

    G=G_(j_0) composed G_(j_1) composed ... composed G_(j_(r-1)).

It maps the closed interval closure I_(j_0) into the compact interior subset closure K_(j_0) and has Lipschitz constant at most sigma^(-sum n_(j_i))<1. Its unique fixed point p is therefore in I_(j_0), and its defining inverse branches show that f^(sum n_(j_i))(p)=p. All intermediate iterates avoid D. This is a regular periodic orbit of the map, of possibly smaller minimal period. Select one such orbit for each directed cycle. There are finitely many and at least one.

For every vertex j, follow its finite directed path to a chosen cycle and pull back a point of that cycle through the corresponding inverse branches. This gives a point z_j in I_j with a finite well-defined forward itinerary to a selected periodic point. Because all itinerary points avoid D, a sufficiently small neighborhood V_j of z_j is mapped diffeomorphically onto a neighborhood of that periodic point.

Now apply(i) to an arbitrary open J in the domain. It has a subinterval mapped diffeomorphically onto some I_j. Pull V_j back through that inverse branch. The resulting subinterval of J has the property in(ii). In particular it contains a preimage of a selected periodic point. Every nonempty relatively open subset of I contains such an open J, proving the density statement.

## 4. Source match and limits

The exact source is V. Araujo, A. Souza and E. Trindade, Upper large deviations bound for singular-hyperbolic attracting sets, arXiv:1711.09626v2, Proposition2.10, printed pages20-21. The actual manuscript is the retained PDF. The source cites Araujo-Pacifico, Three-dimensional flows, Lemma6.30 for this step; those monograph pages were not obtained. Sections2-3 above replace that specific interval-map citation with a complete proof at the stated assumptions.

AST Remark2.11 lifts the finite family to periodic orbits of the sectional return map and then to hyperbolic periodic flow orbits whose weak stable manifolds have dense union near the singular-hyperbolic attracting set. That lifting and the construction of the return map are not proved here. In particular contraction on an abstract open fiber does not alone prove existence of an interior periodic fiber point. The actual geometric return-map hypotheses and the source's lifting theorem must be retained.

The lemma supplies no homoclinic relation between every pair of periodic orbits, no density of the weak stable trace of every individual orbit, and no Euler nonexistence theorem by itself. The source application requires an actual C2 singular-hyperbolic attracting set with a two-dimensional expanding central bundle and a trapping neighborhood; an arbitrary compact statistical support does not suffice.

Dependencies: elementary interval geometry, chain rule, finite directed graph and contraction mapping theorem. No numerical data, formal sources or imported coefficient tables are used.


## Independent audit checks

The stopping proof is also valid when the image just reaches a removed point: lengths are unchanged by deleting finitely many points, and touching three nonempty branch interiors contains the middle branch. At each chosen interior source interval the covering time is positive. Although inverse branches are extended to closed intervals, the fixed point lies in the strict interior of the first source branch. Working around the cycle successively puts every inverse-branch argument in its actual open target, so the resulting point has a genuine finite itinerary. No orbit of a branch endpoint is used. The source match is only the one-dimensional proposition. Its Remark2.11 still supplies the geometric lifting required in B29.

The adjacent verification manifest identifies the exact full input read. This record makes no numerical or formal verification claim.
