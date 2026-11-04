# Note107 report repairs and precise remaining scope

Status: review completed at the scopes below. A2163-A2170, A2172, A2174-A2175 are CONFIRMED. A2171, A2173 and A2176 are OPEN. This does not approve the whole report or prove the unrestricted conjecture.

## 1. Objects, hypotheses and evidence

This audit compares the Note107 five-file assembly with the Note106 assembly, both retained in verification. The current this report and this report are identical, SHA256 ba3784e49fa1efb88b17784b7ba0fb00d01ae9bb2fece643ef09140df4bc0588. It has 6544 split lines. The five diffs are retained; the Euler diff repeats the identical report diff. All changed mathematical passages and their contexts were read, with long table rows read separately. No mathematical computation was required.

Write Jx=e3 cross x, A=cI-omega J, X=Ax, a=1-2c, b=2(1-c), eta=a/b, k=X.V, W=curl V, S=P2-|V|^2/2. Unless otherwise stated the tail discussion has 2/5<c<1/2 and any real omega. A natural actual tail means that the global C2/C1 profile solves the full momentum and divergence equations and has both bounds |U(y)|<=C(1+|y|)^(-p) and |DU(y)|<=C(1+|y|)^(-p-1), p=(1-c)/c. A local reduced construction is not automatically an actual tail.

The dependencies are the complete independent audits upper_pressure_removal_20261103, tail_y_closure_20261103, strain_forms_20261103, mixed_strain_instances_20261103, mixed_strain_cover_20261103, arbitrary_axial_hessian_rank_20261103, positive_pressure_arc_orders_20261103, next_pressure_hessian_20261103, positive_arc_isotropic_pressure_20261103, flat_pressure_means_20261103 and nonzero_pressure_zero_structure_20261103. Each contains its standalone argument and exact scope. This audit checks the assembly against those proved implications.

## 2. Global comparison and the sector alternative

The new summary item10, Theorem7(g), T41 and O12 distinguish two statements. With the full structural equations and rank relation, the global upper comparison and a lower comparison near all common zeros suffice for rigidity. Without the rank relation, LIT271's irrotational-sector alternative is invoked only with the original global two-sided comparison on the whole unit sphere. Its proof uses that comparison away from common zeros as well; the localized lower bound has not been shown to suffice. The repaired passages expressly retain this distinction, so A2066 is resolved as a report-scope repair. Neither comparison follows here from decay.

## 3. Strain densities and exact mixed bounds

Theorem8 now writes the density

    D=a0|S0|^2+b0 tr(S0^3)+(3b0/4-2g'(t)) W0.S0W0
                       +2g'(t)t-3c g(t)-a0 t/2, t=|W0|^2,

where S0=sym DU and W0=curl U, to avoid confusing profile strain with tail pressure S. SF.2 is stated for real constants a0,b0, g in C1([0,infinity)), g>=0, g(0)=0, and a compact trace-free symmetric-matrix set K containing a neighborhood of zero with max_K lambda_max>=1. Nonnegativity on K times all W0 forces a0>=0; a0=0 gives b0=g=0. The three stated one-parameter strain sets and their lower parameter restrictions match A2006-A2008. This is a classification of that density family, not all possible estimates.

SF.3 retains a0>0, g in C1([0,M^2]), g>=0, g(0)=0, g'(0)>a0/[4(1-3c/2)], compact strain K, and strict positivity on the entire product K times {|W0|<=M} away from (0,0). It is applied only to global C2/C1 profiles with Hb and 0<c<2/3. The master cutoff identity and finite energy-growth iteration are those checked at A2004-A2009. Thus A2067/A2077 are repaired. The split table rows correctly remove any vorticity bound from the strain-only criterion.

The two C63 instances and all six C64 rows match A2079-A2083 and A2121-A2125 exactly. The six comparison windows cover (2/5,1/2], but every theorem still requires both global bounds. Exact positivity was checked on 83 rational Bernstein subintervals in the earlier audit; it is not rerun here. The report does not assert optimality or infer those bounds from decay. These new statements are faithful.

## 4. Negative-pressure components

For Y={W!=0} intersect int{k=0}, the actual-profile sign input makes Y intersect {S<0} both open and closed in {S<0}. Hence a connected component C of {S<0} lies in Y or is disjoint from Y. In the former case k=0 and the negative power formula cannot hold. Only in the latter case does k!=0 on C intersect int(supp W), and S=D|k|^q, D<0, on each connected component of that intersection. The new C58 row puts the formula precisely there, includes V=W=0 on C intersect int{k=0}, and keeps the actual-profile sign/equality hypotheses. This resolves the false earlier attribution A2068 without changing the source theorem.

## 5. Closedness, removal and the Harnack domain

The report now retains div V=0, DV X=-((1-c)I+omega J)V, X.grad S=-bS, Delta P2=-tr((DV)^2), W.grad S=0, and k=0 or grad k cross grad S=0 on {S!=0}, as well as the upper comparison and V in C1,alpha with alpha>2/c-4. These structural premises give classical closedness of beta=|S|^(-eta)V on {S!=0}. In particular the vector homogeneity implies X cross W=grad k+aV, so the needed contraction identity has not been dropped.

The Poisson regularity and upper bound give the root estimate and continuous extension, with beta in W1,t locally for 1<=t<1/(1-rho), rho=c/[2(1-c)], and derivative zero almost everywhere on {S=0}. The classical curl identity therefore extends distributionally. The countertest V=(1,sin x1,0), P2=2 has div V=0, tr((DV)^2)=0 and |V|^2<=2S, but curl beta=(3/2)^(-eta)e3 at x1=0. It lacks the structural homogeneities and refutes closedness from only Poisson and comparison, as the new text explicitly states.

The global primitive and the zero-flux argument then give k=0 and invariance under X. The weighted Harnack statement is now confined to balls where w=R^(-tau) is locally integrable and bounded below by a positive constant. The upper comparison supplies the lower bound on w but does not supply its integrability. At an extremal-boundary common zero the earlier proof forces infinite integral over {V!=0}; a lower comparison in a neighborhood of every common zero bounds w there and contradicts it. This is the precise A2020-A2026 argument. A2069/A2070/A2105 are repaired. The H/H0 citation now points to the translated identity checked at A2104.

## 6. Axial jets and positive-pressure arcs

The LIT282-LIT284 statements now include analytic harmonic f,Q near e3, X.grad f=-af, X.grad Q=-bQ, f(e3)=1 and zero transverse gradient. With E=|grad f|^2/a^2 and S=Q-E, the rank field grad f cross grad S cannot vanish through order five for any transverse Hessian. The negative-distinct, isotropic and remaining distinct-root branches are exactly those checked at A2049-A2060 and A2093-A2097. The exceptional order-four germ at c=5/11, omega=0 has rank order five, not an unrestricted profile. Off-axis points, nonzero transverse gradients and existence of an appropriate axial matching point stay open.

The new LIT285 row correctly allows any finite N>=2 on an orbit arc off the rotation axis and says that nonradial applies only when omega!=0. LIT286 uses a genuine next scalar p1, all its transport and Poisson identities, and the full natural actual-profile transfer. It gives isotropy of 3D2S+(eta/S)dS tensor dS on X-perp. LIT287 supplies local altered pressure data meeting this necessary condition; it does not supply p1 or a profile. These rows are faithful at A2086-A2089 and A2107-A2118. The later LIT289 exclusion of the exact axial LIT287 data is separate and was not yet in this pin.

## 7. Pressure means: a confirmed direction and a wording repair

The main new C60 paragraph and row retain smooth local equations on a flowbox, k=0, S=0 on the central orbit, S<0 off it and common flatness. With T=tr((DV)^2), P=S+|V|^2/2, the exact identity is

    M'(r)=-(4 pi r^2)^(-1) integral_(B_r) T, M(0)=0.

T>=0 on a ball forces M(r)<0 for all its positive small radii; if equality held, T would vanish on an inner ball, harmonic flat P would vanish, and the previously proved constant-ratio continuation would contradict S<0. The reverse signs give the other implication. The sequence and trichotomy consequences in the report follow by contraposition. This is faithful and does not assert the false converse identified at A2161-A2162 in C's separate note.

One shorthand in the new ledger row says, for omega=0 with zero period, 'T>0 near x0'. The proved conclusion is that T>0 at points arbitrarily close to x0, not throughout a punctured neighborhood. The main paragraph already has the precise version. The row should use the same explicit quantifier. Until then this wording extension is OPEN A2171; C60 itself remains CONFIRMED.

## 8. Supported zeros are essential to the actual-tail corollary

The local LIT288 theorem is correctly stated as a dichotomy: either V=0 on the connected open G, or every zero has finite order N>=1, W has the same order, and the common zero set is locally one X-orbit arc. The scalar drift is smooth and bounded on each sufficiently small relatively compact ball. Global boundedness of the drift on an arbitrary G is not claimed; 'locally bounded drift' is the precise short wording.

The actual-tail source in LIT288 Section6 explicitly assumes a supported common zero p in supp W. This excludes the identically-zero local branch, since every neighborhood of p then meets {W!=0}. Its pointwise actual-profile law gives DV(p)=0, hence N>=2, and the next scalar gives the LIT286 Hessian condition. The Note107 main paragraph and LIT288 ledger row omit 'supported' before their actual-tail zero. The proof does not remove it. A2173 is OPEN for that enlarged actual-profile reading. Restore p in supp curl V or explicitly retain the nonzero branch. A2140 has always to be read with this source hypothesis; the final application paragraph in the earlier independent proof is qualified here as well.

There is a direct local countertest to removing the branch condition from the reduced equations, even with Poisson and a next scalar. On a branch near (1,0,0), let z=x1+i x2, nu=-b/(c-i omega), V=0, S=P2=Re(z^nu), and p1=0. The function S is positive on a small neighborhood, harmonic since it is the real part of a holomorphic function independent of x3, and X.grad S=-bS since Xz=(c-i omega)z. Every vector, divergence, contraction and transport identity is zero, and -Delta P2=tr((DV)^2)=0. With Z=grad P2, also -Delta p1=2tr(DV DZ)=0. Yet every point is an infinite-order zero of V and none is supported. This is a local reduced solution, not a whole-space profile. It proves why the local dichotomy cannot be silently discarded, without refuting the actual supported-zero theorem or establishing a global counterexample.

## 9. Unchanged full proofs and remaining report coverage

The independent byte comparison in the team records proves that current sections2A,2B,2C,2D are unchanged from the pinned Note106 file. Their full evening audits are A2148-A2152, A2142-A2146, A2040-A2043 and A2072-A2076, respectively. The 2C comparison with its earlier evening snapshot differs only in the already audited label paragraph. Thus the new source pin preserves those confirmations at their exact scopes. In particular 2C does have a recent full audit beyond the older A1217 reference.

This review does not replace the pending whole-assembly coverage of the remaining front matter, sections3-10 and appendices. Unchanged older verdicts are retained; no unread addition is approved here. The unrestricted nonexistence problem for arbitrary helicity and omega remains open. The two live precision repairs are the existential positive-T wording and the supported-zero premise. No numerical or formal build was needed, and no new model client was used. Existing configured model agent-file collaboration supplies the compared proposals; its actual provider execution is not independently attested.
