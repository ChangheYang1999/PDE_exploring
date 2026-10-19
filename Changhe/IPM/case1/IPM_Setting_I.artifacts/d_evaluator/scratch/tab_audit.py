# Table of vaudit logs: c_l, hP-1, flux/N_v max by region, J spread at d = 0.01, B_3 (ibp, wpp_ode)
import sys, json, re
regs = ['r<=0.1', '0.1<=r<=2', '2<=r<=10', '10<=r<=100', '100<=r<=1000', '1000<=r<=R', '|X-P|<0.5', 'all']
for f in sys.argv[1:]:
    L = open(f).read().splitlines()
    head = next(json.loads(l) for l in L if l.startswith('{"file"'))
    rows = {}
    for l in L:
        m = re.match(r'\s+(\S+)\s+flux max (\S+) rms (\S+) \| N_v max (\S+) rms (\S+)', l)
        if m: rows[m.group(1)] = m.groups()[1:]
    b3 = [l for l in L if l.startswith('B3 wpp_ode')]
    J = [l for l in L if l.startswith('J at')]
    relE = ' '.join('%.0e' % r['relE'] for r in head['regions'])
    print(f.split('/')[-1], 'c_l %.7f hP-1 %+.1e' % (head['c_l'], head['hP'] - 1), 'relE', relE)
    print('   flux max: ' + ' '.join('%s %s' % (k, rows[k][0]) for k in regs if k in rows))
    print('   flux rms: ' + ' '.join('%s %s' % (k, rows[k][1]) for k in regs if k in rows))
    print('   N_v max : ' + ' '.join('%s %s' % (k, rows[k][2]) for k in regs if k in rows))
    if J: print('   J spread(d=4..0.01):', J[0].split('spread')[1].split('Jmin')[0].strip())
    if b3: print('  ', b3[0])
