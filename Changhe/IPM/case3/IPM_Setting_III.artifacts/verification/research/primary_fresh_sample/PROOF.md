# Three primary fields on a fresh fixed sample

Written 2026-10-22T11:21:32.840620+00:00, before the sample is evaluated. Status OPEN until independent computation, arithmetic check and actual model review. This result tests whether observations of the earlier selected union persist on a new sample specified without looking at its field values. It is no additional solver run, physical-domain study, or smooth-limit theorem.

## Fields and full-plane inverse

Read the exact input JSON attached to each original frozen coefficient field. Set r squared=x squared+y squared, w=(1+r squared/L squared)^(-alpha), t=1-2w, z=(x+i y) squared/(L squared+r squared). The density is

    rho(x,y)=y w sum over k of Re(z^k) P_k(t),

where P_k is the finite Chebyshev polynomial with the imported coefficients. Here L>0,0<alpha<1/2 and ell=5/2. The exact rational alpha and coefficients retain their original binary64 meanings. The density is smooth on the full plane, even in x and odd in y. Its slope at zero is the alternating sum of the k=0 coefficients. Its sublinear exponent is p=1-2alpha. No x squared factor or prescribed stream is introduced.

For f=rho_x, let f_n be its sine angular modes. The canonical stream has mode

    psi_n(r)=[r^(-n) integral_0^r s^(n+1) f_n(s) ds
              +r^n integral_r^infinity s^(1-n) f_n(s) ds]/(2n).

The finite source decomposition has only even n>=2. The integrals converge at zero by smoothness and at infinity by p<1. This Green formula solves -Delta psi=f, is regular at zero, gives U=(-psi_y,psi_x)=o(r), and has the required parities. A sublinear harmonic velocity difference is constant and parity removes it. Thus no extra harmonic strain is available. The factored radial primitives and their independent derivation are in ../smooth_full_inverse_primitives/PROOF.md, with the accepted manufactured gate and source hash. Use that own implementation, never producer numerical code. Cartesian MP differentiation evaluates grad rho; exact rational source-tail sums independently evaluate c=psi_xy(0).

For a one-mode manufacture rho=a y(1+r squared/L squared)^(-alpha), f_2=-alpha a r squared/L squared (1+r squared/L squared)^(-alpha-1). Consequently c=(1/2) integral_0^infinity f_2(s)/s ds=-a/4. This follows by a single radial substitution, including the origin contact contribution that a naive absolutely convergent third-mode-only formula would miss. It is a prospective check of the imported primitive's strain, not an assignment of the required profile strain. The manufactured field need not solve transport.

## Prospective sample and finite statements

The sample is101 distinct binary64 points, fixed in verification/INPUTS.json before candidate evaluation. It is deliberately stratified, not random and not claimed unbiased. For i=0,...,63, set r=10^(-6+18(i+1/2)/64), theta=(pi/2)(0.01+0.98 vdc_2(i+1)), where vdc_2 reverses the finite binary digits after the radix point. Use(x,y)=(r cos theta,r sin theta). For i=0,...,15, set r=10^(-4+12(i+1/2)/16), e=10^-6(1+i mod3), and add both angles e and pi/2-e. Finally add(0,0),(0,10^-6),(0,1),(10^-6,0),(1,0). The elementary-function construction uses Python binary64 math, and the resulting exact binary64 operands, not ideal transcendental coordinates, define the experiment. Store decimal and hexadecimal forms, group and index; check distinctness. These are independently chosen evaluation points, not a grid extracted from fitting nodes. Deliberate symmetry-axis probes are retained.

At every same point evaluate all three original N36/N40/N44 fields at75 and110 displayed digits. Keep the actual imported ell=5/2, exponent and strain. No numerical result from the old51 points determines this sample. Record the source coefficients and original exact rational JSON by hashes. The independently implemented modal inverse and Cartesian derivatives are the same verifier primitives already tested with explicit fields and direct full-plane quadrature. These do not use the numerics lane's code.

For R=(ell X+U).grad rho-rho, Nf=|(ell x+U1)rho_x|+|(ell y+U2)rho_y|+|rho| and Nv=|rho|+|X.grad rho|+|U.grad rho|, recompute every stored residual and denominator from110-digit decimal operands using separately written exact Fraction arithmetic, within scaled1e-90 rounding tolerance. Compare all15 stored fields across precisions within scaled1e-65. Neither is an accuracy enclosure. Where a denominator is zero keep the ratio undefined and retain absolute R. Triangle inequalities give abs(R)<=Nf and abs(R)<=ell Nv and serve as arithmetic checks.

Report maxima and locations over the complete sample, each construction group, and exact input-coordinate restrictions r<=1,100,10^4,10^8,10^12. Compare old and new maxima only as observations on different sets; if useful provide the maximum over their union by taking the larger finite maximum. These masks are not independent domain runs, and neither increasing nor decreasing sampled maxima proves a trend in a continuum supremum. Origin and horizontal-axis ratios remain undefined. A new larger peak changes a finite observation, not the endpoint by itself. The prior matrices remain immutable and are labelled with their original sample scope.

## Evidence and execution

Use one detached heavy process only, nice19, one CPU thread,14GiB memory cap; the previous334 process must have exited. Every foreground shell command ends within10minutes. No JavaScript/TypeScript/Node, servers/listeners/tunnels, RLScience cluster, GPU, Lean/Lake, commits/push/posts or human contact. All writes stay in this lane. Gate candidate execution on retained manufacture checks and an actual Opus5.5 design review. Preserve failures. Snapshot exact input/code/proof and runtime metadata, save atomic progress, then independently recompute finite arithmetic before actual results review. Record real times. This supplement neither shortens the48-hour run nor supplies a decisive endpoint.
