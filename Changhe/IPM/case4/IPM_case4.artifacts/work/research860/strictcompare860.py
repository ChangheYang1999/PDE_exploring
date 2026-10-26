"""Strict JSON comparator (SPEC v9.10 item 2) for every later bitwise comparison (seed reload, G3 regeneration, snapshot replay records).
Rules: JSON types are compared first (int 1 differs from float 1.0, bool from int); floats compare by bit pattern (+0.0 differs from -0.0,
NaN patterns compare bitwise); dicts need equal key sets, lists equal lengths; strings and ints exactly; named exceptions are granted only by
exact full path (e.g. '/hp_report_float_chart/poisson_max_abs') through a caller-supplied predicate that receives (path, a, b) and returns
True when that single leaf is accepted; every exception used is listed in the result."""
import struct

def _bits(x): return struct.pack('>d', float(x))

def compare(a, b, path='', exceptions=None):
    """Returns {'equal': bool, 'differences': [...], 'exceptions_used': [...]}; differences carry the full path, the JSON types and the values."""
    diffs = []; used = []
    def walk(x, y, p):
        tx, ty = type(x), type(y)
        if tx is not ty:
            if exceptions and exceptions.get(p) and exceptions[p](p, x, y): used.append({'path': p, 'a': x, 'b': y, 'reason': 'type'}); return
            diffs.append({'path': p, 'kind': 'type', 'a_type': tx.__name__, 'b_type': ty.__name__, 'a': x, 'b': y}); return
        if isinstance(x, dict):
            if set(x) != set(y): diffs.append({'path': p, 'kind': 'keys', 'only_a': sorted(set(x)-set(y)), 'only_b': sorted(set(y)-set(x))}); return
            for k in sorted(x): walk(x[k], y[k], p+'/'+str(k))
        elif isinstance(x, list):
            if len(x) != len(y): diffs.append({'path': p, 'kind': 'length', 'a': len(x), 'b': len(y)}); return
            for i, (u, v) in enumerate(zip(x, y)): walk(u, v, p+'[%d]' % i)
        elif isinstance(x, float):
            if _bits(x) != _bits(y):
                if exceptions and exceptions.get(p) and exceptions[p](p, x, y): used.append({'path': p, 'a': x, 'b': y, 'reason': 'float'}); return
                diffs.append({'path': p, 'kind': 'float_bits', 'a': x, 'b': y, 'a_hex': x.hex(), 'b_hex': y.hex()})
        else:
            if x != y:
                if exceptions and exceptions.get(p) and exceptions[p](p, x, y): used.append({'path': p, 'a': x, 'b': y, 'reason': 'value'}); return
                diffs.append({'path': p, 'kind': 'value', 'a': x, 'b': y})
    walk(a, b, path)
    return {'equal': not diffs, 'differences': diffs, 'exceptions_used': used, 'rule': 'SPEC v9.10: types first, floats by bit pattern, equal key sets and lengths, named exceptions by exact full path'}

if __name__ == '__main__':
    r1 = compare({'a': 1, 'b': [1.0, -0.0]}, {'a': 1.0, 'b': [1.0, 0.0]}); assert not r1['equal'] and {d['kind'] for d in r1['differences']} == {'type', 'float_bits'}
    r2 = compare({'x': {'p': 7e-87}}, {'x': {'p': 7.4e-87}}, exceptions={'/x/p': lambda p, a, b: abs(a-b) <= 1e-60}); assert r2['equal'] and len(r2['exceptions_used']) == 1
    r3 = compare({'x': {'p': 7e-87}}, {'x': {'q': 7e-87}}); assert not r3['equal'] and r3['differences'][0]['kind'] == 'keys'
    r4 = compare([True], [1]); assert not r4['equal'] and r4['differences'][0]['kind'] == 'type'
    print('strictcompare860 self-check ok')
