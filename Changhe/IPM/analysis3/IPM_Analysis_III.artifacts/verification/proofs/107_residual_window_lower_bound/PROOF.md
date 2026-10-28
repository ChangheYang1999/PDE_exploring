# A certified radial-window lower bound for the strong residual

## Analytic reduction

Use the exact normalized original modal trial, target Y, residual F, and angular decomposition F=p(gamma+cos(theta)^2 Q) from topics98 and105. Let mu be the probability measure on the circle with density proportional to |cos(theta)|^(-1/2)sin(theta)^2, and let M=2 Beta(1/4,3/2) be its unnormalized mass. Define

 qbar(t)=integral Q(t,theta) dmu(theta).

For any real interval I=[a,b] with 0<=a<b, suppose a directed computation proves qbar(t) belongs to a closed interval J for every t in I. Set d_J=inf{|v|:v in J}. Then

 ||F||_Y^2 >= (b-a) exp(27a/4) M d_J^2.                    (1)

For disjoint intervals their right sides may be added. The same argument applies with an exact lower bound on integral_I exp(27t/4)dt in place of (b-a)exp(27a/4).

Indeed the positive axis energy may be discarded, and Cauchy-Schwarz in the probability measure gives integral Q^2 dmu >= qbar^2. Proof 98 gives the exact radial norm, and integration proves(1). This is an actual integral lower bound once a uniform enclosure on an interval, rather than a value at its midpoint, has been supplied.

If Q=sum_j q_j cos(2j theta), then qbar=sum_j q_j m_j with the exact rational moments m_j of proof 98. Thus it can be enclosed without angular quadrature. Coefficient balls are valid simultaneously throughout I when every radial exponential polynomial is evaluated on the full interval. Dependence between the balls only enlarges the enclosure and cannot invalidate the bound.

## Removing an exact far-field cancellation before interval evaluation

Write h_j(t) for the sine coefficient of rho/r^3 and let t=t_plus+s. Each h_j is a finite sum of terms exp(e s)p(s), with rational exponents e and polynomial coefficient balls p enclosing the exact normalized trial. The linear scaling part of the residual is ell(3h_j+h_j')-h_j. For each such term its polynomial is

 [(3+e)/k-1]p(s)+(1/k)p'(s).                               (2)

The bracket is exactly zero when e=k-3. Formula(2) must therefore be assembled using rational exponent arithmetic before evaluating at an interval. This removes the leading linear tail by the exact identity ell k=1, rather than by cancellation of two wide interval values. The nonlinear two products are then evaluated by the same directed Laurent multiplication as proof 105. Both structural angular quotients remain exact for the reasons proved there.

## Certified numerical conclusion

For the exact normalized original modal trial defined in proof 105, its full strong-target residual satisfies

 ||F||_Y > 933.47.

This lower bound uses only the remainder component and the radial interval 99/10 <= t <= 101/10. It is consequently unchanged if the equivalent scalar axis norm is replaced by the adapted Gamma norm. It is not an upper bound, does not prove or disprove injectivity, and by itself does not exclude a nearby nonlinear solution.

The computation uses512-bit directed arithmetic, a degree20 Taylor polynomial at t=10, and the complex disk of radius1. Its Cauchy error is less than8.64e-16. The witness coefficients are exact binary rationals recorded in evidence/taylor.json. A separate640-bit audit checks the positive scalar bound, the direct angular Gram sum and agreement at the center with the independent point audit of proof 105. The coefficient construction reads the read-only original, whose SHA-256 is a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874.

The earlier full-interval mean-witness calculation in evidence/windows.json was inconclusive because interval dependency obscured its sign. It contributes no positive number to the theorem.

## A fixed angular witness and a Taylor enclosure

A stronger version uses any fixed real cosine polynomial R with H(R)>0, where H is the normalized angular quadratic form of proof 98. Put S(t)=H(Q(t),R). Cauchy-Schwarz gives

 ||F||_Y^2 >= M [inf_(t in I)|S(t)|]^2/H(R)
                    times integral_I exp(27t/4)dt.          (3)

The witness coefficients may be chosen by rounding a point evaluation of Q to exact binary rationals. That choice is only a way to select a test function; the bound is checked afterward for that exact test function.

On the outer analytic continuation, suppose all residual sine indices are at most N. The linear map from the sine vector to its twice-divided cosine quotient has l1 operator norm at most

 C_N=4 N^4(2N+1).

Indeed division by sin(theta) has norm at most2N+1. Each of the two cosine quotient maps has l1 norm at most2N^2, directly from formula(4) of proof 98. These estimates remain valid for complex coefficients and for the linear quotient map with its axis value subtracted. Therefore, for complex t,

 |S(t)| <= C_N ||R||_(coefficient l1) ||s(t)||_(coefficient l1).   (4)

The residual formula gives the additional bound

 ||s||_1 <= ||P||_1 ||3h+h'||_1
                     +||Qvel||_1 ||(2j+1)h_j||_1+||Lh||_1,       (5)

where Lh is the exactly cancelled scaling part in(2). Products of a sine and a cosine polynomial have coefficient l1 norm at most the product of their l1 norms, by the elementary product-to-sum identities.

For an exponential polynomial sum_e exp(e t)p_e(t), expand about the real center t0. Its modulus on the complex disk |t-t0|<=R0 is bounded by

 sum_e exp(|e|R0) sum_j |[exp(e t0)p_e(t0+u)]_j| R0^j.     (6)

The code uses(4)-(6) to produce M_disk with |S|<=M_disk on that disk. If the first m+1 Taylor coefficients of S are enclosed and 0<h<R0, Cauchy's coefficient estimate gives the uniform error

 |S(t)-sum_(j=0)^m S_j(t-t0)^j|
 <=M_disk (h/R0)^(m+1)/(1-h/R0), |t-t0|<=h.               (7)

The Taylor coefficients are assembled by exact exponential-polynomial series and directed Laurent products before evaluating the interval polynomial. Equations(3) and(7) therefore retain cancellations lost by independent full-interval coefficient evaluation. Positivity of the resulting lower endpoint, if obtained, is the only numerical condition needed for a positive norm bound.
