"""Finite read-only dependency authentication in explicit campaign lanes."""
from pathlib import Path
from hashlib import sha256
import os,re
LANES={'numerical_audit','theory_audit','numerics_agent_1','numerics_agent_2','theory_agent_1','theory_agent_2','coordinator'}
R=Path(__file__).resolve().parents[1];P=R.parent.resolve()
def digest(path):
 h=sha256()
 with path.open('rb')as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def named(base,name):
 q=Path(name);assert isinstance(name,str)and not q.is_absolute()and '..'not in q.parts and str(q)==name and '\\'not in name
 return base/q
class Bindings:
 def __init__(self):self.files={};self.symlinks={};self.checks=0
 def add(self,path,expected=None):
  path=Path(path);lexical=Path(os.path.normpath(str(path)));resolved=path.resolve()
  for q in [lexical,resolved]:assert q.is_relative_to(P)and q.relative_to(P).parts[0]in LANES
  actual=digest(path);assert expected is None or actual==expected
  assert re.fullmatch('[0-9a-f]{64}',actual)
  for q in [lexical,resolved]:
   n=str(q.relative_to(P));assert n not in self.files or self.files[n]==actual;self.files[n]=actual
  if lexical!=resolved:self.symlinks[str(lexical.relative_to(P))]=str(resolved.relative_to(P))
  self.checks+=1;return actual
 def mapping(self,base,mapping):
  assert isinstance(mapping,dict)
  for n,h in mapping.items():
   q=Path(n);assert not q.is_absolute()and str(q)==n and '\\'not in n
   # Parent components may only enter named campaign lanes. Final lexical and resolved boundaries are checked by add.
   if '..'in q.parts:
    parts=q.parts;assert len(parts)>2 and parts[0]=='..'and parts[1]in LANES
    if '..'in parts[2:]:assert len(parts)>4 and parts[2]=='..'and parts[3]in LANES and '..'not in parts[4:]
   self.add(base/q,h)
 def recheck(self):
  for n,h in self.files.items():assert digest(P/n)==h;self.checks+=1
 def own(self):return {n[6:]:h for n,h in sorted(self.files.items())if n.startswith('numerical_audit/')}
 def external(self):return {'../'+n:h for n,h in sorted(self.files.items())if not n.startswith('numerical_audit/')}
