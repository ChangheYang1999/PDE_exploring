"""Own finite diff, table, manifest and receipt audit. Peer code is inert."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,os,re,time
R=Path(__file__).resolve().parents[3]; B=R/'research/final_report_diff'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb')as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
def read(p):return json.loads(p.read_text())
def rows(text,columns,anchor=None):
 out={};active=anchor is None
 for line_no,line in enumerate(text.splitlines(),1):
  if anchor and anchor in line:active=True;continue
  if not active:continue
  if anchor and out and not line.startswith('|'):break
  cells=[x.strip()for x in re.split(r'(?<!\\)\|',line)[1:-1]]
  if len(cells)!=columns or not re.fullmatch(r'\d+(?:-\d+)?',cells[0]):continue
  ids=list(map(int,cells[0].split('-')))
  for n in range(ids[0],ids[-1]+1):assert n not in out;out[n]={'line':line_no,'cells':cells}
 return out

def main():
 assert os.sched_getaffinity(0)=={57} and os.getpriority(os.PRIO_PROCESS,0)==19
 begin=datetime.now(timezone.utc).isoformat();tick=time.monotonic();target=B/'verification/result.json';assert not target.exists();checks=[];external={}
 def ck(value,label):checks.append({'check':label,'pass':bool(value)});assert value,label
 m=read(B/'verification/PROOF_FIRST.json');ck(not m['checker_exists'] and not m['result_exists'],'proof precedes checker')
 for marker in ['PARSER_FIRST_v02.json','SECOND_ALIAS_FIRST_v02.json']:
  extra=read(B/'verification'/marker);ck(not extra['checker_v02_exists'],'repair proof precedes code '+marker);m['inputs'].update(extra['inputs']);m['inputs'][str((B/'verification'/marker).relative_to(R))]=sha(B/'verification'/marker)
 for rel,h in m['inputs'].items():ck(sha(R/rel)==h,'local input '+rel)
 old=(R/'research/final_report_numerical/source/report_v01.md').read_text();new=(B/'source/report1900.md').read_text();repro=(B/'source/reproduce1900.md').read_text()
 ck(sha(B/'source/report1900.md')=='ff680b749d855f1c28dfdea1eff56455ca3ded98643838a8c26e3e8dfd57af21','nominated1900report')
 ck(sha(B/'source/report.diff')=='32240684cb3f069b2a8bcbc9b3bdfb8162a932f5206f402e32f67a8498f592f7','nominatedreportdiff')
 ck(sha(B/'source/matrix180.md')=='51bad26ba717650b02322449fc1c9be447167a9913651c706522387b8f34c581','nominatedmatrix180')
 def applydiff(oldtext,newtext,diff,name):
  src=oldtext.splitlines(keepends=True);ds=diff.splitlines(keepends=True);dst=[];at=0;i=2;hunks=[]
  ck(ds[0].startswith('--- ')and ds[1].startswith('+++ '),name+' diff headers')
  while i<len(ds):
   z=re.fullmatch(r'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@[^\n]*\n',ds[i]);ck(z is not None,name+' hunk header '+str(i));a,an,b,bn=[int(x)if x is not None else 1 for x in z.groups()];i+=1;ck(at<=a-1,name+' ordered hunk '+str(a));dst.extend(src[at:a-1]);at=a-1;ck(len(dst)==b-1,name+' new line offset '+str(b));oc=nc=0
   while i<len(ds)and not ds[i].startswith('@@ '):
    op,s=ds[i][0],ds[i][1:];ck(op in ' +- ',name+' valid op '+str(i))
    if op in ' -':ck(at<len(src)and src[at]==s,name+' exact old line '+str(at+1));at+=1;oc+=1
    if op in ' +':dst.append(s);nc+=1
    i+=1
   ck((oc,nc)==(an,bn),name+' hunk lengths '+str(a));hunks.append([a,an,b,bn])
  dst.extend(src[at:]);ck(''.join(dst)==newtext,name+' exact reconstructed output');return hunks
 report_hunks=applydiff(old,new,(B/'source/report.diff').read_text(),'report');repro_hunks=applydiff((B/'source/reproduce1837.md').read_text(),repro,(B/'source/reproduce.diff').read_text(),'reproduce');ck(len(report_hunks)==18,'18reporthunks');ck(len(new.splitlines())==2952,'2952reportlines')
 a=rows(old,8,'| # | framework | candidate |');z=rows(new,8,'| # | framework | candidate |');mat=rows((B/'source/matrix180.md').read_text(),11);ck(set(a)==set(z)==set(mat)==set(range(1,109)),'108tableandmatrixIDs');changed=[]
 def lab(s):
  labels=['RULED OUT','OPEN','PROVED','CONDITIONAL','FLOAT','REFUTED','CONFIRMED','AUDITED','CLAIMED'];return min((s.upper().find(x),x)for x in labels if x in s.upper())[1]
 def candidates(s):
  s=s.split('(')[0];s=s.replace('tail repair R = 2^1024','C1-A2-TAILREP').replace('m10 algebraic repairs','C1-A2-m10 algebraic repairs') if not s.startswith('C1-A2-m10') else s;s=re.sub(r'(?<![\w-])(d2|Mpen2|b6)(?![\w-])',r'C1-A2-\1',s);return set(re.findall(r'C1-(?:N1-\d{3}|A2-[\w]+|BASE-S131)',s))
 for n in sorted(z):
  aa,zz,mm=a[n]['cells'],z[n]['cells'],mat[n]['cells'];ck(aa[0:4]==zz[0:4]and aa[5:]==zz[5:],'row'+str(n)+' unchanged non-residual cells');ck(aa[2]==zz[2]and aa[-1]==zz[-1],'row'+str(n)+' same candidate and verdict')
  if aa[5]!=zz[5]:changed.append({'row':n,'cell':5,'before':aa[5],'after':zz[5]})
  ck(lab(zz[-1])==lab(mm[-1]),'row'+str(n)+' matrix status');left,right=candidates(mm[2]),candidates(zz[2]);ck(left<=right if n in [12,13,14]else left==right,'row'+str(n)+' matrix candidate IDs')
 # Table residual is column4, while the lone revision changes its precision citation.
 ck(not changed,'no threshold cell changes')
 actual_changed=[{'row':n,'column':j,'before':a[n]['cells'][j],'after':z[n]['cells'][j]}for n in z for j in range(8)if a[n]['cells'][j]!=z[n]['cells'][j]]
 ck(len(actual_changed)==1 and actual_changed[0]['row']==80 and actual_changed[0]['column']==4,'onlyrow80residualcitationchanges');ck('T4-488'in actual_changed[0]['after'],'row80strongprecisioncitation')
 compact=' '.join(new.split());ck(compact.count('E_star^2=P2^2+2^14 G1^2+2^18 G0^2')==2,'bothenergycoefficientrepairs');ck(compact.count('the weighted G1 term contributes about 72 percent')==2,'bothG1shareattributions');ck('residual value or bound'in new and'| residual LB | threshold | ratio | status |'not in new,'repairedheading');ck('are rounded summaries of their cited certificates and are not directed bounds'in compact,'explicitroundedsummaryscope');ck('Ratios use the exact underlying bounds and thresholds'in compact,'exactratioinputs')
 def manifest(name,root,inventory_root,expected,extra):
  pairs=[]
  for line in (B/'source'/name).read_text().splitlines():
   q=re.fullmatch(r'([0-9a-f]{64})  (.+)',line);ck(q is not None,name+' valid entry');h,rel=q.groups();p=root/rel;ck(not Path(rel).is_absolute()and p.resolve().is_relative_to(root.resolve()),name+' contained '+rel);pairs.append((rel,h,p))
  ck(len(pairs)==expected and len({x[0]for x in pairs})==expected,name+' exact unique count');observed=[]
  for rel,h,p in pairs:
   ck(p.is_file()and not p.is_symlink(),name+' regular '+rel);before=p.stat();actual=sha(p);after=p.stat();ck((before.st_ino,before.st_size,before.st_mtime_ns)==(after.st_ino,after.st_size,after.st_mtime_ns),name+' stable read '+rel);ck(actual==h,name+' current hash '+rel);external[str(p)]={'sha256':actual,'bytes':after.st_size,'mtime_ns':after.st_mtime_ns};observed.append({'path':rel,'sha256':actual,'bytes':after.st_size,'mtime_ns':after.st_mtime_ns})
  inventory=[]
  for directory,dirs,files in os.walk(inventory_root):
   ck(not any((Path(directory)/x).is_symlink()for x in dirs),name+' no directory symlink '+str(Path(directory).relative_to(root)))
   inventory.extend(str((Path(directory)/f).relative_to(root))for f in files)
  ck(set(inventory)=={x[0]for x in pairs}|set(extra),name+' full current inventory');return {'entries':len(pairs),'file_count':len(inventory),'additional_files':extra,'files':observed}
 snapshots=manifest('snapshot_manifest.sha256',R.parent/'c1-shared',R.parent/'c1-shared/candidate_snapshots',157,[]);artifact=manifest('N1_artifacts_SHA256SUMS',R.parent/'c1-n1/artifacts',R.parent/'c1-n1/artifacts',581,['SHA256SUMS']);ck(artifact['file_count']==582,'582artifactfilesincludingmanifest')
 ids={int(re.search(r'/C1-N1-(\d{3})-',x['path'])[1])for x in snapshots['files']if'/C1-N1-'in x['path']};ck(ids==set(range(1,29)),'28candidateIDs001to028');newest=max(x['mtime_ns']for x in snapshots['files']);stamp=datetime.fromtimestamp(newest/1e9,timezone.utc);ck(stamp.strftime('%Y-%m-%dT%H:%M:%S')<='2026-10-29T15:24:01','snapshotmtimeatwhole-secondprecision')
 for fn,wanted in [('candidate007_exact.json','ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21'),('snapshot_manifest.sha256','a08248330fb4f61b0dece8c40987440a9824d68f3e98ff0a1c742b7606fe6c4d')]:ck(sha(B/'source'/fn)==wanted and wanted in new,'section8hash '+fn)
 ck(next(x['sha256']for x in snapshots['files']if x['path'].endswith('d2w_j7_n4_E2bal_mid180_exact.json'))==sha(B/'source/candidate007_exact.json'),'007copyequalscurrentfrozeninput')
 ck(sha(R.parent/'c1-n1/artifacts/SHA256SUMS')==sha(B/'source/N1_artifacts_SHA256SUMS'),'artifactmanifestcopyequalscurrent');ck(sha(R.parent/'c1-coord/coordination/frozen/candidate_snapshots_H22_manifest.sha256')==sha(B/'source/snapshot_manifest.sha256'),'snapshotmanifestcopyequalscurrent')
 t4=read(B/'source/T4_validation_v06.json');ck(t4['check_count']==len(t4['checks'])==4608 and t4['failures']==[],'T4receipt4608stringszeroerrors');ck(t4['unique_files_hashed']==900,'T4receipt900filesnotfreshrehashed');ck(t4['checker_sha256']==sha(B/'source/T4_validate_v02.py'),'T4receiptcheckerhash');ck(t4['postfreeze_map_sha256']==sha(B/'source/T4_addenda_evidence.json'),'T4receiptaddendamap');ck(read(B/'source/T4_addenda_evidence.json')['addenda_snapshot']['sha256']==sha(B/'source/T4_addenda_through510.md'),'T4immutablethrough510snapshot')
 n4=read(R/'research/final_evidence_integrity/verification/result_v03.json');ck(n4['selection_count']==49 and len(n4['roots'])==49,'N4435selected49roots');ck(n4['direct_edge_count']==7497 and n4['unique_resolved_files']==1924 and not n4['errors'],'N4435saved7497edges1924files');ck(len(n4['external_provenance_not_rehashed'])==245,'N4435saved245externalnotrehashed');ck(sha(R/'research/final_evidence_integrity/code/check_v04.py')=='efbcc30dc31dcbd52893c0cbe14feff674b2963d61892a37db87176e552ba2ac','N4435actualworkingchecker')
 receipt=read(R/'research/theory_final_rerun_receipt/verification/result.json');ck(receipt['counts']=={'byte_identical':51,'rc_trailer_only':3,'timing_only':15}and receipt['saved_log_rc0']==69,'T1savedreceipt51plus15plus3')
 lines=new.splitlines();rlines=repro.splitlines();findings=[]
 def issue(tag,line,kind,current,repair):findings.append({'id':tag,'document':'report1900.md','line':line,'kind':kind,'literal':lines[line-1],'finding':current,'repair':repair})
 n=next(i for i,s in enumerate(lines,1)if 'c62e02da'in s);ck(n==1196,'staleN4hashline1196');issue('F1',n,'required documentation repair','Named current frozen numerical audit has sha256 '+sha(R/'FINAL_REPORT_NUMERICAL_AUDIT.md')+', rather than c62e02da.','Use 18:54:37Z, 15dec905...; file frozen18:56:58Z.')
 ck('clock stamps'in lines[2947]and 'rc=0'not in' '.join(lines[2946:2948]),'reruncaptionomits3trailers');issue('F2',2947,'required documentation repair','T1 output comparison also allows three final rc=0 trailers, independently checked by N4-442.','Say51byte-identical,15timing-only,3rc-trailer-only; execution was by T1, receipt comparisons by N4-442/T4-511.')
 n=next(i for i,s in enumerate(lines,1)if '91334e80'in s);current=sha(R.parent/'c1-t4/FINAL_ADDENDA.md');external[str(R.parent/'c1-t4/FINAL_ADDENDA.md')]={'sha256':current,'scope':'current mutable-document digest only'};issue('F3',n,'historical-hash clarification','The live addenda file has subsequently grown; the immutable through510snapshot retains sha256387c487f....','Label91334e80as a historical live-file hash, or cite only FINAL_ADDENDA_through510.md387c487f... for frozen content.')
 n=next(i for i,s in enumerate(rlines,1)if 'N4-438'in s and '(N4-origin)'in s);findings.append({'id':'F4','document':'reproduce1900.md','line':n,'kind':'optional chronology clarification','literal':rlines[n-1],'finding':'N4-origin describes the initial computation; later independent acceptance is already recorded two rows below.','repair':'Append now independently confirmed by T4-509/N4-440 to avoid reading the historical row as current unreviewed status.'})
 inputs=dict(m['inputs']);inputs.update({str(p.relative_to(R)):sha(p)for p in [Path(__file__),B/'verification/PROOF_FIRST.json']});result={'utc':datetime.now(timezone.utc).isoformat(),'started_utc':begin,'inputs':inputs,'checks':checks,'check_count':len(checks),'report_hunks':report_hunks,'reproduce_hunks':repro_hunks,'row_count':108,'changed_table_cells':actual_changed,'snapshots':snapshots,'artifacts':artifact,'snapshot_latest_metadata_utc':stamp.isoformat(),'external_current_readonly_hashes':external,'external_readonly_hash_count':len(external),'receipt_counts_only':{'T4':{'checks':4608,'files':900},'N4_435':{'roots':49,'edges':7497,'files':1924,'external_not_rehashed':245}},'findings':findings,'verdict':'CONFIRMED scoped repairs, table preservation and current manifests; required literal documentation repairs F1/F2','candidate_verdict_changes':False,'peer_code_executed':False,'new_numerical_integration':False,'elapsed_seconds':time.monotonic()-tick}
 with target.open('x')as f:json.dump(result,f,indent=2);f.write('\n')
 print(result['utc'],len(checks),'checks',len(inputs),'local bindings',len(external),'external hashes',sha(target),result['elapsed_seconds']);print([(x['id'],x['line'],x['kind'])for x in findings])
if __name__=='__main__':main()
