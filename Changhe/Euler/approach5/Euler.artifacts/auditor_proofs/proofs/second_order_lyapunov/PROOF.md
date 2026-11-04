# Intrinsic classification of second-order formal Lyapunov functions

## Exact statement

Fix 0<c<1/2, any real omega and connected open V in R3. Let Hess0 be the 15-dimensional space of tensors T_ijk=T_ikj with sum_i T_iik=0. Let Psi be C1 on V times R3 times sl(3) times Hess0 times R, with arguments (y,u,M,T,p). Put b=(cI-omega J)y+u, w=ax(M), K_ij=epsilon_ilm T_mlj, z=ax(K), with ax(N)_i=epsilon_ijk N_kj.

Test the formal B derivative of Psi on every velocity and pressure 3-jet satisfying momentum through its second derivative and divergence through its second derivative. If every such derivative is nonpositive, then on every admissible projected 2-jet,

    Psi(y,u,M,T,p)=Psi(y,u,0,0,p)=psi(y,u,p).

Here admissibility is Kb+w+omega Jw-Mw=0. The function psi is constant if omega!=0 and equals f(H), f'>=0, if omega=0. H is the nonrotating Bernoulli value from A044. Values of Psi away from admissibility are not classified.

## Third-jet freedom

Let b!=0. Directional differentiation by b maps divergence-free homogeneous cubic vector polynomials onto divergence-free homogeneous quadratic vector polynomials. Rotate b to |b|e1. Given a target N, integrate it in x1 to obtain L. Its divergence is N1(0,x2,x3). Subtract integral_0^x2 N1(0,s,x3)ds from L2. This restores zero divergence and leaves the x1 derivative unchanged; division by |b| completes the construction. Thus T3->T3 b maps the 24-dimensional third-velocity-derivative space onto Hess0.

The second derivative of momentum is T3 b=-Q-L2, where Q=D3P is symmetric and L2 is fixed by the 2-jet. The exact compatibility for the right side to lie in Hess0 is

    sum_i Q_iik=-2 tr(M T_k).

It follows by differentiating div(momentum)=tr(M^2)+Delta P on divergence-free jets. The symmetric-cubic trace map is onto R3, so such Q exists, with its seven-dimensional harmonic cubic part arbitrary. Varying Q by a symmetric trace-free cubic H changes T3 b by -H. Nonpositivity for all its real multiples forces d_T Psi(H)=0 at each admissible nonstagnating 2-jet.

The kernel of T->K is exactly that harmonic-cubic space: zero curl gives symmetry in the first two indices, existing symmetry gives full symmetry, and divergence gives zero trace. Its dimension is seven, so the image is all of sl(3). Admissibility depends on T only through K. Integrating along the connected affine kernel fibers yields a C1 representative Phi(y,u,M,K,p), obtained using a fixed linear right inverse T=rho K.

On b!=0 the admissibility locus is smooth, since K->Kb from sl(3) onto R3 is surjective. The formal characteristic vector from an admissible 3-jet is tangent to it: differentiate the antisymmetric part of the first differentiated momentum equation, using the second differentiated equation and symmetric pressure derivatives. Thus the characteristic derivative of Psi equals that of Phi on this locus.

## Coupled strain freedom

Write M=S+[w]_cross/2 and K=R+[z]_cross/2 with S,R symmetric trace-free. Admissibility reads

    Rb-Sw=-[z]_cross b/2-w-omega Jw.                 (1)

Differentiating the vorticity equation gives

    D_B K=-(1+c)K-omega[J,K]+[M,K]+T_w,
    (T_w)_ij=sum_l T_ijl w_l.                       (2)

This can be checked directly by differentiating D_B w=-w-omega Jw+Mw and subtracting K DB. Replacing the actual Hessian T by T+tH for a harmonic cubic H fixes M,K and admissibility but changes the characteristic directions of M,K by t(H_b,H_w). Therefore dPhi annihilates those paired directions.

When b and w are independent, H->(H_b,H_w) is an isomorphism onto the space of symmetric trace-free pairs (S0,R0) with R0 b=S0 w. Both spaces have dimension seven. Injectivity holds because contraction with two independent directions being zero leaves only a component in their one-dimensional orthogonal complement, and the trace kills that component. Surjectivity of R->Rb follows from the explicit right inverse, for n=b/|b|, q=v/|b|,

    R=q n^T+n q^T-(n dot q)(I+nn^T)/2.

It is trace-free symmetric and Rb=v. The fibers of (1) are connected affine spaces. Hence Psi restricted to them equals a C1 function F(y,u,w,z,p). Use S=0 and the displayed right inverse to choose F; this defines F smoothly even when w is parallel to b, as long as b!=0.

## Elimination of z and w

Taking ax in (2) and using ax(T_w)=Kw gives

    D_B w=-w-omega Jw+Sw,
    D_B z=-(1+c)z-omega Jz+ax([S,R])+Rw.

The cross terms w cross z/2 and z cross w/2 cancel. With a0=F_u-F_p b, k=F_w and l=F_z, the strain-dependent part of the derivative is

    a0 dot Sb+k dot Sw+l dot (ax([S,R])+Rw).

Fix a solution of (1), and vary it independently by sS0 and tR0 where S0 w=0 and R0 b=0. The derivative is a polynomial of degree at most one in each of s,t. Nonpositivity for every real s,t forces its mixed coefficient l dot ax([S0,R0]) to vanish.

For b=e1, w=a e1+d e2, d!=0, put v=(-d,a,0),

    S1=vv^T-(a^2+d^2)e3e3^T, S2=ve3^T+e3v^T,
    R1=e2e2^T-e3e3^T, R2=e2e3^T+e3e2^T.

These meet the constraints. The axial commutators for (S1,R2),(S2,R1),(S2,R2) are

    (-4a^2-2d^2,-2ad,0), (4a,2d,0), (0,0,2d).

Their determinant is -8d^4. Thus l=0. Continuity extends F_z=0 across the parallel locus on b!=0.

Every S remains available in (1), by solving for R. The coefficient of this free trace-free S therefore gives

    sym(b tensor a0)+sym(w tensor k)=mu I.

Each symmetric rank-two summand has at most one positive and at most one negative eigenvalue. Their sum cannot be a nonzero scalar multiple of the three-dimensional identity, so mu=0. For independent b,w polynomial factorization yields k=beta b and a0=-beta w. Continuity extends the relevant identities, and F is constant on each plane b dot w=sigma. Write F=G(y,u,p,sigma). Then

    G_u-G_p b=-2G_sigma w.

Varying w in one such plane forces G_sigma=0. Thus F is independent of w. This is the A081 argument with all its required strain directions available.

## Closure of the admissibility locus and final reduction

For fixed b!=0, admissible jets with independent b,w are dense: perturb w while keeping S,z fixed and solve

    delta R b=(S-I-omega J)delta w

using the smooth right inverse. Lift delta K to delta T with rho. For a stagnating admissible jet with w!=0, perturb b and solve delta S w=K delta b. If b=w=0, approximate S by S_n with L_n=S_n-I-omega J invertible. These matrices are dense, since det L is a nonzero polynomial (already nonzero at S=0). Choose b_n nonzero and sufficiently small that w_n=L_n^-1 Kb_n->0, keep T fixed, and set M_n=S_n+[w_n]_cross/2. This gives admissible approximations with b_n!=0.

For fixed y,u,p and b!=0, taking w->0 in the representative S=0, z=0 makes K and T tend to zero. The common value is therefore psi(y,u,p)=Psi(y,u,0,0,p). The density arguments extend equality to every admissible jet. This psi is globally C1.

Every first jet with b!=0 extends to an admissible second jet by choosing K, and then to a third jet as above. Tangency gives the formal monotonicity of psi there; at b=0 its derivative is zero. The zeroth-order classification A044 now gives the stated f(H) or constant conclusion. A090 also identifies the hypothesis with testing all local analytic germs at nonstagnating points. No global decaying realization is asserted.

## Pressure arguments and ambient counterexample

Allowing DP and D2P as additional arguments does not enlarge the intrinsic class: E0 determines DP smoothly from y,u,M, and E1 determines D2P as the symmetric part of -Tb-M-M^2-omega[J,M]. Substitute these formulas to obtain a C1 function of the listed variables. E1 and E2 ensure agreement of the corresponding characteristic derivatives. This argument is about values on admissible jets only.

In contrast, Psi_res=|Kb+w+omega Jw-Mw|^2 has value and differential zero on the admissibility locus but is not ambient constant. At b=e1,M=0 it is zero for T=0 and one for T_211=1 with all other components zero. Thus literal ambient constancy would be false.

Dependencies: A044/A081 and elementary finite-dimensional calculations, with A090 only for the local-germ interpretation. C16 is CONFIRMED with its intrinsic scope. No all-orders or nonlocal classification is proved.
