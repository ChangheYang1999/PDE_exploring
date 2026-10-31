"""Unexecuted bounded input bridge. No numerical evaluator is imported here."""
import ast
from fractions import Fraction
import hashlib
import io
import json
import math
import re
import struct
import sys
import zipfile

CHANNELS = ('A', 'C', 'B', 'D', 'E')
MEMBERS = frozenset(CHANNELS + ('modes', 'c_l', 'omega', 'R0', 'L', 'Nk', 'channels'))
CHANNEL_KEYS = frozenset(('NkB', 'NkD', 'NkE', 'core_damp', 'R1', 'LB', 'LD', 'LE', 'Mch'))


def _integer(value, lower, upper, name):
    if type(value) is not int or not lower <= value <= upper:
        raise ValueError('Invalid integer ' + name)
    return value


def _sha(raw):
    return hashlib.sha256(raw).hexdigest()


def _bytes(raw, expected, cap, name):
    if type(raw) is not bytes or not 1 <= len(raw) <= cap:
        raise ValueError('Invalid bounded bytes for ' + name)
    if not isinstance(expected, str) or not re.fullmatch('[0-9a-f]{64}', expected) or _sha(raw) != expected:
        raise ValueError('SHA256 mismatch for ' + name)


def _pairs(items):
    result = {}
    for key, value in items:
        if key in result:
            raise ValueError('Duplicate JSON key')
        result[key] = value
    return result


def _constant(value):
    raise ValueError('Nonfinite JSON token: ' + value)


def _json(raw):
    return json.loads(raw, object_pairs_hook=_pairs, parse_constant=_constant)


def _same_real(value, stored, name):
    if type(value) not in (int, float) or not math.isfinite(value) or float(value).hex() != stored.hex():
        raise ValueError('Metadata scalar differs: ' + name)


def _npy(member, name, maximum_modes, maximum_rows):
    if member[:8] != b'\x93NUMPY\x01\x00' or len(member) < 10:
        raise ValueError('Only NPY version one is supported')
    header_size = struct.unpack('<H', member[8:10])[0]
    if not 1 <= header_size <= 4096 or 10 + header_size > len(member):
        raise ValueError('Invalid bounded NPY header')
    header = ast.literal_eval(member[10:10+header_size].decode('latin1'))
    if not isinstance(header, dict) or set(header) != {'descr', 'fortran_order', 'shape'}:
        raise ValueError('Invalid NPY header schema')
    shape, dtype = header['shape'], header['descr']
    if header['fortran_order'] is not False or type(shape) is not tuple or len(shape) > 2:
        raise ValueError('Only bounded C-order scalar or matrix entries are supported')
    if any(type(n) is not int or n < 0 for n in shape):
        raise ValueError('Invalid NPY shape dimension')
    payload = member[10+header_size:]
    if name == 'channels':
        if shape or not isinstance(dtype, str) or not re.fullmatch(r'<U[1-9][0-9]{0,3}', dtype):
            raise ValueError('Expected bounded scalar UTF-32LE channels metadata')
        width = int(dtype[2:])
        if width > 4096 or len(payload) != 4*width:
            raise ValueError('Channels string size mismatch')
        text = payload.decode('utf-32-le').rstrip('\0')
        if '\0' in text:
            raise ValueError('Embedded NUL in channels metadata')
        values = _json(text)
    else:
        expected = '<i8' if name in ('modes', 'L', 'Nk') else '<f8'
        if dtype != expected:
            raise ValueError('Unexpected exact numerical dtype for ' + name)
        if name in CHANNELS:
            if len(shape) != 2 or not 0 <= shape[0] <= maximum_rows or not 1 <= shape[1] <= maximum_modes:
                raise ValueError('Coefficient matrix shape outside registered bounds')
        elif name == 'modes':
            if len(shape) != 2 or not 1 <= shape[0] <= maximum_modes or shape[1] != 3:
                raise ValueError('Harmonic union shape outside registered bounds')
        elif shape:
            raise ValueError('A scalar entry has a nonscalar shape')
        count = math.prod(shape)
        if len(payload) != 8*count:
            raise ValueError('NPY payload size mismatch')
        code = '<q' if expected == '<i8' else '<d'
        flat = [item[0] for item in struct.iter_unpack(code, payload)]
        if expected == '<f8' and any(not math.isfinite(value) for value in flat):
            raise ValueError('Nonfinite binary64 input')
        values = [flat[i*shape[1]:(i+1)*shape[1]] for i in range(shape[0])] if shape else flat[0]
    return values, dict(dtype=dtype, shape=list(shape), payload_sha256=_sha(payload), member_sha256=_sha(member))


def decode_exchange(raw, metadata_raw, *, archive_sha256, metadata_sha256,
                    maximum_archive_bytes, maximum_unpacked_bytes, maximum_metadata_bytes,
                    maximum_modes, maximum_rows, maximum_degree, maximum_damping):
    """Decode exact binary64 inputs and return (config, coefficients, provenance).

    Caller supplies immutable bytes and all caps. This does not authorize reading a
    selected state or constructing Primary; those remain with a reviewed driver.
    """
    _integer(maximum_archive_bytes, 1, 2**30, 'archive byte cap')
    _integer(maximum_unpacked_bytes, 1, 2**30, 'unpacked byte cap')
    _integer(maximum_metadata_bytes, 1, 2**24, 'metadata byte cap')
    _integer(maximum_modes, 1, 4096, 'mode cap')
    _integer(maximum_rows, 1, 512, 'row cap')
    _integer(maximum_degree, 1, 128, 'degree cap')
    _integer(maximum_damping, 0, 128, 'damping cap')
    if (sys.float_info.radix, sys.float_info.mant_dig, sys.float_info.max_exp, sys.float_info.min_exp) != (2, 53, 1024, -1021):
        raise ValueError('IEEE binary64 Python floats are required')
    _bytes(raw, archive_sha256, maximum_archive_bytes, 'exchange archive')
    _bytes(metadata_raw, metadata_sha256, maximum_metadata_bytes, 'exchange metadata')
    metadata = _json(metadata_raw)
    if not isinstance(metadata, dict):
        raise ValueError('Exchange metadata must be a JSON object')
    values, descriptors = {}, {}
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        infos = archive.infolist()
        if len(infos) != len(MEMBERS) or {info.filename for info in infos} != {name+'.npy' for name in MEMBERS}:
            raise ValueError('Exactly the twelve registered exchange members are required')
        if sum(info.file_size for info in infos) > maximum_unpacked_bytes:
            raise ValueError('Unpacked exchange exceeds its registered cap')
        for info in infos:
            if (info.flag_bits & 1 or info.compress_type not in (zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED)
                    or not 1 <= info.file_size <= maximum_unpacked_bytes
                    or not 0 <= info.compress_size <= maximum_archive_bytes):
                raise ValueError('Unsupported or oversized ZIP entry')
            with archive.open(info) as stream:
                member = stream.read(info.file_size+1)
            if len(member) != info.file_size:
                raise ValueError('ZIP entry length differs')
            name = info.filename[:-4]
            values[name], descriptors[name] = _npy(member, name, maximum_modes, maximum_rows)
    modes = values['modes']
    labels = set()
    for ell, m, kind in modes:
        if not 1 <= ell <= maximum_degree or not 0 <= m <= ell or kind not in (0, 1) or (m == 0 and kind):
            raise ValueError('Invalid harmonic label')
        if (ell, m, kind) in labels:
            raise ValueError('Duplicate harmonic label')
        labels.add((ell, m, kind))
    if any(m and (ell, m, 1-kind) not in labels for ell, m, kind in modes):
        raise ValueError('Incomplete harmonic azimuthal pair')
    leading = _integer(values['L'], 1, maximum_degree, 'leading degree')
    nk = _integer(values['Nk'], 1, maximum_rows, 'leading row count')
    channels = values['channels']
    if not isinstance(channels, dict) or set(channels) != CHANNEL_KEYS:
        raise ValueError('Unsupported explicit optional-channel metadata schema')
    if json.dumps(metadata.get('channels'), sort_keys=True, allow_nan=False) != json.dumps(channels, sort_keys=True, allow_nan=False):
        raise ValueError('Optional-channel metadata differs')
    damp = _integer(channels['core_damp'], 0, maximum_damping, 'core damping')
    counts = {'A': nk, 'C': nk}
    degrees = {'A': leading, 'C': leading}
    for name in ('B', 'D', 'E'):
        counts[name] = _integer(channels['Nk'+name], 0, maximum_rows, name+' row count')
        cap = channels['L'+name]
        degrees[name] = leading if cap is None else _integer(cap, 1, maximum_degree, name+' degree cap')
    if channels['Mch'] is not None:
        raise ValueError('This supported exchange profile requires null Mch')
    for name in CHANNELS:
        matrix = values[name]
        if len(matrix) != counts[name] or descriptors[name]['shape'][1] != len(modes):
            raise ValueError('Coefficient count or harmonic union width differs')
        for row in matrix:
            for (ell, m, kind), value in zip(modes, row):
                if value != 0 and (ell > degrees[name] or (name == 'E' and ell < 2)):
                    raise ValueError('Nonzero coefficient outside its declared degree support')
    cl, omega, r0 = (values[name] for name in ('c_l', 'omega', 'R0'))
    if not Fraction(2, 5) < Fraction(cl) < Fraction(1, 2) or omega == 0 or r0 <= 0:
        raise ValueError('Parameters outside the rotating-profile target interval')
    for name in ('c_l', 'omega', 'R0'):
        _same_real(metadata.get(name), values[name], name)
    if type(metadata.get('L_max')) is not int or metadata['L_max'] != leading:
        raise ValueError('Leading degree metadata differs')
    if type(metadata.get('Nk')) is not int or metadata['Nk'] != nk:
        raise ValueError('Leading row-count metadata differs')
    r1 = channels['R1']
    if r1 is not None and (type(r1) is not float or not math.isfinite(r1) or r1 <= 0):
        raise ValueError('Optional R1 must be null or positive finite binary64')
    config = dict(c_l=cl, omega=omega, R0=r0, modes=modes, core_damp=damp, R1=r1)
    ratio = Fraction(omega)/Fraction(cl)
    alpha = (1-Fraction(cl))/Fraction(cl)
    provenance = dict(archive_sha256=_sha(raw), metadata_sha256=_sha(metadata_raw),
        archive_bytes=len(raw), unpacked_bytes=sum(info.file_size for info in infos),
        metadata_bytes=len(metadata_raw), members=descriptors,
        convention='exact_binary_parameters', coefficient_semantics='exact finite binary64 dyadics',
        parameter_hex={name: values[name].hex() for name in ('c_l', 'omega', 'R0')},
        effective_R1_hex=(r0 if r1 is None else r1).hex(),
        omega_over_c_l_exact=dict(numerator=str(ratio.numerator), denominator=str(ratio.denominator)),
        alpha_exact=dict(numerator=str(alpha.numerator), denominator=str(alpha.denominator)),
        mode_count=len(modes), row_counts=counts, degree_caps=degrees,
        actual_maximum_degree=max(ell for ell, m, kind in modes),
        scope='Input decoding only. No gauge, field, residual, pressure or profile claim.')
    return config, {name: values[name] for name in CHANNELS}, provenance
