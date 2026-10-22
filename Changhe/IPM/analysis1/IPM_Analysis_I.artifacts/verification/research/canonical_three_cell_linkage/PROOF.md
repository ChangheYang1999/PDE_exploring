# Canonical meaning of the three accepted radial Taylor models

Status at creation: proof and acceptance criterion, OPEN until the source bindings and independent review pass. This proof precedes its checker.

## Exact statement and hypotheses

Use the exact normalized modal_v2 trial defined by data_exact/modal_v2.json, SHA256 57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6, with the canonical inverse and normalization of topics15 and21. Let t=log r. On the middle spline annulus write

rho(r,theta)=r^3 sum_(j=0)^261 H_j(t) sin((2j+1)theta)
            =r^3 cos(theta)^2 sin(theta) sum_(m=0)^259 a_m(t) cos(2m theta).

There is no halving of the zero cosine coefficient. Each a_m is the exact degree-seven spline from that trial. For each original span [a,b], assume the archive original_knots.jsonl.gz, SHA256 c762afdbea381b750f2c9e382ef2315b2652df9781ccf69511237d944e102648, contains the canonical scaled moment values I_n(a) and J_n(b), 1<=n<=261, in its declared balls. This is the remaining open canonical numerical hypothesis. Membership of the archive's H polynomial coefficients is already proved by accepted topic99 and is not an additional open hypothesis.

Take the three saved candidate NPZ files selected_v3_cell_0000.npz, selected_v3_cell_4102.npz and selected_v3_cell_7808.npz of topic93. Assume their hashes and every inherited acceptance dependency of topics93,98,99 remain unchanged. The candidate arrays P_mid,P_rad,P_rem and R_mid,R_rad,R_rem have exactly the finite-input, whole-box interpretation proved in topic93, with all its mandatory addenda, especially its order20 remainder refinement. Set Q=12. For cell c in {0,4102,7808}, let [t_c,t_(c+1)] be its exact rational interval in partition_exact.json, u=t-t_c and h0=t_(c+1)-t_c.

The conclusion is that, for every mode n=1,...,261 and every u in [0,h0],

P_n(t_c+u)=2n psi_n(exp(t_c+u))/exp(2(t_c+u)),
R_n(t_c+u)=psi_n'(exp(t_c+u))/exp(t_c+u)

belong to the corresponding saved degree12 coefficient-interval polynomial plus the saved symmetric remainder interval of topic93. The prime in psi_n' is the radial derivative. The coefficient intervals also contain the exact Taylor coefficients at u=0. No other cell is concluded here. These are the saved current-runtime candidate arrays, not a claim of identity with the historical numerical flow run.

## Canonical Green identities

The canonical scaled moments obey

I_n'=-(2n+4)I_n+H_(n-1),
J_n'=(2n-4)J_n-H_n,
psi_n(r)=r^4 [J_n(log r)-I_n(log r)]/2.

Their canonical integral definitions fix the homogeneous constants. These definitions and the finiteness and normalization of the modal trial are the accepted analytic dependencies of topics21 and98. Put S_n=(H_(n-1)+H_n)/2 and

A_n(t)=exp(4t)[S_n(t)-2n I_n(t)],
B_n(t)=exp(4t)[2n J_n(t)-S_n(t)],
F_n(t)=[(4-2n)H_(n-1)+(4+2n)H_n+H'_(n-1)+H'_n]/2.

Direct differentiation using the preceding two moment equations gives

A_n'=-2n A_n+exp(4t) F_n,
B_n'= 2n B_n-exp(4t) F_n.

Also A_n+B_n=4n psi_n and, by differentiating the displayed formula for psi_n, B_n-A_n=2r psi_n'. Thus, with E=exp(t_c),

q_+(u)=B_n(t_c+u)/(E^2 exp(2u)),
q_-(u)=A_n(t_c+u)/(E^2 exp(2u)),
P_n=(q_++q_-)/2, R_n=(q_+-q_-)/2

satisfy exactly

q_+'=(2n-2)q_+-E^2 exp(2u) F_n(t_c+u), q_+(0)=B_n(t_c)/E^2,
q_-'=-(2n+2)q_-+E^2 exp(2u) F_n(t_c+u), q_-(0)=A_n(t_c)/E^2.

These are the finite-input ODEs of topic93. Their constants and signs have been derived here independently. Existence and uniqueness follow explicitly from variation of constants for scalar linear ODEs with polynomial times exponential forcing. Consequently a solution with these canonical inputs is the restriction of the canonical Green solution, with no freedom to add a homogeneous mode.

## Complete input correspondence

The accepted topic99 result proves that the exact coefficients in

a_m(t_c+u)=sum_(k=0)^7 T_(c,k,m) u^k

belong to the target T_mid[c,k,m] plus or minus T_rad[c,k,m] in the fixed cert_green.npz, SHA256 c2c2e4f73f5ac6ee49fd0052b81700fc88ee68d01a5a526691cf03c2b82c2ef1. It proves all7809 cells, all8 powers and all260 modes, on the exact child partition. Topic98 proves membership of canonical dimensional A_n(t_c),B_n(t_c) in the A/B boxes in that same file, at all7810 exact boundaries and261 modes, conditional on the archive moment hypothesis above. The checker below must compare every entry of the selected topic93 T,A,B arrays directly with those actual source slices; common file names alone do not suffice.

The exact cell coordinates are the rational equal subdivisions of their stated original knot span. The selected interval never crosses an original knot. The saved h in the topic93 scalar array is a positive upper bound on h0. The saved E interval contains exp(t_c) and is strictly positive. These facts were already checked in topic93 and topic75; the present audit rechecks them at all three cells with exact rational geometry and two directed exponential methods. The entire saved scalar vector is compared byte for byte with the scalar input of topic93. No rounded midpoint is substituted for t_c.

For clarity, there is no extra independent canonical forcing-box hypothesis. The identities

H_0=(2a_0-a_2)/8,
H_1=(2a_0+a_1-a_2-a_3)/8,
H_j=(a_(j-1)+a_j-a_(j+1)-a_(j+2))/8, j>=2,

with a_m=0 outside0<=m<=259, follow from the four signed sine frequencies in cos(theta)^2 sin(theta) cos(2m theta). Substitution into the displayed formula for F_n gives a rational linear map from all T coefficients to F coefficients. At power k, the derivative contributions multiply T_(k+1,m) by k+1, and vanish at k=7. Collect repeated T symbols first. For a collected scalar linear form sum w_l x_l on the product of input intervals [m_l-r_l,m_l+r_l], its exact image is

[sum w_l m_l - sum |w_l|r_l, sum w_l m_l + sum |w_l|r_l].

The exact image formula follows by choosing each independent x_l endpoint according to the sign of w_l, and by the triangle inequality for all intermediate choices. Topic93 checked that this whole image lies in each saved F interval. The present checker independently repeats all6264 containments using the explicit collected H identities above, instead of topic93's signed-frequency construction. In particular componentwise T membership is sufficient; no independence of actual spline errors or of A/B/T values is assumed. The whole-input-box theorem encloses any correlated canonical point in that product.

Now select the actual canonical coefficients, A/B values and E, all members of their identified input boxes. Topic93 applies to this choice and bounds the ODE solution on [0,h], hence on [0,h0]. The canonical ODE identities and uniqueness identify that solution with P_n,R_n above. This proves the stated conclusion. The artificial overhang [h0,h] uses only the polynomial extension in topic93 and makes no claim about the true spline beyond this cell.

## Evidence and scope

This result is a composition of previously independently verified finite lemmas plus a new exact artifact and coordinate audit. It does not rerun the complete coefficient and remainder calculations of topic93 or the full computations of topics98 and99. The new checker must verify every current pin of those three accepted verdicts, the expected verdict hashes, all input identities, all selected coordinate and E containments and all6264 whole-box F images. A separate actual Opus5.5 review of this proof, the new code and the actual output must be read and adjudicated before final acceptance.

The only remaining open canonical input membership here is that the specified archive I_n(a),J_n(b) balls contain the canonical moments. This wording retains the accepted analytic definitions, the exact normalized modal trial and the trusted arithmetic execution of the cited results. It does not assert a second independent integration of those moments or an enclosure of the original X3 profile. No angular cell calculation, spatial range or classification, physical residual derivative, other7806 radial cells, full-field inequality, global inverse, nonlinear closure, X3-distance estimate or decisive IPM endpoint follows.
