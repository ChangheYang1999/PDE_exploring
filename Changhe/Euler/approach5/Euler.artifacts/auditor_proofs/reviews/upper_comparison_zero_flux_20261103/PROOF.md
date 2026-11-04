# Upper comparison removes the additive contraction drift

## 1. Exact theorem

Fix 0<c<1/2, c!=1/3 and any finite omega. Let a=1-2c, b=2(1-c), eta=a/b, Jx=e3 cross x, A=cI-omega J and X=Ax. Let smooth V,S on D=R3 minus{0} satisfy div V=0, DV X=-((1-c)I+omega J)V, X.grad S=-bS and curl V.grad S=0. Put k=X.V. Assume grad k cross grad S=0 on S!=0 and |V|^2<=r_+|S| on the unit sphere, for one finite r_+>0. Then k=0 on D. The normalized form has a global C1 primitive constant along X. Neither a lower comparison nor Poisson is required for this conclusion. No velocity-vanishing assertion is made from the upper bound alone.

## 2. Exactness without a lower bound

The explicit complete flow F_t=e^(ct)exp(-omega tJ) gives V(F_t x)=e^(-(1-c)t)exp(-omega tJ)V(x) and S(F_t x)=e^(-bt)S(x). Hence the upper comparison holds on D. Define beta=|S|^(-eta)V off S=0 and zero there. It is continuous because |beta|<=sqrt(r_+)|S|^(1/2-eta).

For beta_e=(S^2+e^2)^(-eta/2)V, its derivative is dominated by constant multiples of |V_i|^(-2eta)|D V_i| and |S|^(-eta-1/2)|DS|. These are derivatives of the signed power 1-2eta of V_i and the power 1/2-eta of |S|. Both powers are positive and less than one. The smooth-root theorem audited in the team records gives local L^t bounds for some t>1; smoothness supplies the needed finite regularity for every c in this range. On scalar zero sets the first derivatives vanish almost everywhere. The estimates therefore extend to almost every point and give beta in Wloc^(1,t), with zero weak derivative almost everywhere on S=0. Only the upper comparison is used.

The Lamb identity is X cross W=grad k+aV. Cross with grad S and use the two transport identities to obtain grad S cross grad k+a grad S cross V=bSW. Rank therefore gives grad S cross V=(b/a)SW on S!=0, and curl beta=0 there. Sobolev removal extends this to D in distributions. Local mollified primitives and simple connectivity give a global C1 function psi with grad psi=beta. There is no period assumption.

## 3. Drift, regular level and flux

Since (1-c)-b eta=c, the normalized form is invariant under pullback by F_t. Thus psi(F_t x)-psi(x) is independent of x. Continuity and the group law make it Ct for a real constant C, and X.grad psi=C.

Suppose C!=0. Then beta never vanishes, so V and S never vanish. On the unit sphere let u=psi. For pi(x)=exp((omega/c)log|x|J)x/|x|,

    psi(x)=(C/c)log|x|+u(pi(x)).

The boundedness of u shows that the zero level is compact and separates small from large radii. It is a regular C1 embedded sphere: the map n -> F_(-u(n)/C)n parametrizes it, pi is its inverse, and the transversal derivative is C. For C>0 it bounds the region psi<0; for C<0 it bounds psi>0. In either case the region contains a small punctured ball and is bounded.

Let Phi(r) be the outward velocity flux through the radius-r sphere. Divergence freedom on every annulus makes it independent of r, while scaling gives Phi(e^(ct))=e^((3c-1)t)Phi(1). Since c!=1/3, this flux is zero. Integrate divergence over the bounded region between the zero level and a sufficiently small sphere. The omitted origin lies outside this integration region, its inner flux is zero, and therefore the outer flux must vanish.

On that outer level the normal is sign(C)grad psi/|grad psi|. Because V=|S|^eta grad psi, its normal flux is sign(C)|S|^eta|grad psi|, continuous and strictly one-signed on the compact surface. Its integral is nonzero, a contradiction. Hence C=0. It follows that k=|S|^eta X.grad psi=0 off S=0, and V=0 already on S=0 gives k=0 there too.

## 4. Exact exceptions and combination with CO67

At c=1/3, V=Kx/|x|^3 and S=-K^2/|x|^4 satisfy all the other assumptions, including ratio1, rank and transport, but k=(K/3)|x|^(-1) and the sphere flux4pi K are nonzero. This validates the strict exception and is singular at the omitted origin.

For every allowed c, V=0 and S=-|x|^(-b/c) show that scalar vanishing needs more than the upper bound and the reduced equations. No nonzero-velocity example is asserted here.

CO67 is now independently confirmed at A1950-A1954. Therefore for the target range2/5<c<1/2 this theorem supplies its k=0 premise from full rank. All its conclusions now follow under the present smooth upper-comparison hypotheses: a nonzero V forces common-zero extremal boundaries with infinite local integral of R^(-tau), tau=(1/c-2)/2 and R=|V|^2/|S| on V!=0; a positive lower comparison near the entire common-zero set forces V=0; adding the specified Poisson equation gives S=0. Neither the global upper comparison nor full rank has been derived from bare decay.

## 5. Dependencies and read coverage

All four source sections and these five independent sections were read. The entire LIT264 independent proof and CO67 source/audit were read during this sequence; the root estimates and complete level-flux argument were checked again here. The original LIT268 comparison proof provides prior context, but Section3 reconstructs its argument without the lower bound. No numerical computation or formal build was used. Smoothness remains explicit; the previous natural-regularity removal used a lower bound and does not automatically apply. The unrestricted theorem remains open.
