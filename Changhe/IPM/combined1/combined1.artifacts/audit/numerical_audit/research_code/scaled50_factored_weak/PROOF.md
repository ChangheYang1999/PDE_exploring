# Complete weak tests with scaled generators and factored radial localization

## Statement, reference class and correction hypotheses

Fix an exact rational c>1, gamma=1/c and delta=1-gamma. Let the reference
potential be a finite exact rational sum of

    chi_jmwnqR = H_m(x,y) (1+r^2)^(p_j-m)
                         t_R^w u_R^q P_n(2t_R-1),
    H_m=Re(x+i y)^(2m), p_j=(3+gamma-j delta)/2,
    t_R=r^2/(R^2+r^2), u_R=R^2/(R^2+r^2),

where j,m,w,q,n are nonnegative integers, P_n is the Legendre polynomial
and R belongs to {1,10,50,100}. Define the smooth reference fields

    rho=-chi_xxy-chi_yyy, u=(-chi_xyy,chi_xxy),
    F=(cX+u).grad rho-rho.

They obey div u=0. Assume the separately checked leading and forbidden
sectors required by the candidate's registered function class. In
particular rho and u are O(r^gamma) at infinity and are smooth at zero.

Let h be an S1-symmetric L2 correction for which rho+h satisfies the
stationary equation at this same c, in distributions. Require a canonical
divergence-free velocity U[h] in L2 with ||U[h]||2<=||h||2 and locally
integrable products in that weak equation. These are explicit hypotheses,
not outputs of the numerical calculation.

Choose odd n>=1 and integer K>=(n-1)/2, and set

    t=r^2/(1+r^2), v=1/(1+r^2),
    phi=r v^2 t^K sin(n theta),
    Mfield=(2c+1)phi+(cX+u).grad phi,
    Cfield=phi grad rho, I=integral F phi,
    M=||Mfield||2, C=||Cfield||2, H=||grad phi||infinity.

Then phi is smooth at zero: r^(2K+1)sin(n theta) is a harmonic polynomial
of degree n times an even nonnegative power of r. Its denominator is
smooth and positive. It is O(r^-3) at infinity, with bounded gradient.
All displayed reference products are integrable under the stated growth.

The weak identity and Cauchy-Schwarz give the necessary inequality

    |I| <= (M+C)||h||2 + H||h||2^2.                       (1)

Consequently positive L<=|I| and containing upper bounds Mbar,Cbar,Hbar
prove

    ||h||2 >= 2L/(Mbar+Cbar
                +sqrt((Mbar+Cbar)^2+4Hbar L)).           (2)

This is a conditional necessary distance. A positive value excludes only
specified smaller correction balls. It neither constructs a solution nor
an inverse. Moving c requires the separate leading-tail pinning theorem.

## Proof of the weak inequality

Expand the stationary equation at rho. The reference term is F. Testing
the terms cX.grad h+u.grad h-h and integrating by parts gives
-integral h Mfield, since div(cX+u)=2c. The other linear term is
U[h].grad rho and is bounded by C||U[h]||2. The quadratic term gives
-integral h U[h].grad phi and is bounded by H||h||2||U[h]||2.
The L2 velocity contraction proves (1); solving the nonnegative quadratic
proves (2). Smooth radial cutoffs justify the integrations. The reference
boundary terms vanish because gamma<1 and phi decays as r^-3. Correction
terms vanish by L2 tail convergence, Cauchy-Schwarz and the bounded probe
gradient. The same argument gives the independent identity

    I=-integral rho Mfield.                              (3)

## Exact scaled fields

For a=R^2-1 and L(t)=1+a(1-t), the radial numerator of one potential is

    A(t)=t^(m+w)(R^2(1-t))^q P_n(2t/L-1)/L^(w+q).

The finite rational class has poles L=1+99v,1+2499v,1+9999v, all strictly
positive for 0<=v<=1. A common-denominator polynomial equality therefore
implies functional equality on the whole radial interval. Exact division
by t^k requires the first k numerator coefficients to vanish.

A derivative of total order d is S^p r^(-d) A(t) trig_l(theta), S=1+r^2.
Its radial numerator is 2t(1-t)A'+(2pt-d)A. With
B=t A'+t(pA-t A'), x differentiation gives shifted numerators
B+(l-d)A/2 at l-1 and B-(l+d)A/2 at l+1. For y differentiation of sine
the signs are plus and minus, and for cosine minus and plus. Negative
sine frequencies change sign, negative cosine frequencies do not, and
sin(0 theta)=0. These identities derive every physical Cartesian field
without rounding coefficients. Mixed derivatives commute algebraically.

## Factored probe assembly

Keep t^K outside coefficient arrays. Its radial probe factor is

    B_K(t)=(2K+1)-(2K+4)t,
    partial_r phi=v^2 t^K B_K(t) sin(n theta),
    r^(-1)partial_theta phi=n v^2 t^K cos(n theta).

The x derivative shifts n to n+1 and n-1 with coefficients (B_K-n)/2
and (B_K+n)/2. The y derivative has cosine frequencies n-1 and n+1
with coefficients (B_K+n)/2 and (n-B_K)/2. Multiplying by every velocity
mode constructs Mfield, including its drift coefficient
(2c+1)+c B_K. Multiplying phi by every density-gradient mode constructs
both components of Cfield. Ordinary trigonometric product identities
supply the signs, frequency folding and factor1/2.

Each component consequently has the exact form

    r v^2 t^K sum_(ell,kind,l) v^(ell delta/2)
                                   A_(ell,kind,l)(t) trig_l(theta). (4)

All nonzero frequencies l are odd and positive. Angular orthogonality
and r dr=-dv/(2v^2) imply

    norm(field)^2 = pi/2 sum_(matching angular pairs)
       integral_0^1 v^(1+(ell+ell')delta/2) (1-v)^(2K+1)
                                      A(1-v)B(1-v)dv.    (5)

Distinct radial branch pairs have multiplicity2; each vector component
is included. The density is r sum v^(ell delta/2)R_ell(t)sin(l theta),
with ell>=1. Thus (3) is the finite sum

    I=-pi/2 sum_(matching angular pairs)
       integral_0^1 v^((ell+ell')delta/2-1) (1-v)^(K+1)
                                      A(1-v)R(1-v)dv.    (6)

An independent direct F/r projection uses all Cartesian linear terms
and all angular-compatible velocity/gradient pairs, then multiplies by
the probe. Its scalar measure is the same as (6). Direct and parts
pairings must give overlapping containing intervals with adequate bits.
All exponents in (5) exceed -1. In (6), ell+ell'>0 makes the exponent
strictly greater than -1. Positive poles cannot change integrability.

Each integral is exactly the moment proved in
../factored_pole_moments/PROOF.md, with localization integer2K+1 orK+1.
The exact partial fraction identity is replayed. Every pole-power
recurrence is compared with the direct hypergeometric formula; accuracy
failures reject a result. There is no radial cutoff, angular quadrature
or omitted angular sector.

## Exact gradient cap

For K>=1, write B=2K+4. The maximum over theta of |grad phi| is the
larger of the absolute radial and angular amplitudes

    v^2(1-v)^K(-3+Bv), n v^2(1-v)^K.

For the radial amplitude, the derivative after removing a nonnegative
factor vanishes at the two roots in (0,1) of

    -6+(9K+18)v-B(K+3)v^2=0.

Its discriminant is3(K+2)(11K+6)>0. The angular amplitude has its unique
interior maximum at v=2/(K+2). All endpoint amplitudes are zero. Evaluating
these three critical amplitudes in outward balls and choosing a strictly
larger positive rational Hbar proves the bound on the full Euclidean
gradient. No background scale enters this calculation. K=0 needs its
separate endpoint treatment and is not covered by this implementation.

## Verification plan and scope

Before a new candidate run, check mixed radius50 and other-scale
manufactured fields against independent Cartesian Taylor jets through
order4, including all mixed derivatives. Check the R=1 restriction
coefficientwise against the polynomial engine, and the radius10/100
restriction against the accepted scaled engine. At small K, exact
multiplication by t^K must recover ordinary probe assembly. At n21,K522,
the complete R=1 moments, M/C norms, pairings and root must reproduce
the accepted candidate013 record. The new scalar fixtures include mixed
poles and large localization exponents.

The proof and these checks precede any candidate certificate. Raw exact
JSON, candidate/source hashes, every module used, all interval records,
field hashes, real times, calibration evidence and independent review
are retained alongside this proof. Accepted earlier modules are not
modified. New candidate outputs remain OPEN until independently audited.

## Version and exact scale change

This separate version replaces the radius25 pole624 by the radius50
pole2499. The other two poles99 and9999 remain available. It does not
support radius25 inputs. No accepted radius25 source is modified. Every
operation in the rational derivative algebra uses its declared positive
pole, so the same displayed derivation applies with2499 in place of624.
The moment theorem holds for arbitrary distinct positive rational poles.
It is not restricted to the numerical values in the previous fixtures.
Nevertheless the new version must pass radius50 Cartesian manufactured
fields, exact R=1 and radius10/100 coefficient comparisons, and a complete
accepted013 weak test before any017 candidate calculation is accepted.
The new scalar fixture usesa=2499, nonintegerb, and both small and large
localization powers, comparing direct and recurrent hypergeometric
moments. Its results are recorded separately. All candidate results
remain OPEN until independent reproduction.
