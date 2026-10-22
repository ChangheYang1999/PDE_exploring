# Source semantics and exact rank scope

The accepted frozen lin_assembly.py specifies the coordinate of an inner half-line piece as t-b and of an outer half-line piece as t-a. Its ExpPolyBasis evaluator implements these shifts directly. The extracted complete class in sources/ExpPolyBasis.txt is checked against the AST source span with its source hash in evidence/source_binding.json. The one-sided traces used in the theorem are therefore1 and alpha for a unit pure exponential. The stored endpoint convention does not change one-sided traces.

The four external constraints for B and B' are equivalent to matching h and its radial first derivative: h=r^3 B and h_r=r^2(3B+B'), so after the value jump vanishes the derivative jump is a positive multiple of the B' jump. This observation concerns external circles only. No internal joins are checked here.

The source's constraints function selects four external trace differences per angular mode and multiplies columns by a positive diagonal norm scaling. The trace differences have the exact unscaled rank proved here; every finite strictly positive diagonal scaling preserves it. We do not treat a floating SVD's thresholded rank as an exact rank certificate. The source's named external rows are distinct from the singular-vector combinations retained after truncation.
