# Quantifiers in the assembled report and appendix audit

Status: the fixed report was captured at the real time in the team records. All appendix chunks have now been read. The corrections below are required; no full-report confirmation is issued.

## 1. Finite order is a global sufficient condition

Use the exact actual-profile class of A1151: 2/5<c<1/2, arbitrary real omega, U in C2 and P in C1 on R3, Jx=(-x2,x1,0), and

    div U=0, (1-c)U+DU(cx-omega Jx+U)+omega JU+grad P=0,
    U.curl U=0, |U(y)|<=C(1+|y|)^-p,
    |DU(y)|<=C(1+|y|)^(-p-1), p=(1-c)/c, C finite.

Let V,P2 be the actual tails, W=curl V, S=P2-|V|2/2, Z=int{k=0}, k=(cx-omega Jx).V, and E0 the angular support of 1_Z V. Define

    T0={w in S2: V(w)=DV(w)=P2(w)=S(w)=0} intersect supp W.

The confirmed theorem says:

    [For every x0 in T0, V is smooth near x0 and has finite order there]
        implies U=0.

Its local input says that any individual such finite-order point is interior to E0, is an isolated angular velocity zero, and has nonpositive index. It does not say that the individual point cannot exist.

Here is the complete global quantifier step. Under the premise at every T0 point, T0 is contained in int E0. Since boundary E0 is contained in T0, E0 has empty boundary. The sphere is connected, so E0 is empty or the whole sphere. The first case contradicts the necessary existence of T0 for a nonzero U. In the second case all velocity zeros relevant to the index count have nonpositive index, contrary to total index2. In either case U=0.

If the finite-order premise holds only at one point, boundary E0 can still contain other points, and in the full-sphere case other infinitely flat zeros can still carry the missing index. Neither global step follows. Therefore the report's assertion that Theorem7(e) excludes every individual finite-order T0 point is not a consequence of its proof. This is a refuted inference, not a constructed nonzero profile or a claim that finite-order points actually occur.

The corrected consequence is:

    If U!=0 and V is smooth near every point of T0,
    at least one point of T0 has infinite vanishing order.

At a boundary point of E0, or under the global nodal premise N which makes E0 empty, the stronger individual infinite-order conclusion does hold. Those extra premises cannot be silently omitted.

The source errors are in summary item10 and Theorem7(c)'s final finite-order sentence. Exact excerpts and line numbers are retained in the team records. Theorem7(e)'s actual quantified statement and its proof outline are correctly stated.

## 2. A further scope correction in summary item6

The sentence "Each nonexistence theorem in the target range adds a helicity sign ... or global zero helicity ..." is too broad. The report also gives the nonrotating theorem under uniform sublinearity, the axisymmetric corollary, and integrability consequences of the energy theorem. Their hypotheses do not contain a helicity sign. Replace "Each nonexistence theorem" by "The helicity-based nonexistence theorems5 and7". This corrects the taxonomy, without changing any theorem.

## 3. Dependencies and remaining review

The full independent proof of the local and global finite-order result is in the team records, Sections6-7. The necessary T0 theorem is A1050-A1057; its source and proof were already independently audited. No computation, external unique-continuation result or pressure gauge enters the logical correction here.

The appendix inspection will be recorded separately as its reading and consistency checks are completed. A full-report confirmation is not issued by this file.

## 4. The auxiliary divergence theorem needs trapping

AppendixA, source line4042, claims that every C1 field F satisfying [B,F]=-(1+c)F is divergence free under H0 alone. The confirmed A041 theorem additionally assumes U=o(|x|) uniformly and c>0. Its proof uses a bounded backward orbit to bound div F there.

The omitted assumption cannot simply be deleted. Fix any c>0, set omega=0 and

    M=diag(-1-2c,(1+2c)/2,(1+2c)/2),
    U(x)=Mx, P(x)=-x.(M+M2)x/2,
    B(x)=(cI+M)x,
    F(x)=x1^2 e1.

Then tr M=0 and all fields are smooth. Since (1-c)M+M(cI+M)=M+M2, U and P solve the exact profile equation. Thus H0 holds. The first eigenvalue of DB is -(1+c), and

    DF B-DB F=-(1+c)F, div F=2x1.

The claimed divergence conclusion fails. U has linear growth and does not satisfy uniform sublinearity, so this example contradicts only the table's larger class. It is not a decaying-profile counterexample.

For the corrected theorem, the bracket law gives

    F(Phi_t x)=exp(-(1+c)t)DPhi_t(x)F(x).

The spatially constant Jacobian det DPhi_t=exp(3ct) implies, by change of variables and integration by parts,

    div F(Phi_t x)=exp(-(1+c)t)div F(x).

Uniform sublinearity makes the flow complete and every backward orbit bounded. Continuity bounds div F along that orbit; sending t to minus infinity proves div F(x)=0. No second derivative of F is used. The original A041 proof is correct.

## 5. Gauge correction persists in two appendix rows

Rows4164 and4166 still say H=Q=g=0 on critical leaves. In the report's global notation H=P+|U|2/2+(Ax).U, whereas Q=P-Pinf-|U|2/2. Replacing P by P+C preserves the profile equation, U, Q, g and every leaf, but replaces H by H+C. Therefore H=0 without fixing Pinf=0 is not gauge invariant. The correct expression is

    H-Pinf=Q=g=0.

This is the same A1209 correction already made in the report front. Gradients and Hessians in these rows are unaffected by the additive constant.

## 6. The polynomial countermodel does not solve similarity with zero pressure

Row4188 describes the LIT203 polynomial swirls as fields "which solve the similarity equation with no pressure". That literal assertion is false. Let n>=1, r2=x1^2+x2^2 and

    v=r^(2n)Jx, pi=r^(4n+2)/(4n+2).

They solve stationary Euler with pi. Rotation equivariance gives Dv(Jx)=Jv and ordinary homogeneity gives Dv x=(2n+1)v. Hence the rotating similarity residual with pi is

    (1-c)v+Dv(cx-omega Jx+v)+omega Jv+grad pi
        =(1+2nc)v.

The curl of this residual is (1+2nc)(2n+2)r^(2n)e3, nonzero off the axis for c>0. No change of scalar pressure can cancel it on an open set meeting the off-axis region. Replace the phrase by "which solve stationary Euler but fail the similarity equation for every pressure". The full proof and all local jets are in the team records, Sections1-2.

## 7. Repeated scope omissions in the compact table

Row4153 abbreviates the cross-core boundedness premise to "local boundedness". It must mean that every point z of the compact core K_Omega has an ambient ball B(z,r) on which S composed Xi is bounded on E intersect B(z,r), with E the scattering domain. Boundedness merely near points of E is automatic and gives no extra theorem. This repeats A1211.

Row4276 leaves the second Lorentz index of vorticity as q<infinity. The certified formulation uses 1<=q<infinity. The same lower restriction should appear here unless a separate extension is proved. This records the verified scope; it does not claim that smaller positive Lorentz indices fail.

Rows4206-4207 need the leading scalar polynomial to be harmonic for the frozen principal form: A(0):D2H_l=0 for the gradient equation and adj K(0):D2H_l=0 for the first-order system, or explicit coordinates normalized so those matrices are I. An unqualified "harmonic" together with a general positive matrix does not state the source theorem.

The symbols H3 and H9 denote categories of assumptions in the report's notation, rather than individual mathematical predicates. Repeated rows containing only "H9; H3" therefore do not specify an exact class by themselves. Where the intended class is the HF/natural class, say so and refer to the exact inequalities of Theorem7; retain each additional local, nodal or density premise separately. This is an editorial scope repair, not a new nonexistence result.

## 8. The same gauge and polynomial errors recur in the working record

The long chronological record in AppendixB repeats the two errors from Sections5-6. In line4681, the assertions H=Q=g=0 on the regular and critical leaves, and statements that H itself vanishes to positive order, require H-Pinf in place of H. The analogous comparison H~L in line4685 requires H-Pinf~L. The pressure shift test in Section5 applies without any further hypothesis.

Line4687 again says that the LIT203 swirl solves rotating similarity without pressure. The exact residual in Section6 disproves that claim for every c>0 and every omega. The source A1101 says precisely the opposite. This is not merely an obsolete stronger theorem: it is a transcription error which reverses a confirmed obstruction.

Lines5048 and5342 need the ambient-core boundedness quantifier of Section7, and line5349 needs the certified Lorentz second-index range. Later corrections inside a chronological paragraph do not make the earlier literal statements safe to quote on their own. Label AppendixB as a chronological working record, and identify the front theorems and the latest audit verdict as the current statements. Historical OPEN and SUBMITTED labels should not be read as present verdicts where a later entry explicitly supersedes them.

## 9. Surface Stokes uses U dot curl Omega

For a C2 divergence-free Euler profile define Omega=curl U and Q=P-Pinf-|U|2/2. Taking divergence of the profile equation gives the pressure equation -Delta P=tr((DU)^2). The linear rotation contributions cancel because the divergence of DU(Jx) equals the divergence of JU. Since Delta U=-curl Omega,

    Delta Q = -tr((DU)^2)-|DU|2-U.Delta U
            = U.curl Omega-2|sym DU|2.

Thus on a leaf where Delta Q=0 the correct pointwise equality is

    U.curl Omega=2|sym DU|2.

On the regular vortical leaf in the cited theorem, U is a nonzero normal to the leaf. The surface normal component of curl Omega is therefore U.curl Omega/|U|. This is the quantity integrated by Stokes for the one-form Omega.dy. The expression curl U.curl Omega in line4681 is a typo: curl U=Omega is tangent to the leaf and does not give its normal flux. Replacing the factor by U restores the already confirmed A883 argument. This check does not add a boundary-circulation assumption or claim that the conditional Stokes theorem holds without its exhaustion hypotheses.

## 10. The vector rotation generator must include the basis term

For Jx=(-x2,x1,0), define the rotation action on vector fields by U_alpha(x)=exp(alpha J)U(exp(-alpha J)x). Its infinitesimal generator is -L, where

    LU=(Jx.grad)U-JU.

For scalars, by contrast, partial_theta f=(Jx.grad)f. In cylindrical components the vector generator has componentwise partial_theta components, because the moving basis contributes JU. These two conventions must not be interchanged.

For every exact C2 profile and axisymmetric compactly supported C1 weight phi, the equation is E0(U,P)=omega LU, where E0=(1-c)U+cDUx+DUU+grad P. Furthermore

    integral phi U.LU = integral phi partial_theta(|U|2/2)=0.

Multiplying the equation by phi LU therefore proves

    omega integral phi |LU|2
      = integral phi LU.[cDUx+DUU+grad P].

No decay or boundary limit is needed because phi has compact support. This confirms the source formula with the full geometric generator, for arbitrary real omega. The source in the team records defines it correctly. The assembled line4956 abbreviates it to LU=partial_theta U, omitting the source parenthetical convention.

The Cartesian componentwise reading of that abbreviation gives a false identity. Take M=diag(-1/2,-1/2,1), U=Mx and P=-x.(M+M2)x/2. For every c and omega these fields solve the profile equation: tr M=0, M commutes with J, the rotation terms cancel, and M+M2 is symmetric. Here the correct LU=0, whereas the Cartesian derivative (Jx.grad)U=MJx=JU is nonzero off the axis. The right-hand bracket in the displayed balance equals -(1-c)U, so its pairing with JU is identically zero. For omega!=0 and any nonnegative, nonzero smooth axisymmetric compactly supported phi, the proposed Cartesian left-hand side omega integral phi|JU|2 is nonzero. The example has linear growth and disproves only that interpretation of a local identity, not the decaying-profile conjecture.

Write the explicit formula LU=(Jx.grad)U-JU in the report. The equivariant density Q(U) in the source may depend on derivatives of U; this is not an additional error, since its linearization is explicitly the derivative of that local functional.

## 11. The past torque formula needs 0<c<1/2

For a C2 exact profile with uniformly sublinear U, set Gamma=(Jx).U, B=cx-omega Jx+U and a=1-2c. Direct scalar multiplication of the equation gives

    B.grad Gamma=-a Gamma-partial_theta P.

For c>0 uniform sublinearity implies complete characteristics and bounded backward orbits: at sufficiently large radius, x.B>=c|x|2/2, and B has at most linear growth. Thus Gamma and partial_theta P are bounded on the closure of each backward orbit. Integrating the scalar equation yields

    Gamma(x)-exp(-aT)Gamma(Phi_{-T}x)
       =-integral_{-T}^0 exp(as)partial_theta P(Phi_sx) ds.

When 0<c<1/2, a>0, the endpoint vanishes and the integral is absolutely convergent. This proves the A034 formula and the consequence that axisymmetric P forces U_theta=0. The latter is first proved off the axis; continuity gives its vector interpretation at the axis. Nothing in the proof assumes omega small.

The restriction is missing in assembled lines5031-5034, whose section header otherwise says every c>0. It is also missing in the compressed source suggestions. The original MODE_IDENTITIES convention and the full independent A034 proof have the correct range.

There are explicit counterexamples to extending this representation to the printed uniformly sublinear class at c>=1/2. Fix omega!=0, let u=e1, and set

    U(x)=u, P(x)=-(1-c)x1-omega x2.

These are exact smooth profiles for every c>0 and are uniformly sublinear. B has an equilibrium

    x*=-(c e1+omega e2)/(c2+omega2),
    Gamma(x*)=omega/(c2+omega2),
    partial_theta P(x*)=-(1-2c)Gamma(x*).

At c=1/2 the purported integral at x* is zero while Gamma(x*) is nonzero. At c>1/2 its integrand is a nonzero constant times exp((1-2c)s), so the past integral diverges. These constant velocities do not decay; they test the row's explicit H0 plus uniform-sublinearity scope. They neither settle nor refute a hypothetical decaying-profile extension outside the target interval.

## 12. Coverage and final scope of this snapshot audit

All twenty-one wrapped appendix chunks have been read in full. They cover the fixed snapshot's AppendicesA-D, source lines4029 through5891. The current front corrections in Sections1-2 were checked separately. The full bodies of Sections2A-2D were independently reconstructed in the team records. These completed checks do not certify every paper mentioned in the chronological record, nor every unreviewed historical source. They identify the precise errors and the repaired claims above.

The appendix needs the listed repairs before it can be treated as a reliable standalone collection of statements. The main bare-decay conjecture for every omega remains OPEN. No numerical computation, build, new model invocation or remote workload was used in this appendix audit. Its corrected identities and counterexamples were derived directly.
