# Two-contact exclusion of a nonflat W2 direction at C2 regularity

Status: CONFIRMED A2457-A2460 at the exact scopes below; A2461 refutes the claimed necessity of a nonlocal input, and A2462 retains the remaining open cases. The existing coordinator comparison has been read in full. This proof concerns a local tail configuration. It does not prove the unrestricted profile conjecture or infinite flatness of a tail direction.

## 1. Exact local statement

Fix constants 0<a<1 and sigma>0, a point w, and orthonormal vectors e,f,n=e cross f in R3. Write E=span(e,f), h=s e+u f, r=|h|, and suppose a symmetric linear map M satisfies M n=0, M e=tau f and M f=tau e, where tau is either sigma or -sigma. Let O be a neighbourhood of w, let V:O->R3 and k,S:O->R be C2, and put W=curl V and K=supp_O W. Thus W is C1 and K is relatively closed in O. Assume:

1. V(w)=0, DV(w)=M, k(w)=0, grad k(w)=0, D2k(w)=-aM, grad S(w)=0 and D2S(w)=-4 sigma^2 f tensor f.
2. grad k cross grad S=0 on K.
3. At each z in K with W(z)=DW(z)=0 and V(z)!=0, the contact identity holds:
   grad S(z)=2|DV(z)|_F^2 k(z) V(z)/|V(z)|^2.
4. Points of {W!=0} on the transverse plane w+E accumulate at w.

These four assumptions are inconsistent. No Holder continuity of the second derivatives is assumed. No pressure equation or characteristic completeness is needed once these four premises have been supplied.

The actual-profile application uses 2/5<c<1/2 and a=1-2c, so 0<a<1/5. Every omega is allowed. It additionally needs all the HF, natural-decay, C1-tail convergence and escaping lower-window W2 premises described in Section6; the abstract local assertion must not be read as supplying those premises from bare decay.

## 2. Confinement of the support on the transverse plane

The C2 Taylor expansions, uniform as h tends to zero in E, are

    grad k(w+h)=-aMh+o(r),
    grad S(w+h)=-4 sigma^2 u f+o(r).

Since Mh=tau(u e+s f), their cross product is

    grad k cross grad S=4a sigma^2 tau u^2 n+o(r^2).

It is zero at each point of K. Because a,sigma and |tau| are positive, u^2=o(r^2) uniformly on K intersect (w+E). A sufficiently small punctured transverse disc therefore satisfies |u|<|s| at every point of K. In particular s!=0 there.

Also C2 regularity gives V(w+h)=Mh+O(r^2), uniformly in every transverse direction. Since |Mh|=sigma r on E, we can shrink the disc so that |V(w+h)|>=sigma r/2 on the entire punctured disc, not only on K. This distinction will allow differentiation on the whole interval between two contacts.

## 3. A uniformly decreasing contact defect

On the punctured transverse disc define

    G=|DV|_F^2, R=|V|^2, v_f=V.f,
    Q=2G k v_f/R, Phi=grad S.f-Q.

For each fixed s!=0, Phi is C1 as a function of u. In particular G is C1 because V is C2; no third derivative of V occurs. The following expansions are uniform on the whole punctured disc:

    G=2 sigma^2+O(r),       G_u=O(1),
    R=sigma^2 r^2+O(r^3),  R_u=2 sigma^2 u+O(r^2),
    v_f=tau s+O(r^2),      (v_f)_u=O(r),
    k=-a tau s u+o(r^2),   k_u=-a tau s+o(r),
    (grad S.f)_u=-4 sigma^2+o(1).

The estimate for (v_f)_u uses (Mf).f=(tau e).f=0. The bounded derivative G_u follows from the boundedness of DV and D2V on a smaller closed ball in O. The k expansion is a C2 Taylor expansion with zero constant and linear terms. In particular k=O(r^2), while only its remainder after the displayed quadratic term is o(r^2).

Use the quotient rule itself, rather than differentiating an unspecified small remainder:

    Q_u = 2 G_u k v_f/R + 2G k_u v_f/R
          + 2G k (v_f)_u/R - 2G k v_f R_u/R^2.

The first and third terms are O(r). The second is

    -4a sigma^2 s^2/r^2+o(1),

and the fourth is

    8a sigma^2 s^2 u^2/r^4+o(1).

For the errors in the last term, k's o(r^2) error is multiplied by O(r)O(r)/R^2=O(r^-2); the O(r^2) errors of v_f and R_u each leave an extra O(r). Since R/(sigma^2r^2)=1+O(r), the denominator replacements have uniformly vanishing error. The second term's errors are controlled in the same way by k_u's o(r) remainder and v_f's O(r^2) remainder. Consequently

    Phi_u=-4 sigma^2
           +4a sigma^2 s^2(s^2-u^2)/(s^2+u^2)^2+o(1).

For every (s,u)!=(0,0),

    1-s^2(s^2-u^2)/(s^2+u^2)^2
      =u^2(3s^2+u^2)/(s^2+u^2)^2 >= 0.

Thus, since a>0, Phi_u<=-4 sigma^2(1-a)+o(1). Because a<1, there is a smaller disc on whose entire puncture

    Phi_u<=-2 sigma^2(1-a)<0.

The radius depends on the local C2 moduli and bounds, a and sigma, and must lie within O. No uniform radius over a class of fields is asserted.

## 4. Two extreme contacts and the contradiction

Assumption4 supplies a vortical point y0=w+s e+u0 f with |s| as small as needed. Section2 gives s!=0 and |u0|<|s|. Choose it so small that the compact segment

    I_s={w+s e+u f: -2|s|<=u<=2|s|}

lies inside the transverse disc on which Sections2 and3 hold. Its points have r<=sqrt(5)|s| and never equal w. Let

    A_s={u in [-2|s|,2|s|]: w+s e+u f belongs to K}.

It is compact, since I_s lies in O and K is relatively closed. It contains an open interval about u0 because W(y0)!=0. Therefore its minimum u_- and maximum u_+ satisfy u_-<u_+. Section2 implies -|s|<u_-<=u_+<|s|.

For u>u_+ up to 2|s|, and for u<u_- down to -2|s|, the corresponding point of I_s is outside K. Each such point has a full ambient neighbourhood on which W=0. Thus W=DW=0 at those points. By continuity of W and DW, the same holds at z_-=w+s e+u_- f and z_+=w+s e+u_+ f. Both endpoints belong to K=closure_O{W!=0}; by Section2 they have V!=0. Assumption3 therefore gives

    Phi(s,u_-)=Phi(s,u_+)=0.

The entire joining interval stays in the punctured disc of Section3, even if it crosses many vortical or irrotational components. The fundamental theorem of calculus yields

    0=Phi(s,u_+)-Phi(s,u_-)
      <=-2 sigma^2(1-a)(u_+-u_-)<0,

which is impossible. Notice that neither endpoint needs to be in the closure of the same vortical component as y0, or of one fixed component at all. The contact identity must be valid for arbitrary supported endpoints, as it is in the application below.

## 5. Derivation of the contact identity from the tail equations

Here is the necessary input behind Assumption3, reproduced to check that it does not assume the conclusion. In the tail application, set

    X(x)=(cI-omega J)x, L=(1-c)I+omega J,
    a=1-2c, b=2-2c=1+a, q=b/a,
    k=X.V, S=P2-|V|^2/2, W=curl V.

The local equations are div V=0, DV X=-LV, -Delta P2=tr((DV)^2), X.k=-ak, X.S=-bS and grad k cross grad S=0 on {W!=0}. Suppose V,P2 are C2. Since 0<c<1/2, q>2 and (q-1)a=1, q(q-1)a^2=b. The elementary identities are

    grad k=-aV+X cross W,
    Delta k=-2 omega W_3-X.curl W,
    Delta S=-tr((DV)^2)-|DV|_F^2+V.curl W.

At a supported point z with W=DW=0 and v=V(z)!=0, put N=DV(z) and G=|N|_F^2. Then N is symmetric and trace free, grad k(z)=-av, D2k(z)=-aN, Delta k(z)=0 and Delta S(z)=-2G. Also G>0 because NX=-Lv and L is invertible.

Contracting the rank identity with X gives bS grad k=ak grad S. On each connected component of {W!=0,k!=0}, this is grad(S/|k|^q)=0, hence S=D_C|k|^q for a constant D_C on that component. At z, grad k=-av!=0. The set k=0 is therefore locally a C1 surface, and each open vortical neighbourhood contains points with k!=0. Select such x_j tending to z, allowing their components and constants D_j to vary.

At x_j write alpha_j=qD_j|k(x_j)|^(q-2). Differentiating the component law twice gives

    D2S=alpha_j[(q-1)grad k tensor grad k+kD2k],
    Delta S=alpha_j[(q-1)|grad k|^2+k Delta k].

The bracket in the last equation tends to (q-1)a^2|v|^2>0. The left side tends to -2G. Thus alpha_j tends to -2G/((q-1)a^2|v|^2), regardless of the components. Passing to the first-derivative identity grad S=alpha_j k grad k gives

    grad S(z)=2G k(z)v/|v|^2,

using (q-1)a=1. This is Assumption3, including the case k(z)=0 and unbounded component constants. The argument uses only C2, no quantitative component bound, and no derivative of the pressure beyond order2.

## 6. Application to escaping W2 directions

The application has the following standing hypotheses of Theory Agent B W2_FLAT_B subsection3f-ter. Let J(x1,x2,x3)=(-x2,x1,0), 2/5<c<1/2 and omega be real. A profile U in C2(R3;R3), P in C1(R3) satisfies

    div U=0, Omega=curl U, B=Ax+U,
    (1-c)U+(B.grad)U+omega JU+grad P=0,
    U.Omega=0 everywhere, and U(x)->0 uniformly as |x|->infinity.

This is class HF. Require the natural bounds |U(x)|<=C(1+|x|)^(-p) and |DU(x)|<=C(1+|x|)^(-p-1), p=(1-c)/c, with finite C. Require the established C1 local tail limit V(x)=lim_{t->infinity} exp(tL)U(exp(tA)x) away from zero, and the associated pressure limit P2 after the constant pressure at infinity is subtracted and pressure is multiplied by exp(2(1-c)t). The natural-bound pressure result gives P2 in C2 locally away from zero. In particular the pressure in Section5 has this fixed tail normalization.

The lower-window W2 witness is a nonconstant periodic B-orbit Gamma in closure{Omega!=0}, with Omega=DOmega=0, U!=0, g=U.B=0 and H=P+|U|^2/2+(Ax).U constant on Gamma. Its constant covector rate rho satisfies rho<=-2a and the covector law U(Phi_t x)^flat composed with DPhi_t(x)=exp(rho t)U(x)^flat on Gamma. An escaping trace is a B-orbit z(t) in closure{Omega!=0} intersect W^u(Gamma), different from Gamma, with |z(t)|->infinity as t->infinity. The previously established trace result supplies Omega=0, U!=0, g=0, constant H and the same covector law along z. Its scattering direction is w=lim_{t->infinity}exp(-tA)z(t), which is nonzero. The profile flow is denoted Phi_t here only to define the witness; the two-contact proof needs no global flow argument of its own.

Assume additionally that V is C2 on a neighbourhood of w. Thus the local equations of Section5 have the required regularity. All these premises are necessary to this application; smoothness and decay of U alone do not supply them.

The established tail/scattering results A1729-A1737 and A1798-A1799, together with the support result B60, supply V(w)=W(w)=k(w)=S(w)=P2(w)=0, a symmetric trace-free M=DV(w) annihilating X(w), and w in supp W. For the contradiction, assume M!=0. Then the nonflat result A1255 supplies DW(w)=0 and D2k(w)=-aM; it does not supply DW(w)=0 after the conclusion M=0 is reached. The restriction of M to E=X(w)^perp has eigenvalues +sigma and -sigma. The rate dichotomy is equality rho=-b with grad S(w)!=0, or strict rho<-b with grad S(w)=0.

At equality, differentiating grad k cross grad S=0 on the open vortical set and passing to w gives (-aMh) cross grad S(w)=0 for every h. Nonzero grad S(w) would make rank M<=1, contradicting the nonzero trace-free planar saddle. This is the existing B59(a) argument.

In the strict branch, the independently established necessary jets of B59(b), A1732, give an isotropic direction e for the quadratic form h.Mh on E and the transverse orthogonal direction f with D2k(w)=-aM and D2S(w)=-4 sigma^2 f tensor f. Here e.Me=0, while Me=tau f is nonzero. They do not assume C3, Lipschitz second derivatives, or that the configuration exists. These are exactly Assumption1. Continuity extends the tail rank relation from {W!=0} to supp W, giving Assumption2; Section5 supplies Assumption3.

For Assumption4, choose vortical x_j tending to w, as w is supported. A local flowbox for the nonzero linear field X writes x_j=exp(t_j A)y_j with y_j in w+E, t_j->0 and y_j->w. The local vorticity transport law

    W(exp(tA)y)=exp(-t) exp(-omega tJ) W(y)

preserves nonvanishing. Thus each y_j is vortical. This uses only a local flowbox about w and finite local times, not completeness of the V flow. Sections1-4 now contradict M!=0 in the strict branch as well.

Consequently every such escaping lower-window W2 direction with V in C2 near it satisfies V(w)=DV(w)=W(w)=S(w)=P2(w)=0: it is a finite-jet T0 point in the terminology of the existing results. This establishes neither infinite-order flatness nor nonexistence of the finite-jet T0 configuration. The upgrade from the naturally available C1,alpha tail regularity to C2 remains an additional assumption. The bounded W2 connections and unrestricted rotating profile theorem remain outside this argument.

## 7. Audit findings and exact scope

The submitted Step2 writes its first and third quotient-rule terms as o(r); the proved bound is O(r), which suffices because it tends to zero. Its explanation also calls k=o(r^2) on the whole disc; the correct statement is k=-a tau su+o(r^2), hence k=O(r^2). Sections2-3 above use the correct versions. These are repairable remainder descriptions, not failures of the negative derivative estimate.

This result supersedes the local strict-rate C2/C2,beta OPEN configuration in A2039 and the configuration part of A2450, when all the listed premises hold. It does not supersede the global OPEN portions of those entries. The earlier B65 estimates remain valid conditional implications but describe an empty supported nonflat configuration. The assertion that an exclusion must use a nonlocal input is refuted by this local argument.

The coordinator's complete six-section comparison agrees with the cone, the uniform derivative, the two supported contacts, the arbitrary-component contact law and the application scope. Two intermediate numerator descriptions in its Section3 omit the outer factor2, but its displayed final quotient terms and sum have the correct factors, as derived in Section3 above. Its phrase "null line of M" means the isotropic line of the quadratic form, not a kernel line of M on E. Neither shorthand affects the independently written proof.

All mathematical calculations in this proof are algebraic or analytic. The submitted symbolic checker is retained as provenance but is not needed for the proof. No formal theorem-prover verification is claimed. Exact source pins and any comparison response are kept in verification; the final audit entries must name their precise scopes and dates.

Scope correction at 2026-11-04T04:12:28.502917+00:00: Section6 now places the A1255 derivative conclusion explicitly inside the contradiction hypothesis M!=0. The local theorem and final finite-jet conclusion are unchanged. The prior wording and the independent recheck are retained in the team records.
