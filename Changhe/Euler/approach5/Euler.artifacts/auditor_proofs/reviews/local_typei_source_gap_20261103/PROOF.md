# A scalar Gronwall error in a specific local Type I proof

Status: independent reconstruction of LIT109. The entire submitted proof, the actual source statement, the relevant preceding estimates, and rendered printed pages15-16 are read. The exact scalar obstruction is checked independently. A715-A716 refute the exact printed inferences stated below. Focused configured-model comparison remains pending. The source theorem is not refuted.

## 1. Exact source and scope

The source is D. Chae and J. Wolf, On the local Type I conditions for the 3D Euler equations, arXiv1707.00377v1, dated3 July2017. The pinned PDF has22 pages. This audit concerns Lemma3.2, its equation(3.17), the definition of X immediately below it on printed page15, and the differential claim and equation(3.18) on printed page16.

The source Theorem1.1 assumes a local Euler solution v with uniformly bounded local L2 velocity, local-in-time W1,infinity regularity before the terminal time0, and W2,p0 initial data for p0>3. A local limsup of (-t)||grad v|| below1 is its smallness condition. The asserted conclusion is a uniform W2,p0 bound on every smaller ball. Its Section4 applies Lemma3.2 after obtaining a sub-Type-I power bound for the gradient. This audit does not challenge the theorem's truth or prove that its entire proof is unrepairable.

Lemma3.2 uses p>3 and0<beta<1. Write Y(t) for its nonnegative cutoff integral of |grad curl w|^p. Using capital C to avoid confusion with the similarity exponent, the displayed scalar inequality is

    Y(t)<=C integral_(-1)^t (-s)^(-beta)Y(s)ds
             +C(-t)^(-p-beta+1)+Y(-1).              (1)

Take a fixed estimate constant C>1, enlarging it if needed. The printed auxiliary function is

    X(t)=integral_(-1)^t (-s)^(-beta)Y(s)ds
       +C/((p+beta-1)(C-1)) (-t)^(-p-beta+1)
       +Y(-1).                                     (2)

The following page claims a differential inequality with coefficient proportional to (-t)^(-beta), and then

    X(t)<=X(-1) exp(C integral_(-1)^t (-s)^(-beta)ds).
                                                       (3)

Changing a fixed positive C between estimates does not affect the obstruction below. A coefficient C=1 makes(2) undefined and C<1 removes positivity; neither repairs the stated positive-auxiliary-function argument.

## 2. The displayed auxiliary function cannot satisfy the claimed estimate

Let m=p+beta-1>0 and q=C/(m(C-1))>0. Because Y is nonnegative and its initial integral is finite,

    X(t)>=q(-t)^(-m), X(-1)=q+Y(-1)<infinity.

Therefore X(t) tends to infinity as t tends to0 from below. On the other hand,

    integral_(-1)^0 (-s)^(-beta)ds=1/(1-beta)<infinity.

Consequently the right side of(3) is bounded uniformly before0. Thus(3) contradicts the explicit positive term in(2), regardless of any extra Euler properties of Y. The contradiction is stronger than a failure to establish a sufficient estimate: that displayed bound for that displayed X is impossible.

For a direct test of the scalar inference, take Y(t)=0 for all -1<=t<0. It satisfies(1). Equation(2) reduces to X(t)=q(-t)^(-m), with

    X'(t)/X(t)=m/(-t).

No fixed finite K can give X'(t)<=K(-t)^(-beta)X(t), since it would require m<=K(-t)^(1-beta), whose right side tends to0. The original printed equality for X' is therefore false as well. More generally(1) alone permits Y(t)=(-t)^(-m), since its forcing term dominates Y when C>=1. Hence a uniform Y bound requires an argument not contained in(1)-(3).

This is an exact scalar counterexample, not numerical evidence. No computation is needed.

## 3. Relation to this campaign

The campaign gradient-gap reconstruction C35 uses a different localized Holder argument. At its first stage a coefficient C1/(T-t) is retained and produces a polynomial Holder bound, not a uniform bound. A logarithmic singular-integral estimate then improves the gradient. Its later uniform bound uses bounded annular velocity and vorticity and the Dini gradient integral. It never introduces an auxiliary function of the form(2) and does not rely on this source lemma.

This audit identifies a gap in one specified manuscript proof. It does not refute Lemma3.2, Theorem1.1, the existence of a different proof, the global BKM criterion, or any unexamined later version. All such conclusions would require additional evidence. The actual PDF and page images are pinned here, so the statement can be checked without trusting an abstract or a text-extraction artifact.

## 4. Separate precision issue in Appendix A

Printed Lemma A.4 on page21 states, for1<p<infinity, a finite constant C_p such that every u in W1,p(B(R)) and every nonnegative smooth compactly supported cutoff phi obey

    ||(grad u)phi||_p
       <=C_p[||(curl u)phi||_p+||grad phi||_infinity ||u||_p].    (4)

No divergence-free hypothesis or divergence term appears. At that literal scope the statement is false. Fix phi equal to1 on B(R/2), supported in B(3R/4), and let K=||grad phi||_infinity>0. Fix a nonzero smooth scalar f supported in B(1), with ||grad f||_p and ||Hess f||_p both positive. For0<epsilon<R/2 set

    f_epsilon(x)=f(x/epsilon), u_epsilon=grad f_epsilon.

Then curl u_epsilon=0, its support lies where phi=1, and exact scaling gives

    ||Hess f_epsilon||_p=epsilon^(3/p-2)||Hess f||_p,
    ||grad f_epsilon||_p=epsilon^(3/p-1)||grad f||_p.

Inequality(4) would imply ||Hess f||_p<=C_p K epsilon ||grad f||_p for every sufficiently small epsilon, which is impossible. The initial draft incorrectly described the right side as zero: it contains a product of two norms, not the norm of u times grad phi. That sentence is withdrawn. The scaling argument above tests the actual displayed inequality.

The proof's preceding claimed inequality ||grad(u phi)||_p<=C_p||curl(u phi)||_p is itself directly contradicted by u=grad f supported where phi=1: here the right side is zero and the left side is positive. This proof-step counterexample should not be confused with the scaling counterexample needed for its final stated bound.

Adding div u=0, or including the corresponding divergence term in(4), removes this specific obstruction. The application to derivatives of a divergence-free Euler velocity has the needed divergence-free property. Even under that added hypothesis, u phi generally has nonzero divergence, so the proof should use the full div-curl inequality and absorb div(u phi)=u.grad phi into the existing cutoff term. This missing general-statement hypothesis is logically separate from the Gronwall error and does not alone invalidate the Euler application. It is an additional observation for review, not part of LIT109's submitted claim.

## 5. Evidence and review

The source pin, text extraction, and the rendered printed pages15,16 and21 are in verification and were visually inspected. The Appendix A literal missing hypothesis is checked by the shrinking-potential scaling argument above. The proof was written before any computation. Existing configured-model review is requested through files only. No new model client or external communication was used.
