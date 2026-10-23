# Characteristic and x-axis identities

Status: independently derived necessary conditions. The principal existence problem remains open.

## Hypotheses and notation

Assume the exact primary profile in ../origin/PROOF.md. Put W=c_l X+U, A=2c_l-1, and let Phi_t be the flow of W. On the x-axis set w(x)=W1(x,0), h(x)=partial_y W2(x,0), and g(x)=rho_y(x,0).

The global flow exists for every finite positive or negative time because W is smooth locally and |W(X)|<=C(1+|X|). Backward trajectories are bounded. Indeed, for sufficiently large r, W.e_r>=c_l r/2, so a backward trajectory cannot move outward across such a circle.

Every equilibrium of W and every critical point of rho belongs to {rho=0}, by W.grad rho=rho. Therefore rho has no local extremum with a nonzero value. A periodic orbit of W would be a simple closed curve by uniqueness of ODE solutions. Its flux is zero, but the divergence theorem would give flux=2c_l times its positive enclosed area. Thus there is no periodic orbit.

## The x-axis equations

Parity makes both axes invariant. Incompressibility gives

    w'+h=2c_l.

Differentiate the profile equation in y at y=0. Terms involving rho_x on that axis vanish, as do W2 and partial_y W1. The remaining terms give

    w g'=(1-h)g=(w'-A)g.

Where g!=0 this is equivalent to

    (w/g)'=A/g.

On an interval from zero without zeros of g, w(0)=0 gives

    w(x)=A g(x) integral_0^x 1/g(s)ds.

For x>0, g has the fixed sign of a0 on such an interval. The last expression is positive regardless of that sign. The formula cannot be continued by division through a zero of g without additional justification.

Suppose g has a zero of finite order m>=1 at x*. Write z=x-x* and g=d z^m+O(z^(m+1)), d!=0. In the undivided equation, the coefficient of z^(m-1) is m d w(x*), so w(x*)=0. Writing w=w1 z+O(z^2), the next coefficient gives

    m w1=w1-A.

The case m=1 is impossible since A>0. For m>=2,

    w'(x*)=-A/(m-1)<0,  h(x*)=2c_l+A/(m-1)>0.

Parity removes the off-diagonal entries of DW on the x-axis. The equilibrium is therefore a saddle. This finite-order argument makes no assertion that flat zeros of g are absent.

## Reconstruction in the source basin

Let B(0) consist of points whose backward orbit tends to zero. Near zero, parity and the center identities give

    W1=x(A+O(r^2)),  W2=y(1+O(r^2)),
    rho=y(a0+O(r^2)).

A backward orbit in B(0) eventually lies in a small disk, where its radius decays at least exponentially at any rate smaller than 1. The integral of its squared radius over backward time is finite. The scalar y equation then implies convergence of

    eta(X)=lim_{t->infinity} e^t y(Phi_-t X).

For y(X)!=0 the limit has the same sign as y(X) and is nonzero, because e^t y(Phi_-t X) equals y(X) times the exponential of a convergent real integral after a finite initial segment. Along a trajectory, rho(Phi_-t X)=e^-t rho(X). Substitute the local expansion of rho and pass to the limit to obtain

    rho(X)=a0 eta(X),  X in B(0).

This proves the sign of rho on the source basin only. Extending that sign to the whole plane requires a proof that the basin is the whole plane, or another global argument.

## Scope of the single-equilibrium claim

If zero is the only equilibrium, a standard planar limit-set theorem completes the basin argument: a bounded semiorbit whose limit set contains finitely many equilibria has either a periodic limit orbit, a single equilibrium, or a set built from connecting trajectories and equilibria. Apply it to -W. There are no periodic orbits. Zero is a hyperbolic sink of -W, so it has no nonconstant outgoing trajectory and cannot support a connecting cycle. The backward limit is zero. Thus B(0)=R^2 in this separately stated case.

The preceding paragraph explicitly uses the planar limit-set theorem as a dependency. The present work has not proved that the primary PDE has only one equilibrium, finitely many equilibria, or no off-axis equilibria. No such assumption enters the x-axis identities or the source-basin reconstruction.
