#!/usr/bin/env python3
"""Arb certificate for C_N=||B^(1/2) A B^(1/2)|| from finite matrices.

A and B are real symmetric interval matrices.  A numerical rotation is used
only as an exact rational change of coordinates, checked a posteriori.
"""
import json
from fractions import Fraction
from flint import arb,ctx
import numpy as np


def row_bound(M):return max(sum((abs(x) for x in row),arb(0)).upper() for row in M)
def transpose(M):return [list(row) for row in zip(*M)]
def matmul(A,B):return [[sum((a*b for a,b in zip(row,col)),arb(0)) for col in zip(*B)] for row in A]
def packet(v):return {'ball':v.str(70),'midpoint':str(v.mid()),'radius':str(v.rad())}

def cholesky(B):
 n=len(B);L=[[arb(0) for j in range(n)] for i in range(n)]
 for i in range(n):
  for j in range(i+1):
   s=B[i][j]-sum((L[i][k]*L[j][k] for k in range(j)),arb(0))
   if i==j:
    if not s>0:raise ValueError(f'Positive pivot not proved at {i}: {s}')
    L[i][j]=s.sqrt()
   else:L[i][j]=s/L[j][j]
 return L

def exact_float(x):
 n,d=float(x).as_integer_ratio();return arb(n)/d

def symmetric_norm_bound(C,rotate=True):
 n=len(C)
 if not rotate:return {'operator_norm_upper':str(row_bound(C)),'method':'Arb absolute row sum'}
 mids=np.array([[float(x.mid()) for x in row] for row in C])
 _,V=np.linalg.eigh((mids+mids.T)/2)
 Q=[[exact_float(V[i,j]) for j in range(n)] for i in range(n)]
 Qt=transpose(Q);G=matmul(Qt,Q)
 defects=[[G[i][j]-(1 if i==j else 0) for j in range(n)] for i in range(n)]
 defect=row_bound(defects)
 if not defect<1:raise ValueError('Rotation invertibility not certified')
 D=matmul(matmul(Qt,C),Q)
 upper=row_bound(D)/(1-defect)
 return {'operator_norm_upper':str(upper.upper()),'rotation_gram_defect_upper':str(defect),'rotated_row_sum_upper':str(row_bound(D)),'method':'Exact binary-rational numerical rotation, Arb Gram and Gershgorin/row-sum enclosure'}

def certify(A,B,bits=256):
 ctx.prec=bits
 n=len(A);assert len(B)==n and all(len(row)==n for row in A+B)
 for X in [A,B]:
  for i in range(n):
   for j in range(n):
    if not (X[i][j]-X[j][i]).contains(0):raise ValueError('Matrix intervals inconsistent with symmetry')
 L=cholesky(B)
 C=matmul(matmul(transpose(L),A),L)
 result=symmetric_norm_bound(C)
 result.update({'status':'RIGOROUS_CONDITIONAL_ON_INPUT_MATRIX_ENCLOSURES','dimension':n,'bits':bits,'A_norm_bound':symmetric_norm_bound(A),'B_norm_bound':symmetric_norm_bound(B)})
 return result


if __name__=='__main__':
 ctx.prec=256
 A=[[arb(2),arb(1)],[arb(1),arb(-3)]];B=[[arb(4),arb(0)],[arb(0),arb(9)]]
 print(json.dumps(certify(A,B),indent=2))
