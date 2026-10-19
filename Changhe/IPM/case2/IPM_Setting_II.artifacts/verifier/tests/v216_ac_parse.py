"""V215: parse a numerics amplitude-continuation log (runs/pfwd/par/AC*.log, read only): for each solve, the defect of the
starting guess (it = 0), the smallest rms among accepted iterates, and the final record. Usage: python3 -B tests/v216_ac_parse.py LOG"""
import sys, json
first = best = None; amps = []
for l in open(sys.argv[1]):
    try: d = json.loads(l)
    except Exception: continue
    if d.get('state'): amps.append(d['tamp']); print('  stored amplitude', d['tamp']); continue
    if d.get('it') == 0 and 'kind' not in d and not d.get('final'):
        first = (d['defect_max'], d['defect_rms']); best = d['defect_rms']
    elif d.get('accepted') and 'defect_rms' in d and not d.get('final'):
        best = min(best, d['defect_rms'])
    if d.get('final'):
        print('start max %.4f rms %.3e | best accepted rms %.3e | final max %.4f rms %.3e | evaluations %s accepted %s | final/start rms %.2f'
              % (first[0], first[1], best, d['defect_max'], d['defect_rms'], d.get('evaluations'), d.get('accepted_steps'), d['defect_rms'] / first[1]))
