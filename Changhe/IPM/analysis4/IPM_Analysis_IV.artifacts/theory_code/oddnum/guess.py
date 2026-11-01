import itertools, sys
data = {}
for line in open('digits_sin1.out'):
    if not line.startswith('p='): continue
    t = line.split()
    p = int(t[0][2:]); a = int(t[1][2:])
    dig = eval(line.split('=')[-1])
    data[(p, a)] = dig
def search(pairs, label):
    sols = []
    for s in range(1, 400):
        for r in range(-400, 401):
            for sgn in ('1', 'chi4', 'chi8', 'chi3'):
                ok = True
                for (p, X) in pairs:
                    e = 1
                    if sgn == 'chi4': e = 1 if p % 4 == 1 else -1
                    if sgn == 'chi8': e = 1 if p % 8 in (1, 7) else -1
                    if sgn == 'chi3': e = 1 if p % 3 == 1 else -1
                    if s % p == 0 or (e * r - X * s) % p: ok = False; break
                if ok: sols.append((r, s, sgn))
    print(label, sols[:12])
for a in (3, 5, 7):
    pairs = [(p, d[3]) for (p, aa), d in data.items() if aa == a and 2 * a < p]
    print(a, pairs)
    search(pairs, f'a={a} v=-1 digit')
