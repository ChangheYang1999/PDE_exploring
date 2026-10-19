"""Summarize a homotopy log: per lambda stage, final c_l, weighted residual, compatibility defect, iterations."""
import sys, re
for fn in sys.argv[1:]:
    print("# " + fn)
    print("lambda   c_l        |res|      id=c_l-1/2-c   its  note")
    stage = None; last = None; its = 0; note = ""
    def flush():
        if stage is not None and last is not None:
            m = re.search(r"\|res\|=([0-9.e+-]+).*?cl=([0-9.e+-]+) id=([0-9.e+-]+)", last)
            print("%.3f    %.6f   %.3e   %9.2e   %3d  %s" % (stage, float(m.group(2)), float(m.group(1)), float(m.group(3)), its, note))
    for line in open(fn):
        if line.startswith("=== "):
            flush(); stage = float(re.search(r"lambda = ([0-9.]+)", line).group(1)); last = None; its = 0; note = ""
        elif line.startswith("it "):
            last = line; its += 1
        elif "no decrease" in line:
            note = "LM: no decrease"
    flush()
