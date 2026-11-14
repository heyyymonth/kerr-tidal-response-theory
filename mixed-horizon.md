# Mixed quadrupoles: a controlled horizon-curvature limit

Venkata Hemanth Athota · Analytical working note · 13 November 2026

## Question and result

Can a finite applied quadrupolar tide cancel the curvature singularity associated with a decaying quadrupolar seed in the stationary, axisymmetric solution family used by Gounis, Kehagias and Riotto [1]?

For the reflection-symmetric local vacuum family specified below, the answer is no. With fixed decaying amplitude $d\ne0$ and finite applied amplitude $c$, the dimensionless Kretschmann scalar $\mathcal K$ obeys

$$
\boxed{\lim_{r\to0^+}r^6\log\mathcal K=\frac32d^2>0.}
$$

Here $r$ is the dimensionless cylindrical Weyl radius on the equatorial plane; it is not the Boyer–Lindquist radius. If $s=x-1$ is the prolate-coordinate distance from the background horizon, $r^2=s(s+2)$, and therefore

$$
\boxed{\lim_{s\to0^+}s^3\log\mathcal K=\frac3{16}d^2.}
$$

This reconstructs the leading logarithmic divergence reported in Eq. (5.18) of [1], including a finite growing tide. It does not reproduce that equation's full prefactor. The static calculation is exact; the rotating conclusion is an asymptotic argument conditional on the stated vacuum family and reflection symmetry. Neither result establishes a new physical Love-number theorem.

## Conventions and assumptions

Set the prolate length scale $\sigma=1$ during the calculation. Restore dimensions by $\mathcal K=\sigma^4R_{abcd}R^{abcd}$, so the logarithm has a dimensionless argument. The signature is $(-,+,+,+)$, with stationary Weyl metric

$$
ds^2=-f(dt-\omega\,d\phi)^2
+f^{-1}\{e^{2\gamma}(dr^2+dz^2)+r^2d\phi^2\}.
$$

Use the harmonic seed

$$
\psi=(cR^2+dR^{-3})P_2(\cos\vartheta),\qquad
R^2=x^2+y^2-1,\quad \cos\vartheta=xy/R.
$$

These are **Weyl-spherical** seed amplitudes, not the separated prolate $P_\ell(x),Q_\ell(x)$ amplitudes in the preliminary [Ernst note](README.md). On $z=y=0$, $x=\sqrt{1+r^2}$ and

$$
\psi=-\frac{c r^2}{2}-\frac{d}{2r^3}.
$$

The limit holds for each fixed finite $c$, each fixed real $d\ne0$, and finite normalization constants. It is not a uniform limit as $d\to0$, as spin tends to zero, or as the Kerr seed becomes extremal. A growing tide is a local external-field description, not an asymptotically flat boundary condition at infinity.

## 1. Exact static control

Write

$$
U=U_S+\psi,\quad U_S=\frac12\log\frac{x-1}{x+1},\quad
v=U_r=\frac1{rx}-cr+\frac{3d}{2r^4},\quad f=e^{2U}.
$$

Reflection symmetry and the static vacuum equations give $\gamma_{s,r}=rv^2$. Direct integration yields

$$
\gamma_s=\log(r/x)+V,
$$

$$
V=-2cx+dW+\frac{c^2r^4}{4}+\frac{3cd}{r}
-\frac{3d^2}{8r^6}+C_0,\qquad
W=\frac{x(2r^2-1)}{r^3}.
$$

Differentiating this expression exactly recovers $rv^2$. The finite integration constant $C_0$ cannot change the scaled logarithmic limit.

The curvature contraction on the reflection plane is

$$
\mathcal K=e^{4U-4\gamma_s}Q_0,\qquad
Q_0=8(A^2+B^2+C^2),
$$

$$
A=v'+2v^2-rv^3,\quad
B=-v'-v/r+rv^3-v^2,\quad
C=v/r-v^2,
$$

where the prime means $d/dr$. The independent frame calculation below recovers this identity. With $c=d=0$, the full expression gives $48/(x+1)^6$, the Schwarzschild result for unit mass.

For fixed nonzero $d$,

$$
Q_0=\frac{729d^6}{4r^{22}}[1+O(r^3)],
$$

and direct expansion gives

$$
\log\mathcal K=
\frac{3d^2}{2r^6}+\frac{2d}{r^3}
-\frac{12cd+6d}{r}-22\log r+O(1).
$$

The positive $d^2/r^6$ term dominates both signs of $d$ and every fixed finite $c$.

### Mixed terms are subleading, not necessarily finite

The published discussion following Eq. (5.18) addresses simultaneous $c,d\ne0$. Our static control gives the more precise check

$$
\lim_{r\to0^+}r\left.\partial_c\log\mathcal K\right|_{c=0}=-12d.
$$

Thus the coefficient linear in $c$ in $\mathcal K$ can itself diverge at the horizon. Pointwise analyticity in amplitudes does not make those coefficients uniformly bounded there. The surviving singularity is justified by asymptotic dominance, without requiring all mixed contributions to remain finite.

We also rederive $V$ rather than importing the printed Eq. (5.10). At $d=0,y=0$, its linear term is $+2cx$, whereas the vacuum equation gives $-2cx$. The derivative difference is $4c$ with respect to $x$, which cannot be repaired by an integration constant. The later pure-growing expression, Eq. (5.26), has the negative sign. These checks concern formulas and the local argument, not a refutation of the paper's physical conclusion.

## 2. A stationary curvature identity

In a local region with $f>0$, let $U=\tfrac12\log f$ and define the physical twist variable

$$
\tau=\frac{f\omega_r}{r}.
$$

Use the orthonormal coframe

$$
\theta^0=e^U(dt-\omega\,d\phi),\quad
\theta^1=e^{\gamma-U}dr,\quad
\theta^2=e^{\gamma-U}dz,\quad
\theta^3=re^{-U}d\phi.
$$

At a reflection plane, the stationary vacuum equations imply

$$
\gamma_r=rv^2-\frac r4\tau^2,\qquad
U_{zz}=-v'-v/r-\frac12\tau^2.
$$

For $\mathcal T_z=f\omega_z/r$, the twist equation gives
$\partial_z\mathcal T_z=-\tau'-2v\tau$ on that plane. These identities eliminate transverse derivatives from the curvature contraction:

$$
\mathcal K=e^{4U-4\gamma}(Q_0+\Delta Q),
$$

$$
\begin{aligned}
\Delta Q={}&-4(\tau')^2
+(8rv^2-24v-2r\tau^2)\tau\tau'\\
&+\left(-12r^2v^4+24rv^3+8rvv'-20v^2+12v'+\frac{12v}{r}\right)\tau^2\\
&+3(r^2v^2-rv+1)\tau^4-\frac{r^2}{4}\tau^6.
\end{aligned}
$$

The program constructs the connection and Riemann tensor from the coframe, checks every vacuum Ricci component, and contracts the tensor independently. It also checks Schwarzschild and two exact, nonzero-spin Kerr equatorial points. Those background checks support the implementation; the general identity follows from the symbolic contraction with the declared vacuum equations.

Every term in $\Delta Q$ contains physical twist or its derivative. There are no inverse powers of either. This is the relevant control on possible rotating cancellations. Equatorial radial data suffice once reflection symmetry and the vacuum equations have been imposed.

## 3. The two rotating branches

Use reflection-preserving solution-generating constants, so the auxiliary functions on $y=0$ are $a_{\rm aux}=-k$, $b_{\rm aux}=k$, with

$$
k=\alpha\exp(2cx-dW),\qquad 0<|\alpha|<1.
$$

Here $\alpha$ labels the Kerr seed. Its isolated Kerr mass/spin relations do not define a physical spin for a distorted spacetime without matching. The reflection-symmetric family agrees with the later pure-decaying expressions in [1], Eqs. (5.12)–(5.13), at $c=0$.

The amplitude obeys the first-order equation $k_r/k=-2\psi_r/x$. Define

$$
S=x+1-(x-1)k^2,\qquad T=x-1-(x+1)k^2.
$$

The equatorial metric functions reduce to

$$
f=e^{2\psi}\frac TS,\qquad
\omega-K_2=\frac{4kx e^{-2\psi}}T,\qquad
H=f(\omega-K_2)=\frac{4kx}S.
$$

The finite constant $K_2$ drops out of $\omega_r$; using $H$ makes no global coordinate claim. The exact soliton expression
$\gamma=\gamma_s+\tfrac12\log(ST/r^2)+\text{constant}$
is also consistent with the radial vacuum equation above on the local $f>0$ branches.

Since

$$
\log|k/\alpha|=d/r^3-3d/(2r)+O(1),
$$

there are two distinct limits:

| Fixed amplitude | Auxiliary limit | Leading $U$ | Leading $H$ |
|---|---|---|---|
| $d<0$ | $k\to0$ | $\psi+U_S$ | $2k$ |
| $d>0$ | $|k|\to\infty$ | $\psi-U_S$ | $-8/(r^2k)$ |

In both cases $T/S>0$ sufficiently close to $r=0$. Corrections to the displayed $U$ and to its first two radial derivatives are exponentially small times powers of $r$. The same is true of $H$ and its first two radial derivatives: differentiating $k$ only adds algebraic factors because $k_r/k=-2\psi_r/x$. In the large-$k$ branch this follows by expanding the rational expressions in $1/k$; factors $1/(x-1)$ contribute only powers of $1/r$.

Consequently

$$
\tau=\frac{H_r-2U_rH}{r},\qquad \tau'
=O\!\left(r^{-N}e^{-|d|/r^3+O(r^{-1})}\right)
$$

for some finite power $N$ for each derivative. This is a bound on physical twist, not a claim that $\omega$ itself tends to zero.

Both branches therefore have

$$
v=\frac{3d}{2r^4}+O(r^{-1}),\qquad
\gamma_r=\frac{9d^2}{4r^7}+O(r^{-4}),\qquad
\gamma=-\frac{3d^2}{8r^6}+O(r^{-3}).
$$

The reduced curvature satisfies

$$
Q_0+\Delta Q=\frac{729d^6}{4r^{22}}[1+O(r^3)].
$$

It is eventually positive. Its logarithm grows only logarithmically in $r$, while $4U=O(r^{-3})$ and $-4\gamma=3d^2/(2r^6)+O(r^{-3})$. Multiplication by $r^6$ proves the stated limit for either sign of $d$.

## What this establishes and the next proof obligation

Within this reflected quadrupolar family, a nonzero decaying seed obstructs a regular extension at the equatorial point of the background horizon. Finite applied amplitude cannot cancel that obstruction. This is a reconstruction of an existing curvature argument with controlled limits, not a novelty claim.

It does not classify global event horizons or prove nakedness. It does not establish that the solution-generating family contains every admissible tidally perturbed Kerr solution. Most importantly, a seed amplitude has not yet been identified with an independently matched nonlinear response coefficient.

The next substantive question is whether a regular, *driven* mixed-multipole solution can carry an independent conservative response after fixing mass, spin, gauge, and the applied-field normalization. The mixed Ernst equation in [the starting note](README.md#4-derive-the-actual-nonlinear-coupling-equation) states that boundary-value problem. Excluding the singular branch examined here is necessary for this family; it does not solve the driven matching problem.

## Reproduction and sources

Run `python3 verify_mixed_horizon.py` with the versions in `requirements.txt`; `--write` regenerates [the verification record](results/mixed-horizon.json). The record includes the exact stationary curvature polynomial, checked identities, script hash, and explicit limits of the calculation. The rotating asymptotic proof is the argument above, not a black-box symbolic certificate.

1. L.-R. Gounis, A. Kehagias and A. Riotto, *The vanishing of the non-linear static Love number of Kerr black holes and the role of symmetries*, JCAP 03 (2025) 002. [DOI](https://doi.org/10.1088/1475-7516/2025/03/002); [published version](https://access.archive-ouverte.unige.ch/access/metadata/6f750ab1-3a83-4f83-b11c-4d26903dce33/download). Source-version provenance is recorded in [README](README.md#evidence-and-source-versions).

This note has not been incorporated into the cluster-dynamics manuscript or submitted as a research result.
