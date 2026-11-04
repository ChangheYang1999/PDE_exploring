# Final local recheck of the joint strain singular set

Status: CONFIRMED A3259 after the complete 117-line existing A comparison and independent six-section disposition. This final-phase recheck covers the existing A476 local equality; neither A3249 nor A3255 had included it in its fresh scope.

## 1. Exact statement and notation

Fix 0<c<1, any finite real omega and T in R. Let J(y1,y2,y3)=(-y2,y1,0), A=cI-omega J and L=(1-c)I+omega J. Suppose U in C2(R3;R3) is bounded, P in C1(R3), and

    div U=0, LU+(DU)(Ay+U)+grad P=0.

For t<T let tau=T-t, s=-log tau, Q_s=exp(omega sJ), y=exp(sA)x and

    u(x,t)=tau^(c-1)Q_s U(y),
    xi=curl_x u=tau^-1 Q_s(curl U)(y),
    S_phys=(D_x u+D_x u^T)/2.

These fields solve physical Euler with pressure tau^(2c-2)P(y). All matrix norms below are Euclidean operator norms; lambda_max means the largest real eigenvalue of a symmetric matrix. On R3 minus {0} define

    Sigma_I={x_*: limsup_((x,t)->(x_*,T),t<T) tau||D_xu(x,t)||>0},
    Sigma_S={x_*: limsup_((x,t)->(x_*,T),t<T) tau lambda_max(S_phys(x,t))>=1}.

Then Sigma_I=Sigma_S. Both sets are invariant under exp(sigma A), for every real sigma. At every x_*!=0 the normalized joint strain limsup belongs to {0} union [1,infinity], with infinity allowed.

The assertion uses joint space-time limsups, not separate limits at fixed x. It needs no velocity decay, global bound on DU, pressure normalization, vorticity integrability, energy, helicity or symmetry assumption. Constants in the local proof may depend on x_*, its chosen neighborhood, compact initial C2 data, M=sup|U|, c and omega. It is not an assertion that the local Lipschitz failure set equals these sets, or that the threshold is 1+c/2, or that these sets are empty.

## 2. Complete characteristics and subcritical local vorticity

The exact rescaling gives |u(x,t)|<=M tau^(c-1) everywhere. If M=0 the theorem is immediate, so assume M>0. On every compact preterminal time interval u is locally Lipschitz in space and bounded globally by a finite function of time. A finite path cannot escape to infinity on that interval, so ordinary continuation gives complete physical characteristics there, without a global gradient bound. In particular a backward displacement from t to q is at most

    d(q,t)=(M/c)((T-q)^c-(T-t)^c).                              (1)

Let x_*!=0 lie outside Sigma_S. By the definition of joint limsup, choose a in (0,1), rho in (0,|x_*|/2) and t1<T such that

    lambda_max(S_phys(x,t))<=a/(T-t)
    on B(x_*,rho) times [t1,T).

Choose t1 later until (M/c)(T-t1)^c<rho/2. Every characteristic ending in B(x_*,rho/2) at t>=t1 stays in B(x_*,rho) back to t1. Along it, physical vorticity obeys

    (d/dt)|xi|^2=2 xi.S_phys xi<=2a(T-t)^-1|xi|^2.

Initial vorticity is bounded on the compact closure of B(x_*,rho). Integration therefore yields

    |xi(x,t)|<=C(T-t)^-a=:w(t) on B(x_*,rho/2).                 (2)

Since div u=0, the symmetric matrix S_phys has trace zero. Its two smaller eigenvalues are bounded below by -2a/tau, so ||S_phys||<=2a/tau. The skew part of Du has norm |xi|/2. Equation (2) and a<1 thus give, in the same neighborhood after another later starting time,

    ||D_xu||<=C1/tau=ell(t).                                   (3)

This is a derived local Type I estimate; it was not assumed globally.

## 3. A polynomial local Holder bound

Choose a fixed smooth cutoff chi0 supported in B(x_*,rho/2) and equal to one on B(x_*,3rho/8). Put v=BS(chi0 xi), where BS f=(-Delta)^-1 curl f, and h=u-v. In the interior, -Delta h=curl xi-curl(chi0 xi)=0. Thus h is harmonic; it need not be curl free because chi0 xi need not be divergence free. The degree-minus-two Biot-Savart kernel and (2) give |v|<=C_rho w. Harmonic interior estimates consequently bound Dh and D2h by C_rho Z, where

    Z(t)=M tau^(c-1)+w(t).

For a ball E with margin d inside B(x_*,rho/4), 0<d<=min(1,rho/32), local cancellation and a second cutoff give

    [D_xu]_(1/2,E)<=C_rho[xi]_(1/2,E+d)
       +C_rho w d^-1/2(1+|log d|)+C_rho Z.                    (4)

Here the degree-minus-three mean-zero kernel is bounded on Holder differences. The part supported beyond d has supremum C_rho w(1+|log d|) and derivative C_rho w/d; interpolation gives the displayed bound. The cutoff Holder cost is C_rho w d^-1/2. These facts also give the pointwise split used below. Only local C2 regularity is needed.

Take t0>=t1 late enough that tau0<=1 and (2M/c)tau0^c<=rho/16, with (M/c)tau0^c<=min(1,rho/32). For centers z in B(x_*,rho/16), use

    r0(t)=rho/16+(2M/c)tau^c,
    Theta_z(t)=[xi(t)]_(1/2,B(z,r0(t))),
    E0(t)=exp(integral_(t0)^t ell(q)dq).

These balls and all their required margins lie in B(x_*,rho/4). Backward paths ending there lie at earlier q in radius r0(t)+d(q,t), with remaining margin d since r0(q)=r0(t)+2d. Their joining segments stay in the same convex ball. For tau<=1, (1) gives d>=M(t-q). Bound their earlier separation by E0(t)/E0(q) times terminal separation, subtract xi'=(D_xu)xi and use (2)-(4). This yields

    Theta_z(t)<=E0(t)^1/2 Theta_z(t0)
      +integral_(t0)^t (E0(t)/E0(q))^1/2
       [(ell+C_rho w)Theta_z+C_rho w^2 ell1(t-q)+C_rho wZ](q)dq,
    ell1(v)=v^-1/2(1+|log v|).                                (5)

The margin is used only for q<t; its vanishing at q=t is harmless. These seminorms are Borel and bounded on compact preterminal intervals, because xi is C1 locally and the open balls vary continuously. Initial seminorms are uniformly bounded over z by compact C2 regularity.

Divide (5) by E0(t)^1/2. Since w,Z<=C/tau for tau<=1 and ell1 is integrable, its inhomogeneous integral is at most Ctau^-2. Since a<1, integral_(t0)^T w is finite. Integral Gronwall therefore gives, uniformly in z,

    Theta_z(t)<=C tau^-N, N=2+3C1/2.                          (6)

No terminal regularity, bounded global vorticity or prior Holder bound has been used.

## 4. Pointwise recovery and the joint equality

At each z in B(x_*,rho/16), localize xi inside B(z,rho/16), with cutoff equal to one near z and fixed positive margin. Its cutoff Holder seminorm is at most C_rho(Theta_z+w), by (6), and its supremum is at most w. Split the degree-minus-three derivative kernel at eta, with 0<eta smaller than the fixed margin. Cancellation inside eta, radial integration outside eta and the harmonic estimate in Section 3 give

    ||D_xu(z,t)||<=C_rho[eta^1/2(Theta_z+w)
                       +w(1+|log eta|)+Z].                  (7)

Take eta=tau^(2N+4), after restricting to sufficiently late times so it is below the margin. Equations (2),(6),(7) imply

    ||D_xu(z,t)||<=C[1+tau^-a(1+log(1/tau))+tau^(c-1)].

Consequently

    tau||D_xu(z,t)||<=C[tau+tau^(1-a)(1+log(1/tau))+tau^c] ->0

uniformly throughout this neighborhood. This proves x_* is outside Sigma_I, so Sigma_I is contained in Sigma_S. Conversely lambda_max(S_phys)<=||D_xu|| gives Sigma_S contained in Sigma_I directly. The equality follows. Trace zero makes lambda_max nonnegative; the same local argument shows that a normalized joint strain limsup below one is zero.

Finally S_phys=tau^-1 Q_s sym(DU(y))Q_s^T. For every real sigma, set x'=exp(-sigma A)x and tau'=exp(-sigma)tau. Then s'=s+sigma and y'=y. Both tau||D_xu|| and tau lambda_max(S_phys) are unchanged. This invertible continuous map carries joint terminal neighborhoods at x_* onto those at exp(-sigma A)x_*. It proves invariance for both signs of sigma and every omega, with no angular-mode or rational-angle restriction.

## 5. Dependencies and audit boundary

This proof uses only the full profile equation, exact physical transformation, ordinary complete-flow continuation under an integrable velocity bound, the explicitly derived local Biot-Savart estimates and finite-time Gronwall. The mathematical portion of the source GD.1 and Steps 3-5 is captured with exact identity in the team records. The global strain and scattering equivalences A3249 and pure scaling A3255 are adjacent results, not premises of this local proof.

The equality gives a local threshold of one. It does not say that every point in Sigma_I has growth faster than tau^(-1-c/2), and it does not identify Sigma_I pointwise with the local Lipschitz failure set. Those stronger formulations are outside this recheck. Uniform U decay is not needed here and would not make the sets automatically empty. This remains a conditional local description within an unresolved nonexistence problem. No computation or formalization is claimed; the configured model comparison is through existing working files, with provider runtime independently unattested.
