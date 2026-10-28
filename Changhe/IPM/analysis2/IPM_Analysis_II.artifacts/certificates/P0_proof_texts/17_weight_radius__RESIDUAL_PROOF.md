# Annular lower bound for the accepted weighted residual

Status: independently checked analytical proof and768-bit original-source certificate, CONFIRMED V089. The argument was written before its certificate run.

## Statement and spaces

Use the exact accepted state 131 reconstructed from the read-only original in `../source_audit/state131_exact.json`, and its canonical velocity. Put c=c_l, gamma=1/c, delta=1-gamma, q=2gamma-1, R=2^32, w=(1+r^2/R^2)^(-11/10). For a parity density f, let L(f)=||wf||_{dot H^{-1}} and N_s^w(f)=E_w(J^s f), with E_w^2=P2^2+2^22 P1^2+2^53 L^2 as in this topic's PROOF.md. The bounded inverse Bessel estimate in ../16_weighted_fractional/SHARP_LOW_COMMUTATOR_PROOF.md gives

    N_s^w(f) >= 2^(53/2) L(f)/6,  0<s<=2^-12.

The present proof will give a lower bound for f=F(rho_131). It uses only an explicit compactly supported homogeneous H1 test, exact rational Fourier algebra, and rigorously bounded omitted binomial terms.

## The test function

Fix an odd positive integer m and let chi(t)=(t-1)^2(2-t)^2 on 1<=t<=2, zero elsewhere. Let phi(r,theta)=sign(e_m) chi(r/R) sin(m theta), where e_m is the leading coefficient of F. This test is C1, compactly supported, and has the required even-x, odd-y parity. Direct polynomial integration gives

    integral chi(t) dt=1/30,
    integral chi(t)^2 dt=1/630,
    integral t chi'(t)^2 dt=1/35.

Consequently ||Dphi||_2^2=pi integral[t chi'^2+m^2 chi^2/t]dt <=pi(1/35+m^2/630). Suppose for every r>=R the sin(m theta) coefficient of F has sign e_m and absolute value at least b r^q. Since q+1>0 and w>=5^(-11/10) on the test annulus,

    |<wF,phi>| >= pi b R^(q+2) 5^(-11/10)/30,
    L(F) >= sqrt(pi) b R^(q+2) 5^(-11/10)
                    /(30 sqrt(1/35+m^2/630)).                 (1)

The inequalities below verify a positive b without numerical quadrature.

## Exact finite sectors and uniform tail error

Each canonical potential summand is v r^(2k)(1+r^2)^(p_j-k) cos(2m theta), with p_j=(3+gamma-j delta)/2, 0<=j<=3 and |p_j-k|<26. Retain binomial orders 0<=a<=Q. Their density powers are gamma-j delta-2a. Differentiate the angular monomials exactly to obtain the truncated density rho_t, velocity u_t and residual F_t. The residual powers are gamma-j delta-2a, with linear and quadratic coefficients combined exactly. The leading gamma term vanishes because c gamma=1. All remaining powers are <=q.

Write A_j=sum_{branch j}|v| and a0=Q+1. For d=3,4 define

    M_d=sum_(j,a<=Q) B_(d,j,a) R^(-j delta-2a),
    tau_d=((a0+26)/(a0+1))
                    *((2a0+34)/(2a0+32))^d/R^2,
    T_d=binom(a0+25,a0)(2a0+32)^d R^(-2a0)
                    sum_j A_j R^(-j delta)/(1-tau_d).

Here B_(d,j,a) is the maximum, over Cartesian components of the d-th derivative of its potential sector, of the sum of absolute angular coefficients. These are exact rational numbers. The ratio test is valid because the binomial coefficient majorant is binom(a+25,a), and every Cartesian derivative multiplies the angular coefficient norm by at most 2a+32 for d<=4. Indeed |gamma+3-j delta-2a|+2m+2(d-1)<2a+32 for the archived indices. The displayed ratio decreases in a. Thus, for r>=R, each potential derivative component satisfies

    |D^d chi_t| <= M_d r^(gamma+3-d),
    |D^d(chi-chi_t)| <= T_d (R/r)^(2a0) r^(gamma+3-d).

The density is a sum of two third derivatives and each velocity component is one third derivative. Hence the tensor bounds give

    |rho-rho_t| <=2T3 r^gamma (R/r)^(2a0),
    |u-u_t| <=sqrt(2)T3 r^gamma (R/r)^(2a0),
    |D(rho-rho_t)| <=2sqrt(2)T4 r^(gamma-1)(R/r)^(2a0),
    |u_t| <=sqrt(2)M3 r^gamma,
    |D rho_t| <=2sqrt(2)M4 r^(gamma-1).

Since 2a0>delta, the full pointwise residual difference obeys, uniformly for r>=R,

    |F-F_t|/r^q <= Ctail,
    Ctail=(2sqrt(2)c T4+2T3) R^delta
                      +4(T3 M4+M3 T4+T3 T4).                  (2)

The normalized sin(m theta) coefficient of an error bounded by Ctail is at most (4/pi)Ctail<2Ctail. Let

    B_m=sum_(p<q)|coefficient_(p,m)(F_t)| R^(p-q).

Then b=|e_m|-B_m-2Ctail is a valid lower bound for the signed normalized coefficient at every r>=R. The certificate encloses (1), (2), B_m and b using Arb from exact rational inputs. The source hash, precision, exact sector coefficients, derivative component bounds and all final lower bounds are recorded. A float is never used to prove a bound.

## Combining angular tests

The single-mode tests are orthogonal in the gradient inner product. To obtain one explicit improved test, put d_m=1/35+m^2/630 and use

    phi=chi(r/R) sum_m (e_m/d_m) sin(m theta).

All coefficients of this angular polynomial are exact rationals. If b_m>0 are the bounds proved above, its squared gradient norm is at most pi sum_m e_m^2/d_m, and its pairing is at least pi R^(q+2)5^(-11/10) sum_m |e_m|b_m/d_m /30. Dividing gives the combined lower bound recorded by the certificate. This is one test function, not a sum of incompatible estimates.

## Certified conclusion

The program verification/annular_residual.py reconstructs the original coefficients and retains eight potential sectors (Q=1). All twenty odd modes1 through39 have positive signed coefficient bounds. The combined rational test proves

    L_(2^32)(F_131)>563055561251943055,
    N_(s,2^32)(F_131)>8906250109564824650127350>2^82,
                         0<s<=2^-12.

At s=2^-30 and eta=2^-46, the strict sufficient-smallness gap is greater than2^128. Three independent Cartesian evaluations of the complete original potential also satisfy the uniform omitted-binomial error bound. These point checks supplement the analytic continuum bound. No value from the older radius was inserted in this norm.

## Scope

This is a lower bound on the weighted norm of one exact reference residual, not an obstruction to all nearby exact solutions or a lower bound over an optimized family. The same test argument applies to a repaired residual only after its actual annular coefficient and error are separately checked. In particular the P14 repairs cancel all residual powers >=-2, so their original growing sector cannot be inserted in (1).
