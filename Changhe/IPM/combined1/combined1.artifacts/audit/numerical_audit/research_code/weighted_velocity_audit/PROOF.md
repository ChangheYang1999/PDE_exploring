# Independent S1 weighted velocity certificate

## Statement

Let 0<a<2 and let w(r)>0 be radial. Assume log w(exp(t)) is locally absolutely continuous and p(t)=-(log w(exp(t)))' satisfies 0<=p<=a almost everywhere. In particular w(r)=(1+r²/R²)^(-a/2), for every R>0, satisfies these assumptions. Let H consist of real functions even in x and odd in y with finite norm ||w h||_2. Define U=(-R1R2,R1²) initially on smooth compactly supported S1 functions, with the usual Fourier multipliers Rj=i xi_j/|xi|.

Put K_n=(n+a)/(n-a), n>=2. On sequences indexed by i>=0 define the symmetric tridiagonal matrix M by

    d_0=2, d_i=3+K_(2i)² (i>=1), e_i=M_(i,i+1)=1+K_(2i+2).

Then U extends boundedly to H and

    ||w U[h]||_2 <= sqrt(||M||/8) ||w h||_2.

If a positive sequence v and a number rho satisfy Mv<=rho v componentwise, then the constant sqrt(rho/8) is valid. No square summability of v is required. For the finite rational certificates in the accompanying record, valid constants C at a=6/5,13/10,7/5,3/2,19/10 are respectively 1616466,1836267,2142307,2585263,13806975 divided by 10^6. These are upper bounds, not claimed optimal constants.

## Weighted radial block estimate

Here are the analytic dependencies, included to fix every sign and norm. Let B have Fourier multiplier (xi_1-i xi_2)²/|xi|². Its mode m maps to m-2. Under the isometry F(t)=exp(t) f_m(exp(t)), set n=m-1. For n>0 its block is

    F(t)-2n integral_0^infinity exp(-nv) F(t+v) dv.

For n<0, putting k=-n, it is F(t)-2k integral_0^infinity exp(-kv) F(t-v)dv. The n=0 block is the identity. These formulas follow by solving g'-ng/r=f_m with the decaying endpoint for n>0 and regular endpoint for n<0, then applying g'+ng/r. They are first proved away from the origin on smooth inputs.

Conjugate by w. The future integral H is bounded on L² by 1/(n-a), since w(t)/w(t+v)<=exp(av). It satisfies H'=(n-p)H-F. Therefore F=-H'+(n-p)H and the output G=-H'-(n+p)H. Young's bound and this equation give H in H¹. Since Re integral H' conjugate(H)=0,

    K_n²||F||²-||G||²
      =4na/(n-a)² { ||-H'+(a-p)H||²
                    +(n²-a²)/a integral (a-p)|H|² } >=0.

For the past integral H, the kernel ratio is at most one and H'=F-(k+p)H. Hence F=H'+(k+p)H, G=H'-(k-p)H, and ||F||²-||G||²=4k integral p|H|²>=0. These identities need no derivative of p. They prove the future bound K_n and the past bound one. The approximation and H¹ boundary identity extend them to all weighted L² inputs in each permitted mode.

## S1 angular bookkeeping

Write h=sum_(i>=0) h_i(r) sin((2i+1)theta). Its weighted norm squared is pi sum_i ||g_i||², where g_i(t)=w(exp(t))exp(t)h_i(exp(t)). This follows from real sine orthogonality. In complex modes the coefficients are g_i/(2i_complex) at positive odd indices and their negatives at negative indices. The exact identity U2+iU1=-(I+B)h/2 includes the local term in U2.

The output at positive index 2i+1 has bracket g_i+T_(2i+2)g_(i+1). The output at negative index -(2i+3) has bracket -(g_(i+1)+P_(2i+2)g_i). The output at -1 vanishes because the n=0 block is the identity. The complex Fourier coefficient 1/2, angular integral 2pi, and velocity factor 1/4 give

    ||w U[h]||²
      =pi/8 sum_i {||g_i+T_(2i+2)g_(i+1)||²
                    +||g_(i+1)+P_(2i+2)g_i||²}
      <=pi/8 sum_i {(x_i+K_(2i+2)x_(i+1))²+(x_(i+1)+x_i)²}
      =pi/8 <Mx,x>,

where x_i=||g_i||. This proves both the stated matrix entries and positivity. Its entries are uniformly bounded, so M is bounded. Initially use finite angular sums with smooth radial support away from zero. These are dense in H by radial truncation and angular approximation. The estimate defines the unique bounded extension. This suffices also for singular weights at the origin; no unproved density assertion for nonintegrable weighted constants is needed.

## Infinite certificate and exact arithmetic

For a finitely supported sequence z use

    2|z_i z_j| <= (v_j/v_i)|z_i|²+(v_i/v_j)|z_j|².

Multiplication by each nonnegative M_ij and summation gives |<Mz,z>|<=sum_i ((Mv)_i/v_i)|z_i|²<=rho||z||². Boundedness and density prove ||M||<=rho. In the supplied data v is a list of N=64 positive rationals followed by a positive constant tail. Check rows 0 through N+1 individually. At i>=N+2, all three vector entries are equal and the ratio is

    5+K_(2i)²+K_(2i)+K_(2i+2).

K_n decreases with n because dK_n/dn=-2a/(n-a)²<0. Thus this tail ratio decreases, and its value at N+2 bounds the whole tail. The checker recomputes every rational ratio, its maximum rho, and 8C²-rho>0, independently of the floating procedure that found the vector. It also checks the finite square expansion against the stated tridiagonal matrix.

## Scope

The proof and finite exact certificate supply only a weighted velocity norm. They give no signed-energy bound, high inverse, resolvent estimate, or nonlinear solution. They reproduce the S1 refinement proposed in T1 TP-2 and checked by T4-072. The complete T1 review and T4 arguments are frozen alongside this proof; the independent checker reads certificate data but never runs their programs.
