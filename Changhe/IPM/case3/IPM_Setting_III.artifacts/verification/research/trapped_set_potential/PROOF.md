# A maximum of the canonical potential removes the finite-zero hypothesis

Date: 2026-10-20. Status: CONFIRMED. Independent exact checks passed 17:26Z; actual Opus5.5 lead and separate referee hdyn2 audits agree, including non-isolated equilibria. The existence of any primary profile remains OPEN. This result is conditional on an exact primary profile, but does not assume a finite or isolated equilibrium set.

## 1. Statement, notation and dependencies

Let ell>1 and let a smooth exact full-plane primary profile satisfy

    W.grad rho=rho, W=ell X+U, div U=0, curl U=-rho_x,
    rho(-x,y)=rho(x,y), rho(x,-y)=-rho(x,y),
    U1 odd in x/even in y, U2 even in x/odd in y,
    a=rho_y(0)!=0,
    |rho|+(1+r)|grad rho| <= C(1+r)^gamma, 0<gamma<1,

with the canonical sublinear velocity. Put A=2ell-1 and p=1/ell. Define the complete flow Phi_t of W. Write Hdyn for: every nonzero trajectory tends to zero backward and escapes to infinity forward. Let Theta be the asymptotic coefficient in rho=r^p Theta(theta)+o(r^p), uniform in angle.

Then

    Hdyn if and only if Theta(theta)!=0 for every 0<theta<pi.    (1)

No isolation or finiteness assumption on equilibria is needed. In particular an exact profile whose rescaled flow has additional equilibria must have an upper-half-circle zero of its far-field density coefficient. This is a necessary alternative, not an exclusion of profiles with such zeros.

We use the already proved consequences of the primary equations: c=psi_xy(0)=1-ell, DW(0)=diag(A,1); U and rho have order r^p; all their derivatives have symbol bounds of order p; and the uniform smooth angular far-field limit exists. These are established in ../origin/PROOF.md, ../far_field_holder/PROOF.md and ../local_ipm_continuation/PROOF.md. Their proofs do not assume Hdyn or a finite equilibrium set. The flow, potential and maximum arguments below are rederived independently. Only the usual local strong unstable manifold for a smooth vector field with a spectral gap is used as a local ODE fact; the exact spectral gaps used below are specified.

## 2. The compact connected trapped set

Choose R so large that W.X/r >= ell r/2 for r>=R. Linear growth gives a complete flow. The closed disk D_R is invariant under backward flow. Its backward images Phi_{-t}(D_R) are nested compact topological disks. Their intersection

    K=intersection_(t>=0) Phi_{-t}(D_R)

is compact, nonempty and connected, since it contains zero and is the nested intersection of compact connected sets. It is exactly the set of forward-bounded trajectories: once a trajectory leaves D_R it has strictly increasing, at least exponentially growing radius and cannot return. Conversely a forward-bounded trajectory can never have left D_R. The flow preserves K in both time directions.

The volume formula det D Phi_t=exp(2ell t) gives |K|=0, although the maximum argument below does not need this measure assertion. Transport gives

    rho(Phi_t X)=exp(t)rho(X).

For X in K the left side is bounded for t>=0. Thus rho=0 on K. Every equilibrium lies in K, and every point outside K escapes forward.

Parity gives rho=y G with G smooth and G(0)=a!=0. Hence the nodal set near zero is exactly the x-axis. Along that axis set

    w(x)=W1(x,0), g(x)=rho_y(x,0).

Here w is odd, w'(0)=A>0 and w(x)>0 for all sufficiently large positive x. Its positive zeros, if any, form a compact set away from zero. Let b be their largest member, taking b=0 if there are none. Direct scalar flow on the invariant x-axis gives

    K intersect {y=0}=[-b,b] times {0}.                    (2)

Indeed each scalar trajectory in this interval remains between its boundary equilibria, while outside it the sign of w and absence of further zeros imply escape. This assertion allows infinitely many roots inside the interval.

## 3. The canonical potential and backward limits

The vector field W+rho e2 is curl-free. Define the smooth real potential P by

    P(0)=0, grad P=W+rho e2,
    P(X)=integral_0^1 [W(tX)+rho(tX)e2].X dt.

The integral differentiates to the claimed gradient by symmetry of its derivative. It also gives P=ell r^2/2+O(1+r^(p+1)). Along any trajectory,

    dP(Phi_t X)/dt=|W|^2+rho W2.                          (3)

On K, and on every nodal trajectory, this is |W|^2. Therefore any maximizer of P on K is an equilibrium: otherwise its small positive-time displacement remains in K and increases P.

All backward orbits are bounded because the exterior radial field is outward. On such a bounded orbit the error |rho W2| in (3) is O(exp(t)) for t<=0. Integration implies integral_(-infinity)^0 |W(Phi_t X)|^2 dt<infinity. On the compact orbit closure the derivative of |W|^2 is bounded, so this nonnegative uniformly continuous integrable function tends to zero as t tends to negative infinity. Every backward limit point is consequently an equilibrium. In particular if K={0}, the entire backward trajectory converges to zero; forward escape for every nonzero point already follows from Section 2. Thus K={0} implies Hdyn, without an isolated-limit-set theorem.

On the x-axis P_x=w and P(0)=0, so

    P(x,0)=A x^2/2+O(x^4)>0 for sufficiently small x!=0.  (4)

If K is not a singleton, connectedness implies that it has points of every sufficiently small positive radius. These points are on the x-axis because K is nodal and the local nodal set is the axis. Hence (4) implies

    max_K P>0.                                           (5)

Any maximizer is therefore an extra equilibrium, distinct from zero.

## 4. A fast unstable nodal branch at every equilibrium

At any equilibrium Q, differentiating transport gives

    DW(Q)^T grad rho(Q)=grad rho(Q), tr DW(Q)=2ell.

If grad rho(Q)!=0, the two eigenvalues are 1 and A>1. If grad rho(Q)=0, the curl identity gives DW21=DW12, so DW is a real symmetric matrix with trace 2ell. Its largest eigenvalue is at least ell>1. Thus at every equilibrium there is a spectral subspace with eigenvalues strictly greater than one, separated from the remaining eigenvalues by a cutoff chosen above one and away from the spectrum.

The local strong unstable manifold for this subspace has backward contraction O(exp(-lambda T)) for some lambda>1. It has positive dimension. Since rho(Q)=0 and rho is locally C1, any point X on it satisfies

    |rho(X)|=exp(T)|rho(Phi_{-T}X)|
            <= C exp((1-lambda)T), T>=0.

Letting T increase proves rho(X)=0. Its continued trajectories are nodal. For a nonstationary point on this manifold, (3) and backward convergence to Q imply

    P(X)-P(Q)=integral_(-infinity)^0 |W(Phi_t X)|^2 dt>0.  (6)

The integral converges by the stated exponential contraction.

At a nonzero x-axis equilibrium Q=(x,0), parity makes

    DW(Q)=diag(w'(x),2ell-w'(x)).

In particular if w'(x)<=0, the strong unstable manifold is a curve tangent to the vertical direction, with eigenvalue 2ell-w'(x)>1. It has a branch entering y>0 and another entering y<0, including the degenerate case w'=0. If w'(x)>0, then P_x(Q)=0 and P_xx(Q)=w'(x)>0. By (2), at least one sufficiently short horizontal side of Q lies in K. The strict one-sided local minimum of P along the axis then rules out Q as a maximizer of P on K. This argument applies also at either extreme root b or -b.

## 5. Escaping upper nodal trajectories and scattering

The symbol bounds imply that every escaping trajectory has a nonzero vector limit

    Q_infinity(X)=lim_(t->infinity) exp(-ell t)Phi_t X.

For completeness, in exterior polar coordinates r'=ell r+O(r^p) and theta'=O(r^(p-1)); hence log r-ell t and theta converge, with a positive limiting radial factor. To check that an escaping trajectory in y>0 has limiting angle strictly between 0 and pi, use radius as time. The angular equation is

    dtheta/dr=Utheta/[r(ell r+Ur)],
    |partial_theta^j right side| <= C_j r^(p-2).

The first derivative is integrable, so the limiting angular map from a fixed large circle has derivative exp(integral partial_theta right side), bounded above and below by positive constants. It is a circle diffeomorphism. Axis invariance fixes angles 0 and pi (and also pi/2), so it maps the upper angular interval onto itself, with its endpoints excluded for interior initial angles. This proves the required strict direction statement, including arbitrarily close trajectories to the x-axis.

Using ell p=1, the uniform far-field limit and transport give

    rho(X)=|Q_infinity(X)|^p Theta(arg Q_infinity(X)).       (7)

Thus if Theta has no zero in 0<theta<pi, every nodal point in y>0 lies in K. By reflection the same assertion holds in y<0. This is the only sign condition needed for the maximum argument.

## 6. Proof of the converse in (1)

Assume Theta has no zero in the open upper half-circle. Suppose for contradiction K is not {0}. Choose a maximizer Q of P on K. By (5) and (3), Q is an extra equilibrium.

If Q is off the x-axis, choose a nonstationary point X sufficiently close to Q on its fast unstable nodal manifold. X remains in the same open half-plane. Section 5 implies X in K. But (6) gives P(X)>P(Q), contradicting maximality.

If Q lies on the x-axis, the case w'(Q)>0 is excluded by the horizontal local-minimum argument in Section 4. In the remaining case w'(Q)<=0, take X on its upper fast unstable nodal branch. Again X lies in K by Section 5 and (6) contradicts maximality.

All cases are excluded. Therefore K={0}, and Section 3 gives Hdyn. No finiteness, isolation, graph decomposition, analytic unique continuation or order of vanishing at a degenerate equilibrium has been used.

## 7. Proof of the forward implication and scope

Assume Hdyn. For any point in y>0 its backward trajectory stays in y>0 by uniqueness and approaches zero. Near zero, rho has the sign of a y, so transport implies rho/a>0 throughout y>0. To infer that Theta has no interior zero, rather than merely nonnegativity, use the exterior angular scattering map from Section 5. For each interior limiting angle, there is an escaping trajectory with that angle: choose the inverse angular point on the fixed exterior circle. Formula (7) has a nonzero density value on that trajectory and a positive radial factor. Hence Theta is nonzero at that angle. This proves (1).

The condition that Theta has no interior zero remains an additional alternative to check; it does not follow from parity or a nonzero y-axis amplitude alone. This theorem therefore does not settle full-class existence, nonexistence, or the unconditional Hdyn question. It improves the finite-equilibrium criterion in the separate hdyn1 draft by a compact-set maximum argument, and does not depend on that draft's finite-tree lemma. A profile with extra equilibria, if one exists, must have an escaping off-axis nodal trajectory and an interior far-field zero.

## 8. Additional independent checks of the axis and scattering statements

The preceding theorem can be combined with the following equivalent conditions:

    Hdyn;
    W has only the equilibrium zero;
    w(x)>0 for every x>0;
    g(x)!=0 for every real x.

To verify this directly, differentiation of transport in y on the axis and div W=2ell give

    w g'=(w'-A)g.                                        (8)

If w has no positive zero, (2) makes zero an isolated point of K, since the nodal set near zero is the axis. Connectedness gives K={0}, hence Hdyn. Conversely Hdyn excludes all other equilibria, so w is positive by its sign near zero. Equation (8) is a nonsingular linear equation on every compact subinterval of x>0; starting near zero where g has the sign of a proves g never vanishes. Reflection covers negative x. If g never vanishes but w has a positive zero, let x1 be the first root. It exists because w>0 near zero and at infinity. Its derivative is nonpositive. Equation (8) at x1 instead gives w'(x1)=A>0, a contradiction. The equilibrium formulation follows since an axis root is an equilibrium, and Hdyn excludes any extra equilibrium.

If Hdyn fails, x1 exists and g(x1)=0. Write lambda=w'(x1)<=0. For lambda<0, the solution of (8) on the left is

    g(x)=C w(x)exp(-A integral_(x*)^x ds/w(s)).

A simple smooth zero of w gives a smooth nonvanishing factor times (x1-x)^(1-A/lambda), with nonzero coefficient. Smooth extension of g therefore forces m=1-A/lambda to be an integer m>=2. Thus

    lambda=-A/(m-1), DW(x1,0)=diag(lambda,2ell-lambda).

The full leading density term is C1 (x-x1)^m y, with C1!=0. To see that no lower term occurs, at a critical equilibrium the first nonzero Taylor homogeneous term R_k must obey (DW z).grad R_k=R_k. At this diagonal saddle a monomial z1^n z2^q can occur only when

    n lambda+q(2ell-lambda)=1,
    n-q=(2ell q-1)(m-1)/A.

The value q=0 is impossible, q=1 gives n=m, and every q>1 has total degree n+q>m+1. There is at most one resonant monomial at each fixed degree because the eigenvalues are distinct. The nonzero coefficient of g supplies the displayed term. Higher Taylor degrees need not satisfy a homogeneous resonance equation: they have forcing from lower density jets and nonlinear velocity jets. No claim about such higher degrees is used.

If lambda=0, the eigenvalues are 0 and 2ell. Every polynomial eigenvalue is 2ell q with integer q>=0, so none equals one. Differentiated transport gives a zero first jet, and induction in the full Taylor equation then gives a zero jet at every order. Thus rho and g are flat there, without any assertion of analytic unique continuation. In both cases the vertical fast unstable nodal branch from Section 4 exists. If m is odd in the saddle case, g changes sign across x1. A point just above the right-hand axis therefore has density of the sign opposite to a. It escapes since its density is nonzero and K is nodal. Equation (7), together with the sign of Theta at pi/2, supplies an interior zero of Theta. The theorem in Section 6 supplies such a zero for the even-m and degenerate alternatives as well.

Finally the scattering map in Section 5 is a smooth diffeomorphism

    Q_infinity: R^2 minus K -> R^2 minus {0}.

Every escaping orbit crosses a fixed sufficiently large circle exactly once, by outward radial transversality. Its crossing angle theta and elapsed time t form smooth coordinates. In these coordinates

    Q_infinity=exp(ell t) A_R(theta) exp(i S_R(theta)),

where S_R is the circle diffeomorphism already proved and A_R is strictly positive. Its explicit expression is

    A_R(theta)=R exp(integral_R^infinity
       Ur(s,theta(s))/[s(ell s+Ur(s,theta(s)))] ds).

All angular derivatives of the integrand are O(s^(p-2)); the angular flow and its fixed-order derivatives are uniformly bounded by integrable-coefficient ODEs. Hence the integral converges in every angular Ck norm. The displayed formula gives a smooth bijection with smooth inverse to the punctured plane. Axis invariance gives quadrant preservation. Formula (7) then shows that escaping upper nodal trajectories correspond one-to-one to the interior angular zeros, with time translates identified. A finite-order angular zero has the same transverse order along its trajectory. These statements do not assume that the full equilibrium set is finite.
