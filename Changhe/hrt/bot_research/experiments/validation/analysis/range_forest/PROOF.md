# An exact obstruction search for route occupancy in turret ranges

## Statement and notation

Let V be a finite set of square-grid cells, with an undirected edge between
cells sharing a side. A linear forest is a graph whose connected components
are paths, including isolated vertices. Let f(V) be the largest cardinality
of a subset W of V whose induced graph is a linear forest.

The following finite algorithm returns f(V) and a witnessing W. Start with
U=V and an incumbent legal subset, initially the empty set. At each recursive
node, use the following rules:

1. If |U| is at most the incumbent size, stop this branch.
2. If a vertex v has at least three neighbors a,b,c in U, recurse on each
   of U without v, U without a, U without b, and U without c.
3. Otherwise, if the graph on U contains a cycle C, recurse on U without x
   for each vertex x of C.
4. Otherwise U is a linear forest. Store it if larger than the incumbent.

A previously processed vertex subset may be skipped on later visits.
The result is exact with integer arithmetic. The search must finish; an
interrupted search certifies only its incumbent lower bound.

## Proof of the algorithm

Every induced subgraph of a linear forest is a linear forest. If all four
vertices v,a,b,c from rule 2 were retained, the retained graph would have
degree at least three at v, which a linear forest cannot have. Thus every
legal subset of U omits at least one of these four vertices and is included
in at least one of the recursive branches. If a cycle C were wholly retained,
the retained graph would contain that cycle, which is also forbidden.
Consequently rule 3 likewise covers every legal subset of U.

A finite graph of maximum degree at most two consists only of paths, cycles
and isolated vertices: starting at a vertex and following edges cannot branch;
it either terminates, or returns to an already visited vertex in a cycle.
Therefore when neither obstruction occurs, U is itself a legal linear forest.
Rule 1 discards only subsets that cannot improve the incumbent. The recursive
sets strictly decrease in cardinality, so the recursion terminates. Induction
on |U| now shows that the search either finds every possible improvement or
prunes it using an already attained bound. At the root it returns f(V).

Memoization is sound because all future descendants and all obstructions
depend only on U. A completed earlier visit either explored an improving
subset or pruned it below the then-current incumbent. The incumbent never
decreases. A repeated visit cannot reveal an improvement that was excluded
by that earlier bound. There is no recursive cycle because cardinality
strictly decreases.

## Connection to the bundled game

A shortest path in an unweighted grid has no edge between nonconsecutive
path vertices. Such an edge would shortcut at least one step and contradict
minimality. Its induced graph is therefore a path, and the path vertices
inside any cell set V induce a linear forest. They number at most f(V).
This applies to the BFS route used by the bundled engine, including any
legal added buildings. Omitting blocked cells can only lower f(V).

For a turret at the origin with radius R, use
V_R = {(x,y) in the integer grid: 0 < x*x+y*y <= R*R}.
The center is excluded because it is occupied by the turret. A turret near
the board boundary has only a subset of these cells, so the same upper bound
applies. For R=5/2, 3 and 7/2 the defining comparisons can use the exact integer
inequality 4*(x*x+y*y) <= 25, 36 and 49 respectively.

## Verification and scope

The neighboring verification directory records completed runs, their exact
input sets, witnesses, search statistics and source hashes. The completed
searches return f(V_5/2)=15, f(V_3)=20 and f(V_7/2)=27; see
`verification/evidence.json` and its registered result. The implementation
is independent of the economy lane's include/exclude DFS: it branches on
forbidden degree and cycle obstructions. This is a finite computation with
an informal correctness proof, not a theorem-prover certificate. The bound
limits geometric route exposure, not the damage or strategic strength of a
whole policy.
