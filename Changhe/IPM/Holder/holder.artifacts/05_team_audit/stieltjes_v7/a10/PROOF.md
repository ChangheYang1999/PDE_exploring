# A finite positive certificate for the diagonal norm at exponent 1/10

## Statement and witness

For real functions on R^2 let [f]_a=sup_(z!=w)|f(z)-f(w)|/|z-w|^a. Define T_xx by the circular principal-value kernel (z_1^2-z_2^2)/(2pi|z|^4), extended modulo constants by convergent increments. Let D_a be the operator seminorm of R_1^2=T_xx-I/2, equivalently its supremum over smooth compactly supported functions. Subject to the certificate checks and a CONFIRMED verdict in the adjacent accepted.json, the proposed bound is

    D_(1/10) >= 7.0445434786.

Use the projection-cusp witness of ../../../11_lattice_pole_constraints/axis_projection_stieltjes/PROOF.md with a=1/10, b=3/8, shift=-1/40 and K=1003/1000. Its polygon, profile and clamping operations are fixed by that proof. The independently checked profile certificate gives [P]_(1/10)<=1.002471319750<1003/1000. The lattice construction therefore gives [f]_a<=1, f(1/2,0)=-1/2 and f(-1/2,0)=1/2. Its diagonal increment is

    1+4 integral_(X>0,Y>0) V(X,Y)(-d_Y f)dX,
    V(X,Y)=XY/[pi(((X-1/2)^2+Y^2)((X+1/2)^2+Y^2))].

The cited witness and monotone-axis proofs establish positivity, principal values, the local identity contribution and convergence at infinity. Their compact approximation transfers this witness bound to smooth compactly supported inputs.

## Finite lower sum

Write X=1/2+s d for s=+1 or-1. On both signs use log d in[-150,-18], divided into4096 strips, and log(Y/d) in[-6,3], divided into512 cells. Additionally use log d in[-18,12] on the positive sign and[-18,log(1/2)] on the negative sign, each divided into16384 strips with the same512 ratio cells. All endpoints are exact affine subdivisions before exponentiation; the last negative d endpoint is exactly1/2. Strip interiors do not overlap. Every omitted portion of the integral is nonnegative.

On each included cell apply the nonnegative lower rules proved in ../PROOF.md: direct enclosure, exact homogeneous profile difference, first- or second-order mean-value bound, or complete subdivision. Multiply the chosen valid lower variation by a valid lower endpoint kernel bound and the strip width. Outward rounding gives a lower bound for that cell. Twenty records cover all included strips exactly once. Exact rational resummation must place the certified lower sum strictly between7.0445434786 and7.0445434787, establishing the displayed decimal.

## Verification and scope

The structural auditor checks every parameter, profile certificate and source hash, all strip coverage and overlaps, every saved interval and the final downward rounding. Its only change from the already accepted a20/a30 auditor admits the existing profile certificate rows at1/20 and1/10 as well as1/5. The producer combiner has the same one-line extension. The new shift remains at least-1/2, as required by the admissibility proof.

Three selected chunks are replayed independently, covering the direct rule, exact homogeneous rule, derivative and subdivision rules, and the negative-side endpoint. Every numerical field and rule count must agree. This is complete structural recombination with selected geometric replay, not a full independent rerun of all production cells.

The producer's pre-launch record is dated2026-10-28T11:06:33Z; the run completed2026-10-28T11:44:50Z. The verifier's snapshot at11:16Z was taken during the run and is not an independent pre-launch observation. All these records are retained and checked. This proof was written before the independent recombination and selected replays. The result remains OPEN until their acceptance record is present.
