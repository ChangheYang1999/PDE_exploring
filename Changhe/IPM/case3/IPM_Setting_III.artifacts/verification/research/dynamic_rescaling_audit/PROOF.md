# Dynamic rescaling, physical time and two local gauges

Written 2026-10-21 as an independent audit of the lead's 05:16 proposal. These are exact change-of-variable and Taylor identities. They provide a numerical formulation, not a proof that it converges or that a steady state exists.

## 1. Equations and hypotheses

Let rho(X,tau) be real, smooth in X and differentiable in tau, with the required even-x/odd-y parities and with its canonical full-plane velocity U[rho]. Assume enough local time regularity for the derivatives below and the sublinear growth needed for the inverse. Let A(tau),L(tau)>0 be continuously differentiable. Define physical time and coordinates by

    dt/dtau=L/A,  X=Z/L,
    varrho(t,Z)=A rho(X,tau),   u(t,Z)=A U[rho](X,tau).

The stream is Psi=A L psi(X,tau). It obeys -Delta_Z Psi=partial_Z1 varrho and generates u. The physical transport equation holds exactly if and only if

    partial_tau rho=c_w rho-(c_x X+U[rho]).grad rho,
    c_w=-A'/A,   c_x=-L'/L.                                      (DR)

Indeed, dividing varrho_t+u.grad_Z varrho by A^2/L gives rho_tau+(A'/A)rho-(L'/L)X.grad rho+U.grad rho. All changes are invertible while A,L>0 and the fields remain regular. The canonical parity and sublinear velocity condition are preserved by these positive amplitude and spatial changes, using the uniqueness and scaling of the inverse in ../inverse/PROOF.md and ../scaling/PROOF.md (or the original prompt's directly verified scaling law).

## 2. Physical time and gradient, including variable rates

Put G(tau)=int_0^tau(c_x-c_w)(s) ds. Direct integration gives

    A/L=(A(0)/L(0)) exp(G(tau)),
    t(tau)-t(0)=(L(0)/A(0)) int_0^tau exp(-G(s)) ds.                (1)

Consequently the available physical time as tau tends to infinity is finite if and only if int_0^infinity exp(-G(s)) ds is finite. Pointwise c_x>c_w alone does not imply this condition. For example, take c_w=1 and c_x=1+1/(1+tau); then G=log(1+tau) and physical time diverges logarithmically. Taking c_x=1+2/(1+tau) instead gives finite physical time, while the difference still tends to zero. Constant rates give finite physical time exactly when c_x>c_w. A uniform positive lower bound on their difference eventually is sufficient. These examples concern the rescaling functions and refute the general time criterion independently of whether a particular solution realizes the rates.

The physical origin slope is (A/L) rho_y(0,tau). If that rescaled slope is held at 1, its physical value is exactly the first expression in (1). For a nonconstant rescaled slope one must retain that factor. A statement exp((c_x-c_w)tau) without the integral is valid for constant rates only.

## 3. Steady normalization

Suppose DR has a steady state and constant rates c_w>0, c_x/c_w>1. Linearity of the canonical inverse gives rho*=rho/c_w, U*=U/c_w, and

    ((c_x/c_w)X+U*).grad rho* = rho*.

Thus ell*=c_x/c_w and a*=rho_y(0)/c_w. This is the two-parameter amplitude normalization of the general equation; fixing the dynamic slope at 1 does not fix the slope of the normalized stationary equation. A steady state with c_w<=0 or c_x/c_w<=1 does not give the required primary branch through this argument. An independent evaluator must still compute the canonical center strain and residual after normalization.

## 4. Center coefficient evolution

Use coefficient, not derivative, conventions

    rho=a y+b x^2 y+e y^3+O(r^5),
    psi=c xy+d x^3 y+f x y^3+O(r^6).

Poisson gives d+f=-b/3. Expanding U=(-psi_y,psi_x) in DR yields

    a'=(c_w-c_x-c)a,
    b'=(c_w-3c_x+c)b-3a d,
    e'=(c_w-3c_x-3c)e-a f.                                      (2)

For example, the x^2 y transport coefficient is [2(c_x-c)+(c_x+c)]b+3ad, and the y^3 coefficient is 3(c_x+c)e+af, which prove the last two equations with their signs. There are no omitted quartic-stream contributions to these cubic identities.

Holding a=1 requires c_w=c_x+c. With that gauge, e'=-2c_w e-f. On the chart e=e_ref!=0, holding e fixed therefore gives

    c_w=-f/(2e),   c_x=-f/(2e)-c.                                (3)

These formulas use the actual canonical f and c at each stage. They do not guarantee c_w>0 or ell*>1 and can cease to define the desired chart if e vanishes or c_w vanishes. For a fixed target C>1, the alternative c_x=C c_w gives c_w=c/(1-C); positivity requires c<0. Both are legitimate conditional computational choices; neither assumes a*=1 without loss of generality.

The transport part of a frozen monomial x^m y^n has rate c_w-(c_x-c)m-(c_x+c)n. Under the slope gauge and c_w>0, division by c_w gives (1-n)-(2ell*-1)m. It is negative for all permitted higher density monomials (m even nonnegative, n odd positive, m+n>1) when ell*>1. This calculation omits the nonlocal variation U[h].grad rho and therefore is not a stability proof for DR.

## 5. Computational moving-map term

A variable compactification cannot be changed silently in a coefficient ODE. To distinguish it from physical L, write its scale as L_map and

    r=L_map sqrt(s)/[2(1-s)]^kappa,   0<s<1.

Then at fixed physical r

    partial_tau s = [kappa' log(2(1-s))-L_map'/L_map]
                    2s(1-s)/(1-s+2kappa s).                    (4)

This follows by differentiating log r=log L_map+(log s)/2-kappa log(2(1-s)); the coefficient of s' is 1/(2s)+kappa/(1-s). A changing-kappa representation rho(X)=E(q,kappa)(X) has derivative E_q q'+E_kappa kappa' at fixed X. Dropping the second term changes DR. An implementation can instead explicitly remap a physical-density time step to the new map, but must state that operation and check its error.

For a fixed map, xi=2s-1 satisfies dxi/dlog r=(1-xi^2)/[kappa+1/2+(kappa-1/2)xi], asymptotic to (1-xi)/kappa at infinity. This confirms only the leading compact radial speed quoted in the proposal. It does not establish a complete CFL condition for the nonlinear nonlocal discretization or stability of a time integrator.

## 6. Scope and verification

All statements above are identities or explicit criteria under their stated hypotheses. Convergence of DR, asymptotic stability of a candidate, behavior of its angular trace and a full-plane YES endpoint remain OPEN. Time-step stability, regridding accuracy and the canonical inverse require their own numerical checks. Exact polynomial gates can verify (2), (3) and the map derivative algebra; they do not turn a simulation into a proof. This audit uses no cluster, server, JavaScript, or formal build.
