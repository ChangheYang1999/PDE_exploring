# Normalization in the finite-order pressure-ratio claim

## 1. Literal row and counterexample

The Appendix A LIT261/LIT262 row in the pinned report says that a finite-order incompressible velocity zero with continuous pressure has limsup R >= 1. The ratio conclusion needs the extra assumptions of A1762, not just the preceding mean identity.

On a ball about zero in R3 set v=(x2,x1,0), E=x1^2+x2^2 and P=-1-E/2. Then div v=0, curl v=0, (v.grad)v=(x1,x2,0) and grad P=-(x1,x2,0). Thus stationary momentum and div div(v tensor v+P I)=0 hold. The velocity has first order one at zero. Put H=E/2-P=1+E, S=-H and R=E/H. Then H>0 and lim R=0 at zero. All fields are smooth. The condition v=0 on {H=0} is vacuous, so even adding it and H>=0 does not repair the omitted normalization P(0)=0.

This is a local stationary countertest. It is not twisted homogeneous and is not an entire decaying rotating profile. It refutes the condensed unnormalized local claim, not the original audited theorem.

## 2. Correct statement and proof

Let m>=1, v in C^m and P continuous near zero, div v=0 and div div(v tensor v+P I)=0 distributionally. Suppose v has first nonzero homogeneous Taylor term V_m of degree m. Assume in addition P(0)=0, H=|v|^2/2-P>=0 and v=0 on {H=0}. Define R=|v|^2/H on {H>0}. Then limsup at zero through {H>0} of R is at least one.

Indeed A1760-A1761, whose complete standalone proof is copied in the team records, give

    lim <P(0)-P>/<|v|^2> <= 1/2,

where the brackets are averages on small spheres centered at zero. If limsup R<1, choose 0<Rstar<1 with R<=Rstar on {H>0} near zero. There -P>= (1/Rstar-1/2)|v|^2. On {H=0} both v and P vanish, so the same inequality holds throughout a smaller ball. Averaging and using P(0)=0 contradicts the displayed upper bound, since 1/Rstar-1/2>1/2. The assumption of a nonzero Taylor term makes the sphere energy positive for all sufficiently small radii.

Equivalently one can always use the shifted scalar H0=|v|^2/2-(P-P(0)), provided H0>=0 and v=0 on {H0=0}, and define the ratio with H0. One cannot keep the unshifted ratio after shifting pressure only in the proof.

## 3. Audit and report repair

The exact finite-jet pressure mean, with P(0)-P explicitly subtracted, is unchanged. The equality characterization concerns the leading homogeneous jet. Restore P(0)=0, H=|v|^2/2-P>=0 and v=0 on {H=0} for the row's ratio consequence, or state the shifted version. The pressure identity and the independent LIT262 angular-frequency clause are not refuted here.

All six sections of the earlier independent proof and all three sections of this proof were read. No computation is required. The unconditional rotating Euler conjecture remains open.
