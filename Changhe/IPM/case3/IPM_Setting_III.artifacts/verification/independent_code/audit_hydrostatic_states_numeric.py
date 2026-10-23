"""Numeric-array adapter for the unchanged result187 field evaluator."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
import numpy as np
import torch
import audit_hydrostatic_states
with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):
    audit_hydrostatic_states.main()
