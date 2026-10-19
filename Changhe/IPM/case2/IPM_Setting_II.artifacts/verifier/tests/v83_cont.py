"""V83 (lead team notes 08:03Z item 3): continuation of the p = 0.35 family along m1 = 1/2 with the c13 compensator
(log A += c (sin th + sin 3th), x = (0.24474 + c, a_2, -0.20666 + c, 0.122, 0.107, -0.027); c = 0.07 is the V74 / V79 family).
Own solver (tests/fs_run.py), 512 angles, r_min e^-14, smode, x-even projection, 30 iterations per solve. Per a_2: at most three
solves, c from a secant on m1 (first step with slope dm1/dc = 0.4, the numerics' value at a_2 = -1.0, or the last secant slope),
accepted when |m1 - 1/2| <= 0.0015. Every solve gets v64_m1, v68_div, v74_axis_speed and v83_point. Stop when the accepted
point has min |V|/r < 0.05 in 80-100 deg (an extra zero of V), when a solve fails, or when err_fullT > 0.05.
First waits for the V79a fs_run of a_2 = -1.3 (c = 0.07, PID given as argv[1]; the V79a chain bash was stopped) and runs its
diagnostics. Log runs/v83.log (POINT / CURVE lines)."""
import os, sys, json, time, subprocess, math
os.chdir('.')
LOG = 'runs/v83.log'
def log(s):
    with open(LOG, 'a') as f: f.write(time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()) + ' ' + s + '\n')
def run(cmd, out, tmo):
    with open(out, 'w') as f:
        subprocess.run(['timeout', str(tmo)] + cmd, stdout=f, stderr=subprocess.STDOUT)
def diag(O):
    run(['python3', 'tests/v64_m1.py', O + '.npz'], O + '_m1.log', 580)
    run(['python3', 'tests/v68_div.py', O + '.npz'], O + '_div68.log', 900)
    run(['python3', 'scratch/v74_axis_speed.py', O + '.npz'], O + '_axis.log', 580)
    run(['python3', 'tests/v83_point.py', O], O + '_point.log', 580)
    pt = None
    for l in open(O + '_point.log'):
        if l.startswith('POINT '): pt = json.loads(l[6:])
    log('POINT ' + json.dumps(pt))
    return pt
def X(a2, c):
    return '%.5f:%s:%.5f:0.122:0.107:-0.027' % (0.24474 + c, a2, -0.20666 + c)
def solve(a2, c, init):
    O = 'runs/v83_a2%s_c%.4f' % (a2, c)
    log('solve a2=%s c=%.4f init=%s' % (a2, c, init))
    run(['python3', 'tests/fs_run.py', 'p=0.35', 'kind=expf', 'par=' + X(a2, c), 'init=' + init, 'nt=512', 'tmin=-14',
         'tmax=10', 'nstep=800', 'iters=30', 'smode=1', 'hs=0.03', 'xsym=1', 'out=' + O + '.npz'], O + '.log', 3000)
    if not os.path.exists(O + '.npz'):
        log('no state written for ' + O); return None
    pt = diag(O)
    if pt is None or 'm1' not in pt: return None
    pt['c'] = c; pt['O'] = O
    return pt
log('start; waiting for PID %s' % sys.argv[1])
while os.path.exists('/proc/%s' % sys.argv[1]): time.sleep(30)
p13 = None
if os.path.exists('runs/v79_a2-1.3_c07_x.npz'):
    p13 = diag('runs/v79_a2-1.3_c07_x')
    if p13 is not None and 'm1' in p13: p13['c'] = 0.07; p13['O'] = 'runs/v79_a2-1.3_c07_x'
    else: p13 = None
    with open('runs/v79a.log', 'a') as f:
        f.write(time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()) + ' chain bash stopped after -1.3 (replaced by V83, m1 = 1/2 '
                'continuation); -1.3 diagnostics run by tests/v83_cont.py\n')
known0 = {'-1.3': [p13] if p13 else []}
curve = []; slope = 0.4; prev_state = 'runs/v79_a2-1.25_c07_x.npz'
for a2 in ['-1.228', '-1.3', '-1.4', '-1.5', '-1.6', '-1.7', '-1.8', '-1.9', '-2.0']:
    known = list(known0.get(a2, []))
    if not known:
        if len(curve) >= 2:
            (aa, ca), (ab, cb) = [(float(q['a2']), q['c']) for q in curve[-2:]]
            c = cb + (cb - ca)/(ab - aa)*(float(a2) - ab)
        elif curve:
            c = curve[-1]['c']
        else:
            c = 0.07
        c = round(c, 4)
        pt = solve(a2, c, prev_state)
        if pt is None: log('stop: solve failed at a2=%s' % a2); break
        known.append(pt)
    while len(known) < 3 and min(abs(q['m1'] - 0.5) for q in known) > 0.0015:
        ks = sorted(known, key=lambda q: abs(q['m1'] - 0.5))
        if len(ks) >= 2 and abs(ks[0]['m1'] - ks[1]['m1']) > 2e-4:
            s = (ks[0]['m1'] - ks[1]['m1'])/(ks[0]['c'] - ks[1]['c'])
            if 0.05 < s < 3: slope = s
        c = ks[0]['c'] + max(-0.08, min(0.08, (0.5 - ks[0]['m1'])/slope))
        c = round(c, 4)
        pt = solve(a2, c, ks[0]['O'] + '.npz')
        if pt is None: break
        known.append(pt)
    if not known: break
    ks = sorted(known, key=lambda q: abs(q['m1'] - 0.5)); best = ks[0]
    cv = dict(a2=a2, c=best['c'], m1=best['m1'], err_fullT=best.get('err_fullT'), D_div=best.get('D_div_fd1'),
              D_dir=best.get('D_dir_fd1'), spread_upper=best.get('spread_upper_div/dir'),
              spread_lower=best.get('spread_lower_div/dir'), win_upper_minV=best['upper min|V|/r'],
              win_upper_minalpha=best['upper min alpha'], nsolve=len(known), O=best['O'])
    if len(ks) >= 2 and abs(ks[0]['m1'] - ks[1]['m1']) > 2e-4 and 'D_div_fd1' in ks[1]:
        w = (0.5 - ks[0]['m1'])/(ks[1]['m1'] - ks[0]['m1'])
        cv['interp_to_m1_half'] = dict(c=round(ks[0]['c'] + w*(ks[1]['c'] - ks[0]['c']), 4),
                                       D_div=round(ks[0]['D_div_fd1'] + w*(ks[1]['D_div_fd1'] - ks[0]['D_div_fd1']), 4),
                                       D_dir=round(ks[0]['D_dir_fd1'] + w*(ks[1]['D_dir_fd1'] - ks[0]['D_dir_fd1']), 4), w=round(w, 3))
    log('CURVE ' + json.dumps(cv))
    curve.append(cv); prev_state = best['O'] + '.npz'
    if best['upper min|V|/r'][0] < 0.05:
        log('stop: window min |V|/r %.4f < 0.05 at a2=%s' % (best['upper min|V|/r'][0], a2)); break
    if best.get('err_fullT') is None or best['err_fullT'] > 0.05:
        log('stop: err_fullT %s > 0.05 at a2=%s' % (best.get('err_fullT'), a2)); break
log('done')
open('runs/v83_chain.done', 'w').close()
