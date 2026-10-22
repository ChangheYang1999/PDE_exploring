# Resonant logarithms in the exact modal trial's cubic-axis integrand

Topic60. This standalone proof precedes its exact-input arithmetic application. Its scope is the specific modal trial and the validity of a proposed finite-part calculation. It supplies neither existence nor exclusion of a nearby IPM solution.

## 1. Exact density and notation

Let the inner factor of the normalized trial be

    a(r,theta)=1+sum_(j=1)^7 (r/R)^(2j) D_j(theta)
                  +(r/R)^bi P(log(r/R),theta),
    D_j(theta)=sum_(m=0)^(M-1) D[m,j-1] cos(2m theta), R=exp(t_a), bi>49.

P is a finite polynomial in its logarithmic argument with a finite even Fourier expansion. The exterior is the canonical sublinear extension in the exact modal-repair construction; the join corrections and strain repair preserve the D entries. Put rho=x²y a, U=(-psi_y,psi_x), V=c_l X+U, and obtain psi from -Delta psi=rho_x by the full-plane Green formula. The canonical normalization is c_l=(1+psi_xy(0))/3. Define A=2c_l-1>0, D_s=4c_l-1, p=6+2/A, and suppose 6<p<7.

On the positive x-axis set

    w=V1(x,0), v1=V2_y(x,0), G1=rho_y(x,0), G3=rho_yyy(x,0)/6,
    w2=V1_yy(x,0)/2, v3=V2_yyy(x,0)/6,
    f=-(w2 G1'+v3 G1), q=(3v1-1)/w,
    E=-integral_0^x(q(t)+p/t)dt, H=x^-p exp(-E),
    Q_f=x exp(-E) f/w.

These are definitions for the trial, which need not satisfy the profile equation. Smoothness on the punctured axis permits every derivative used below; the explicit finite inner expansion controls the remainders.

Write d_m=D[m,0], and define two exact angular coefficients before the common factor R^-2:

    h7=(d2+d3-d4-d5)/8,
    b2raw=sum_m (1-2m²)d_m.

Assume M>=6, with missing coefficients interpreted as zero for the general identity. Set H7=h7/R², b2=b2raw/R² and lambda=3H7. The application below must independently check h7 and b2raw are nonzero from the pinned exact input.

## 2. The resonant Green term

The degree-five density is r5 sum_l H_l sin(l theta). The identity

    cos²(theta) sin(theta)=(sin(theta)+sin(3theta))/4

and the product-to-sum formula give its frequency-seven coefficient H7 above. Differentiating a single term gives

    partial_x[r5 sin(l theta)]
       =r4[(5-l)sin((l+1)theta)+(5+l)sin((l-1)theta)]/2.

Thus the coefficient of r4 sin(6theta) in rho_x is 6H7. The l=5 contribution is zero; the l=7 contribution is 6H7. The polar Laplacian identity is

    Delta[r6 log(r) sin(6theta)]=12 r4 sin(6theta).

Consequently the particular stream at this resonance is

    psi_log=-(H7/2)r6 log(r) sin(6theta).

On y=0,x>0, partial_y[r6 log(r) sin(6theta)]=6x5 log(x). Since U1=-psi_y, the coefficient of x5 log(x) in w is lambda=3H7.

This coefficient cannot be changed by the far field or the canonical strain. For forcing r^s sin(n theta), the nonresonant particular stream is -r^(s+2) sin(n theta)/((s+2)²-n²), and at n=s+2 the term is -r^n log(r) sin(n theta)/(2n). The regular homogeneous terms are r^n sin(n theta); the lower Green integral excludes r^-n. The cubic density x²y has only the nonresonant forcing partial_x(x²y)=2xy=r² sin(2theta). Applying the derivative formula with degree three gives frequency-two contributions (3-1)/8+(3+3)/8=1, not 5/2. All other density terms have degree at least seven or bi+3>52. Hence, with constants w3,w5 determined by the entire canonical field,

    w=-Ax+w3 x³+lambda x5 log(x)+w5 x5+O(x7(1+|log x|)).       (1)

Expansion (1) holds on 0<x<R, with remainder W obeying |W^(j)(x)|<=C_j x^(7-j)(1+|log x|) for j=0,1,2,3. This follows by differentiating each of the finitely many displayed modal particular solutions and regular homogeneous terms. The join repair changes the inner high-order term (r/R)^bi P; it does not leave the entire inner density unchanged. Its particular solutions have stream degree at least bi+4, so their axis velocities have degree at least bi+3. The far-field contribution is harmonic on r<R and changes only the regular homogeneous terms. Powers arising from P remain far above the displayed orders even after differentiation. No unknown remainder constant is used as a numerical enclosure.

## 3. The logarithm in Q_f

The density expansion gives integer-power axis traces

    G1=x²+g4 x4+g6 x6+O(x8),
    G3=b2 x²+b4 x4+b6 x6+O(x8).                              (2)

For b2, expand (x²+y²)cos(2m arctan(y/x))=x²+(1-2m²)y²+O(y4/x²), and multiply by x²y. This proves its formula without taking nonexistent general fifth derivatives at the origin.

Divergence and curl give, independently of stationarity,

    v1=2c_l-w', w2=(G1'-w'')/2, v3=-w2'/3.

From (1), the first logarithmic terms in w2 and v3 are respectively -10lambda x³log(x) and 10lambda x²log(x). Thus f has first logarithmic term

    f=f2 x²+10lambda x4 log(x)+f4 x4+O(x6(1+|log x|)).        (3)

Products with the integer terms of G1 cannot alter this coefficient. Furthermore q=-p/x+O(x)+O(x³log x), E=O(x²)+O(x4log x), and x/w=-1/A+O(x²)+O(x4log x). Substituting (3) yields

    Q_f=q2 x²-(10lambda/A)x4 log(x)+q4 x4
                              +O(x6(1+|log x|)).             (4)

Therefore if h7 is nonzero, Q_f has a nonzero x4log(x) coefficient, namely -30H7/A. No constants q2,q4,q6,K can satisfy

    |Q_f-q2x²-q4x4-q6x6|<=Kx8

near zero. To prove this, first divide by x² to determine q2; then divide the remaining expression by x4. Formula (4) diverges logarithmically, whereas the proposed expression would have a finite limit q4.

This refutes the application of the polynomial-only B1 finite part and the associated O(x8) cutoff bound to this trial's Q_f. It does not refute the conditional B1 theorem for integrands satisfying its hypotheses.

## 4. Adding the cubic defect does not restore the polynomial-only hypothesis

Define the actual cubic defect E3=wG3'+(3v1-1)G3-f. Then

    Q_total=x exp(-E)(f+E3)/w=x^(p+1)(H G3)'.                (5)

The x4log(x) term in Q_f cancels against the defect. There is nevertheless a later logarithm. Put F=-w/(Ax). Direct differentiation gives

    E=3 log F-(p-3) integral_0^x (F(t)-1)/(t F(t))dt.

Since the first logarithm in F is -(lambda/A)x4log(x), the first logarithm in E has coefficient (p-15)lambda/(4A). The first logarithm in exp(-E) consequently has coefficient

    C_log=(15-p)lambda/(4A)

at x4log(x). Multiplying by (2) and differentiating in (5) gives

    Q_total=Q2 x²+Q4 x4+(6-p)C_log b2 x6 log(x)+Q6 x6
                             +O(x8(1+|log x|²)).             (6)

If h7 and b2raw are both nonzero, this logarithmic coefficient is nonzero because 6<p<7 and A>0. The same limit argument at order six rules out an O(x8) remainder after only polynomial subtractions. Thus the plain B1 finite-part functional cannot be applied even to f+E3 as written in the lead's C1.

The integer-power density trace still has no x^p term. A generalized finite part with logarithmic subtractions can express that fact. Locally HG3 has only powers x^(2j-p), possibly multiplied by log(x), through its divergent orders, and its remainder is O(x^(8-p)(1+|log x|²)), which tends to zero. Since p is noninteger, none of the retained powers is zero. Subtracting all these divergent powers and logarithmic powers therefore leaves constant zero. For example an x^j log(x) term in Q has primitive

    x^(j-p)[log(x)/(j-p)-1/(j-p)²].

This defines the required logarithmic subtraction; a polynomial fit omits it. Relating this local constant to an endpoint integral also requires the trial's correct source exponent (3v1(L)-1)/w'(L) and the endpoint condition HG3->0. These hold under positive source exponent and bounded G3, but are not assumed from an exact-profile identity v1(L)=1. This note makes no claim about a validated value of B3[f] in any generalized convention.

## 5. Evidence obligations and scope

The check uses the exact JSON coefficients and independently parses the original binary NPY payload, including its Fortran layout. It reconstructs the whole degree-five forcing by two distinct algebraic methods: trigonometric differentiation and complex Laurent differentiation. It checks the resonant Laplacian and the local logarithmic coefficients symbolically. Arb and mpmath.iv then separately enclose H7, b2, lambda and both integrand logarithmic coefficients, using different exponential formulas and independently verified rational brackets. No sampled nonzero value is proof of nonzero.

Dependencies: exact modal definition and canonical normalization from modal_repair; inner finite expansion from inner_majorant; the elementary div/curl and integrating-factor identities rederived here and in b3_coefficient. The singularity is in the trial and invalidates a particular estimator assumption. A nearby smoother exact profile is not excluded. No decisive endpoint follows.
