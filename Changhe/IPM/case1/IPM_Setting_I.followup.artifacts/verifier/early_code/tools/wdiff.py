"""Word-level diff of two markdown files after whitespace normalization; prints changed word runs with context."""
import sys, difflib, re
a = open(sys.argv[1]).read().split()
b = open(sys.argv[2]).read().split()
ctx = int(sys.argv[3]) if len(sys.argv) > 3 else 12
sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag == 'equal':
        continue
    pre = ' '.join(a[max(0, i1-ctx):i1])
    post = ' '.join(a[i2:i2+ctx])
    print('=' * 20, tag)
    print('CTX: ...', pre)
    if i2 > i1:
        print('[-', ' '.join(a[i1:i2]), '-]')
    if j2 > j1:
        print('[+', ' '.join(b[j1:j2]), '+]')
    print('POST:', post, '...')
