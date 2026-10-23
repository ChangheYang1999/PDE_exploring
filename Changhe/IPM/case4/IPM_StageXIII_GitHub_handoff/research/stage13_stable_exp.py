"""Private field namespaces with allocation-independent scalar-libm exp.

This helper changes no imported module or source file. The frozen field source
text executes in private namespaces; only those namespaces' explicit np.exp
primitive is replaced. All other operations and analytic expressions are the
original ones. Exact-byte caching changes cost only, never an argument/value.
"""
import builtins
from collections import OrderedDict
import importlib
import math
from pathlib import Path
import sys
import types

from absolute_common import ROOT,BASE,np,read,digest


class ScalarExpProxy:
    """NumPy delegation except fixed scalar math.exp, with bounded exact keys."""
    def __init__(self,maximum_arrays=256):
        self.maximum_arrays=int(maximum_arrays)
        if not 1<=self.maximum_arrays<=1024:raise ValueError('A bounded exact-input cache is required')
        self.cache=OrderedDict();self.calls=self.hits=self.misses=self.evictions=self.peak_entries=0
    def __getattr__(self,name):return self.exp if name=='exp' else getattr(np,name)
    def exp(self,value,*args,**kwargs):
        if args or kwargs:raise ValueError('Frozen field exp calls must have exactly one argument')
        value=np.asarray(value)
        if value.dtype!=np.dtype(float):raise ValueError('Expected native binary64 field exponent input')
        contiguous=np.ascontiguousarray(value);key=(value.dtype.str,value.shape,contiguous.tobytes())
        self.calls+=1
        if key in self.cache:
            self.hits+=1;result=self.cache.pop(key);self.cache[key]=result
        else:
            self.misses+=1
            result=np.fromiter((math.exp(float(v)) for v in contiguous.ravel()),dtype=float,count=value.size).reshape(value.shape)
            result.setflags(write=False);self.cache[key]=result
            if len(self.cache)>self.maximum_arrays:self.cache.popitem(last=False);self.evictions+=1
            self.peak_entries=max(self.peak_entries,len(self.cache))
        return result.copy()
    def metadata(self):
        return {'calls':self.calls,'hits':self.hits,'misses':self.misses,'evictions':self.evictions,
            'maximum_arrays':self.maximum_arrays,'peak_entries':self.peak_entries,'current_entries':len(self.cache),
            'retained_input_and_output_bytes':sum(len(k[2])+v.nbytes for k,v in self.cache.items()),
            'key':'Exact dtype string, shape, and complete binary64 input bytes',
            'cached_value_alias_returned':False,'interpolation_used':False,
            'scalar_primitive':'Python math.exp (native scalar libm)',
            'other_numpy_operations':'Delegated unchanged to original NumPy'}


def _private_module(path,name,redirects,proxy):
    """Execute exact saved text with private imports, never sys.modules edits."""
    module=types.ModuleType(name);module.__file__=str(path);module.__package__=''
    importer=builtins.__import__
    def private_import(import_name,globals=None,locals=None,fromlist=(),level=0):
        if not level and import_name in redirects:return redirects[import_name]
        return importer(import_name,globals,locals,fromlist,level)
    private_builtins=dict(vars(builtins));private_builtins['__import__']=private_import
    module.__dict__['__builtins__']=private_builtins
    original_path=sys.path[:]
    try:exec(compile(path.read_bytes(),str(path),'exec'),module.__dict__)
    finally:sys.path[:]=original_path
    module.np=proxy
    return module


def private_field_namespaces():
    """Return exact-source private spectral/core modules and arithmetic record."""
    freeze_path=ROOT/'provenance/stage13_numerical_sources_v2.json';freeze=read(freeze_path)
    base_path=ROOT/'provenance/base_manifest.json';base=read(base_path)
    if digest(base_path)!=freeze['base_manifest_sha256']:raise ValueError('Original frozen base manifest changed')
    names=('absolute_fields.py','stage13_model.py','stage13_model_v2.py','absolute_fields_v2.py','highprecision_origin.py')
    paths={name:ROOT/name for name in names};paths['base/spectral_basis.py']=BASE/'spectral_basis.py'
    expected={name:freeze['files'][name] for name in names}
    expected['base/spectral_basis.py']=base['spectral_basis.py']
    if any(digest(path)!=expected[name] for name,path in paths.items()):raise ValueError('Private namespace source changed')
    original_core=importlib.import_module('absolute_fields');original_spectral=importlib.import_module('spectral_basis')
    original_core_np=original_core.np;original_spectral_np=original_spectral.np;original_exp=np.exp
    proxy=ScalarExpProxy(256)
    spectral=_private_module(paths['base/spectral_basis.py'],'_ipm_stage13_v3_private_spectral',{},proxy)
    core=_private_module(paths['absolute_fields.py'],'_ipm_stage13_v3_private_core',{'spectral_basis':spectral},proxy)
    if original_core.np is not original_core_np or original_spectral.np is not original_spectral_np or np.exp is not original_exp:
        raise RuntimeError('Original independent namespaces changed during private loading')
    if core.evaluate_modes is not spectral.evaluate_modes or core._harmonics is not spectral._harmonics:
        raise RuntimeError('Private core did not bind the private spectral functions')
    return core,spectral,proxy,{'frozen_physical_source_sha256':expected,
        'original_v2_freeze_path':str(freeze_path),'original_v2_freeze_sha256':digest(freeze_path),
        'base_manifest_sha256':digest(base_path),'helper_sha256':digest(Path(__file__)),
        'compiled_source_text_modified':False,'sys_modules_modified':False,
        'replacement':'Only explicit np.exp in the two private field namespaces',
        'original_independent_stateless_namespaces_modified':False}
