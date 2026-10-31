# Coefficient derivative of the fixed discrete weighted residual

Status: proved finite-dimensional identity under the stated active-set hypotheses. This is not a convergence theorem for the pressure discretization.

## Statement and notation

Fix 2/5<c<1/2, w>0 and R0>0. Fix finitely many positive radial nodes r_j, angular nodes n_a, positive angular weights b_a, positive row weights q_j, and a shell-mean matrix M with nonnegative entries. A nonempty row of M has sum one; an empty row is zero. Fix a linear pressure-gradient map K from scalar source samples on a subset of these nodes to vectors on every evaluation node. All these quantities are independent of the scalar coefficient coordinate t. The field representation and the tail constraints are linear in coefficients at fixed c,w. Thus, for a fixed coefficient direction,

U(t)=U+tV, D U(t)=D U+tD V, L U(t)=L U+tL V,

where L is the rotating linear momentum operator of stable_linear_operator/PROOF.md. Let J(x1,x2,x3)=(-x2,x1,0), y_ja=r_j n_a, and define

T1=(1-c)U, T2=c D U y, T3=w(JU-D U Jy), T4=D U U,

f=tr((D U)^2), T5=K f, R=L U+T4+T5.

The derivative at t=0 is

f'=2 tr(D U D V), T4'=D V U+D U V, T5'=K f',

R'=L V+T4'+T5'.

The other term derivatives are T1'=(1-c)V, T2'=c D V y and T3'=w(JV-D V Jy).

For each term k and shell s define

Q_ks=sum_j M_sj a_j^2 sum_a b_a |T_kja|^2,

a_j=(1+r_j^2/R0^2)^(alpha/2), alpha=(1-c)/c.

Take fixed positive numbers epsilon, delta, lambda and cap. Set h_ks=sqrt(max(Q_ks,epsilon)), d_s=sum_k h_ks, e_s=h_4s+h_5s, F=max(delta max_s d_s,epsilon), G=max(delta max_s e_s,epsilon). Let S_far be a fixed set of shells and

v_s=1/(d_s+F) for s outside S_far,

v_s=1/(d_s+F)+lambda/(e_s+G) for s in S_far,

u_s=v_s^2.

Let m be the lower median of u_s over occupied shells. Set z_s=min(u_s,cap m), zbar=(1/Nr)sum_j z_shell(j), W_j=z_shell(j)/zbar. The vector residual at a node is

r_ja=sqrt(q_j b_a) a_j sqrt(W_j) R_ja.

Assume every nonempty Q_ks is strictly on one side of epsilon; the selected maxima, absolute-floor branches, lower-median index and caps stay fixed on a neighborhood of t=0. Assume zbar>0. Empty shell rows are identically zero and contribute zero derivatives. Then the derivative is

r'_ja=sqrt(q_j b_a) a_j sqrt(W_j) [R'_ja + (W'_j/(2W_j)) R_ja],

with derivatives obtained by the explicit formulas below. All quantities are finite-dimensional real numbers, so the result also applies when the fixed entries of K are exact real values of saved binary64 constants.

## Proof

The affine field identity follows from the fixed-parameter linear coefficient expansion. Differentiating tr((D U+tD V)^2) gives tr(D U D V)+tr(D V D U)=2tr(D U D V), using the finite-dimensional cyclic trace identity. Differentiating the quadratic convection term gives D V U+D U V. Linearity and constancy of K give T5'=K f'. The remaining field identities follow directly by the product rule.

Since c,w,R0 and all nodes are fixed, a_j has zero derivative. Therefore

Q'_ks=2 sum_j M_sj a_j^2 sum_a b_a T_kja dot T'_kja.

On an active square-root branch h'_ks=Q'_ks/(2h_ks); on a strict floor branch h'_ks=0. Thus d'=sum h' and e'=h'_4+h'_5. If s_d is the selected maximum shell, F'=delta d'_s_d unless the absolute floor is active, in which case F'=0. The analogous formula is G'=delta e'_s_e or zero. Branch stability justifies these choices; uniqueness of the selected extrema is sufficient but not necessary when tied branches agree throughout the neighborhood.

Differentiating each reciprocal gives

v'_s=-(d'_s+F')/(d_s+F)^2,

with the additional term -lambda(e'_s+G')/(e_s+G)^2 on S_far. Hence u'_s=2v_s v'_s. For the fixed median index s_m, m'=u'_s_m. For each fixed cap branch, z'_s equals u'_s or cap m'. Consequently

zbar'=(1/Nr)sum_j z'_shell(j),

W'_j=z'_shell(j)/zbar-W_j zbar'/zbar.

All u_s and their capped values are positive, hence W_j>0. The derivative of sqrt(W_j) is W'_j/(2sqrt(W_j)). Substitution into the product defining r proves the result.

## Verification scope

This formula supplies an independent analytic coefficient derivative without subtracting nearly equal residuals. A numerical implementation must record its active switches and refuse a differentiability claim at unresolved switch boundaries. Comparing several centered-difference steps estimates the numerical noise of that comparison; it does not bound the analytic derivative error.

A first check can retain the production pressure matrix constants exactly while independently reconstructing U,V, the source contraction, pressure contractions, all nonlinear weights and their derivatives in extended arithmetic. This checks the derivative of that discrete operator. It does not independently establish the accuracy of K, the continuous Newton pressure, or the radial interpolation. Those need the separate full-source pressure route and quadrature refinements. A second precision or summation-order comparison measures sensitivity, not a rigorous rounding enclosure.

The coefficient expansion may either use the independently solved tail constraints or the saved production linear map. These are distinct checks and must be labelled. The planned reference uses an independent tail solve and compares that solve against the saved production map before reporting a derivative comparison.

## Dependencies

The tail-coordinate proof, field-reconstruction proof and stable-linear-operator proof in neighboring topic folders. All further steps above use finite sums, linearity and the ordinary product and chain rules. No formal proof is claimed.
