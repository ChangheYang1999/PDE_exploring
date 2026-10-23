# Common-point multiprecision comparison of three primary trial fields

Written 2026-10-22T10:15:31.155313+00:00, before this new finite comparison. Status OPEN until the computation and separate checker finish. This result addresses only the sampling mismatch in the earlier N36/N40/N44 selected maxima. It neither supplies another solver run nor proves existence, nonexistence, or convergence.

## Fields and full-plane inverse

Read the exact input JSON attached to each original frozen coefficient field. Set r squared=x squared+y squared, w=(1+r squared/L squared)^(-alpha), t=1-2w, z=(x+i y) squared/(L squared+r squared). The density is

    rho(x,y)=y w sum over k of Re(z^k) P_k(t),

where P_k is the finite Chebyshev polynomial with the imported coefficients. Here L>0,0<alpha<1/2 and ell=5/2. The exact rational alpha and coefficients retain their original binary64 meanings. The density is smooth on the full plane, even in x and odd in y. Its slope at zero is the alternating sum of the k=0 coefficients. Its sublinear exponent is p=1-2alpha. No x squared factor or prescribed stream is introduced.

For f=rho_x, let f_n be its sine angular modes. The canonical stream has mode

    psi_n(r)=[r^(-n) integral_0^r s^(n+1) f_n(s) ds
              +r^n integral_r^infinity s^(1-n) f_n(s) ds]/(2n).

The finite source decomposition has only even n>=2. The integrals converge at zero by smoothness and at infinity by p<1. This Green formula solves -Delta psi=f, is regular at zero, gives U=(-psi_y,psi_x)=o(r), and has the required parities. A sublinear harmonic velocity difference is constant and parity removes it. Thus no extra harmonic strain is available. The factored radial primitives and their independent derivation are in ../smooth_full_inverse_primitives/PROOF.md, with the accepted manufactured gate and source hash. Use that own implementation, never producer numerical code. Cartesian MP differentiation evaluates grad rho; exact rational source-tail sums independently evaluate c=psi_xy(0).

For a one-mode manufacture rho=a y(1+r squared/L squared)^(-alpha), f_2=-alpha a r squared/L squared (1+r squared/L squared)^(-alpha-1). Consequently c=(1/2) integral_0^infinity f_2(s)/s ds=-a/4. This follows by a single radial substitution, including the origin contact contribution that a naive absolutely convergent third-mode-only formula would miss. It is a prospective check of the imported primitive's strain, not an assignment of the required profile strain. The manufactured field need not solve transport.

## Fixed common point set

Freeze the union of every original MP input-coordinate file admitted by the accepted N36/N40/N44 manifests. Use exact binary64 coordinate identity, preserve source provenance for each point, and sort deterministically. Preliminary inspection gives51 distinct points, including origin, horizontal/vertical-axis and extreme-radius samples; freeze and check this count instead of selecting after seeing the new residuals. This is an a posteriori union of earlier searches, not an independent random or exhaustive grid. Every state is evaluated at every same point at75 and110 displayed digits with the primitive's extra internal conditioning precision. No optimizer is rerun and no exact exponent or strain is substituted.

For each point compute R=(ell X+U) dot grad rho-rho, Nf as the sum of absolute directional transport terms and abs(rho), and Nv=abs(rho)+abs(X dot grad rho)+abs(U dot grad rho). Undefined zero denominators stay undefined; report raw R and denominators. The separate checker recomputes these from110-digit decimal operands as exact fractions, allowing scaled1e-90 rounding discrepancy, and checks all75/110 fields at scaled1e-65. These are finite consistency tolerances, not error enclosures. Rf<=1 and Rv<=ell follow by the triangle inequality and are useful arithmetic checks.

Recompute every extent mask x squared+y squared<=R squared from the original binary64 coordinates in exact rational arithmetic. Give the complete common-set maxima and the restrictions to radii100,1e4,1e8,1e12 and1e250, with locations, sample counts, absolute residual and both ratios. Near the nominal1e250 boundary use exact membership, never decimal intuition. These restrictions do not become independent physical-domain runs. Compare repeated original point records and new outputs at matched coordinates; the old selected peaks need not equal the common-set peaks.

The only admissible trend statement concerns these fixed finite samples. If the values decrease, that supplies limited additional numerical evidence, not systematic full-plane convergence. If they increase, that is a finite observation, not a proof that the true suprema increase. No nonzero finite residual coefficient alone rejects numerical YES. The primary combined endpoint is assessed separately.

## Execution and evidence

Run only after333 has exited, as the lane's sole heavy process at nice19, one CPU thread and14GiB memory cap. No GPU, JavaScript/TypeScript, servers/listeners/tunnels, RLScience, Lean/Lake, commits/push/posts or human contact. All writes remain inside this lane. The worker must refuse an existing candidate directory, bind input/code/proof/manufactures, record real process/module/runtime metadata, save atomic progress and recheck hashes before completion. Its checker is a separate program. Review any failures and final outputs with actual Opus5.5; preserve rejected or unavailable responses.
