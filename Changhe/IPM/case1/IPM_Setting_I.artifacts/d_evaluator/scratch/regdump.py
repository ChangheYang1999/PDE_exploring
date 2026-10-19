import json, sys
L = 7.651424601381517
for f in sys.argv[1:]:
    d = json.load(open(f))
    print('==', f.split('/')[-1])
    for x in d['residual']:
        print('  %-48s Nf %.4e at r %.4g (%.4g L) th %.4f | Nv %.4e at r %.4g (%.4g L) th %.4f' % (
            x['region'][:48], x['flux_max'], x['flux_argmax_r'], x['flux_argmax_r'] / L, x['flux_argmax_theta'],
            x['Nv_max'], x['Nv_argmax_r'], x['Nv_argmax_r'] / L, x['Nv_argmax_theta']))
