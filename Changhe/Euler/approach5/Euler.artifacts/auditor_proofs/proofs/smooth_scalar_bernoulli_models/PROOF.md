# Smooth scalar forcing does not control the Bernoulli coefficient at the core

## Exact statement

Fix 2/5<=c<1/2 and finite omega. Set A=cI-omega J, a=1-2c>0, sigma=a/c, and B(y)=Ay on R3. Its complete flow is Phi_t(y)=exp(tA)y and div B=3c. There are radial smooth real functions H,F with F nonzero, nonnegative and compactly supported, and H->0 uniformly at infinity, such that

    (B+a)H=a F, f=H-F>=0, BH=-a f.

For every y!=0,

    H(y)=a integral_0^infinity f(Phi_t y)dt,
    K(y)=lim_(t->infinity) exp(at)H(Phi_t y)
        =H(y)+a integral_0^infinity exp(at)F(Phi_t y)dt
        =C |y|^-sigma,

where C>0. Both integrals converge absolutely. The limit at y=0 is infinite, so the actual finite-limit domain is R3 minus {0}. For finite p>=1, K is locally Lp exactly when p<3c/a. These functions satisfy all the scalar spatial and transported bounds used in A287-A293.

There is also a nonzero smooth compactly supported radial H and smooth compactly supported F satisfying the same scalar equations, whose coefficient K is identically zero at every point and whose orbit integrals converge absolutely at every point. In that second construction f need not have one sign.

These statements audit LIT64. Neither construction is an Euler profile: B=Ay would require actual U=0, so actual canonical pressure, H,F and f would all vanish.

## First construction and direct verification

Choose a smooth nonincreasing eta:[0,infinity)->[0,1], equal to one on [0,1] and zero on [4,infinity). Let

    F(y)=eta(|y|^2),
    H(y)=sigma integral_0^1 t^(sigma-1)eta(t^2|y|^2)dt.

All derivatives in y may be moved under the integral on compact sets because their absolute values are bounded by a constant times t^(sigma-1), which is integrable. Thus H is smooth globally, and H=F=1 in the unit ball. Since t<=1 and eta is nonincreasing, eta(t^2|y|^2)>=eta(|y|^2). The weight sigma t^(sigma-1) has integral one, giving H>=F.

For r>0 substitute s=tr:

    H(r)=sigma r^-sigma integral_0^r s^(sigma-1)eta(s^2)ds.

Differentiation yields rH'(r)+sigma H(r)=sigma F(r). Rotation annihilates the radial H and c sigma=a, so this is exactly (B+a)H=aF. Smoothness extends the identity to zero. For r>=2,

    H(r)=C r^-sigma,
    C=sigma integral_0^2 s^(sigma-1)eta(s^2)ds>0.

In particular H decays uniformly, and its gradient is O(r^(-sigma-1)). The equality sigma+1=1/c-1 is the gradient exponent appearing in the conditional Dini estimate, but does not supply a velocity field.

For every nonzero y, |Phi_t y|=exp(ct)|y|. After a finite time the radius exceeds two, F(Phi_t y)=0 and exp(at)H(Phi_t y)=C|y|^-sigma. The weighted forcing integral therefore has a finite initial interval only. Integration of the exact scalar equation gives its equality with K-H. Also f>=0 and H(Phi_t y)->0, so integrating BH=-af gives the nonnegative, finite future integral for H. At zero, H=F=1 and the orbit is stationary: the renormalized H and weighted forcing integral both diverge. Assigning an arbitrary finite value to K at zero does not change that fact.

## Integrability and the precise bounds tested

Polar integration gives

    integral_(B_R) |K|^p=4 pi C^p integral_0^R r^(2-sigma p)dr.

It is finite exactly when p sigma<3, with logarithmic divergence at equality. Let beta=5-2/c in [0,1). Since 3-2sigma=beta+2>0, the smooth bounded core and exact exterior power give

    integral_(B_R) |H|^2<=C1 R^(beta+2), R>=1.

Compact support of F gives integral_(B_R)|F|^p<=C_p<=C_p R^beta for every finite p>=1 and R>=1. In particular the forcing bound holds in every exponent used in A293. Change of variables gives

    ||F composed Phi_t||_Lp(Q)
        <=exp(-3ct/p)||F||_Lp(R3)

for every measurable Q. On bounded Q, the spatial H estimate and div B=3c give

    ||H composed Phi_t||_L2(Q)<=C_Q exp(-at).

The analogous f estimate follows from f=H-F. Thus the example retains the scalar estimates, exact evolution and derivative relation, while its coefficient still fails local critical Lp. It does not prove that the weaker guaranteed exponent in the actual Euler problem is optimal.

## Second construction and zero coefficient

Choose any nonzero smooth radial H supported in the annulus 1<|y|<2 and set

    F=H+(BH)/a, f=-(BH)/a.

These are smooth and compactly supported, and both scalar equations hold by definition. For y!=0 the orbit crosses the support in a bounded time interval and eventually leaves it forever. Hence exp(at)H(Phi_t y) is eventually zero, and both weighted and unweighted integrals converge absolutely. At zero all functions vanish, so these assertions hold there as well. Integration gives the same two formulas, now with K=0 and H nonzero.

The radial identity also gives

    integral_0^infinity r^(sigma-1)F(r)dr
        =[r^sigma H(r)]_0^infinity/sigma=0.

F cannot be identically zero: the homogeneous radial ODE would force the compactly supported H to be zero. Thus this F takes both signs. The claim makes no nonnegativity assumption on this second forcing.

## Scope and evidence

The missing Euler equalities are H=P0+|U|^2/2+Ay.U, F=P0-|U|^2/2, f=U.B, and B=Ay+U for the same velocity and canonical pressure. With the chosen B they force all four scalar fields to vanish. Therefore these are counterexamples only to scalar closure arguments and to transfer of volume-almost-everywhere limits onto singular invariant supports. They do not challenge any theorem using the full Euler identities. All formulas were checked analytically; no computation or additional source theorem was needed.
