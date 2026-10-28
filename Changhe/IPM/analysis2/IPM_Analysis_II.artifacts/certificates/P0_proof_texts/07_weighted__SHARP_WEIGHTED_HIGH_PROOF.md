# A smaller compatible weighted inverse norm

## 1. Statement

Let the reference be exact state131, with canonical full-plane velocity, exponent c, center slope a0 and even-x, odd-y density parity. Use the notation and Hilbert completions of SHARP_WEIGHTED_H2_PROOF.md:

    R=2^35, w=(1+r^2/R^2)^(-11/10), L(h)=||wh||_(Hdot^-1),
    omega0=<r>^(-6/5), omega1=<r>^(-1/5), omega2=(1+4r^2)^(2/5),
    Pj(h)=||omegaj D^j h||_2,
    E1^2=P1^2+2^31 L^2, E2^2=P2^2+2^22 E1^2,
    Q3(h)=||omega2 D^3h||_2, E3^2=Q3^2+2^24 E2^2,
    theta=1/62, alpha=1/124, X_w=[E2,E3]_theta.

Every derivative tensor is ordered Cartesian with its Euclidean norm. Compact smooth parity functions, including functions with nonzero center y-jet, define the completions. Write D_Xw for the strong-generator domain of

    L_fix h=(cX+Ubar).D h-h+U[h].D rhobar.

Then L_fix:D_Xw -> X_w is bijective with inverse norm at most40. The canonical velocity maps X_w to its vector version with norm at most13/2. Define

    C_ad(h)=||h||_(C^alpha(B2))
       +sup_(j>=0) 2^(-j/4)
          [||h||_(Linfinity(Aj))+2^(j alpha)[h]_(C^alpha(Aj))],
    Aj={2^j<=r<=2^(j+1)}, b=h_y(0),
    M(h)=[int_(r<1) r^-260 |h-by|^256 dX]^(1/256).

The compatible inverse estimate is

    L(h)+C_ad(h)+M(h)+|c[h]| <=2^36 ||L_fix h||_Xw.        (1)

In addition,

    ||Dh||_infinity<=2^16||h||_Xw,
    [Dh]_(C^alpha(R2))<=2^20||h||_Xw,
    C_ad(h)<=2^20||h||_Xw, M(h)<=2^21||h||_Xw,
    |c[h]|<=2^29||h||_Xw.                                (2)

The inverse restricts to a bijection between c[h]=0 in its domain and f_y(0)=0 in X_w. On this domain it is the full normalization-dependent linearization. The accepted, unnormalized density residual belongs to X_w. No smallness or nonlinear solvability is asserted.

## 2. Third derivative energy with every lower term

The first two levels have decay1/10 and1/20 by V073. The auxiliary principal matrix at derivative order3 is bounded below by -5I/4 by the complete certificate used in WEIGHTED_HIGH_PROOF.md. Put v=omega2^2, a=D rhobar. The exact identity for each scalar f=D^2h is equation(1) of SHARP_WEIGHTED_H2_PROOF.md. Its scalar error coefficient divided by v is at most

    (1/2)(10*16+2*8)=88,

using |D2v|<=10v/<r>2, |Dv|<=2v/<r>, |D rhobar|<16 and <r>|D2rhobar|<=8. Also

    |D(va)|/v <= |D2rhobar|+(2/<r>)|D rhobar| <=35,

using |D2rhobar|<=3. Since D^3h is centrally even, its omega2 velocity bound is the unrestricted16/3. Thus the identity's first-order error is at most(560/3)P2 Q3. The scalar error is at most88P2^2.

The remaining differentiated transport terms are bounded by

    3*3 P2 Q3 + 2*16 P1 Q3,

because |D2Ubar|<=3 and <r>|D3Ubar|<16. The remaining differentiated nonlocal terms, with all Leibniz multiplicities, are bounded by

    3*3*(9/5) P2 Q3,
    3*2*32*(3/2) P1 Q3,
    2*512*(8/3) P0 Q3.

Here the Riesz constants apply respectively to centrally odd D^2h, unrestricted Dh, and centrally odd h. The weight ratios are omega2/omega1<=2<r> and omega2/omega0<=2<r>2. We used <r>|D3rhobar|<=32, a consequence of the stronger V045 bound, and the V074 bound <r>2|D4rhobar|<512. Tensor Cauchy-Schwarz handles all ordered derivative indices without an omitted component factor.

Since P0,P1,P2<=E2, the total cross coefficient is

    C3=560/3+9+32+81/5+288+8192/3=48938/15<3263.

Young's inequality C3 E2 Q3<=(1/4)Q3^2+C3^2 E2^2 therefore gives

    -<D3 L_fix h,v D3h>
       >=-(3/2)Q3^2-(C3^2+88)E2^2.                       (3)

The exact inequality C3^2+88<2^24 holds. Adding2^24 times the E2 decay inequality yields

    -<L_fix h,h>_E3 >=-(3/2)E3^2.                        (4)

In particular the coefficient2^24 is sufficient without relying on third-order coercivity.

## 3. Common realization, interpolation and bijectivity

The smooth complete transport field has bounded DV, <r>D2V and <r>D3V, by the same coefficient bounds. Its flow acts strongly continuously on E3: the differentiated composition rule uses exactly the weight ratios above. The canonical coupling U[h].D rhobar is bounded on E3 by its product rule and those same coefficient and velocity estimates. The low, E2 and E3 semigroups are therefore the consistent bounded-perturbation Duhamel constructions.

The common compact smooth parity core is a graph core for transport by approximation of its resolvent integral by finite sums of transported core functions. Bounded perturbation preserves it and the generator domain. Consequently(4) extends to the generator domain, and the E3 semigroup grows by at most exp(3t/2). Interpolating it with E2 decay gives

    ||exp(t L_fix)||_(Xw -> Xw)
       <=exp(-[(1-theta)/20-(3/2)theta]t)=exp(-t/40).

Strong continuity follows by density of the common core. The integral -int_0^infinity exp(t L_fix)f dt has norm at most40||f||_Xw. Finite integral identities followed by closedness show it belongs to D_Xw and maps to f. A kernel element would have a constant semigroup orbit and must vanish by the strict decay. This proves surjectivity, injectivity and consistency with the lower inverse.

The levelwise velocity bounds are13/2 in L,3/2 at the first derivative,9/5 at the second, and16/3 at the third. They imply ||U||<=13/2 on E2 and E3, hence on X_w by interpolation. The low13/2 bound is V067. Parity of every derivative is as used in section2.

## 4. Explicit embeddings, strain and moment

Use the exact compact radial cutoffs of WEIGHTED_HIGH_PROOF.md, whose derivative bounds are1,16,1024,32768 through order3. The Bessel H2 product-rule coefficient sum is1092; the H3 sum is38038. On a rescaled annulus of radius t>=1 the common weight-comparison constant is6, as proved there. Hence the SAME cutoff map T_t satisfies

    ||T_t||_(E2 -> H2) <2^13 t^(1/5),
    ||T_t||_(E3 -> H3) <2^18 t^(6/5).

The central cutoff satisfies the same inequalities at t=1. Complex interpolation gives

    ||T_t h||_(H^(2+theta))
       <=2^(13+5theta)t^(1/5+theta)||h||_Xw
       <2^14 t^(1/5+theta)||h||_Xw.                       (5)

The previous proof's Fourier constants are less than4 for the gradient supremum and9 for the alpha-Holder gradient seminorm. Repeating its explicit nearby/far pair argument with2^14 in place of2^24 proves the first three bounds in(2). It also gives density growth O(r^(67/310)) and gradient decay O(r^(-243/310)). Thus the velocity agrees with the canonical sublinear full-plane extension, by the same kernel subtraction and harmonic uniqueness argument.

The exact strain identity, including its local distributional term, is

    c[h]=-b/4+(1/pi)PV int sin(3theta)h(X)r^-3 dX.

Its quantitative bound is

    |c[h]| <= 2^16||h||_Xw/4
       +4*2^20||h||_Xw/[pi alpha(1+alpha)]
       +2^((1+1/5)/2)P0(h)/sqrt(2pi(1-1/5))
       <2^29||h||_Xw.

The exact y-jet cancellation and Taylor's first-order integral formula give the moment bound in(2), since256(1+alpha)+2-260=2/31>0. This moment uses no assumed third derivative at the origin. These constants and40(1+2^20+2^21+2^29)<2^36 prove(1).

## 5. Normalization, residual and bilinear scope

The center expansions of h and U[h] are C1, so the same direct substitution as in WEIGHTED_HIGH_PROOF.md yields f_y(0)=a0 c[h]. Here the reference center normalization is exact. This proves the normalized-range assertion. The excluded column X.D rhobar grows like r^gamma and is outside X_w. Fixing the full leading angular profile excludes the scaling mode and exponent logarithm; free tail parameters are not included in this theorem.

The accepted density residual has leading exponent2/c-1<1/5, and each derivative lowers this exponent by one. The low and derivative integrals thus converge. Smooth radial truncations converge in E3, so the actual residual belongs to X_w. This is a membership result only.

The cylinder argument of FRACTIONAL_BILINEAR_PROOF.md applies without change: it uses only E2>=P2 and E3^2>=P2^2+Q3^2. Its multiplier constant is still less than5. Together with(2) and the low velocity bound it gives, for every low weight radius,

    L_R(U[h].Dg) <=(13/2)(||Dg||_infinity+5||g||_Xw)L_R(h)
                  <=2^19||g||_Xw L_R(h).                 (6)

Closed X_w balls are closed in the low metric by weak compactness and the continuous distributional injection. A compatible uniform HIGH inverse for L_fix+U[k].D on such a ball remains OPEN. Neither(1) nor(6) supplies it, because differentiating the rough transport three times loses derivatives. The nonlinear residual-smallness test is also OPEN for this norm.
