from pathlib import Path
from html.parser import HTMLParser
from datetime import datetime,timezone
import re,json,xml.etree.ElementTree as E
class Text(HTMLParser):
 def __init__(self):super().__init__();self.words=[];self.skip=0
 def handle_starttag(self,t,attrs):
  if t in ['script','style']:self.skip+=1
 def handle_endtag(self,t):
  if t in ['script','style']:self.skip=max(0,self.skip-1)
 def handle_data(self,s):
  if not self.skip:self.words.append(s)
def txt(raw):
 p=Text();p.feed(raw);return ' '.join(' '.join(p.words).split())
v=Path('research/193_recent_literature_search/verification')
raw=(v/'arxiv_Boussinesq_recent.txt').read_text();blocks=re.findall(r'<li class="arxiv-result">(.*?)</li>',raw,re.S);assert len(blocks)==50
out=[]
for b in blocks:
 ident=re.search(r'arxiv.org/abs/([\d.]+)',b).group(1)
 title=txt(re.search(r'<p class="title is-5 mathjax">(.*?)</p>',b,re.S).group(1))
 abstract=txt(re.search(r'<span class="abstract-full.*?>(.*?)</span>',b,re.S).group(1)) if 'abstract-full' in b else ''
 # Get complete text separately, since nested spans may delimit the abbreviated extractor.
 out.append({'id':ident,'title':title,'text':txt(b),'abstract_extract_may_end_at_nested_span':abstract})
(v/'search_entries.json').write_text(json.dumps(out,indent=2)+'\n')
raw=(v/'arxiv_math_AP_new.txt').read_text();blocks=re.findall(r'<dt>(.*?)</dt>\s*<dd>(.*?)</dd>',raw,re.S);assert len(blocks)==91,len(blocks)
daily=[]
for dt,dd in blocks:
 ident=re.search(r'/abs/([\d.]+)',dt).group(1)
 title=txt(re.search(r"<div class='list-title mathjax'>(.*?)</div>",dd,re.S).group(1)).removeprefix('Title:').strip()
 daily.append({'id':ident,'title':title,'text':txt(dd)})
(v/'daily_entries.json').write_text(json.dumps(daily,indent=2)+'\n')
for name in ['arxiv_math_AP_new','arxiv_Boussinesq_recent']:(v/(name+'_visible.txt')).write_text(txt((v/(name+'.txt')).read_text())+'\n')
relevant=[x for x in daily if any(w in x['text'].lower() for w in ['boussinesq','self-similar','inviscid primitive'])]
print(json.dumps({'search_entries':len(out),'daily_entries':len(daily),'daily_screened':relevant,'first_search_entries':[{'id':x['id'],'title':x['title']} for x in out[:6]]},indent=2))
