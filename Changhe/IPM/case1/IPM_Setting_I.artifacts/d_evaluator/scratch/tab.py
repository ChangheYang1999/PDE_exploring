import json, sys
for f in sys.argv[1:]:
    print('==', f)
    for l in open(f):
        l = l.strip()
        if not l.startswith('{'):
            print(l[:300]); continue
        o = json.loads(l)
        print('tau %.4f step %s wall %s rtrel %.3e cl %.7f c %.6f id %.2e hP %.5f nearP1 %.2e b2_10 %.2e b10_100 %.2e' % (
            o.get('tau', 0), o.get('step'), int(o.get('wall', 0)), o['rho_tau_rel'], o['cl'], o['c'], o['ident'], o['hP'],
            o['nearP_1'][0], o['band[2,10]'][0], o['band[10,100]'][0]))
