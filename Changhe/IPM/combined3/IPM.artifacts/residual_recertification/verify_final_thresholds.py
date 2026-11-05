"""Pure-Python independent exact rational checks of final norm thresholds."""
import argparse,hashlib,json,sys
from fractions import Fraction as Q
from pathlib import Path
sys.set_int_max_str_digits(0)

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(args):
    path=Path(args.summary).resolve();data=json.loads(path.read_text())
    e=Q(data['Task_A']['energy_upper_exact'])
    e2=Q(data['Task_B']['E2_upper_exact']);e3=Q(data['Task_B']['E3_upper_exact'])
    assert min(e,e2,e3)>=0
    checks={
        'Task_A_required':e<Q('7.96121055107e-7')**2,
        'Task_A_stronger':e<Q('7.961207e-7')**2,
        'Task_A_display':e<Q('7.960467e-7')**2,
        'Task_B_required':e2**9*e3<Q('0.094')**20,
        'Task_B_display':e2**9*e3<Q('0.016684')**20,
        'actual_source_bindings_preserved':data['source_hashes']=={'base007':'ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21','phi013':'a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a'},
        'fixed_c_preserved':Q(data['fixed_c_exact'])==Q(4076476460239181,2251799813685248),
        'complete_panel_count':data['coverage']['finite_panels']==342 and len(data['panel_replay'])==342,
        'both_verdicts_pass':data['Task_A']['verdict']==data['Task_B']['verdict']=='PASS',
        'independent_of_historical_residual_evidence':data['historical_residual_evidence_used']is False,
    }
    assert all(checks.values())
    result={'status':'PASS_INDEPENDENT_EXACT_THRESHOLDS','input_summary_file':path.name,'input_summary_sha256':digest(path),'method':'Python fractions.Fraction only; no float, Arb, inherited residual bound or scalar producer import.','checks':checks,'L2_display_strict_upper_exact':str(Q('7.960467e-7')),'Q_display_strict_upper_exact':str(Q('.016684')),'L2_required_energy_slack_exact':str(Q('7.96121055107e-7')**2-e),'L2_stronger_energy_slack_exact':str(Q('7.961207e-7')**2-e),'Q_required_twentieth_power_slack_exact':str(Q('.094')**20-e2**9*e3),'code_sha256':digest(Path(__file__))}
    Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items()if 'slack'not in k},indent=2))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--summary',default=str(Path(__file__).resolve().parent/'validated_summary.json'));p.add_argument('--output',default=str(Path(__file__).resolve().parent/'independent_threshold_check.json'));run(p.parse_args())
