# Local regularity of the exact modal forcing

Written before the associated finite knot check. This argument concerns the
exact modal trial of topic15, with degree7 and exact knot data in
`data_exact/modal_v2.json`. It does not concern the original exponential
X3 interpolant, and it makes no fifth derivative claim at the origin.

On any compact subannulus of the open spline annulus all interior knots
are simple. The finite check must establish that the disk of radius3delta
about every allowed P lies inside this open annulus, and that the actual
interior knot multiplicities equal1. On this disk the density is C6, the
canonical velocity is C6, and its stationary residual g is C5. Therefore
g belongs to W4,infinity on a neighborhood of the smaller closed disk of
radius9delta/4. Multiplication by the stated C4 compact cutoff gives H4.

Here is a direct justification of the spline smoothness used in that
statement. Write N_(i,p) for the basis defined by the exact Cox recurrence
in full_t_linkage/PROOF.md. Near an interior simple knot, the degree1
basis consists of continuous linear ramps. Induction in p using the Cox
recurrence proves continuity of every higher basis. On the open knot
spans, differentiating that recurrence and collecting the two lower-degree
terms gives

 N'_(i,p)=p N_(i,p-1)/(k_(i+p)-k_i)
          -p N_(i+1,p-1)/(k_(i+p+1)-k_(i+1)).

Terms with zero denominator are zero, consistently with the defining
recurrence. The identity follows by induction on p: differentiate the two
linear factors, substitute the derivative identities for degree p-1,
and apply the recurrence once to collect the resulting degree p-2 terms.
All denominators are constants. If the degree p-1 basis is C^(p-2) at the
simple knot, the right side is C^(p-2). The degree p basis is continuous
and piecewise differentiable with this common continuous derivative;
integration across the knot shows that this derivative is its ordinary
derivative there. It is consequently C^(p-1). At degree7 this yields C6.
The finitely many smooth angular factors and the coordinate t=log r
preserve C6 on a closed annulus separated from zero.

No elliptic regularity theorem is needed for the velocity here. The
canonical streamfunction of this finite angular density has finitely many
angular modes. Each radial coefficient satisfies, for an integer m,

 psi_m''+psi_m'/r-m^2 psi_m/r^2=-f_m,

where f_m is the corresponding mode of partial_x rho and is C5 on the
open spline annulus. The canonical Green expression is an ordinary
integral there, so it gives a C2 solution. The displayed ODE then gives
successively C3,C4,...,C7, since its coefficients are smooth and f_m is
C5. Thus U=(-psi_y,psi_x) is C6. The function

 g=(c0 X+U).grad rho-rho

is C5, including across the simple knots. Compactness of the closed disk
inside the open annulus bounds all derivatives through order4. The outer
and inner joining repairs and the coordinate origin are outside this
disk. Their lower global regularity cannot create a local singularity in
the finite Green ODE. Existence and the definition of that canonical Green
solution remain the previously proved modal-trial dependencies; no finite
numerical Green enclosure is inferred from this smoothness argument.
