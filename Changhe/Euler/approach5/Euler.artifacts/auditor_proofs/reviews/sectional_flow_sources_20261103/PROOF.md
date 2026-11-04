# Equilibrium atoms and the scope of two sectional-flow arguments

Status: A437 REFUTES the three bare implications by explicit countertests; A438 CONFIRMS the recurrence lemma, ergodic-decomposition repair and exact source-scope findings after a focused configured-model review. The full existence theorems remain OPEN in A439. The review configuration is the primary model; this is not independent provider attestation.

## 1. Exact claims and notation

For a smooth flow \(\phi_t\), write \(f=\phi_1\). At an invariant set carrying a splitting \(E^s\oplus E^{cu}\), put

\[
J(x)=\log|\det(Df|_{E^{cu}_x})|.
\]

The following three implications are false without a further exclusion of equilibrium components:

1. In central dimension two, a dominated splitting with contracting \(E^s\) and an ergodic probability satisfying \(h_\nu(f)-\int J\,d\nu>0\) forces \(\nu\) to be supported on an attracting periodic orbit.
2. In that setting, a positive central area exponent forces all central exponents except the neutral flow exponent to be positive.
3. Hyperbolic saddle equilibria, domination, \(|\det(Df|_{E^{cu}})|\ge1\), and \(h_\nu(f)\ge\int J\,d\nu\) force \(\nu\) to have a non-atomic part.

These are statements about the displayed dynamical data at an invariant probability. We do not assert counterexamples satisfying every attracting-set or positive-volume empirical-limit hypothesis of either manuscript.

A separate valid statement is the following. Let \(f\) be a continuous map of a compact metric space, and let \(S\) be a closed set. If, for every \(\varepsilon>0\), some open neighborhood \(B_r(S)\) satisfies

\[
\limsup_{n\to\infty}\frac1n\sum_{j=0}^{n-1}
\mathbf 1_{B_r(S)}(f^j x)<\varepsilon,
\tag{1}
\]

then every weak limit of the empirical probabilities of \(x\) gives \(S\) zero mass. In the application, \(S\) is the finite equilibrium set. No entropy premise is needed for this conclusion.

## 2. One linear family proves all three countertests

Choose real numbers \(d>b>0\) and \(q>0\), and consider

\[
G(x,y,z)=(-dx,-by,qz),\qquad
\phi_t(x,y,z)=(e^{-dt}x,e^{-bt}y,e^{qt}z).
\]

This flow is smooth and complete. At its hyperbolic saddle equilibrium \(0\), let

\[
E^s=\mathbb Re_1,\qquad E^{cu}=\operatorname{span}(e_2,e_3).
\]

In the Euclidean norm, for every \(t\ge0\),

\[
\|D\phi_t|_{E^s}\|=e^{-dt},\qquad
\|D\phi_{-t}|_{E^{cu}}\|=e^{bt},\qquad
\|D\phi_t|_{E^s}\|\|D\phi_{-t}|_{E^{cu}}\|=e^{-(d-b)t}.
\]

Thus the stable contraction and domination conditions hold at this invariant set. The probability \(\delta_0\) is ergodic for the flow and for \(f\). Its entropy is zero: every measurable partition has only one positive-measure atom modulo \(\delta_0\), including all its dynamical joins. Its Lyapunov exponents are

\[
-d,\quad-b,\quad q,
\]

and \(J(0)=q-b\). There is no nonzero flow vector at the origin, hence no neutral flow direction to remove from this list. Averaging \(\delta_0\) over flow times leaves it unchanged.

For \((d,b,q)=(4,2,1)\), one has \(J=-1\), \(h-J=1>0\) and a positive exponent \(1\). The measure is supported on a saddle equilibrium, not an attracting periodic orbit. This refutes implication 1.

For \((d,b,q)=(4,1,2)\), the central area exponent is \(1\), while the central exponents are \(-1\) and \(2\). Equivalently, the logarithmic norm of the inverse central exterior square is \(-1\). This refutes implication 2.

For \((d,b,q)=(4,1,1)\), the central determinant is exactly \(1\), and both entropy and the integral of \(J\) are zero. All three equilibrium exponents are nonzero, and the measure is purely atomic. This refutes implication 3.

If a compact ambient manifold is desired for these local tests, place the displayed vector field in a coordinate ball of a three-torus and multiply it by a smooth cutoff equal to one near the origin and supported in that ball. Extend by zero. The resulting smooth compact-manifold flow is complete and has the same derivative, invariant splitting and probability at the origin. This observation does not give a trapping region whose entire maximal invariant set has the required splitting or expansion. In particular, the linear singleton is a saddle, not an attracting set.

## 3. The weak-recurrence conclusion

Let \(\mu_{n_k}=n_k^{-1}\sum_{j=0}^{n_k-1}\delta_{f^j x}\) converge weakly to \(\mu\). For any \(\varepsilon>0\), choose \(r\) as in (1). The set \(B_r(S)\) is open, so Portmanteau gives

\[
\mu(S)\le\mu(B_r(S))
\le\liminf_{k\to\infty}\mu_{n_k}(B_r(S))
\le\limsup_{n\to\infty}\mu_n(B_r(S))<\varepsilon.
\]

Therefore \(\mu(S)=0\). No claim about an arbitrary boundary measure, convergence of indicator integrals, or existence of a generic point for a nonergodic measure is used. A zero-entropy statement cannot replace (1), as \(\delta_0\) in Section 2 illustrates.

## 4. Actual source passages and the unresolved steps

The versioned source manuscripts are:

- Araujo, Salgado and Sousa, *Physical measures for mostly sectionally expanding flows*, arXiv:2205.04207v6, manuscript dated 29 October 2025, 56 pages. Its arXiv metadata title omits the final `ly` in `sectionally`; the PDF title is the one used here.
- Araujo and Salgado, *Physical measures for asymptotically sectional expanding flows in higher co-dimensions*, arXiv:2511.18986v1, manuscript dated 25 November 2025, 30 pages.

The exact PDFs and extracted text are pinned in the team records, along with the submitted LIT88 proof. The relevant rendered pages were independently inspected. This audit concerns those versions. A publisher record for the first paper does not establish that the final published proof is identical.

### 4.1. First source: the precise residual equilibrium case

Theorem E, page 13, assumes a partially hyperbolic attracting set with central dimension two and a positive-volume expanding set. Neither stable contraction and domination on pages 4-5 nor this theorem excludes equilibria. Its displayed expansion premise concerns a positive-volume set of initial points, not every ergodic component of a selected empirical limit.

On page 42, set \(\Upsilon=\{y:\mu_y(J)>0\}\), where \(\mu_y\) are ergodic components for \(f\). The sentence saying that every component in \(\Upsilon\) has only positive central exponents apart from the neutral flow exponent is literally false at an equilibrium, as the second countertest shows. Both uses of that sentence survive, however. At an equilibrium atom in \(\Upsilon\), one has \(h-J=-J<0\) directly. For a component satisfying \(h=J>0\), positive entropy already excludes an equilibrium atom, and its two central exponents are indeed \(0,J\). This is a harmless misstatement, not a second gap in the argument.

The substantive unresolved step is Claim 5.3, page 43. It obtains a component outside \(\Upsilon\) with

\[
\mu_y(J)\le0,\qquad h_{\mu_y}(f)-\mu_y(J)>0,
\]

and asserts that its flow average is supported on an attracting periodic orbit. If the component gives equilibria zero mass, its central exponents are \(0,\mu_y(J)\). Ruelle's inequality rules out \(\mu_y(J)=0\), and the usual sink argument applies to the remaining negative transverse exponent. At an equilibrium atom \(\delta_\sigma\), the displayed strict inequality instead says exactly \(J(\sigma)<0\). An actual hyperbolic sink is still handled by the source's basin argument. What remains untreated is an atom at a non-sink equilibrium with negative central trace. It may be a hyperbolic saddle, as in the first countertest, or a nonhyperbolic equilibrium with a nonnegative central real part. Theorem E does not assume hyperbolicity of the equilibria.

No premise of Theorem E, or of Theorem 1.6 on page 11 or Theorem 1.10 on page 15 used in its proof, excludes those components. Theorem 1.6 requires that the initial trajectory not converge to an equilibrium; this does not prevent an empirical limit from charging one. Theorem 1.10 bounds entropy for the whole empirical measure. It does not assign the same lower bound to each component. Slow recurrence (SR), page 8, would exclude equilibrium mass by Section 3; condition (21), page 13, would exclude the offending negative central trace, as Remark 5.5 on page 43 explains. These are premises of separate results, including Theorem B and Corollaries D and F. Page 17 explicitly notes that (SR) was not assumed for Theorem E.

The local examples do not realize the theorem's full empirical-limit construction. They refute the bare component inference, not Theorem E. An additional global argument excluding or treating precisely these non-sink equilibrium atoms is still required in the written proof.

### 4.2. Second source: equality in the determinant hypothesis

Theorem A(A), page 8, permits \(|\det(Df|_{E^{cu}_\sigma})|=1\) at a saddle-type hyperbolic equilibrium. Its other premises do not exclude this equality. The pointwise expansion assumption is imposed away from the stable manifolds of equilibria and gives no direct bound on equilibrium mass in an empirical limit of an initial point in the trapping region. On page 12, equation (11) instead uses strictly positive central logarithmic determinant at every equilibrium in the atomic part. The third countertest invalidates this strict-positivity inference. The equality is also present in the authors' Section 3.1 matrices, page 14, equation (12): their two central diagonal entries have opposite signs and zero sum. This is evidence that equality lies within the written range, not a global counterexample.

Replacing (A) by strict inequality repairs this particular purely atomic case. Equilibrium atoms then have positive central Jacobian integral. Regular periodic atoms have positive integral from the pointwise expansion condition and the argument in Section 4.3 below. A positive weighted average remains positive, contradicting zero entropy and the lower entropy bound. For the mixed branch with a nonzero non-atomic part, the source uses only nonnegativity of the atomic central integral. Thus strict (A) repairs the equilibrium step locally without requiring a different mixed-branch argument. Under the alternative weak-recurrence premise (B), Section 3 excludes equilibrium atoms. These repairs do not certify the complete existence or physical-basin conclusion.

### 4.3. Complete repair of the nonergodic generic-point passage

The sentence on page 11 invoking a point generic for a possibly nonergodic non-atomic measure is not supplied by Birkhoff's theorem. The entropy-formula step nevertheless has the following repair.

Let \(\mu\) be an \(f\)-invariant probability on a compact flow-invariant set with continuous invariant splitting \(E^s\oplus E^{cu}\), uniformly contracting \(E^s\), and \(\dim E^{cu}\ge2\). Assume the flow is \(C^2\), its nonzero flow direction lies in \(E^{cu}\), \(\mu(\operatorname{Sing})=0\), and, for \(\mu\)-almost every \(z\),

\[
\liminf_{n\to\infty}\frac1n\sum_{j=0}^{n-1}\psi(f^jz)
\le-c_0(z)<0,\qquad
\psi=\log\|\wedge^2(Df|_{E^{cu}})^{-1}\|.
\tag{2}
\]

Then

\[
h_\mu(f)\le\int J\,d\mu.
\tag{3}
\]

If the reverse inequality is also known, equality holds for \(\mu\) and for almost every component of its ergodic decomposition. No uniform positive lower bound on \(c_0(z)\) is needed.

Indeed, for \(\mu\)-almost every \(z\), the empirical measures of \(z\) converge to an ergodic component \(\mu_z\), and \(\mu=\int\mu_z\,d\mu(z)\). Conditional Birkhoff averages of the continuous function \(\psi\) give

\[
\mu_z(\psi)\le-c_0(z).
\]

Moreover \(\mu_z(\operatorname{Sing})=0\) for almost every component, since its nonnegative integral equals \(\mu(\operatorname{Sing})=0\). Along such a component the flow vector has exponent zero: covariance identifies its iterates with the bounded flow vector at \(f^nz\), giving a nonpositive exponent, while recurrence to a set where its norm is bounded below excludes a negative exponent. Oseledets regularity supplies the exponent's existence. This argument needs neither time-one ergodicity of the entire \(\mu\) nor integrability of the logarithm of the flow speed.

Write the central exponents of \(\mu_z\), with multiplicity, as \(\chi_1\le\chi_2\le\cdots\). Submultiplicativity of the inverse exterior-square cocycle gives

\[
-(\chi_1+\chi_2)
=\lim_{n\to\infty}\frac1n
\log\|\wedge^2(Df^n|_{E^{cu}})^{-1}\|
\le\mu_z(\psi)\le-c_0(z).
\]

Since one central exponent is zero, \(\chi_1<0\) would imply \(\chi_2\le0\), a contradiction. Thus \(\chi_1=0\) is simple and every other central exponent is at least \(c_0(z)>0\). Uniform contraction supplies only negative exponents in \(E^s\), so the sum of all positive exponents is \(\mu_z(J)\). Ruelle's inequality gives \(h_{\mu_z}(f)\le\mu_z(J)\). Entropy is affine under ergodic decomposition; integrating proves (3). If equality holds after integration, the nonnegative component deficits have integral zero and therefore vanish almost everywhere.

In the source, the equilibrium set is finite and the considered non-atomic measure gives it zero mass. Almost every point is outside every equilibrium stable manifold, since convergence to an equilibrium would give that equilibrium atom as its empirical limit. The pointwise hypothesis therefore supplies (2). The same proof applies to the non-atomic measure \(\eta\) in the mixed branch on page 12, and to a regular periodic component with its own positive constant. This audit certifies the entropy-formula repair only. Further assertions using Ledrappier-Young theory or positive-volume basins are outside this targeted check.

### 4.4. Limiting quantifiers

The first source defines (wASE) by a positive upper limit on page 11, equation (15), but Theorem E on page 13 displays a positive lower limit of \(T^{-1}\log|\det(D\phi_T|_{E^{cu}})|\). The following prose on page 14 describes a sequence of times, and the forward proof on page 42 selects such a sequence. The second source repeats the lower-limit display and sequence description on page 6. A positive lower limit implies the sequence condition; the converse does not follow from the definition alone. We retain the stronger displayed hypothesis when recording the theorem.

For central dimension two, the inverse exterior-square logarithm is exactly the negative logarithmic determinant. Thus the forward proof uses only the integer-time upper-limit form. In the converse argument on page 44, the displayed chain actually bounds the upper limit of the inverse-area growth by a strictly negative number. Bounded derivatives over the remaining bounded time interval then give the positive lower limit for all real times. This sharpens the quantifier bookkeeping but does not supply the missing equilibrium-component argument in Claim 5.3.

## 5. Euler scope and dependencies

The backward Euler carrier spectrum \((1-2c,0,-1-c)\) is known on the regular ergodic measures specified in A399. This measurewise spectrum alone does not construct a continuous invariant splitting on the compact core, establish domination, or exclude invariant probabilities on the carrier or vorticity zero sets. Those are precisely among the premises that a proposed use of these sectional-flow sources would need to check.

The present note proves no bound on \(\Gamma_Z\), gives no global decaying Euler counterexample, and changes neither A417 nor A422. The unrestricted C2 coverage and helicity-sign questions remain open. Dependencies of the countertests are explicit linear ODEs, the definition of entropy on a singleton, and the determinant identity. The recurrence argument uses Portmanteau. The source assessment is a targeted proof audit, not certification or refutation of either full paper. The focused review did not re-audit this Euler-context paragraph; its references are the auditor's previously checked A399, A417 and A422. Source-counterexample suggestions in Section 9 of the received review remain separate, unverified proposals and are not used here.
