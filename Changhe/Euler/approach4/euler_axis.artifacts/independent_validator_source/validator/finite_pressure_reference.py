"""Compare finite supplied pressure values without hiding missing references."""
import numpy as np

def compare_pressure_reference(reconstructed_pressure,reconstructed_gradient,samples):
    p=np.asarray(reconstructed_pressure,dtype=float);g=np.asarray(reconstructed_gradient,dtype=float);ref=np.asarray(samples['P'],dtype=float)
    if p.ndim!=1 or p.shape!=ref.shape or g.shape!=p.shape+(2,):raise ValueError('Pressure shapes differ')
    if not np.isfinite(p).all()or not np.isfinite(g).all():raise ValueError('Independent reconstruction contains a nonfinite value')
    for key in ['r','z','R','mu']:
        if np.asarray(samples[key]).shape!=p.shape or not np.isfinite(samples[key]).all():raise ValueError('Invalid sample coordinates')
    valid=np.isfinite(ref);indices=np.flatnonzero(valid)
    if not len(indices):raise ValueError('No finite supplied pressure reference')
    error=p[valid]-ref[valid];worst=int(indices[np.argmax(abs(error))])
    return dict(count=int(p.size),finite_reference_count=int(valid.sum()),unavailable_reference_count=int((~valid).sum()),unavailable_reference_indices=np.flatnonzero(~valid).tolist(),unavailable_reference_R=np.asarray(samples['R'])[~valid].tolist(),reference_nan_count=int(np.isnan(ref).sum()),reference_positive_infinity_count=int(np.isposinf(ref).sum()),reference_negative_infinity_count=int(np.isneginf(ref).sum()),finite_reference_mask=valid.tolist(),max_abs_error=float(np.max(abs(error))),rms_error=float(np.sqrt(np.mean(error**2))),max_reference_scale=float(np.max(abs(p[valid]))),worst_index=worst,worst_point_r_z=[float(samples['r'][worst]),float(samples['z'][worst])],reconstructed_worst=float(p[worst]),exported_worst=float(ref[worst]),scope='Pressure comparison restricted to explicitly identified finite supplied references. Every reconstructed value is required finite. No value is imputed for an unavailable reference, and the omitted points do not contribute zero error.')
