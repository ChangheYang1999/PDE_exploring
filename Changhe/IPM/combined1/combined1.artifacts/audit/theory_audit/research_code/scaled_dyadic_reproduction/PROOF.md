# Independent polar reproduction of the candidate010 dyadic witnesses

## Exact statement and hypotheses

Fix c=4076476460239181/2251799813685248, gamma=1/c and delta=1-gamma. Let chi be the exact finite rational potential in ../multiscale_point_010/data/candidate010.json, with the raw hash recorded in every result. Its generators are

    Re(x+iy)^(2m) (1+r^2)^(p_j-m) t_R^w u_R^Q P_N(2t_R-1),
    p_j=(3+gamma-j delta)/2, t_R=r^2/(R^2+r^2), u_R=1-t_R,

with nonnegative integral indices and R in {1,10,100}. P_N is the Legendre polynomial. Put rho=-partial_y Delta chi, psi=partial_xy chi, U=(-partial_y psi,partial_x psi), and F=(cX+U).grad rho-rho. All fields are smooth. Their canonical velocity, origin normalization and tail class have been checked separately. In particular chi_xxyy(0)=1-c and a0=rho_y(0)>=5c-4.

For a>=0 and n=1 or3 let

    J_n(a)^2=int_R2 (1+r^2)^(2-a) |Delta Pi_n F|^2 dX,
    J(a)^2=J_1(a)^2+J_3(a)^2,

where Pi_n is the full-circle orthogonal sine projection with coefficient pi^(-1)int F sin(n theta)dtheta. If N_a(F)=||(1+r^2)^((2-a)/2)Delta F||2, orthogonality gives J(a)<=N_a(F), including when the latter is infinite.

The numerical claim to be independently checked is that all seven cells in [0,1+1/c] strictly violate

    5^((a-2)/2) N_a(F)<H(c-1)(1+c-ca)/(1+a),             (1)
    H(d)=max_(0<s<d)(d-s)sqrt(4pi s(1+s)).

This excludes only a scheme for which (1) is necessary. Its application to the registered dyadic inverse scheme also requires the complete low realization, input hyperplane f_y(0)=0, canonical velocity, finite fixed localization radius, high inverse and absorption hypotheses in ../origin_dyadic_inverse/PROOF.md and ../dyadic_weighted_closure/PROOF.md, including their accepted reviews. Under those hypotheses the origin theorem excludes a>=1+1/c because the required low rate is nonpositive; the seven cells below cover the remaining 0<a<1+1/c. Only with both parts may one state exclusion of that sufficient scheme over0<a<2,0<s<1. This is not a nonexistence claim for stationary profiles.

## Polar construction of the complete selected residual

Put t=r^2/(1+r^2), v=1-t. Each generator is (1+r^2)^p_j A(t)cos(2m theta), where A is rational with denominator a product of positive factors1+99v and1+9999v. Its numerator is obtained directly from

    A=sum_(k=0)^N (-1)^(N+k) binom(N,k)binom(N+k,k)
              R^(2Q) t^(m+w+k) v^Q /[1+(R^2-1)v]^(w+Q+k).

This is an exact polynomial identity for P_N after substituting t_R=t/[1+(R^2-1)v]. For R=1 the denominator is1. Differentiation therefore stays within this rational class and introduces no pole on the closed integration interval.

For a radial factor (1+r^2)^p A, Euler differentiation is E_p A=2t v A'+2pt A. Applying the polar Laplacian and -partial_y gives rho; applying partial_xy gives psi. Explicitly, with angular frequency m, B=E_p(E_p A)-m^2 A and D=E_p B-2B, the density numerators before the common division by t^2 are (D+mB)/2 at m-1 and -(D-mB)/2 at m+1. The stream numerators are (E_p-(m+2))(E_p-m)A/4 at m+2 and -(E_p+(m-2))(E_p+m)A/4 at m-2. Negative sine frequencies are folded with a minus sign. Exact origin zeros justify division by t^2. Thus

    rho=r sum v^((j+1)delta/2) R_jn(t)sin(n theta),
    psi=r^2 sum v^((j+1)delta/2) S_jn(t)sin(n theta).

For T_(z,d)A=(d-2zt)A+2tvA', the radial derivatives of these fields have factors T_(z,1)R and T_(z,2)S. Multiplying the complete fields and retaining every pair that can produce frequency n gives

    Pi_n F=r sum_ell v^(ell delta/2) P_ell(t) sin(n theta).

The linear coefficient is c T_(z,1)R-R. A stream mode m and density mode k contribute (kR T_(z,2)S-mS T_(z',1)R)/2 to m+k and (-kR T_(z,2)S-mS T_(z',1)R)/2 to k-m, with signed folding. All pairs, including those with large cancelling angular frequencies, are retained.

For each residual branch z=ell delta/2,

    Delta[r v^z P(t)sin(n theta)]=r v^(z+1)L(t)sin(n theta),
    tL=T_(z,1)(T_(z,1)P)-n^2 P.                       (2)

Indeed r partial_r applied twice produces the numerator on the right, and r^(-2)=v/t. The numerator vanishes at t=0 by smoothness; the code verifies that zero exactly before division.

## Endpoint factors and full-plane integration

Remove the exact order q of the numerator L(1-v) at v=0, writing L=v^q B(t), where B has only the same positive poles. Check ell delta+2q-2>0 for each nonzero branch. Angular orthogonality, r dr=dv/(2v^2) and r^2=(1-v)/v give

    J_n(a)^2=(pi/2) sum_(ell,k)
       int_0^1 v^(a+(ell+k)delta/2+q_ell+q_k-3)
                  (1-v) B_ell(1-v)B_k(1-v)dv.         (3)

Off-diagonal unordered pairs receive multiplicity2. The checked endpoint condition makes every exponent greater than-1 for a>=0, so all terms in this finite sum converge. Every angular pair has already been accounted for; no radial truncation or quadrature is introduced.

Each rational numerator is divided by the exact product denominator. The principal parts are reconstructed by the polynomial Chinese remainder identity, and that identity is replayed exactly. Its polynomial part integrates termwise by int v^b dv=1/(b+1). A remaining principal part uses

    int_0^1 v^b/(1+A v)^k dv
       = 2F1(k,b+1;b+2;-A)/(b+1), b>-1,A>0,k>=1.

This follows by the Euler integral representation; the independently accepted positive-pole moment proof is ../rational_pole_audit/PROOF.md. The own CRT/direct-hypergeometric implementation used here is already independently accepted for candidate010 weak tests. It is reused without modifying that accepted code. Arb encloses every non-rational operation. More than150 relative accuracy bits and positive final energies are required.

## Cell argument and verification

J(a) is decreasing, since its nonnegative integrand is pointwise decreasing in a. The scalar (1+c-ca)/(1+a) is also decreasing. Therefore for a in[l,h] and e>=h,

    5^((a-2)/2)N_a(F)>=5^((l-2)/2)J(e),
    H(c-1)(1+c-ca)/(1+a)<=H(c-1)(1+c-cl)/(1+l).

The difference of these last two quantities is a rigorous lower bound on the obstruction margin. Use endpoints0,1/4,...,3/2,1+1/c and e=1/4,...,7/4. The exact inequality3/2<1+1/c<7/4 ensures coverage. Differentiating the square of H's objective shows its interior maximizer is

    s*=[2d-3+sqrt((2d-3)^2+16d)]/8.

The endpoint values are0, and the other critical root is negative, so this is the maximum. Its containing interval is checked against0<s*<d.

The implementation independently reconstructs the raw polar fields, checks the six physical point values against the accepted Cartesian record, verifies exact origin identities, integrates all eight weights for both complete selected modes, and compares every resulting interval and all35 cell quantities with frozen N4 records. Every source, code and mode output is hash-bound. Results remain OPEN until the independent calculation completes. No formal proof assistant is used.
