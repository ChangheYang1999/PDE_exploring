"""Fixed-t growth of the canonical logarithmic coefficients (lead). Reads the output of logseries_tprofile.py and prints,
for each t in the grid, the 18-order mean increment of log10 ||f_n(t,.)||_{l1} (unit amplitude) ending at selected n,
and the cancellation lFabs - lF. 18 orders keep the residue class mod 3.
Usage: analyze_tprofile.py file.jsonl"""
import sys, json
rows = [json.loads(l) for l in open(sys.argv[1])]
by = {r['n']: r for r in rows}
TS = rows[0]['t']
W = 18
sel = [60, 100, 140, 180, 200, 220, 240, 250, 260]
print('t grid', TS)
for key in ('lF', 'lG'):
    print('\n%s: mean increment per order over the preceding %d orders' % (key, W))
    print('n    ' + ' '.join('%7.0f' % t for t in TS))
    for n in sel:
        if n in by and n - W in by and by[n][key] and by[n - W][key]:
            inc = [(by[n][key][i] - by[n - W][key][i]) / W for i in range(len(TS))]
            print('%-4d ' % n + ' '.join('%7.4f' % v for v in inc))
    print('%s: cancellation log10(abs-sum / value)' % key)
    for n in sel:
        if n in by and by[n][key]:
            ab = key + 'abs'
            print('%-4d ' % n + ' '.join('%7.2f' % (by[n][ab][i] - by[n][key][i]) for i in range(len(TS))))
    print('%s: value log10 at n' % key)
    for n in sel:
        if n in by and by[n][key]:
            print('%-4d ' % n + ' '.join('%7.2f' % by[n][key][i] for i in range(len(TS))))
