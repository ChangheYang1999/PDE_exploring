# Non-profiles satisfying three scalar identities and outward dynamics

Status: CONFIRMED by an independent complete argument, 2026-10-20.
This reconstructs SGN2-C from the frozen source in
`../../evidence/sgn2_audit/`. Verification files check algebraic ingredients;
the existence of the constructed parameters follows by the argument below,
not by an asserted numerical root.

## Exact statement

Fix \(s<0\) or \(s\ge1/2\). There is \(D_s>0\) such that for each
\(0<D<D_s\), with \(\ell=1+D\), \(p=1/\ell\), and \(a=D/s\), there
is a sequence of smooth functions \(\rho_n\) with canonical velocities
\(U_n=(-\psi_{n,y},\psi_{n,x})\), \(-\Delta\psi_n=\rho_{n,x}\), such that:

1. \(\rho_n\) is even in \(x\), odd in \(y\), has
   \(\rho_{n,y}(0)=a\ne0\), and \(\psi_{n,xy}(0)=-D\).
2. The quotient \(\rho_n/(ay)\) is positive and comparable to
   \((1+r)^{p-1}\), and all fields have symbol bounds of their natural
   orders. Constants for higher derivatives may depend on \(n\).
3. For \(W_n=\ell X+U_n\),
   \(DW_n(0)=\operatorname{diag}(2\ell-1,1)\) and
   \(X\cdot W_n(X)\ge r^2/2\). Thus the origin is its unique equilibrium.
4. The canonical strain identity, the scalar divergence identity below,
   and the cubic weighted transport identity below all hold exactly.
5. All \(\rho_n\) have the same leading density trace
   \(\Theta_0(\theta)=a\sin\theta\). Nevertheless
   \(\|\nabla\rho_n\|_\infty\to\infty\) and
   \(\|DU_n\|_\infty\to\infty\).

These are NOT profiles. They fail the necessary second far-field transport
coefficient. Hence no bound depending only on these fixed scalar data,
leading trace and outward lower bound can bound both gradients on the
larger class satisfying items 1--4. This does not contradict a bound that
uses the full transport PDE or further local and global consequences of it.

## Notation and the three scalar constraints

Set
\[
 \phi(X)=r^{-3}\sin3\theta=\frac{3x^2y-y^3}{r^6},
 \quad Q=\{x>0,y>0\}.
\]
For \(v=yq\), with smooth even-even \(q\), \(q(0)=1\), and the stated
decay, let \(V[v]\) denote its canonical velocity. Define
\[
 J(v)=\frac1\pi\lim_{\epsilon\downarrow0,\ R\uparrow\infty}
                  \int_{\epsilon<r<R}v\phi\,dX,
 \quad S(v)=\frac14-J(v),
 \quad B(v)=\lim_{\epsilon\downarrow0,\ R\uparrow\infty}
                  \int_{\epsilon<r<R}v V[v]\cdot\nabla\phi\,dX. \tag{1}
\]
The circular truncations are part of these definitions. At the origin,
\(v=y+O(r^3)\), \(V=(hx,-hy)+O(r^3)\), and
\[
 y\phi=r^{-2}\sin\theta\sin3\theta,
 \qquad y(hx,-hy)\cdot\nabla\phi
       =-3h r^{-2}\sin\theta\sin5\theta.             \tag{2}
\]
Both leading angular means vanish. The remainders are locally integrable.
At infinity the integrals converge since \(p<1\). In particular the
second integral has radial size at most \(r^{2p-3}dr\).

The canonical strain formula is
\(\psi_{v,xy}(0)=-S(v)\). Equivalently, if
\[
 S=-\frac4\pi\int_Q\frac{xy^2}{r^4}q_x\,dX,
 \qquad T=-\frac4\pi\int_Q\frac{y^3}{r^4}q_y\,dX,
\]
then \(S+T=1\): their sum is
\(-4\pi^{-1}\int\sin^2\theta\int q_r\,dr\,d\theta=1\).
This identity holds for every such \(q\), independently of transport.
For \(\rho=av\), fixing \(S(v)=s=D/a\) fixes the strain \(-D\).
The cubic weighted identity required by exact transport is
\[
 -D\int\rho\phi\,dX+\int\rho U\cdot\nabla\phi\,dX
                  =-\frac{\pi aD}{2}.              \tag{3}
\]
Since \(J=1/4-s\), substituting \(\rho=av\), \(D=as\) into (3)
gives precisely
\[
 B(v)=-\pi s(s+1/4)=:C_s.                           \tag{4}
\]
Thus it suffices to construct positive quotients with \(S=s\), \(B=C_s\).

## A radial reference and concentrated perturbations

We use the compact parameter range \(1/2\le p<1\). Put
\[
 F_p(r)=(1+r^2)^{(p-1)/2},\quad v_p=yF_p(r),\quad
 h_p(r)=\int_0^1t^3F_p(rt)\,dt.
\]
Direct differentiation shows that \(\psi_p=-xyh_p(r)\) is the smooth
canonical stream for \(v_p\). Consequently \(S(v_p)=1/4\),
\(h_p(0)=1/4\), \(h_p(\infty)=0\), and \(h'_p\le0\).
The elementary bounds on \(F_p,rF'_p,r^2F''_p\), uniform in this
parameter range, bound \(\|DV[v_p]\|_\infty\) by one finite constant
\(M_0\). Polar integration gives
\[
 B(v_p)=\frac{3\pi}{4}\int_0^\infty F_p(r)h'_p(r)\,dr
                 \in[-3\pi/16,0].                 \tag{5}
\]
Only finiteness and uniformity of these bounds are needed below.

Choose a smooth radial nonnegative bump \(\eta\) supported in the unit
disk, with integral one, and write
\(\eta_\delta(X)=\delta^{-2}\eta(X/\delta)\).
For a unit vector \(z=(\cos\theta,\sin\theta)\) in the first quadrant,
choose \(\delta\) small enough that its four reflected disks are disjoint
and avoid the axes. Set
\[
 g_{z,\delta}(X)=\sum_{\sigma,\tau\in\{\pm1\}}
        \tau\eta_\delta(X-(\sigma z_x,\tau z_y)).     \tag{6}
\]
This has density parity and is nonnegative in the upper half-plane.
Smoothness of \(\phi\) on the disks gives
\[
 J(g_{z,\delta})\longrightarrow\frac4\pi\phi(z).
\]
In fact radial harmonic averaging gives equality, since \(\phi\) is
harmonic on each disk; the limit alone suffices. At angles with the same
sign of \(\phi(z)\) as \(1/4-s\), the coefficient
\[
 \beta_{z,\delta}=\frac{1/4-s}{J(g_{z,\delta})}>0     \tag{7}
\]
is bounded above and away from zero as \(\delta\downarrow0\).
Then \(S(v_p+\beta g)=s\) exactly. The quotient remains positive;
its origin germ and its tail equal those of the radial reference.

We compute the divergent part of \(B\). For a radial bump, Plancherel
and the canonical multipliers give
\[
 \int\eta V_1[\eta]=0,\qquad
 \int\eta V_2[\eta]=-	frac12\|\eta\|_2^2.           \tag{8}
\]
The first multiplier is angularly odd. The second is
\(-\xi_x^2/|\xi|^2\); its angular average is \(-1/2\).
Translation and scaling of a single bump show its self contribution to
\(B(\beta g)\) is
\(-\beta^2\delta^{-2}\|\eta\|_2^2\phi_y(z)/2+O(\delta^{-1})\).
The error follows by replacing \(\nabla\phi\) on the bump disk with
its center value: the error in that gradient is \(O(\delta)\), while
Cauchy--Schwarz and the \(L^2\) multiplier bound give an
\(O(\delta^{-2})\) product integral. Reflections have identical
\(\phi_y\) and the bump signs are squared, so all four self terms sum to
\[
 -2\beta^2\delta^{-2}\|\eta\|_2^2\phi_y(z)
                                      +O(\delta^{-1}).         \tag{9}
\]
Distinct disks contribute \(O(1)\) because the kernel is smooth between
them and their masses stay bounded.

The cross terms with \(v_p\) are \(O(\delta^{-1})\), uniformly in \(p\).
On a fixed neighborhood of the disks, use
\(\|V[g]\|_2\le\|g\|_2=O(\delta^{-1})\) and the uniformly bounded
\(L^2\) function \(v_p\nabla\phi\). The term with density \(g\) and
velocity \(V[v_p]\) is bounded by its \(L^1\) mass and uniform local
bounds. Near zero, \(V[g]=(hx,-hy)+O(r^3)\) with Taylor constants
uniform in \(\delta\), since the bumps stay a fixed distance away;
(2) cancels the only singular circular mean. At infinity,
\(v_p\nabla\phi\) is uniformly square integrable away from zero,
and the same \(L^2\) estimate applies. This proves (9), including all
cross terms needed for \(B(v_p+\beta g)\).

Now \(\phi_y(z)=3\cos4\theta\) on the unit circle. For \(s<0\), take
\(\theta_-=\pi/12\), \(\theta_+=\pi/4\). Both have \(\phi>0\),
and their \(\phi_y\) signs are respectively positive and negative.
For \(s\ge1/2\), take
\(\theta_-=5\pi/12\), \(\theta_+=17\pi/48\). Both have \(\phi<0\),
with the same respective signs of \(\phi_y\).
It follows that, for sufficiently small fixed \(\delta>0\),
\[
 B(v_p+\beta_-g_-)<C_s<B(v_p+\beta_+g_+)             \tag{10}
\]
uniformly for \(1/2\le p<1\), with a positive uniform margin.
Choose such a \(\delta\) once and for all.

## Fixing the outward lower bound and the scalar root

For \(0\le t\le1\), define
\[
 v_{p,t}=v_p+(1-t)\beta_-g_-+t\beta_+g_+.
\]
The quotient is positive, \(S=s\) along this path, and \(B(v_{p,t})\)
is a continuous quadratic function of \(t\). The intermediate value
theorem and (10) give at least one \(t\) for which (4) holds.

There is a finite constant \(M\), independent of \(p,t\), bounding
\(\|DV[v_{p,t}]\|_\infty\). The reference has the uniform bound already
proved. Each added density is fixed and smooth with compact support; its
canonical velocity has bounded derivatives by local cancellation and the
decaying kernel outside a compact set. This also follows from the bounded
Fourier multipliers applied to its rapidly decaying Fourier transform.
Choose
\[
 0<D<D_s:=\min\{1,|s|/(4M)\}.
\]
Then \(p=(1+D)^{-1}\in(1/2,1)\), \(|a|M<1/4\), and
\(U=aV[v_{p,t}]\) obeys \(\|DU\|_\infty<1/4\).
Since parity gives \(U(0)=0\),
\[
 X\cdot(\ell X+U)\ge(\ell-1/4)r^2\ge3r^2/4.       \tag{11}
\]
At the origin the fixed value \(S=s\) gives
\(DU(0)=\operatorname{diag}(D,-D)\), hence the stated source matrix.

## Compact potential oscillations with a scalar correction

Choose a fixed smooth cutoff \(\chi\), even in \(x\) and odd in \(y\),
supported on four reflected rectangles away from zero, the axes, and
both bump families. Let it equal one on a smaller first-quadrant rectangle.
For positive integers \(n\), put
\[
 f_n=\epsilon n^{-2}\chi(X)\cos(nx),\quad
 d_n=-\Delta f_n,\quad Z_n=(-f_{n,xy},f_{n,xx}).      \tag{12}
\]
The compact stream \(\partial_x f_n\) solves
\(-\Delta\partial_x f_n=\partial_xd_n\), so \(Z_n=V[d_n]\)
exactly in the canonical gauge. Since \(\Delta\phi=0\) on the support,
integration by parts gives \(J(d_n)=0\). Both \(d_n\) and \(Z_n\)
vanish on a neighborhood of the origin, so even the velocity germ is
unchanged. Product differentiation gives uniform bounds
\[
 \|d_n\|_\infty+\|Z_n\|_\infty\le C\epsilon.         \tag{13}
\]
On their fixed support the positive reference quotient is bounded below
uniformly in \(p,t\); the added bumps are nonnegative in \(y>0\).
Thus sufficiently small \(\epsilon>0\) preserves the density sign for
all \(n,t\). It also preserves (10), since
\[
 B(v_{p,t}+d_n)-B(v_{p,t})
 =\int(d_nV[v_{p,t}]+v_{p,t}Z_n+d_nZ_n)\cdot\nabla\phi
\]
is bounded by \(C'(\epsilon+\epsilon^2)\) uniformly in \(n,t,p\).
All terms here have compact support away from zero, so no singular
integration is being estimated by an absolute bound. For each \(n\),
a new intermediate value argument gives \(t_n\in[0,1]\) with
\(B(v_{p,t_n}+d_n)=C_s\), while \(S=s\) remains exact.

Let \(r_*>0\) be the least radius on the oscillation support. By further
decreasing \(\epsilon\), enforce \(|a|C\epsilon\le r_*/4\).
Equation (11) and (13) then give the lower bound \(r^2/2\) for the
perturbed \(X\cdot W\). Set \(\rho_n=a(v_{p,t_n}+d_n)\).
On the smaller rectangle where \(\chi=1\),
\[
 d_n=\epsilon\cos(nx),\qquad Z_n=(0,-\epsilon\cos(nx)).
\]
The derivatives of the backgrounds are bounded uniformly in \(n\)
since \(t_n\in[0,1]\). Every sufficiently large \(n\) has points in
this rectangle with \(|\sin(nx)|=1\). Hence
\(\|\rho_{n,x}\|_\infty\ge|a|\epsilon n-C_1\) and
\(\|\partial_xU_{n,2}\|_\infty\ge|a|\epsilon n-C_2\).
This proves the asserted divergence of both gradient norms.
All higher symbol bounds hold individually: the perturbations are smooth
and compactly supported. The constants need not be uniform in \(n\).

## Why the constructed fields fail transport

Outside a compact set their density equals
\[
 \rho_n=ay(1+r^2)^{(p-1)/2}
       =ar^p\sin\theta+O(r^{p-2}).                  \tag{14}
\]
Thus their coefficient at degree \(2p-1\) is zero. Their leading
canonical velocity is that of the radial reference; compact density
perturbations have strictly lower order velocity. From its stream,
\[
 u_{0r}=\frac a{p+3}\cos2\theta,\qquad
 u_{0\theta}=-\frac{a(p+1)}{p+3}\sin\theta\cos\theta.
\]
The necessary second coefficient from the exact transport equation is
\[
 \Theta_1=\frac{p u_{0r}\Theta_0+u_{0\theta}\Theta_0'}D
    =-\frac{a^2}{D(p+3)}\sin\theta
                       (\cos^2\theta+p\sin^2\theta).         \tag{15}
\]
It is nonzero in the upper open half-circle, contradicting (14), since
\(p-2<2p-1\). This conclusion can also be obtained by direct substitution
of (14) and the leading velocity into the PDE. Thus no member of this
sequence is an exact profile.

## Dependencies and limits

The canonical strain and cubic weighted identities are independently
proved in the earlier origin/strain results. The necessary second term is
`../far_field_second_term/PROOF.md`; the compact-density tail estimate is
also covered by `../critical_inverse_decay/PROOF.md`. Formula (8) follows
directly from the canonical full-plane Fourier multipliers, without a box
or fitted harmonic field. The calculations in `verification/` are checks
of this proof, not substitutes for its uniform bounds or intermediate
value arguments. In particular no numerical full PDE solution or
nonexistence theorem is claimed. Local cubic jet relations, differentiated
energy identities and other full PDE consequences were not imposed by
this construction and cannot be silently added to its conclusion.

Independent implementation checks completed 2026-10-20T19:45:09.497250+00:00. See `verification/independent_checks.json`; all checks passed. These checks support the algebra and manufactured examples; the proof above supplies the quantified statements.
