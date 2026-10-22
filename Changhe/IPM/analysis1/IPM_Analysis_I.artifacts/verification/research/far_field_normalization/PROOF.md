# Canonical scalar normalization, a growing far-field residual, and an exact repair

Status: analytical statements with independently computed scalar enclosures. This is a correction of trial normalization, not an existence theorem.

## Exact trial and canonical parameter

Let bar-rho be the exact X3 function with its stored exponent 0<k<1 and scale L>0. All its radial shape factors depend only on r/L: q=1-(1+(r/L)^2)^(-(1-k)/2), s=(r/L)^2/(1+(r/L)^2), chi=(r/L)^2/((r/L)^2+r_0^2), and S=sum_m chi^max(m-1,0) b_m(q) cos(2m theta)+s^(p/2)|cos(theta)|^(p-2) sin^2(theta) T(2q-1). Here p=6+2k/(2-k). The full formula is bar-rho=x^2y W_L exp(S). Define the residual convention F(rho,c_l)=(c_l X+U[rho]) dot grad(rho)-rho. Write c_0=psi[bar-rho]_{xy}(0). The independently audited scalar certificate proves

15.72608782162331 < c_0 < 15.72608782162370,
3/k-1-c_0 > 1.03009 times 10^{-8}.

Define the canonical normalized parameter c_l^can=(1+c_0)/3. It differs from the exponent-matched parameter c_l^tail=1/k. The parameter in this note is specified exactly by these definitions, not by a rounded decimal.

## Leading residual at infinity

For every fixed interior angle theta in (0,pi/2), the explicit X3 formula and its radial derivative give

bar-rho(r,theta)=r^k Theta_0(theta)+O(r^{2k-1}),
r bar-rho_r(r,theta)=k r^k Theta_0(theta)+O(r^{2k-1}),
Theta_0(theta)=L^{3-k} cos^2(theta)sin(theta) exp(S(1,theta))>0.

Indeed, 1-q=O(r^{k-1}); each spline is a polynomial on its last span with a finite one-sided derivative at q=1. The cutoff factors s and chi equal 1+O(r^{-2}). The base factor equals L^{3-k}r^{k-3}(1+O(r^{-2})). Composition and differentiation therefore give the two expansions. On any closed interior angular interval the bounds can be made uniform. The previously proved global velocity and gradient estimates give U=O(r^k) and grad(bar-rho)=O(r^{k-1}), so U dot grad(bar-rho)=O(r^{2k-1}).

It follows that the canonical normalized residual is

F_can(bar-rho)= (c_l^can k-1) r^k Theta_0(theta)+O(r^{2k-1}).

The coefficient c_l^can k-1=-(k/3)(3/k-1-c_0) is strictly negative by the scalar certificate. Since k>0 and 2k-1<k, F_can tends to minus infinity on every fixed interior ray. In particular,

sup_{R^2}|F_can(bar-rho)|=infinity.

This concerns the true canonical normalized residual of the stored density. It does not contradict finite sampled values or a bounded residual evaluated with c_l=1/k, which fails the exact central scalar relation. It also does not preclude a weighted forcing space allowing r^k growth or a slightly repaired trial.

At theta=pi/4 the leading coefficient is especially simple. If b_m(1) is the last spline coefficient and T(1) is the sum of the six Chebyshev coefficients, then

S(1,pi/4)=sum_m b_m(1) cos(m pi/2)+2^{-p/2} T(1),
Theta_0(pi/4)=L^{3-k} 2^{-3/2} exp(S(1,pi/4)).

The accompanying interval calculation encloses this coefficient directly from exact stored data.

## An exact one-parameter scalar repair

Hold k and all dimensionless X3 coefficients fixed. Put

c_target=3/k-1,
a=sqrt(c_target/c_0)>1,
L_star=aL,
rho_star(X)=a^3 bar-rho(X/a).

Equivalently rho_star is the same X3 formula with L replaced by L_star. Its center factor remains one. To check the canonical scaling explicitly, set psi_star(X)=a^4 bar-psi(X/a). Then -Delta psi_star=a^2 bar-rho_x(X/a)=partial_x rho_star, and its velocity is a^3 bar-U(X/a). Parity is unchanged and a^3 bar-U(X/a)=o(|X|); uniqueness in this class, proved in ../trial_regularities/PROOF.md, excludes any extra harmonic strain. Thus this is the canonical inverse and c_star=a^2 c_0=c_target. Thus the exact common parameter c_l=1/k satisfies both the central normalization and the leading tail relation for rho_star. The finite regularity and sublinear growth are preserved by this rescaling.

L_star is an exactly defined real number through the displayed scalar integral and positive square root. Its interval enclosure alone must not be mistaken for an exact choice of binary64 coefficient. Replacing L_star by a rounded approximation reintroduces a generally nonzero scalar mismatch. The JSON description records the exact definition and a certified enclosure separately.

This density rescaling is not a symmetry of the stationary nonlinear equation at fixed c_l. In fact, with Y=X/a,

F(rho_star,1/k)(X)=a^3 [F(bar-rho,1/k)(Y)+(a^2-1) bar-U(Y) dot grad(bar-rho)(Y)].

This identity follows from the exact scaling of the linear and quadratic terms. The repair enforces the scalar and leading-tail relations; a full residual norm must still be computed for the repaired trial.

## Explicit distance in the weighted factor norm

Write W_L(r)=(1+r^2/L^2)^{(k-3)/2}, bar-rho=x^2y W_L exp(S). Let C_m=max_i|c_{i,m}| over the spline coefficients including the first zero coefficient, Csum=sum_m C_m, C_T=sum_j|t_j|, and B_p=max_{0<=z<=1}z^{p-2}(1-z^2). These give the uniform bound M=exp(Csum+C_T B_p).

Let D_m bound |b'_m(q)| on [0,1]. The degree-seven spline derivative has degree-six B-spline coefficients

7(c_{i+1,m}-c_{i,m})/(knot_{i+8}-knot_{i+1}),

so their maximum absolute value is a valid D_m by nonnegative partition of unity. Define Q_1=1-k; the exact identity r q_r=(1-k)s(1-q) gives 0<=r q_r<=Q_1. Also 0<=r s_r=2s(1-s), and

|r partial_r chi^j|=2j chi^j(1-chi)<=1 for integer j>=1.

For the last inequality, the maximum is 2j^{j+1}/(j+1)^{j+1}; Bernoulli's inequality gives (1+1/j)^j>=2, so this maximum is at most j/(j+1)<1. For j=0 the derivative is zero.

Finally |T'_j(z)|<=j^2 on [-1,1]. To see this, write z=cos(theta), use T'_j(z)=j sin(jtheta)/sin(theta), and the finite geometric sum bound |sin(jtheta)|<=j|sin(theta)|; endpoint values follow by continuity. Put C_T'=sum_j j^2|t_j|. Differentiating the explicit radial factors now gives the global bound

|r S_r|<=Q_1 sum_m D_m + sum_{m>=2} C_m + B_p[p C_T+2Q_1 C_T'] = R_S.

Here the loose bound |r partial_r s^{p/2}|=p s^{p/2}(1-s)<=p is sufficient. Thus |partial_{log L} log(W_L exp(S))|<=H_1=(3-k)+R_S.

For t=log(a)>0, along scales L e^v, 0<=v<=t, one has W_{L e^v}/W_L<=exp((3-k)v). Integrating the scale derivative proves

sup |rho_star-bar-rho|/[x^2|y|W_L]
<= M H_1 t exp((3-k)t).

All constants in this bound are obtained from exact inputs with rational maxima and outward arithmetic in the companion script. An independent mpmath.iv calculation at 70 decimal digits, with no import from the Arb implementation, confirms the public bounds 7.65142460388744<L_star<7.65142460388754 and weighted factor distance <0.00001477. It independently parses all modes and six Chebyshev coefficients, checks their layout, and evaluates cos(2m*pi/4)=cos(m*pi/2) by its exact four-cycle. See evidence/independent_iv.json. The finite number is an explicit neighborhood size for this scalar repair. It is not a bound on the correction from a trial to an exact PDE solution.

## Dependencies and scope

The exact X3 scalar certificate, canonical inverse uniqueness, spline partition of unity, and trial growth are independently recorded in the preceding verification topics. The new conclusions are the unbounded unweighted canonical residual, the exact scalar-and-leading-tail repair, and its weighted factor distance. No inverse estimate or nonlinear closing inequality is supplied.
