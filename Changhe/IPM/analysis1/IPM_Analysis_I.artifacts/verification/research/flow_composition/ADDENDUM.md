# Fixed mathematical centres and first review resolutions

This addendum is mandatory with PROOF.md. The original proof is retained.
The actual first response used claude-opus-5-5 and ended normally. It
accepted the conditional criterion and requested explicit input premises.

The exact angular nodes are [l*pi/51200,r*pi/51200]. Their expansion
centre is the fixed real number theta0=(l+r)*pi/102400, and their true
half-width is (r-l)*pi/102400. It is not the floating midpoint of an Arb
ball. Topic73 proved membership of the derivatives at this exact centre
and d>=the true half-width for every selected node here. Fresh source
coefficient arrays must equal that accepted archive byte for byte.
Therefore the review's suggested uncovered slivers do not occur under
these premises. An arbitrary point of the source centre ball is never
chosen as the mathematical Taylor centre. The source centre ball merely
encloses theta0 during evaluation.

The selected nodes are (0,1,7), (12800,12801,7), (25599,25600,7).
Their closed endpoints include both axes and an interior cell. Only
these three angular cells are used. The supplied coefficient and error
membership hypotheses are the conclusions of topic73 at these nodes.
Its finite trigonometric identities and derivative remainder proof are
inherited explicitly. In particular C=cos(theta)sin(2n theta)/sin(theta)
and S=sin(theta)sin(2n theta)/cos(theta) are understood through their
finite trigonometric-polynomial extensions at the axes. This criterion
never divides by a zero coordinate.

The radial coefficient and remainder premise is exactly topic93's
finite-input result for cells0,4102,7808. Canonical spline and Green data
membership is still OPEN and is not supplied by the present experiment.
The mu enclosure, h<1/522, scalar powers and exponential cell endpoints
are the accepted topic75 scalar premises, with byte equality checked for
the selected radial files. No unconditional physical flow verdict will
be issued from this result.

Rename the subinterval left endpoint in the Bernstein argument alpha;
the parameter a always means129/20. Let B_0,...,B_Q be the coefficients
on [0,2ell]. The left and right coefficients after subdivision are

 L_k=2^(-k) sum_(j=0)^k binom(k,j) B_j,
 R_k=2^(-(Q-k)) sum_(j=0)^(Q-k) binom(Q-k,j) B_(k+j).

Repeated midpoint interpolation proves these identities by Pascal's
identity: row p consists of 2^(-p) sum_(j=0)^p binom(p,j) B_(i+j).
For the underlying polynomial the coefficients are correct because
substituting z=w/2 into sum B_j binom(Q,j) z^j(1-z)^(Q-j), expanding
1-w/2=(1-w)+w/2, and collecting w^k(1-w)^(Q-k) yields L_k.
The substitution z=(1+w)/2 gives R_k in the same way, or by reflecting
z to1-z and reversing B. This is a direct proof of the subdivision
identity, independent of the translated power-coefficient construction.

The proof's E_fX uses the polynomial magnitude A_X only. The source
TMArr.sup also includes E_X, so its source remainder expression includes
one extra nonnegative E_f E_X. This makes that particular analytic
formula more conservative. The new reference calculation uses the
complete minimal triangle bound proved in PROOF.md. All actual source
floating operations remain untrusted until the final output comparison.

The new exact and iv programs must compute their own enclosures. They
must not call the source range code to obtain a reference bound. A failed
reference containment is OPEN for this sufficient criterion, not a
counterexample to the source output.
