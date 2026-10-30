"""Numerical cross-check of an analytically evaluated integral, not its proof."""
from pathlib import Path
from datetime import datetime, timezone
import json
import mpmath as mp
from flint import arb, ctx
mp.mp.dps=60;ctx.prec=256
integral=16*mp.quad(lambda t:t*(mp.cot(t)-mp.sin(t)*mp.cos(t)),[0,mp.pi/4,mp.pi/2])
formula=2*mp.pi*(4*mp.log(2)-1)
kappa=((4*arb(2).log()-1)/(8*arb.pi())).sqrt()
out={'utc':datetime.now(timezone.utc).isoformat(),'integral_FLOAT':str(integral),'formula_FLOAT':str(formula),'absolute_difference_FLOAT':str(abs(integral-formula)),'kappa_arb':kappa.str(60),'status':'analytic formula proved in PROOF.md; quadrature is a numerical cross-check only'}
Path(__file__).resolve().parents[1].joinpath('verification/constant.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
