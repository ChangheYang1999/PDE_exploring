# Conditional compactness at large slope and audit of proposed section 3.72

Status. Conditional theorem, not a profile existence or nonexistence result. Exact rescaling and the inverse bounds are proved in the companion results anisotropic_inverse_limit and anisotropic_weighted_hessian. This proof states their required hypotheses and proves the additional compactness consequence. All variables range over the whole plane. Write r=(xi^2+y^2)^(1/2), 0<gamma<1, and s in {1,-1}.

Let g_n be smooth, even in xi and odd in y, with g_n,y(0)=1. Suppose |g_n|<=C(1+r)^gamma, |grad g_n|<=C(1+r)^(gamma-1), |g_n,xixi|<=C(1+r)^(gamma-2) for the same C,gamma. Let eps_n>0 tend to zero and let V_n=(-Phi_n,y,Phi_n,xi) be the canonical parity-compatible sublinear velocity solving -Phi_n,yy-eps_n Phi_n,xixi=s g_n,xi. If g_n converge in C^2 on every compact set to g, the inverse theorem gives locally uniform convergence to s V_0[g], where

V_0,1(xi,y)=-int_y^infinity g_xi(xi,t)dt,
V_0,2(xi,y)=int_0^y t g_xixi(xi,t)dt+y int_y^infinity g_xixi(xi,t)dt (y>=0),

extended by the parities. Its growth is bounded by C'(1+r)^gamma, uniformly in n, and Phi_n,xiy(0) -> s int_0^infinity g_xixi(0,t)dt. To recall why the common majorants suffice for varying inputs, use the positive Poisson kernel P_a(z)=a/[pi(a^2+z^2)] and the oddness estimate |P_a*g_xi(xi,t)|<=C min((1+t)^(gamma-1), |xi|(1+t)^(gamma-2)). The other integrand is bounded by C(1+t)^(gamma-2), multiplied by min(y,t). These are integrable uniformly on compact (xi,y) sets. On a bounded t interval, C^2 local convergence and uniform global sup bounds control the Poisson convolution: split its xi integration into a fixed compact interval and its complement, whose kernel mass tends uniformly to zero as a->0. Then take the t tail to zero with the integrable majorant. This proves both velocity convergence and the strain limit. The formulas define the unique sublinear parity-compatible hydrostatic velocity since a homogeneous difference has potential y beta(xi), velocity (-beta,y beta'), and sublinearity on each vertical line forces beta'=0; odd beta then vanishes.

Suppose in addition ell_n -> ell and

(ell_n xi+V_n,1)g_n,xi+(ell_n y+V_n,2)g_n,y=g_n.

Products of locally uniformly convergent quantities converge locally uniformly. Thus g is C^2, has the parities, obeys all three bounds and g_y(0)=1, and solves the corresponding transport equation with ell and sV_0[g]. If the g_n came from exact profiles through x=sqrt(|a_n|)xi, rho_n=a_n g_n and eps_n=1/|a_n|, their centre identity passes to

s int_0^infinity g_xixi(0,t)dt=1-ell.

Now let J be a compact subset of (1,infinity). Fix C,gamma and finite positive constants C_R for integer R>=1. Assume that no hydrostatic solution of the preceding signed problem exists for any ell in J with these three bounds. There is then M such that no exact profile with ell in J and signed slope s a>=M has a rescaled representative satisfying the bounds and |D^3g|<=C_R on each radius-R disc. Otherwise choose a sequence with |a_n|->infinity. Compactness of J yields a convergent subsequence of ell_n. On each disc the density and gradient bounds control orders0,1. The second-derivative bound in just the xi direction does not control all second derivatives, but the local D^3 bound and the gradient bound do: on a slightly larger disc, apply the one-dimensional Taylor formula to each first derivative on a fixed short line segment in each coordinate direction. If |f|<=A and |f''|<=B along the segment, |f'(0)|<=2A/h+Bh/2 for fixed h>0. Here f is a first derivative of g. Thus all second derivatives are uniformly bounded on each disc, and the D^3 bound makes them uniformly Lipschitz. Arzela-Ascoli followed by a diagonal subsequence gives C^2 local convergence, and the limit just proved contradicts hydrostatic nonexistence. This fills the uniform C^2-bound detail implicit in the proposed report's Arzela-Ascoli sentence. No such hydrostatic nonexistence or common bounds for profile sequences have been proved.

The second divergence example in 3.72(c) can also be checked directly. Put g=(1+xi^2)^(-1) f(y), f(y)=y(1+y^2)^((gamma-2)/2). The xi Fourier transform of (1+xi^2)^(-1) is pi exp(-|k|), with inverse factor1/(2pi). The half-plane Green derivative at y=0 is exp(-sqrt(eps)|k|t). Therefore for s=1 the strain is -2 int_0^infinity f(t)/(1+sqrt(eps)t)^3 dt. On substituting t=v/sqrt(eps), eps^(gamma/2)c_eps tends to -2 int_0^infinity v^(gamma-1)/(1+v)^3 dv=-2B(gamma,3-gamma). Dominated convergence follows because the substituted numerator is bounded above by v^(gamma-1), which is integrable with the denominator at both endpoints. This nonprofile has the original density and gradient bounds but not the extra weighted xi Hessian bound; its divergence does not contradict the compactness theorem.

Audit verdicts for the proposed text: (a) CONFIRMED exact signed coordinate transformation, cubic relation 6E=(s-2A eps)B and fixed-eps gauge uniqueness; (b) CONFIRMED distributional stratified nonprofile and failure of the global gradient bound; (c) CONFIRMED both inverse counterexamples and constants; (d) CONFIRMED with the common weighted Hessian hypothesis; (e) CONFIRMED conditional compactness and contrapositive, with the elementary second-derivative estimate above. For negative slopes the formulas must explicitly use -V_0[g] and minus the strain integral. This is a signed formula correction/clarification, not a new theorem.

Numerical normalization paragraph: for the dilation rho_l(X)=l rho(X/l), K_l=l^(1-p)K and b_l=b/l^2, e_l=e/l^2. At ell=3 and K=10 the length making K_l=a is l=(a/10)^(3/2), NOT (10/a)^(3/2). If the reciprocal lambda is used, rho_new(X)=rho(lambda X)/lambda must be stated. The reported B,E equal b/l^2 and e/(a l^2) and can be recomputed from this lane's previously verified exact-jet data. Half-widths and sampled box differences in the initial paragraph are only producer computations until separately re-evaluated. A finite five-grid sequence whose jet increments decrease does not exclude convergence; say that the coefficients have not stabilized at those sizes. No inference to a stratified limit follows from these data.

## Revised text audit at 2026-10-21T07:56:50.031335+00:00

The repaired 07:55 text implements the signed negative-slope condition, the correct dilation length, fixed common bounds, C2 compactness, and the limited regularity of the limiting stream. These changes are CONFIRMED by the argument above. One new minor identity is REFUTED as an equality. For the positive half-line Green kernel D_q, write u=exp(-qy). Splitting its y derivative at t=y gives

int_0^infinity |partial_y D_q(y,t)| dt
= exp(-qy)(cosh(qy)-1)/q + exp(-qy)cosh(qy)/q
= (1-u+u^2)/q <= 1/q.

The text states equality with 1/q. Equality holds at y=0, and is strict for finite y>0. The needed inequality is valid, so the boundedness and canonical uniqueness arguments survive unchanged. The other kernel integral is (1-exp(-qy))/q^2 <= q^-2. No endpoint claim follows. Frozen repaired texts are in verification/revised0755/. The density-width and box audit is a separate calculation, result179.
