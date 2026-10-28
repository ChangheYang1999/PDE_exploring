# Completed three-mode pure-spline section: accounting and exact input comparison

## Statement and scope

Use the exact degree-seven stride60 B-splines b_i, i=4,...,29, and the three angular modes m=1,2,3 of proof 198, in their stored positive binary scales from S1M4P/meta.json. The78 columns are u_(i,m)=r^3 cos(theta)^2 sin(theta)b_i(log r)(cos(2m theta)-(-1)^m)/s_i. Their low input norm is L2(w), with w=|cos(theta)|^(-17/2)e^(mu(log r)), mu(t)=-17t/2 for t<0 and -5t/4 for t>=0. Let G be their exact input Gram and G_f the exact dyadic interpretation of the symmetrized binary matrix in evidence/parts_matrices.npz.

For every nonzero v in R^78,

 |v^T(G_f-G)v| < (336/125000000) v^T G v = 2.688e-6 v^T G v.       (1)

The stored completed quadrature run assigns its1569 cell IDs exactly once to its four final parts. Retained checkpoints duplicate1531 of those same cells and are excluded. This is an accounting result. The output Gram B_f is a floating quadrature result with no rigorous total output-pair enclosure. No displayed generalized eigenvalue is a certified value for the exact operator.

The78 columns all belong to the low transport graph. By proof 206, only66 belong to the fixed high input space, and60, i=7,...,26 in all three modes, belong to its high graph. Any values computed below on those60 columns still use the low norms. No high-norm lower bound, actual base injectivity, complement inverse or nonlinear closure follows.

## Accounting proof

The original production log specifies1569 cells and four workers and records all four completed worker counts. The final part_0,...,part_3 files contain their exact integer done arrays. Each is the subsequence wid,wid+4,... of the exact expected list0,...,1568. These four sets are disjoint and their union is the expected list; their cardinalities393,392,392,392 agree with the stored diagnostics and the completed log. No base files or resumed producer history are present. Every checkpoint done array is a prefix of its worker's final array. Adding a checkpoint to its final part would count those cells again, so the verifier sums final parts alone using math.fsum entry by entry, then takes the binary symmetric part. Both resulting matrices are finite78 by78 arrays. This defines the precise binary matrices certified or diagnosed here, including their rounding. It does not remove errors made while producing any cell contribution.

The original running producer used pseudoinverse angular division, including the low input templates. The producer on disk was subsequently repaired. Its snapshot is explicitly named current_producer_NOT_original_running_code.py and is not asserted to be the code executed by this run. Source metadata, cell coverage, exact basis scales, final parts and the completed log are separately preserved and hashed.

## Proof of the input comparison

Proof 198 reconstructs G directly from the immutable original Analysis I trial, using rational Cox-de Boor polynomials, independent de Boor identities, exact angular Beta moments and directed exponential radial moments. Its512-bit and640-bit constructions and fresh768-bit replay were accepted in V202. The original source SHA256 is a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874 and the78-column certificate SHA256 is bc7512502550c11fd5ba859d7b4630ae70b7d643ff2de6d6af5e329e9261d606. The present metadata hash is exactly the one used by that certificate. Thus the saved interval matrix encloses the exact Gram of the declared scaled columns.

Choose T by floating Cholesky whitening of the interval midpoint, then treat every entry of T as its exact binary rational. Directed640-bit arithmetic applied to the saved interval enclosure yields

 e = ||T^T G T-I||_2 < 1.131e-11,
 d = ||T^T(G_f-G)T||_2 < 2.687787e-6,
 d/(1-e) < 2.688e-6.

Here the computed maximum absolute row sums of symmetric matrices are upper bounds for the spectral norms. The interval certificate gives the sharper bounds e<=1.130567545287425e-11 and d/(1-e)<=2.687786027886388e-6. Since e<1, T has full rank. Put v=Tz. Then v^T G v>=(1-e)||z||_2^2 and |v^T(G_f-G)v|<=d||z||_2^2. Division proves(1). The exact binary whitening matrix, interval row bounds, complete source hashes and executable code are preserved beside this proof. The choice of T involves no assumption that floating Cholesky was exact.

## Floating observations, not certified operator bounds

The independent completed assembly at2026-10-28T15:44:22.390881+00:00 gives these first three generalized square-root eigenvalues of(B_f,G_f):

| Selected columns | Count | First three floating values |
|---|---:|---|
| m=1 |26|50.32008245,52.39138200,56.37934897|
| m=2 |26|25.47290134,53.06550877,57.65581698|
| m=3 |26|12.11424387,53.60055185,58.51279091|
| m=1,2 |52|3.455656563,4.247678609,5.460412731|
| m=1,2,3 |78|2.765547309,3.268491498,4.391313969|
| High-graph conforming subset, measured in low norms |60|2.864768631,3.408895982,4.616982941|

The normalized input Gram condition number for all78 columns is approximately6.3982e5. Restricting to the stored floating strain-zero hyperplane gives first values2.766194858,3.269534378,4.393297670. That hyperplane is defined by the stored binary strain row, not the exact strain functional. V202 separately bounds its entry errors. Using the exact input Gram midpoint instead gives2.765547692,3.268491837,4.391314476 with the same uncertified output matrix.

Against the separate52-column S1M3 run, the common input and output blocks change in relative Frobenius norm by3.5864668e-8 and1.7763071e-7. These are consistency diagnostics. They are not integration error bounds. The accepted input error(1) does not address the output division or quadrature errors, and the accumulation-only sensitivity model is not a total certificate. The observed additional decrease from the third angular mode therefore warrants continued finite-section investigation, without establishing any continuum singular value.

## Dependencies and verification evidence

Proof 198 supplies the exact input form and its independent original-data reconstructions. Topics176 and183 give the accounting and floating-matrix scope; proof 206 gives exact high conformity. The copied code is the exact original executed script and locates its work directory by relative paths. Re-execution uses the original work/m4p_audit/code/check.py, retained in this team, so that its source paths resolve as recorded. evidence/check.json binds all final parts, metadata, original trial, matrix and script hashes. There is no formal source and no Lean build.
