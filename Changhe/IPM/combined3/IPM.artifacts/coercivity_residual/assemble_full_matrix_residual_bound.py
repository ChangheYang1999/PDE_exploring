"""Combine genuine Riesz-source coordinates and full-matrix test Grams.

All inherited matrix/source hypotheses are explicitly retained. The output is
an upper bound of the entire full-plane inverse-matrix residual functional,
obtained by a rigorous rank-one positive-operator comparison.
"""
import argparse,json
from fractions import Fraction
from datetime import datetime,timezone
from hashlib import sha256
from pathlib import Path
from flint import arb,fmpq as Q,ctx


def aq(x):
    x=Fraction(str(x));return arb(x.numerator)/x.denominator


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--source-coordinate',type=Path,required=True)
    ap.add_argument('--matrix-gram',type=Path,required=True);ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--source-norm-upper',default='0.0055545729030073655758');args=ap.parse_args();ctx.prec=384
    source=json.loads(args.source_coordinate.read_text());matrix=json.loads(args.matrix_gram.read_text())
    assert source['status']in ['CERTIFIED_SOURCE_PROJECTION','CERTIFIED_ANGULAR_SOURCE_PROJECTION']
    assert matrix['status']in ['CERTIFIED_FULL_MATRIX_TEST_DUAL','CERTIFIED_FULL_MATRIX_ANGULAR_TEST_DUAL']
    assert source['configuration']['source_hashes']==matrix['configuration']['source_hashes']
    assert source['configuration']['width']==matrix['configuration']['width']
    if 'm'in source['configuration']:assert source['configuration']['m']==matrix['configuration']['m']
    c=arb(source['c_interval']);c_lower=c.abs_lower();assert c_lower>0
    B=arb(matrix['B_interval']).upper();n=aq(args.source_norm_upper)
    beta_star=aq('704955805507/1000000000000');old=(n*n/beta_star).upper();values={}
    for text,row in matrix['by_beta'].items():
        beta=aq(text);Gamma=arb(row['Gamma_full_upper']).upper()
        assert 0<beta<beta_star and Gamma>0 and B>0
        d2=(n*n/beta-c_lower*c_lower/(beta*beta*(Gamma+B/beta))).upper();assert d2>0
        d=d2.sqrt().upper();effective=(beta*d2).sqrt().upper()
        assert d.is_finite()and effective.is_finite()
        values[text]={'Gamma_upper':Gamma.str(80),'B_upper':B.str(80),
            'full_matrix_d_squared_upper':d2.str(80),'full_matrix_d_upper':d.str(80),
            'effective_source_sqrt_beta_d_upper':effective.str(80),
            'upper_bound_ratio_to_inherited_scalar_bound':(d2/old).str(80),
            'strictly_improves_inherited_scalar_upper':bool(d2<old)}
    result={'status':'FULL_MATRIX_RIESZ_RESIDUAL_UPPER_BOUND_WITH_EXPLICIT_INHERITED_PREMISES',
        'inputs':{str(path):sha256(path.read_bytes()).hexdigest()for path in [args.source_coordinate,args.matrix_gram]},
        'source_hashes':source['configuration']['source_hashes'],
        'inherited_source_norm_upper':args.source_norm_upper,'inherited_pointwise_matrix_lower':'704955805507/1000000000000',
        'inherited_premises':['The combined2 actual whole-plane ||J^2.1(WF)||₂ upper and its accepted source identities/arithmetic/remainders.',
            'The combined2 actual pointwise M>=beta_star I and its accepted complete-source/analytic/balanced-root hypotheses.'],
        'source_coordinate_interval':c.str(80),'absolute_coordinate_lower':c_lower.str(80),
        'inherited_scalar_d_squared_upper':old.str(80),'by_beta':values,
        'identity':'d²<=n²/beta-|c|²/[beta²*(Gamma+B/beta)], Gamma>=<Phi,(M-betaI)^-1Phi>, c=<RH,Phi>',
        'scope':'A genuine full-plane matrix-weighted Riesz residual upper. Inherited premises are not newly discharged here; high-order coercivity, invariant ball and existence remain separate.',
        'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'finished_utc':datetime.now(timezone.utc).isoformat()}
    args.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2),flush=True)

if __name__=='__main__':main()
