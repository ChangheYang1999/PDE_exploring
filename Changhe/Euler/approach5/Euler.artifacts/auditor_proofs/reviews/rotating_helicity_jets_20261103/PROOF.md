# Exact obstruction for one rotating helicity-free quadratic jet

Auditor verdict: A429, CONFIRMED at the exact finite-order and linear-rank scopes below. Final focused review received and checked 2026-11-03T02:42:17Z.

## Statement and precise finite-order meaning

Fix c=9/20, omega=1, u=e1, w=e3 and

    M=[[-1/3,-2/5,0],[3/5,-2/3,0],[0,0,1]],
    J(x,y,z)=(-y,x,0), A=cI-omega J, kappa=1+c,
    p0=-A^(-1)u=(-180/481,-400/481,0), N=A+M.

Use coordinates X=(x,y,z)=y-p0. Let V0=u and V1=MX. Fix V2 to be the exact rational homogeneous quadratic stored in the degree2 velocity record of in the team records. Its three free coefficients in the row-reduction convention below are 1,2,3; this convention uniquely specifies the same polynomial and provides a definition independent of copying its large coefficients into prose.

The proposition is that this fixed first and second jet has real rational extensions through velocity degree6, but has no extension through velocity degree7 even over the complex numbers. No parity restriction is imposed on cubic or higher coefficients. The proof below explains why their parity follows for this particular first and second jet.

An extension through degree n is a list V0,...,Vn of homogeneous vector polynomials with divergence identically zero, whose vorticity and helicity residual coefficients through degree n-1 vanish. A polynomial pressure then makes momentum vanish through degree n. These statements concern truncated Taylor coefficients. They do not assert that the velocity polynomial solves Euler at every degree, has a convergent infinite extension, or decays at infinity.

All large coefficient data remain in exact JSON. Every imported algebraic assertion was regenerated or checked against the original equations; importing those data alone is not a proof. This is a computer-assisted exact algebraic result, not a Lean formalization or numerical residual test.

## 1. Derive the recurrence and recover pressure

Write Omega=sum_j W_j with W_j=curl V_(j+1). At the point p0, A p0+u=0, so

    B=NX+sum_(j>=2)V_j.

For an incompressible profile the exact vorticity equation is

    [B,Omega]+kappa Omega=0.

Collect homogeneous degree n-1 for n>=2 and impose zero helicity. The new unknown Vn solves

    div Vn=0,
    L_n Vn=-sum_(i,j>=2, i+j=n+1)
                 [(Vi.grad)W_(j-1)-(W_(j-1).grad)Vi],
    u.curl Vn=-sum_(i=1)^(n-1) Vi.W_(n-1-i),          (6)

where

    L_n V=(NX.grad)curl V+(kappa I-N)curl V-(w.grad)V.

Only lower jets occur on the right sides. In particular the constant w gives the last term in L_n, which must not be lost at the stagnation point. The first-jet identities are tr M=0, curl(MX)=w, u.w=0, and Mw=w+omega Jw=w. These are satisfied exactly.

For pressure, let Em be the homogeneous degree-m part of momentum without its pressure gradient. The vorticity equation is curl(momentum)=0, so the required coefficients give curl Em=0. Euler's homogeneous identity then yields

    grad(X.Em)=(m+1)Em.

Thus P_(m+1)=-X.Em/(m+1) gives Em+grad P_(m+1)=0. This proves the equivalence with momentum through degree n. No harmonic-pressure normalization or boundary flux is used: this is local polynomial exactness of a closed one-form.

## 2. Rank bounds and independent exact lower certificates

For each n let T_n V=(div V,L_n V,u.curl V). Full homogeneous polynomials give 3 binom(n+2,2) columns and 5 binom(n+1,2) rows. Direct differentiation gives the structural identity

    div(L_n V)+(w.grad)div V=0.                         (7)

It has binom(n,2) independent scalar coefficient relations. Independence follows because the divergence map from an arbitrary three-vector of degree n-1 to degree n-2 is onto, so the displayed relation functionals on the output coordinates are independent.

There is also a two-dimensional kernel: take V=grad q for a homogeneous harmonic polynomial q of degree n+1 in x,y alone. Then div V=curl V=partial_z V=0. Therefore

    rank T_n<=min(3 binom(n+2,2)-2,
                  5 binom(n+1,2)-binom(n,2)).          (8)

The independently written sparse-monomial checker builds T_n directly from (6), without importing the submitted solver or SymPy. It reduces entries modulo101, records a full-size pivot minor, and recomputes its determinant. The denominators in the rational operator are invertible modulo101. For every n=2,...,7 and omega=-1,1,3, the certified ranks equal (8):

| Degree | Rows | Columns | Rank | Kernel | Extra compatibility beyond (7) |
|---:|---:|---:|---:|---:|---:|
| 2 | 15 | 18 | 14 | 4 | 0 |
| 3 | 30 | 30 | 27 | 3 | 0 |
| 4 | 50 | 45 | 43 | 2 | 1 |
| 5 | 75 | 63 | 61 | 2 | 4 |
| 6 | 105 | 84 | 82 | 2 | 8 |
| 7 | 140 | 108 | 106 | 2 | 13 |

Every minor determinant is nonzero, so each modular lower bound is a rational lower bound. Together with (8), this proves the ranks. The certificate includes row and column indices, not only a numerical rank reported by a routine.

At fixed c,omega=1,u,w, the operator entries depend polynomially on parameters a,b in

    M(a,b)=[[a,b,0],[b+1,-1-a,0],[0,0,1]].

The finite product of the nonzero minor polynomials is nonzero at the displayed matrix. Hence these ranks hold on a nonempty Zariski-open subset of this two-parameter slice. For the fixed normalization u=e1,w=e3 this is the full admissible first-jet slice. It is not a change of coordinates reducing an arbitrary orientation relative to J to this normalization. No genericity across arbitrary u,w orientations or every parameter value is asserted. Only the linear rank checks were repeated at omega=-1 and3; the nonlinear obstruction remains at omega=1.

## 3. Why no higher parity-breaking extension is omitted

Let S=diag(1,1,-1). The reflection-fixed velocities have first two components even in z and third component odd in z. The first two jets have this property, and J commutes with S. Divergence is a scalar, curl transforms as an axial vector, and helicity as a pseudoscalar, so (6) respects the resulting output parities 0,1,1,0,1.

The reflection-restricted operator has the following ranks, again established independently by nonzero minors modulo101 plus the restricted form of (7) and the same two kernel vectors:

| Degree | Rows | Columns | Rank | Kernel |
|---:|---:|---:|---:|---:|
| 2 | 7 | 10 | 7 | 3 |
| 3 | 14 | 16 | 13 | 3 |
| 4 | 24 | 24 | 22 | 2 |
| 5 | 36 | 33 | 31 | 2 |
| 6 | 51 | 44 | 42 | 2 |
| 7 | 68 | 56 | 54 | 2 |

The independent restricted relations in (7) correspond to odd-z monomials of degree n-2. Their counts are 0,1,2,4,6,9, and the same surjectivity argument applies with these parities.

For n=3,...,7 the restricted kernel has the full kernel's dimension, so the full kernel lies in the reflection-fixed subspace. If the lower jets are reflection-fixed and Vn solves the full equation, its complementary parity part solves the homogeneous operator. That part must vanish. Induction proves that every possible higher continuation of this V2 through degree7 is reflection-fixed. The larger full degree2 kernel is irrelevant because V2 is fixed in the theorem.

## 4. Deterministic exact elimination

Order degree-n monomials x^i y^j z^(n-i-j) by increasing i, then j. Order velocity components 1,2,3 and retain their reflection parities. Order output components as divergence, three vorticity components, and helicity, with the same monomial order. This defines a rational matrix Cn.

The reduced row echelon form of [Cn|I] has right block En, an invertible row transformation. Applying it to the right side bn of (6) gives pivot formulas in its first rank(Cn) entries and every compatibility expression in the remaining entries. Nonpivot coefficients remain free. When a compatibility expression is not identically zero, the symbolic construction keeps it as an equation while provisionally continuing the pivot formulas. It never discards a nonzero compatibility equation.

At degree2 the free coefficients are set to1,2,3. This regenerates the V2 specified in the statement and verifies its equations. At degree3 the free coefficients are

    alpha=[x^2 y](V3)_2, beta=[x^3](V3)_2,
    t=[x^2 z](V3)_3.

The quartic step has no additional restriction on these three and gives free coefficients eta=[x^3 y](V4)_2 and theta=[x^4](V4)_2. The degree5 and6 steps produce respectively one and three nonzero compatibility expressions. Together they have the form

    K(t)(alpha,beta,eta,theta)^T=h(t),                  (9)

with K and h polynomial in t. The degree5 free coefficients are mu=[x^4 y](V5)_2 and nu=[x^5](V5)_2. The two degree6 free coefficients do not occur in the degree7 compatibility expressions. These assertions were checked by regenerating the entire symbolic in the team records from (6) with all compatibility equations retained.

## 5. Every exceptional denominator value is excluded

Exact determinant factorization gives det K=C D, where C is a nonzero rational constant and D=q1 q2 is the product of the two explicit quadratics recorded in the team records. Their coefficients and the determinant constant are exact data; they are not approximate fitted values. The script checks that D is squarefree, that the common denominator of K^(-1)h is proportional to D, and that the polynomial P=D times its eta component is, up to a nonzero rational factor, a Cramer replacement determinant.

The primitive integer versions of D and P have degrees4 and5. Exact polynomial gcd gives gcd(D,P)=1. This is independently certified modulo101: their degrees are retained, and their Sylvester resultant is22, which is nonzero. A nonzero integer resultant modulo a prime is nonzero over Q, hence they have no common complex root.

If D(t0)=0 and (9) had a solution, replacing the eta column of the singular K(t0) by a vector in its column span would still give determinant zero. That would force P(t0)=0, contradicting the coprimality. Thus all zeros of D are inconsistent. No denominator-zero branch is omitted.

At t=0, D(0)!=0. Equation(9) has a rational solution. Substituting it yields an extension through degree6 with arbitrary mu,nu and the two degree6 free coefficients. Setting these four to zero gives the concrete JSON branch checked directly in Section7.

## 6. The complementary parameter set is also impossible at degree7

On D!=0 substitute the unique solution K^(-1)h into all degree7 compatibility expressions. There are seven nonzero expressions, each affine in mu,nu. Clear denominators and divide each row by its polynomial content to form a row Ri(t) in the columns (mu,nu,1), i=0,...,6. The exact calculation checks that every removed polynomial factor has all its roots in D=0. Thus these row equations remain equivalent for D!=0.

Let Delta0 and Delta1 be the determinants of rows(0,1,2) and(0,1,3). Exact division gives

    Delta0=C0 q1^3 q2^4 f,
    Delta1=C1 q1^3 q2^4 g,                             (10)

where C0,C1 are nonzero rational constants and f,g are primitive degree9 integer polynomials. Exact gcd gives gcd(f,g)=1. The independent Python-integer Sylvester determinant over the field of101 elements is63, nonzero, with degrees preserved, and certifies this coprimality separately.

Any solution would give Ri(t).(mu,nu,1)=0 for all seven rows, hence both determinants in (10) would vanish. Since q1 q2!=0, this forces f(t)=g(t)=0, a contradiction over C. Together with Section5, this covers every complex t and proves the degree7 impossibility.

As a separate small check at t=0, the first three augmented integer rows reduce modulo103 to [[81,25,70],[36,5,102],[100,3,91]], whose determinant is36. The coefficient matrix has rank2 and the augmented matrix rank3. This check confirms the subbranch but does not replace the general exceptional-locus argument.

## 7. Direct verification, independent data and reproduction

The concrete degree6 velocity has identically zero divergence. An independent direct-momentum script constructs each homogeneous momentum coefficient Em directly from U and A, checks curl Em=0, constructs -X.Em/(m+1), and checks each momentum component. All degrees0 through6 vanish exactly. It separately checks every helicity coefficient through degree5 and the necessary first-helicity-derivative identity u.(D Omega w)=-1. It does not infer exactness from a small residual.

Nine regenerated result JSON files agree semantically with the pinned submission outputs: degree5, general system7, both branch systems, elimination, certificates, direct check, concrete degree6 and the modular resultant check. The three supplied substitution files were then derived independently from the regenerated degree5 and degree6 compatibility equations. Their exact symbolic equality to the supplied files and agreement with the general elimination at t=0 are recorded separately in the team records; independently derived copies are retained in derived_substitutions. The independently built36 full/restricted operator minors are additional evidence not taken from the submission. Every row and column index is retained in the team records.

The reproduction instructions specify the command order. The initial theoretical question and pass/fail criteria were written before computation in the team records. All symbolic work used rational arithmetic and univariate exact polynomials. CPU55, one process at a time and one library thread were used, with bounded individual commands. Hashes pin scripts, inputs and outputs.

## 8. Universal necessary identities and limits of counting

For any actual helicity-free profile at a vortical B-zero, let u=U(p), w=Omega(p), M=DU(p). The vorticity equation gives Mw=w+omega Jw. Differentiating U.Omega=0 in direction w yields

    0=(Mw).w+u.(D Omega w)
      =|w|^2+u.(D Omega w).

Thus u cannot vanish when w!=0. The fixed quadratic jet satisfies this requirement. It gives no contradiction.

For the velocity one-form alpha=U.dy and q=|U|^2/2, the complete momentum equation gives

    L_B alpha=-a alpha+d(q-P), a=1-2c.

Indeed A^T=cI+omega J, so the rotation terms cancel in (B.grad)U+(DB)^T U. If alpha wedge d alpha=0, applying L_B yields d(q-P) wedge d alpha=0, or Omega(q-P)=0. It does not imply d(q-P)=0. This necessary condition is not a sign argument.

The full operator dimensions count15 new parameters and26 compatibility functionals beyond (7) through degree7. They do not give26 algebraically independent equations on15 parameters. Evaluating the lower-jet right sides can make some functionals vanish, repeat or become dependent, as the present branch shows. Consequently neither parameter counting nor failure of a global optimizer proves a universal finite-jet obstruction. Other first or quadratic jets are unexcluded.

The theorem is fixed at omega=1 and one V2. It is not uniform nonlinear nonexistence for arbitrary omega, not a theorem excluding C2 local profiles, and not a global decaying-profile result. In fact [A428](auditor_proofs/proofs/helicity_equilibrium_rank/PROOF.md) already excludes this first jet from every GLOBAL C2 uniformly sublinear helicity-free profile: its required left-eigenvector condition fails because N^T e1=(7/60,3/5,0). That conclusion uses global recurrence and the rank theorem; it does not assert a local first-order obstruction. The degree7 algebraic theorem remains a separate local finite-order result. The exact degree6 extension rules out a contradiction from just these finite orders for every datum. The all-data local helicity-free stagnation problem remains OPEN.

## Review provenance

The source proof and every executed Python script were read in full. The equations, kernel upper bounds, parity argument, pressure reconstruction, exceptional loci and resultant logic were reconstructed independently, and the computations above were reproduced locally. This agent's author is a second model the external referee (a second model). The Theory Agent B  submission records that its delegated calculation did not consult model. The focused configured-model coordinator review is received and pinned in the team records. It independently checks the recurrence, pressure, structural ranks and parity, and redoes the elimination from our regenerated in the team records using a separate script. Its two degree29 denominator-cleared minors have gcd proportional to q1^6 q2^4, which has no root off D=0. This provides a second route that avoids row-content removal. We read the complete script, review and mathematical output, checked this implication against our exact resultant certificates, and incorporated the global-scope correction above. The recorded model configuration is the primary model; it is not independent provider attestation. No new model client was used.
