"""Finite-grid minimax approximation, with a denser independent grid check."""
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
            "NUMEXPR_NUM_THREADS"):
    os.environ[key] = "1"
import resource
resource.setrlimit(resource.RLIMIT_AS, (1900*1024**2, 1900*1024**2))
import warnings, json
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
root = Path(__file__).parent
z = np.load(root/"endpoint_32768.npz")
th, e = z["theta"], z["e"]
N = len(th); k = 0.17936053129375418
v = np.abs(np.cos(th))**(4+2*k/(2-k))*np.sin(th)**2
eh = np.fft.rfft(e); vh = np.fft.rfft(v)
eh[401:] = 0; vh[401:] = 0
e_low = np.fft.irfft(eh, n=N)
v_tail = v-np.fft.irfft(vh, n=N)
v_scale = np.max(np.abs(v_tail))
target = (e-e_low)/1e-5
v_tail /= v_scale
idx = np.arange(0, N//4+1, 2)
mm = np.arange(201)
rows = []
for special,weighted in [(False,False),(True,False),(False,True)]:
    basis = np.cos(2*np.outer(th[idx],mm))
    if special:
        basis = np.column_stack([basis, v_tail[idx]])
    weights = np.where(th[idx]>1.4, 1., 10.) if weighted else np.ones(len(idx))
    ub = np.vstack([np.column_stack([basis,-weights]),
                    np.column_stack([-basis,-weights])])
    rhs = np.r_[target[idx],-target[idx]]
    objective = np.zeros(basis.shape[1]+1); objective[-1] = 1
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        sol = linprog(objective, A_ub=ub, b_ub=rhs,
                      bounds=[(None,None)]*basis.shape[1]+[(0,None)],
                      method="highs-ds", options={"threads":1})
    print("solved",special,sol.success,sol.message,flush=True)
    fit = e_low.copy()
    for m,b in enumerate(sol.x[:201]):
        fit += 1e-5*b*np.cos(2*m*th)
    if special: fit += 1e-5*sol.x[201]*v_tail
    er = np.abs(e-fit)
    row=dict(singular=special, weighted=weighted, discrete_minimax=float(sol.fun*1e-5),
             verified_grid_max=float(er[:N//4+1].max()),
             axisband_max=float(er[(th>1.4)&(th<=np.pi/2)].max()),
             at=float(th[:N//4+1][er[:N//4+1].argmax()]),
             singular_coefficient=float(1e-5*sol.x[201]/v_scale) if special else 0)
    rows.append(row)
    print(json.dumps(row),flush=True)
(root/"approximation.json").write_text(json.dumps(rows,indent=2))
