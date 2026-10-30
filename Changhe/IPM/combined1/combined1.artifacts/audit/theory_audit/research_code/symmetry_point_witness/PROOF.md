# Symmetry improves the necessary pointwise correction bound

## Statement

Let 0<s<=1/2. Let h be a real function in H^(2+s)(R²), even in x and odd in y. For every |y|>=1/2,

|D h(0,y)|=|h_y(0,y)| <= [16pi s(1+s)]^(-1/2) ||h||_(H^(2+s)).       (1)

This improves the unrestricted directional gradient constant by sqrt(2). It uses the position (0,y) and parity, not an additional derivative assumption.

For the baseline high norm Ns=E2(J^s h), where

E2(h)²=||omega D²h||²+2^14||Dh||²+2^18||h||²+2^18(20/21)||h||_H²,
omega=(1+4|X|²)^(2/5), H=dot H^-1,

we have ||h||_(H^(2+s))<=Ns(h). Fix a smooth S1 reference rho, its fixed exponent c, velocity U[rho]=(-R1R2 rho,R1²rho), stationary residual F and drift V=cX+U[rho]. If h is an exact S1 stationary correction and Ns(h)<=r, then at X=(0,y), |y|>=1/2,

|F(X)| <= [C1s |V(X)|+C0(1+|D rho(X)|)]r+C0 C1s r²,                 (2)

where C0=[4pi(1+s)]^(-1/2) and C1s=[16pi s(1+s)]^(-1/2).

In particular, suppose for some 0<mu<=3/10 the ball has positive scalar gap

mu-4800s-5r/sqrt(s)>0.                                            (3)

Then every exact stationary correction in the ball necessarily satisfies

|F(0,y)| < (87/10000)|V(0,y)|
          +(53/1000000)(1+|D rho(0,y)|)+1/2000000.                (4)

Thus a strict violation of (4) excludes the exact reference from every such ball, including every positive-gap ball using the audited base rate297/1000. This is not a claim about arbitrary component boxes, modified norms or inverse estimates with different rough costs.

## 1. Parity and the reproducing kernel

Use hat f(xi)=integral e^(-iX.xi)f(X)dX and Sobolev norm squared (2pi)^(-2) integral (1+|xi|²)^(2+s)|hat f|² dxi. The kernel for point evaluation is

G_s(X)=(2pi)^(-2) integral e^(iX.xi)(1+|xi|²)^(-2-s)dxi.

For h even in x and odd in y, h_x(0,y)=0. Projection of the derivative evaluation functional h_y(0,y) onto the odd-y subspace replaces exp(i y xi_y) by cos(y xi_y). The resulting representer is already even in x. Its squared norm is consequently

(2pi)^(-2) integral xi_y² cos²(y xi_y)(1+|xi|²)^(-2-s)dxi
=(1/2)[C1²-G_s''(2|y|)],                                      (5)

where the prime denotes differentiation along the y axis and

C1²=(2pi)^(-2) integral xi_y²(1+|xi|²)^(-2-s)dxi
    =1/[8pi s(1+s)].

All these integrals converge absolutely for s>0. Cauchy-Schwarz proves the derivative bound with the constant in (5). It remains to show G_s''(r)>=0 for r>=1 and 0<s<=1/2.

## 2. Sign of the reflected derivative covariance

The gamma integral and two-dimensional Gaussian Fourier integral give, for r>0,

G_s(r)=1/[4pi Gamma(2+s)] integral_0^infinity t^s exp(-t-r²/(4t))dt.

Differentiation under the integral is justified by exponential decay at both endpoints. Define

K_nu(r)=integral_0^infinity exp(-r cosh u) cosh(nu u)du.

The substitution t=(r/2)exp(u), and pairing u with -u, gives

integral_0^infinity t^(nu-1)exp(-t-r²/(4t))dt=2(r/2)^nu K_nu(r).

Differentiating the preceding heat integral twice and using this identity yields

-G_s''(r)=(r/2)^s/[4pi Gamma(2+s)] [K_s(r)-r K_(1-s)(r)].          (6)

For 0<s<=1/2 and u>=0, cosh(su)<=cosh((1-s)u). The integral definition implies K_s(r)<=K_(1-s)(r). If r>=1, the bracket in (6) is nonpositive. This proves the desired sign. Substituting in (5) gives squared constant at most C1²/2, proving (1). This argument needs no numerical Bessel evaluation or unproved covariance sign.

## 3. Stationary equation

The high norm dominates H^(2+s), since omega>=1 and

|xi|^4+2^14|xi|²+2^18 >= (1+|xi|²)².

The standard point evaluation integral gives |h(X)|<=C0 Ns(h). Every scalar projection of U[h] has Fourier multiplier bounded by one, so |U[h](X)|<=C0 Ns(h) as well. These vector bounds follow by taking the supremum over unit scalar projections; they do not add an unnecessary factor sqrt(2).

Expand the fixed-exponent stationary equation as

0=F+V.Dh-h+U[h].D rho+U[h].Dh.

At the specified axis point, (1) bounds |Dh| by C1s r. Applying the preceding point bounds to the remaining factors proves (2). The equation may initially hold distributionally: h in H^(2+s) has continuous first derivatives, and U[h] has the same Sobolev regularity, so every displayed term is continuous and the equality holds pointwise.

## 4. Uniform rational corollary

Condition (3) implies s<mu/4800<=1/16000, so the hypothesis s<=1/2 of (1) is automatic. Also

r < sqrt(s)(mu-4800s)/5.

The maximum of the right side over 0<s<mu/4800 is attained at s=mu/14400 and equals mu^(3/2)/900. Hence, using pi>3,

C1s r < mu/(20sqrt(pi)) <=3/(200sqrt(3)) <87/10000,
C0 r < mu^(3/2)/(1800sqrt(pi)) <=1/(6000sqrt(10)) <53/1000000.

The second displayed middle bound follows by squaring both sides at mu=3/10 and pi=3. Finally

(C0 r)(C1s r) < (53/1000000)(87/10000) <1/2000000.

Substitution in (2) proves (4). Every relaxation has the direction needed for a necessary upper bound.

## 5. Data contract and scope

To apply (4), supply outward interval enclosures for the exact reference's |F(0,y)|, |V(0,y)| and |D rho(0,y)| at a rational point with |y|>=1/2. The lower endpoint of |F| minus the upper endpoint of the right side must be positive. The source must satisfy S1 and use the same fixed exponent and velocity convention. This application needs no global residual-norm bound or background coercivity certificate.

The copied N4 Cartesian witnesses are independently evaluated inputs. The companion script only applies rational arithmetic to those intervals and checks the rational constant relaxations. This theorem is a new T4 argument, requiring independent T1/T2 review before promotion from CLAIMED to AUDITED. Its conclusion concerns the stated scalar-gap family, not every possible rigorous existence framework.
