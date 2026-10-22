from pathlib import Path,PurePosixPath
from datetime import datetime,timezone
from collections import Counter
import tarfile,hashlib,json,time,re
V=Path('research/318_finalizer_clock_and_coverage/verification');ROOT=Path('analysis');start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();C=[];archives={}
def ck(n,v,d=None):C.append(dict(name=n,passed=bool(v),detail=d))
class HashReader:
 def __init__(self,f):self.f=f;self.h=hashlib.sha256();self.bytes=0
 def read(self,n=-1):
  b=self.f.read(n);self.h.update(b);self.bytes+=len(b);return b
manifest=(V/'MANIFEST.md').read_text();decl={}
for line in manifest.splitlines():
 parts=[x.strip()for x in line.split('|')]
 if len(parts)>5 and parts[1].startswith('bq3_'):decl[parts[1]]=dict(bytes=int(parts[2]),sha256=parts[3],members=int(parts[4]))
side=json.loads((V/'manifest_members.json').read_text());ck('three_archives',len(decl)==3)
for name,d in decl.items():
 p=ROOT/'artifacts'/name;st0=p.stat();members=[];kinds={};duplicates=[];odd=[]
 with p.open('rb')as raw:
  reader=HashReader(raw)
  with tarfile.open(fileobj=reader,mode='r|gz')as tar:
   for member in tar:
    n=member.name;members.append(n);kinds[n]='file'if member.isfile()else'directory'if member.isdir()else'link'if member.issym()or member.islnk()else'other'
    pp=PurePosixPath(n)
    if pp.is_absolute()or'..'in pp.parts or str(pp)!=n:odd.append(n)
  while reader.read(1<<20):pass
  actualhash=reader.h.hexdigest();nbytes=reader.bytes
 st1=p.stat();duplicate=[k for k,n in Counter(members).items()if n>1]
 ck(name+'_size',nbytes==d['bytes']==st0.st_size,[nbytes,d['bytes'],st0.st_size]);ck(name+'_hash',actualhash==d['sha256'],actualhash);ck(name+'_member_count',len(members)==d['members'],len(members));ck(name+'_sidecar_exact',members==side.get(name));ck(name+'_no_duplicates',not duplicate,duplicate);ck(name+'_relative_normalized_paths',not odd,odd[:10]);ck(name+'_stable_during_read',(st0.st_size,st0.st_mtime_ns,st0.st_ino)==(st1.st_size,st1.st_mtime_ns,st1.st_ino))
 archives[name]=dict(bytes=nbytes,sha256=actualhash,members=members,kinds=kinds,duplicate_names=duplicate,odd_paths=odd,mtime_ns=st1.st_mtime_ns)
 print('ARCHIVE',name,nbytes,actualhash,len(members),'types',dict(Counter(kinds.values())),flush=True)
rows={}
for line in(V/'REGISTRY.md').read_text().splitlines():
 parts=[x.strip()for x in line.split('|')]
 if len(parts)>=4 and re.fullmatch('[APER][0-9]+',parts[1]):
  ck('registry_id_unique',parts[1]not in rows,parts[1]);rows[parts[1]]=(parts[2],parts[3])
text=(V/'actual_report.md').read_text();ids=set(re.findall(r'(?<![A-Za-z0-9_])([APER]\d{2,4})(?![A-Za-z0-9_])',text))-{'R84'};coverage=[]
def lookup(ident,reg=rows,arcdata=archives):
 if ident not in reg:return False,'missing row',[]
 bundle,member=reg[ident];name=f'bq3_{bundle}.tar.gz'
 if name not in arcdata:return False,'missing archive',[]
 kinds=arcdata[name]['kinds'];matches=[n for n,kind in kinds.items()if(n.startswith(member)if member.endswith('/')else n==member)and kind=='file']
 return bool(matches),name,matches
for ident in sorted(ids):
 ok,arc,mat=lookup(ident);ck('cited_regular_member_'+ident,ok,[arc,rows.get(ident)]);coverage.append(dict(identifier=ident,archive=arc,registered=rows.get(ident),regular_matches=len(mat)))
ck('unknown_identifier_detected',lookup('P999')[0]is False)
fake=dict(rows);fake['A171']=('analysis','astra/not_present_A171/')
ck('missing_registered_directory_detected',lookup('A171',reg=fake)[0]is False)
# Current material rather than hypothetical link/path defects.
ck('all_cited_have_regular_evidence',all(x['regular_matches']>0 for x in coverage))
out=dict(started_utc=start,ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-tick,passed=sum(x['passed']for x in C),total=len(C),checks=C,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),archives=archives,cited_identifier_count=len(ids),coverage=coverage,scope='Read-only independent gzip-byte hashing and actual tar-header comparison from the same stream. No extraction or teammate-code execution. Build-time snapshots, not eventual final artifacts.')
(V/'archive_checks.json').write_text(json.dumps(out,indent=2)+'\n');print('RESULT',out['passed'],out['total'],'seconds',out['elapsed_seconds'],'cited',len(ids),flush=True);print('FAILED',[x for x in C if not x['passed']],flush=True)
