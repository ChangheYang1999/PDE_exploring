# A double-factor low norm and a conditional Fredholm estimate

## Statement and exact hypothesis

Use the actual modal field, b, p, X_s and D_s of topics123,126 and130. In particular b=e^((3+delta)t) for t<=-1, b=e^(gamma t) for t>=1, delta=9/5, gamma=-1/2, and sigma=25/4. Put S=T+C_R and fix a finite L>=0. For 0<epsilon<=1 let X_(s-epsilon) be the same bulk/cofactor space with the two orders lowered by epsilon, retaining the same weights, physical parity and zero vertical trace. Define

 N_0(h)=||h/[b(t) cos(theta)^4]||_L2(dt dtheta).

This is a Hilbert norm on its completion. It does not replace X_s or its transport domain.

Assume the following estimate, which is not proved here:

 ||h||_Xs<=C_s[||(S-lambda)h||_Xs+||h||_X(s-epsilon)],
                 h in D_s, 0<=lambda<=L.               (H)

Then there is a compact map K from X_s into

 W=X_(s-epsilon) direct-sum N_0-completion

and a finite C_1, independent of lambda in [0,L], such that

 ||h||_Xs<=C_1||(S-lambda)h||_Xs+||K h||_W.             (1)

The sum norm is used on W. The compact operator is specified below by two radial cutoffs. Thus the actual compact-error assertion H3 follows from (H). This theorem is conditional: neither (H), low injectivity nor a numerical inverse constant is asserted.

## Hardy bounds, interpolation and local compactness

Write v=h/b and u=chi_y h/(b p). Away from the vertical axes, cos(theta)^(-4) is bounded, so N_0 is controlled by the bulk L2 norm. Near a vertical axis let phi be its signed angular distance and choose a smaller sector where chi_y=1. The cofactor u is even in phi and has zero trace. Since sigma>3/2, its first normal trace also vanishes. Taylor's integral formula gives

 u(t,phi)/phi^2=integral_0^1 (1-a) u_(phi phi)(t,a phi) da. (2)

Minkowski's inequality on a finite one-sided sector gives the explicit estimate

 ||u/phi^2||_L2 <= [integral_0^1 (1-a)a^(-1/2) da]
                          ||u_(phi phi)||_L2
                    =(4/3)||u_(phi phi)||_L2.          (3)

The norm on the right may be taken over the larger sector, since scaling its argument inward only shortens the integration interval after change of variables. Reflect for the other side. The factor phi^2/cos(theta)^2 is smooth and bounded there. Since v/cos^4=sin(theta)u/cos^2, (3) proves

 N_0(h)<=C_H||h||_Xs.                                  (4)

Formula (2) is a direct proof of the double Hardy step; applying an unweighted first-order Hardy inequality twice without accounting for the intermediate weight would not by itself justify it.

Differentiating (2) once in t or phi gives bounded maps from H^3 of the cofactor strip to H^1 of its double quotient. The dilation integrals are finite: the t derivative uses the same integral4/3, and the phi derivative uses integral_0^1(1-a)a^(1/2)da=4/15. Smooth cutoffs and the factor phi^2/cos^2 do not change boundedness. Thus for every compactly supported radial cutoff psi, h->psi h is compact from X_s to the N_0 completion, by H^1-to-L2 compactness on a bounded strip. Away from the vertical axes the usual local H^s_0-to-L2 compactness suffices.

The same map is compact X_s->X_(s-epsilon). Locally the order gap is epsilon, and the dyadic high-frequency tail of the lower norm is bounded by 2^(-J epsilon) times the high norm; finitely many smoothed blocks on a bounded strip are compact. This argument applies both to the variable-order bulk and the constant-order cofactor, and it preserves the closed trace condition.

Finally, for every eta>0 there is C_eta<infinity with

 ||h||_X(s-epsilon)<=eta||h||_Xs+C_eta N_0(h).           (5)

To prove this, split the dyadic blocks above and below J with 2^(-J epsilon) small enough. High blocks give the first term. The finite low blocks are controlled by ||v||_L2 and ||u||_L2. The first is at most N_0(h); the second is at most C N_0(h), since on the cofactor support |chi_y/p|<=C cos^(-4). This also checks the endpoint weights in (5): the same b occurs in all three norms.

## Exact low energy

Let beta=(log b)', W=(q,vartheta) and

 kappa=1+ell-(1+beta)q+4 vartheta tan(theta).             (6)

The quotient vartheta tan(theta) has a bounded continuous extension across the vertical axes, by parity and the bounded first angular derivative of vartheta. The exact divergence formula is

 div_C W=partial_t q+partial_theta vartheta=2ell-2q.     (7)

Indeed physical div V=2ell, while the physical area form is e^(2t)dt dtheta. With omega=b^(-2)cos^(-8), integration by parts gives

 -Re<T h,h>_N0=integral_C kappa |h/(b cos^4)|^2 dt dtheta. (8)

For smooth compactly supported core functions there is no boundary term at a vertical axis: h/(b cos^4) is bounded there, and vartheta=O(cos theta). Radial compact support removes the radial boundary.

Equation (8) holds on all of D_s. Here is a justification that does not assume an unproved graph-core statement. For core initial data integrate the finite-time norm identity along the actual transport flow. Since kappa is bounded, this flow is bounded on N_0 for every finite positive or negative time. Approximate arbitrary X_s data by the trace-preserving dense core from proof 126. Its X_s finite-time bound and (4) pass the integrated N_0 identity to the limit. For h in D_s, the X_s semigroup derivative at time zero exists and is T h, by the maximal-domain theorem of proof 126. The continuous embedding (4) gives the same derivative in N_0. Differentiating the integrated identity at zero proves (8). All products in (8) are integrable because kappa is bounded.

## Positive end limits

At the origin beta=3+delta, q->-A cos^2+D sin^2 and vartheta tan(theta)->Sigma sin^2(theta), uniformly. The last convergence follows directly from C1 convergence of vartheta and its zero values on each vertical axis. Alternatively uniform convergence plus a uniform second-derivative bound gives C1 convergence by the elementary interpolation inequality on the circle. Therefore

 kappa_-(theta)=(3Sigma/2+delta A)cos^2(theta)
                       +(3Sigma/2-delta D)sin^2(theta).

The two exact coefficients are

 kappa_x=(63ell-24)/5,
 kappa_y=(9ell-6)/5.                                   (9)

At infinity beta=gamma=-1/2, q->ell and vartheta tan(theta)->0 uniformly, so

 kappa_+=1+ell/2=m_infinity.                            (10)

All coefficients in (9) exceed (10) for the exact ell; in particular kappa_y-m_infinity=(13ell-22)/10>0. Thus for any fixed 0<c_0<m_infinity there is T_e with kappa>=c_0 whenever |t|>=T_e-1. For a function g in D_s supported in that region and Re lambda>=0, (8) and Cauchy-Schwarz give

 (c_0+Re lambda)N_0(g)<=N_0((T-lambda)g).               (11)

No normal-family inverse and no first-order perturbation estimate enters this low energy bound.

## Coupling tails in N_0

For translated end cutoffs psi_E^R supported in |t|>=R-1, equal to one for |t|>=R and with bounded derivatives, one has

 N_0(psi_E^R C_R h)<=e_R||h||_Xs,  e_R->0.              (12)

One proof combines (4) with the full X_s tail result of proof 138. There is also an independent proof giving a decay rate and using only the matrix estimates of proof 123, as in the theory author's proposed Lemma D. Those six matrices and their Schur sums give small H^sigma norm of the unprojected cofactor output and a small bulk norm on the ends. Its axis trace is Gamma_C[h]/a. The trace map H^(5/2)(R^2)->H^2(R) bounds the localized axis coefficient by the localized unprojected cofactor norm, with a slightly larger radial cutoff. Subtract this coefficient, obtaining an even cofactor with zero value and first normal trace. Apply (3) to its H^2 norm. Away from the vertical axes, the subtracted term is controlled by the same H^2 trace norm. This proves (12) and, with constants depending on the cutoffs, the rate

 e_R<=C[exp(-(2-delta)R)+exp(-(1-k)R)]                  (13)

for R sufficiently large. The weaker half-exponent rate stated in the theory author's Lemma D follows as well. A trace has not been incorrectly promoted to H^sigma: only H^2 of the trace is used for N_0.

## Compact-error assembly

Let f=(S-lambda)h, psi_m=1-psi_E^R and let C_2 be a uniform X_s multiplier bound for psi_E^R. Apply (H), split its lower norm, and use (5) on psi_E^R h:

 ||h||_Xs<=C_s||f||_Xs+C_s||psi_m h||_X(s-epsilon)
                 +C_s eta C_2||h||_Xs+C_s C_eta N_0(psi_E^R h).

By (11), (12) and the exact cutoff identity,

 N_0(psi_E^R h)<=c_0^(-1)[C_H||f||_Xs+e_R||h||_Xs
                                      +N_0(q(psi_E^R)'h)].

The first term uses |psi_E^R|<=1 in N_0, not an unrecorded high-norm cutoff constant. Choose eta so C_s eta C_2<=1/4, then R large enough that C_s C_eta e_R/c_0<=1/4. Absorption proves (1) with

 C_1=2C_s(1+C_eta C_H/c_0),
 K h=(2C_s psi_m h, 2C_s C_eta c_0^(-1)q(psi_E^R)'h).    (14)

Both factors have compact radial support. Local compactness proved above applies to the first component and to (psi_E^R)'h in the second. Multiplication by bounded q is bounded in N_0, so the second is compact too. All choices are independent of lambda in [0,L]. This proves the conditional theorem and audits the theory author's Proposition H3-red, including its constants and exact compact-map target.

## Scope

The new low norm has a positive actual end energy in every angular direction and is controlled by X_s. It resolves the compactness reduction once (H) is known. It does not supply the missing high-frequency estimate (H). A bounded transport commutator alone, without comparison to the small positive endpoint margin, is not a proof of (H).
