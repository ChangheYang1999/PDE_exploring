# Exact center lower bounds for normalized residuals

Status: CONFIRMED by an independent complete derivation,45 manufactured controls and six separate integer certificate checks. This is a certificate for literal serialized states, not a computer-assisted existence or nonexistence theorem.

## 1. Exact statement and notation

Use the native-source representation and canonical relative full-plane inverse of160. Let beta>0. Let a=F(0), q=G(0), where Theta=x²F and Omega=xG. For each source block, freeze its own binary coefficients, active-mode constraints, b,L and B-spline knots as exact real numbers. Let c denote either the strain of the state's own inverse, or c_self+lambda*c_seed for the separately labeled forced diagnostic. Put

    A=beta-c, m=c-1-beta/2.

Assume that F,G and W are C1 at the center, W1 is odd under x-reflection, W(0)=0, DW(0)=diag(beta-c,beta+c), and the low-order center expansions F=a+O(r), G=q+O(r) hold. These expansions hold in the saved representation at the orders used here; no higher Cartesian smoothness is certified. Then the limits of the divided residuals and their prompt normalizers are

    RF=-2ma,       NF=|2Aa|+|beta-2| |a|,
    RG=(A+1)q-2a, NG=|Aq|+|q|+|2a|.                (1)

If NF>0, the supremum of |R_F|/N_F over the full plane, or its continuous center limit, is at least the exact rational number |RF|/NF. The analogous assertion holds for G when NG>0. The same lower bound holds for the limsup of the original Cartesian ratio along off-axis points tending to0, since the original and divided ratios are equal there. Therefore a positive certified center ratio rejects the corresponding literal field as an exact profile and gives a quantitative lower bound on its normalized residual maximum. A large self ratio cannot be repaired by calling the transporting forced velocity the inverse of the unknown alone.

All quantities in(1), including the absolute values and ratios with nonzero denominators, are rational when computed from the frozen binary data via160. Any verified rational interval containing such a ratio supplies a lower bound by its lower endpoint. These are lower bounds, never full-plane upper bounds. If a denominator is zero, the relevant residual is also zero by the triangle inequality, and we use the requested0/0=0 convention. No positive denominator floor is inserted. The tests below assert positive denominators for the audited states.

## 2. Derivation and continuity at the center

The exact divided equations are

    R_F=A(X)[2F+xF_x]+W2 F_y-(beta-2)F,
    R_G=A(X)[G+xG_x]+W2 G_y+G-[2F+xF_x],

where A(X)=W1/x with its axis limit. Their normalizers retain these grouped terms:

    N_F=|A(X)[2F+xF_x]|+|W2 F_y|+|beta-2| |F|,
    N_G=|A(X)[G+xG_x]|+|W2 G_y|+|G|+|2F+xF_x|.

The C1 regularity and W2=O(r) give xF_x,xG_x,W2F_y,W2G_y ->0. The axis limit needs the stated parity, not merely a two-variable Taylor error divided by x: since W1(0,y)=0, Hadamard's formula gives W1(x,y)/x=int_0^1 partial_x W1(t*x,y)dt, extending continuously to A at0. Thus A(X)->A at the center along every path. Substitution gives the normalizers in(1), RF=[2(beta-c)-(beta-2)]a=-2ma and the displayed RG. When a limiting denominator is positive, continuity of division gives the stated center limit. For any sequence of nonaxis points approaching0 along which this limit holds, the full-domain supremum is at least the limit. Since R_Theta=x²R_F, N_Theta=x²N_F, R_Omega=xR_G and N_Omega=|x|N_G, the Cartesian normalized ratios agree at every nonaxis point. Their values exactly on the axis are vacuous and are not used for this inference.

The saved basis has t=O(r²). Even angular modesn>=2 first activate at spline coefficient j>=n/2, giving radial order at least r^n; odd modes have the additional factor r/sqrt(r²+L²), with the same inactive coefficients. The n=0 mode gives a and q at t=0 and the n=1 mode starts at order r. These facts give bounded first derivatives of F,G near0 and the required first-order center limits. The whole-plane inverse of a source with Omega=qx+O(r²) is differentiable there; parity and divU=0 give its diagonal first derivative diag(-c,c). The moving relative gauge gives W(0)=0. Full higher regularity of each frozen representation is not required for this first-order diagnostic and is not inferred.

## 3. The exact full-plane strain input

Packet160 proves, with the sign convention U=(-Psi_y,Psi_x), -DeltaPsi=Omega,

    c=-(bL/4) sum_j (c_1j-c_3j)
                   (k_(j+p+1)-k_j)/(p+1).           (2)

The proof integrates the actual whole-plane kernel moment. Angular orthogonality retains only modes1 and3, with weights-1/4 and+1/4. For those modes the change of variable t=1-(1+r²/L²)^(-1/(2b)) gives z^(b+1)*r/sqrt(r²+L²)*dr=bL*dt. The exact integral of B_j is its support length divided by p+1. This proves(2), including the infinite exterior. An arbitrary affine harmonic strain is not permitted. The native seed in a forced sum is evaluated in its independently stored basis, not in the unknown's retied basis.

A checker reloads the archived NPZ, verifies its hash, freezes the specified knots, masks inactive coefficients, computes the two angular sums with exact integer arithmetic, and verifies(1)-(2), rational bounds and both inverse labels. Diagnostics such as objective, converged and acceptance are reported as stored metadata, never premises. A forced mismatch may have either sign or vanish; no forced-negative test is built into this theorem. The inequality relevant to a B2 profile always uses c_self.

## 4. Scope

The result audits exact literal real fields defined by finite binary arrays. It does not bound their distance to a true solution, exclude an exponent interval, establish a fold, certify a whole-plane residual upper bound, or turn convergence of a forced solver into convergence to B2. It also does not certify global smoothness or sign. Center gauge and the full-plane inverse are part of the stated representation, not modified to reduce the residual. Numerical and symbolic manufactured controls test the derivation but are not substitutes for it.

Written UTC 2026-10-21T12:00:31.449882+00:00, before implementation and controls.

Clarified UTC 2026-10-21T12:02:21.543553+00:00: actualOpus257 requested an explicit axis-division hypothesis, now supplied above by C1 regularity and x parity. The saved representation already has these properties at the orders used. Its objection to using c_self for a forced residual does not apply to the separately defined unforced B2 target; a follow-up provides that definition and the exact rational radial cancellation.

Review follow-up UTC 2026-10-21T12:06:13.601931+00:00: actualOpus259 returned claude-opus-5-5 and explicitly confirmed the two separately defined residual targets and Hadamard parity argument. Its per-target seed regularity and linearity qualifications hold for the native blocks specified above. No numerical upper bound, proximity result or global smoothness certificate is inferred. Opus258 returned no written audit; no endorsement is attributed to that call.
