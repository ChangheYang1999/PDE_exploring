# Complete-entry audit of the fifth axis relation at a simple endpoint

Status: standalone informal derivation written before the new checks. P306 and P311 already prove the two residue families. This packet audits their complete report entry, supplies the remaining polynomial and finite-limit arguments, and tests the further-indicial statement. Coefficient comparisons and report adoption are recorded separately; the general B2 problem remains OPEN.

## Exact setting and hypotheses
Fix beta=2, a real endpoint y_* and signed u=y_*-y. Let A,C be nonzero with A/C>0. Near u=0, b(y)=B(u) is analytic, B(0)=0 and B'(0)=1. Primes in this proof denote d/du; a subscript y denotes d/dy. The five scalar equations are

    B T'=(8+2B')T,
    B eta'=(5+B')eta-T,
    eta=-B''-2v,
    B D'=(16+4B')D+8v'T-12vT',
    B gamma'=(13+3B')gamma-D+2v'eta-6v eta'.       (1)

They express the x^2,x^4 temperature coefficients, x,x^3 vorticity coefficients and the first curl coefficient. Here T=Theta_xx(0,y), D=Theta_xxxx(0,y), eta=Omega_x(0,y), gamma=Omega_xxx(0,y), v is the x^2 coefficient of W2. The relation in y variables is

    b gamma_y+(13-3b_y)gamma=D+2v_y eta-6v eta_y. (2)

A is a constant specifying the signs of T and eta on the relevant side, not another equation imposed at this local endpoint. No global inverse, material-center normalization or attachment to an actual axis component is claimed for these examples.

## Coefficients and arbitrary-parameter residue families
Inserting W2=B+v x^2+..., W1=(4+B')x+v'x^3/3+..., Theta=T x^2/2+D x^4/24 and Omega=eta x+gamma x^3/6 in the defining Cartesian PDE gives (1) directly, with d_y=-d_u. Multiplication of the x^3 vorticity coefficient by6 gives precisely (2).

P306 proves for B=u+ku^2-(Ck/260)u^13, Ck!=0, that T=C u^10 times an analytic unit, eta=u^6(H+O(u)), v=-(B''+eta)/2 and an analytic D satisfy the first four equations. A normalized homogeneous factor for the fifth is Z=u^16(1+O(u)). Its variation-of-constants derivative has residue

    r=-9Ck(231H+k^7)/385.

An analytic gamma exists if and only if r=0; otherwise every one-sided solution includes r Z log|u| and fails to be C^16 at0. An arbitrary addition ell T^2 to D changes the derivative by -ell T^2/(BZ)=O(u^3), so cannot change r. With H/A>0 and A/C>0, the condition H=-k^7/231 requires Ak<0. The leading I2=D/T^2=-(120k/(11C))u^-11(1+O(u)) is then positive infinite from u>0, whereas A I2 has the sign of A. These are distinct signed statements.

P311 proves that adding c u^9 removes this sign restriction. For arbitrary real c,a the temperature residue and the fifth nonlogarithmic residue are

    rho=48k/5+2496a/C+(169088/165)c k^4/C,
    r=-(6/5)CHk-(9/385)Ck^8+1092aH
        +(517832/1155)cHk^4+162Cc.

Choosing c=k(231H+k^7)/6930 and a=-Ck/260-(2642/6435)c k^4 makes both vanish. The resulting analytic solutions have D=-(120Ck/11)u^9(1+O(u)) and gamma=O(u^5) when k!=0. A I2 has limit -sgn(k) infinity from u>0 and sgn(k) infinity from u<0. For H/A>0 either sign of k is permitted. The k=0 analytic construction exists but its distinct leading I2 formula must not be inferred from a zero multiple of u^-11.

For completeness, the scalar criterion used here follows by writing gamma=Z w. The meromorphic derivative w' has a convergent Laurent series with finitely many negative terms. Only its u^-1 coefficient produces a logarithm. Multiplication by Z makes all integrated negative powers analytic at0; the normalized nonzero residue produces u^16 times an analytic unit times log|u|. Its sixteenth derivative is unbounded. If rho!=0 in the temperature equation, D=T^2(I0+rho log|u|+const), where I0 is the zero-constant meromorphic primitive after subtracting rho/u. Only the nonlogarithmic part is used in the displayed r before compatibility. Once rho=0 it is the ordinary meromorphic residue. Its numerical value depends on normalizing Z, but its vanishing does not.

## Remaining polynomial and finite-limit examples
Let B=u, T=C u^10, eta=H u^6-(C/4)u^10, v=-eta/2 and

    D=E u^20-(36/5)CH u^15+5C^2 u^19.

The first four equations are checked by differentiation. Equation (2) reduces to

    -u gamma'+16gamma=D-2eta eta',              (3)

because 2v_y eta-6v eta_y=2eta eta_y=-2eta eta'. Thus the RHS in y notation is D+2eta eta_y, not D-2eta eta_y. Expanding the RHS of (3) gives

    -12H^2 u^11+(4/5)CH u^15+(15/4)C^2 u^19+E u^20.

The operator -u d/du+16 multiplies u^j by16-j. Therefore every real F gives the exact polynomial solution

    gamma=-(12/5)H^2 u^11+(4/5)CH u^15+F u^16
          -(5/4)C^2 u^19-(E/4)u^20.             (4)

This proves the polynomial part for all parameters, not just sampled triples. It also exposes the sign error in the draft proof outline while confirming its stated polynomial.

For the other part of (c), P296/P304 establish analytic B,T,eta with v=0 and D=ell T^2 for arbitrary real ell, T=C u^10(1+O(u)), eta=u^6(H+O(u)). The derivative -D/(BZ) is then O(u^3), hence analytic. Its primitive is analytic, so gamma=Z(const+primitive) is analytic of order at least16. The quotient I2 is exactly ell for u!=0. Choosing H/A>0 enforces both required local signs; ell stays arbitrary. These examples give every finite limit. The ninth-order family gives both infinities. Reflection transfers the one-end statements to the other orientation, without claiming a pair of compatible global endpoints.

## Higher scalar homogeneous exponents and scope
For the series Theta=sum a_n x^(2n), Omega=sum q_n x^(2n+1), W2=b+sum v_(2j) x^(2j), incompressibility fixes W1's coefficients. Direct coefficient extraction gives homogeneous parts

    b (a_n)_y+[(4n-1)beta+2-2n b_y]a_n,
    b (q_n)_y+[(4n+2)beta+1-(2n+1)b_y]q_n.

At beta2 and B'(0)=1 they become -u f'+10n f and -u f'+(10n+6)f at leading order. With fixed analytic lower-order coefficients, each scalar equation has one possible Laurent-residue obstruction to an analytic solution. This is a possibility, not a proof that the obstructions are nonzero, independent, or impossible to remove using remaining coefficient functions or homogeneous constants. It is not convergence of the infinite transverse series. An additional finite p=3,...,13 coefficient experiment may be reported as checked arithmetic, with exact source hashes; it is not needed for (a)-(c).

A smooth simple endpoint already has an extended-real I2 limit by4.53(a), since T has finite order and smooth D is flat or has finite order. Hence the new scope sentence must not say that existence of a limit is undecided. What is undecided is any additional restriction on the attainable limit or its sign from the remaining hierarchy or from actual profiles. Local satisfaction of five equations does not establish any B2 solution or decisive endpoint.

## Complete report comparison
Freeze actual report, SPEC, entry text, preview, application source, registry references and the existing proof packets. Compare the full preview with exactly the six declared textual changes, one added result row and one added timeline entry; preserve every prior table row and timeline item. Check all theorem hypotheses, the signed conversions above, normalized residues, local scope and the report's changed summaries. Do not execute/import lead code. Retain initial failed controls and dated corrections. All proofs use ordinary analysis; no Lean/Lake build is authorized or claimed.
