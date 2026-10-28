# Ill-conditioned coordinates do not identify a spurious small section value

## Statement

A small generalized singular value with a nearly cancelling coordinate vector in an ill-conditioned basis can be an exact singular value of the operator. Its disappearance after deleting one of those basis columns, and its persistence while changing the conditioning of the columns, do not prove it is a numerical artifact. This is a finite-dimensional counterexample to that inference. It is not a claim that any current IPM section value is exact.

## Complete counterexample

Give X=Y=R^2 the Euclidean norm. Fix any0<epsilon<1 and define A=diag(1,epsilon). For every delta>0 choose basis

 b1=(1,0), b2=(1,delta).

Its column matrix P is invertible, with determinant delta. The exact input and output Grams are

 G=P^T P=[[1,1],[1,1+delta^2]],
 B=P^T A^T A P=[[1,1],[1,1+epsilon^2 delta^2]].

For a real lambda, congruence gives

 det(B-lambda G)=delta^2(1-lambda)(epsilon^2-lambda).

Thus the two exact generalized square-root eigenvalues are epsilon and1, for every positive delta. The smallest is the exact operator minimum, not a coordinate error. Its coefficient vector(-1,1) represents the small physical vector delta e2, and its Rayleigh quotient is

 sqrt(((-1,1) B (-1,1)^T)/((-1,1) G (-1,1)^T))=epsilon.

After normalizing each basis column to Euclidean length1, the input Gram is

 [[1,(1+delta^2)^(-1/2)],[(1+delta^2)^(-1/2),1]].

Its smallest eigenvalue is1-(1+delta^2)^(-1/2), which tends to zero like delta^2/2. Therefore the coordinate basis can be made arbitrarily ill-conditioned while retaining the same genuine small operator singular value and the nearly cancelling weakest coordinate vector. Deleting b2 leaves the one-dimensional section spanned by b1, whose minimum is1. Every assertion follows from these exact matrices, so no numerical computation is needed.

## Consequence for interpretation

In the shifted-junction S1J1 run, the low input form, conditioning and output matrix play different roles. V277 certifies the complete input-form comparison. The output remains floating. Neither a near-null coordinate combination nor the rise after dropping outer columns decides whether the exact output quotient is small. A certified output evaluation of the physical direction, with division and integration errors, is needed to answer that question. The elementary example above shows why a coordinate-conditioning diagnosis cannot replace it.

The valid present observations are: the smallest computed value is about4.7481; the corresponding coordinate vector is concentrated in the shifted outer columns; the section without those columns has first computed value about50.3201; the output calculation is sensitive under the stated accumulation model. These observations motivate a better conditioned basis and a certified output calculation. They prove neither a continuum small singular value nor that the apparent one is spurious.

The current numerical report additionally lists four first values below50, namely about4.7481,15.1419,34.287 and44.210. Hence its sentence 'the only value below50' is inconsistent with its own table. Its model interval printed as[3.74,5.58] does not contain the same log's printed model upper endpoint5.5835. If quoting two-decimal endpoints, use an upper endpoint at least5.59, and retain the accumulation-model qualification. None is a rigorous interval for the exact output operator.

This counterexample is independent of all IPM operator assumptions. The application uses only the completed-run accounting and floating scope of proof 242 and the frozen numerical files in evidence. No theorem or certificate for an IPM inverse, high norm or complement is asserted.
