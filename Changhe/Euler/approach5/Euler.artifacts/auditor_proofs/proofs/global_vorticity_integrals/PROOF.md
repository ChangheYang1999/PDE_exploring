# Global vorticity geometry and conditional Liouville theorems

## Exact statement

Let U in C2(R3;R3), P in C1(R3), c>0 and omega in R satisfy the full divergence-free rotating Euler profile equation. Assume U(y)=o(|y|) uniformly. Set B=(cI-omega J)y+U and Omega=curl U.

1. If there is a fixed a0 in R3 with Omega(y).(y-a0)=0 for every y, then U is constant. This conclusion holds for every c>0.
2. If 0<c<1/2 and there are globally defined real F1,F2 in C2(R3) with Omega.grad Fj=0 and grad F1 cross grad F2 nonzero wherever Omega is nonzero, then U is constant.

Under the additional target condition U(y)->0, the constant is zero. In particular, part 2 applies to a global representation U=A grad C+grad D with real C3 functions A,C,D. These are additional global geometric hypotheses; they are not derived from decay.

## Common dynamical facts

Uniform sublinearity makes B at most linear, hence its C1 flow Phi_s complete. Since B.y=c|y|^2+U.y, every backward orbit from a fixed compact set remains in one common compact ball. Curling the equation gives

    [B,Omega]=-(1+c)Omega,
    D Phi_s Omega=exp((1+c)s) Omega composed with Phi_s.

There is no nonconstant periodic Omega trajectory. Otherwise, a periodic trajectory of period T is sent by Phi_-s to one of period exp(-(1+c)s)T. These curves all lie in one compact convex ball. Let L be the Lipschitz constant of Omega on that ball. For any one such curve z of period T0 and temporal mean zbar, the periodic Wirtinger inequality gives

    integral_0^T0 |z'|^2
      = integral_0^T0 (Omega(z)-Omega(zbar)).z'
      <= L ||z-zbar||_2 ||z'||_2
      <= L T0/(2pi) ||z'||_2^2.

Thus T0>=2pi/L whenever L>0; L=0 itself prohibits a nonconstant periodic curve. The shrinking periods contradict this. This argument uses no global completeness assumption for other Omega trajectories.

For part 2 we additionally use A048-A049, proved in the team records. The Omega flow psi_tau is complete. Its compact initial sets grow at most C(1+|tau|)^((c+epsilon)/(1+c)); choose epsilon>0 so this exponent is below 1/3. Because div Omega=0, volume packing makes its time-one map conservative and almost every point recurrent in both directions. No vorticity integrability is assumed in those results.

## Proof of the spherical condition

For r>0 put V(n)=Omega(a0+r n) on the unit sphere. It is a C1 tangent field. The radial component vanishes at every radius, so the spherical divergence formula and div Omega=0 imply div_S V=0. This step would not follow from tangency to a single sphere alone.

Let sigma be the sphere area form. The closed C1 one-form i_V sigma is dq for a real C2 function q, since every closed one-form on S2 is exact. If V is not zero, q is nonconstant. Sard's theorem for a C2 scalar function on a two-dimensional manifold supplies a regular value in the interior of its image. Its nonempty level set is a compact one-dimensional manifold, hence has a circle component. V is tangent to that circle and nowhere zero there. Its flow on the circle is periodic. Rescaling by r gives a nonconstant periodic Omega trajectory, which the common argument excludes.

It follows that Omega vanishes on every sphere about a0 and hence, by continuity, also at a0. Every component of U is harmonic, because div U=curl U=0. For fixed x, the harmonic gradient estimate gives

    |grad U(x)| <= C R^-1 sup_(|y-x|<=R)|U(y)| -> 0.

Uniform sublinearity justifies the limit even on translated balls. Therefore U is constant.

## Proof of the two-integral condition

Set F=(F1,F2) and N={Omega!=0}. F is a C2 submersion on the open set N. Its global set C of critical values has two-dimensional measure zero by Sard's theorem: the differentiability threshold is k>3-2, satisfied by k=2. Moreover N intersect F^-1(C) has three-dimensional measure zero. To see this, use countably many submersion charts on N, in which F is projection to the first two coordinates. Fubini gives nullity in each chart; C1 changes of coordinates preserve null sets on relatively compact subcharts.

For almost every x in N, x is recurrent for psi_1 and F(x) is a globally regular value. The full fiber M=F^-1(F(x)) is then a closed embedded C2 one-dimensional manifold without boundary. The complete Omega trajectory remains in its connected component. A connected one-dimensional manifold is a line or a circle. A nonzero trajectory on a line is monotone in an intrinsic coordinate and cannot return to its initial point. On a circle containing zeros, each nonconstant trajectory stays in an ordered arc and has the same obstruction. On a circle without zeros, every trajectory is periodic. Ambient recurrence implies intrinsic recurrence near x because the fiber is embedded. Thus x lies on a nonconstant periodic Omega trajectory, again impossible.

Almost every point of N would have these two generic properties, so N has measure zero. As N is open, it is empty. The harmonic argument above completes the proof. For the Clebsch representation, Omega=grad A cross grad C; take F1=A,F2=C.

## Audit scope and dependencies

This confirms both parts of LIT32. The only external general inputs are the ordinary differential equation existence theorem, Wirtinger's inequality, elementary sphere cohomology, Sard's theorem, the regular value theorem and harmonic interior estimates. A048-A049 provide the separately proved completeness and recurrence inputs for part 2. There are no pressure boundary terms or pressure normalization assumptions. The proof is uniform in finite omega and does not impose axisymmetry. Local first integrals do not suffice, nor does one unrestricted global first integral.

Audit written: 2026-11-02T20:39:22Z
