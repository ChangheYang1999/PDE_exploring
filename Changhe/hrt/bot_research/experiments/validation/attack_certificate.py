"""Exact rational implementation of analysis/attack_certificate/PROOF.md.

This is an independent certificate checker, not a tactical search policy.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction
from functools import lru_cache

RANGE_CELLS={2.5:15,3.0:20,3.5:27}
RADIUS4={2.5:25,3.0:36,3.5:49}
EXPECTED_MINIONS={
    'tier1':(20,5),'tier2':(70,12),'tier3':(180,26),
    'tier4':(560,60),'tier5':(1500,140)}
EXPECTED_TURRETS={
    'gun1':(30,8,2.5,0),'gun2':(80,22,3.0,0),
    'gun3':(200,55,3.5,0),'splash':(60,10,0.0,8)}


def validate_rules(rules):
    g=rules['globals']
    if ((g['width'],g['height'],g['ticks_per_round'])!=(12,12,250)
        or tuple(g['spawn'])!=(0,0) or tuple(g['base'])!=(11,11)
        or g['factory_cost']!=20 or rules['wall_cost']!=1
        or any(v['cost']<=0 for v in rules['minions'].values())):
        raise ValueError('Certificate requires the bundled board and tick count.')
    if {k:(v['hp'],v['damage']) for k,v in rules['minions'].items()}!=EXPECTED_MINIONS:
        raise ValueError('Certificate requires bundled minion HP and damage.')
    if {k:(v['cost'],v['damage'],v['range'],v['aoe'])
        for k,v in rules['turrets'].items()}!=EXPECTED_TURRETS:
        raise ValueError('Certificate requires bundled turret parameters.')


def offsets(kind,rules):
    if kind=='splash':
        return [(x,y) for x in (-1,0,1) for y in (-1,0,1) if (x,y)!=(0,0)]
    limit=RADIUS4[rules['turrets'][kind]['range']]
    return [(x,y) for x in range(-4,5) for y in range(-4,5)
            if 0<4*(x*x+y*y)<=limit]


def free_neighbors(x,y,kind,blocked,rules):
    return sum(0<=x+dx<12 and 0<=y+dy<12 and (x+dx,y+dy) not in blocked
               for dx,dy in offsets(kind,rules))


@lru_cache(maxsize=128)
def gun_capacities(items,gold):
    """Exact integer maxima; the value is monotone in available gold."""
    result=[0]*(gold+1)
    for budget in range(1,gold+1):
        result[budget]=max([result[budget-1]]+
            [result[budget-cost]+damage for cost,damage in items if cost<=budget])
    return tuple(result)


def fraction_pair(value):
    value=Fraction(value)
    return {'numerator':value.numerator,'denominator':value.denominator}


def certify(buildings,gold,n_existing,package,rules,exact_guns_upto=20000):
    validate_rules(rules)
    if type(gold) is not int or gold<0 or type(n_existing) is not int or n_existing<0:
        raise ValueError('Gold and active-prefix length must be nonnegative integers.')
    buildings=list(buildings)
    blocked={(x,y) for x,y,_ in buildings}
    if len(blocked)!=len(buildings):
        raise ValueError('Duplicate building cells.')
    if any(not (0<=x<12 and 0<=y<12) for x,y in blocked):
        raise ValueError('Building outside the board.')
    if any(kind not in {'wall',*rules['turrets']} for _,_,kind in buildings):
        raise ValueError('Unknown building kind.')
    # Legality of the current map is checked using the authoritative BFS.
    from td_game.pathfinding import shortest_path
    if (0,0) in blocked or (11,11) in blocked or shortest_path(12,12,blocked,(0,0),(11,11)) is None:
        raise ValueError('The current map must be legal.')
    lmax=sum(min(3,sum((x,y) not in blocked for x in (bx,bx+1) for y in (by,by+1)))
             for bx in range(0,12,2) for by in range(0,12,2))-1
    entries=[((n_existing+j)%250,kind) for j,kind in enumerate(package)]
    if any(kind not in rules['minions'] for _,kind in entries):
        raise ValueError('Unknown package minion.')
    eligible=[(tick,kind) for tick,kind in entries if tick<=249-lmax]
    if not eligible:
        return {'rational':fraction_pair(0),'integer_lower_bound':0,'eligible':0,'L_max':lmax,
                'splits':[]}
    groups=sorted({tick for tick,_ in eligible})
    m=len(groups)
    span=min(250,groups[-1]+lmax-groups[0])
    splash0=0
    gamma0=0
    for x,y,kind in buildings:
        if kind=='wall':
            continue
        spec=rules['turrets'][kind]
        count=free_neighbors(x,y,kind,blocked,rules)
        if kind=='splash':
            splash0+=10*min(7,count)
        else:
            gamma0+=spec['damage']*min(span,m*min(RANGE_CELLS[spec['range']],count))
    items=tuple((spec['cost'],spec['damage']*min(span,m*RANGE_CELLS[spec['range']]))
                for kind,spec in rules['turrets'].items() if kind!='splash')
    efficiency=max(Fraction(value,cost) for cost,value in items)
    capacities=gun_capacities(items,gold) if gold<=exact_guns_upto else None
    counts=Counter(kind for _,kind in eligible)
    splits=[]
    optimum=None
    for k in range(gold//60+1):
        s=splash0+70*k
        remaining=gold-60*k
        gamma=Fraction(gamma0)+(capacities[remaining] if capacities is not None else efficiency*remaining)
        positive=[]
        total=0
        for kind,count in counts.items():
            hp,damage=EXPECTED_MINIONS[kind]
            need=hp-s
            if need>0:
                positive.append((Fraction(damage,need),need,damage,count))
                total+=count*damage
        capacity=gamma
        removed=Fraction(0)
        for ratio,need,damage,count in sorted(positive,reverse=True):
            used=min(Fraction(count),capacity/need)
            removed+=used*damage
            capacity-=used*need
            if capacity==0:
                break
        value=max(Fraction(0),total-removed)
        splits.append({'splash_count':k,'splash_bound':s,'gun_bound':fraction_pair(gamma),
                       'damage_lower_bound':fraction_pair(value)})
        optimum=value if optimum is None else min(optimum,value)
        if optimum==0:
            break
    return {'rational':fraction_pair(optimum),
            'integer_lower_bound':-(-optimum.numerator//optimum.denominator),
            'eligible':len(eligible),'groups':m,'L_max':lmax,'span':span,
            'existing_splash_bound':splash0,'existing_gun_bound':gamma0,
            'gun_relaxation':capacities is None,'splits':splits}
