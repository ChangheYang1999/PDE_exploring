# Conditional source reconstruction on the ordinary slabs

This argument is written before a revised executable or source calculation. It extends the radial-domain part of the admitted capped-slab argument. It establishes no new computed inequality. The complete source identities and containing-arithmetic contract are imported from numerical_audit/research/background_slabs_independent/PROOF.md (campaign-relative) and its cited source admission.

## Statement and exact inputs

Fix c=4076476460239181/2251799813685248, Candidate007 with SHA256 ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21, and source013 with raw coefficient SHA256 a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a. The seven fields a,b,e,rh,sh,ud,uh have the complete 45-branch,621400-coefficient source with SHA256 2e3c649402c72ad50836f41f35c5657f50232a877557a5641038262355fa689d. Write t=r^2/(1+r^2), s=1-t, phi=2theta and d0=(1+3t)/4. The imported exact identities are

    d0 (M-(3/5)I) = [[a, sin(phi)e], [sin(phi)e, b]],
    |grad h|^2 = rh^2 + sin(phi)^2 sh^2,
    ||Sym Du||_op^2 = ud^2 + sin(phi)^2 uh^2/4.

Precisely, let X=(x,y), r=|X|, psi=partial_y chi_007+phi_013, h=-Delta phi_013, rho_background=-Delta psi and u=(-psi_xy,psi_xx). Here chi_007 and phi_013 are the exact rational functions fixed by the stated coefficient files. Write Sym D for the symmetric part of a Jacobian. The matrix is

    M=(c+1+(cX+u).X/(1/4+r^2))I-(21/10)Sym D(cX+u)
        + [[partial_y rho_background,-partial_x rho_background/2],
           [-partial_x rho_background/2,0]].

The symbol rho below is the radial expansion radius, distinct from rho_background. The seven field identities specify the numerical quantities used below; their source derivation is an imported proved dependency, not reconstructed from a truncated series.

Each field is a sum of source terms

    s^B (1+(A-1)s)^(-d) P(1-s, cos(phi)),

where B>=0 is rational, A>0 is rational, d>=0 is an integer, and P is the complete exact source polynomial. Let j be an integer with56<=j<=97. Suppose a complete successful source reconstruction and an independent actual review establish containing field intervals on every product cell in the closed slab j/128<=t<=(j+1)/128 and all angles. Then each conjunction of verified cell predicates gives its stated bound throughout that slab. In particular, the conjunction

    a>=0, b>=0, ab-sin(phi)^2 e^2>=0,
    rh^2+sin(phi)^2 sh^2<=(1/4)^2,
    ud^2+sin(phi)^2 uh^2/4<=(137/125)^2

gives M>=(3/5)I, |grad h|<=1/4 and ||Sym Du||_op<=137/125 there. Replace1/4 by71/500 for the stronger gradient predicate, or137/125 by3/2 for the larger strain predicate. Failed sufficient predicates are inconclusive. This statement is conditional on containing arithmetic, complete source coverage, full cell coverage and verified predicates.

## Radial geometry and convergence

Set sigma=(255-2j)/256 and rho=1/(255-2j). For56<=j<=97,

    61/256<=sigma<=143/256, 1/143<=rho<=1/61.

The map s=sigma(1+x), -rho<=x<=rho, has endpoints(127-j)/128 and(128-j)/128. Thus it parametrizes exactly the stated closed slab, whose squared-radius endpoints are j/(128-j) and(j+1)/(127-j).

For one branch define base=1+(A-1)sigma and g=(A-1)sigma/base. Every s in this interval lies strictly between0 and1, so1+(A-1)s=(1-s)+As>0. In particular,

    base(1-g rho)=1+(A-1)sigma(1-rho)>0,
    base(1+g rho)=1+(A-1)sigma(1+rho)>0.

Also base>0. It follows that1-|g|rho>0. Since rho<1, the two binomial series of(1+x)^B and(1+gx)^(-d) converge absolutely and uniformly on|x|<=rho. No assertion|g|<1 is needed. Indeed sigma may exceed1/2 for these ordinary slabs, so the capped proof's sufficient condition for that assertion is unavailable.

The transformed radial factor is sigma^B base^(-d)(1+x)^B(1+gx)^(-d). For B>=0, the absolute coefficient of x^k in(1+x)^B is at most the coefficient of x^k in(1-x)^(-B): this follows term by term from|B-i|<=B+i for each nonnegative integer i, including B=0. The denominator coefficients are majorized by those of(1-|g|x)^(-d). Hence

    E(x)=(1-x)^(-B)(1-|g|x)^(-d)

has nonnegative coefficients E_k and is finite at x=rho. This proves the uniform majorant used for every branch.

## Exact polynomial conversion and tail

Convert every angular power to Chebyshev modes by the binomial identity obtained from cos(phi)=(w+w^(-1))/2. Apply the exact affine radial substitution to the complete polynomial. Write its resulting coefficients U_il, so the polynomial equals sum_i,l U_il x^i cos(l phi). If containing arithmetic supplies nonnegative m_i>=sum_l|U_il|, all omitted total degrees above N are bounded uniformly by

    sigma^B base^(-d) [ (sum_i m_i rho^i) E(rho)
      - sum_(i=0..min(N,deg P)) m_i rho^i
          sum_(k=0..N-i) E_k rho^k ].

To prove this, expand the finite polynomial times the absolutely convergent radial series. For each degree i+k>N, take absolute values and use|cos(l phi)|<=1 and|x|<=rho. Summing the nonnegative majorant gives precisely the displayed difference. Its exact value is nonnegative. An interval implementation takes a containing upper endpoint, requiring it finite and nonnegative; it does not interpret a negative lower endpoint as a negative tail. The same containing m_i must appear in both terms. Sum every retained coefficient across all branches. If high polynomial rows are removed later, add their explicit absolute row sums times rho to the corresponding degree to the tail.

## Complete cell enclosure and scalar conclusion

Partition[-rho,rho] into32 equal closed radial cells and[0,pi] into256 equal closed angular cells. Their Cartesian products cover the whole transformed slab. For an angular coefficient G(phi)=sum_l Gamma_l cos(l phi), use the containing midpoint and first derivative, with|G''|<=sum_l l^2|Gamma_l|, to enclose its value on the entire angular cell. Insert those intervals in radial interval Horner evaluation and add the complete analytic and finite-row tails. Containing pi, trigonometric functions and all arithmetic operations are explicit dependencies.

The resulting intervals contain the seven exact fields everywhere in each closed product cell. Nonnegative a,b and determinant imply positivity of the displayed real symmetric2-by-2 matrix; d0>0 then gives M>=(3/5)I. The two squared identities give the norm bounds. Taking the conjunction over every distinct pair of radial and angular indices proves the regional bounds. Folding to[0,pi] loses no angle because the predicates use only cos(phi) and sin(phi)^2. Exact endpoint checks and product-cell enumeration include boundaries.

## Verification and scope

The revised executable must use exactly the42 roots97 down to56, retain the complete source, preserve the containing Taylor and cell method, and remove only the unnecessary|g|<1 assertion. Its code, source identities, proof and execution conditions require independent method review. A separate exact recount must check all cell intervals, flags, branch tails, source bindings and successful owner execution. No source run, actual result, host admission or new regional certificate exists merely because this argument has been written. A later union theorem remains necessary for a whole-plane background statement; near estimates, the inverse, O3 and existence are separate obligations.
