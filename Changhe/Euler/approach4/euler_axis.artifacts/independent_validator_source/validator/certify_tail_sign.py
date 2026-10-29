#!/usr/bin/env python3
"""Exact rational sign witnesses, independently from exterior NPZ labels."""
from pathlib import Path
from fractions import Fraction
from datetime import datetime, timezone
import argparse, hashlib, json, time
import numpy as np


def exact_legendre_value(coeff, x):
    x = Fraction(x)
    prev = Fraction(1)
    value = Fraction(coeff[0]) if coeff else Fraction(0)
    if len(coeff) < 2:
        return value
    current = x
    value += Fraction(coeff[1]) * current
    for n in range(2, len(coeff)):
        nxt = ((2*n-1)*x*current-(n-1)*prev)/n
        value += Fraction(coeff[n])*nxt
        prev, current = current, nxt
    return value


def fraction_record(value):
    return {'numerator':str(value.numerator), 'denominator':str(value.denominator),
            'sign':(value > 0)-(value < 0), 'approximate_value':float(value)}


def run(path, output):
    start=time.perf_counter(); cpu=time.process_time()
    raw=Path(path).read_bytes()
    with np.load(path, allow_pickle=False) as data:
        meta=json.loads(str(data['meta_json']))
        elements=meta['elements']
        i=len(elements)-1
        element=elements[i]
        if element['kind'] != 'exterior':
            raise ValueError('Expected a documented exterior element')
        labels=element.get('labels_q', element['labels'])
        values=np.asarray(data[f'q_el{i}'], dtype=np.float64).copy()
    if len(labels)!=len(values) or not np.all(np.isfinite(values)):
        raise ValueError('Invalid coefficient vector')
    alpha=float(meta['alpha']); target=alpha+1
    powers=sorted(set(float(label[1]) for label in labels))
    selected=min(powers,key=lambda p:abs(p-target))
    if abs(selected-target)>1e-12:
        raise ValueError('No leading swirl power in exterior')
    coeff=[Fraction(0) for _ in range(int(element['nmax'])+1)]
    seen=set()
    for (degree,power),value in zip(labels,values):
        if float(power)==selected:
            degree=int(degree)
            if degree in seen:raise ValueError('Duplicate angular label')
            seen.add(degree);coeff[degree]=Fraction.from_float(float(value))
    grid=np.linspace(-1,1,8193)
    sample=np.polynomial.legendre.legval(grid,[float(c) for c in coeff])
    locations={Fraction(-1),Fraction(0),Fraction(1),
               Fraction(int(np.argmin(sample))-4096,4096),
               Fraction(int(np.argmax(sample))-4096,4096)}
    witnesses=[]
    for x in sorted(locations):
        value=exact_legendre_value(coeff,x)
        witnesses.append({'mu':fraction_record(x),'value_before_positive_normalization':fraction_record(value)})
    signs={row['value_before_positive_normalization']['sign'] for row in witnesses}
    record={
        'recorded_utc':datetime.now(timezone.utc).isoformat(),
        'source':str(Path(path).resolve()),'coefficient_sha256':hashlib.sha256(raw).hexdigest(),
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'c_l':float(meta.get('cl',meta.get('c_l'))),'alpha':alpha,
        'selected_power':selected,'normalization_omitted':f"{element['Rlo']}**{selected}, strictly positive",
        'coefficients_exact_binary':[fraction_record(c) for c in coeff],
        'witnesses':witnesses,'certified_changes_sign':-1 in signs and 1 in signs,
        'certified_negative_witness':-1 in signs,'certified_positive_witness':1 in signs,
        'scope':'Exact sign of represented float64 polynomial. No global extrema or unconditional Euler obstruction claimed.',
        'elapsed_seconds':time.perf_counter()-start,'cpu_seconds':time.process_time()-cpu}
    out=Path(output);out.parent.mkdir(parents=True,exist_ok=True)
    temp=out.with_name(out.name+'.tmp');temp.write_text(json.dumps(record,indent=2)+'\n');temp.replace(out)
    print(json.dumps({k:record[k] for k in ['recorded_utc','coefficient_sha256','certified_changes_sign','elapsed_seconds']}))
    return record


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('candidate',type=Path);p.add_argument('--output',type=Path,required=True)
    args=p.parse_args();run(args.candidate,args.output)
