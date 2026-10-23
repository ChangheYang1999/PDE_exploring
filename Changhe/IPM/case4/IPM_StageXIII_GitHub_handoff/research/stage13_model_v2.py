"""Exact cached field provider with consistently order20 origin residual jets.

The v1 direct-radius cache and its complete cl chain are inherited unchanged.
This explicit version only replaces the small-radius residual and ALL raw
derivatives with the same potential's higher-order independent Taylor algebra.
The old provider and every old result remain untouched.
"""
from stage13_model import CachedAbsoluteProblem as CachedV1,np
from highprecision_origin import residual_series,evaluate_series
from absolute_fields_v2 import ORIGIN_ORDER


class CachedAbsoluteProblem(CachedV1):
    version='stage13_exact_last_cl_field_cache_v2_origin20'
    origin_order=ORIGIN_ORDER

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self._origin_value_key=None;self._origin_derivative_key=None

    def _evaluate(self,p,extra,key,derivatives):
        if key!=self._evaluation_key:
            self._origin_value_key=None;self._origin_derivative_key=None
        result,jacobian=super()._evaluate(p,extra,key,derivatives)
        if np.any(self.small):
            need_value=self._origin_value_key!=key
            need_derivative=derivatives and self._origin_derivative_key!=key
            if need_value or need_derivative:
                series=residual_series(self._prepared,order=ORIGIN_ORDER,derivatives=bool(need_derivative))
                if need_value:
                    result[self.small]=self.root[self.small]*evaluate_series(series['residual'],self.x[self.small],self.y[self.small])
                    self._origin_value_key=key
                if need_derivative:
                    for column,poly in enumerate(series['derivatives']):
                        jacobian[self.small,column]=self.root[self.small]*evaluate_series(poly,self.x[self.small],self.y[self.small])
                    self._origin_derivative_key=key
        return result,jacobian

    def cache_record(self):
        result=super().cache_record()
        result.update(production_origin_residual_order=ORIGIN_ORDER,
            production_origin_all_raw_derivative_order=ORIGIN_ORDER,
            physical_model_or_objective_changed=False,original_provider_edited=False)
        return result

    def clear_cache(self):
        super().clear_cache();self._origin_value_key=None;self._origin_derivative_key=None
