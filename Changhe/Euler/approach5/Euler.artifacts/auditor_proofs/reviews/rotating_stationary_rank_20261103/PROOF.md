# Analytic rotating potential with a stationary rank zero

## 1. Exact local theorem

For every 2/5<c<1/2 and every finite omega!=0, let a=1-2c, d=1-c, Jx=e3 cross x, A=cI-omega J, X=Ax and L=dI+omega J. There exist x* off the vertical axis, an open ball about x*, and real analytic f,U,P there such that Delta f=0, X.grad f=-af, U=-grad f/a, P=-|U|^2/2 and

    div U=curl U=0, LU+DU(X+U)+grad P=0.

For the actual contraction k=X.U, S=P-|U|^2/2 and F=grad k cross grad S, one has k=f, U(x*)!=0 and F(x*)=DF(x*)=0. This is an actual local analytic solution, not only a compatible algebraic jet. Its vorticity is zero throughout the ball, so it does not give a supported vortical contact or a global extension.

## 2. Exact jets and all constraints

Set s=sqrt(2/d-3), mu=(-1+s)/2, nu=(-1-s)/2 and kappa=1/d. Since 1/2<d<3/5, 0<s<1, so mu,nu<0. They obey mu+nu=-1 and 1+mu^2+nu^2=1/d. Let

    g=e1, H=diag(1,mu,nu), X*=(-d,-omega/mu,0),
    x*=A^(-1)X*, f*=d/a, h2=mu(1-mu), h3=nu(1-nu),
    t=(-mu+d h2)/X*_2.

The inverse exists and X*_2!=0. Since A preserves the horizontal and vertical subspaces, x* is horizontal and nonzero, hence off the axis. Define the symmetric third tensor T by

    T111=kappa, T122=h2, T133=h3, T222=t, T233=-t,
    T112=T113=T123=T223=T333=0.

The trace of H is zero. For T, the contractions with e1,e2,e3 have traces kappa+h2+h3=0, t-t=0 and zero respectively. Thus the harmonic equation and all of its first derivatives hold at these jets.

The transport constraints through second derivative are X*.g=-af*, HX*=-Lg and T_X*=-H-omega[J,H]. The first two follow from X*_1=-d and mu X*_2=-omega. The commutator has only entries12 and21, equal to1-mu. Direct contraction gives diagonal entries -d kappa=-1, -d h2+X*_2 t=-mu and -d h3-X*_2 t=-nu, and entry12 equals X*_2 h2=-omega(1-mu). All other off-diagonal entries vanish. The final diagonal identity also follows from zero trace. Differentiating X.grad f=-af gives T_X+HA+A^T H=-aH, where HA+A^T H=2cH+omega[J,H]; since a+2c=1 the sign is exact.

## 3. Vanishing rank through first order

Let R=g cross(Hg) for the potential gradient and Hessian. At the prescribed point Hg=g, so R=0. For lambda=(grad f.D2f grad f)/|grad f|^2, differentiation at Hg=g cancels the gradient derivatives against the denominator derivative, giving grad lambda=(T111,T112,T113)=kappa g. Moreover

    T_g=H-H^2+kappa g tensor g.

Hence the value and derivative of D2f grad f-lambda grad f both vanish: its derivative is T_g+H^2-H-g tensor grad lambda=0. It follows that R=DR=0. Since S=-|grad f|^2/a^2, the actual F is -(2/a^2)R. Also U(x*)=-e1/a is nonzero.

## 4. Analytic realization, not just jet compatibility

Choose an analytic transversal to the nonzero field X at x* and flow coordinates (tau,u,v), with X=partial_tau. All exact solutions of the scalar transport equation are f=e^(-a tau)phi(u,v). The Euclidean flow is a rotation times dilation. In particular the identity [X.grad,Delta]=-2c Delta shows that for any such transported f,

    X.grad(Delta f)=-(a+2c)Delta f=-Delta f.

Therefore imposing Delta f=0 on the transversal imposes it on a whole flow neighborhood. On the transversal it is a linear analytic second-order equation for phi. Its principal symbol is the positive Laplacian symbol restricted to covectors annihilating X, so it is positive definite. Choose a transversal chart and solve for phi_vv; its coefficient is positive. This yields analytic normal form phi_vv=G(u,v,phi,phi_u,phi_v,phi_uu,phi_uv).

The order3 jet of f has20 scalar entries. The transport equation and its derivatives through order2 supply exactly the transport constraints that identify it with a unique transverse order3 jet, which has10 entries. This can also be seen directly in the flow coordinates, where every derivative involving tau is fixed by the derivatives without tau. The harmonic value and two transverse first derivatives give the normal-form constraints on phi_vv, phi_uvv and phi_vvv. The flow derivative is redundant by the displayed commutator identity. Thus there are exactly seven free transverse derivatives.

Choose polynomial Cauchy data phi(u,0) through order3 and phi_v(u,0) through order2 to equal those seven target derivatives. The normal form fixes the other three to the prescribed values because all harmonic compatibility conditions were checked in Section2. Apply analytic Cauchy-Kovalevskaya to obtain phi near the basepoint. One explicit first-order reduction uses unknowns phi,phi_u,phi_v, with v derivatives respectively phi_v, partial_u phi_v and G; the initial data satisfy phi_u=partial_u phi. The relation persists because its v derivative is zero. Hence this is an applicable first-order normal-form problem with no hidden mixed-derivative requirement.

The primary input is Gantumur's 2011 Theorem18 and higher-order Corollary20, printed pages9-11. Their statements and proofs were reread from the retained text for this audit; the PDF and hash are recorded in the team records. The general analytic ODE and majorant inputs remain external. Real analytic coefficients and real data give a real solution by uniqueness and conjugation. Transforming back realizes f*,g,H,T exactly and solves both scalar equations in a neighborhood; restrict to a ball about x*.

## 5. Complete nonlinear equation

Harmonicity gives div U=0 and the potential formula gives curl U=0. The transport equation gives X.U=f, so k=f is the actual contraction. Differentiating transport with its transpose gives D2f X=-(aI+A^T)grad f=-L grad f. Thus DU X=-LU. For irrotational U, DU U=grad(|U|^2/2), canceled exactly by grad P. This verifies every term of the nonlinear momentum equation. It also gives the local pressure Poisson equation. Sections2-4 prove the asserted stationary rank zero for these actual analytic fields.

## 6. Consequences and limitations

All six submitted sections and all six independent sections were read. Every tensor component, normal-form compatibility constraint and momentum sign was checked by hand; no numerical computation was used. The construction is valid for every nonzero omega, with no uniform limit claimed as omega approaches zero. Its third jets involve division by omega.

It refutes extending the pointwise first-order rank obstruction of LIT275 to arbitrary nonzero rotation under only harmonicity, twisted homogeneity, zero remainder and nonzero velocity. LIT275 itself remains correct at omega0. The special complex-power family of LIT274 remains excluded; the present analytic solution is not that family. No supported vorticity, global matching, canonical whole-space pressure, natural whole-space decay or second derivative vanishing of F is established. Those extensions and the unrestricted conjecture remain open.

The subsequently confirmed local lemma in the team records applies to these analytic potentials, since their target exponents exclude c=1/3. It proves D2F(x*)!=0: otherwise R and its first two derivatives would vanish, contrary to that lemma. Together with F=DF=0, the analytic rank field has exact vanishing order2 at x*. This is a local derivative conclusion and uses no vorticity-support premise.
