# A finite-order construction of two regular linear Kerr drivers

Venkata Hemanth Athota · 22 November 2026

We construct six rational Ernst perturbation functions for two tidal drivers
through spin squared. They satisfy the linearized equations identically. A
metric reconstruction establishes local horizon and axis smoothness, and a
separated Schwarzschild kernel argument gives uniqueness in a finite-mode class
with the stated growing data, parameter choices and gauge fixed.

The boundary data include spin-linked odd angular terms. Identifying these
solutions with purely electric external tides whose independent magnetic
moments vanish requires a further calibration. This note constructs the linear
fields; it assigns no mixed response coefficient or physical Love number.

## 1. Fixed domain and mathematical normalization

Use $x\ge1$, $-1\le y\le1$, $|\chi|<1$, and a reference scale $M>0$:

```math
k=\sqrt{1-\chi^2},\quad \sigma=Mk,\quad
\alpha=\frac{\chi}{1+k},\quad
\mathcal E_K=1-\frac{2p}{x+p+iqy},\quad p=1/k,\quad q=\chi/k.
```

The sign of the imaginary Ernst potential fixes the twist convention. Reversing
the azimuthal coordinate reverses the metric's signed angular momentum. Here
$M,\chi$ are the fixed reference Kerr labels; no identification of distorted
Komar charges with newly matched physical parameters is needed or asserted.

Let $R_0^2=x^2+y^2-1$, $z_0=xy$, and $H_j=R_0^jP_j(z_0/R_0)$. These are
polynomials, including at $R_0=0$:

```math
H_0=1,\quad H_1=z_0,\quad H_2=(3z_0^2-R_0^2)/2,
```
```math
H_3=(5z_0^3-3z_0R_0^2)/2,\quad
H_4=(35z_0^4-30z_0^2R_0^2+3R_0^4)/8.
```

For each $\ell=2,4$ define an amplitude $\epsilon_\ell$ by the harmonic seed

```math
U=\epsilon_\ell N_\ell k^\ell(H_\ell-1),\qquad
N_2=1/3,\quad N_4=1/105.
```

The factor $k^\ell$ fixes the leading solid harmonic measured in units of $M$.
Subtracting one sets $U(1,\pm1)=0$ at both horizon poles; it is an explicit
constant-potential/time-normalization convention. The constants $N_\ell$
agree with the earlier linear STF Taylor convention, but $\epsilon_\ell$ is
a mathematical seed amplitude that has not been identified with a fully matched
physical tidal moment. The label $\ell$ specifies the zero-spin driver, not
every angular component at nonzero spin.

## 2. Exact map and the six functions

We use the known distorted-Kerr solution-generating map, as recorded in
[Gounis et al., published Eq. (4.1)](https://doi.org/10.1088/1475-7516/2025/03/002)
and the metric in [Abdolrahimi et al., section 2](https://arxiv.org/html/1509.01665v2).
Define

```math
A_\ell=2(x-y)\sum_{j=0}^{\ell-1}H_j,\qquad
B_\ell=2(x+y)\sum_{j=0}^{\ell-1}(-1)^jH_j,
```
```math
a=-\alpha e^{\epsilon_\ell N_\ell k^\ell A_\ell},\quad
b=\alpha e^{\epsilon_\ell N_\ell k^\ell B_\ell},\quad
Z=x(1+ab)+iy(b-a),\quad C_E=1-ab-i(a+b),
```
```math
\mathcal E=e^{2U}\frac{Z-C_E}{Z+C_E}.
```

For zero amplitude this is exactly $\mathcal E_K$. Differentiate in amplitude
at fixed $(x,y,M,\chi)$ and write

```math
h_\ell=\left.\frac{\partial\mathcal E}{\partial\epsilon_\ell}\right|_0
=u_\ell^{(0)}+i\chi v_\ell^{(1)}+\chi^2u_\ell^{(2)}+O(\chi^3).
```

Here all three displayed functions are real. Put
$\Psi=H_\ell-1$, $S=A_\ell+B_\ell$, $T=A_\ell-B_\ell$,
$f=(x-1)/(x+1)$ and $g=[-x(x+1)+2y^2]/(x+1)^3$. Then the closed forms are

```math
u_\ell^{(0)}=2N_\ell f\Psi,
```
```math
v_\ell^{(1)}=N_\ell\frac{4y\Psi+yS-xT}{(x+1)^2},
```
```math
u_\ell^{(2)}=N_\ell\left[
2\Psi g+\frac{-xS+yT}{(x+1)^2}
+\frac{2y(yS-xT)}{(x+1)^3}\right]-\frac\ell2u_\ell^{(0)}.
```

The last term is required by $k^\ell=1-\ell\chi^2/2+O(\chi^4)$.
These finite polynomial formulas specify all six functions without quadratures;
their fully expanded rational forms are saved in [linear-drivers.json](../results/linear-drivers.json).
For example,

```math
u_2^{(0)}=\frac{(x-1)(3x^2y^2-x^2-y^2-1)}{3(x+1)}.
```

Their only radial denominators are powers of $x+1$, so the potentials are smooth
on the closed exterior coordinate domain. Metric regularity requires the
reconstruction in section 4.

## 3. Direct differential-equation check and boundary data

Let $D$ and $B$ be the operators in
[the Ernst equation note](ernst-equation.md#ernst-equation), and set
$t=2y/(x+1)^2$, so $\mathcal E_K=f+i\chi t+\chi^2g+O(\chi^3)$.
Independent substitution checks the three residuals, for each $\ell$:

```math
fDu_0+u_0Df-2B(f,u_0)=0,
```
```math
fDv_1+u_0Dt-2B(f,v_1)-2B(t,u_0)=0,
```
```math
fDu_2+gDu_0+u_2Df+u_0Dg
-2B(f,u_2)-2B(g,u_0)+2B(t,v_1)=0.
```

The real fields are even in $y$, the imaginary field odd. At $x=1$,
$u_\ell^{(0)}=v_\ell^{(1)}=0$, while

```math
u_2^{(2)}=-\frac{(1-y^2)^2}{6},\qquad
u_4^{(2)}=-\frac{(1-y^2)^2(1+y^2)}{210}.
```

**Complete boundary prescription.** For each of the six rational fields, use
polynomial division in $x$ to specify its full nondecaying polynomial part.
These polynomials are saved as `polynomial_boundary_data` in the same record.
They are prescribed formal exterior data, not a claim of asymptotic flatness
for the finite-amplitude exact metric. Fix the rod scale, coordinates, twist
origin, and azimuthal/time conventions. To fix the remaining spin mode, project
$v_\ell^{(1)}$ on $P_1(y)$ using
$\tfrac32\int_{-1}^1yv_\ell^{(1)}dy$ and prescribe its partial-fraction
coefficient of $(x+1)^{-2}$ as $-16/15$ for $\ell=2$ and $-32/735$ for
$\ell=4$. This algebraic residue is not a condition of inner-horizon regularity
and is not claimed to fix a separately matched physical angular momentum.

In particular the leading odd growing term is

```math
v_\ell^{(1)}=-4N_\ell x^{\ell-1}P_{\ell-1}(y)+O(x^{\ell-2}).
```

For $\ell=2$ this includes a rotating-frame type mode; for $\ell=4$ it
includes an odd $\ell=3$ growing sector. Discarding these while leaving the
other coefficients unchanged fails the sourced recursion. A different
prescription with those independent growing modes removed requires a new
solution, including compensating second-spin-order corrections.

## 4. Metric reconstruction and smooth horizon

For this one-driver seed write $c=\epsilon_\ell N_\ell k^\ell$. The second
metric potential reduces to

```math
V=c\sum_{j=0}^{\ell-1}[(-1)^{\ell-j+1}(x+y)-x+y]H_j
+\frac\ell2c^2[H_\ell^2-R_0^2H_{\ell-1}^2].
```

Direct polynomial evaluation gives $V(1,y)=2U(1,y)$ and $V(x,\pm1)=0$.
In the following metric formulas $\mathsf A,\mathsf B,\mathsf C$ differ
from the auxiliary $A_\ell,B_\ell$ above. Put $X=x^2-1$, $Y=1-y^2$ and

```math
\mathsf A=X(1+ab)^2-Y(b-a)^2,\quad
\mathsf B=[x+1+(x-1)ab]^2+[(1+y)a+(1-y)b]^2,
```
```math
\mathsf C=X(1+ab)[b-a-y(a+b)]+Y(b-a)[1+ab+x(1-ab)].
```

The known vacuum metric has
$g_{tt}=-e^{2U}\mathsf A/\mathsf B$,
$g_{t\phi}=(2\sigma\mathsf C+K e^{2U}\mathsf A)/\mathsf B$,
$g_{xx}=\sigma^2\mathsf B e^{-2U+2V}/[(1-\alpha^2)^2X]$,
and $g_{yy}=Xg_{xx}/Y$, with $K=-4\sigma\alpha/(1-\alpha^2)$.
We use that published exact vacuum family as input, and independently verify
the displayed linear Ernst equations and the following regularity identities.
We have not recomputed the full exact metric's Ricci tensor.

The apparent $\mathsf A^{-1}$ in $g_{\phi\phi}$ is removable. Define

```math
\mathsf D=Y[(x+1)^2+ab(x-1)^2]^2
-X[a(1+y)^2-b(1-y)^2]^2.
```

The polynomial identity
$\mathsf B^2XY-4\mathsf C^2=\mathsf A\mathsf D$ yields

```math
g_{\phi\phi}=\frac{\sigma^2e^{-2U}\mathsf D-4\sigma K\mathsf C
-K^2e^{2U}\mathsf A}{\mathsf B},\qquad
\det(g_{t\phi\text{ block}})=-\sigma^2XY.
```

This cancellation handles the stationary-limit surface as well as the horizon.
At $x=1$, let $e=e^{2U(1,y)}>0$. Then
$a=-\alpha/e$, $b=\alpha/e$, and
$\mathsf B_H=4(1+\alpha^2y^2/e^2)>0$. All stationary-block components
are analytic near the horizon. Define the constants

```math
\Omega_H=-\frac{\alpha(1-\alpha^2)}{2\sigma(1+\alpha^2)},\qquad
\Lambda=\frac{4\sigma^2(1+\alpha^2)}{(1-\alpha^2)^2},\qquad b_H=\Lambda/\sigma.
```

The horizon generator $\xi=\partial_t+\Omega_H\partial_\phi$ obeys
$g_{\xi\phi}=g_{\xi\xi}=0$ there, and $g_{yy,H}g_{\phi\phi,H}=\Lambda^2$.
Apply the horizon-penetrating differential transformation

```math
dt=dv-\frac{b_H}{X}dx,\qquad
d\phi=d\varphi-\frac{\Omega_Hb_H}{X}dx.
```

The determinant identity gives
$g_{\xi\xi}=g_{\xi\phi}^2/g_{\phi\phi}-\sigma^2XY/g_{\phi\phi}$.
Since $g_{\xi\phi}=O(X)$, the new radial pole is proportional to

```math
\frac1X\left[Yg_{yy}-\frac{b_H^2\sigma^2Y}{g_{\phi\phi}}\right].
```

Its numerator vanishes at $X=0$ by the horizon area identity, so the pole is
removable analytically. Cross terms are finite for the same reason. The sign
of the transformation selects one of the two horizon-penetrating patches;
time reversal supplies the other. Thus a smooth local Killing-horizon extension
exists, rather than merely a bounded Ernst potential.

On both axes the even seeds give $ab=-\alpha^2$, $V=0$, and the chosen $K$
sets the axial shift to zero. Elementary flatness follows with azimuthal period
$2\pi$. At the horizon corners the two-metric is
$\Lambda[dy^2/F+F d\varphi^2]$, where

```math
F=\frac{(1+\alpha^2)(1-y^2)e}{\alpha^2y^2+e^2}.
```

The pole normalization gives $e(\pm1)=1$, hence $F'(1)=-2$, $F'(-1)=2$.
The same even-axis factors make the horizon-penetrating cross terms smooth in
local polar Cartesian coordinates. On any fixed compact exterior interval,
$\mathsf B$ stays positive for sufficiently small amplitudes, by continuity
from Kerr. No claim about a growing tide at arbitrarily large radius follows.
The patch constants are independent of amplitude in this pole convention and
analytic at $\chi=0$, so amplitude and finite-order spin differentiation preserve
this local smoothness.

## 5. Kernel classification and a restricted uniqueness lemma

In a fixed rod/coordinate gauge, write a Schwarzschild homogeneous perturbation
as $h=u+iv$. The operator splits exactly:

```math
\mathrm{Re}(L_0h)=f^2D(u/f),\qquad
\mathrm{Im}(L_0h)=f(Dv-4\partial_xv).
```

For a finite Legendre expansion, the real radial branches are $fP_j(x)$ and
$fQ_j(x)$. Horizon regularity of a homogeneous real difference in this fixed-rod
gauge requires $u/f$ smooth; the $Q_j$ logarithms are excluded. This condition
does not require the individual sourced $u_\ell^{(2)}$ to vanish at the horizon.
The remaining $P_j$ coefficients are fixed by the
polynomial exterior data, including the constant normalization.

For imaginary modes the radial equation is

```math
(x^2-1)R_j''+(2x-4)R_j'-j(j+1)R_j=0.
```

For $j\ge2$ a basis is $(x-1)^2P_j''(x)$ and $(x-1)^2Q_j''(x)$.
Indeed the radial operator applied to $(x-1)^2F''$ equals $(x-1)^2$
times the second derivative of the Legendre equation for $F$; this is an
identity for arbitrary $F$ and $j$, not an inference from low-mode examples.
The second branch has finite horizon value $1/2$, but derivative
$-j(j+1)/4$. The twist reconstruction, up to its conventional overall sign,
gives

```math
g_{t\phi}=\frac{\sigma(x+1)^2R_j'}{j(j+1)}(1-y^2)P_j'(y).
```

Thus its horizon value requires an angular velocity proportional to $P_j'(y)$.
For $j\ge2$ that is nonconstant and is incompatible with a smooth Killing
horizon generated by a constant combination of the two Killing fields. In a
finite sum these higher polynomials cannot cancel to a constant except by
eliminating their coefficients. The growing $P_j''$ branch is fixed by exterior data.

The exceptional $j=1$ branches are $x-2$ (rotating frame) and $(x+1)^{-2}$
(spin variation); the former is fixed by the growing data, the latter by the
declared residue condition. At $j=0$ there are a twist constant
and $x/(x+1)^2$ (NUT-type) branch. Both are excluded by the imposed odd twist
reflection condition; the twist origin is also fixed explicitly. Variations
of the rod scale and coordinates are outside this fixed-gauge problem.

**Restricted lemma.** In formal series through $\chi^2$ with real-even,
imaginary-odd spin parity, finite angular expansions, the stated horizon/axis
conditions, fixed polynomial exterior data from section 3 and fixed exceptional
modes, the six displayed fields are unique. Proof: subtract two candidates.
Their zero-spin difference lies in the just-classified homogeneous kernel and
vanishes. The difference at order $\chi$ therefore obeys the same homogeneous
equation and vanishes; the difference at order $\chi^2$ does likewise.
Uniqueness depends on the complete boundary data, including the spin-linked
odd growing modes and the exceptional-mode prescription. Infinite angular sums
require separate convergence control, and no convergent all-spin theorem is asserted.

## 6. Verification and related constructions

[verify_linear_drivers.py](../verify_linear_drivers.py) gives 82 exact checks of
the map derivative, six differential equations, parity, horizon values, metric
identities and representative kernel branches. The general kernel and analytic
extension arguments above are proofs with stated assumptions, not consequences
of counting tests. The [saved record](../results/linear-drivers.json) preserves
all six expressions and all their nondecaying boundary polynomials.

[The mixed construction](mixed-construction.md) uses these fields to construct
their driven interaction, with its own mixed-order boundary data and uniqueness
argument. [The radial reduction](radial-response.md) then evaluates a connection
coefficient under a specified subtraction convention. Zero independent magnetic
growing data, a different rotating frame or physical matching would require a
further transformation. In particular, the present $\epsilon_\ell$ family has
not been identified with the external variables in the
[response definition](response-definition.md).
