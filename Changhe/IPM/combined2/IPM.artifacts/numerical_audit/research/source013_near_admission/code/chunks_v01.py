"""Exact partition into bounded groups and complete block summation."""
from fractions import Fraction as F

def partition(indices):
 assert isinstance(indices,list)and indices and all(type(i)is int and i>=0 for i in indices)
 assert indices==sorted(set(indices))
 return[indices[k:k+8]for k in range(0,len(indices),8)]

def sums(rows):
 totals={j:[F(0),F(0)]for j in[4,5,6]}
 for energies in rows:
  assert[row['order']for row in energies]==[4,5,6]
  for row in energies:
   lo,hi=F(row['lower_exact']),F(row['upper_exact']);assert 0<=lo<=hi
   totals[row['order']][0]+=lo;totals[row['order']][1]+=hi
 return[{'order':j,'lower_exact':str(totals[j][0]),'upper_exact':str(totals[j][1])}for j in[4,5,6]]

def assemble(job,rows,identity,owner_total):
 expected=partition(job['indices']);assert len(rows)==len(expected)
 assert[row['chunk']for row in rows]==list(range(len(expected)))
 indices=[]
 for k,row in enumerate(rows):
  assert row['status']=='ADMITTED_NEAR_CHUNK'and row['job']==job['id']and row['chunk']==k
  assert row['indices']==expected[k]and row['identity']==identity
  assert[row2['index']for row2 in row['panels']]==expected[k]
  assert row['all_comparisons_passed']is True and row['precision_bits']==2048
  assert all(p['majorant']['passed']is True for p in row['panels'])
  assert row['laplacian_energies']==sums([p['containing_intersections']for p in row['panels']])
  indices+=row['indices']
 assert indices==job['indices']
 total=sums([row['laplacian_energies']for row in rows]);assert total==owner_total
 return total
