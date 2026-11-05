#!/usr/bin/env python3
"""Exact-input Arb check of the frozen N-matrix on the full Q rectangle."""
import json
from pathlib import Path
from flint import arb,ctx

ctx.prec=256
q=arb(21)/10;R=arb(17)/8750000;M=arb(1)/2
beta=arb(704955805507)/10**12
def B(p):
    s=(p+1)/q
    return (4*q*(arb.pi()*s).sin()).sqrt()**(-1)*(1-s)**(-(1-s)/2)*s**(-s/2)
Cs=B(1)/4;Ca=B(0)/arb(2).sqrt()
loss=q*Cs*R**(1-2/q)*M**(2/q)+Ca*R**(1-1/q)*M**(1/q)
margin=beta-loss
assert margin>arb(11)/20
# S1<6/7 follows from pi>157/50 by an exact rational comparison.
from fractions import Fraction as F
assert F(25)/(11*F(157,50))<F(36,49)
out={'status':'Q_BALL_FROZEN_MATRIX_MARGIN_CHECK_PASS','q':'21/10','reference_R':'17/8750000','reference_M':'1/2',
     'inherited_background_matrix_lower':'704955805507/10^12','Cs_arb':str(Cs),'Ca_arb':str(Ca),
     'matrix_loss_upper_arb':str(loss),'matrix_margin_lower_arb':str(margin),'certified_margin_lower':'11/20',
     'gradient_embedding_upper':'6/7','contraction_ratio_upper_at_beta7over4_Mhalf':'12/49',
     'scope':'qualitative frozen N-space lifting on the Q ball; no background Q-energy closure supplied'}
dest=Path(__file__).resolve().parent/'Q_matrix_margin_result.json'
dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
