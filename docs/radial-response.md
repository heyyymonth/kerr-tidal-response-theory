# A quadrupolar connection coefficient with a fixed subtraction

Venkata Hemanth Athota · 24 November 2026

We reduce the constructed mixed field to a forced quadrupolar
Legendre equation and define a source-subtracted connection coefficient without
using the regular solution as its own reference. In the finite-part convention
specified below, its static value is zero and its spin-squared value is

```math
b^{(0)}=0,\qquad b^{(2)}=-\frac{16172}{218295}.
```

The same value follows from the source and horizon smoothness alone. It depends
on the subtraction: an alternative defined below changes the coefficient while
preserving the homogeneous normalization. Thus it does not settle the original
independently matched vanishing conjecture or define a convention-independent
response or physical Love coefficient.

## 1. Isolating the radial problem

Use the coordinates, amplitudes and complete boundary data of
[the mixed construction](mixed-construction.md). Write
$w_{24}=w_0+i\chi w_1+\chi^2w_2+O(\chi^3)$ and let
$\Pi_2(F)(x)=\tfrac52\int_{-1}^{1}P_2(y)F(x,y)dy$.
Set

```math
f=\frac{x-1}{x+1},\quad X=x^2-1,\quad
R_j=\frac{\Pi_2(w_j)}{f},\qquad j=0,2.
```

The real Schwarzschild operator satisfies
$L_0(fR_jP_2(y))=f^2P_2(y)\mathcal L_2R_j$, with

```math
\mathcal L_2R=(XR')'-6R.
```

All spin mixing is moved into the known source. Using the mixed note's $D,B$
and source coefficients $S_0,S_2$, define

```math
F_0=\frac{\Pi_2(S_0)}{f^2},
```
```math
F_2=\frac{\Pi_2\left(S_2-gDw_0-w_0Dg+2B(g,w_0)-2B(t,w_1)\right)}{f^2},
```

where $t=2y/(x+1)^2$ and $g=[-x(x+1)+2y^2]/(x+1)^3$. Then

```math
\mathcal L_2R_0=F_0,\qquad \mathcal L_2R_2=F_2.
```

The spin-squared source uses the two linear drivers and the already fixed
$w_0,w_1$, not the target $w_2$. Other angular sectors contribute through those
lower-order fields; they have not been discarded before projecting.

For example the static reduction is

```math
R_0=\frac{8(3x^2-1)(x^4-5)}{6615},\qquad
F_0=\frac{32x^6}{245}-\frac{832x^4}{6615}+\frac{32x^2}{2205}.
```

The spin-squared source is explicitly

```math
\begin{aligned}
F_2={}&-\frac{96x^6}{245}-\frac{64x^5}{735}-\frac{64x^4}{2205}
+\frac{6368x^3}{24255}+\frac{32x^2}{105}
-\frac{24224x}{31185}+\frac{20224}{43659}\\
&+\frac{1024}{8085(x+1)}+\frac{256}{4851(x+1)^2}
+\frac{512}{24255(x+1)^3}
-\frac{2176}{72765(x-1)}+\frac{2176}{218295(x-1)^2}.
\end{aligned}
```

Both equations hold as exact rational identities. Their full solutions and
source projections are preserved in [radial-response.json](../results/radial-response.json).

## 2. A definition fixed before evaluating the solution

Choose the standard exterior Legendre branches

```math
P=P_2(x)=\frac{3x^2-1}{2},\qquad
Q=Q_2(x)=\frac{3x^2-1}{4}\log\frac{x+1}{x-1}-\frac32x.
```

These solve $\mathcal L_2P=\mathcal L_2Q=0$ for $x>1$; $Q$ has leading
term $2/(15x^3)$ at infinity. Define the Wronskian flux

```math
C[R]=X(PR'-P'R).
```

Direct differentiation gives

```math
C[P]=0,\qquad C[Q]=-1,\qquad (C[R])'=P\mathcal L_2R=PF.
```

The standard Legendre equation and Wronskian framework are recorded in
[NIST DLMF section 14.2](https://dlmf.nist.gov/14.2); the explicit conventions
and identities above are independently verified here.

For a rational function, define $\mathrm{FP}_{\infty}$ as its constant
Laurent coefficient in the specified coordinate $x$. Equivalently, take the
constant coefficient of its polynomial quotient. This is a finite-part
operation, not an ordinary limit of a generally divergent function.

**Subtraction prescription.** Construct $J[F]$ from the source alone by

```math
J'[F]=PF,\qquad \mathrm{FP}_{\infty}J[F]=0.
```

For the two sources here, $PF$ has only poles at $x=\pm1$ of order at most
three, and its simple-pole residues vanish. Divide it into a polynomial and
partial fractions. Integrate the polynomial with zero constant and integrate
each pole term $a_m/(x-c)^m$, $m\ge2$, as
$a_m(x-c)^{1-m}/(1-m)$. This gives a unique rational $J$ with the required
finite part. No logarithm or logarithmic scale enters this primitive.

Now define the **finite-part connection coefficient**

```math
b_F[R]=J[F]-C[R].
```

It is independent of radius on solutions. It also equals
$-\mathrm{FP}_{\infty}C[R]$, and adding $AP+BQ$ to a solution changes it by
$B$ alone. Thus it is calibrated to the coefficient of the decaying homogeneous
branch, while accounting for the nonzero source.

To make the reference solution explicit without importing the answer, set

```math
R_{\ast}(F)(x)=P(x)\int_2^x\frac{J(F)(s)}{(s^2-1)P(s)^2}\,ds.
```

Since $P>0$ on $x>1$, this reference is well defined there, obeys
$\mathcal L_2R_{\ast}=F$ and has $C[R_{\ast}]=J[F]$. Every solution therefore has

```math
R=R_{\ast}(F)+AP+b_F[R]Q.
```

The base point 2 sets a growing-branch normalization. Moving it changes only
$A$, not $b_F$. The reference need not satisfy horizon regularity. Neither the
definition of $J$ nor the reference integral uses the previously constructed
regular $R_2$.

All uses of infinity concern formal coefficients of these rational functions.
They do not extend a finite-amplitude tidal geometry to an asymptotically flat
global spacetime or assert a uniform large-radius perturbation limit.

## 3. Determining the coefficient from the source and horizon

At the horizon put $s=x-1$. For the present source class a local solution can
have a forced pole and a logarithmic homogeneous part:

```math
R=\frac{a}{s}+L\log s+O(1).
```

Higher terms of the logarithmic branch can include $s\log s$. The source fixes
$a=\tfrac12\lim_{x\to1}(x-1)^2F$. The flux has the leading form

```math
C[R]=-\frac{2a}{s}-13a+2L+o(1).
```

The pole in $R=\Pi_2(w)/f$ is allowed: $f\sim s/2$, so it leaves a finite
Ernst coefficient. It is a result of dividing by the background horizon zero.
Smoothness of the actual mixed metric in the fixed common chart, already
established for this family, implies smoothness of its Ernst coefficients and
excludes the $s\log s$ contribution to $w=fR$. Hence $L=0$.

Let $\mathrm{FP}_H J$ mean the constant term after subtracting the forced
$-2a/s$ pole. The regular solution must satisfy

```math
b_F=\mathrm{FP}_H J+13a.
```

Every quantity on the right is determined by the source and our subtraction
rule. The calculation gives

| Spin order | Forced pole $a$ | $\mathrm{FP}_H J$ | $b_F$ |
|---|---:|---:|---:|
| 0 | 0 | 0 | 0 |
| 2 | $1088/218295$ | $-30316/218295$ | $-16172/218295$ |

Direct substitution of the previously constructed $R_0,R_2$ gives exactly the
same values, providing a separate check rather than defining the reference.
For spin squared, the source-normalized reference has logarithmic coefficient
$L_*=-8086/218295$. The term $b_FQ$, with $Q\sim-\tfrac12\log s$, cancels
that logarithm in the total solution. A nonzero connection coefficient is
therefore consistent with a smooth geometry.

This also explains why excluding an independently singular homogeneous field
does not by itself determine the coefficient relative to a sourced reference:
the reference and homogeneous contribution can each contain logarithms that
cancel in their sum.

## 4. Testing the subtraction convention

The definition above is unambiguous once its conventions are fixed. Those
conventions are not uniquely selected by the radial equation.

For a Laurent expansion $R=\sum_n a_nx^n$, the flux definition gives

```math
b_F=\frac{15}{2}a_{-3}-5a_{-1}-\frac12a_1.
```

A second source-only reference can instead be defined by the Frobenius
recursion

```math
[(n-2)(n+3)]a_n-(n+2)(n+1)a_{n+2}=f_n,\qquad F=\sum_n f_nx^n,
```

with the free reference coefficients $a_2=a_{-3}=0$. Source compatibility at
the two resonances $n=2,-3$ holds here, so a formal Laurent solution without
logarithms exists. Relative to this reference the decaying coefficient is
$b_{\rm L}=15a_{-3}/2$. It also returns 0 on $P$ and 1 on $Q$, but the
spin-squared values differ:

| Prescribed reference | Static coefficient | Spin-squared coefficient |
|---|---:|---:|
| Zero finite part of $J$ at infinity | 0 | $-16172/218295$ |
| Zero $x^{-3}$ coefficient of the Frobenius reference | 0 | $-17760/218295$ |

The general freedom is $J[F]\mapsto J[F]+\kappa[F]$, giving
$b_F\mapsto b_F+\kappa[F]$. Requiring $\kappa[0]=0$ preserves homogeneous
calibration. Even retaining the static zero does not remove the freedom:

```math
\kappa_\lambda[F]=\frac\lambda2\lim_{x\to1}(x-1)^2F
```

vanishes for the zero source and $F_0$, but shifts the spin-squared result by
$\lambda(1088/218295)$. The parameter is a subtraction choice, not a new
freedom in the uniquely fixed regular metric. Choosing it after seeing the
answer to force a zero would not establish a vanishing theorem.

Changing the radial coordinate also changes a freshly imposed finite-part
rule. As a diagnostic, carry the full operator, basis and flux through
$x=z+1$, then impose zero finite part in $z$ instead: the coefficient becomes
$2944/43659$. This lies outside the original fixed-coordinate prescription;
it is not a second answer within it.

Differences between two solutions of the **same source problem** are independent
of the additive source subtraction, because the common $J[F]$ cancels. By
contrast, an absolute statement that the coefficient is zero requires a
specified origin for that subtraction. This mathematical example is consistent
with the broader need to distinguish coordinate and solution conventions in
[Gralla's analysis](https://arxiv.org/html/1710.11096v3#S3). We do not import
that paper's historical status claims or identify this coefficient with a
physically matched observable.

## 5. Evidence and the remaining question

[verify_radial_response.py](../verify_radial_response.py) supplies 45 exact
checks of the radial reduction, branch normalization, source-only primitives,
both coefficient extractions, horizon balance, Frobenius resonances and
reference coefficients, and subtraction/coordinate diagnostics. The formal
Frobenius reference is checked through $x^{-7}$; the differential equations,
flux identity and finite-part value are exact rational identities. Its formal
series check is not a proof of convergence.

The standard Legendre framework is prior mathematics; no novelty or physical
counterexample is claimed.

An absolute response requires a normalization criterion beyond regularity and
homogeneous-branch calibration. Without one, the natural invariant quantities
are differences between solutions of the same source problem. Physical matching
could supply such a criterion, but is not assumed in this calculation.
