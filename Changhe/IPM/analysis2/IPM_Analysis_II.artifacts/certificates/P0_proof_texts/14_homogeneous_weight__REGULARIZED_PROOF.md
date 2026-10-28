# A sharp Beurling bound for the regularized negative-order weight

## 1. Statement and scope

Fix R>0 and 0<=s<3. Let

    w(r)=(1+r^2/R^2)^(-s/2),
    H_(s,R)(h)=||w h||_(homogeneous H^(-1)).

The space is the completion of complex centrally odd compact smooth functions in this norm. Use the canonical full-plane transform

    B=(partial_x-i partial_y)^2(-Delta)^(-1).

Then its exact operator norm on this complex space is

    ||B||_(H_(s,R) -> H_(s,R))=3(s+1)/(3-s).                (1)

For the real density parity of this project, the canonical velocity consequently satisfies

    H_(s,R)(U[h]) <= (s+3)/(3-s) H_(s,R)(h).               (2)

Here the left side is the Hilbert sum over both velocity components. In particular at s=11/5 the constants are12 for B and13/2 for U, uniformly in R. Sharpness is claimed for B on the full complex centrally odd space, not for U or the narrower real density parity.

This is a regularized-weight result. It does not transfer the homogeneous-weight coercivity counterexample of PROOF.md to this weight.

## 2. Cylinder norm and the exact angular operators

Set t=log r and define

    alpha(t)=-partial_t log w(e^t)
            =s e^(2t)/(R^2+e^(2t)).

Thus0<=alpha<=s and alpha'>=0. For an angular mode n, odd, write

    w h = r^-2 F_n(t)e^(in theta).

Let Q_n=n^2-partial_t^2. The contribution to the squared negative norm is

    2pi ||Q_n^(-1/2)F_n||_2^2.                             (3)

This follows by solving -Delta Phi=w h: the cylinder potential is Q_n^(-1)F_n, and its Dirichlet integral is (3). It also gives the dual formula with the norm ||Q_n^(1/2)phi||_2.

For n>=3, the canonical Beurling transform sends n to n-2 and gives

    G_n=-F_n+2(n-1)y,
    (n-partial_t-alpha)y=F_n.                              (4)

The solution is the convergent Volterra integral

    y(t)=integral_t^infinity exp[-n(v-t)+integral_t^v alpha]
                              F_n(v) dv.

For n=-k, k>=1 odd, it gives

    G_n=-F_n+2(k+1)y,
    (partial_t+k+alpha)y=F_n,                              (5)

with the Volterra integral over(-infinity,t]. In physical radial coordinates the underlying unweighted formulas are

    B_n h=-h+2(n-1)r^(n-2) integral_r^infinity u^(1-n)h(u)du,
    B_(-k)h=-h+2(k+1)r^(-k-2) integral_0^r u^(k+1)h(u)du.

They follow by solving the radial Poisson equation and differentiating twice; the regular harmonic branch is selected at zero and the decaying branch at infinity. Thus no harmonic velocity is added. The remaining odd mode n=1 is exactly G_1=-F_1 in angular mode-1.

All these assertions are first applied to finitely many angular modes and compact radial support. The bounds below provide the completion. The Volterra kernels have integrable exponential majorants, so their solutions lie in L2 and H1 for an L2 source.

## 3. Positive angular modes

Let n>=3 and m=n-2. From (4),

    F_n=(n-partial_t)y-alpha y,
    G_n=(m+partial_t)y+alpha y.

The Fourier multipliers Q_n^(-1/2)(n-partial_t) and Q_m^(-1/2)(m+partial_t) have modulus one. Also ||Q_j^(-1/2)||_(L2 -> L2)=1/|j|. The ordinary and reverse triangle inequalities therefore give

    ||Q_n^(-1/2)F_n|| >= (1-s/n)||y||,
    ||Q_m^(-1/2)G_n|| <= (1+s/m)||y||.

The input factor is positive because n>=3>s. Hence the norm of this angular block is at most

    n(n-2+s)/[(n-2)(n-s)]
      =1+2s(n-1)/[(n-2)(n-s)].                             (6)

This decreases for real n>=3: the derivative of (n-1)/[(n-2)(n-s)] has numerator s-1-(n-1)^2<0. Its maximum is the right side of (1).

No derivative of alpha is needed for these positive modes. Multiplication by alpha occurs before Q^(-1/2), so no commuting of a variable coefficient with a Fourier multiplier has been assumed.

## 4. Negative angular modes

Let n=-k, k>=1, m=k+2, and A=partial_t+k+alpha. Its adjoint is A*=-partial_t+k+alpha. Integration by parts gives

    ||A*z||_2^2 = ||z'||_2^2+||(k+alpha)z||_2^2
                      +integral alpha' |z|^2
                 >=||Q_k^(1/2)z||_2^2.                  (7)

This holds on H1 by approximation. The adjoint Volterra equation is solvable for every L2 right side, since k+alpha>=k>0, and its solution belongs to H1. For y=A^-1F, duality against u=A*z and (7) yields

    ||y||_2 <= ||Q_k^(-1/2)F||_2.                          (8)

Indeed <y,u>=<F,z>, bounded by the negative norm times ||Q_k^(1/2)z||, which is at most||u||.

Equation(5) gives G=(m-partial_t)y-alpha y. Therefore

    ||Q_m^(-1/2)G|| <= (1+s/m)||y||
        <= (1+s/(k+2))||Q_k^(-1/2)F||.                    (9)

This is at most1+s/3, and hence no larger than3(s+1)/(3-s). The n=1 block has norm one. Orthogonality of angular modes now proves the upper bound(1).

## 5. Sharpness and velocity

For the positive n=3 block, shift a compact source on the t-line by T towards infinity. The coefficient alpha(t+T) tends to s uniformly on bounded intervals. Its Volterra kernel is dominated by exp[-(3-s)(v-t)]. Dominated convergence in L2, using this convolution majorant, proves convergence of the output to the constant-alpha=s block for each fixed compact source. The input norm is unchanged by translation. For this constant block, sources with Fourier mass near tau=0 have norm ratio approaching3(s+1)/(3-s), as computed in PROOF.md, section1. First taking T to infinity and then taking longer smooth packets proves the matching lower bound. All the sources are compactly supported annular smooth functions. Thus(1) is sharp on the completion.

For real h, U_2+i U_1=(B-I)h/2. Its complex negative norm squared is the sum of the two real component norms squared. The triangle inequality gives(2), since [3(s+1)/(3-s)+1]/2=(s+3)/(3-s). Reflection exchanges B with its opposite complex derivative and preserves this radial norm, so the same bound is available for either convention.

## 6. Consequences for the existing weighted framework

The weight in07_weighted/WEIGHTED_HIGH_PROOF.md has s=11/5 and R=2^179. Its previous weighted-low velocity bound2^35 may therefore be replaced by13/2. The proof of07_weighted/BILINEAR_PROOF.md uses the velocity bound only once, followed by the already proved product estimate. It consequently gives

    ||U[h].grad g||_L <= (13/2) Z(g)||h||_L,
    Z(g)=||grad g||_infinity
             +15 sqrt(||D2g||_2^2+||rD3g||_2^2).            (10)

No extra regularity of the first argument is imposed. The hypotheses on the second argument in that bilinear theorem are unchanged.

The same velocity bound13/2 holds on E1,E2,E3 and their interpolation space X in WEIGHTED_HIGH_PROOF.md. To see this, use(2) on the low component and the bounds from MELLIN_RIESZ_PROOF.md on each weighted derivative component:3/2 for first derivatives with weight<r>^(-1/5),9/5 for centrally odd second derivatives with weight(1+4r^2)^(2/5), and16/3 for unrestricted third derivatives with that weight. Each is below13/2. Summing the squared components and interpolating proves the claim. Induced vector parities retain central oddness in the low component; tensor components are counted by the same Euclidean sums used in the existing norms.

These improved mapping constants do not by themselves reprove a nonlinear high inverse or lower the previously fixed hierarchy coefficients. Any such improvement requires recomputing the corresponding energy estimates. The exact regularized negative-order transform bound and(10) stand independently of that future work.
