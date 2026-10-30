# Independent Cartesian audit of candidate007's mode7 rational probe

## Exact conditional claim

Let rho be exact C1-N1-007-d2w-j7-e2bal at c=4076476460239181/2251799813685248. Its canonical S1 velocity u is divergence free; its smooth sublinear growth and complete F=(cX+u).grad rho-rho in L2 are established in the candidate and norm audits. Suppose real h in L2 has canonical velocity U[h] in L2 with ||U[h]||2<=||h||2 and solves

    F+div((cX+u)h)-(2c+1)h+U[h].grad rho+div(U[h]h)=0

in distributions. The claim being audited is

    ||h||2>4769166867/1000000000000=0.004769166867.

This concerns corrections at the specified c and exact background. It neither supplies a high inverse nor excludes all stationary profiles.

Let n=7, t=r2/(1+r2), v=1-t, and let P be exactly the rational polynomial in source/T4_n7_a0.json. It is divisible by t3. Set phi=r v2 P(t) sin(n theta). Each term is Im(x+iy)^n times a nonnegative integer power of x2+y2 divided by a positive integer power of1+r2. Thus phi is smooth and has phi=O(r^-3), grad phi=O(r^-4). The proof in ../angular_weak_probes/PROOF.md justifies testing with radial cutoffs and gives

    |I|<=(M+C)m+H m2, m=||h||2,
    I=int F phi,
    M=||(2c+1)phi+(cX+u).grad phi||2,
    C=||phi grad rho||2, H>=||grad phi||infinity.

Therefore m is at least the positive root 2|I|/(M+C+sqrt((M+C)^2+4H|I|)). The checker must place that entire interval above the exact claimed floor.

## Independent Cartesian formulas

Define Q=(1-4t)P+2tvP'. The polar derivatives are v2 Q sin(n theta) and n v2 P cos(n theta). Converting to Cartesian components gives

    partial_x phi=(v2/2)[(Q-nP)sin((n+1)theta)+(Q+nP)sin((n-1)theta)],
    partial_y phi=(v2/2)[(Q+nP)cos((n-1)theta)+(nP-Q)cos((n+1)theta)].

The dilation part is (2c+1)phi+cX.grad phi=r v2[(2c+1)P+cQ]sin(n theta). Multiply the first derivative formula by the exact Cartesian velocity u1, and the second by u2. Independently construct phi rho_x and phi rho_y from the corresponding Cartesian density derivatives. The product identities are

    cos(l)sin(j)=[sin(j+l)+sin(j-l)]/2,
    sin(l)cos(j)=[sin(l+j)+sin(l-j)]/2,
    sin(l)sin(j)=[cos(l-j)-cos(l+j)]/2.

Indices denote angular frequencies. Fold negative sine indices with a sign and negative cosine indices without a sign; zero sine terms vanish. Every contributing output frequency is positive and odd for this background and probe. These Cartesian products are independent of T4's stream-function polar Gram assembly and density-gradient angular formulas.

The background fields have the verified forms

    u_i=r sum_(j,l) v^((j+1)delta/2) U_(i,j,l)(t) trig_l(theta),
    rho_i=sum_(j,l) v^((j+1)delta/2) R_(i,j,l)(t) trig_l(theta),

where delta=1-1/c and every polynomial is rational. Exact t2 cancellation in the original derivatives is checked before conversion. Every field entering M or C therefore has the form r v2 sum_(ell,l) v^(ell delta/2) A_(ell,l)(t) trig_l(theta). Orthogonality and r dr=dv/(2v2) show that its energy is pi/2 times

    sum_(matching l,ell,ell') int_0^1 t v^(1+(ell+ell')delta/2)
        A_(ell,l)(t) A_(ell',l)(t) dt.

Both Cartesian components of C are squared separately and added. Distinct radial branches occur twice. The exact complete n7 sine projection of the independently assembled residual gives

    I=(pi/2) sum_ell int_0^1 t v^(ell delta/2-1)
        P_(ell,7)(t) P(t) dt.

These integrals include all radial branches, interactions contributing to mode7 and the infinite-radius endpoint. Convert exact polynomials to v=1-t and evaluate finite beta moments outward at2048bits, with all exponents integrable. Comparison intervals must be accurate and positive where required.

## Exact gradient cover

For fixed t, the angular maximum of |grad phi| is v2 max(|Q|,n|P|). Hence it suffices to bound the two rational polynomials v2 Q and n v2 P on[0,1]. Use the exact Bernstein conversion and midpoint de Casteljau proof from ../optimized_probe_audit/PROOF.md. Every accepted dyadic leaf stores its exact maximum absolute control coefficient. Verify their disjoint interiors and exact tiling of[0,1], and require each bound to be strictly below the frozen peer's rational H=9600067/250000000000. This is independent of the peer's Taylor subdivision.

## Verification and scope

At three rational Cartesian points compare the constructed M, phi rho_x and phi rho_y fields with direct evaluation of the displayed polar gradient and Cartesian candidate jets. Compare all complete I,M,C and root intervals with the frozen T4 result. The first-mode helper used for norm evaluation and Bernstein arithmetic was independently calibrated in N4-152; the generalized field construction and H factor n are new and are explicitly tested here. The canonical source, complete residual cache and assembly, polynomial, peer proof and code, own code and proof, and helper hashes are retained. A successful independent reproduction confirms only the conditional fixed-c correction-distance statement above.
