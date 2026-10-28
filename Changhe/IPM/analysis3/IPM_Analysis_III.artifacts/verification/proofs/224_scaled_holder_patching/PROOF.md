# Cutoff errors in the scaled global graph

## Exact statement

Fix 0<alpha<1, 2k-1<beta<k and gamma>4k. Let Z, C0, A0=T+C0 and its closed maximal domain D_Z be exactly those of proof 222. Use the graph norm ||h||D=||h||Z+||A0h||Z, equivalent to ||h||Z+||Th||Z because C0 is bounded. All functions have the physical parities and vanish on x=0. Constants in this topic are qualitative.

Let chi be a smooth compact function even in both coordinates. Suppose a regular analytic flow box Q=(x0,y0), separated from both axes and its reflections, satisfies

 V1(Q)!=0, a(Q)!=0, a=V.grad chi.

Then [T,chi] and [A0,chi] are bounded noncompact operators D_Z->Z. Their noncompactness is witnessed by a graph-bounded sequence of compact smooth inputs with c=J=0. There is also a particular origin patch

 K=chi R_delta eta:Z->D_Z

whose error A0K-chi eta is not compact Z->Z. Here R_delta is the full actual-column origin inverse from topics215/217, chi is supported in its region of exact agreement with A0, and eta is1 on its coefficient support. These choices and every operator domain are specified below.

This proves that the noncompact cutoff mechanism of proof 216 persists after the far norm is changed. It does not prove that every sum of local patches has noncompact error: cancellations between patches have not been excluded. It does not prove that A0 is non-Fredholm or noninvertible on Z. The common-Y range obstructions of topics220/221 are not asserted for Z.

## Multipliers, compact supports and the graph

A fixed smooth compact even multiplier chi is bounded on Z. Its local factor is chi times the global E2 function chi0 h in proof 222 (1), so the supported-endpoint product estimate of proof 213 applies. On the finitely many annuli meeting its support, ordinary C^alpha multiplication is bounded; on the other annuli it is zero. Its weighted L2 bound is immediate. The same argument applies to a=V.grad chi, whose needed bounded first derivatives follow from the actual compact-join and origin regularity. Its parities are even in both coordinates.

The distributional Leibniz identity implies

 T(chi h)=chi Th+a h.

Thus chi preserves D_Z and [T,chi]h=a h. Since C0 and chi are bounded on Z, the full commutator is bounded D_Z->Z as well. No density assertion about smooth inputs in the maximal domain is used.

On a fixed compact set away from x=0, ordinary C^alpha bounds imply Z bounds for supported functions. Indeed their E2 norm is bounded by a support-dependent C^alpha norm, the finite annular factors are bounded, and the weighted L2 norm is bounded by the supremum. On a compact set contained in B2, E2 bounds imply Z bounds even when the support meets the axes. The cutoff defining Z equals1 there.

## Exact transverse packets

Use the exact smooth local flow Phi_s and coordinates

 F(s,z)=Phi_s(x0,y0+z).

Since V1(Q)!=0, F is a diffeomorphism on a sufficiently small rectangle. It satisfies V.grad s=1, V.grad z=0 and F(0,z)=(x0,y0+z). For fixed compact smooth cutoffs eta1(s),theta(z), equal1 near0, set

 u_n(F(s,z))=n^(-alpha)eta1(s)theta(z)cos(nz).

Extend by zero and reflect evenly in x and oddly in y, with disjoint supports. Splitting differences at distance1/n proves uniform C^alpha bounds for u_n and Tu_n. The transport differentiates eta1, so it never differentiates the oscillation. Their suprema are O(n^(-alpha)). All supports are fixed, compact and separated from both axes. The preceding norm comparison proves uniform Z bounds and full graph membership, using boundedness of C0.

The physical strain kernel is smooth on the support. An integration by parts in z gives c[u_n]=O(n^(-alpha-1)). Choose a fixed compact smooth physical-parity q, away from the axes and the flow boxes, with c[q]=1,J(q)=0. Such q is obtained from a reflected bump where the strain kernel has fixed nonzero sign. Then

 h_n=u_n-c[u_n]q

has exact c=J=0, is bounded in the actual graph, and tends uniformly to0. Every perturbation and image belongs to the stated spaces. On the two points Q and Q_n=(x0,y0+pi/n), the correction and cutoff variations vanish for sufficiently large n, and

 h_n(Q)=n^(-alpha), h_n(Q_n)=-n^(-alpha).

If the box lies inside B2, the local E2 component gives

 liminf ||a h_n||Z >=2|a(Q)|/(x0^2 pi^alpha)>0.

For a general fixed box choose an overlapping annulus containing these points; its ordinary C^alpha seminorm instead supplies a positive fixed lower bound. A convergent Z subsequence would converge locally uniformly to0, whereas this lower bound prevents convergence to0. Thus multiplication by a is noncompact.

## The complete nonlocal commutator tends to zero on these packets

Let K be the fixed compact support of h_n, including q, separated from x=0 and the origin. For all compact physical-parity h supported there,

 ||[C0,chi]h||Z<=C_K||h||infinity.                 (1)

To prove this without a weighted Riesz theorem, write W=U[chi h]-chi U[h]. The local multiplier term cancels. The canonical subtraction constants vanish by parity for both compact inputs. The kernel of W is

 (chi(Y)-chi(X))K_i(X-Y).

On bounded sets its size is O(|X-Y|^(-1)). For an output difference d, the disks of radius2d contribute O(||h||infinity d), and their complement contributes O(||h||infinity d(1+|log d|)) by the kernel derivative bound O(|X-Y|^(-2)). This is O_alpha(||h||infinity d^alpha). Thus W has a bounded ordinary C^alpha norm controlled by ||h||infinity, with no derivatives of h used.

On a fixed strip about x=0, the source set K is separated from the output. Every fixed derivative of W is bounded by C_K||h||infinity. Parity gives W1(0,y)=0, so W1/x and its first y derivative are bounded there. The actual coefficients a1=rho0_x/x and a2=rho0_y/x^2 and their first y derivatives are globally bounded by the exact origin, join and far formulas. Consequently

 (W.grad rho0)/x^2=a1(W1/x)+a2 W2

has the required vertical Holder bound in the strip. Outside it division by x^2 is harmless and the ordinary C^alpha bound supplies that estimate. Horizontal differences follow from the same bound and the bounded Lipschitz gradient of rho0. This proves the E2 bound C_K||h||infinity, hence its local component in Z.

At sufficiently large output radius, chi(X)=0 and W=U[chi h]. The compact odd-y input has zero mass, so |D^j W|<=C_K||h||infinity r^(-3-j), for j=0,1. Hence the coupling and its scaled Holder norm have far order r^(k-4). Its annular factor is bounded because k-4-beta<0. Its weighted square integral is bounded because gamma>4k>2k-6. This proves the entire far and weighted components of (1), for all gamma>4k, without the former restriction gamma<2.

Finally the rank-one part is

 c[chi h]M0-chi c[h]M0.

The two scalars are bounded by C_K||h||infinity, since their physical-origin kernels are smooth on K. The columns M0 and chi M0 belong to Z by strict beta>2k-1. This proves (1). In particular [C0,chi]h_n tends to0 in Z. It cannot cancel the transport lower bound, and [A0,chi] is noncompact on the displayed graph-bounded sequence.

## A particular full-column origin patch

Choose delta sufficiently small for the inverse in proof 217, with the coefficient cutoff supported in B_delta and equal1 on B_(delta/2). Denote that exact full extension by L_delta and its inverse on E2 by R_delta. Choose chi supported in B_(delta/2), and eta smooth radial, equal1 on B_delta and supported in a slightly larger disk contained in B2. The full expressions L_delta and A0 agree on supp chi for every E2 input, including the canonical velocity and exact M0 column.

There exists a transition flow box of chi with the properties above. Near0, V=(-A x,D y)+O(r^3), with A>0,D>0. On a radial transition take x nonzero and y nonzero sufficiently smaller than x, so V1 and V.grad chi do not vanish. Avoid a radial join by a small change of radius. Put the correction q inside B_(delta/2), away from the four boxes and axes.

The map eta:Z->E2 is bounded because its support lies where the local E2 factor controls h. R_delta eta maps into its exact maximal E2 transport domain. For u=R_delta eta f, the identity V_delta.grad u=u+eta f-B_delta u belongs to E2 with a bounded norm. Multiplying by chi, using equality of the transports there, and differentiating chi shows T(chi u) is compactly supported with bounded E2 norm. Thus Kf=chi u belongs to D_Z, with a bounded graph norm. C0 supplies its complete global image.

For the packets above set f_n=L_delta h_n. Their transport terms are supported in B_(delta/2), and their extended coupling is supported in B_delta. They have bounded E2 norms and hence bounded Z norms, with eta f_n=f_n. Exact maximal-domain inversion gives R_delta eta f_n=h_n. Therefore

 (A0K-chi eta)f_n=A0(chi h_n)-chi L_delta h_n
                    =[A0,chi]h_n.

The right side has no convergent subsequence. This proves the claimed noncompactness of this specific patch error.

## What would close a global construction

If a bounded graph-valued K:Z->D_Z is constructed and the actual complete error E=A0K-I has ||E||Z->Z<1, then K(I+E)^(-1) is a bounded right inverse. This proves surjectivity. Injectivity must still be proved, for example by an independent lower estimate ||h||Z<=C||A0h||Z on D_Z. A right inverse alone does not prove injectivity.

Alternatively, both a left and a right parametrix modulo compact operators would give a Fredholm problem, followed by a separate kernel, cokernel and index analysis. Noncompactness of one cutoff component does not exclude compactness of the assembled error after exact cancellations. It does refute obtaining that conclusion from local inverses and individual cutoff compactness without further proof.

Proof 223 supplies an exterior inverse with a small parameter at infinity. Topics215/217 supply an origin inverse with a small parameter at0, and topics208-210 supply actual source inverses. None of these results bounds the middle-annulus assembled error, provides both-sided parametrices, or gives global injectivity on Z. The independent Sobolev condition(I) is on a different realization and cannot be transferred without norm/domain comparison. Closed physical cubic normalization and nonlinear closure remain separate issues.

Dependencies: topics213-217 for compact norm comparisons, actual origin extension and local kernel formulas; proof 222 for the exact global scaled realization; proof 223 for the exterior scope. Every new global-tail, graph, packet and noncompactness statement is proved above. No computation or global inverse claim is made.
