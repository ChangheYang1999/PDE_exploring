"""Origin20 exact-cl cache with private deterministic scalar-exp field basis.

The inherited residual, all186 raw derivatives, center chart and origin20
Taylor algebra are unchanged. The exact frozen cache-building method executes
with a private global dictionary referring to private field namespaces. The
independent old stateless functions and every old module remain untouched.
"""
import types
from pathlib import Path
import absolute_fields as _old_fields
import spectral_basis as _old_spectral
import absolute_fields_v2 as _old_fields_v2
import absolute_model as _old_absolute_model
import absolute_model_v2 as _old_absolute_model_v2
import stage13_model as _old_model
from stage13_model_v2 import CachedAbsoluteProblem as CachedV2
from absolute_common import np,digest
from stage13_stable_exp import private_field_namespaces


_CORE,_SPECTRAL,_EXP,_ARITHMETIC=private_field_namespaces()
# Capture actual objects, not just names/hashes. Every public evaluation checks
# that the old independent namespace and original NumPy primitive still agree.
_SENTINELS=(
    ('numpy.exp',np,'exp',np.exp),
    ('absolute_fields.np',_old_fields,'np',_old_fields.np),
    ('absolute_fields.core_matrices',_old_fields,'core_matrices',_old_fields.core_matrices),
    ('absolute_fields.fields',_old_fields,'fields',_old_fields.fields),
    ('absolute_fields.residual',_old_fields,'residual',_old_fields.residual),
    ('absolute_fields._harmonics',_old_fields,'_harmonics',_old_fields._harmonics),
    ('absolute_fields.evaluate_modes',_old_fields,'evaluate_modes',_old_fields.evaluate_modes),
    ('spectral_basis.np',_old_spectral,'np',_old_spectral.np),
    ('spectral_basis.evaluate_modes',_old_spectral,'evaluate_modes',_old_spectral.evaluate_modes),
    ('spectral_basis._harmonics',_old_spectral,'_harmonics',_old_spectral._harmonics),
    ('absolute_fields_v2.np',_old_fields_v2,'np',_old_fields_v2.np),
    ('absolute_fields_v2.fields',_old_fields_v2,'fields',_old_fields_v2.fields),
    ('absolute_fields_v2.residual',_old_fields_v2,'residual',_old_fields_v2.residual),
    ('absolute_model.physical_residual',_old_absolute_model,'physical_residual',_old_absolute_model.physical_residual),
    ('absolute_model_v2.physical_residual',_old_absolute_model_v2,'physical_residual',_old_absolute_model_v2.physical_residual),
    ('stage13_model.core_matrices',_old_model,'core_matrices',_old_model.core_matrices),
    ('stage13_model.evaluate_modes',_old_model,'evaluate_modes',_old_model.evaluate_modes),
    ('stage13_model.CachedAbsoluteProblem._ensure_basis',_old_model.CachedAbsoluteProblem,'_ensure_basis',_old_model.CachedAbsoluteProblem._ensure_basis),
)


def original_namespace_identity_record():
    rows={name:getattr(owner,key) is expected for name,owner,key,expected in _SENTINELS}
    rows['original_core_function_numpy_is_original']=_old_fields.core_matrices.__globals__['np'] is np
    rows['original_spectral_function_numpy_is_original']=_old_spectral.evaluate_modes.__globals__['np'] is np
    rows['private_core_function_numpy_is_private_proxy']=_CORE.core_matrices.__globals__['np'] is _EXP
    rows['private_spectral_function_numpy_is_private_proxy']=_SPECTRAL.evaluate_modes.__globals__['np'] is _EXP
    return {'passed':all(rows.values()),'identities':rows,
        'old_independent_stateless_modified':False,'global_numpy_exp_replaced':False}


def _assert_original_namespaces():
    record=original_namespace_identity_record()
    if not record['passed']:raise RuntimeError('Original/private field namespace identity changed: '+str(record))


_original_ensure=_old_model.CachedAbsoluteProblem._ensure_basis
_private_globals=dict(_original_ensure.__globals__)
_private_globals.update(core_matrices=_CORE.core_matrices,evaluate_modes=_SPECTRAL.evaluate_modes)
_private_ensure=types.FunctionType(_original_ensure.__code__,_private_globals,
    _original_ensure.__name__,_original_ensure.__defaults__,_original_ensure.__closure__)
_private_ensure.__kwdefaults__=_original_ensure.__kwdefaults__
_private_ensure.__doc__=_original_ensure.__doc__


class CachedAbsoluteProblem(CachedV2):
    version='stage13_exact_last_cl_field_cache_v3_origin20_private_scalar_exp'
    _ensure_basis=_private_ensure

    def __init__(self,*args,**kwargs):
        _assert_original_namespaces()
        super().__init__(*args,**kwargs)
        self.namespace_identity_checks=1
        _assert_original_namespaces()

    def fun(self,p=None,extra=None):
        _assert_original_namespaces()
        try:return super().fun(p,extra)
        finally:
            _assert_original_namespaces();self.namespace_identity_checks+=1

    def jacobian(self,p=None,extra=None):
        _assert_original_namespaces()
        try:return super().jacobian(p,extra)
        finally:
            _assert_original_namespaces();self.namespace_identity_checks+=1

    def cache_record(self):
        _assert_original_namespaces()
        result=super().cache_record()
        result.update(arithmetic_provider=_ARITHMETIC,scalar_exp_cache=_EXP.metadata(),
            original_namespace_identity=original_namespace_identity_record(),
            namespace_identity_checks=self.namespace_identity_checks,
            cache_builder_code_object_is_original=_private_ensure.__code__ is _original_ensure.__code__,
            residual_and_full_raw_derivative_inherited_unchanged=True,
            model_provider_sha256=digest(Path(__file__)))
        return result
