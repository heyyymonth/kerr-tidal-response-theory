# Ernst equation and perturbative sources

Venkata Hemanth Athota

These conventions fix the background and mixed source used throughout the
construction. The parameter labels in this note refer to the reference Kerr
background. Published equation numbers refer to the journal version of Gounis
et al.; source details are in the [literature audit](literature-audit.md).

Work in four-dimensional vacuum general relativity near a subextremal Kerr
background, with $G=c=1$, $a=J/M$ and $|a|<M$. The fields are stationary and
axisymmetric. Growing tidal data describe a local exterior region; they are not
extended to infinity as an asymptotically flat solution. Horizon and axis
regularity are separate from specifying the outer data and a response convention.

## Ernst equation

In cylindrical Weyl coordinates $(\rho,z)$, introduce the complex Ernst potential

$$
\mathcal E=f+i\varpi,
\qquad
\Delta_{\rm ax}=\partial_\rho^2+\rho^{-1}\partial_\rho+\partial_z^2.
$$

Here $f$ is the metric potential and $\varpi$ is the twist potential. The correctly normalized equation is

$$
\mathrm{Re}(\mathcal E)\Delta_{\rm ax}\mathcal E
=\nabla\mathcal E\cdot\nabla\mathcal E.
$$

The gradient product is bilinear, with no complex conjugate. Equivalently,

$$
(\mathcal E+\overline{\mathcal E})\Delta_{\rm ax}\mathcal E
=2\nabla\mathcal E\cdot\nabla\mathcal E.
$$

Splitting real and imaginary parts gives

$$
f\Delta_{\rm ax}f=(\nabla f)^2-(\nabla\varpi)^2,
\qquad
f\Delta_{\rm ax}\varpi=2\nabla f\cdot\nabla\varpi.
$$

These equations provide the starting convention independently of the printed complex equation in [Gounis et al.](https://doi.org/10.1088/1475-7516/2025/03/002).

For prolate coordinates with scale $\sigma=\sqrt{M^2-a^2}$, define

$$
D h=\partial_x[(x^2-1)\partial_xh]
+\partial_y[(1-y^2)\partial_yh],
$$

$$
B(g,h)=(x^2-1)g_xh_x+(1-y^2)g_yh_y.
$$

The common factor $[\sigma^2(x^2-y^2)]^{-1}$ cancels from the Ernst equation, leaving $\mathrm{Re}(\mathcal E)D\mathcal E=B(\mathcal E,\mathcal E)$.

Two independent exact-background checks fix the normalization:

* Schwarzschild: $\mathcal E_S=(x-1)/(x+1)$ satisfies the equation.
* Kerr: $\mathcal E_K=1-2p/(x+p+iqy)$ satisfies it for $p=M/\sigma$, $q=a/\sigma$, and $p^2-q^2=1$. The sign of the twist is conventional.

### Printed normalization issue

Published Eq. (2.11), p.4, lacks the factor 2 above. Our Schwarzschild substitution gives

$$
2\mathcal E_S D\mathcal E_S-B(\mathcal E_S,\mathcal E_S)
=\frac{4(x-1)}{(x+1)^3}\ne0\quad (x>1).
$$

This is a reproducible normalization inconsistency, apparently typographical. It does not establish that the paper's independently constructed distorted metric or tidal conclusion is false.

## Static seeds

For a real Ernst potential $\mathcal E=e^{2u}$, direct substitution yields

$$
\mathcal E D\mathcal E-B(\mathcal E,\mathcal E)
=2\mathcal E^2 D u.
$$

Thus the static equation reduces to $D u=0$. Subtracting the Schwarzschild background potential leaves a harmonic distortion $\psi$. In a finite separated expansion,

$$
\psi(x,y)=\sum_\ell
\big[A_\ell P_\ell(x)+B_\ell Q_\ell(x)\big]P_\ell(y).
$$

Both radial branches obey

$$
\frac{d}{dx}\left[(x^2-1)\frac{dU_\ell}{dx}\right]
-\ell(\ell+1)U_\ell=0.
$$

For nonnegative integer $\ell$, $P_\ell$ is a polynomial with $P_\ell(1)=1$. The second solution has

$$
Q_\ell(x)=\tfrac12P_\ell(x)\log\frac{x+1}{x-1}
-W_{\ell-1}(x),
$$

where $W_{\ell-1}$ is polynomial (zero for $\ell=0$). It diverges logarithmically as $x\to1^+$ and decays as $x^{-\ell-1}$ at large $x$.

Consequently a bounded distortion on the horizon excludes the $Q_\ell$ branch for each separated mode. In a finite sum, its logarithmic coefficient cannot cancel for every $y$ unless each $B_\ell$ vanishes, by linear independence of the Legendre polynomials. An infinite expansion requires additional convergence control.

This recovers a known seed-level regularity argument. It does **not** identify every decaying term in a nonlinear metric as an independent tidal response. Even $e^{2\psi}$ contains products of applied fields. Physical matching remains necessary; [Combaluzier-Szteinsznaider et al.](https://doi.org/10.1007/JHEP03(2025)124) and [Iteanu et al.](https://doi.org/10.1007/JHEP02(2025)174) perform such matching in the Schwarzschild setting.

### Printed holomorphic shortcut fails an elementary check

Equation (6.7) of [Gounis et al.](https://doi.org/10.1088/1475-7516/2025/03/002), printed p.15, describes arbitrary real parts of holomorphic functions of $\rho+iz$ as seed solutions. Take $\psi=\mathrm{Re}(\rho+iz)^2=\rho^2-z^2$. Then

$$
(\partial_\rho^2+\partial_z^2)\psi=0,
\qquad
\Delta_{\rm ax}\psi=2.
$$

It is harmonic for the flat two-dimensional operator, but not for the three-dimensional axisymmetric operator required here. This disproves that shortcut as stated; it does not disprove the separate Legendre ladder identities or the physical Kerr response result. Such transformations cannot be assumed to preserve the axisymmetric equation.

## Mixed perturbations

Let $\mathcal E_0$ be the Kerr background, $f_0=\mathrm{Re}(\mathcal E_0)$, and define the real-linear operator

$$
\mathcal L_0h=f_0Dh+\mathrm{Re}(h)D\mathcal E_0
-2B(\mathcal E_0,h).
$$

For $\mathcal E=\mathcal E_0+\epsilon\mathcal E_1+\epsilon^2\mathcal E_2+\cdots$, with no factorial in the second-order term,

$$
\mathcal L_0\mathcal E_1=0,
\qquad
\mathcal L_0\mathcal E_2
=B(\mathcal E_1,\mathcal E_1)
-\mathrm{Re}(\mathcal E_1)D\mathcal E_1.
$$

For two independent applied fields, use

$$
\mathcal E=\mathcal E_0+\alpha\mathcal E_A+\beta\mathcal E_B
+\alpha\beta\mathcal E_{AB}+\cdots.
$$

The mixed equation is

$$
\mathcal L_0\mathcal E_{AB}
=2B(\mathcal E_A,\mathcal E_B)
-\mathrm{Re}(\mathcal E_A)D\mathcal E_B
-\mathrm{Re}(\mathcal E_B)D\mathcal E_A.
$$

This identity was checked for arbitrary component functions, not fitted to particular solutions. The second-order equation is driven. Excluding a singular homogeneous branch is insufficient to determine whether the regular, driven solution contains an independent conservative response after matching.

The [linear](linear-construction.md) and [mixed](mixed-construction.md) notes solve these equations through spin squared for prescribed seed-family boundary data. Identification with purely electric physical tidal data and a matched response remains open.

The proposed quadrupole–hexadecapole sector permits a quadrupolar angular term:

```math
P_2(y)P_4(y)=\frac27P_2(y)+\frac{20}{77}P_4(y)+\frac5{11}P_6(y).
```

This product alone does not determine the source in the full gravitational
equation or establish a response. The explicit construction supplies the source
for its declared mathematical drivers.

The identities are checked in [verify_baseline.py](../verify_baseline.py), with
the expected expressions retained in [baseline.json](../results/baseline.json).
See [verification](verification.md) for the distinction between symbolic checks,
formal proofs and the analytic assumptions in the construction.
