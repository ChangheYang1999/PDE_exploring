# A circular cut preserving the polygonal far field

## Exact statement

Fix 0<alpha<1 and a>0. Put x=(1/2,0), y=-x. Let Z_a and sigma_a be the
centrally symmetric polygonal zero set and centrally odd component sign
of ../../05_team_audit/structured_witness/PROOF.md, translated so that its
poles are x,y. The old witness is

    g(z)=2^(alpha-1) sigma_a(z) dist(z,Z_a)^alpha.

Let B_x=B(x,1/2), B_y=B(y,1/2), and S_x,S_y their boundary circles. Define

    Z=(Z_a \ (B_x union B_y)) union S_x union S_y.

For a phase phi write coordinates of q after rotation by -phi/2 as u,v,
and set

    d_phi(q)=(|u|-|v|)_+/sqrt(2).

This is the Euclidean distance to the closed set N_phi={|u|<=|v|} of
nonpositive own-kernel sectors, including the origin. On B_x put

    r=|z-x|,
    h(z)=2^(alpha-1)(1/2-r)^alpha,
    F(z)=-1/2+d_phi(z-x)^alpha,
    f(z)=max(-h(z),min(h(z),F(z))).

On B_y set f(z)=-f(-z). On the exterior of the two closed disks put

    d(z)=min(dist(z,Z_a), |z-x|-1/2, |z-y|-1/2),
    f(z)=2^(alpha-1) sigma_a(z) d(z)^alpha.

On Z set f=0; either boundary formula has this same value. Then

    [f]_alpha<=1,       f(x)=-1/2, f(y)=1/2.

For the phase kernel and centered principal-value increment in
../cut_sets/PROOF.md, the resulting rigorous lower functional is

    D_alpha >= |pv integral nu_phi(z) f(z) dA(z)|+1/2.

There is no seminorm loss factor. This is an admissible family, not a
claimed numerical improvement. Its integral remains to be evaluated.

## Geometry of the cut and the distance formula

The two open disks are disjoint and their circles touch at the origin.
The set Z is nonempty and closed. Each disk is a component of R^2\Z. For
z in B_x, every point outside B_x is at distance at least 1/2-|z-x|,
and S_x is part of Z. Thus dist(z,Z)=1/2-|z-x|. The same holds on B_y.

For z outside both open disks, the claimed minimum formula is exactly
dist(z,Z). To see this, the distance to either circle is |z-p|-1/2.
If a point w of the old Z_a was removed because it lies inside B_p, then

    |z-w| >= |z-p|-|w-p| > |z-p|-1/2.

Consequently the added circle always supplies a nearer point than any
removed point. Removing the old interior pieces therefore does not
alter the minimum of the three displayed distances. No explicit
clipping of polygonal segments is needed to evaluate d(z).

Outside the disks, sigma_a is constant on each component of the new
complement: adding the circles cannot connect two old components.
Inside B_x, F is Holder with seminorm at most one, since distance to a
nonempty closed set is 1-Lipschitz and |s^alpha-t^alpha|<=|s-t|^alpha.
The displayed d_phi follows by projecting onto the nearest of the two
lines u=+v,u=-v in either positive sector. Inside B_y the reflected F
has the same bound.

## Global admissibility and the pole jump

Apply the closed-cut-set lemma of ../cut_sets/PROOF.md. On an exterior
component choose F=+infinity or -infinity according to sigma_a. On B_x
choose the displayed finite F and on B_y its negative reflection. All
finite component functions have seminorm at most one. The clamp
amplitude is exactly 2^(alpha-1)dist(z,Z)^alpha in every component.
The lemma proves the global seminorm bound and continuity across Z.
At x the amplitude is 1/2 and F=-1/2, so f(x)=-1/2. Central oddness gives
f(y)=1/2.

The kernel is centrally odd, and the own-pole constants cancel in
centered principal values. The Holder remainder is locally integrable;
the kernel increment is O(|z|^-3), while f is O(|z|^alpha). Thus the
principal value and the tail converge. The identity contribution is
+1/2. The two operators T_phi-I/2 and T_phi+I/2 both have norm D_alpha,
so choosing the favorable identity sign gives the absolute-value lower
functional. Compact smooth approximation is justified by the setup
lemma; no norm density is claimed.

## The far field is unchanged beyond an explicit radius

Put M=sqrt(a^2+1/4). The polygonal-witness proof shows that Z_a has
Hausdorff distance at most M from the three lines of its limiting
six-sector profile. The nearest of those lines is at distance at most
|z|/2. Hence

    dist(z,Z_a)<=|z|/2+M.

For p=x,y, |z-p|-1/2>=|z|-1. If |z|>=2(M+1), both circle distances are
therefore at least dist(z,Z_a). The minimum d(z) equals dist(z,Z_a),
and

    f(z)=g(z) whenever |z|>=2(M+1).

The existing polygonal far-tail enclosure can be reused verbatim beyond
that radius. In particular the circular cut preserves the sharp
1/(1-alpha) coefficient of that fixed polygonal family. Indeed the difference
f-g is supported in that fixed compact disk, has seminorm at most two,
and has bounded pole values. After subtracting these values at the poles,
its integral is uniformly bounded for 1/2<=alpha<1. The unchanged tail
therefore has the same leading coefficient as the old witness tested
against the same phase. More explicitly, reflection in Y makes the old
axis-phase integral zero, so its coefficient at phase phi is
sin(phi)*3*sqrt(3)/(4*pi). The sharp positive coefficient is preserved
for phi=pi/2; it is not asserted for every phase. This construction does not
preserve the old finite-radius integral, which must be recomputed.

## Dependencies

The nonempty closed-cut lemma, the polygonal witness and its Hausdorff
estimate, the kernel convention and compact approximation theorem.
No numerical quadrature or unproved seminorm estimate enters this
admissibility theorem.
