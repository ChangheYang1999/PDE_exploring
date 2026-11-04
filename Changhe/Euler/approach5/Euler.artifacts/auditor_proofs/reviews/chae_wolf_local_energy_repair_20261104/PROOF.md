# Local energy repair for the Chae-Wolf concentration argument

Status: independent mathematical reconstruction, reconciled with the existing Theory Agent A  comparison. The exact classical criterion below is distinct from the general weak-solution concentration theorem.

## 1. Statement, notation and dependencies

Fix R>0. Write I_r=(-r^(5/2),0), Q_r=B_r times I_r in three dimensions. Let (v,p) solve v_t+(v.grad)v=-grad p and div v=0 on Q_R. Assume v is C1 in time and C2 in space, p is C0 in time and C1 in space, with these regularities up to the spatial boundary on every compact time interval before zero. Suppose

    E_* = ess sup_(t in I_R) integral_B_R |v(t)|^2 < infinity,
    v in L3(Q_R),
    A_* = sup_(0<r<=R) A(r) < infinity,
    liminf_(r->0) A(r)=0,
    A(r)=r^(-1) integral_Q_r |v|^3.

Then every weak terminal energy measure of v has no atom at zero. A terminal measure means any weak limit on compact subsets of B_R of |v(t_j)|^2 dx with t_j increasing to zero. The uniform L2 bound supplies such subsequential measures. The conclusion is local and imposes no self-similarity or rotation assumption.

The analytic dependencies are the bounded-ball Stokes pressure projection and the usual Calderon-Zygmund estimate. For the ball let E_R^*f=grad pi, where -Delta w+grad pi=f, div w=0, w=0 on the boundary, and pi has mean zero. It is bounded on Lq for 1<q<infinity, fixes gradients, and for f=div F the mean-zero pi satisfies ||pi||_q<=C_q||F||_q with the scale-invariant normalization. Harmonic interior estimates are used only on compact subballs. These standard statements are also specified in the primary manuscript's Section2 and AppendixA; no weak-solution compactness theorem is assumed in this reconstruction.

The exact source being audited is LIT395, SHA256 3e5cbb0be255dd843c53e523b15fdcecf28185816c9efbf8b8fe0b35445e25a5. Its seven sections and fifty obligations were read. The primary is Chae-Wolf, arXiv:1706.02020v2, SHA256 6fb036499add1639bc4e03d31246d7a206529fae320cfa2eab829c9a1f5b14f0. Sections2,3,4 and AppendixA.4 have been reread as extracted text for this audit; printed pages7,12,29,31 were also visually checked. This is a source-formula audit and a replacement classical proof, not certification of every primary statement.

## 2. The correct projected balance

Put h=grad p_h=-E_R^*v, v_tilde=v+h, and grad p_0=-E_R^*((v.grad)v), choosing p_0 with mean zero. Since div v=0, h is a harmonic gradient and div v_tilde=0. Applying the projection to Euler gives

    partial_t v_tilde+(v.grad)v=-grad p_0.

Use symmetry of Dh and write v_tilde=v+h. Multiplication by 2v_tilde gives the exact identity

    partial_t |v_tilde|^2
      +div[(|v_tilde|^2-|h|^2)v+2p_0 v_tilde]
      =2(v tensor v):Dh.                                      (1)

In particular, if F=(|v_tilde|^2-|h|^2)v+2p_0 v_tilde and phi is fixed in space with compact support, then for t<s<0,

    integral |v_tilde(t)|^2 phi
      =integral |v_tilde(s)|^2 phi
        -integral_t^s integral F.grad phi
        -2 integral_t^s integral (v tensor v):Dh phi.           (2)

The minus signs follow by solving the integrated time derivative for its earlier value. They are not sign conventions for pressure. The ordinary velocity balance likewise has minus its forward flux when solved backwards. The primary's literal (2.11) has plus signs, omits -|h|^2v from the flux, and has coefficient1 instead of2 in the bulk term. Its ordinary (2.12) also has the wrong backwards sign. On page12 the square expansion must be either

    |v|^2=|v_tilde|^2-2v.h-|h|^2

or |v_tilde|^2-2v_tilde.h+|h|^2. Mixing their cross term and last sign is false.

## 3. Exact tests of the literal primary formulas

First let v=b be a nonzero constant. Since E_R^*b=b, h=-b. The ratio of its L3 norm on B_R to that on B_r is R/r. Thus the radius-independent comparison printed in (4.9), with the harmonic norm on B_R bounded by the original norm on B_r, fails. A correct interior harmonic estimate uses the original velocity on the fixed outer ball.

Second let Jx=(-x_2,x_1,0), v=Jx, and p=(x_1^2+x_2^2)/2. This is steady Euler. Its Stokes projection vanishes: w=(R^2-|x|^2)Jx/10 has zero boundary values, div w=0, and -Delta w=Jx, so pi=0. Hence h=0. Here A(r)=C r^(15/2) tends to zero and the terminal energy is the nonzero, smooth density |Jx|^2. For a fixed nonnegative outer cutoff zeta, its energy is positive; for shrinking inner cutoffs eta_r it tends to zero. The last page31 chain asserting that the fixed-ball projected energy is at most the shrinking terminal mass is false. The preceding inequality instead proves only that the atom is zero, as in Section6 below.

A test that directly refutes literal (2.11) uses D=diag(1,1,-2), s(t)=exp(-2t),

    v=Dx+s(t)Jx,
    p=-[(1-s(t)^2)(x_1^2+x_2^2)+4x_3^2]/2.

D and J commute and s'+2s=0. Therefore v_t+(v.grad)v=-grad p exactly. The Stokes projection of Dx is Dx and that of Jx is zero, so h=-Dx and v_tilde=sJx. Since Dx is time independent, p_0=p up to an irrelevant time gauge. For a nonnegative radial compact cutoff phi, let K=integral x_1^2 phi=integral x_2^2 phi=integral x_3^2 phi>0. Direct integration gives

    integral |v_tilde|^2 phi=2Ks^2,  its derivative=-8Ks^2,
    integral (|v_tilde|^2v+2p_0v_tilde).grad phi=-4Ks^2,
    integral (v tensor v):Dh phi=K(6-2s^2),
    -integral |h|^2v.grad phi=-12K.

The correct forward right side in (1), after testing, is -4Ks^2-12K+2K(6-2s^2)=-8Ks^2. In contrast the sum of the two printed (2.11) integrands is 6K(1-s^2)<0 at negative times, although the earlier projected energy is strictly greater than the later energy. Thus its literal inequality fails on a classical Euler solution. All these test fields fail the campaign's spatial decay condition and have smooth terminal energy; none is a counterexample to Euler nonexistence or to the no-atom conclusion.

## 4. A local pressure estimate with the required scaling

The following elementary estimate supplies the pressure step without the primary's erroneous radius comparison. Let n>=2, gamma>0, 1<p<infinity and 0<lambda<n. Set Q_r=B_r times (-r^gamma,0). If -Delta u=partial_i partial_j f_ij, with u,f in Lp(Q_R), and

    M_f=sup_(0<r<=R) r^(-lambda) integral_Q_r |f|^p<infinity,

then

    sup_(0<r<=R) r^(-lambda) integral_Q_r |u|^p
       <=C(n,p,lambda)[R^(-lambda)||u||_Lp(Q_R)^p+M_f]. (3)

To prove it for r<R/8, extend f by zero spatially and put T f=(-Delta)^(-1)partial_i partial_j f_ij. Split T f into B_(2r) and successive annuli of radius a=2r,4r,...,R, for each time in I_r. Calderon-Zygmund controls the near contribution by C M_f^(1/p)r^(lambda/p). The size bound C a^(-n) for the far kernel and spatial Holder followed by Minkowski give each annulus the Lp(B_r times I_r) bound

    C r^(n/p) a^(-n/p) ||f||_Lp(B_(2a) times I_r)
      <= C M_f^(1/p)r^(n/p)a^((lambda-n)/p).

The final annulus uses Q_R. Since lambda<n, the geometric sum is at most C M_f^(1/p)r^(lambda/p). The difference u-Tf is harmonic on B_R at each time. Its interior bound, integrated in time, is C(r/R)^(n/p)(||u||_Lp(Q_R)+||f||_Lp(Q_R)). Raise to p and divide by r^lambda; the remaining factor (r/R)^(n-lambda) is at most1. For radii comparable to R use the full norm directly. Only inclusions I_r subset I_a are needed, so no constant depends on gamma.

For our pressure, take n=3, gamma=5/2, p=3/2, lambda=1 and f=v tensor v. The Stokes bound supplies p_0 in L^(3/2)(Q_R), and (3) gives

    B_*=sup_(0<r<=R)r^(-1) integral_Q_r |p_0|^(3/2)<infinity. (4)

The pressure-flux Holder factor is B_*^(2/3)A(r)^(1/3). Keeping this exponent is necessary; a constant may subsequently depend on B_*.

## 5. Existence of the projected terminal trace and error estimates

The L2 projection bound and harmonic interior estimates give, on every compact subball,

    sup_t (||h||_infinity+||Dh||_infinity)<=C_R E_*^(1/2).

For a fixed compact test phi, F.grad phi and (v tensor v):Dh phi are integrable in space-time up to zero. Indeed v,h,v_tilde are locally L3, p_0 is L^(3/2), and the bulk uses the uniform L2 bound. Equation(2) therefore supplies a unique terminal projected energy trace sigma_tilde, a positive Radon measure locally in B_R. This assertion is proved here for the classical class rather than imported from literal (2.11).

Choose zeta supported in B_(3R/4), equal to1 on B_(R/2), and eta_r supported in B_r, equal to1 on B_(r/2), both between0 and1, with |grad eta_r|<=C/r. Use phi=zeta(1-eta_r). Define H(r)=r^(-1) integral_Q_r |h|^3. Then H(r)<=C_R E_*^(3/2)r^(9/2). On the inner cutoff support,

    integral_I_r integral |F||grad eta_r|
      <= C[A+A^(2/3)H^(1/3)
             +B_*^(2/3)(A^(1/3)+H^(1/3))].             (5)

This uses |v_tilde|^2-|h|^2=|v|^2+2v.h. Outer-cutoff fluxes tend to zero by absolute integrability on shrinking time intervals. The entire bulk term tends to zero by the uniform harmonic bound, finite E_*, and |I_r|->0. Hence all errors vanish along radii r_j tending to zero with A(r_j)->0.

## 6. Removing the atom, not the fixed-ball energy

The volume of Q_r is C r^(11/2). Holder gives

    r^(-5/2) integral_Q_r |v|^2 <= C A(r)^(2/3).

Choose t_j in I_(r_j) so that integral_B_(r_j)|v(t_j)|^2 is at most twice this average. This uses a set of positive measure, not assumed attainment of the exact average. The harmonic energy on B_(r_j) is O(r_j^3), so the projected energy there tends to zero too.

Apply (2) with phi=zeta(1-eta_(r_j)), let the later time tend to zero, and use (5) and the small inner energy. It follows that

    integral |v_tilde(t_j)|^2 zeta
       <=integral zeta(1-eta_(r_j)) d sigma_tilde+o(1).

The left side tends to S=integral zeta d sigma_tilde. Since eta_(r_j) tends pointwise to the indicator of {0}, dominated convergence gives S<=S-sigma_tilde({0}). Positivity forces sigma_tilde({0})=0. No step asserts S=0.

Finally, uniformly in time,

    integral_B_r ||v_tilde|^2-|v|^2|
       <=C_R E_* (r^(3/2)+r^3).

Test shrinking cutoffs along any subsequence defining a terminal energy measure sigma of v, first take the time limit and then let r tend to zero. The displayed estimate shows sigma({0})=sigma_tilde({0})=0. This proves Section1.

## 7. Relation to the previously confirmed critical-profile result

A103 concerns c=2/5, bounded C1 profiles with distributional blow-down zero and bounded DU, for every finite omega. A031 supplies canonical pressure and A054 supplies finite energy. Their associated physical solution has constant L2 energy, ||Du(t)||_infinity<=C/(-t), and terminal measure ||U||_2^2 delta_0 by dominated convergence, even though the rotation need not converge. Its exclusion uses the primary's separate whole-space pure-point Theorem3.1, not its Section4 passage from an arbitrary atom to a limiting solution. The present classical local criterion does not replace that pure-point theorem automatically: its small-liminf premise has not been derived for these profiles.

The Section3 chain was reread here to check the dependency distinction. Finite energy and the Type I bound imply ||u(t)||_infinity<=C(-t)^(-3/5), hence u in L3 in space-time and canonical p in L^(3/2). The trace and local balances can therefore be obtained from the correct ordinary Euler identity, without invoking the literal Section2 inequality. The backwards sign in the displayed Lemma3.4 balance is also immaterial to its estimate after both fluxes are bounded in absolute value. Section3.2's weighted estimates bound absolute fluxes. Section3.3 instead derives the transformed equation directly, with p_1=p_0+|h|^2/2, and bounds both projected pressure pieces in norm; reversing a displayed pressure-decomposition sign does not change those bounds. Its outer-solenoidal decay estimate feeds the exterior Helmholtz argument of Section3.4. The page25 gradient-pressure error was already corrected in A109: the corrected term remains a gradient and pairs to zero with the zero-normal exterior solenoidal field. The resulting backward inequality and arbitrarily fast decay give vanishing exterior vorticity; preservation of the nonzero-vorticity set's volume on compact time intervals gives the contradiction.

For completeness, the projected equation used there yields

    partial_t |v_tilde|^2+div[|v_tilde|^2 v+2p_1 v_tilde]
        =2(v_tilde tensor v_tilde):Dh,
    p_1=p_0+|h|^2/2.

Its left side exceeds that of (1) by div[|h|^2(v_tilde+v)]. Its right side exceeds that of (1) by 2[(v+h) tensor (v+h)-v tensor v]:Dh=(2v+h).grad|h|^2=div[|h|^2(2v+h)]. These are identical because v_tilde=v+h and both v and h are solenoidal. The old comparison expression div[|h|^2(v_tilde-2v-h)]=0 is false in general; it has been corrected rather than used.

Thus the particular Section2/4 errors refuted here do not invalidate the independently audited A103 application. This is a compatibility check with A103/A109 and the stated repairs, not a new blanket certification of the manuscript, its weaker printed function spaces, or its full general-atom blow-up construction. The finite-energy and Type I premises remain essential.

## 8. Scope and completed comparison

The literal identities and terminal fixed-ball-energy chain in Section3 are refuted by exact smooth examples. The classical local criterion in Section1 is proved by Sections2,4-6. No result here derives its quantitative A assumptions, finite gradient budget, or derivative decay from the rotating profile PDE. No nondecaying test is admitted as a profile counterexample. The arbitrary-omega conjecture in the open interval remains unresolved. The general weak blow-up passage in the primary remains outside this certification.

The existing configured model A comparison is retained as in the team records, SHA25612d3a443b80a1bd7af55e90b2543ca29d85a4184c2a12ece24db0f0253de8820. All189 lines, ten items and six optional remarks are read and checked. The corrected flux cancellation is proved in Section7. Its remarks about the harmless backward sign in Lemma3.4 and generic coefficients in (3.22) agree with the independent primary-source recheck. Its numerical or symbolic diagnostic output is not adopted as proof. Actual provider execution is independently unattested; no additional agent or remote model client is used.
