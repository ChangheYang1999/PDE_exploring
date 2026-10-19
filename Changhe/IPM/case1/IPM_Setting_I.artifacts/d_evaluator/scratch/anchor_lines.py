# Print the line numbers of the C8 anchor phrases (scratch/prompt_map.md) in a report file.
# Usage: python3 scratch/anchor_lines.py FILE
import sys
A = [
 ("6/109 candidate", "The trial density is given by an explicit formula with stored coefficients"),
 ("6/109 candidate", "arranged in seven parts; the file INDEX.txt"),
 ("14 timing", "T0 = 2026-10-17T17:37:12Z"),
 ("14 timing", "T_end ="),
 ("14 timing", "Elapsed time ="),
 ("25 gate", "STATUS:"),
 ("25 gate", "waived as a gate by the"),
 ("62 strong vs weak", "(i) The posed strong setting (a smooth and even near 0) is not answered by this result"),
 ("104 gauge", "Harmonic gauge: excluded by (V3)"),
 ("104 jet", "x^2 y jet: a(0) = 1 by construction"),
 ("104 zero", "Zero state:"),
 ("104 U(0)", "U(0) = 0 by these parities"),
 ("104 gauge", "Gauge. The harmonic term lambda x y"),
 ("106 R", "Normalizations. R = W.grad rho - rho"),
 ("106 absolute", "Absolute values. The maxima of |R| itself"),
 ("106 E", "Elliptic equation."),
 ("106 E", "the elliptic residual E = -Lap psi - d_x rho"),
 ("106 axis", "Axis."),
 ("107 domains", "The domain columns hold c_l at the candidate's value"),
 ("108 manufactured", "Manufactured test of the separate evaluator"),
 ("108 parity", "Parity: by construction"),
 ("108 aliasing", "is the aliasing check"),
 ("108 conditioning", "least first-order cost of a unit"),
 ("108 conditioning", "column-scaling"),
 ("108 R8", "R8"),
 ("109 far-field model", "This is the far-field model."),
 ("109 finite box", "Finite-box artifacts:"),
 ("111 not a proof", "It is not a proof."),
 ("111 stable c_l", "The requirement of the standard that c_l be stable holds for the fitted values along each construction"),
 ("open", "[OPEN]"),
]
L = open(sys.argv[1]).read().split("\n")
heads = [(i + 1, l) for i, l in enumerate(L) if l.startswith("#")]
def sec(n):
    h = [l for i, l in heads if i <= n]
    return h[-1][:40] if h else "-"
# Search the text with line breaks and indentation collapsed to single spaces, so that phrases wrapped over two lines
# are found; a hit is reported at the line where it starts.
import re, bisect
J, starts = "", []
for l in L:
    starts.append(len(J)); J += re.sub(r"\s+", " ", l.strip()) + " "
def hits_of(a):
    a = re.sub(r"\s+", " ", a); out, k = [], J.find(a)
    while k >= 0:
        n = bisect.bisect_right(starts, k)
        if not out or out[-1] != n: out.append(n)
        k = J.find(a, k + 1)
    return out
for key, a in A:
    hits = hits_of(a)
    print("%-22s %-60s %s" % (key, a[:60], ", ".join("%d [%s]" % (n, sec(n)) for n in hits[:4]) + (" ..." if len(hits) > 4 else "") if hits else "NOT FOUND"))
