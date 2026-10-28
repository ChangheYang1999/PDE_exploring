# Lead alpha=3/10 projection-cusp certificate

For real functions on R^2 use the homogeneous seminorm[f]_(3/10), circular
principal-value kernels K_xx=cos(2theta)/(2pi r^2), and R_1^2=T_xx-I/2,
with increments modulo constants as in ../../01_setup/PROOF.md. Then

    D_(3/10)>=2.9418686222.

Use the witness and full proof in
../../11_lattice_pole_constraints/axis_projection_stieltjes/PROOF.md with
alpha=3/10,b=3/2,shift=0,K=1007/1000. The geometric profile certificate
data/geometric_profile_a30_tight.json proves the required seminorm
bound because alpha<=1/2; its source hashes and full-tree completion
identity have been checked. Thus the witness has seminorm at most one,
pole values -1/2 and1/2, and exact diagonal increment
1+4 integral V(-d_Yf). All omitted portions have positive sign.

The finite Stieltjes grid has32768 strips for each sign and256 vertical
ratio intervals, logs[-18,24] for the outer sign and[-18,log(1/2)] for
the inner sign, and vertical logs[-12,14]. Each strip contributes the
certified variation decrease times the minimum endpoint value of V
and the strip width. The proof above establishes unimodality of V
and monotonicity of the witness, so this is a rigorous lower sum.

The eight saved chunks form exactly one cover of both strip partitions.
The independent audit recombines the printed component intervals as
exact rationals and verifies every source hash. Its lower endpoint is
at least2.94186862221497579, so downward rounding yields the stated
number. No claim is made about a complete upper enclosure of the
witness or the sharpness of the finite parameters.

Evidence:verification/independent_audit.json. The original source and
chunk paths and hashes are included there; they are read-only in the
lead investigator. The computation used the verifier source with only three
path-handling expressions changed, checked by direct source comparison.
