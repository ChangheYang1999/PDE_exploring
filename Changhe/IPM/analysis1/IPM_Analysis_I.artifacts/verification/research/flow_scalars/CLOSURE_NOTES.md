# Final scope and responses to the second review

The second actual Opus 5.5 review returned ACCEPT_STATED_SCALAR_SCOPE. Its
mathematical acceptance is recorded together with the following corrections.
The initial proof and run-bound addendum remain unchanged so that all prior
hash bindings remain verifiable. This note supersedes their initial status
and clarifies the wording; the final machine-readable verdict is authoritative.

1. The first review found the mathematical core sound but withheld acceptance
   until the omitted source and provenance obligations were supplied. Our
   earlier phrase "accepted the mathematical criterion" referred to that core,
   not to acceptance of the whole result. The omitted source and obligations
   were supplied and passed before the second review.
2. The rational grid is defined by the displayed formulas. The generator,
   stored hsub, array counts and endpoints support its consistency with source;
   exact point containment and abutment establish the geometry. No historical
   argv is inferred.
3. All three computations passed: checks.json, saved_audit.json and
   metadata_audit.json. Their exact hashes are bound in the final verdict.
   The producer's OPEN status at proof-writing time is a historical statement.
4. review_counts.json is NOT byte-identical to checks.json. It is the exact
   JSON object obtained by deleting only the constants field, as the creating
   command stated. The complete checks.json is preserved. The fresh audit
   explicitly binds its SHA256
   3f3eb9bb76a4ab31670473b03398c8bc37ae4863cc75da327abb5b958aa3cb2e.
   The finalizer compares the projection for equality and independently checks
   the complete 444-name constant set and its target rationals. We reject the
   review's suggestion to claim byte identity between distinct files.
5. Source expressions m +/- r and 1+h+h*h are evaluated in the installed
   binary64 round-to-nearest runtime, with explicit nextafter operations where
   displayed. The exact finite containment tests establish soundness even
   without assuming a general error bound for every reconstruction primitive.
6. Explicitly excluded are the tm_exp tolerance 1+1e-12, all cell_bounds and
   AngCache scalars outside this topic's list, and the use of the local Taylor
   variable in the full models. We do not adopt the review's extra assertion
   that this variable is necessarily anchored at the exported midpoint:
   the source coefficients and exponentials are balls intended to contain
   values at exact partition points. Establishing their intended common
   anchoring belongs to the full radial-model audit. The current proof uses
   the exact partition point for its mathematical cell and checks only the
   listed scalar inputs and radial geometry. It leaves full model anchoring
   OPEN rather than replacing it by an unproved midpoint assertion.

The accepted claim remains the finite scalar theorem and the geometry of
all 19389 finite cells. It does not establish a flow inequality or a full
Taylor-model certificate.
