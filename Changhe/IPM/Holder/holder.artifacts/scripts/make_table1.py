# Table 1 of the final report: best certified upper and lower bounds at the listed exponents.
# Every entry is read from an interval certificate. Upper bounds use the upper interval endpoint (or the
# certificate's saved safe upper decimal) rounded up at 6 decimals; lower bounds the lower endpoint rounded down.
# Usage: python3 make_table1.py <data_dir>   (data_dir = the certified-data folder of the accompanying artifacts)
import json, re, sys, math, glob, os
from fractions import Fraction
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, getcontext
getcontext().prec = 60
D = os.path.abspath(sys.argv[1]).rstrip('/') + '/'   # absolute, so that the sibling folders also resolve from a relative path
def parts(s):
    m = re.match(r'\[([-0-9.e+]+) \+/- ([0-9.e+-]+)\]', s.strip())
    return Decimal(m.group(1)), Decimal(m.group(2))
def lo(s): c, r = parts(s); return c - r
def hi(s): c, r = parts(s); return c + r
up6 = lambda x: Decimal(x).quantize(Decimal('0.000001'), rounding=ROUND_CEILING)
dn6 = lambda x: Decimal(x).quantize(Decimal('0.000001'), rounding=ROUND_FLOOR)
key = lambda a: Fraction(str(a)).limit_denominator(100000)
def rows(fn):
    d = json.load(open(D + fn))
    r = d['rows']
    if isinstance(r, str):
        import ast; r = ast.literal_eval(r)
    return d, r
up_C, up_D, low = {}, {}, {}
def add(dct, a, val, name, better):
    a = key(a)
    if a not in dct or better(val, dct[a][0]): dct[a] = (val, name)
lt = lambda x, y: x < y
gt = lambda x, y: x > y
# Upper families
_, r = rows('explicit_bounds_intervals.json')
F = {}; G = {}
for x in r:
    F[key(x['alpha'])] = hi(x['intervals']['upper_C']); G[key(x['alpha'])] = hi(x['intervals']['upper_D'])
    add(up_C, x['alpha'], F[key(x['alpha'])], 'F (Thm 3.1)', lt); add(up_D, x['alpha'], G[key(x['alpha'])], 'G (Thm 3.1)', lt)
_, r = rows('local_projection_intervals.json')
GP = {}
for x in r:
    GP[key(x['alpha'])] = hi(x['upper_D']); add(up_D, x['alpha'], GP[key(x['alpha'])], 'G (Thm 3.2)', lt)
for fn, nm in [('midpoint_split_certificate_fine.json', 'midpoint split (Thm 3.3)'),
               ('midpoint_split_certificate_coarse.json', 'midpoint split (Thm 3.3)'),
               ('reflection_orbit_certificate_v2_coarse.json', 'reflection orbits (Thm 3.4)'),
               ('reflection_orbit_certificate_v2_fine.json', 'reflection orbits (Thm 3.4)'),
               ('circle_composite_upper_fine.json', 'exterior circles (Thm 3.5)'),
               ('circle_composite_upper_n768.json', 'exterior circles (Thm 3.5)'),
               ('middle_composite_upper_n512.json', 'middle-circle transport (Thm 3.6)')]:
    if not os.path.exists(D + fn): continue
    _, r = rows(fn)
    for x in r:
        add(up_C, x['alpha'], Decimal(x['safe_upper_C']), nm, lt); add(up_D, x['alpha'], Decimal(x['safe_upper_D']), nm, lt)
# Explicit cutoff bounds H and linear-remainder bounds J (Thm 5.7), exact rational upper endpoints at rational cutoffs
EXS = os.path.dirname(D.rstrip('/')) + '/08_improved_upper_bounds/explicit_second_term/verification/rational_cutoffs.json'
if os.path.exists(EXS):
    for x in json.load(open(EXS))['rows']:
        for k, dct in (('H_C', up_C), ('J_C', up_C), ('H_D', up_D), ('J_D', up_D)):
            q = Fraction(x['bounds'][k]['upper'])
            add(dct, x['alpha'], Decimal(q.numerator) / Decimal(q.denominator), 'cutoff %s (Thm 5.7)' % k[0], lt)
else: print('# missing explicit second-term values', file=sys.stderr)
# Closed form F** (Thm 9.3), independently evaluated values at the table exponents (audited): C only
CF = os.path.dirname(D.rstrip('/')) + '/05_team_audit/closed_form37_lead/verification/'
if os.path.exists(CF + 'closed_form_values.json'):
    assert json.load(open(CF + 'accepted.json'))['verdict'] == 'CONFIRMED'
    for x in json.load(open(CF + 'closed_form_values.json'))['rows']:
        q = Fraction(x['upper']); v = Decimal(x['safe_upper_C'])
        assert Decimal(q.numerator) / Decimal(q.denominator) <= v
        add(up_C, x['alpha'], v, 'closed form F** (Thm 9.3)', lt)
else: print('# missing closed-form F** values', file=sys.stderr)
# Paired local circles (Thm 3.7): C only
for fn in ['local_circle_composite_a30.json', 'local_circle_composite_a50.json',
           'local_circle_composite_a75.json', 'local_circle_composite_a90.json']:
    if not os.path.exists(D + fn): continue
    _, r = rows(fn)
    for x in r:
        assert hi(x['upper_C']) <= Decimal(x['safe_upper_C'])
        add(up_C, x['alpha'], Decimal(x['safe_upper_C']), 'paired local circles (Thm 3.7)', lt)
# Direct Theorem 3.7 certificates with plans chosen at the exponent itself (audited): C only
T37 = os.path.dirname(D.rstrip('/')) + '/05_team_audit/table37_lead/verification/accepted.json'
if os.path.exists(T37):
    d = json.load(open(T37)); assert d['verdict'] == 'CONFIRMED'
    for x in d['rows']: add(up_C, x['alpha'], Decimal(x['safe_upper_C']), 'paired local circles (Thm 3.7)', lt)
else: print('# missing direct Theorem 3.7 values', file=sys.stderr)
# The same certificates with the balanced residual coupling of Thm 3.7 (exact mass replay, audited): C only
BR = os.path.dirname(D.rstrip('/')) + '/08_improved_upper_bounds/local_disk_transport/balanced_residual/existing_certificates/verification/accepted.json'
if os.path.exists(BR):
    d = json.load(open(BR)); assert d['verdict'] == 'CONFIRMED'
    for x in d['rows']: add(up_C, x['alpha'], Decimal(x['safe_upper_C']), 'paired local circles, balanced residual (Thm 3.7)', lt)
else: print('# missing balanced-residual values', file=sys.stderr)
# The same certificates with the balanced residual paired radius by radius (Thm 3.7, eight subintervals per radial bin; audited): C only
RR = BR.replace('existing_certificates', 'radial_refinement')
if os.path.exists(RR):
    d = json.load(open(RR)); assert d['verdict'] == 'CONFIRMED'
    for x in d['rows']: add(up_C, x['alpha'], Decimal(x['safe_upper_C']), 'paired local circles, radial residual (Thm 3.7)', lt)
else: print('# missing radial-residual values', file=sys.stderr)
# The middle-circle certificates of Thm 3.6 with the middle-arc residual coupling (exact mass replay, audited): C and D
MR = os.path.dirname(D.rstrip('/')) + '/08_improved_upper_bounds/middle_circle_transport/balanced_residual/verification/accepted.json'
if os.path.exists(MR):
    d = json.load(open(MR)); assert d['verdict'] == 'CONFIRMED'
    for x in d['rows']:
        add(up_C, x['alpha'], Decimal(x['safe_upper_C']), 'paired local circles, radial and middle-arc residual (Thm 3.7)', lt)
        add(up_D, x['alpha'], Decimal(x['safe_upper_D']), 'middle-circle transport, middle-arc residual (Thm 3.6)', lt)
else: print('# missing middle-arc residual values', file=sys.stderr)
# The same middle-arc residual cost on the direct Theorem 3.7 certificates (same extracted masses, audited): C only
MT = MR.replace('/verification/', '/table37/verification/')
if os.path.exists(MT):
    d = json.load(open(MT)); assert d['verdict'] == 'CONFIRMED'
    for x in d['rows']: add(up_C, x['alpha'], Decimal(x['safe_upper_C']), 'paired local circles, radial and middle-arc residual (Thm 3.7)', lt)
else: print('# missing middle-arc residual values for the direct certificates', file=sys.stderr)
# Exact sine interpolation of adjacent phase bounds (H_delta, Section 3) applied to the accepted phase arrays (audited): C and D
PI = os.path.dirname(D.rstrip('/')) + '/08_improved_upper_bounds/phase_interpolation/verification/accepted.json'
if os.path.exists(PI):
    d = json.load(open(PI)); assert d['verdict'] == 'CONFIRMED'
    for x in d['rows']:
        if x['operator'] == 'C': add(up_C, x['alpha'], Decimal(x['safe_upper']), 'paired local circles, radial and middle-arc residual, phase interpolation (Thm 3.7)', lt)
        else: add(up_D, x['alpha'], Decimal(x['safe_upper']), 'middle-circle transport, middle-arc residual, phase interpolation (Thm 3.6)', lt)
else: print('# missing phase-interpolation values', file=sys.stderr)
# Thm 3.6 with the middle bins of the direct Thm 3.7 certificates and their middle-arc residual gains (audited): D only
D36 = os.path.dirname(D.rstrip('/')) + '/05_team_audit/d36_recombination/verification/accepted.json'
if os.path.exists(D36):
    d = json.load(open(D36)); assert d['verdict'] == 'CONFIRMED'
    r = d['rows']
    if isinstance(r, str):
        import ast; r = ast.literal_eval(r)
    for x in r: add(up_D, x['alpha'], Decimal(x['safe_upper_D']), 'middle-circle transport on the direct certificates, phase interpolation (Thm 3.6)', lt)
else: print('# missing direct-certificate Theorem 3.6 values', file=sys.stderr)
# Thm 3.6 with the cross-disk part enclosed on 2048^2 rectangles, phase interpolation (audited): D only
X48 = os.path.dirname(D.rstrip('/')) + '/05_team_audit/cross2048/recombination/verification/accepted.json'
if os.path.exists(X48):
    d = json.load(open(X48)); assert d['verdict'] == 'CONFIRMED'
    for x in d['rows']: add(up_D, x['alpha'], Decimal(x['safe_upper_D']), 'middle-circle transport, finer cross disks, phase interpolation (Thm 3.6)', lt)
else: print('# missing finer cross-disk values', file=sys.stderr)
# The strict saving of Thm 3.9 in the identity term, subtracted from the best D endpoints above (audited): D only
SS = os.path.dirname(D.rstrip('/')) + '/08_improved_upper_bounds/local_projection/strict_increment/larger_disks/radial_density/symmetric_concavity/fourth_moment/numerical_values/accepted.json'
if os.path.exists(SS):
    d = json.load(open(SS)); assert d['verdict'] == 'CONFIRMED'
    for x in d['rows']:
        if x['kind'] == 'retained cutoff': nm = 'cutoff J with the strict saving (Thm 5.7, 3.9)'
        elif 'circle_composite' in x['source']: nm = 'exterior circles with the strict saving (Thm 3.5, 3.9)'
        else: nm = 'middle-circle transport, finer cross disks, phase interpolation, strict saving (Thm 3.6, 3.8, 3.9)'
        add(up_D, x['alpha'], Decimal(x['safe_upper_D']), nm, lt)
else: print('# missing strict-saving values', file=sys.stderr)
# The exact radial density in the strict saving of Thm 3.9, from the same bases (audited): D only
ER = os.path.dirname(D.rstrip('/')) + '/08_improved_upper_bounds/local_projection/strict_increment/larger_disks/exact_radial_density/numerical_values/accepted.json'
if os.path.exists(ER):
    d = json.load(open(ER)); assert d['verdict'] == 'CONFIRMED'
    for x in d['rows']:
        if x['kind'] == 'retained cutoff': nm = 'cutoff J with the strict saving (Thm 5.7, 3.9)'
        elif 'circle_composite' in x['source']: nm = 'exterior circles with the strict saving (Thm 3.5, 3.9)'
        else: nm = 'middle-circle transport, finer cross disks, phase interpolation, strict saving (Thm 3.6, 3.8, 3.9)'
        add(up_D, x['alpha'], Decimal(x['safe_upper_D']), nm, lt)
else: print('# missing exact-radial strict-saving values', file=sys.stderr)
# Sharper local deficiencies in J_C, J_D (Thm 5.7(ii)), with the strict saving of Thm 3.9(c) for D (audited)
SD = os.path.dirname(D.rstrip('/')) + '/08_improved_upper_bounds/explicit_second_term/sharp_deficiency/numerical_values/accepted.json'
if os.path.exists(SD):
    d = json.load(open(SD)); assert d['verdict'] == 'CONFIRMED'
    for x in d['rows']:
        if x['mode'] != 'finite': continue
        if x['operator'] == 'C': add(up_C, x['alpha_or_epsilon'], Decimal(x['safe_upper']), 'cutoff J (Thm 5.7)', lt)
        else: add(up_D, x['alpha_or_epsilon'], Decimal(x['safe_upper']),
                  'cutoff J with the strict saving (Thm 5.7, 3.9)' if x['retained_reflection'] else 'cutoff J (Thm 5.7)', lt)
else: print('# missing sharp-deficiency values', file=sys.stderr)
# Thm 3.6 with the cross-disk part enclosed on 4096^2 rectangles, phase interpolation, exact-radial saving of Thm 3.9 (audited): D only
CX = os.path.dirname(D.rstrip('/')) + '/08_improved_upper_bounds/local_projection/strict_increment/larger_disks/exact_radial_density/cross4096_values/accepted.json'
if os.path.exists(CX):
    d = json.load(open(CX)); assert d['verdict'] == 'CONFIRMED'
    for x in d['rows']:
        if x['kind'] == 'retained cutoff': nm = 'cutoff J with the strict saving (Thm 5.7, 3.9)'
        elif 'circle_composite' in x['source']: nm = 'exterior circles with the strict saving (Thm 3.5, 3.9)'
        else: nm = 'middle-circle transport, finer cross disks, phase interpolation, strict saving (Thm 3.6, 3.8, 3.9)'
        add(up_D, x['alpha'], Decimal(x['safe_upper_D']), nm, lt)
else: print('# missing 4096 cross-disk values', file=sys.stderr)
# Exact exterior series in J_C, J_D (Thm 5.7(ii)) (audited)
TS = os.path.dirname(D.rstrip('/')) + '/08_improved_upper_bounds/explicit_second_term/tail_series/numerical_values/accepted.json'
if os.path.exists(TS):
    d = json.load(open(TS)); assert d['verdict'] == 'CONFIRMED'
    for x in d['rows']:
        if x['mode'] != 'finite': continue
        if x['operator'] == 'C': add(up_C, x['alpha_or_epsilon'], Decimal(x['safe_upper']), 'cutoff J (Thm 5.7)', lt)
        else: add(up_D, x['alpha_or_epsilon'], Decimal(x['safe_upper']),
                  'cutoff J with the strict saving (Thm 5.7, 3.9)' if x['retained_reflection'] else 'cutoff J (Thm 5.7)', lt)
else: print('# missing exact-tail values', file=sys.stderr)
# Larger disks and eight reflection moments (Thm 3.10) on the same bases (audited): D only
OD = os.path.dirname(D.rstrip('/')) + '/08_improved_upper_bounds/local_projection/strict_increment/larger_disks/optimal_axis_disks/numerical_values/accepted.json'
if os.path.exists(OD):
    d = json.load(open(OD)); assert d['verdict'] == 'CONFIRMED'
    for x in d['rows']:
        if x['mode'] != 'finite': continue
        a = key(x['alpha_or_epsilon'])
        if x['kind'] == 'cutoff': nm = 'cutoff J with the strict saving (Thm 5.7, 3.10)'
        elif a in (Fraction(1, 20), Fraction(1, 10)): nm = 'exterior circles with the strict saving (Thm 3.5, 3.10)'
        else: nm = 'middle-circle transport, finer cross disks, phase interpolation, strict saving (Thm 3.6, 3.8, 3.10)'
        add(up_D, x['alpha_or_epsilon'], Decimal(x['safe_upper']), nm, lt)
else: print('# missing larger-disk values', file=sys.stderr)
# Phase-uniform reflection density (Thm 3.10(c)) on the same disks and bases (audited): D only
PU = OD.replace('/larger_disks/optimal_axis_disks/', '/phase_uniform_density/')
if os.path.exists(PU):
    d = json.load(open(PU)); assert d['verdict'] == 'CONFIRMED'
    for x in d['rows']:
        if x['mode'] != 'finite': continue
        a = key(x['alpha_or_epsilon'])
        if x['kind'] == 'cutoff': nm = 'cutoff J with the strict saving (Thm 5.7, 3.10(c))'
        elif a in (Fraction(1, 20), Fraction(1, 10)): nm = 'exterior circles with the strict saving (Thm 3.5, 3.10(c))'
        else: nm = 'middle-circle transport, finer cross disks, phase interpolation, strict saving (Thm 3.6, 3.8, 3.10(c))'
        add(up_D, x['alpha_or_epsilon'], Decimal(x['safe_upper']), nm, lt)
else: print('# missing phase-uniform values', file=sys.stderr)
# Supplemental disjoint axis disks (Thm 3.10(d)) on top of the phase-uniform values (audited): D only
SD = PU.replace('/numerical_values/', '/supplemental_disks/numerical_values/')
if os.path.exists(SD):
    d = json.load(open(SD)); assert d['verdict'] == 'CONFIRMED'
    for x in d['rows']:
        if x['mode'] != 'finite': continue
        a = key(x['alpha_or_epsilon'])
        if x['kind'] == 'cutoff': nm = 'cutoff J with the strict saving (Thm 5.7, 3.10(d))'
        elif a in (Fraction(1, 20), Fraction(1, 10)): nm = 'exterior circles with the strict saving (Thm 3.5, 3.10(d))'
        else: nm = 'middle-circle transport, finer cross disks, phase interpolation, strict saving (Thm 3.6, 3.8, 3.10(d))'
        add(up_D, x['alpha_or_epsilon'], Decimal(x['safe_upper']), nm, lt)
else: print('# missing supplemental-disk values', file=sys.stderr)
# Lower families
for fn, nm, fld in [('gated_lower_intervals.json', 'gated (Thm 4.3)', 'safe_decimal_lower_10_places'),
                    ('cusp_refinement_intervals.json', 'two-cusp (Thm 4.2)', 'C_and_D_lower_interval'),
                    ('homogeneous_lower_intervals.json', 'degree-3 (Thm 4.4)', 'C_lower_interval')]:
    _, r = rows(fn)
    for x in r:
        v = x[fld]
        if v.startswith('['): v = lo(v)
        else: q = Fraction(v); v = Decimal(q.numerator) / Decimal(q.denominator)
        add(low, x['alpha'], v, nm, gt)
d, r = rows('structured_full_a_half.json')
for x in r: add(low, x['alpha'], Decimal(x['safe_decimal_lower_10_places']), 'polygonal a=1/2 (Thm 4.5)', gt)
for fn in sorted(glob.glob(D + 'structured_shape_certificates/alpha_*.json')):
    d = json.load(open(fn))
    for x in d['rows']: add(low, x['alpha'], Decimal(x['safe_decimal_lower_10_places']), 'polygonal a=%s (Thm 4.5)' % d['a'], gt)
d = json.load(open(D + 'structured_layercake_certificate_fine.json'))
add(low, d['alpha'], Decimal(d['safe_decimal_lower_10_places']), 'polygonal a=1/2 (Thm 4.5)', gt)
# Lower bounds for D only (finite projection witness, Thm 4.6); elsewhere the best D lower bound is L(alpha)
low_D = dict(low)
for fn in sorted(glob.glob(D + 'finite_D_lower_a*.json')):
    if fn.endswith('_geometric.json'): continue   # superseded by finite_D_lower_a30_geometric_fine.json
    d = json.load(open(fn))
    add(low_D, Fraction(d['alpha']), Decimal(d['safe_D_lower']), 'projection witness (Thm 4.6)', gt)
# Half-plane lattice witnesses in the axis phase (Thm 4.7). Explicit list of audited certificates only
# (a combined file is listed here after its independent audit; an automatic glob could pick up unaudited runs).
LAT = os.path.dirname(D.rstrip('/')) + '/11_lattice_pole_constraints/'
for fn, nm in [('axis_clamped_layercake/verification/a75_b75_combined_131072.json', 'axis polygon clamp (Thm 4.7(ii))'),
               ('axis_clamped_layercake/verification/a90_b35_combined_131072.json', 'axis polygon clamp (Thm 4.7(ii))'),
               ('axis_clamped_layercake/verification/a99_b1_long_combined_2097152.json', 'axis polygon clamp (Thm 4.7(ii))'),
               ('axis_sector_cusp/verification/a50_b75_tm30_combined_131072.json', 'axis sector cusp (Thm 4.7(iii))'),
               ('axis_projection_stieltjes/verification/a50_n8192_m128_v2_combined.json', 'axis projection cusp (Thm 4.7(iv))'),
               ('axis_projection_stieltjes/verification/a50_n32768_m256_v2_combined.json', 'axis projection cusp (Thm 4.7(iv))')]:
    if not os.path.exists(LAT + fn):
        print('# missing lattice certificate', fn, file=sys.stderr); continue
    d = json.load(open(LAT + fn))
    add(low_D, Fraction(d['alpha']), Decimal(d['safe_D_lower_10_places']), nm, gt)
LEAD = os.path.dirname(D.rstrip('/')) + '/lead_projection/verification/'
for fn, nm in [('a30_b150_t0_n32768_m256_combined.json', 'axis projection cusp (Thm 4.7(v))')]:
    if not os.path.exists(LEAD + fn):
        print('# missing lattice certificate', fn, file=sys.stderr); continue
    d = json.load(open(LEAD + fn))
    add(low_D, Fraction(d['alpha']), Decimal(d['safe_D_lower_10_places']), nm, gt)
# Two-dimensional cell enclosure of the witness of Thm 4.7(iv) (independent repaired replay; audited)
AUD = os.path.dirname(D.rstrip('/')) + '/05_team_audit/note14_certificate/'
for fn, nm in [('replay_a50/independent_audit.json', 'axis projection cusp, cell enclosure (Thm 4.7(iv))'),
               ('replay_a75/independent_audit.json', 'axis projection cusp, cell enclosure (Thm 4.7(vi))')]:
    if not os.path.exists(AUD + fn):
        print('# missing cell-enclosure certificate', fn, file=sys.stderr); continue
    d = json.load(open(AUD + fn))
    assert d['verdict'].startswith('CONFIRMED')
    add(low_D, Fraction(d['alpha']), Decimal(d['safe_D_lower_10_places']), nm, gt)
# Cell enclosures of the finite region with the homogeneous tail of Thm 4.7(vii) (audited)
TAIL = AUD + 'homogeneous_tail/verification/accepted.json'
if os.path.exists(TAIL):
    d = json.load(open(TAIL)); assert d['verdict'] == 'CONFIRMED'
    for x in d['rows']: add(low_D, Fraction(x['alpha']), Decimal(x['safe_D_lower']), 'axis projection cusp, homogeneous tail (Thm 4.7(vii))', gt)
else: print('# missing homogeneous-tail certificates', file=sys.stderr)
# The same finite regions with the explicit pole-disk lemma of Thm 4.7(vii) (audited; first the linear, then the quadratic clamp error)
for fn in ['pole_profile/verification/accepted.json', 'pole_profile/quadratic_lower/verification/accepted.json']:
    if not os.path.exists(AUD + fn):
        print('# missing pole-disk certificates', fn, file=sys.stderr); continue
    d = json.load(open(AUD + fn)); assert d['verdict'] == 'CONFIRMED'
    for x in d.get('rows', d.get('records')): add(low_D, Fraction(x['alpha']), Decimal(x['safe_D_lower']), 'axis projection cusp, pole disks and tail (Thm 4.7(vii))', gt)
# The complete fine partitions at alpha = 1/2 and 3/4 with the same pole-disk lemma and tail (independent full replays; audited)
for fn in ['replay_fine_a50/full_quadratic/accepted.json', 'replay_fine_a75/full_quadratic/accepted.json']:
    if not os.path.exists(AUD + fn):
        print('# missing complete fine replay', fn, file=sys.stderr); continue
    d = json.load(open(AUD + fn)); assert d['verdict'] == 'CONFIRMED' and d['task_count'] == d['total_manifest_tasks']
    add(low_D, Fraction(d['alpha']), Decimal(d['safe_D_lower']), 'axis projection cusp, pole disks and tail (Thm 4.7(vii))', gt)
# The finer producer computations at alpha = 1/2 and 3/4: audited task records, exact recombination, 52 and 70 selected
# complete-task replays
for fn in ['producer_fine_a50/quadratic_recombination/accepted.json', 'producer_fine_a75/quadratic_recombination/accepted.json']:
    if not os.path.exists(AUD + fn):
        print('# missing audited producer certificate', fn, file=sys.stderr); continue
    d = json.load(open(AUD + fn)); assert d['verdict'] == 'CONFIRMED' and int(d['selected_task_replays']) > 0
    add(low_D, Fraction(d['alpha']), Decimal(d['safe_D_lower']), 'axis projection cusp, pole disks and tail (Thm 4.7(vii))', gt)
# Sharper Stieltjes sums of Thm 4.7(viii) (audited; the combined chunk certificate is in lead_projection/verification/)
for fn in ['stieltjes_v7/a20/accepted.json', 'stieltjes_v7/a30/accepted.json', 'stieltjes_v7/a10/accepted.json']:
    if not os.path.exists(AUD.replace('note14_certificate/', '') + fn):
        print('# missing sharper Stieltjes certificate', fn, file=sys.stderr); continue
    d = json.load(open(AUD.replace('note14_certificate/', '') + fn)); assert d['verdict'] == 'CONFIRMED'
    cf = LEAD + fn.split('/')[1] + 'v7_combined.json'
    if os.path.exists(cf):
        assert json.load(open(cf))['safe_D_lower_10_places'] == d['safe_D_lower']
    add(low_D, Fraction(d['alpha']), Decimal(d['safe_D_lower']), 'axis projection cusp, sharper Stieltjes sums (Thm 4.7(viii))', gt)
C0 = 0.5 - (1 - math.log(2)) / math.pi
REPORT = '--report' in sys.argv
if REPORT:
    print('| $\\alpha$ | $F\\ge C_\\alpha$ | $F+\\frac12$ | $G\\ge D_\\alpha$ | best upper $C_\\alpha$ | best upper $D_\\alpha$ | $L(\\alpha)\\le C_\\alpha$ | polygon shape $a$ | best lower $D_\\alpha$ | ratio for $C$ | ratio for $D$ | $\\frac2{\\pi\\alpha}+C_0$ |')
    print('|---|---|---|---|---|---|---|---|---|---|---|---|')
    for a in sorted(F):
        uc, nc = up_C[a]; ud, nd = up_D[a]; L, nl = low[a]
        ratio = (up6(uc) / dn6(L)).quantize(Decimal('0.0001'), rounding=ROUND_CEILING)
        shape = nl.split('a=')[1].split(' ')[0] if 'a=' in nl else nl
        LD, nld = low_D[a]
        ratioD = (up6(ud) / dn6(LD)).quantize(Decimal('0.0001'), rounding=ROUND_CEILING)
        sD = f'**{dn6(LD)}**' if nld != nl else f'{dn6(LD)}'
        print(f'| {float(a):g} | {up6(F[a])} | {up6(G[a])} | {up6(GP[a])} | {up6(uc)} | {up6(ud)} | {dn6(L)} | {shape} | {sD} | {ratio} | {ratioD} | {2/(math.pi*float(a))+C0:.4f} |')
    for a in sorted(F): print('#', float(a), up_C[a][1], '|', up_D[a][1], '|', low[a][1], '|', low_D[a][1], file=sys.stderr)
    sys.exit(0)
print('| $\\alpha$ | $F$ | $F+\\frac12$ | $G$ | best upper $C_\\alpha$ | best upper $D_\\alpha$ | best lower $L(\\alpha)$ | lower family | best lower $D_\\alpha$ | upper/lower for $C$ | upper/lower for $D$ | $\\frac2{\\pi\\alpha}+C_0$ |')
print('|---|---|---|---|---|---|---|---|---|---|---|---|')
for a in sorted(F):
    uc, nc = up_C[a]; ud, nd = up_D[a]; L, nl = low[a]
    ratio = (up6(uc) / dn6(L)).quantize(Decimal('0.0001'), rounding=ROUND_CEILING)
    LD, nld = low_D[a]
    ratioD = (up6(ud) / dn6(LD)).quantize(Decimal('0.0001'), rounding=ROUND_CEILING)
    print(f'| {float(a):g} | {up6(F[a])} | {up6(G[a])} | {up6(GP[a])} | {up6(uc)} ({nc.split(" (")[0]}) | {up6(ud)} ({nd.split(" (")[0]}) | {dn6(L)} | {nl} | {dn6(LD)} ({nld.split(" (")[0]}) | {ratio} | {ratioD} | {2/(math.pi*float(a))+C0:.4f} |')
