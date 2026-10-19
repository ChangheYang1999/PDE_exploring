"""Full analysis of a candidate file: diagnostics D1-D8 (diag.report), independent FD transport residual (check_fd),
axis export for the B_3 diagnostic (export_axis), and the self-consistent collocation residual on regions."""
import sys, os, numpy as np, torch
sys.path.insert(0, 'src')
import ipm1, diag, check_fd, export_axis
path = sys.argv[1]; tag = os.path.splitext(os.path.basename(path))[0]
m, b, cl, flds, st, ad = diag.report(path, device='cuda')
print("\n=== independent FD transport residual ===")
check_fd.check(path, K=600)
print("\n=== axis export ===")
try:
    export_axis.export(path, f'axis_{tag}.npz')
except Exception as ex:
    print("axis export failed:", ex)
