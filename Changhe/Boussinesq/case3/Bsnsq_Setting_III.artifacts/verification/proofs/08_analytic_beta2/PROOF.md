# The beta=2 branch cannot have globally real-analytic velocity

Status: complete informal argument by the independent verifier, confirmed by the Opus 5.5 lead on 2026-10-20 at 13:49 UTC. Restricted theorem only. Global real analyticity is stronger than the smoothness required by the prompt.

## Statement

Suppose beta=2, U is real analytic on R^2, div U=0, and U(X)=o(|X|) uniformly at infinity. Put W=2X+U-U(0). Suppose Theta is C^3, even in x, vanishes on x=0, has expansion Theta=a0 x^2+O(|X|^3) with a0!=0, and solves W.grad Theta=0. Suppose also the B2 parity and center relation give DW(0)=diag(0,4).

Then such W and Theta do not exist. In particular no full B2 profile at beta=2 with real-analytic U exists. Analyticity of Theta is not required in this statement.

## 1. A local arc of zeros

Since partial_y W_2(0)=4, the implicit function theorem gives a curve y=h(x), h(0)=h'(0)=0, on which W_2=0. Smooth even-x divisibility gives Theta=x^2 F(x,y), with F(0)=a0 and enough differentiability that

    Theta_x(x,h(x))=2a0 x+o(x).

It is nonzero for small nonzero x. Evaluating W.grad Theta=0 on the curve therefore gives W_1=0 there. The origin also is a zero. Thus the zero set Z={W=0} contains a nontrivial arc. This is the local result in `../02_beta2_curve/PROOF.md`, proved using the implicit function theorem rather than a choice of center manifold.

## 2. The zero set is compact

At large radius, W(X).X=2|X|^2+o(|X|^2)>0. Hence all zeros lie in a fixed ball. The set Z is closed, so it is compact. Everywhere, div W=4.

Let Z' denote the set of accumulation points of Z. It is closed, compact and nonempty, because of the local arc. We show that Z' is a real-analytic embedded one-dimensional manifold without boundary.

## 3. Local structure at an accumulation zero

Fix p in Z'. Since Z is closed, W(p)=0. The derivative DW(p) cannot be invertible: the inverse function theorem would make p the only zero nearby. It cannot have rank zero either, because its trace is div W(p)=4. Thus its rank is exactly one.

Some component of W has a nonzero derivative in some coordinate. The analytic implicit function theorem expresses the zero set of that component, near p, as one analytic graph, parametrized by a scalar s. Restrict the other component of W to this graph. It is a real-analytic function f(s). Z has distinct zeros tending to p, so f has zeros accumulating at the parameter of p. The one-dimensional analytic identity theorem gives f=0 on an interval about that parameter.

Consequently, in a sufficiently small neighborhood of p, the entire set Z is exactly this analytic graph. Every point of the graph is an accumulation zero, so locally Z'=Z and is a regular curve with no endpoint or branch. This proves the asserted manifold structure. The argument applies at every point of Z'; it makes no assumption that a selected local curve can simply be continued indefinitely.

## 4. A compact zero curve contradicts the divergence

A nonempty compact one-dimensional manifold without boundary has a connected component diffeomorphic to a circle. Since Z' is embedded in R^2, this component is a regular simple closed curve Gamma. Let D be its bounded Jordan interior. Along Gamma, W=0. The divergence theorem gives

    4 area(D) = integral_D div W = integral_Gamma W.n d ell = 0.

The interior of a simple closed regular curve is nonempty and open, so its area is positive. This contradiction proves the theorem.

## Why the result is restricted

For a C^infinity function, zeros on one side of a point do not imply zeros on the other side. A function may vanish to infinite order at an endpoint and then become nonzero. Step 3 therefore does not follow from C^infinity regularity. Neither the transport equations nor the elliptic inverse has been shown here to force real analyticity of an arbitrary smooth profile. There is no full beta=2 exclusion.

The proof also gives the following general lemma: a real-analytic planar vector field with constant nonzero divergence and a compact zero set has only isolated zeros. The B2 temperature jet at beta=2 supplies the contradiction to this lemma.

Dependencies: C^1 and analytic implicit/inverse function theorems, the one-dimensional analytic identity theorem, the classification of compact one-dimensional manifolds, the Jordan curve theorem, and the divergence theorem. These are used in precisely the forms spelled out above. No numerical evidence is used as proof.

## A stronger smooth consequence: an infinitely flat temperature jet is necessary

There is a second exclusion that does not assume analytic U. Let U and Theta be C^infinity with the same beta=2 hypotheses, including sublinear U and the nonzero quadratic temperature jet at the origin. Then there exists an accumulation zero p of W at which every positive-order derivative of Theta vanishes:

    partial^nu Theta(p)=0 for every multi-index nu with |nu|>=1.

The value Theta(p) itself need not be zero. This is a necessary flat jet, not a contradiction in the smooth class. In particular, globally real-analytic, nonconstant Theta is impossible even when U is only smooth.

Proof. Retain the compact zero set Z, its nonempty compact derived set Z', and div W=4 from Steps 1-2. At any p in Z', the same inverse-function and trace argument gives rank DW(p)=1, with distinct eigenvalues 0 and 4. Apply an invertible linear change of coordinates centered at p to diagonalize this matrix. In these coordinates (s,n), W=(0,4n)+O(|(s,n)|^2).

Suppose Theta has a finite first nonconstant Taylor order m>=1 at p. Write

    Theta(s,n)=Theta(p)+P_m(s,n)+O(|(s,n)|^(m+1)),

where P_m is a nonzero homogeneous polynomial of degree m. The lowest-order part of W.grad Theta=0 is

    4 n partial_n P_m=0.

Hence P_m=c s^m for a nonzero c. The implicit function theorem applied to W_n=0 supplies a graph n=h(s), with h(0)=h'(0)=0. On it,

    partial_s Theta(s,h(s))=m c s^(m-1)+O(|s|^m),

which is nonzero for sufficiently small nonzero s. The transport equation on this graph forces W_s=0. Therefore the whole graph consists of zeros of W, and all zeros near p lie on it. As before, Z' is locally a regular curve without endpoints.

If every point of Z' had such a finite Taylor order, Z' would be a nonempty compact embedded one-manifold without boundary. Its circle component contradicts the divergence theorem exactly as in Step 4. Some p in Z' therefore has no first nonconstant finite Taylor order, proving the flat-jet assertion.

If Theta is real analytic and nonconstant on the connected plane, it cannot have an infinitely flat nonconstant jet at any point: its local Taylor series would make it locally constant, and analytic continuation would make it constant everywhere. Its prescribed quadratic jet already rules out a constant. This proves the analytic-temperature exclusion.

This argument is also a useful regularity diagnostic: a beta=2 smooth candidate must exhibit a temperature that becomes infinitely flat at some accumulation point of its stagnation set. No finite list of nearly vanishing derivatives demonstrates that property numerically. Conversely, a sequence of analytic approximations can approach a nonanalytic smooth limit, so finite-dimensional failure or analyticity of approximants does not exclude such a limit.

## The vorticity jet is also flat at this point

Assume now the full smooth B2 equations, including W.grad Omega+Omega=Theta_x. At the accumulation zero p furnished above, every derivative of Theta of positive order vanishes. Then every derivative of Omega, including its value, vanishes at p.

First Omega(p)=Theta_x(p)=0 because W(p)=0. Inductively suppose all derivatives of Omega of order less than m vanish, and let Q_m be its homogeneous Taylor term of order m in coordinates diagonalizing DW(p). If Q_m were nonzero, the degree-m part of the vorticity equation would be

    (4 n partial_n + 1) Q_m = 0.

All higher-order terms of W act only at higher degree because the lower Omega jets vanish. The right side Theta_x has zero Taylor series; this remains true after an invertible linear coordinate change since the original x derivative becomes a fixed linear combination of coordinate derivatives. On each monomial s^(m-j)n^j the displayed operator multiplies by 1+4j, which never vanishes. Thus Q_m=0, completing induction.

Consequently curl W=-Omega is flat at p, and -Delta Psi=Omega has flat right side there. This does not imply analyticity of Psi or local vanishing of Omega: a smooth flat function can be nonzero in every neighborhood. No unique-continuation theorem is claimed. This extension independently verifies the lead's 13:49 UTC proposal.
