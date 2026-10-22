# A nonzero thermal jet forces a compatibility obstruction

Status: complete informal proof, written before implementation. Independent exact controls passed; written actual claude-opus-5-5 review193 CONFIRMED the stronger beta>2 extension under hypotheses already present and repeated below. Calls191/192 returned no written audit and are not counted as endorsements. This is a criterion for a prescribed stream, not a nonexistence theorem for B2.

## Exact statement and notation

Let beta>0, k=beta-2, c=1+beta/2 and lambda2=beta+c=1+3beta/2. Let Psi be smooth near0, odd in x, with Psi_xy(0)=c. Put Omega=-DeltaPsi, W=beta X+gradperpPsi-gradperpPsi(0), F=W.gradOmega+Omega, and define the normalized horizontal primitive Theta(x,y)=int_0^x F(u,y)du in a rectangle about0. Let t=W.gradTheta-kTheta, and let E be the compatibility polynomial of124/137. Assume

    j1=Psi_xxx(0) !=0.                                 (1)

Write a homogeneous Taylor polynomial in ordinary monomial coefficients, with no factorials. If the first nonzero homogeneous part of t has degree N and is

    t_N=sum_(a+b=N) t_ab x^a y^b,

then t_N is even in x and every nonzero term has a>=2. The first nonzero homogeneous part of E has the SAME degree N and is

    E_N=-j1 sum_(a+b=N) a[lambda2(b+1)-k] t_ab x^a y^b.  (2)

Every diagonal factor in(2) is nonzero. Consequently t is flat at0 if and only if E is flat at0.

If Psi is real analytic near0, E vanishes identically near0 if and only if the normalized primitive satisfies the exact thermal equation there. The vorticity equation already holds by the primitive definition. If Psi is real analytic on the connected plane and its E has one nonzero Taylor coefficient at0, then there is NO nonempty open subset admitting any C2 temperature satisfying both transport equations for this prescribed W,Omega, even without parity or axis normalization on that alternative temperature. This last assertion is an obstruction for this fixed stream, not for streams in a neighborhood or the broad class.

Conversely, for a real analytic whole-plane Psi satisfying(1), E identically0 implies that the normalized whole-plane primitive solves both transport equations everywhere. Elliptic inversion, admissible growth, nontrivial center vorticity and the prescribed temperature jet must still be checked separately before calling such fields B2 profiles. These conditions are not inferred merely from E=0.

## Proof of the leading term

Parity and center subtraction give W(0)=0, W1=(beta-c)x+O(|X|²) and W2=lambda2 y+O(|X|²). Also

    J=partial_x W2=Psi_xx=j1 x+O(|X|²),
    partial_y J=O(|X|), partial_y W2=lambda2+O(|X|).

There is no y term in J because J is odd in x. The source F is odd in x, so Theta is even in x, vanishes on x=0, and is divisible by x² as a smooth function. Thus t also has that property, using W1 odd in x. In particular any first nonzero Taylor monomial of t has even a>=2.

By exact differentiation of the horizontal integral, f=F-Theta_x=0. Identity137, which uses only smooth local fields, therefore gives

    E=J² t_y-J W2 t_xy+[W2 J_y+J(k-W2_y)]t_x.          (3)

If t starts at degree N, J²t_y and W2J_y t_x start at degree N+1. In the two remaining terms all higher parts of J,W2,W2_y likewise contribute only degrees above N. The part of degree N is exactly

    -j1 lambda2 x y partial_xy t_N+j1(k-lambda2)x partial_x t_N,

which is(2). For b>=0,

    lambda2(b+1)-k >= lambda2-k = 3+beta/2 >0.

Together with j1!=0 and a>=2 this proves the nonzero diagonal factors. Multiplication and differentiation preserve flatness, so(3) proves that flat t gives flat E. If t is not flat, its first nonzero finite Taylor degree and(2) show E not flat, proving the reverse implication.

## Analytic implications and scope

For analytic Psi, the finite horizontal primitive of analytic F is analytic locally; this also follows by integrating its convergent power series on a smaller rectangle. Analyticity and equality of every Taylor coefficient imply equality on a neighborhood. Hence E identically0 near0 implies t flat, then t identically0 near0. Conversely t=0 gives E=0 by(3).

For a globally real analytic Psi, W,Omega and E are analytic on all of R². If E has a nonzero coefficient at0, it cannot vanish on any nonempty open set by the identity theorem on the connected plane. Any C2 temperature satisfying both equations would make E vanish there by124's no-division necessary identity, contradiction. That alternative temperature need not be the normalized primitive. This inference relies on analyticity of the prescribed W and Omega, not on analytic regularity of the temperature.

If E identically0 globally, the local result gives t=0 near0. The normalized primitive is real analytic on the plane (analytic parameter integration on each finite segment), so its t is analytic, and the identity theorem gives t=0 everywhere. The vorticity equation is exact by definition. This is an analytic reformulation only. If j1=0, the degree-preserving argument is unavailable, and the general J identically0 counterexample of137 rules out any unconditional sufficiency claim. If Psi is merely smooth, equivalence of flatness does not assert local vanishing; flat defects remain possible.

Dependencies: elementary Taylor algebra; the explicitly verified identity137; the local necessary condition and analytic identity principle of124. No numerical observation is used in the proof. All coefficient data and tests are separate verification artifacts.

Written UTC: 2026-10-21T06:57:33.671983+00:00.

## Extension for beta>2 without the first-derivative condition

This extension was written UTC:2026-10-21T07:00:59.210597+00:00, before its independent controls.

Assume beta>2 and retain all definitions above. Explicitly W2=beta y+Psi_x(x,y)-Psi_x(0), so W2(0)=0 and W2_y(0)=lambda2. The smooth function t vanishes to second order in x along x=0; this follows from the normalized odd-source primitive and parity, as proved above. Replace(1) by the weaker hypothesis that J=Psi_xx is not flat at0. Let J_d be its first nonzero homogeneous Taylor polynomial, of degree d>=1. If t_N is the first nonzero homogeneous term of t, then the first nonzero term of E has degree N+d-1 and equals

 P=-lambda2 y J_d partial_y H
           +[lambda2 y partial_y J_d+(k-lambda2)J_d]H,
 H=partial_x t_N.                                      (4)

In particular P cannot vanish. Thus all the flatness and analytic conclusions above hold for beta>2 whenever J is not flat, even when j1=0.

To prove the degree assertion, use(3). The J²t_y term starts at degree2d+N-1, strictly greater than d+N-1. Taking the leading J_d and W2=lambda2 y in the other terms gives exactly(4), and every omitted jet term has higher degree. It remains to prove P nonzero, since its displayed expression could a priori cancel.

The polynomial H is nonzero because every monomial of t_N has x exponent at least2. Write J_d=y^s A(x,y), H=y^b B(x,y), where s,b are nonnegative integers, and A(x,0),B(x,0) are nonzero polynomials. The coefficient of the lowest power y^(s+b) in P is

    [lambda2(s-b-1)+k] A(x,0)B(x,0).                  (5)

The real polynomial ring has no zero divisors. Also0<k/lambda2<2/3 for beta>2, so s-b-1+k/lambda2 cannot be0 because the first three terms have an integer value. Hence(5) is nonzero. This proves both noncancellation and the exact first degree. The flatness equivalence follows as before. The extension does not apply at beta2: k/lambda2=0 is an integer and the lowest-y-power argument can have a kernel.

For a real analytic whole-plane stream in the target sublinear-velocity class, J cannot be identically0. Indeed Psi_xx=0 and oddness imply Psi=x h(y). Then U1=-x h'(y); along x tending to infinity with y fixed, sublinear velocity forces h'(y)=0 for each y. This contradicts Psi_xy(0)=1+beta/2>0. Analyticity on the connected plane therefore makes J nonflat at0. Consequently for beta>2 an admissible real analytic prescribed stream with the required center strain satisfies E identically0 if and only if its normalized primitive satisfies both stationary transport equations; all other profile conditions and growth/nontriviality of the primitive still require their own verification. The equivalence does not provide a solution or rule out analytic profiles. A smooth field with flat J is not covered.

Review193 interface clarification UTC:2026-10-21T07:03:07.824326+00:00. Connectedness is stated separately at every global analytic step; no local analytic assumption is used to conclude global nonflatness without it.
