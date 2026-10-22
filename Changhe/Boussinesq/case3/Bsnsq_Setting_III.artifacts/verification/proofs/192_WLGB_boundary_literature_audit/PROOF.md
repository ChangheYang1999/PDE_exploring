# Primary boundary-profile claims and the wall trace

Status: CONFIRMED, 2026-10-21. Complete informal argument preceded controls and review; the tail and growth extensions were written before their separate review. Actual Opus354/356 partial and357 complete written reviews were adjudicated against the primary source and independent derivations. This packet audits a literature sentence and a possible calibration method. It establishes no B2 solution or exclusion.

## Statements and sources

The primary source is Yongji Wang, Ching-Yao Lai, Javier Gomez-Serrano and Tristan Buckmaster, Asymptotic self-similar blow-up profile for three-dimensional axisymmetric Euler equations using neural networks, arXiv:2201.06780v3. The downloaded versioned PDF and abstract page are retained with retrieval metadata and SHA256 digests in verification. The abstract revision table gives 7 May 2023, 23:57:49 UTC for v3. The PDF's internal title date is 9 May 2023; these are different kinds of date, not an altered version identification. Pages below are physical PDF page numbers, not supplementary printed page numbers.

The lead's frozen draft has five source assertions:

L1. The spatial domain is the upper half plane x2>=0 with impermeability u2(x1,0)=0. CONFIRMED as a statement of the source, physical PDF page1, after its equation(1).

L2. The source uses u=(1-t)^lambda U(y), theta=(1-t)^(lambda-1)Theta(y), y=x/(1-t)^(1+lambda). CONFIRMED, page1 preceding equation(2). Therefore its exponent translates to beta=1+lambda in the prompt's spatial similarity coordinate. This is an algebraic translation, not an identification of the two boundary-value problems.

L3. U1 is odd and U2 even under y1 reflection. CONFIRMED, page2 following equation(3). The same sentence assigns odd parity to Phi and Omega and even parity to Psi, where the source's Psi means the y2 derivative of temperature, not a stream function.

L4. The source reports lambda=1.917 plus or minus0.002. CONFIRMED, page2 Figure1 caption, hence beta=2.917 plus or minus0.002. Supplementary section1.4, physical page10, explains the reported spread using different random initializations and normalization checks. This is a numerical report, not a certified enclosure of an exact exponent.

L5. The reported equation residual amplitudes are approximately five orders smaller than the solution amplitudes. CONFIRMED, page3 discussion of Figure1, also its page2 caption. This statement describes the authors' numerical comparison; it is not a rigorous uniform residual estimate, solution-error estimate, or whole-plane verification.

The source enforces x parity by symmetrizing network outputs. The wall and normalization are imposed by loss penalties; no exact numerical satisfaction is inferred. The printed symmetric computational box and the absolute-value outer conditions do not alone settle which half plane was sampled. L1 records the stated physical problem, not an independently reproduced training domain. The reported exponent spread is not a bound on total error, including domain truncation.

The proposed insertion is accurate with its adjacent qualification that these are numerical boundary profiles without certified error control. No journal status or whole-plane theorem is being inferred.

## Derivation of the exponent conversion

Put tau=1-t. Equating the spatial coordinate denominators tau^beta=tau^(1+lambda) for every positive tau gives beta=1+lambda. Then beta-1=lambda and beta-2=lambda-1, reproducing the source's velocity and temperature powers. Addition of the exact constant1 translates the endpoints1.915 and1.919 to2.915 and2.919 without changing the reported half-width. The symbol lambda in this paper is a similarity exponent. It is not the numerics lane's forcing homotopy parameter.

The half-plane wall remains a physical boundary under this change of notation. In particular x reflection and the wall together force the boundary origin velocity to be zero: U1(0,0)=0 by oddness, U2(0,0)=0 by impermeability. B2 instead uses the full plane and a moving material center with only x reflection. Thus the cited computation cannot be imported as a B2 candidate merely by replacing its exponent symbol.

## A wall-trace obstruction for a proposed sine representation

Let H={(x,y): y>=0}. Suppose omega is C1 on a neighborhood of the origin in the closed half plane. Assume its tangential derivative at the origin satisfies partial_x omega(0,0)=-1. The primary source imposes this normalization on page2 and again as condition g2 on physical page8. Its exact nonzero value is immaterial for the lemma; any nonzero value suffices. The lemma concerns a hypothetical exact classical normalized profile, not an assertion that the trained network meets its penalty conditions exactly.

Claim A. No continuous odd-in-y whole-plane extension of omega exists near the origin. More precisely, if such an extension is continuous, then omega(x,0)=0 for every nearby x, and therefore partial_x omega(0,0)=0, a contradiction.

Proof. Oddness gives omega(x,0)=-omega(x,0), so the boundary trace vanishes. Differentiate the identically zero trace in x using the C1-up-to-wall hypothesis. This gives the contradictory zero tangential derivative. Alternatively the nonzero normalized derivative implies omega(x,0)=-x+o(x) (using the source's x oddness at the origin), so its trace is nonzero for sufficiently small nonzero x. This proves A.

Claim B. A sequence of smooth angular sine representations that imposes omega_N(x,0)=0 cannot converge in C1 up to the wall to that normalized profile. Indeed every trace tangential derivative is zero. Even locally uniform convergence on the closed half plane is impossible if the target trace is nonzero. This does not prohibit sine expansions in interior L2, distributional odd extensions, or a method that treats the one-sided trace separately. It prohibits identifying their pointwise zero boundary values and derivatives with the required classical wall trace.

Proof. C1 convergence preserves the tangential derivative at the origin, contradicting the normalization. Uniform convergence preserves the zero trace at each fixed boundary point, contradicting its nonzero values. These are direct properties of those convergence notions, and make no claim about interior L2 convergence. This proves B.

## Why the image inverse itself can still be legitimate

For a scalar source f smooth and compactly supported on the closed upper half plane, write its odd extension for y!=0 as f_odd(x,y)=sgn(y) f(x,|y|). Its value on y=0 is irrelevant to its distribution. If the upper trace is nonzero, this extension has a jump across the wall. It is locally integrable and defines an ordinary Poisson source distribution; it need not be a smooth whole-plane vorticity.

Let Ybar=(Y1,-Y2). With the convention -Delta psi=f, the Dirichlet image kernel on H is

    psi(X)=-1/(2pi) integral_H [log|X-Y|-log|X-Ybar|] f(Y)dY.

The two distances agree when X lies on the wall, so psi=0 there. In the open upper half plane, applying -Delta_X produces f from the first logarithm, and the reflected source lies below the wall. This also follows by splitting the full-plane logarithmic integral of f_odd into its two half planes. The formula is therefore a boundary inverse and the full-plane inverse of the nonsmooth odd source, under the ordinary compact-source normalization. It does not turn the half-plane solution into a smooth B2 source.

For U=(-psi_y,psi_x), impermeability is U2=psi_x=0 on the wall, consistent with the constant Dirichlet trace of psi. It imposes no zero trace on f=-Delta psi. A local polynomial makes the distinction explicit: psi=xy^2/2 gives U=(-xy,y^2/2), div U=0 and U2(x,0)=0, while f=-Delta psi=-x and partial_x f(0,0)=-1. This example is local, not decaying and not a Boussinesq solution. It proves only that impermeability does not imply zero vorticity trace. Its odd stream-function extension is C1 and has no distributional wall delta in its Laplacian, but its source jumps across the wall. No additional physical boundary condition may be silently imposed on f.

## Source sign conventions require separate handling in a calibration

Offline rendered inspection of physical pages1,7,8 confirms that this is a printed discrepancy, not a text-extraction artifact. The source's main text, bottom of physical page1, defines Omega=partial_y1 U2-partial_y2 U1. The displayed supplemental equation(1.1), physical page7, and residual f5 in(1.4), physical page8, appear to use Omega=partial_y2 U1-partial_y1 U2 instead. The two printed orientations are opposite. The normalization, domain, exponents, parity and reported residual comparison above do not depend on resolving this apparent print inconsistency. Any implementation must fix one convention explicitly and check its transport forcing and inversion together, rather than transcribing inconsistent signs. The B2 prompt explicitly fixes -Delta Psi=Omega with U=(-Psi_y,Psi_x), for which the usual curl partial_x U2-partial_y U1 equals -Omega. Explicitly, the main-text equations are D Omega_W+Omega_W=partial_x Theta_W and D Theta_W=(beta-2)Theta_W, where D=(beta X+U).grad. Substituting Omega_B=-Omega_W and Theta_B=-Theta_W gives D Omega_B+Omega_B=partial_x Theta_B and D Theta_B=(beta-2)Theta_B. With the same U and its stream function this has exactly the prompt's -Delta Psi=Omega_B orientation. The wall and x parity give U(0)=0 in this boundary problem, so the prompt's moving subtraction vanishes in this comparison. The local polynomial example uses f=-Delta psi; its usual curl has the opposite normalized sign, and it is not offered as the cited paper's profile. Under the main-text sign translation, its normalization partial_x Omega_W(0)=-1 becomes partial_x Omega_B(0)=+1. The wall-trace lemma needs only a nonzero derivative. The opposite printed supplementary orientation must not be silently assigned the same normalized sign. This sign observation does not resolve what the authors actually executed.

## Optional tail extension of the image formula

The preceding two-image proof is deliberately compact-source only. A literal absolutely integrated two-image kernel can diverge for f=O(r^(-alpha)),0<alpha<1, because the leading far-source term is O(1/r). For the calibration's additional x-odd parity, a four-image grouping cancels this term.

Precisely, suppose f is locally bounded on H, odd in x, and |f(Y)|<=C(1+|Y|)^(-alpha) with alpha>0. Write Q={Y1>0,Y2>0}, SxY=(-Y1,Y2), SyY=(Y1,-Y2), and

    D(X,Y)=log|X-Y|-log|X-SyY|-log|X-SxY|+log|X+Y|.

Then the grouped integral psi(X)=-1/(2pi) integral_Q D(X,Y)f(Y)dY converges absolutely for each fixed X and has an absolutely convergent velocity integral obtained by differentiating once in X. Local logarithmic and inverse-distance singularities are integrable against locally bounded f. For |Y|>2|X|, let F_Y(X)=log|X-Y|. Reflection identities express D as the double finite difference F_Y(x,y)-F_Y(x,-y)-F_Y(-x,y)+F_Y(-x,-y). Therefore

    D(X,Y)=integral_(-x)^x integral_(-y)^y partial_st F_Y(s,t) dt ds.

This oriented integral identity remains true for either sign of x or y. Since |(s,t)|<=|X| and |Y|>2|X|, the Hessian kernel is bounded by a constant/|Y|^2. Thus |D(X,Y)|<=C0 |x y|/|Y|^2. Differentiating the finite-difference integral at an endpoint, or using the first mixed derivative and one interval, gives |grad_X D|<=C1 |X|/|Y|^2. The outer radial absolute bound is a constant times integral r^(-alpha-1)dr, finite for alpha>0. This proves the claimed convergence and local uniform far-tail differentiation; the local derivative is justified by the integrable inverse-distance kernel. The distributional Poisson identity follows first for compact truncations preserving the reflection grouping, then in the limit against compact tests. The formula has zero stream-function trace on the wall and x axis, and defines a particular grouped boundary inverse with no appended homogeneous term.

For x-odd f the four-image formula is exactly the x-symmetrically grouped two-image integral: split H into Q and its x reflection, change variables on the reflected part, and use f(SxY)=-f(Y). This is an ordering statement, not absolute convergence of the ungrouped two-image integrand.

This tail extension does not prove smoothness of the odd-in-y source across the wall. Its nonzero one-sided wall trace still jumps. It does not identify the grouping used in any author's implementation, or certify a numerical profile. In particular the compact-source formula alone should not be advertised as having already fixed every slow-tail inverse convention. The four-image argument shows why a blanket claim that no image-based inverse can handle the native alpha=1/beta>0 tail would also be incorrect.

## Growth and uniqueness in the explicitly reflected class

The grouped inverse just constructed has U=o(r). Here is a proof that does not assume alpha<1. Choose any gamma with0<gamma<min(alpha,1). The source bound implies |f(Y)|<=C_gamma(1+|Y|)^(-gamma). For r=|X|>=2, split the velocity integral into |Y|>2r and |Y|<=2r. The grouped outer-kernel bound gives at most

    C r integral_(2r)^infinity s^(-gamma-1)ds <= C_gamma r^(1-gamma).

For each of the four first-derivative kernels in the inner region, split once more at |Y|=r/2. On the inner disk every distance from X to each reflected source point is at least r/2, so its contribution is at most

    C/r integral_0^(r/2) s(1+s)^(-gamma)ds <= C_gamma r^(1-gamma).

On r/2<|Y|<=2r, the source is bounded by C_gamma r^(-gamma). The inverse-distance integral over the corresponding reflected annulus is at most the integral over a radius3r disk centered at X, namely6pi r. This contribution has the same bound. Summing gives |U(X)|<=C_gamma r^(1-gamma), hence U=o(r) uniformly in direction. Since psi(0)=0 and grad psi is continuous, integrating it along the straight segment from0 to X gives psi=O(1+r^(2-gamma)), in particular psi=o(r^2).

The distributional identity established in the preceding section is -Delta psi=f_oddodd, with precisely that sign. Thus the constructed inverse belongs to the comparison class below.

If two whole-plane distributional potentials for the same odd-in-x, odd-in-y source have these parities and sublinear velocity, their difference H is an entire harmonic function. Each first derivative h=partial_i H is harmonic and o(r). For fixed X0, the standard interior gradient estimate on B_L(X0) gives |grad h(X0)|<=C L^-1 sup_(B_L(X0))|h|, which tends to0 as L tends to infinity by uniform sublinear growth. Thus both first derivatives are constant and H is affine. An affine function odd in both coordinates is zero. This proves uniqueness in the stated reflected, sublinear-velocity class. It is not a uniqueness theorem for B2's one-reflection class or for the nonlinear boundary profile equation. In particular the entire harmonic term cxy has linear velocity and is excluded by this growth condition.

## Dependencies and scope

Dependencies are the retained primary PDF/abstract page, the prompt, elementary similarity algebra, boundary traces, and the fundamental solution of the planar Laplacian. The wall claims have complete proofs above. They are conditional representation statements, not a prohibition on every use of a sine basis. No source code from another lane is executed. No formal verification or interval certification of the cited neural profile is asserted.
