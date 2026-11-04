# Original and tail vorticity density are equivalent

Status: CONFIRMED, independent correction and extension of CO34.

## 1. Exact assumptions and conclusion

Let c satisfy 1/3<c<1, let omega be any finite real number, and put Jx=(-x2,x1,0), A=cI-omega J and T_t=exp(tA). Let U in C2(R3;R3) and P in C1(R3) solve

    div U=0, (1-c)U+DU(Ax+U)+omega JU+grad P=0.

Assume U is bounded, U(R .)->0 in distributions, and

    integral_1^infinity m(r)dr/r<infinity,
    m(r)=sup_(|x|>=r)|DU(x)|.

Write Omega=curl U, M=sup|U|, and let Phi_t be the complete flow of B=Ax+U. Let

    Xi(x)=lim_(t->infinity) T_(-t)Phi_t(x),
    K=Xi^(-1)({0}), E=R3 minus K, D=R3 minus {0}.

The confirmed A209-A210 scattering theorem gives Xi:E->D a C1 diffeomorphism, |Xi(x)-x|<=M/c, K compact and null, and the actual continuous vorticity tail W with the exact identities

    W(Xi(x))=D Xi(x)Omega(x), x in E,
    W(T_t z)=exp(-t)exp(-omega tJ)W(z).

Under these assumptions the following are equivalent:

(i)  {Omega!=0} is dense in {|x|>R} for at least one finite R.
(ii) {Omega!=0} is dense in E.
(iii){W!=0} is dense in D.
(iv) {Omega!=0} is dense in all of R3.

No helicity or pressure normalization hypothesis is needed for this equivalence. Natural velocity and gradient bounds imply the assumptions. Uniform U->0 together with any derivative premise in A601 also implies them when c>1/3.

## 2. Proof of equivalence

Because D Xi is invertible, Omega(x)=0 if and only if W(Xi(x))=0 for x in E. A homeomorphism preserves density. Hence(ii) and(iii) are equivalent. Since K is compact, E contains an exterior region, so(ii) implies(i). Since K is null and closed, E is dense in R3. Thus(ii) also implies(iv): every nonempty open set in R3 meets E in a nonempty open set. The reverse implication(iv) implies(ii) follows because E is open.

It remains to show(i) implies(iii). Suppose otherwise. Continuity of W gives a nonempty open set O in D on which W=0. Shrink O to a ball with compact closure in D. Then inf_O|z|=delta>0. Twisted homogeneity gives W=0 on T_t O for every t. Choose t large enough that exp(ct)delta>R+M/c. The set Xi^(-1)(T_t O) is a nonempty open subset of E because Xi:E->D is an onto diffeomorphism. For every x there,

    |x|>=|Xi(x)|-M/c>R.

The exact scattering identity and invertibility of D Xi force Omega=0 on this whole set. This contradicts(i). All four conditions are equivalent.

The proof uses the exact scattering identity, not just convergence of rescaled vorticity. Uniform convergence alone would not give this conclusion. A595 did not infer tail density; that limitation of its argument is not a nonimplication theorem.

## 3. CO34 and the full conditional profile theorem

Restrict now to 2/5<c<1/2 and suppose, additionally, that U->0 uniformly, U.Omega=0 everywhere, and DU=O(sqrt(|x|)). Let V and P2 be the actual tails supplied by the confirmed natural-tail package. Put

    a=1-2c, p=(1-c)/c, beta=(p-1)/(2p),
    k=(Ax).V, S=P2-|V|^2/2.

Suppose either S is identically0, or b=|S|^beta is a locally A2 weight on D. If any one of(i)-(iv) holds, then U=0 by A598 and the equivalence above. The A601 derivative alternatives may replace DU=O(sqrt(|x|)); all other hypotheses remain. This confirms CO34's conditional conclusion. Its remark that original exterior density and tail density are not known to imply one another must be replaced by the proved equivalence.

There is also the source's direct proof. A539 gives continuous grad k and grad S. A413 and actual C1 tail convergence imply grad k cross grad S=0 on {W!=0}. Tail density extends this rank equation to D, and A596 gives V=0. If S is identically0, the mean identity A591 already gives V=0. Finally the zero-tail improvement and the vanishing energy boundary terms in A570/A598 give U=0. This argument is consistent with, and is now a second proof of, the density replacement.

## 4. Rank failure forces an actual irrotational spiral region

Retain the full-profile, helicity, decay and derivative hypotheses of Section3, without assuming any of the equivalent density conditions. Suppose U!=0 and b=|S|^beta is locally A2. Then S is not identically0, and

    Sigma_0={z in D: grad k(z) cross grad S(z)!=0}

is nonempty by the contrapositive of A596 and zero-tail rigidity. It is open. It is invariant under T_t, because

    (grad k cross grad S)(T_t z)
       =exp(-(3-2c)t)exp(-omega tJ)(grad k cross grad S)(z).

It is contained in {W=0}, since the rank equation already holds on {W!=0}. On Sigma_0 the actual linear Lamb identity gives V=-grad k/a and Delta k=0. Also Pi=P2+|V|^2/2 is harmonic and S=Pi-|V|^2. In particular grad S is not parallel to V there, and neither gradient vanishes.

This tail rank defect forces more than an open zero set in the limit. Set H=P+|U|^2/2+(Ax).U, R=P-|U|^2/2 and let P_infinity be the normalized constant supplied by the confirmed pressure theorem. For every compact subset of D, A539 gives

    h_t(z)=exp(at)(H(T_t z)-P_infinity)->k(z) in C1,
    r_t(z)=exp(2(1-c)t)(R(T_t z)-P_infinity)->S(z) in C1.

For the first convergence, h_t=k_t+exp(-t)(p_t+|u_t|^2/2), where u_t(z)=exp((1-c)t)exp(omega tJ)U(T_t z), p_t(z)=exp(2(1-c)t)(P(T_t z)-P_infinity), k_t=(Az).u_t, and these tail fields are uniformly bounded in C1 on compact subsets. Choose a ball O with compact closure in Sigma_0 and with |grad k cross grad S| bounded below by a positive number on its closure. For all t>=t0, grad h_t cross grad r_t is nonzero throughout O. The chain rule then gives grad H cross grad R nonzero throughout T_t O. A413 states that this rank is0 on the original vortical set, so

    Omega=0 on the open set union_(t>=t0) T_t O.

This is an actual irrotational region meeting arbitrarily large radii. It follows directly from C1 convergence and original rank, with no unsupported unique continuation across its boundary. Exterior real analyticity would force Omega identically0 in that connected exterior and hence U=0 by A595, so a hypothetical nonzero profile in this class is analytic on no full exterior region.

## 5. Dependencies and scope

The diffeomorphism, its surjectivity, invertible derivative, null zero fibre and the exact vorticity identity were reread in full in auditor_proofs/proofs/scattering_conjugacy/PROOF.md and auditor_proofs/proofs/scattering_profile_tail/PROOF.md. The derivative composition A601, rank A413, C1 tail convergence A539, canonical mean A591 and weighted exclusion A596/A598 supply the explicitly conditional profile corollaries. The existing configured-model coordinator source in the team records was read and compared; its theorem is correct and its stated comparison of assumptions is repaired here. No new model client or numerical computation is used. The unrestricted bare-decay conjecture remains open.
