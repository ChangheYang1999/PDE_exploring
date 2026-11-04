# Source013 whole-plane weighted and unweighted residual norms

Written before this consumer code. All claims below are conditional on the named complete regional certificates; no numerical endpoint is asserted here.

## Exact statement and inputs

Fix c=4076476460239181/2251799813685248 and authoritative Candidate007 with SHA256 ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21. Use precisely the source013 raw correction a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a, canonical correction2531d462643034e1083b40f5e60a6c4b0fa3ba84425cea3cadb68c767847fc33 and complete fields3d5f08e06859af2577f6e099374a8ce5e139a0b66280055ada847745943bf8cb. Put psi=partial_y chi_007+phi, rho=-Delta psi, u=(-psi_xy,psi_xx), F=(cX+u).grad rho-rho and g=sqrt(1+4r^2)F. The Fourier transform is unitary. Define N_s(g)^2=integral (1+|xi|^2)^s |g_hat(xi)|^2 dxi.

Let D={r<=1/50}, A={1/50<=r<=10000} and E={r>=10000}. For j=0,1,2,3, suppose the source013 origin admission, the complete six-block annulus admission and the complete exterior derivative admission give rational containing intervals [l_Bj,u_Bj] for integral_B |D^j g|^2, where the derivative tensor is ordered. All endpoints must be nonnegative, include the complete analytic errors, bind the same exact source and be supported by successful independent reductions. In particular, a partial annulus, a receipt alone or an endpoint from source009 is insufficient.

Set L_j=sum_B l_Bj, U_j=sum_B u_Bj, and E_m^-=sum_{j=0}^m binom(m,j)L_j, E_m^+=sum_{j=0}^m binom(m,j)U_j. Then g belongs to H^3 and

    sqrt(E_m^-) <= N_m(g) <= sqrt(E_m^+)       (m=0,1,2,3).

If E_1^+>0, the fractional bounds are

    max(sqrt(E_2^-), ((E_2^-)^11/E_1^+)^(1/20))
       <= N_(21/10)(g) <= ((E_2^+)^9 E_3^+)^(1/20).

If E_1^+=0 all these norms are zero.

For each annulus panel let its center be c_p, half-width h_p, containing analytic radius d_p, and Taylor order K_p, with0<h_p<d_p<c_p. The entire weighted radial zeroth integrand, including angular integration and radial Jacobian, is analytic on |r-c_p|<=d_p and bounded there by H_p. Its Taylor coefficients in x=(r-c_p)/h_p belong to rational intervals [a_j,b_j]. Require

    m_p=1+4c_p^2-8c_p d_p-4d_p^2 > 0.

Divide the containing Taylor polynomial by 1+4(c_p+h_p x)^2 through order K_p. Let [P_p^-,P_p^+] contain its integral with dr=h_p dx over -1<=x<=1. Put

    e_p=2h_p (H_p/m_p) (h_p/d_p)^(K_p+1)/(1-h_p/d_p),
    J_p^-=max(0,P_p^- - e_p),   J_p^+=P_p^+ + e_p.

Then, for the exact adjacent union of all114 source013 panels,

    L_F=l_D0/(1+4/2500)+sum_p J_p^-,
    U_F=u_D0+sum_p J_p^++u_E0/(1+4*10000^2)

satisfy sqrt(L_F)<=||F||_2<=sqrt(U_F). The exterior zeroth interval may instead come directly from the admitted same-source exterior energy certificate, since the latter suffices for this inequality.

## Weighted assembly proof

Every source scale is positive, so g is smooth on compact sets. The three regions cover the plane except for two null circles. The containing regional derivative energies imply that every derivative through order3 is square integrable. Integration against compactly supported test functions identifies the classical derivatives with the weak derivatives, hence g belongs to H^3. No derivative of a sharp regional indicator is used.

Under the unitary Fourier transform the squared full ordered derivative tensor has multiplier |xi|^(2j). Parseval and the binomial theorem therefore identify N_m(g)^2 with the stated binomial energy sum. Exact rational interval addition proves the integer bounds.

Holder interpolation gives E_(21/10)<=E_2^(9/10)E_3^(1/10). Monotonicity gives E_(21/10)>=E_2. A second Holder interpolation, 2=(1/11)*1+(10/11)*(21/10), gives E_2<=E_1^(1/11)E_(21/10)^(10/11). Substituting containing endpoints and taking square roots gives the fractional inequalities. If E_1^+=0, the zeroth energy vanishes and g=0 almost everywhere.

## Unweighted quotient proof

For z with |z|<=d_p,

    |1+4(c_p+z)^2| >= 1+4c_p^2-8c_p d_p-4d_p^2=m_p>0.

The reciprocal is analytic on this disk. Dividing the complete weighted radial integrand by this polynomial gives exactly the unweighted radial integrand and a disk upper H_p/m_p. Cauchy's coefficient estimate and integration of the geometric tail on |r-c_p|<=h_p give e_p. Thus the stated panel intervals contain the full unweighted integral.

For clarity, the normalized reciprocal coefficients satisfy v_0=(1+4c_p^2)^(-1) and

    v_j=-(8c_p h_p v_(j-1)+4h_p^2 v_(j-2))/(1+4c_p^2),

where v_(-1)=0. The exact coefficient of an original Taylor coefficient a_j in the integrated truncated quotient is

    alpha_j=2h_p sum_{k=j,...,K_p; k even} v_(k-j)/(k+1).

Choose the lower or upper coefficient endpoint according to the sign of alpha_j. This proves rational dot-product containment without assuming signs of the original coefficients. An independent containing-ball method builds a reciprocal by truncated Newton iteration V <- V(2-DV), multiplies the interval coefficient polynomial and integrates its even terms. Starting from a containing constant reciprocal, each iteration contains the exact formal reciprocal to the doubled truncation order. Induction proves this assertion, so its integral also contains the same finite polynomial integral. The two methods give separate containing intervals; overlap alone is only a diagnostic.

On D the weight squared lies between1 and1+4/2500, giving the asserted disk bounds. On E it is at least1+4*10000^2, giving the tail upper and the lower0. Summing the panels and these outer estimates proves the global unweighted bound. Full annulus adjacency and coverage are hypotheses checked in the consumer; local block indices must be preserved when locating individual coefficient files.

## Arithmetic and evidence requirements

Exact rational addition and division determine all energies. Output dyadic intervals may be rounded outward. Every reported square-root endpoint is checked by squaring a nonnegative rational. Fractional endpoints are checked by the corresponding exact twentieth-power inequalities. Decimal displays round outward separately.

Both numerical stages must bind the source013 regional admission methods and reviews, all actual admission/result/panel files and their recorded code hashes. The complete annulus assembly must retain all six block identities and exact parent indices0through113, while each panel file keeps its original block-local index. The unweighted quotient must recheck the original weighted panel integral and full analytic remainder before using its coefficients. The consumer is not an alternative source of primary coefficient containment.

An independent reducer reconstructs the actual source bindings, uses the containing Newton quotient, recomputes energy sums in reverse order and checks every power inequality. All data are exact JSON or the existing compressed JSON certificate files. No coefficient table is hardcoded into generated theorem source.

## Dependencies, reading order and scope

Read ../source013_energy_admission/PROOF.md, ../source013_annulus_admission/PROOF.md and ../source013_derivative_deployment/PROOF.md first, together with the full analytic source proofs they cite. The rational quotient and independent Newton arguments reuse ../distributed_unweighted_ps1/PROOF.md and NEWTON_PROOF.md; no source009 numerical endpoint is transported. The whole-plane argument is the accepted regional assembly specialized to the frozen source013 identity.

Code and numerical evidence are in code/ and verification/. No Lean or Lake work is performed under the run restrictions. These bounds can supply the source inputs of G1 and L only after actual admission. They do not prove a background gap, the near coefficient derivative bounds, a far Fourier form, a full inverse, an invariant ball or a stationary solution.

The actual exterior zeroth admission must use ../source013_exterior_admission/PROOF.md and the repaired deployment manifest86dcf83162501b78b949c90b8b707a051cb8f95d7aa0ee15efa581eb38282c12. The exterior tensor application is ../source013_derivative_restart/PROOF.md. The original failed exterior deployment supplies no endpoint. Origin remains the original independently admitted successful calculation.
