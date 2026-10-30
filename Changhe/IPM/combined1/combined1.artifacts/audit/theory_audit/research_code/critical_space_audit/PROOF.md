# Audit of the critical far-field obstruction

## 1. Exact conclusion and its limits

Fix an integer m>=3, a real kappa, and0<gamma<1. Set c=1/gamma, delta=1-gamma, R=(1+|X|²)^(1/2) and w=(1+log R)^kappa. Let X be the real S1 completion of compact smooth densities in

    ||h||_X²=sum_(j=0)^m ||w R^(j-1-gamma) D^j h||_2².

All Cartesian derivative tensors use ordered indices. Assume a smooth S1 reference rho and its canonical velocity u satisfy, for0<=j<=m,

    |D^j u|<=C_j R^(gamma-j),
    |D^(j+1)rho|<=C'_j R^(gamma-1-j),

with finite constants. Define on the compact core

    A h=(cX+u).Dh-h+U[h].D rho,
    B h=A h-c[h]X.D rho,
    U=(-R1R2,R1²), c[h]=partial_y U2[h](0).

The canonical Riesz realization includes the local identity in R1². There exist unit h_n in X, compactly supported away from the origin, with

    h_n weakly ->0, c[h_n]=0, B h_n ->0 in X,

and every finite prescribed list of real linear functionals on that compact core vanishes exactly on h_n. The functionals need not be continuous. All center jets vanish too.

Let E,F be arbitrary Banach spaces. Suppose a closed linear operator T from a domain in X direct-sum E to X direct-sum F contains all these compact pairs (h,0), and on the compact constrained core satisfies

    T(h,0)=(B h+K h,Q h),

where K:X->X and Q:X->F are bounded compact maps. Then T cannot have both closed range and finite-dimensional kernel. This conclusion does not cover a noncompact bulk observation Q, a different remainder norm, or a domain that excludes the compact packets. It makes no claim that a proposed augmented formula is automatically closed.

This is the common scoped conclusion audited in the frozen P61, P64 and P68 excerpts. A finite number of boundary or phase coordinates does not remove it. A strictly subcritical remainder norm remains outside the obstruction.

## 2. Canonical velocity and strain

Use a radial dyadic partition with annular radii R_i=2^i, taking the central ball as radius1. Each source piece h_j is centrally odd, so its integral is zero. Away from the diagonal the kernel of U and its lth derivative have bounds C_l |z|^(-2-l); the local identity has no separated-annulus contribution.

For inner source radius R_j and outer target radius R_i, subtract the kernel at X using the source's zero integral. The output derivative satisfies

    ||D^l U[h_j]||_(L2 target i)
       <=C R_i^(-2-l) R_j² ||h_j||_2.

After the target and source weights this is bounded by

    C (R_j/R_i)^(3+gamma) ((1+i)/(1+j))^kappa

times the source annular norm. For an outer source, central oddness and evenness of the kernel give U[h_j](0)=0. At l=0 subtract that value; at l>=1 use the directly differentiated kernel. The resulting weighted factors are respectively

    C (R_i/R_j)^(1-gamma) ((1+i)/(1+j))^kappa,
    C (R_i/R_j)^(l-gamma) ((1+i)/(1+j))^kappa.

Nearby blocks follow from the unweighted L2 multiplier bound, derivative commutation, and comparability of radii. Since

    ((1+i)/(1+j))^kappa <=(1+|i-j|)^|kappa|,

both separated directions are summable in the index difference. Discrete convolution gives a bounded canonical U:X->X_vector. This calculation uses parity, not an unjustified general weighted singular-integral estimate.

Compact sources have U[h]=O(r^-3), D^l U[h]=O(r^-3-l); radial cutoffs therefore converge in X_vector. The extension takes values in the stated completion. Local H^m embedding gives C^(1,alpha) regularity for every0<alpha<1 because m>2+alpha. Apply this to U[h] to make c[h] a bounded functional on X. The exponent column X.D rho need not belong to X; it is never applied to a nonzero c[h] in the packet argument.

## 3. The packets and their errors

Choose nonzero real chi in C_c^infinity((0,1)). For L>=2 put

    f_L=L^(-kappa-1/2) r^gamma sin(5theta)
                                   chi((log r-L)/L).

The support lies in e^L<r<e^(2L). S1 parity follows from the odd angular frequency5. All center jets vanish. The exact strain formula, including its local term, gives c[f_L]=0: the local derivative is zero and sin(5theta) is orthogonal to the sin(3theta) integral kernel.

For fixed j, Cartesian differentiation gives finite sums of

    L^(-kappa-1/2-a) r^(gamma-j) P_(j,a)(theta)
                                   chi^(a)((log r-L)/L),

where0<=a<=j and the angular tensors are fixed smooth functions. In logarithmic radius t=log r, the squared weighted radial measure is comparable on the support to t^(2kappa) dt. The normalization cancels L^(2kappa+1). The j=0 term tends to

    pi integral_1^2 s^(2kappa) chi(s-1)² ds>0,

and every derivative norm through m+1 is bounded. Thus ||f_L||_X is bounded above and below away from zero.

Because c gamma=1, (cX.D-1)f_L differentiates only the slow cutoff. Its X norm is O(1/L). The reference transport u.D f_L has norm O(exp(-delta L)), since its coefficient relative to one packet derivative has the additional factor r^(gamma-1).

For U[f_L].D rho split the target radius at T=exp(L/2), after differentiating the product. On r>=T the reference symbol bounds leave a factor R^(-delta) times the corresponding weighted derivative of U[f_L]. The velocity bound therefore gives error O(exp(-delta L/2)). On r<T the source is separated. Kernel cancellation gives

    |U[f_L](X)|<=C L^(-kappa-1/2) exp(-delta L) r,
    |D^j U[f_L](X)|<=C_j L^(-kappa-1/2) exp(-(j-gamma)L), j>=1.

In that region these are bounded by the common expression

    C_j L^(-kappa-1/2) exp(-delta L) R^(1-j).

The weighted product derivatives are therefore bounded by that same prefactor times w R^-1. Its squared radial integral up to T is at most a fixed power of L; the exponential makes the norm tend to zero. No derivative of an indicator function is taken in this argument. Hence

    ||B f_L||_X <= C_kappa [L^-1+(1+L)^(2|kappa|+1)exp(-delta L/2)] ->0.

The precise polynomial exponent is immaterial; the displayed conservative bound is finite for each fixed kappa.

## 4. Exact constraints and the closed-operator conclusion

For d prescribed functionals use d+1 normalized packets with scales L=3^j n,0<=j<=d. Their supports and every derivative support are disjoint, so they are orthonormal in X. The d by (d+1) matrix of functional values has a unit real null vector. The corresponding packet combination h_n has norm1 and satisfies every constraint exactly. Its defect is at most sqrt(d+1) times the largest normalized packet defect. It is supported outside e^n and therefore converges weakly to zero by the weighted L2 tail estimate in every derivative component.

Compactness gives K h_n->0 and Q h_n->0. For v_n=(h_n,0), the graph norm of T tends to1 and v_n is weakly null in the graph space. If the range were closed and the kernel finite-dimensional, the quotient inverse theorem would give

    dist_graph(v_n,ker T)<=C||T v_n||->0.

A finite-dimensional subspace has a bounded projection in the graph Banach space. This projection sends the weakly null v_n to zero in norm. The distance estimate then forces the graph norm of v_n to zero, a contradiction. This proves the scoped failure of upper semi-Fredholmness.

## 5. What adjoining a leading tail can and cannot do

For a finite polynomial-log tail zeta(r)r^gamma sum_(q=0)^N(log r)^q Theta_q(theta), with highest nonzero coefficient Theta_N in angular H^m, membership in X holds exactly when kappa<-N-1/2. The zeroth radial energy has leading integrand t^(2kappa+2N) dt, proving necessity. Every differentiated term has at most the same log degree, proving sufficiency; angular smoothing and radial truncation place it in the completion.

When such a tail belongs to X, its asymptotic coefficient is not a continuous trace: compact radial cutoffs converge in X but have zero asymptotic coefficient. When the tail is external to X, adjoining it as a parameter does not remove the compact packet sequence if the new equations vanish on compact remainders or observe them only compactly. These facts do not preclude changing the power weight, using a noncompact bulk constraint, or proving a suitable different domain.

## Dependencies and audit scope

The proof uses the canonical compact-source strain formula audited in T4-001, elementary kernel decay, Hilbert-space completion, finite-dimensional nullspaces and the closed-range quotient theorem. The source excerpts are preserved with hashes. No numerical existence or nonexistence neighborhood is inferred from this linear obstruction.
