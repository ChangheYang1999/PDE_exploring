# Differentiating the decaying Newton pressure

Status: proved conditional identity. The conditions concern a family of represented fields, not solutions of the Euler equation.

## Hypotheses and statement

Let Θ be open in R² with coordinates (c,ω), and let U:Θ×R³→R³ be C1 in θ with smooth spatial dependence and commuting mixed derivatives. Fix θ0∈Θ. Assume there is a neighborhood K of θ0, constants C>0 and β>1/2, such that for θ∈K, p∈{c,ω}, y∈R³ and j=0,1,2,

|D^j U(θ,y)| + |D^j Up(θ,y)| ≤ C(1+|y|)^(-β-j).

Any fixed Euclidean tensor norm may be used, enlarging C if necessary. Let DU have entries ∂j Ui, and define

f(θ,y)=tr(DU(θ,y)DU(θ,y)),
P(θ,y)=(1/(4π))∫R³ f(θ,z)/|y-z| dz.

Then this integral converges absolutely, P is the unique C2 decaying solution of -ΔP=f, and

fp=2 tr(DU DUp),
Pp(y)=(1/(4π))∫R³ 2 tr(DU(z)DUp(z))/|y-z| dz,
-ΔPp=2 tr(DU DUp).

The parameter derivative of ∇P is ∇Pp, with the gradient kernel obtained by differentiating |y-z|^-1. In particular, there is no freely chosen harmonic correction. Divergence freedom is not needed to differentiate this scalar source. It is needed for f to be the pressure source of the incompressible Euler system.

## Proof

In components, f=Σi,j (∂j Ui)(∂i Uj). Differentiation gives

fp=Σi,j[(∂j Upi)(∂i Uj)+(∂j Ui)(∂i Upj)].

Interchanging i and j in the first sum shows that it equals the second. Thus fp=2tr(DU DUp). This is a matrix trace product, not 2Σi,j(∂j Ui)(∂j Upi).

Let q=2β+2>3. The hypotheses bound |f| and |fp| by a constant times (1+|z|)^(-q), uniformly for θ∈K. Both sources therefore belong to L1(R³)∩L∞(R³). Near a fixed y, the kernels |y-z|^-1 and |y-z|^-2 are locally integrable in dimension three, and the sources are uniformly bounded. Away from y, source decay gives an integrable majorant for either kernel. The parameter mean-value theorem and dominated convergence justify differentiating the Newton integral and its first spatial derivative in p, giving the formulas above.

For completeness, the Newton potential of either source tends to zero. Put r=|y|≥2. On |z|≤r/2 the potential is bounded by 2||f||1/r. On |z|>r/2 and |z-y|≤3r, the source is bounded by a constant times r^-q and the kernel integral over that ball is O(r²), giving O(r^(2-q)). On |z-y|>3r, one has |z|≥|z-y|-r>(2/3)|z-y|, so integration in |z-y| gives another O(r^(2-q)). All terms tend to zero; the same argument applies to fp.

The distributional identity -Δ(1/(4π|y|))=δ0 gives -ΔP=f and -ΔPp=fp. The assumed local spatial smoothness of the sources gives C2 classical potentials by local Newton-potential regularity. This can also be checked by subtracting f(y) in the near-field second-derivative integral; the remainder is O(|z-y|), which makes its |z-y|^-3 kernel integrable, and the subtracted constant is handled by the explicit ball potential. Finally, the difference of two C2 decaying solutions is harmonic. On a ball of radius R the maximum principle bounds its absolute value by its maximum on the boundary. Taking R→∞ proves uniqueness.

## Why the assumptions fit the intended tails

On any compact parameter set inside 2/5<c<1/2, α=(1-c)/c has a minimum greater than 1. Differentiating r^-α and the logarithmic twist introduces powers of log r. For any β strictly between 1/2 and min α, these logarithms can be absorbed by r^(min α-β) for r≥1. Thus a uniformly smooth family with the specified differentiated tail bounds implies the stated majorant. Verifying those bounds for a specific representation is a separate task; importing a finite coefficient file does not prove them.

## Interior and exterior Green integrals

Use orthonormal spherical harmonics Y_lm with -ΔS²Y_lm=l(l+1)Y_lm, and write flm(r)=∫S² f(rn) conjugate(Y_lm(n)) dn. For r>0,

Plm(r)=1/(2l+1)[r^(-l-1)∫0^r s^(l+2)flm(s) ds + r^l∫r^∞ s^(1-l)flm(s) ds].

One obtains this formula by solving the radial equation -(r²Plm')'+l(l+1)Plm=r²flm. Its homogeneous solutions are r^l and r^(-l-1); regularity at zero and decay at infinity select the displayed variation-of-constants solution. Differentiating the two integrals in r cancels their boundary terms, giving

Plm'(r)=1/(2l+1)[-(l+1)r^(-l-2)∫0^r s^(l+2)flm(s) ds + l r^(l-1)∫r^∞ s^(1-l)flm(s) ds].

Parameter differentiation replaces flm by (fp)lm in BOTH integrals. Their geometric kernels have no physical dependence on c or ω. A numerical twisted-frame or factored-source representation may place parameter dependence in its kernel matrices, phase rotations, extrapolation and source weights. The full derivative must include those numerical dependencies. Differentiating sampled f while freezing such a matrix does not generally differentiate the implemented pressure.

At a finite quadrature cutoff R(θ), Leibniz's rule adds boundary terms from R'(θ) and differentiation of any appended tail. A parameter-dependent partition of an exact integral contributes canceling internal endpoint terms. A discretized adaptive partition need not have exactly canceling derivatives; numerical convergence must be tested across partition changes as well as within fixed partitions.

## Field consistency and divergence check

Suppose now div U=0 and define R as in the companion proof. With (DU)ij=∂j Ui, differentiation in y yields

div[(c y-ωJy)·∇U]=c div U-ωΣi,j Jji ∂j Ui,
div(ωJU)=ωΣi,j Jij ∂i Uj.

Relabeling i,j in the second expression gives cancellation of the two rotation terms. Also div(U·∇U)=tr((DU)²) because div U=0. Hence div R=f+ΔP. For the exact Newton pressure this is zero for every divergence-free field, even when R itself is nonzero. Differentiating gives div Rp=fp+ΔPp=0.

This is a useful consistency check, but its small defect alone does not bound R or certify pressure accuracy. If a supplied DU is not the derivative of the supplied U, cancellation in this calculation is not justified. Pressure agreement using the same inconsistent source is also insufficient. Spatial finite differences or a separate differentiable field reconstruction are required to test that issue.
