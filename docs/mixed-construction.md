# The regular mixed solution through spin squared

Venkata Hemanth Athota · 23 November 2026

**Result.** For the two mathematical drivers in [the linear construction](linear-construction.md),
we construct the coefficient of their product explicitly through spin squared.
It satisfies the three forced Ernst equations identically. The known exact
metric family supplies a smooth local horizon and axis extension. The solution
is unique in the earlier finite-mode, fixed-gauge class when its complete mixed
boundary data are prescribed. It is nonzero, including in its quadrupolar
projection. This is neither a nonzero Love coefficient nor a vanishing theorem.

The construction differentiates a known distorted-Kerr solution. Its exact
family and existence are prior work, recorded in
[Abdolrahimi et al., section 2](https://arxiv.org/html/1509.01665v2#S2) and
[Gounis et al., published Eq. (4.1)](https://doi.org/10.1088/1475-7516/2025/03/002).
The former credits Bretón, Denisova and Manko with the explicit metric.
We give a reproducible specialization and finite-order proof, without a novelty
claim for the family or this differentiation.

## 1. What is being solved

Keep the fixed coordinates, background labels, spin convention and harmonic
polynomials from the linear note. In particular $x\ge1$, $-1\le y\le1$,
$k=\sqrt{1-\chi^2}$, $\sigma=Mk$, $\alpha=\chi/(1+k)$,
$N_2=1/3$, $N_4=1/105$, and $\Psi_\ell=H_\ell-1$.
The amplitudes $\epsilon_\ell$ are mathematical seed parameters, not already
matched physical electric tidal moments.

Introduce both seeds simultaneously:

```math
c_2=\epsilon_2N_2k^2,\qquad c_4=\epsilon_4N_4k^4,\qquad
U=c_2\Psi_2+c_4\Psi_4.
```

Equivalently the constant seed is $c_0=-c_2-c_4$. There is **no independently
added mixed seed** proportional to $\epsilon_2\epsilon_4$. This specifies a
particular nonlinear boundary prescription. The two linear drivers by
themselves do not select all mixed boundary data.

The auxiliary polynomials are

```math
A_\ell=2(x-y)\sum_{j=0}^{\ell-1}H_j,\qquad
B_\ell=2(x+y)\sum_{j=0}^{\ell-1}(-1)^jH_j.
```

Use $a=-\alpha\exp(c_2A_2+c_4A_4)$,
$b=\alpha\exp(c_2B_2+c_4B_4)$ and the same exact map

```math
Z=x(1+ab)+iy(b-a),\quad C_E=1-ab-i(a+b),\quad
\mathcal E=e^{2U}\frac{Z-C_E}{Z+C_E}.
```

Define the mixed coefficient at fixed $(x,y,M,\chi)$ by

```math
w_{24}=\left.\frac{\partial^2\mathcal E}
{\partial\epsilon_2\partial\epsilon_4}\right|_{\epsilon_2=\epsilon_4=0}
=w_0+i\chi w_1+\chi^2w_2+O(\chi^3).
```

The expansion of $\mathcal E$ includes $\epsilon_2\epsilon_4w_{24}$ with
**no factorial**. The functions $w_j$ displayed below are real.

For clarity define the differential operators explicitly:

```math
Dv=\partial_x[(x^2-1)\partial_xv]+\partial_y[(1-y^2)\partial_yv],
```
```math
B(u,v)=(x^2-1)u_xv_x+(1-y^2)u_yv_y.
```

The bilinear form has no complex conjugation. Linearization about $\mathcal E_K$
gives $L_Kv=\mathrm{Re}(\mathcal E_K)Dv+\mathrm{Re}(v)D\mathcal E_K-2B(\mathcal E_K,v)$.
The mixed equation is

```math
L_Kw_{24}=S[h_2,h_4]
=2B(h_2,h_4)-\mathrm{Re}(h_2)Dh_4-\mathrm{Re}(h_4)Dh_2.
```

Its source is fixed by the two already constructed linear fields. This is the
step that an argument excluding a singular homogeneous solution does not supply.

## 2. Three closed-form functions

Put $d=x+1$, $N=N_2N_4=1/315$, and $f=(x-1)/(x+1)$. Direct differentiation gives

```math
w_0=4Nf\Psi_2\Psi_4,
```
```math
w_1=\frac{N}{d^2}\left[
(y-x)(2\Psi_2+A_2)(2\Psi_4+A_4)
+(y+x)(2\Psi_2+B_2)(2\Psi_4+B_4)\right],
```
```math
\begin{aligned}
w_2={N\over2d^3}\big[&
(y+1)(y-x)(2\Psi_2+2A_2)(2\Psi_4+2A_4)\\
&+(y-1)(y+x)(2\Psi_2+2B_2)(2\Psi_4+2B_4)\\
&+2(y^2-x^2)(2\Psi_2+A_2+B_2)(2\Psi_4+A_4+B_4)
\big]-3w_0.
\end{aligned}
```

The last term follows from $c_2c_4=\epsilon_2\epsilon_4N k^6$ and
$k^6=1-3\chi^2+O(\chi^4)$. Dropping it changes the boundary convention
and fails the stated spin-squared equation.

One way to derive these expressions without solving the forced equations is
to set $E_a=\exp(c_2A_2+c_4A_4)$, $E_b=\exp(c_2B_2+c_4B_4)$ and expand the
rational factor of the exact map:

```math
\frac{Z-C_E}{Z+C_E}=f+i\chi
\frac{(y-x)E_a+(y+x)E_b}{d^2}
+\chi^2\frac{(y+1)(y-x)E_a^2+(y-1)(y+x)E_b^2
+2(y^2-x^2)E_aE_b}{2d^3}+O(\chi^3).
```

Multiply by $e^{2U}$, differentiate once in each seed, then include $k^6$.
The script independently checks this map expansion and all three differential
equations; it does not infer the residuals from membership in the exact family.

## 3. Explicit source and direct verification

Write $h_2=u+i\chi v+\chi^2z$ and $h_4=\widetilde u+i\chi\widetilde v+
\chi^2\widetilde z$ at the retained orders. Then $S=S_0+i\chi S_1+\chi^2S_2$,
where

```math
S_0=2B(u,\widetilde u)-uD\widetilde u-\widetilde uDu,
```
```math
S_1=2B(u,\widetilde v)+2B(v,\widetilde u)-uD\widetilde v-\widetilde uDv,
```
```math
\begin{aligned}
S_2={}&2B(u,\widetilde z)+2B(z,\widetilde u)-2B(v,\widetilde v)\\
&-uD\widetilde z-zD\widetilde u-\widetilde uDz-\widetilde zDu.
\end{aligned}
```

Set $t=2y/d^2$, $g=[-x(x+1)+2y^2]/d^3$, so $\mathcal E_K=f+i\chi t+\chi^2g+
O(\chi^3)$. Exact substitution establishes

```math
fDw_0+w_0Df-2B(f,w_0)=S_0,
```
```math
fDw_1+w_0Dt-2B(f,w_1)-2B(t,w_0)=S_1,
```
```math
fDw_2+gDw_0+w_2Df+w_0Dg-2B(f,w_2)-2B(g,w_0)+2B(t,w_1)=S_2.
```

These are polynomial/rational identities throughout the coordinate domain,
not checks at selected radii. The [saved record](../results/mixed-solution.json)
contains factored sources, fields, every angular projection, and exterior data.
The angular sectors are $0,2,4,6$ for $w_0$, $1,3,5,7$ for $w_1$, and
$0,2,4,6,8$ for $w_2$. The static identity $w_0=u_2^{(0)}u_4^{(0)}/f$
is a useful control: the static Ernst potential is exponential in the harmonic seed.

## 4. Boundary data and regularity

For each $w_j$, prescribe the complete polynomial quotient obtained by division
in $x$, including all constant and nondecaying terms. These are the
`polynomial_boundary_data` in the saved record. They are formal exterior data;
the finite-amplitude growing field is not assumed asymptotically flat.
Fix the rod scale, coordinates, time/azimuth normalization, and twist origin as
in the linear construction. To fix the remaining spin variation prescribe
the coefficient of $(x+1)^{-2}$ in the $P_1(y)$ projection of $w_1$ as
$1024/33075$. The full projection is

```math
\begin{aligned}
\frac32\int_{-1}^{1}yw_1\,dy={}&
-\frac{8x^5}{1225}+\frac{208x^4}{11025}-\frac{272x^3}{6615}
+\frac{1888x^2}{33075}-\frac{344x}{33075}-\frac{208}{3675}\\
&+\frac{2048}{33075(x+1)}+\frac{1024}{33075(x+1)^2}.
\end{aligned}
```

This is an algebraic normalization of an exceptional homogeneous mode, not an
inner-horizon condition or a separately matched angular momentum. The chosen
data retain the spin-linked odd sectors of the original construction.

The rational potentials have only powers of $x+1$ in their denominators. At the
outer horizon,

```math
w_0(1,y)=w_1(1,y)=0,\qquad
w_2(1,y)=-\frac{(1-y^2)^3(1+y^2)}{315}.
```

For a metric proof, the exact two-seed potential $V$ contains the one-seed
linear and quadratic terms from the linear note, plus

```math
V_{24}=\frac83c_2c_4[H_2H_4-R_0^2H_1H_3].
```

The factor $8/3$ includes both ordered pairs in the published double sum.
This cross term vanishes at $x=1$ and $y=\pm1$, so $V_H=2U_H$ and
$V_{\rm axis}=0$ still hold. Also $U(1,\pm1)=0$, and the even seed exponents
still give $a_H=-\alpha e^{-2U_H}$, $b_H=\alpha e^{-2U_H}$ and
$ab=-\alpha^2$ on both axes.

Consequently all the amplitude-independent horizon chart constants,
stationary-block cancellation, radial-pole cancellation, and elementary-flatness
identities in [section 4 of the linear note](linear-construction.md#4-metric-reconstruction-and-smooth-horizon)
continue to apply. On each fixed compact exterior region the remaining metric
denominator stays positive for sufficiently small amplitudes by continuity
from Kerr. The reconstructed metric is jointly smooth in the amplitudes and
analytic at zero spin in those common horizon and axis charts. Taking its mixed
derivative and finite spin coefficients preserves smoothness.

This statement concerns the **mixed metric**, including quadratic products of
the first-order fields in metric reconstruction. A bounded $w_{24}$ alone would
not prove it. The vacuum property of the full exact family is a cited input;
we independently verify the mixed Ernst equations and the additional $V$
identities. We do not claim a new full Ricci-tensor calculation, a global
exterior completion, uniformity to infinite radius, or an extremal limit.

## 5. Restricted uniqueness

Consider two formal solutions with the same $h_2,h_4$, the mixed polynomial
data above, the same spin residue, the earlier parity and fixed-gauge
conventions, finite angular expansions, and smooth reconstructed Killing
horizons and axes in a common chart. Their difference has zero mixed source.
The quadratic products of the common linear fields cancel in their metric
difference as well.

At spin zero, that difference obeys the real Schwarzschild homogeneous equation.
The [earlier kernel classification](linear-construction.md#5-kernel-classification-and-a-restricted-uniqueness-lemma)
excludes the $fQ_j$ branch by smoothness of the homogeneous difference divided
by $f$, while zero polynomial data eliminate the $fP_j$ branch. The spin-zero
difference is therefore zero. At first spin order the remaining difference
obeys the imaginary Schwarzschild equation: horizon regularity excludes the
higher decaying branches, exterior data eliminate the growing branches, and
the residue fixes the exceptional spin mode. At spin squared the lower
differences have vanished, so the real argument applies again.

Thus the three mixed coefficients are unique **for these complete data and
this class**. This does not prove that horizon regularity and the two linear
fields alone determine the mixed exterior data. Infinite angular sums or a
convergent all-spin series need additional analysis.

## 6. The quadrupolar tail and what it does not mean

Define a coordinate projection
$\Pi_2(F)(x)=\tfrac52\int_{-1}^{1}P_2(y)F(x,y)dy$.
One result is particularly transparent:

```math
\Pi_2[w_0]=\frac{8(x-1)(3x^2-1)(x^4-5)}{6615(x+1)}.
```

Its polynomial quotient leaves $128/[6615(x+1)]$, hence a nonzero $x^{-3}$
term at large $x$. The spin-squared projection is also recorded exactly.

| Coordinate quantity | Raw coefficient of $x^{-3}$ |
|---|---:|
| $\Pi_2[w_0]$ | $128/6615$ |
| $\Pi_2[w_2]$ | $112192/218295$ |

These are coefficients of the full sourced potential in the fixed prolate
coordinates, not amplitudes of independently added homogeneous $Q_2$ solutions.
The elementary static example already produces a tail by expanding an
exponential of regular applied seeds. Polynomial division defines a useful
mathematical split, but its decaying remainder generally does not solve the
homogeneous field equation.

Physically, the two applied patterns interact and change the geometry. The
computed mixed field describes that change for the chosen data. A further
quantity called an independent response requires a specified rule separating
the forced contribution from any additional response. A mathematical version
of that rule also needs a reference solution or boundary functional; naming
every decaying term a response does not supply one.

## 7. Evidence and next step

[verify_mixed_solution.py](../verify_mixed_solution.py) supplies 36 exact checks:
the rational map expansion and amplitude derivatives, all three forced
equations, parity, boundary splits, angular reconstructions, horizon values,
the additional metric-potential identities and the declared spin residue.
An independent AI-assisted derivation agreed with the fields, equations,
residue and quadrupolar projections; this is not scientific peer review.
The older 181 checks/components remain unchanged, giving 217 in total.

We have now constructed both the inputs and their regular driven interaction
for one fully specified mathematical problem. The next step is to isolate the
quadrupolar radial problem and define a response functional independently of
the answer. Its subtraction convention and allowed changes of normalization
must be stated before testing a vanishing claim. Choosing the present solution
as its own reference and declaring the residual zero would be circular.
Physical calibration and matching remain a later, distinct interpretation.
