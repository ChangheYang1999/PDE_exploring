# Bounded exterior dynamics forced by a regular trapping region

## Statement

Let c>0, omega in R, U in C1(R3;R3) be divergence-free and uniformly sublinear, and B=(cI-omega J)y+U. Let Phi_t be its complete flow. Let N be a compact smooth domain such that B points strictly outward on its boundary. Assume that its boundary is not diffeomorphic to a single two-sphere; disconnected boundaries are allowed. A toroidal boundary is an important special case. For every sufficiently large R with N contained in the open R-ball, define

    E={x in boundary(N): Phi_t x never reaches S_R for t>=0}.

Then E is nonempty and compact. Its surface measure and its B-flux measure are zero. Every x in E has a nonempty compact forward limit set disjoint from N.

If additionally B has no zero in N, then B has at least one zero in B_R minus N. No nondegeneracy is needed. The latter hypothesis holds when the maximal backward-invariant set of N is regular. This result is kinematic and does not use W=curl U.

## Completeness and first hits

Uniform sublinearity gives at most linear growth of B and completeness. Since B.y=c|y|^2+U.y, for large r one has B.y>=(c/2)r^2. Every sufficiently large sphere is strictly outward, and after reaching S_R an orbit grows at least exponentially in radius. All bounded forward trajectories stay inside that sphere.

Suppose E were empty. The first-hit map Q:boundary(N)->S_R would be defined everywhere. Strict transversality at both sections makes Q a C1 local diffeomorphism. It is injective: two points with the same image lie on the same orbit, but a trajectory can cross a strictly outward boundary of N at most once. Indeed any subsequent outward crossing would require a previous inward crossing, which the boundary direction forbids. The image of Q is open by local invertibility and closed by compactness. Since S_R is connected, Q is a diffeomorphism onto S_R. This would make the entire boundary of N diffeomorphic to a single two-sphere, contrary to the hypothesis. This contradiction proves E is nonempty. The argument allows multiple boundary components, since injectivity holds across components as well.

The finite-hit set is open, so E is closed in compact boundary(N). Equivalently E consists of the initial points whose entire forward orbit remains in the closed R-ball. Every such orbit has a nonempty compact invariant limit set. It stays outside int N after time zero. Its limit cannot meet boundary(N), because full invariance of the limit set would then place a short negative-time segment inside N. The limit is therefore disjoint from N.

## Null boundary measure

Let nu=(i_B m)|boundary(N), oriented outward. It is a strictly positive continuous density. The map

    (x,t) -> Phi_t x,    x in E, 0<t<T,

is injective by the same no-second-crossing argument. Its volume Jacobian is exp(3ct)nu. Its image lies in the R-ball, so the change-of-variables formula gives

    vol(B_R) >= [(exp(3cT)-1)/(3c)] integral_E nu.

Letting T tend to infinity gives integral_E nu=0. Since nu is bounded below by a positive multiple of area on the compact boundary, E also has surface measure zero.

## A zero outside a regular trap

On S_R the normalized field B/|B| is homotopic to the outward radial map: the straight interpolation between B and y remains outward. Hence its Brouwer degree is one. If B has no zero on N, its degree on int N is zero. Additivity of degree gives

    deg(B, B_R minus N, 0)=1.

Thus there is a zero in B_R minus N. If these exterior zeros happen to be finitely many and nondegenerate, the sum of signs of det DB at them is one. No source classification follows from this index count.

A zero of B lying in N belongs to every Phi_-t N, so is in the maximal backward-invariant set. Therefore regularity of that maximal set supplies the no-zero hypothesis on N.

## Scope

The first-hit argument reconstructs the coordinator's regular_kinematic review. The degree argument adds an elementary consequence. Both remain valid under uniform sublinearity, which is weaker than the review's compact support or decay assumption. They require no pressure normalization and are uniform in omega. The nonempty exceptional set E is null, so this is compatible with volume expansion and with almost every boundary point escaping. It neither excludes a regular backward attractor nor constructs the necessary exterior invariant sets.

Audit written: 2026-11-02T20:43:26Z

Scope broadened to every boundary not diffeomorphic to a single two-sphere: 2026-11-02T20:45:49Z
