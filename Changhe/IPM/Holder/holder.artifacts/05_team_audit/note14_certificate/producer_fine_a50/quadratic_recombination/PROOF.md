# Quadratic recombination of the finer half-exponent producer certificate

## Exact statement and normalization

For real functions on R^2 use [f]_(1/2)=sup_(z!=w)|f(z)-f(w)|/|z-w|^(1/2). Let T_xx have circular principal-value kernel (z_1^2-z_2^2)/(2pi|z|^4), with convergent increments defining its extension modulo constants. Set D_(1/2)=||T_xx-I/2||. The polygon-plus-projection witness in the parent proof has exact parameters alpha=1/2, b=3/4, c=-3/20 and lambda=1000/1021. The accepted global profile proof gives [f]_(1/2)<=1, f(0)=1/2 and f(e_1)=-1/2. The accepted compact approximation theorem transfers each fixed increment lower bound to real C_c^infinity inputs.

The exact positive increment endpoint below, plus 1/2, is a lower bound for D_(1/2). It is not admitted until the finite certificate and every analytic condition have passed. The final exact value and its downward rounding are in independent_audit.json and accepted.json.

## Finite integration and proof dependencies

The parent PROOF.md states the complete imported-interval contract. There are 4019 tasks and 24900260 cells: near-pole annuli from radius 10^(-8) to 1/2, and the complementary midpoint annuli from radius 1/100 to R=10^8, with exactly the exclusions of the frozen evaluator. Reflection duplicates the one-pole near contribution. All printed midpoint and radius uncertainty is retained as rational endpoints. Exact radial coverage, task parameters, source provenance and cell counts are checked. Fifty-two selected complete tasks are independently replayed, including endpoint tasks, angular-count transitions and largest error contributions. Unsampled fine-mesh tasks are audited producer records. V164 remains the separate complete coarser replay.

Choose epsilon from a near-task endpoint. Retain the near intervals beyond epsilon and sum them as [N_-,N_+]; sum every midpoint interval as [W_-,W_+]. The inner tasks are replaced, without duplication, by the analytic pole bound below. Taking the best of finitely many admissible epsilons selects among proved inequalities and does not claim a globally optimal epsilon.

The analytic dependencies are the accepted global profile certificate, the quadratic pole theorem (V148), the homogeneous exterior theorem and its angular refinement, the midpoint sliver estimate, and compact approximation. Their source and proof hashes must agree with the accepted records. The parent proof specifies the witness and all these dependencies; the present argument gives the complete recombination.

## Pole disks

Write alpha=1/2, k=2^(alpha-1), C_e=(1-2epsilon)^(alpha-1), and

    A=Gamma(1+alpha/2)/(2sqrt(pi)Gamma(3/2+alpha/2)),
    M=lambda A epsilon^alpha/alpha+epsilon^2/4,
    E_c=alpha C_e^3 epsilon^(3-2alpha)/(6pi lambda^2(3-2alpha)),
    E_s=epsilon^(alpha+2)/((alpha+2)(1-epsilon)^2).

Require 0<epsilon<1/2, (lambda+k)epsilon^alpha<=c+1/2 and lambda epsilon^alpha<=1/2. The quadratic pole theorem gives the per-pole lower bound M-E_c-E_s. In that theorem the negative clamp contribution is bounded by integrating its positive quadratic majorant, using P(u)>=alpha |u|^alpha(-u_1/|u|)^2. The pure projection contributes lambda A epsilon^alpha/alpha. Harmonicity makes the opposite-pole constant contribution exactly epsilon^2/4. The own-pole constant has zero circular mean, so this retains the original principal-value convention.

For the upper bound use U_c=0 if alpha C_e epsilon^(1-alpha)<=lambda/2 and U_c=alpha C_e epsilon/pi otherwise. The sign-controlled upper pole estimate is M+E_s+U_c. Every condition is checked with outward ball endpoints.

## Exterior and midpoint hole

Set H=sqrt((b+1/2)^2+b^2), B=max(H^alpha+|c|,1/2+2^(-alpha)) and q=1/(4R^2). Require lambda(1+2^(-alpha))>=1. The accepted six-lobe angular formula defines a_3(alpha). The homogeneous exterior theorem gives

    T=2a_3(alpha)R^(alpha-1)/(1-alpha),
    E_T=4B/(pi R)+B/(3R^3(1-q)^2)
                         +R^(alpha-3)/(2(3-alpha)(1-q)^2).

The exterior integral differs from T by at most E_T. Its dipole decay is integrable because alpha<1. For the midpoint hole of radius eta=1/100 the absolute error is

    E_0=2^(alpha+3)eta^(alpha+3)/(pi(alpha+3)sqrt(1-eta^2)).

There is no separate pointwise-at-infinity assumption or full Holder norm in this argument.

## Exact recombination

With each sign selecting the indicated outward endpoint, the trace-free increment I0 is in [L,U], where

    L=2N_-+W_-+T_-+2M_--2(E_c)_+-2(E_s)_+-(E_T)_+-(E_0)_+,
    U=2N_++W_++T_++2M_++2(E_s)_++2(U_c)_++(E_T)_++(E_0)_+.

For this witness the R_1^2 increment is I0+1/2. Rotation of both the witness and its increment direction through pi/2 changes the T_xx increment to -I0, while preserving the function increment -1 and hence the identity gain +1/2. Consequently D_(1/2)>=max(|I0+1/2|,|-I0+1/2|)=1/2+|I0|>=1/2+max(0,L,-U). This also explains the absolute-value convention in the parent acceptance code.

Finite optimization over admissible epsilon retains validity. Exact rational arithmetic checks the recombination and the downward ten-place decimal rounding. Acceptance binds all imported intervals, sources, selected replays, analytic proofs and this statement, and explicitly identifies the partial independent replay scope.
