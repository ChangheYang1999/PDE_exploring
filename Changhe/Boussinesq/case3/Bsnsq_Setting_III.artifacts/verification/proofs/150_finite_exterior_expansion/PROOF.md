# Finite exterior expansions forced by the profile equations

Status: CONFIRMED finite exterior expansion theorem and its applications to class A profiles and the configurations of135. The theorem assumes full spatial symbol bounds; those hypotheses are independently checked for each stated application below. A vanishing dipole is a necessary condition only. No nonexistence endpoint is asserted.

## 1. Statement and notation

Fix beta>2 and put s=1/beta, m=1-2s. For an exterior smooth function, write f in S^a when, for every integer j>=0, |D^j f(X)|<=C_j r^(a-j) on all sufficiently large circles, uniformly in angle. Constants may depend on j. Vector and tensor bounds have the same meaning. Let smooth whole-plane fields have Psi odd in x, Theta even in x, Omega=-Delta Psi, V=(-Psi_y,Psi_x), V(0)=0, and let V be the canonical once-subtracted full-plane inverse. Assume

    Omega in S^-s, V in S^(1-s), Theta in S^m.            (1)

Assume both equations

    (beta X+V).gradOmega+Omega=Theta_x,
    (beta X+V).gradTheta=(beta-2)Theta                    (2)

hold outside a fixed ball. The equations need not hold on its interior for this theorem.

Then there are finite exterior sums P,H of smooth angular coefficients times r^e times polynomials in log r, such that

    Psi-P in S^(2-mu), Theta-H in S^(1-s-mu)             (3)

for some mu with 3<mu<4. Stream exponents in P belong to {2-Ks-n: K>=1,n>=0 integers}, together with homogeneous harmonic terms of degrees1 and-1. Temperature exponents in H belong to {1-Ls-n: L>=2,n>=0 integers}. All logarithmic indices are nonnegative integers. P can be chosen odd in x and H even. Consequently (3) implies exactly the remainders required in149: Psi-P=o(r^-1), D(Psi-P)=o(r^-2), D²(Psi-P)=o(r^-3), Theta-H=o(r^-2).

No coefficient is freely added to the inverse. In particular the harmonic coefficients are extracted from the actual field. The degree1 term is an exterior constant velocity, not a newly imposed strain or observer drift. The degree-1 term is the actual exterior dipole coefficient. This theorem only supplies a finite expansion at the stated depth, not convergence of an infinite formal series.

The smooth residual f=(beta X+V).gradOmega+Omega-Theta_x is compactly supported because the vorticity equation holds outside a ball. If exact thermal transport holds also in the interior, combining this theorem with149 gives, whenever beta has reduced rational denominator greater than3 or is irrational,

    integral x f=2pi(1-3beta)D,

where D is the coefficient of x/r² in P. For a profile f=0, this implies D=0. This is a necessary scalar identity and does not rule out a profile.

## 2. Leading coefficients follow by radial integration

Holding the polar angle fixed, (2) becomes

    (beta r partial_r+1)Omega=-V.gradOmega+Theta_x,
    (beta r partial_r-(beta-2))Theta=-V.gradTheta.

By (1) the two right sides belong to S^-2s and S^(1-3s). Therefore

    partial_logr(r^s Omega) in S^-s,
    partial_logr(r^-m Theta) in S^-s.

Here the S notation for these cylindrical expressions means every angular and log-radius derivative has the displayed radial bound. Integrating from r to infinity and differentiating the absolutely convergent integrals in angle gives smooth angular limits a,A and

    Omega=r^-s a+S^-2s,
    Theta=r^m A+S^(m-s).                               (4)

For radial derivatives the equations give the same bounds directly, and repeated differentiation of the integrable right sides gives every cylindrical derivative. Cartesian derivatives follow from the polar differentiation formulas on annuli. The remainders in(4) therefore are full spatial symbols, not just angular bounds. Parity gives a odd and A even under theta->pi-theta.

## 3. Whole-plane Poisson remainder estimate

We first prove the following elementary estimate. Let rho be smooth and odd in x, rho in S^-mu outside a ball, with 0<mu<4 and mu different from1 and3. Let Z be its canonical relative stream, so -Delta Z=rho, grad Z(0)=0 and Z odd. Its velocity is sublinear. Then:

- if0<mu<1, Z belongs to S^(2-mu);
- if1<mu<3, Z=Cx+Z_rem with Z_rem in S^(2-mu);
- if3<mu<4, Z=Cx+D x/r²+Z_rem on the exterior, with Z_rem in S^(2-mu).

The C,D are determined by rho and the center normalization. For mu>1, C=-(1/(2pi))integral Y_1 rho(Y)/|Y|² dY, which is absolutely convergent. In the last case D=(1/(2pi))integral x rho, also absolutely convergent. For mu<1 a genuine linear term can occur, for example for compact rho, but is absorbed in S^(2-mu); no divergence of the center integral is asserted.

Use G(z)=-(1/(2pi))log|z|. The twice-subtracted stream kernel

    G(X-Y)-G(-Y)-gradG(-Y).X

is absolutely integrable at infinity against rho for every mu>0, because the far kernel is O(r²/|Y|²). At Y=0 its gradient subtraction is locally integrable against smooth rho; at Y=X the logarithm is locally integrable. It gives the canonical relative stream. To verify its sublinear velocity bound, split the once-subtracted gradient kernel into |Y|<2r and |Y|>2r and a ball near X. These estimates give O(r^(1-mu)) for mu<1 and O(1)+O(r^(1-mu)) for mu>1, with harmless constants from bounded Y; all are sublinear. These are only sublinearity bounds: at mu=2 a direct intermediate estimate r^-1 log r is harmlessly absorbed in O(1). The difference from any other specified sublinear solution has entire harmonic gradient components and is zero at0, so the harmonic gradient estimate on growing disks makes the difference zero. Oddness removes the stream constant.

For0<mu<1, split at |Y|=r/2 and2r. On centered radial regions the integrals of rho times log r or log|Y| vanish by x-oddness. On the inner region, the log kernel after subtracting log r is O(|Y|/r), giving

    r^-1 integral_0^(r/2) t²(1+t)^-mu dt=O(r^(2-mu)).

The linear subtraction is bounded by

    r integral_0^(2r) (1+t)^-mu dt=O(r^(2-mu)).

The middle region is bounded after scaling Y=rZ and using the integrability of log|e-Z| on fixed annuli; the subtraction has the same bound. On the outer region the second-order kernel gives

    r² integral_(2r)^infinity t^(-1-mu)dt=O(r^(2-mu)).

This proves the zeroth-order stream bound.

For mu>1, the center-gradient integral is absolutely convergent. Extract its fixed linear term Cx and define the remaining potential directly by the kernel G(X-Y)-G(-Y). On centered radial regions the integral of G(-Y) against odd rho vanishes; its subtraction makes the far integrand absolutely integrable: |G(X-Y)-G(-Y)|<=Cr/|Y| for |Y|>2r. The far contribution is at most

    r integral_(2r)^infinity t^-mu dt=O(r^(2-mu)).

For1<mu<3 the inner first-multipole estimate above gives O(r^(2-mu)); its bounded-inner contribution is O(r^-1), smaller than this power. The middle region has the same scaled logarithmic estimate. This proves the second case, including mu=2; the absent zeroth angular mode avoids a logarithmic monopole.

For3<mu<4 the first moment integral is absolutely convergent. Subtract from the potential its full first multipole

    (1/(2pi r)) e.integral Y rho(Y)dY = D x/r².

The y moment is zero by oddness in x. On |Y|<r/2 the remaining kernel is O(|Y|²/r²), giving

    r^-2 integral_0^(r/2) t³(1+t)^-mu dt=O(r^(2-mu)).

On the middle annulus both the logarithmic integral and the subtracted multipole are O(r^(2-mu)). On |Y|>2r the logarithmic contribution has the previous bound, and the omitted part of the full multipole is bounded by

    r^-1 integral_(2r)^infinity t^(2-mu)dt=O(r^(2-mu)).

These estimates prove the third case and its coefficient sign.

The full derivative bounds follow locally. On a ball of radius comparable to r centered at X, subtract the harmonic terms already extracted, rescale to a unit ball and use a cutoff Newton potential for the right side rho. For order j>=1, a derivative of this Newton potential can be written as a first derivative of G convolved with j-1 derivatives of the smooth compact source. The first derivative kernel is locally integrable; the zeroth order uses the locally integrable logarithm. These formulas give bounds through every fixed order from the source symbol bounds. The remaining harmonic function has all derivative bounds from its supremum on a slightly larger ball. The just-proved stream bound and the symbol bounds of rho therefore give |D^j Z_rem|<=C_j r^(2-mu-j). This proves the Poisson estimate with all derivatives, without any artificial box boundary.

## 4. Inverting finite powers and logarithms

For e real, t=log r and a finite polynomial Q(t,theta),

    Delta(r^e Q)=r^(e-2)[(partial_theta²+e²)Q
                                      +2e partial_t Q+partial_t² Q].

Given an odd smooth-angular polynomial source r^(e-2) B(t,theta), there is an odd finite polynomial Q with -Delta(r^eQ)=r^(e-2)B. To prove this, split the angular functions into the kernel of L_e=partial_theta²+e² and its orthogonal complement. On the complement L_e is invertible on smooth periodic functions. Solving for the log coefficients from highest to lowest gives a finite polynomial solution. Smoothness follows, for example, from the Fourier coefficients divided by e²-k², which preserve rapid decay away from the finitely many kernel modes.

If the kernel is nonzero and e!=0, its equation is

    (partial_t²+2e partial_t)Q_kernel=-B_kernel.

For every polynomial right side, first solve (partial_t+2e)P=-B_kernel in polynomials by descending coefficients, and then integrate P to obtain Q_kernel. This adds at most one log power. If e=0 the angular kernel consists of constants; it has no odd-in-x component. Thus the kernel case at e=0 is absent. This proves the claim for every required exponent. The inversion commutes with the x-reflection, so the odd subspace is preserved. Fix each resonant particular solution by setting its constant-in-log angular-kernel coefficient to zero. A homogeneous harmonic summand can then be assigned separately, without logs; this convention also applies at degrees1 and-1.

To transfer a vorticity expansion to a stream expansion, solve each of its finitely many terms this way, multiply the resulting particular stream by a common radial cutoff equal1 outside a large ball and identically0 on a neighborhood of0, and subtract it from the actual Psi. Its new smooth vorticity equals the residual source on the exterior and is compactly altered in the interior. Every particular stream exponent is less than2, so its velocity is sublinear even with finitely many logarithms. The cutoff makes its gradient vanish near0. Since V(0)=0 was assumed for the actual field, subtracting the cutoff particular preserves zero center gradient. The remaining field is therefore exactly the canonical relative inverse of its new source by the uniqueness argument in section3, without any added observer drift. Apply the Poisson remainder estimate and extract its harmonic Cx and, when mu>3, D x/r². Every coefficient is obtained from the actual field and the specified cutoff construction. Combine all terms having equal radial exponent and logarithmic degree. The total expansion coefficients above a common remainder threshold are unique: if their finite difference had a nonzero highest exponent, its highest nonzero logarithmic coefficient at some fixed angle would grow relative to the strictly lower remainder power, a contradiction. Repeat downward through the finite list. Although intermediate particular solutions and harmonic extractions depend on the cutoff convention, the resulting combined coefficients at the retained depths do not. Outside the exceptional beta set, no ordinary stream exponent is-1; the isolated D then is the actual dipole coefficient. At exceptional beta the log-free harmonic projection is fixed by the convention above, but further degree-1 terms can enter149 and cannot be discarded.

## 5. One simultaneous improvement of both scalar expansions

Define the locally finite exponent set

    E={Ks+n: K>=1,n>=0 integers}.

Local finiteness holds because s>0. Suppose s<mu<4, mu not in E and mu not equal1 or3, and that we already have finite expansions

    Omega=O_fin+R_O, R_O in S^-mu,
    Theta=T_fin+R_T, R_T in S^(1-s-mu),                 (5)

with vorticity degrees -Ks-n and temperature degrees1-Ls-n,L>=2. Retain only terms above the corresponding remainder thresholds. All log indices are nonnegative integers. The leading terms are those of(4).

Section4 and then section3 give

    Psi=P_fin+R_P, R_P in S^(2-mu),
    V=V_fin+R_V, R_V in S^(1-mu), V_fin=gradperp P_fin. (6)

The appended harmonic degrees are1, and-1 if mu>3. Bounds for the actual fields and the stronger remainders in(5)-(6) show that O_fin belongs to S^-s, T_fin to S^m and V_fin to S^(1-s), even though lower-order terms may contain logarithms. The leading scalar transport exponents are never resonantly forced, and the leading stream exponent2-s is noninteger and nonresonant, so these leading terms have no logarithms. Lower exponents with logarithms remain bounded at the critical powers by their strict gaps. These critical bounds are enough to avoid logarithmic losses in the following errors:

    -V.gradOmega+Theta_x
      =-V_fin.grad O_fin+partial_x T_fin+S^(-mu-s),
    -V.gradTheta
      =-V_fin.grad T_fin+S^(1-mu-2s).                  (7)

For example R_V.gradOmega has degree1-mu-s-1=-mu-s; V_fin.gradR_O has the same degree, and partial_x R_T also has that degree. The two temperature errors have degree1-mu-2s. Differentiating products gives the same symbol bounds at every order.

The finite expressions on the right of(7) are powers times log polynomials. The stream main degree2-Ks-n has velocity degree1-Ks-n. Pairing it with a vorticity derivative yields -(K+K')s-(n+n'), with K+K'>=2. Differentiating temperature yields -Ls-n,L>=2. A degree1 harmonic velocity adds one integer to the vorticity index n; a degree-1 harmonic velocity adds three. All these forcing degrees are strictly less than-s and belong to -E. The temperature products have degrees1-(K+L)s-(n+n'), K+L>=3, or have the integer index increased by1 or3 by a harmonic velocity. They are strictly less than m and belong to the permitted temperature family. Logarithmic differentiation preserves the degrees.

Every scalar Euler equation can now be integrated term by term. For a vorticity forcing r^q B(log r,theta) with q<-s, the polynomial equation for its particular solution is

    (1+beta q)Q+beta partial_t Q=B.

Its constant coefficient is nonzero, so descending polynomial coefficients gives a unique finite polynomial Q. The analogous temperature coefficient is beta(h-m), nonzero since h<m. No new transport resonance occurs below the leading degrees. Both actual leading angular coefficients in(4) fix the integration constants. For the remainder use the integral from infinity: if (beta r partial_r+1)u belongs to S^-nu, nu>s, and r^s u tends to0, then

    u(r,theta)=-(r^-s/beta) integral_r^infinity t^(s-1)g(t,theta)dt

belongs to S^-nu. The temperature formula is the same after replacing its critical degree by m. Apply this to(7), with nu=mu+s for vorticity. It gives the improved finite expansions with remainders S^(-mu-s) and S^(1-mu-2s), before discarding any lower terms.

Choose any mu' strictly between mu and mu+s, below4, avoiding E,1,3. Discard all finite terms with degree below the new thresholds -mu' and1-s-mu'. Such terms, including their finitely many logarithms, belong to the respective new symbol remainders because there is a strict positive gap. No term is exactly at a threshold, by the avoidance of E. This proves(5) with mu' in place of mu.

## 6. Finitely many improvements give the required depth

Start from(4) with any mu0 strictly between s and2s, avoiding E,1,3. This is possible since the avoided set is locally finite. For every step before reaching3, choose mu' in (mu+s/3,mu+2s/3), still below4 and outside the avoided set. There is always such a choice. After finitely many steps the weight lies strictly between3 and4; if a selected step would hit3 it is excluded and another point is chosen. Since s<1/2, no final overshoot can reach4. Apply section4 at this final weight to obtain P,H and(3).

The construction preserves parity at every step and retains only finitely many powers and logarithmic coefficients. The harmonic terms at the final weight are Cx and D x/r²; they are allowed terms in149. The remainder exponent2-mu<-1 and the temperature remainder exponent1-s-mu<-2 give all stated little-o estimates, uniformly in angle. This proves the conditional symbol-class theorem.

## 7. Class A and compact-residual applications; scope

The argument uses the full spatial symbol bounds(1), not merely the undifferentiated tail or angular convergence. It supplies a finite expansion for exact exterior solutions satisfying those bounds, including sign-changing fields. It does not assign the dipole sign or prove it nonzero. It does not show that the entire series converges, and it gives no uniform estimates as beta tends to2 or infinity.

For the class A application, work with the relative physical fields in the translated material observer:

    u_tau(z)=tau^(beta-1)V(tau^-beta z),
    omega_tau(z)=tau^-1 Omega(tau^-beta z),
    theta_tau(z)=tau^(beta-2)Theta(tau^-beta z).

Direct differentiation with physical time t=-tau gives omega_t+u.gradomega=theta_x, theta_t+u.gradtheta=0, div u=0 and partial_y u_1-partial_x u_2=omega. These are precisely the equations in36. This does not set the absolute observer's U(0) to zero or turn B2 into B1; it uses the required relative velocity U-U(0). No velocity time-derivative bound is required.

Packet36 proves all local spatial derivatives of these physical fields bounded on each fixed annulus, from its verified base estimates and local uniform limits. On 1<=|z|<=2 set r=tau^-beta. For every multi-index alpha of length j, the three exact derivative scaling identities are

    D_z^alpha omega_tau(z)=r^(s+j)(D^alpha Omega)(rz),
    D_z^alpha theta_tau(z)=r^(-m+j)(D^alpha Theta)(rz),
    D_z^alpha u_tau(z)=r^(s-1+j)(D^alpha V)(rz).

Their bounds give exactly(1), for every fixed j. A late-time interval and bound depending on j are sufficient, since each symbol estimate allows its own constant and exterior radius. The common-cutoff elliptic estimate, k=2 transport starting step, local induction and spatial compactness proof in36 were reread independently for this application. The earlier actual Opus27 review remains recorded there. A fresh actual Opus223 request returned no written audit (service stop_reason refusal), so it supplies no additional endorsement. No infinite time-Taylor expansion or analytic regularity is inferred.

This checked dependency proves the class A corollary: every class A B2 profile with beta>2 has the finite expansions in(3). For beta outside Z={M/N>2: M,N coprime positive integers, N<=3}, its actual exterior dipole coefficient is D=0 by149. Nothing in this argument makes D nonzero, and no existence or nonexistence conclusion follows.

The configurations in135 also satisfy the hypotheses directly. Its precise theorem gives, for every order j, the three symbol bounds(1), the canonical relative velocity, global thermal transport, and the vorticity equation outside8R. Its high-order argument first proves smoothness at one fixed gluing radius using uniform estimates on its iterates, then removes the intermediate epsilon loss by commuting Cartesian derivatives in the fixed-point transport equations. The gains are s-2epsilon=s/2>0. The inverse estimate and the transported trace give the corresponding full velocity and temperature symbols. These statements and their proofs have been reread independently. If the stream in135 retains the absolute linear gauge l x, apply the present theorem to Psi_rel=Psi-l x, where l=Psi_x(0); then grad_perp Psi_rel=V and grad Psi_rel(0)=0. This is the required relative field, and does not alter Omega or f. Thus the expansions hold for every configuration in135, and, outside Z, its compact residual satisfies integral x f=2pi(1-3beta)D. This proves a formula for its actual dipole, not a claim that its residual or dipole vanishes. Sign-changing variants require their own existence and symbol hypotheses, rather than an implicit positivity extension.

Dependencies: whole-plane subtracted logarithmic inverse and harmonic uniqueness; oddness, kernel Taylor bounds and localized harmonic derivative estimates; elementary periodic Fourier inversion; radial Euler integration; finite induction. The class A application uses36; the compact-residual application uses135; the dipole identity uses149. These are conditional necessary statements for the stated fields, not a decisive endpoint.

Independent audit: all estimates above were checked against the full hypotheses, including the center gauge, derivative symbols, finite exponent closure, logarithmic resonances and fixed-angle coefficient uniqueness. The 82 independent controls are recorded in verification/SUMMARY.md. Actual Opus220 and222 supplied complete written Poisson audits;222 withdrew objections after checking the full theorem header and the bound at mu=2. Actual Opus221 gave a written positive verdict on the induction conditional on the Poisson lemma, but its response was truncated before completing the requested exposition. Its listed clarifications are supplied explicitly in sections4,5 and7. The follow-up224 returned no audit text, so no complete follow-up endorsement is claimed. The verifier's complete argument supplies the final verdict; numerical controls and partial model text are not substituted for a proof.

Initial complete proposed proof saved UTC 2026-10-21T09:07:00.778943+00:00.

Audit revisions saved UTC 2026-10-21T09:18:42.610783+00:00. Final independent verification completed UTC 2026-10-21T09:23:55.302509+00:00.
