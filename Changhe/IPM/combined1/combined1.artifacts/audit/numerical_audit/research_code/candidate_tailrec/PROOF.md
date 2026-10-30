# Exact nonintegrable tail recurrence for a finite candidate list

## Statement, chart and hypotheses

Fix a finite exact rational potential of the campaign generator form

    chi=sum a_(j,m,w,n,q,R) H_m(x,y)(1+r^2)^(p_j-m)
                                   t_R^w u_R^q P_n(2t_R-1),
    H_m=Re(x+i y)^(2m), t_R=r^2/(R^2+r^2), u_R=1-t_R,
    p_j=(3+gamma-j delta)/2, gamma=1/c, delta=1-gamma.

All indices are nonnegative integers, each R>0 is rational, and c is the
exact rational4076476460239181/2251799813685248. Hence1/2<gamma<3/5 and,
with e_j=gamma-j delta, e_3>-1>e_4. Set

    rho=-chi_xxy-chi_yyy, psi=chi_xy,
    u=(-chi_xyy,chi_xxy)=(-psi_y,psi_x).

For j=0,1,2,3 define the entire leading potential profile

    C_j(theta)=sum_(m,w,n,R) a_(j,m,w,n,0,R) cos(2m theta).

Only q=0 contributes. All coefficients are summed exactly. Let Theta_j
and Psi_j be the resulting density and stream coefficients at radial
powers r^e_j and r^(e_j+1), respectively. The certificate compares every
coefficient with the independently accepted007 profiles and tests

    [partial_theta^2+(e_j+1)^2]Psi_j
                =-e_j cos(theta)Theta_j+sin(theta)Theta_j',       (1)

and, for j=1,2,3,

    j(c-1)Theta_j = sum_(l+m=j-1)
          [-e_m Psi_l' Theta_m+(e_l+1)Psi_l Theta_m'].            (2)

For every candidate whose exact result says all coefficients in(2) are
zero, these are exact finite algebraic identities. Failure or differing
profiles is reported explicitly. No floating tolerance is used. The
source list and each raw hash are specified in verification/result.json.

This is the numerical coefficient requirement NC-T-TAILREC in theory_v04.
The theorem forcing(2) for a distributional solution requires its
separate asymptotic-chart, canonical-velocity and remainder hypotheses.
Satisfying(2) is necessary in that chart and is not sufficient for a
solution, a controlled remainder, an inverse or an existence proof.

## Extracting the complete leading profile from scaled generators

As r tends to infinity, t_R tends to1, u_R=R^2 r^-2+O(r^-4),
P_n(2t_R-1) tends to P_n(1)=1, and

    H_m(1+r^2)^(p_j-m)=r^(2p_j)cos(2m theta)(1+O(r^-2)).

The finite generator has a convergent expansion in r^-2 sufficiently
far out. It and its derivatives through every fixed order may be
differentiated there term by term. Thus a q=0 term contributes exactly
its coefficient to C_j. A q>=1 term starts at least two powers lower.
Third derivatives produce density and velocity; their leading powers
are e_j-2q. Because gamma-2<-1 and e_4<-1, no q>=1 or j>=4 term
contributes to any density or velocity exponent greater than or equal
to-1. There is no omitted branch at the L2 boundary in this finite list.

For an independent Cartesian computation form the smooth surrogate

    chi_sur=sum_(j=0..3,m) A_jm H_m(1+r^2)^(p_j-m),
    A_jm=sum_(w,n,R) a_(j,m,w,n,0,R).

Its leading potential is exactly the same C_j. It differs from the full
potential by terms lower by at least two powers in these four branches.
Consequently its derivative leading coefficients through order4 equal
the full potential's corresponding coefficients. The surrogate is used
only to extract these tails. It is not asserted to equal the candidate
on the plane, at the origin, or in any norm.

The audited Cartesian recurrence represents an order d derivative as

    (1+r^2)^p_j r^-d A_(j,l,d)(t) trig_l(theta),
    t=r^2/(1+r^2).

Its leading coefficient is exactly A_(j,l,d)(1). For the surrogate the
initial polynomial is A_jm t^m. The extraction therefore uses the same
independently checked Cartesian derivative engine as the prior007 tail
certificate, without importing the publisher's homogeneous-sector code.

## Exact verification of every recurrence coefficient

Represent trigonometric polynomials as Laurent polynomials in
z=exp(i theta) over Q[i]. Products are exact finite convolution and
angular derivatives multiply the coefficient of z^n by i n. This
includes every angular frequency and has no quadrature aliasing.

Extract rho,psi,u1,u2,rho_x,rho_y in each of the four branches. Recover
U_r=cos(theta)u1+sin(theta)u2 and
U_theta=-sin(theta)u1+cos(theta)u2. Check U_r=-Psi_j' and
U_theta=(e_j+1)Psi_j. Check both Cartesian density gradient profiles
against polar differentiation, and then(1). These checks verify the
sign conventions and derivative reconstruction independently.

The Cartesian product

    B_j=sum_(l+m=j-1) [u1_l (rho_x)_m+u2_l (rho_y)_m]

has radial exponent e_l+e_m-1=e_j. Compare it with the polar right
side of(2) using exact Laurent convolution. The stationary dilation
coefficient is c e_j-1=-j(c-1), so the residual coefficient is exactly
B_j-j(c-1)Theta_j. Its complete map must vanish for a passing candidate.
For candidates matching007, the potentially nonzero positive sine
frequencies are1..39,1..59,1..79, with20+30+40=90 coefficient checks.
All other frequencies are also checked by complete map equality.

## Source handling and scope of independent reproduction

Only locally frozen immutable snapshots are executed or parsed as
numerical inputs. SHA256SUMS, manifest, raw exact coefficient strings
and the candidate's exact c are checked. All source indices and scales
are validated. The source and derived tail hashes are recorded, along
with the executed own modules, the prior independent007 acceptance,
theory_v04 hash and actual elapsed times. Identical profile outputs may
refer to the one hash-bound prior exact profile file; differences are
recorded explicitly. No source-owned cache or output is written.

This certificate concerns the finite nonintegrable prefix. It does not
certify the full far-field residual, a remainder beyond that prefix,
spatial background constants, or feasibility of any correction ball.
A correct leading recurrence can coexist with a large residual and a
rigorously excluded nearby ball, as other campaign checks demonstrate.
