# Binding Gaussian correction

Read this with PROOF.md and AUDIT_CLARIFICATIONS.md. The original proof and first clarification hashes are preserved. This correction supersedes the Gaussian velocity in equation (9), the preceding sentence, and the corresponding sentence in team note138.

For the Gaussian potential V in proof 247, the coefficient of x^2 after multiplication by exp(-x^2) is

    (2g-g'')/2-g=-g''/2.

Consequently the canonical vertical velocity on x=0 is

    b(y)=partial_xx V(0,y)=-g''(y),
    w_g(y)=-g''(y)+(v(y)-u(y)/ell0)/nu,
    lambda_g=1/(ell0 nu).

Here v(y)=U2[zeta](0,y); the capital V denotes the two-dimensional Gaussian potential. Proof 241 calls that potential v, but it is a different function from the lower-case v in proof 247. With g(y)=-y^3 exp(-y^2)/6, the explicit corrected Gaussian trace is

    -g''(y)=(y-(7/3)y^3+(2/3)y^5)exp(-y^2).

The previous formula b=2g-g'' is false as a function of y. Its difference from the canonical trace is 2g, nonzero for every y other than zero. Both traces happen to have derivative 1 at zero, so the central strain check could not detect the error. Their contributions w f'-2w'f to the axis identity differ by 2g f'-4g'f; since f(y)=y+O(y^3), this difference has leading term (5/3)y^3 and is not identically zero. Thus the correction matters for the remaining Gaussian image estimate.

Equations (1) through (8), which keep b as the actual velocity trace, are unchanged. The facts c[d]=1, J[d]=0, zero cofactor and actual high-domain membership come from the correctly differentiated construction in proof 241 and are unchanged. No estimate of the full high norm, violation of(I) or(S), or inverse follows. The corrected topic remains pending the requested independent audit.
