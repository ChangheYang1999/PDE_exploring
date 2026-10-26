"""Physical widths W_x, W_y from the Decimal Taylor jets (SPEC section 6; lead pre-audit F14, lead review of topics 31 and 33).
widths(hp) never raises: an undefined width (zero denominator, or a negative squared width) is None with a reason; l = (1/2) log(W_x W_y)
and eta = log(W_x / W_y) are None unless both widths are defined. Shared by campaign860 and assess860."""
from decimal import Decimal, localcontext, InvalidOperation, DivisionByZero

def widths(hp, precision=60):
    """hp: a chart860.hp_report dict (jets a, b, c as Decimal strings). Returns a dict of binary64 values or None, with reasons."""
    out = {'W_x': None, 'W_y': None, 'l': None, 'eta': None, 'a0': None, 'reasons': {}}
    try:
        with localcontext() as ctx:
            ctx.prec = precision
            a = Decimal(str(hp['jets']['a'])); b = Decimal(str(hp['jets']['b'])); c = Decimal(str(hp['jets']['c']))
            out['a0'] = float(a)
            for name, den in (('W_x', b), ('W_y', c)):
                if den == 0: out['reasons'][name] = 'undefined: zero denominator (jet %s = 0)' % ('b' if name == 'W_x' else 'c'); continue
                ratio = -a/den
                if ratio <= 0: out['reasons'][name] = 'undefined: squared width -a/%s = %s is not positive' % ('b' if name == 'W_x' else 'c', format(ratio, '.6e')); continue
                out[name] = float(ratio.sqrt())
            if out['W_x'] is not None and out['W_y'] is not None and out['W_x'] > 0 and out['W_y'] > 0:
                wx = Decimal(out['W_x']); wy = Decimal(out['W_y'])
                out['l'] = float((wx*wy).ln()/2); out['eta'] = float((wx/wy).ln())
            else: out['reasons']['l_eta'] = 'undefined: both widths must be defined and positive'
    except (InvalidOperation, DivisionByZero, KeyError, TypeError, ValueError) as exc:
        out['reasons']['exception'] = type(exc).__name__+': '+str(exc)
    return out
