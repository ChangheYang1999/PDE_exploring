import json,sys
f=sys.argv[1]
for l in open(f):
    d=json.loads(l); r=d['round']; s=d['snapshot']
    if r==0: continue
    buys=[]
    for e in d['event']:
        if e.get('kind')=='action':
            a=e['action']; op=a['op']
            if op=='buy_factory': buys.append('F')
            elif op=='build_wall': buys.append('w')
            elif op=='build_turret': buys.append(f"{a['type']}@{a['x']},{a['y']}")
            elif op=='buy_minion': buys.append(a['type'])
            else: buys.append(op)
            if not e.get('accepted'): buys[-1]+='!REJ'
    comb=[e for e in d['event'] if e.get('kind')=='combat']
    c=comb[0] if comb else {}
    from collections import Counter
    cnt=Counter(buys)
    print(f"r{r} p{d['player']} hp={s['hp']} gold={s['gold']} fac={s['n_factories']} tur={s['n_turrets']} ros={[x['type'] for x in s['roster']]} buys={dict(cnt)} in_dmg={c.get('base_damage')} spawned={c.get('spawned')} killed={c.get('killed')}")
