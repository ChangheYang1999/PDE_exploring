# Besov smallness, pressure conventions and exact scaling

## 1. Statements and conventions

The physical Euler equation here is partial_t v+(v.grad)v=-grad p, div v=0 on R3 times[0,T), T>0. A pressure-unqualified solution means a smooth pair satisfying this equation with no pressure growth or normalization restriction.

Let Delta_j be the homogeneous Fourier multiplier m(2^(-j)xi), with a fixed smooth radial annular partition, and write

    N(f)=sum_(j in Z)||Delta_j f||infinity,

using Euclidean vector length. This is the specified homogeneous Besov seminorm on tempered vector distributions; polynomial representatives and any low-frequency convention remain part of the function-space definition. The inhomogeneous B1_(infinity,1) norm additionally has a low-frequency block preserving constants and weighted high-frequency blocks.

The following hold. There is a pressure-unqualified classical velocity in C([0,T);B1_(infinity,1)) with zero vorticity and no continuation in that space through T. The seminorm N is exactly invariant under simultaneous orthogonal spatial/vector rotations and dyadic spatial dilation; a valid dyadic norm can fail exact invariance under other dilations. A small N(W) rotating-profile continuation argument is valid conditional on the actual physical continuation class and its pressure estimates. Amplitude scaling gives arbitrarily small nonzero stationary compact vortices from any one such stationary solution, but does not preserve the fixed similarity equation in general.

## 2. The pressure countertest is literal and limited

Set v=e1/(T-t), p=-x1/(T-t)². Every spatial derivative of v and its curl is zero, while partial_t v=e1/(T-t)²=-grad p. Thus the PDE holds exactly. The inhomogeneous norm retains the constant low-frequency velocity and is a positive fixed multiple of (T-t)^(-1). Its dependence on t is continuous on [0,T), and its divergence at T forbids a continuous continuation through T.

In particular the usual estimate d||v||_(B1)/dt<=C||grad v||infinity||v||_(B1) fails: the right side is zero and the left side is positive. A continuation result that uses this estimate is not a theorem for every pressure-unqualified pair. A canonical-pressure or equivalent well-posedness convention excludes this affine pressure. This test does not refute that intended theorem, has no spatial decay and is not a nonzero-vorticity profile counterexample.

## 3. Dyadic dilation and rotation are exact

Let D_lambda f(x)=f(lambda x) and R_Q f(x)=Q f(Q^T x), Q in SO(3). Fourier substitution gives

    Delta_j D_(2^n)f=D_(2^n)Delta_(j-n)f, n in Z.

Taking L-infinity norms and relabeling j gives N(D_(2^n)f)=N(f), including infinite sums. Since m is radial, Delta_j commutes with R_Q. Orthogonality preserves vector length and essential suprema, hence N(R_Q f)=N(f). These are distributional multiplier identities; no integrability of f itself is required.

For tau=T-t and any orthogonal rotation Q(t), if

    omega(x,t)=tau^(-1)Q(t)W(tau^(-c)Q(t)^T x), c>0,

then tau N(omega(t))=N(W) whenever tau^(-c)=2^n. The times t_n=T-2^(-n/c) lie in any terminal interval (t0,T) for all sufficiently large n. Thus a continuation criterion using an infimum over time needs only these exact dyadic equalities. Changing a partition or the vector norm changes the smallness threshold by fixed norm-equivalence factors.

## 4. An explicit failure of arbitrary-dilation equality

Choose a smooth nonnegative radial dyadic partition with multiplier supported in 1/2<=|xi|<=2. Its radial function satisfies m(1)=1, m(1/2)=m(2)=0 and m(r)+m(r/2)=1 for 1<r<2. Continuity gives a lambda in (1,2) with m(lambda)=m(lambda/2)=1/2.

Take the real smooth bounded divergence-free vector field

    f(x)=e2 cos(x1)+e3 cos(2x1).

Only the frequency blocks j=0 and j=1 contribute at the original scale, each with L-infinity norm one. Hence N(f)=2. For D_lambda f the three contributing blocks have norms 1/2, 1/sqrt(2), 1/2. The middle value follows from Euclidean length, with both cosine magnitudes bounded by one and attaining one simultaneously at x1=0. Therefore

    N(D_lambda f)=1+1/sqrt(2)<2=N(f).

This is an exact analytic counterexample to universal nondyadic equality for this legitimate norm convention. It is not a counterexample to norm equivalence. The field is even the curl of the bounded smooth velocity (0,(1/2)sin(2x1),-sin(x1)). No numerical Fourier experiment is needed.

## 5. Conditional rotating application and stationary scaling

Assume a rotating physical solution lies in a valid B1_(infinity,1) continuation class for which sufficiently small inf_(t<T)(T-t)N(omega(t)) yields regular continuation. Section3 then supplies that smallness whenever N(W) is below its appropriate threshold. Such continuation gives bounded physical vorticity near T, while the exact ordinary supremum is tau^(-1)||W||infinity. Thus W=0. If the profile velocity is bounded and uniformly decays, curl U=div U=0 makes U harmonic and hence identically zero. This conditional argument supplies neither the physical Besov regularity nor its pressure convention from profile decay.

For the stationary test, let (u,p) be any nonzero smooth compactly supported divergence-free stationary Euler pair. Then (epsilon u,epsilon²p) is also stationary for every epsilon>0. Its vorticity supremum is epsilon||curl u||infinity. That original supremum is finite and positive: zero curl and zero divergence would make each compactly supported velocity component harmonic, hence zero. Thus no universal absolute positive vorticity threshold excludes all stationary compact vortices. The campaign's previously audited Gavrilov source supplies the existence premise; the scaling argument itself is conditional on the displayed pair.

For the fixed similarity operator L U=(1-c)U+((cI-omega J)x).grad U+omega JU, an original profile instead has scaled residual

    L(epsilon U)+(epsilon U.grad)(epsilon U)+grad(epsilon²P)
                     =epsilon(1-epsilon)L U.

It does not vanish in general. Therefore this stationary test says nothing against the fixed-c profile smallness theorem.

## 6. What the actual Chae manuscript establishes and what it does not

The primary source is Dongho Chae, arXiv:math/0604234v8, dated27April2006, with18printed pages. Its arXiv version record was checked. The actual local PDF header, introduction, definitions, Theorem1.1, Corollary1.1, Theorem1.2 and Remark1.3 were read, as were the complete proofs of Theorem1.1 and Corollary1.1 on printed pages8-9. Rendered pages5 and9 were visually inspected. The Navier-Stokes arguments and the rest of the asymptotic Euler proof are not certified by this audit.

Theorem1.1 is an existential small critical dotB0_(infinity,1) vorticity continuation result for a physical classical solution v in C([0,T);B1_(infinity,1)), using the usual well-posedness a priori estimates. Corollary1.1 applies it to an exact self-similar vorticity representation in that same class. The printed infinity,0 subscript in the corollary is inconsistent with its proof and Theorem1.1; the intended index is infinity,1. The corollary's exponent must exclude alpha=-1, and the campaign has alpha=(1-c)/c>1. The separate asymptotic Theorem1.2 explicitly adds alpha>-1, convergence in the critical Besov norm and vorticity membership in every sufficiently small positive Lq space.

The proof's denominator is 1-C2(T1-t)N(omega(t)). To make it at least1/2, choose eta<=1/(2C2). The printed eta=C2/2 needs this reciprocal repair. The positive-constant conclusion survives, but no explicit universal numerical value follows without the underlying norm constants. The derivative-order superscripts in display(2.2) also require the intended gradient/vorticity estimates, rather than a literal reading of those indices. The all-dilation norm equality is repaired by Section3's terminal dyadic sequence; Section4 shows the qualification is substantive.

Remark1.3 explicitly leaves replacement of the critical Besov norm by L-infinity as a question. Thus this source is an earlier small-vorticity precedent, not the campaign's L-infinity profile theorem. The source's pressure-unqualified notation must be interpreted with the actual local well-posedness class, as Section2 demonstrates. This audit neither refutes that canonical-pressure theorem nor certifies a statement for arbitrary affine-pressure solutions.

## 7. Dependencies and novelty boundary

The complete four-section LIT247 source and the complete five-section small-vorticity literature note were read. All elementary countertests and scaling claims are confirmed. The exact nondyadic example in Section4 is an added clarification. The actual primary source passages, not only its abstract, support the stated Besov precedent and qualifications. A statement that the campaign theorem or its constant is the first or sharp is not supported by this audit. The earlier full-gradient and all-small-Lq literature comparisons retain their separately audited hypotheses; they are not vorticity-supremum theorems.

No mathematical computation or formal build was used. Existing configured model agents receive these findings through files; runtime model identity is unattested. No new model client or agent is used. All extra Besov, pressure or smallness conditions remain explicit, and the main arbitrary-helicity bare-decay conjecture remains open.
