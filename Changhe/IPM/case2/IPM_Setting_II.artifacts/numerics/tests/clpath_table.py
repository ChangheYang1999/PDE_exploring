"""Summarize a c_l-continuation log: per prescribed c_l, final lambda, weighted residual, compatibility defect, iterations."""
import sys, re
for fn in sys.argv[1:]:
    print("# " + fn)
    print("c_l      lambda     |res|      id         its")
    stage = None; last = None; its = 0
    def flush():
        if stage is not None and last is not None:
            m = re.search(r"\|res\|=([0-9.e+-]+).*?LAMBDA=([0-9.e+-]+).*?id=([0-9.e+-]+)", last)
            if m: print("%.4f   %.5f   %.3e  %9.2e  %3d" % (stage, float(m.group(2)), float(m.group(1)), float(m.group(3)), its))
    for line in open(fn):
        if line.startswith("=== c_l continuation"):
            flush(); stage = float(re.search(r"c_l = ([0-9.]+)", line).group(1)); last = None; its = 0
        elif line.startswith("it "):
            last = line; its += 1
    flush()
