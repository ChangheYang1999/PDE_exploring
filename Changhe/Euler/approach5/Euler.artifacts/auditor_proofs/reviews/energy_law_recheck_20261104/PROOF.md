# Repeated audit of the energy law and pressure normalization

This audit concerns the exact report pin97da5b934c7bcf460a5bb258d7690655818bde0c1cd38eb85d5a470c88cf8572. Its entire Section2A, lines730-1212, was read. The complete existing configured model Theory Agent A  recheck, including its2026-11-04T04:58Z addendum, was read and compared. Actual provider execution is independently unattested. The argument below rederives the energy theorem used in the helicity-sign proof; it does not newly prove the separately stated weak-profile theorem or external convolution theorems.

## 1. Exact statement and notation

Let 0<c<1, omega be any finite real number, J(y1,y2,y3)=(-y2,y1,0), A=cI-omega J and B=Ay+U. Suppose U is a real C1 vector field on all of R3, P is C1, div U=0, and

    (1-c)U+(B.grad)U+omega JU+grad P=0.

Assume M0=sup|U|<infinity and U(R.) tends to0 in distributions as R tends to infinity. Uniform decay implies this latter assumption by dominated convergence. Write

    E(R)=integral_(|y|<R)|U|^2,
    alpha=5-2/c, g(R)=R^(-alpha)E(R),
    epsilon(R)=sup_(|y|>=R)|U(y)|.

For c<2/5, U=0. At c=2/5, U is square integrable and its exterior square integral is O(R^-5). For c>2/5, g has a finite nonnegative limit L, with |g(R)-L|<=C/R for R>=2, and L>0 unless U=0. The finite constants in this energy theorem can depend on c,M0,E(4), but not on omega. If U decays uniformly, the last error improves to

    C[epsilon(R/2)/R+R^((alpha-5)/2)]=o(1/R).

These assertions do not rule out nonzero profiles in the target range2/5<c<1/2: there alpha lies strictly between0 and1, and positive L gives the necessary infinite-energy growth.

## 2. Exact energy identity

Put q=|U|^2/2. Since U.JU=0, div B=3c and div U=0, the dot product with U gives

    (1-5c/2)|U|^2+div(qB+PU)=0.

All fields in this equality are C1. The divergence theorem on a ball is therefore valid. On its boundary Jy is tangent, and the flux of U alone is0. For every spatial constant p,

    (cR/2)E'(R)+(1-5c/2)E(R)
       =-integral_(|y|=R)(q+P-p)U.n.

The left side equals(c/2)R^(1+alpha)g'(R). Integration in R gives the annular formula

    g(R2)-g(R1)=-(2/c) integral_(R1<|y|<R2)
          |y|^(-1-alpha)(q+P-p)U.(y/|y|).

A separate constant may be used on each annulus, since it contributes zero on every sphere. No boundary limit has been assumed.

## 3. The pressure normalization is a conclusion

Let T_ij have Fourier multiplier -xi_i xi_j/|xi|^2, and let F_ij=U_i U_j. Away from0 its kernel is

    K_ij(w)=[3w_iw_j-delta_ij|w|^2]/(4pi|w|^5).

For every compactly supported smooth test phi, T_ij partial_k phi belongs to L1: locally use its L2 bound and outside a ball use integration by parts and |grad K|<=C|w|^-4. Thus

    <G_k,phi>=-sum_ij integral F_ij T_ij partial_k phi

defines a distribution. Taking divergence of the profile equation gives -Delta P=partial_i partial_j F_ij. The two omega terms cancel exactly. Since T_ij Delta phi=-partial_i partial_j phi, partial_k P-G_k is a harmonic distribution, hence a smooth harmonic function h_k.

Set U_R(z)=U(Rz). Testing the rescaled profile equation yields

    <(partial_k P)(R.),psi>
       =integral U_R.Lambda_k psi
          +R^-1 sum_j integral U_(R,k)U_(R,j)partial_j psi,

where

    Lambda_k psi=(4c-1)psi e_k-omega psi J^T e_k
                   +(Az.grad psi)e_k.

The canonical term is

    <G_k(R.),psi>=-R^-1 sum_ij integral F_ij(Rz)T_ij partial_k psi(z)dz.

Both terms with R^-1 tend to0. Boundedness and distributional convergence of U_R imply convergence against every L1 test, by approximation with compactly supported smooth functions. They also allow an L1-convergent sequence of moving tests.

Fix x and choose a radial compactly supported smooth phi of integral1. The harmonic mean identity expresses h_k(x) as its integral against phi((.-x)/R)/R^3. In the formulas above use psi_R(z)=phi(z-x/R). The Lambda tests converge in L1, and the L1 norms of the transformed derivative tests are independent of translation. Every term tends to0. Thus h_k(x)=0 for every x, and grad P=G. No bound or normalization on P was an extra premise. The factors involving omega occur only in fixed tests in this limiting step and do not enter the estimates below.

## 4. Annular pressure and flux bounds

For a radius R split F into |z|<R/2, R/2<=|z|<4R and |z|>=4R. The first two pieces have compact support and are in L2. Write their transforms as Pi2 and Pi1. For |x|<2R define

    Pi3(x)=integral_(|z|>=4R) sum_ij
                   [K_ij(x-z)-K_ij(-z)]F_ij(z)dz.

The difference is integrable because its absolute value is at most C R M0^2|z|^-4. Differentiation under the integral and the canonical gradient identity show that P-Pi1-Pi2-Pi3 is constant p_R on the connected ball.

The contracted Fourier multiplier has norm at most1 on matrix-valued L2, so

    ||Pi1||_2<=epsilon(R/2)E(4R)^(1/2).

For a real vector u,

    |sum K_ij(w)u_i u_j|<=|u|^2/(2pi|w|^3).

Consequently |Pi2(x)|<=4E(R/2)/(pi R^3) on R<=|x|<2R. Differentiating the contraction gives terms with coefficients6,15,3 divided by4pi, and therefore

    |grad(sum K_ij(w)u_i u_j)|<=6|u|^2/(pi|w|^4).

On the segment x replaced by tx, |tx-z|>=|z|/2. Hence

    |Pi3(x)|<=192 R I(R)/pi,
    I(R)=integral_(|z|>=4R)|z|^-4|U|^2
         <=4 integral_(4R)^infinity r^-5 E(r)dr.

The final inequality is integration by parts, discarding its negative lower boundary term; the upper boundary tends to0 by boundedness of U.

Let Phi(R)=integral_(R<|y|<2R)|q+P-p_R||U|. Cauchy-Schwarz, the preceding bounds and the annular volume(28pi/3)R^3 give

    Phi(R)<=epsilon(R)E(2R)/2+epsilon(R/2)E(4R)
      +(28pi/3)^(1/2)R^(3/2)E(2R)^(1/2)
           [4E(R/2)/(pi R^3)+192 R I(R)/pi].

If E(r)<=K r^mu for r>=1 and0<=mu<=3, then for R>=2,

    I(R)<=K R^(mu-4),
    Phi(R)<=C1(M0 K+K^(3/2))R^mu,

with an absolute C1. Indeed the two far-field products have exponent(3mu-3)/2<=mu. There is no omega in any of these bounds.

## 5. Dyadic bootstrap and the limit

Put beta=mu-1-alpha. The energy identity and the flux bound imply, whenever R<=R1<R2<=2R,

    |g(R2)-g(R1)|<=C2 R^beta,
    C2=(2/c)max(1,2^(-1-alpha))C1(M0 K+K^(3/2)).

If beta>0, sum along the finite descending dyadic chain ending in[2,4). The geometric sum gives E(R)<=C R^(mu-1). If beta=0 it gives E(R)<=C R^(mu-1)(1+log R). If beta<0, sum along the infinite increasing dyadic chain and include the final partial interval. The sum converges, proving existence of L and |g(R)-L|<=C R^beta. Bounds on[1,2] can always be restored by enlarging K. These steps depend only on the indicated constants and E(4).

Start with mu=3 from boundedness. If alpha<0, apply the positive-beta step to reach exponents2,1,0. At mu=0, positive or zero beta gives E(R)<=C R^-1(1+log R), and negative beta gives bounded g and E(R)<=C R^alpha. Each tends to0. Monotonicity and nonnegativity of E force U=0.

If0<alpha<3, lower mu by1 while mu-1>alpha. At an equality use the logarithmic estimate and absorb its logarithm in R^(1/4), so the new exponent is alpha+1/4. In every case a finite number of steps reaches mu-1<alpha with mu>=alpha. The convergent case gives L and bounded g, hence E(R)<=K R^alpha. Applying the same estimate once more with mu=alpha gives the O(1/R) error.

If L=0, this error lowers the energy exponent to alpha-1. Reapply the convergent dyadic estimate while the exponent remains nonnegative, always using the same already identified limit0. After finitely many steps E has a negative power bound and vanishes identically. Thus a nonzero field has L>0.

Under uniform decay, the sharper flux inequality with mu=alpha gives

    Phi(R)<=C epsilon(R/2)R^alpha+C R^((3alpha-3)/2).

Summing the corresponding increments from R to infinity gives the improved error in Section1. Epsilon is nonincreasing, and both geometric sums converge. Since alpha<3, the second error is o(1/R), as is the first.

## 6. The critical square-integrable tail

If alpha=0, the positive-beta steps give mu=2 and then1. The zero-beta step gives E(R)<=C(1+log R)<=C'R^(1/4). The negative-beta step proves that E converges to E_infinity. Reapply it with mu=0 to obtain Tl(R)=E_infinity-E(R)=O(1/R).

For the sharper tail, retain the tail rather than the full energy in the flux estimate. The local cubic term and middle pressure term are bounded by C Tl(R/2). The inner pressure term is bounded by C R^-3/2 E_infinity Tl(R)^(1/2). For the far term, R I(R)<=C R^-3 Tl(4R); using its finiteness gives the same bound. Therefore

    Phi(R)<=C[Tl(R/2)+R^-3/2 Tl(R)^(1/2)].

The integrated energy identity and the dyadic sum yield

    Tl(R)<=C R^-1 Tl(R/2)+C R^-5/2 Tl(R)^(1/2).

All flux sums are absolutely convergent under this estimate. If Tl=O(R^-tau), it improves to exponent min(tau+1,(5+tau)/2). Starting even from tau=0, four steps reach tau=4. Then the first term is O(R^-5); Young's inequality bounds the second by Tl(R)/2+C R^-5. Absorption proves Tl=O(R^-5). Neither this argument nor the theorem concludes that U=0 at c=2/5.

## 7. Corollary and source-scope checks

The entire remaining report Section2A was also read. The annular lower bound follows from E(2R)-E(R)=(2^alpha-1)L R^alpha+O(R^(alpha-1)) and the exact annular volume. The printed constant c1 is the square root of half the leading energy divided by that volume. The Lp consequence uses boundedness when p<2, and a fixed-inner-ball/tail Holder split for2<=p<=p*=3c/(1-c), where3-6/p-alpha<=0.

For the weighted conclusion, integration by parts gives

    integral_(1<|y|<R)|y|^-alpha|U|^2
         =alpha L log R+O(1).

The elementary Lorentz estimates L1-L3 in the report follow respectively from monotonicity of rearrangements, layer-cake integration split at the weak-norm threshold, and dominated convergence of the tail rearrangements. Its vorticity corollary additionally uses the explicitly named Hardy-Littlewood-Sobolev and O'Neil inequalities. Their source statements were not freshly reread in this audit. Given those inputs, the split1<p1<3c<p2<3 and the harmonic-mean removal of the velocity remainder check; the convolution target exponent is1/p*=1/(3c)-1/3. No endpoint weak-Lp Liouville conclusion is inferred.

For the twisted natural tail, substituting epsilon(R)=O(R^(-(1-c)/c)) in the refined energy error gives E(R)-L R^alpha=O(R^(5-3/c)); both terms have that exponent. Thus an exact exterior homogeneous tail requires its constant energy offset to vanish when c<3/5. This remains a necessary matching condition, not an exact Euler example.

The literature-history sentences and the separately stated TheoremW depend on earlier audits and are not independently recertified from primary sources here. In particular a nonnegative weak defect cannot be silently replaced by zero defect. The proof above establishes the C1 energy theorem at its exact hypotheses and no stronger Euler nonexistence result.

## 8. Bounded-background normalization

The report's CorollaryA.5 removes the dilation hypothesis at the cost of a constant background and a spatial translation. Here is a separate check. With U merely bounded and still C1, the equation in divergence form makes grad P tempered. The canonical G is also tempered by its defining estimates. The harmonic distribution H=grad P-G is a polynomial. The rescaled equation and the R^-1 estimate for G show H(R.) bounded on every fixed test as R tends to infinity. A nonconstant polynomial would contradict this on a test pairing nontrivially with its top homogeneous term. Thus H=g0 is a constant vector.

Let M=(1-c)I+omega J, which is invertible since1-c>0. Any weak-star subsequential limit v of U(R.) is bounded and satisfies

    Mv+(Az.grad)v+g0=0.

The quadratic term vanishes because it is multiplied by R^-1. Put b=-M^-1 g0 and w=v-b. Solving the transport equation on transformed test functions gives

    w(exp(tA)z)=exp(-tM)w(z).

An invertible linear change of variables preserves the essential supremum, while exp(-tM) is exp(-(1-c)t) times an orthogonal matrix. Hence ||w||_infinity=exp(-(1-c)t)||w||_infinity and w=0. Weak-star subsequences exist because L1 is separable; since every subsequential limit is b, the whole dilation family tends weak-star to b.

A is invertible since c>0. Set z0=-A^-1 b, W(y)=U(y+z0)-b and Ptilde(y)=P(y+z0)+(Mb).y. Then A(y+z0)+U(y+z0)=Ay+W(y). Direct substitution proves the same profile equation for W,Ptilde. Translations of L1 tests by z0/R tend in L1 to the original tests, so W satisfies the dilation-zero hypothesis. Sections1-6 apply to W. This proves the printed background conclusion, and introduces no nonconstant decaying counterexample.

## 9. Verification record

All483 report lines in Section2A and the entire99-line Theory Agent A  recheck were read. The Theory Agent A  addendum lists the same constants, exponents, pressure normalization and critical-tail iteration independently recomputed above. Its mathematical conclusions agree. The same pin is the input for the conditional helicity theorem, whose use of E(R)<=C R^alpha remains valid at the critical endpoint alpha=0 as well.

 Formal verification is not claimed. The primary proof of an external theorem is never replaced here by an unexamined citation or a numerical result.
