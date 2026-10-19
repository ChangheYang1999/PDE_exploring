"""V224: for each solve in a numerics amplitude-continuation log (read only), the smallest rms and smallest maximum
defect over ALL iterate records after it = 0 (accepted or not), relative to the starting guess.
Usage: python3 -B tests/v224_ac_trials.py LOG"""
import sys, json
first = None; trials = []
def flush(tag):
    if first is None: return
    mr = min(t[1] for t in trials) if trials else float('nan')
    mm = min(t[0] for t in trials) if trials else float('nan')
    print('%-8s start %.4f / %.3e | n_trials %d | min trial rms %.3e (ratio %.2f) | min trial max %.4f (ratio %.2f)'
          % (tag, first[0], first[1], len(trials), mr, mr / first[1], mm, mm / first[0]))
for l in open(sys.argv[1]):
    try: d = json.loads(l)
    except Exception: continue
    if d.get('state'): flush(str(d['tamp'])); first = None; trials = []; continue
    if d.get('it') == 0 and 'kind' not in d and not d.get('final'):
        first = (d['defect_max'], d['defect_rms']); trials = []
    elif first is not None and 'defect_rms' in d and not d.get('final'):
        trials.append((d['defect_max'], d['defect_rms']))
