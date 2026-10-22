# Smooth fields within the finite spline representation

Written 2026-10-21 before the exact controls. Status: CONFIRMED mathematical counterexample to a universal representation claim; 61 exact controls and a separate negative control passed, and the actual Opus5.5 reviews were independently checked. It is not a B2 profile or an existence construction.

## Statement

Consider the finite degree-five clamped B-spline representation from packet169. Its radial variable is t=1-(1+r^2/L^2)^(-1/(2b)), with b,L>0; its temperature and vorticity envelopes are (1-t)^(b+2) and (1-t)^(b+1). Keep only angular mode zero, set every coefficient of that mode equal to1, and set all other angular coefficients to0. Then the exact represented physical fields are

    Theta(x,y)=x^2(1+(x^2+y^2)/L^2)^(-(b+2)/(2b)),
    Omega(x,y)=x(1+(x^2+y^2)/L^2)^(-(b+1)/(2b)).

Both are real analytic on the entire finite plane. They have the prescribed x parity and Theta(0,y)=0, with Theta=x^2+O(r^4) and Omega=x+O(r^3). All interior radial spline derivative jumps vanish. Thus a finite field in this representation can be smooth, even with nonzero center coefficients. A nonzero fifth-derivative jump must be established from the actual coefficients; it does not follow from finite spline degree alone.

For b=beta=4 and L=1 the additional local relation Omega_x(0)=4a0/beta holds, with a0=1. Nevertheless these fields are not B2 profiles: the canonical relative inverse has center strain Psi_xy(0)=0 instead of1+beta/2=3. This last failure prevents confusing the representation counterexample with a candidate.

## Proof of the spline identity

Let the nondecreasing knot list have endpoints0 and1 repeated p+1 times and simple interior knots, with p=5. The degree-zero basis consists of indicators of consecutive nonempty knot intervals. Their sum equals1 in (0,1). The Cox-de Boor recursion is

    B_(j,p)(t)=(t-k_j)/(k_(j+p)-k_j) B_(j,p-1)(t)
              +(k_(j+p+1)-t)/(k_(j+p+1)-k_(j+1)) B_(j+1,p-1)(t),

with zero contributions when a denominator vanishes. In the sum over j, the coefficient of a nonzero lower-degree basis function B_(j,p-1) is

    (t-k_j)/(k_(j+p)-k_j)+(k_(j+p)-t)/(k_(j+p)-k_j)=1.

The two unmatched boundary terms have support of zero length under endpoint clamping. Induction therefore gives sum_j B_(j,p)=1 on (0,1); continuity and the clamped endpoint convention extend it to [0,1]. Coefficients all equal to1 represent the constant polynomial1 on every cell. Every derivative of positive order is zero, including both one-sided fifth derivatives at every interior knot. The other modes vanish identically. The radial and angular representation formulas now give the displayed physical fields exactly.

The scalar q=1+(x^2+y^2)/L^2 is strictly positive on R^2. The real function q^alpha=exp(alpha log q) is real analytic for q>0 for every real alpha. Composition with this positive polynomial and multiplication by x or x^2 prove global real analyticity at every finite point, including the center and every knot circle. Expanding q^alpha at q=1 proves the stated center expansions. The parity and axis conditions follow directly.

## Inverse and scope of the example

The vorticity is odd in x and even in y, smooth, and O(r^(-1/b)) at infinity. The canonical relative whole-plane velocity integral converges: its kernel difference has size O(|X|/|Y|^2) at large Y, so the tail is bounded by a constant times int_R^infinity r^(-1-1/b)dr. The local velocity kernel is integrable. The resulting stream function is odd in x and even in y, modulo a linear x term whose velocity is the allowed constant vertical gauge. In particular Psi_xy(0)=0. The same conclusion follows directly from the center strain integral, whose integrand contains the factor y times the even-in-y radial source; that derivative integral is absolutely convergent near zero and at infinity. The absolute velocity itself need not converge without the relative subtraction, and is not used here.

For b=beta=4, Omega_x(0)=1 and a0=1, but the required B2 center strain is3. Hence the exact thermal equation fails at quadratic order. At b=4 the temperature grows like r^(1/2) on nonaxial rays and the vorticity decays like r^(-1/4); no bounded-temperature claim is made. The strain conclusion uses the parity of the entire source, not its local jet alone. This counterexample establishes only the possibility of smooth finite fields in the representation, together with the invalidity of an automatic nonsmoothness inference. It says nothing about the regularity of an untested saved archive and does not undo the exact nonzero jumps already proved for the three archives in packet169. It also gives no B2 existence result, approximation guarantee or full NO theorem.

## Dependencies and verification plan

The proof uses the defining spline recursion, elementary real analytic composition, parity, and the canonical relative inverse fixed in SPEC.md and independently derived in earlier verifier packets. Packet169 gives the general jump criterion and the three certified nonsmooth archive applications. Exact rational coefficients and knots will be stored in verification/input.json. Independent cell-polynomial recursion will check partition of unity and derivative jumps; a separate exact derivative-coefficient calculation will provide a cross-check and a nonconstant negative control. No fitting-lane code is used. No Lean/Lake build is permitted.
