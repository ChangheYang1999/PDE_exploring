# P337 general smooth endpoint theorem

CONFIRMED 2026-10-22T10:08:36.873373+00:00, conditional on actual C-infinity fields. For W=(xa,P), a,P even in x, a(0)=A>0, P_u(0)=-kappa<0, lambda>=0,2A-lambda>0, WTheta=lambdaTheta, the stated zero-axis/nonzero-axis-coefficient hypotheses imply n=(2A-lambda)/kappa is a positive integer and

    Theta=(C_u/2)x^2 Z^n,
    Z=(u-H(x))L, L>0, L(0)=1,
    H(x)=k x^2/(2A+kappa)+O(x^4), k=P_xx(0)/2,
    WZ=(lambda-2a)Z/n.

H is the unique smooth unstable graph germ; Z is the unique smooth normalized factor. The actual local zero set is precisely the axis and the graph; off them signTheta=sign(C_u)sign(u-H)^n. The axis coefficient is nonzero on both punctured sides and cannot be extended by zero. For even n, I=xZ^(n/2) is odd, Theta=(C_u/2)I^2 and WI=lambda I/2, a first integral only for lambda0.

For actual smooth B2 with beta>=2, A=2beta+kappa,lambda=beta-2,n=2+(3beta+2)/kappa. In signedu=y*-y, the report's unsigned incoming C must be converted to C_u=epsilon^n C, epsilon=sgn(y*) for the central component. There is no extra2. Other components use the occupied-side sign. Degenerate and opposite-sign endpoint linearizations are outside this theorem.

The proof uses a pinned fixed-ball C-infinity stable-manifold theorem and actual scalar ODE arguments, not formal realization or finite checks. The formal P331 hierarchy is not known to converge. The separate flat actual first integral demonstrates why nonzero-axis data are essential. No actual full-plane B2 solution is constructed; general B2 remains OPEN.

Final finite controls74/74 at2026-10-22T10:07:17.425824+00:00 to2026-10-22T10:07:18.360211+00:00, 0.934382s: five file-integrity checks,43 manufactured consistency/data checks,six predicates on eight sampled values,four single-perturbation negatives,eight orientation identity sanity checks,eight other exact/smoke checks. Only three manufactured fields claim constant divergence2beta; the fourth is a nonlinear local thermal manufacture. None verifies an actual full B2 profile. Initial incomplete SymPy run is retained. See verification/version_map.json and review_adjudication.md for exact versions and actual Opus5.5 reviews584/585/586.

Reading order: PROOF.md, verification/proof_freeze.json, verification/checks.json, verification/review_adjudication.md. Evaluator: code_independent/check_general_smooth_endpoint.py. Source dependency: research/334_smooth_temperature_factorization/sources/.
