"""Stage XII nondegenerate C5 chart without an imposed amplitude sign.

The frozen Stage XI class, N/E maps, Newton correctors and all five equalities
remain unchanged. This subclass overrides only point qualification, replacing
its inherited a0 > 1e-12 restriction by the symmetric |a0| > 1e-12 numerical
nondegeneracy check. It does not search a separate branch or alter the PDE.
"""
import json
from pathlib import Path
import numpy as np
from coefficient_normal_chart import CoefficientNormalChart
from c5_chart import hp_report

POLICY_VERSION='stage12_absolute_a0_nondegeneracy_v1'


class Stage12CoefficientNormalChart(CoefficientNormalChart):
    """Same exact local chart, with sign-neutral nondegeneracy qualification."""
    policy_version=POLICY_VERSION

    def _verify(self,p):
        self._bounds(p)
        report=hp_report(p)
        if (report['max_abs']>=self.tolerance or report['center_abs']>=self.tolerance
                or report['poisson_max_abs']>=self.tolerance or abs(report['a0'])<=1e-12
                or not report['physical_bounds']):
            raise ValueError('local C5 point fails unchanged HP, center, Poisson, bounds or absolute-a0 nondegeneracy conditions')
        return report


def chart(p,record=None):
    if record is None:
        path=Path(__file__).resolve().parent/'results'/'chart_coefficient_normal.json'
        record=json.loads(path.read_text())
    return Stage12CoefficientNormalChart(record,base=np.asarray(p))
