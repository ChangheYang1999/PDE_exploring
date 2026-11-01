"""Validated integer coverage; singleton leaves use an exact integer point."""
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb
from gmpy2 import mpq
from pure_cartesian_ball import ball
from certified_initial_majorants import pack
import json,time

def lower(value):
    m,e=value.mid().man_exp();r,re=value.rad().man_exp()
    return abs(F(int(m))*F(2)**int(e))-F(int(r))*F(2)**int(re)

def ceil(value):return -((-value.numerator)//value.denominator)
def floor(value):return value.numerator//value.denominator

def cover(response,K,s,progress=None,max_depth=90,max_nodes=50000,interval_encloser=None,enclosure_metadata=None,point_split_width=0):
    started=time.monotonic();s=F(s);h=response.h;edge=F(1,2*h*K-2)
    assert K>=1 and edge>0 and s>0
    stack=[(F(0),edge,'')];nodes=[];splits=0;adjustments=[];last_report=started
    limit=response.compact(arb(0))
    if limit is not None and lower(limit)>0:
        previous=s
        while s>=lower(limit)/2:s/=2
        if s!=previous:adjustments.append(dict(k='limit',old_s=str(previous),new_s=str(s),enclosure=pack(limit)))
    while stack:
        a,b,address=stack.pop();lo=max(K,ceil((1/b+2)/(2*h)));hi=None if not a else floor((1/a+2)/(2*h))
        row=dict(a=str(a),b=str(b),address=address,lower=lo,upper=hi)
        if hi is not None and hi<lo:
            row['status']='empty';nodes.append(row)
        elif hi is not None and hi==lo:
            value=response.compact(ball(mpq(1,2*h*lo-2)))
            assert value is not None and lower(value)>0, ('unresolved_integer',lo,str(value))
            old=s
            while s>=lower(value)/2:s/=2
            if s!=old:adjustments.append(dict(k=lo,old_s=str(old),new_s=str(s),enclosure=pack(value)))
            row.update(status='singleton',k=lo,enclosure=pack(value));nodes.append(row)
        else:
            if hi is not None and hi-lo+1<=point_split_width:
                value=None
            elif interval_encloser is None:
                value=response.compact(ball(mpq(str(a))).union(ball(mpq(str(b)))))
            else:
                value=interval_encloser(a,b)
            if value is not None and lower(value)>s:
                row.update(status='interval',enclosure=pack(value));row.update(enclosure_metadata or {});nodes.append(row)
            else:
                assert len(address)<max_depth and len(nodes)+splits<max_nodes, ('unresolved_interval',address,len(nodes),splits)
                mid=(a+b)/2;stack.extend([(mid,b,address+'1'),(a,mid,address+'0')]);splits+=1
        if time.monotonic()-last_report>45:
            print(json.dumps(dict(time=datetime.now(timezone.utc).isoformat(timespec='seconds'),stage='discrete_cover',leaves=len(nodes),splits=splits,pending=len(stack),s=str(s),elapsed_s=time.monotonic()-started)),flush=True)
            if progress is not None:progress(dict(K=K,h=h,edge=str(edge),s=str(s),nodes=nodes,splits=splits,stack=[(str(a),str(b),q) for a,b,q in stack],adjustments=adjustments))
            last_report=time.monotonic()
    return dict(h=h,K=K,edge=str(edge),s=str(s),nodes=nodes,splits=splits,adjustments=adjustments,actual_elapsed_s=time.monotonic()-started)
