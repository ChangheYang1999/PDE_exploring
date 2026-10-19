"""Validate GPUDerivative against the lead's CPU CentreDerivative on a shape file.
Usage: python3 test_gpu_op.py SHAPE.npz [nr nt] [fit_radius]"""
import sys, time, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "b_fit_domain"))
import numpy as np, torch
from centre_fit import load_shape, CentreDerivative
from gpu_op import GPUDerivative

path = sys.argv[1]
nr = int(sys.argv[2]) if len(sys.argv) > 2 else 2048
nt = int(sys.argv[3]) if len(sys.argv) > 3 else 480
fr = float(sys.argv[4]) if len(sys.argv) > 4 else None
t0 = time.time()
s, z = load_shape(path, nr, nt, fit_radius=fr)
f = s.fun(z)
print("loaded", path, "nr", nr, "nt", nt, "ncol", len(z), "nrow (incl. source and 2 centre rows)", len(f), "norm", np.linalg.norm(f), "t", time.time() - t0, flush=True)
t0 = time.time()
op = CentreDerivative(s, z)
print("CPU operator built", time.time() - t0, "s; shape", op.shape, flush=True)
t0 = time.time()
g = GPUDerivative(op)
torch.cuda.synchronize()
print("GPU operator built", time.time() - t0, "s", flush=True)
rng = np.random.default_rng(1)
for trial in range(2):
    v = rng.standard_normal(op.shape[1])
    u = rng.standard_normal(op.shape[0])
    t0 = time.time(); Av = op @ v; tc = time.time() - t0
    t0 = time.time(); ATu = op.rmatvec(u); tcr = time.time() - t0
    vt = torch.as_tensor(v, device="cuda"); ut = torch.as_tensor(u, device="cuda")
    torch.cuda.synchronize(); t0 = time.time(); Avg = g.matvec(vt); torch.cuda.synchronize(); tg = time.time() - t0
    t0 = time.time(); ATug = g.rmatvec(ut); torch.cuda.synchronize(); tgr = time.time() - t0
    Avg = Avg.cpu().numpy(); ATug = ATug.cpu().numpy()
    print("trial", trial, "matvec: rel err %.3e (CPU %.2fs, GPU %.3fs); rmatvec: rel err %.3e (CPU %.2fs, GPU %.3fs); adjoint <Av,u>-<v,ATu> rel: CPU %.3e GPU %.3e" % (
        np.linalg.norm(Avg - Av) / np.linalg.norm(Av), tc, tg, np.linalg.norm(ATug - ATu) / np.linalg.norm(ATu), tcr, tgr,
        abs(np.dot(Av, u) - np.dot(v, ATu)) / (np.linalg.norm(Av) * np.linalg.norm(u)),
        abs(np.dot(Avg, u) - np.dot(v, ATug)) / (np.linalg.norm(Avg) * np.linalg.norm(u))), flush=True)
    # component-wise worst
    i = np.argmax(np.abs(Avg - Av)); print("  worst matvec row", i, Av[i], Avg[i], "last three rows (source, E, D2): CPU", Av[-3:], "GPU", Avg[-3:])
    j = np.argmax(np.abs(ATug - ATu)); print("  worst rmatvec col", j, ATu[j], ATug[j], "k column: CPU", ATu[0], "GPU", ATug[0])
# timing of repeated GPU products
torch.cuda.synchronize(); t0 = time.time()
for _ in range(10):
    x = g.rmatvec(g.matvec(vt))
torch.cuda.synchronize(); print("GPU matvec+rmatvec: %.4f s per pair" % ((time.time() - t0) / 10))
print("GPU mem GB", torch.cuda.max_memory_allocated() / 1e9)
# pass/fail (referee request): relative errors below 1e-10 and adjoint identity below 1e-13
ok = (np.linalg.norm(Avg - Av) / np.linalg.norm(Av) < 1e-10 and np.linalg.norm(ATug - ATu) / np.linalg.norm(ATu) < 1e-10
      and abs(np.dot(Avg, u) - np.dot(v, ATug)) / (np.linalg.norm(Avg) * np.linalg.norm(u)) < 1e-13)
print("PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
