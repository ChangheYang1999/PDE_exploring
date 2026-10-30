# Derivative loss and the common low-domain step

## 1. Setting and conclusions

All scalar functions are real and S1: even in x, odd in y. Define U=(-R1 R2,R1^2), with Rj=partial_j(-Delta)^(-1/2), and H=Hdot^-1(R2). Set omega=(1+4r^2)^(2/5), b0=20/21 and

    N_s(h)^2 = ||omega D^2 J^s h||_2^2 + 2^14 ||D J^s h||_2^2
               + 2^18 ||J^s h||_2^2 + 2^18 b0 ||J^s h||_H^2,
    J=(1-Delta)^(1/2), s>0.

The space is the completion of the compact smooth S1 core. Tensor norms use all ordered derivatives. Write B(k,h)=U[k].grad h and c[h]=partial_y U_2[h](0), the latter on N_s where the derivative trace exists.

Two different facts are proved here.

1. For every nonzero compact smooth S1 function k, B(k,.) is unbounded as an operator N_s -> N_s. This remains true on compact smooth test h having exact c[h]=0 and every origin jet zero. One can also take k with c[k]=0. A proof that bounds the full quadratic transport term in N_s by C N_s(h)^2 with a fixed C is therefore invalid.
2. The baseline two-norm argument avoids this derivative loss. Given its stated high semigroup, low energy estimate and common L2 realization, the required low generator-domain inclusion follows from a simultaneous-density argument. No assumption that arbitrary H solutions belong to L2 is needed.

The second assertion audits a functional-analytic step in the baseline proof, not the numerical coefficient bounds that yield its energy estimates.

## 2. An explicit high-norm derivative loss

Because k is nonzero in L2, U_1[k] is not identically zero: its multiplier xi_1 xi_2/|xi|^2 vanishes only on a set of Lebesgue measure zero. Choose a small open set away from the origin and the axes where U_1[k] is nonzero. A real amplitude A in C_c^infinity can be chosen with S1 parity, supported in this set and its reflection images, and with U_1[k] A not identically zero. Put

    f_n(X)=A(X) cos(nx).

The following modulated-function asymptotics hold:

    N_s(f_n)/n^(2+s) -> ||omega A||_2/sqrt(2),
    N_s(B(k,f_n))/n^(3+s) -> ||omega U_1[k] A||_2/sqrt(2). (1)

Here is the multiplier justification, including the fractional derivative. For any fixed compact smooth amplitude G, the Fourier transform of

    n^(-s) exp(-inx) J^s(exp(inx)G)

is n^(-s) <xi+n e1>^s Ghat(xi), which tends to Ghat in Schwartz topology. On |xi|<=n/2, Taylor bounds for the multiplier and each of its derivatives give the difference O(n^(-1)) times a fixed polynomial in xi. Outside that region all derivatives of Ghat decay faster than any prescribed power, while the multiplier derivatives grow at most polynomially in n and xi. Splitting these two regions proves convergence in every Schwartz seminorm. The same argument applies to the negative carrier and to sine.

Consequently the xx derivative of J^s f_n is -n^(2+s) A cos(nx)+o(n^(2+s)) in weighted L2. Other second derivatives and all lower norm components have lower order; the H component is bounded by its ordinary L2 and weighted first-moment estimates on the modulated Schwartz amplitudes. Finally, integral omega^2 A^2 cos^2(nx) tends to ||omega A||_2^2/2. This proves the first limit in (1). The leading term of B(k,f_n) is -n U_1[k] A sin(nx); its remaining amplitude terms are compact smooth and have one less power of n. Applying the same argument proves the second limit.

Thus the quotient N_s(B(k,f_n))/N_s(f_n) grows linearly in n. These tests already vanish identically near zero. To impose exact strain zero, choose a fixed compact smooth S1 function

    phi(X)=eta(r)(3x^2 y-y^3),

where eta is nonnegative, nonzero and supported in an annulus. The contact formula gives c[phi]=integral eta(r) r dr>0. Since f_n is supported away from zero, its strain is the integral of a compact smooth amplitude times cos(nx). Repeated integration by parts gives c[f_n]=O(n^(-N)) for every N. Replace f_n by

    f_n - (c[f_n]/c[phi]) phi.

This changes both quantities in (1) by less than every inverse power of n and makes c[f_n] exactly zero. All origin jets remain zero. A nonzero zero-strain k is obtained by taking two independent compact annular S1 functions and a nontrivial linear combination in the kernel of c.

For completeness this also refutes a bounded quadratic map on the entire high ball. Normalize the zero-strain tests by their N_s norm and call them h_n. The term B(h_n,k) has bounded N_s norm because the second factor k is fixed smooth, as proved by the multiplication estimate in ../alternative_route/PROOF.md. If Q_2(h)=B(h,h) were bounded on every bounded subset of N_s, the polarization identity

    Q_2(k+h_n)-Q_2(k-h_n)=2 B(k,h_n)+2 B(h_n,k)

would bound B(k,h_n) uniformly. This contradicts (1). The polarization uses only smooth inputs, so it does not presuppose that Q_2 extends to the entire high space. The baseline does not claim this invalid quadratic bound.

## 3. Common low-domain lemma

Let A=L+U[k].grad be a fixed frozen operator. Assume:

- A has a strongly continuous semigroup S_X on X=N_s, and this is the restriction of a strongly continuous semigroup S_2 on S1 L2.
- A on L2 is its maximal distributional realization. This holds for the baseline globally Lipschitz, at-most-linearly growing transport field plus a bounded L2 coupling.
- X is dense in H, X embeds continuously in both H and L2, and

      ||S_X(t)f||_H <= exp(-nu t)||f||_H,   nu>0, f in X.

Then S_X extends by density to a strongly continuous semigroup S_H on H, with the same bound. Moreover, if w in X and Aw=f in H intersect L2 distributionally, then w is in the generator domain D(A_H), A_H w=f, and

    ||w||_H <= ||f||_H/nu.                               (2)

### Extension and simultaneous density

The bound gives a unique extension at each time. Strong continuity follows first for data in X by its high strong continuity and the continuous inclusion X -> H, then for all H data by density and the uniform bound for t in a compact interval. The semigroup law passes by continuity.

The compact smooth S1 core is dense in H intersect L2 in the sum norm. To see this, first cut off the Fourier transform on annuli bounded away from zero and infinity and approximate it smoothly, preserving parity and reality. These approximations converge in both L2(dxi) and L2(|xi|^(-2) dxi). Their inverse transforms are Schwartz. A smooth radial spatial cutoff then gives compact smooth functions; convergence in H follows from

    ||g||_H <= ||r g||_2                                  (3)

for centrally odd Schwartz g. This inequality is proved by duality and angular Poincare: for centrally odd test phi, integral |phi|^2/r^2 <= integral |grad phi|^2 because only nonzero angular modes occur. Thus |integral g phi| <= ||r g||_2 ||grad phi||_2. An arbitrary test may first be projected onto the centrally odd subspace without increasing its gradient norm.

S_H and S_2 agree on the common core because both agree there with S_X. Their boundedness on finite time intervals and simultaneous density show that they agree on H intersect L2 as distributions. Distributional identification is legitimate: compact smooth test functions pair continuously with both H and L2.

### The domain, not just an a priori estimate

Since w in X is in L2 and Aw=f in L2, maximality places w in D(A_2). The L2 orbit identity is

    S_2(t)w-w = integral_0^t S_2(tau) f dtau.

The common-space consistency just proved turns both sides into the corresponding H identity. The integral exists as a Bochner integral in H. Dividing by t and taking t down to zero yields the H derivative f. Hence w belongs to D(A_H).

For arbitrary f in H, the convergent integral -integral_0^infinity S_H(t)f dt is in D(A_H), solves A_H w=f, and has norm at most ||f||_H/nu. An element of its kernel has a constant orbit and also decays, so it is zero. This proves (2) for the identified w.

## 4. Why the nonlinear differences satisfy the lemma

For z,v in N_s, write psi[z]=partial_x(-Delta)^(-1)z. Then

    U[z].grad v = div(psi[z](v_y,-v_x)),
    ||psi[z]||_2 <= ||z||_H.

Consequently

    ||B(z,v)||_H <= ||z||_H ||grad v||_infinity.           (4)

This forcing also belongs to L2, since U[z] is bounded and grad v is in L2. Therefore every difference w=T(k)-T(l) from the high frozen-inverse construction, satisfying

    A_k w = -B(k-l,T(l)),

falls exactly under the common low-domain lemma. The trace condition c[k]=0 is imposed in the high space where it is continuous; no trace is asserted on H alone.

The closed high ball intersected with ker c is complete in the H metric. An H-Cauchy sequence in that ball has an H limit. A subsequence converges weakly in the Hilbert high space; distributional uniqueness identifies the same limit. Weak lower semicontinuity preserves the high radius and weak continuity of the bounded linear functional c preserves its zero value. This proves completeness.

Under the baseline high inverse and embedding assumptions, (2)-(4) therefore yield a valid low-metric contraction. The rough transport term remains in the generator throughout. Neither the nonlinear map nor its derivative is assumed bounded high-to-high.

## Dependencies and verdict scope

The construction of the high semigroup and its numerical decay constants are inputs here. Their original proof is copied in source/baseline_quasilinear.md; the sharpened 4800 and 5 constants are stated in source/baseline_closure.md. This note independently verifies the domain-consistency step, the low product estimate, complete-ball argument and the derivative-loss obstruction. It does not certify the background profile or infer a nonlinear solution from low-energy weak convergence alone.
