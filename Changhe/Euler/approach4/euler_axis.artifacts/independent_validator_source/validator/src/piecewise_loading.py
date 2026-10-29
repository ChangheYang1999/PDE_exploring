"""Select an independently implemented evaluator from explicit basis metadata."""
import json
import numpy as np
from piecewise_adapter import PiecewiseField
from piecewise_jacobi import JacobiPiecewiseField


def load_piecewise(path):
    with np.load(path,allow_pickle=False) as data:
        meta=json.loads(str(data['meta_json']))
    radial=meta['elements'][0].get('radial','cheb')
    if radial in ['cheb','chebyshev']:
        return PiecewiseField.load(path)
    if radial=='jacobi':
        return JacobiPiecewiseField.load(path)
    raise ValueError('Unsupported documented ball basis: '+str(radial))
