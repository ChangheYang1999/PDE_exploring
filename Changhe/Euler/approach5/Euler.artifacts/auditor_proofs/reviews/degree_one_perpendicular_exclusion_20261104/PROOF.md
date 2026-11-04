# Perpendicular axes cannot have a nonnegative degree-one source

## 1. Exact statement

Fix 0<beta<1, t=(beta-3)/2 and k=(beta+1)/2=t+2. Let a,b be nonzero real vectors in R3 with a dot b=0. Suppose a C1 field U agrees for |y|>=2 with the homogeneous expression

    T(y)=|y|^t [k a-t(a dot n)n+b cross n], n=y/|y|.

Then, at every r>=2,

    tr((DU(r b/|b|))^2)
        = -2 r^(2t-2) [t^2 k |a|^2+|b|^2] < 0.                   (1)

In particular no perpendicular pair in this family has q=tr((DU)^2)>=0 throughout the exterior. No pressure, Euler equation, energy normalization, or assumption on the completed core is needed. This sharpens the previous statement that the necessary interval for the poloidal fraction is not sufficient in general for perpendicular axes.

## 2. Proof and nearby nonparallel axes

Differentiate T, or use the independently confirmed derivative formula of A3166. At |n|=1 it gives

    q_T(n)/2 = t^2[(k+3)(a dot n)^2-k|a|^2]
               -t|b|^2+(t-1)(b dot n)^2
               -t(k+t)(a cross b) dot n.                         (2)

For n=b/|b| the first scalar product and the cross term vanish, while (b dot n)^2=|b|^2. Thus (2) is -t^2 k|a|^2-|b|^2. It is strictly negative since k>0. Homogeneity yields DT(rn)=r^(t-1)DT(n), proving (1). Continuity also gives a nonempty open set of negative angular source around that direction at each radius.

For completeness, the other statement in A150 also follows from (2). Fix any nonparallel angle between a and b, a normalization D|a|^2+|b|^2=C>0, D=k^2+2, and vary rho=D|a|^2/C. Evaluating (2) at the two normals to the span of a,b gives the necessary condition

    |b|^2+tk|a|^2 >= |k+t| |a cross b|.                          (3)

At rho_plus=D/(D-kt), the left side is zero, whereas the right side is positive: both vector lengths are positive, their angle is nonparallel, and |k+t|=1-beta>0. By continuity (3) fails for all rho sufficiently close to rho_plus from below, at that fixed nonparallel angle. This does not assert that every nonparallel pair fails; (1) is the stronger universal statement for perpendicular pairs.

## 3. Dependencies and scope

The only imported identity is the degree-one derivative formula already confirmed in A3166; its substitution and homogeneity are written out above. The comparison is the existing theory agent's Note A150, which supplies the same exact evaluation and condition (3). The retained extract is in the team records. No numerical probe is used as evidence, and no formal build was performed. The statement refutes source nonnegativity for this family; it supplies no Euler counterexample or unrestricted nonexistence theorem.
