# Kerr tidal response: proof reconstruction

Venkata Hemanth Athota · Working research note · 13 November 2026

The question is whether regular rotating black holes must have vanishing independently induced conservative response to stationary, axisymmetric tides beyond linear order. The present work reconstructs the starting equations and audits the closest published argument. It establishes algebraic consistency checks and a conditional horizon-curvature obstruction, not a general nonlinear Kerr Love theorem or a physical counterexample.

For the research question, learning sequence, and reasons earlier approaches do not settle this proof, start with [What we are trying to prove, and how we reached the question](research-context.md).

The [new-chat handoff](NEW_CHAT_HANDOFF.md) preserves the scientific status, repository setup preferences, authorship, and starting instructions for continuing this work in a separate repository.

The horizon calculation is recorded in [Mixed quadrupoles: a controlled horizon-curvature limit](mixed-horizon.md). It derives the static mixed-field divergence exactly and reconstructs the leading rotating divergence within a specified reflection-symmetric vacuum family.

## Evidence and source versions

The audit authority is the **published** paper [1]. It includes mixed growing/decaying quadrupoles after Eq. (5.18); that paragraph is absent from arXiv v1.

The published PDF's SHA-256 is `58d49474ca3438ce77fa3c9dc87002cb930c48710bbccfb246bebb3df65cd1d6`. The University of Geneva copy includes three preliminary pages: printed page 4 is PDF page 7; printed page 15 is PDF page 18. Both pages were visually inspected, rather than relying only on extracted equations. The downloaded reference is kept outside this working directory.

The 2026 review [2], §6.3.2, identifies all-multipole stationary Kerr response and effective-field-theory matching as unfinished. It is an invited-review **preprint**, not a verified journal publication. This is a literature-supported research opening, not a certification that the particular channel proposed below is unpublished.

## 1. Define the boundary-value problem

Use four-dimensional vacuum general relativity near a regular, subextremal Kerr black hole. Set $G=c=1$, define $a=J/M$, and restrict $|a|<M$. External matter lies beyond the local vacuum region. The field is stationary and axisymmetric about the spin axis; a rotating spacetime itself is stationary, not static.

The tidal solution is matched in a region where the black-hole scale is much smaller than the distance to external sources. A growing tidal term is not extended to arbitrarily large radius and called globally asymptotically flat. Regularity must include the horizon and rotation axis. Matching must fix the normalization of time, the definition of mass and spin, and the separation between applied fields and response.

The familiar isolated-black-hole uniqueness statement cannot replace this boundary-value problem: the imposed tidal boundary conditions differ from those of an isolated asymptotically flat black hole.

## 2. Independently normalize the governing equation

In cylindrical Weyl coordinates $(\rho,z)$, introduce the complex Ernst potential

$$
\mathcal E=f+i\varpi,
\qquad
\Delta_{\rm ax}=\partial_\rho^2+\rho^{-1}\partial_\rho+\partial_z^2.
$$

Here $f$ is the metric potential and $\varpi$ is the twist potential. The correctly normalized equation is

$$
\operatorname{Re}(\mathcal E)\Delta_{\rm ax}\mathcal E
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

These equations provide the starting convention independently of the printed complex equation in [1].

For prolate coordinates with scale $\sigma=\sqrt{M^2-a^2}$, define

$$
D h=\partial_x[(x^2-1)\partial_xh]
+\partial_y[(1-y^2)\partial_yh],
$$

$$
B(g,h)=(x^2-1)g_xh_x+(1-y^2)g_yh_y.
$$

The common factor $[\sigma^2(x^2-y^2)]^{-1}$ cancels from the Ernst equation, leaving $\operatorname{Re}(\mathcal E)D\mathcal E=B(\mathcal E,\mathcal E)$.

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

## 3. Recover the known static seed argument

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

This recovers a known seed-level regularity argument. It does **not** identify every decaying term in a nonlinear metric as an independent tidal response. Even $e^{2\psi}$ contains products of applied fields. Physical matching remains necessary; [3] and [4] perform such matching in the Schwarzschild setting.

### Printed holomorphic shortcut fails an elementary check

Equation (6.7) of [1], printed p.15, describes arbitrary real parts of holomorphic functions of $\rho+iz$ as seed solutions. Take $\psi=\operatorname{Re}(\rho+iz)^2=\rho^2-z^2$. Then

$$
(\partial_\rho^2+\partial_z^2)\psi=0,
\qquad
\Delta_{\rm ax}\psi=2.
$$

It is harmonic for the flat two-dimensional operator, but not for the three-dimensional axisymmetric operator required here. This disproves that shortcut as stated; it does not disprove the separate Legendre ladder identities or the physical Kerr response result. We cannot import an arbitrary-holomorphic-transformation symmetry into our proof.

## 4. Derive the actual nonlinear coupling equation

Let $\mathcal E_0$ be the Kerr background, $f_0=\operatorname{Re}\mathcal E_0$, and define the real-linear operator

$$
\mathcal L_0h=f_0Dh+\operatorname{Re}(h)D\mathcal E_0
-2B(\mathcal E_0,h).
$$

For $\mathcal E=\mathcal E_0+\epsilon\mathcal E_1+\epsilon^2\mathcal E_2+\cdots$, with no factorial in the second-order term,

$$
\mathcal L_0\mathcal E_1=0,
\qquad
\mathcal L_0\mathcal E_2
=B(\mathcal E_1,\mathcal E_1)
-\operatorname{Re}(\mathcal E_1)D\mathcal E_1.
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
-\operatorname{Re}(\mathcal E_A)D\mathcal E_B
-\operatorname{Re}(\mathcal E_B)D\mathcal E_A.
$$

This identity was checked for arbitrary component functions, not fitted to particular solutions. It exposes the real proof obligation: the second-order equation is driven. Excluding a singular homogeneous branch is insufficient to determine whether the regular, driven solution contains an independent conservative response after matching.

These equations have not been solved for tidal Kerr perturbations here. Their regular boundary conditions, solvability constraints and response extraction remain to be established.

## 5. Scope of the published argument and the candidate extension

Paper [1] constructs metrics from a harmonic seed, reports a quadrupolar curvature obstruction, and distinguishes seed ladder operators from transformations of the full Ernst potential. The full Kretschmann calculation has not been independently reproduced here.

The extension must establish both regularity for multipole mixtures and the connection from seed parameters to independently matched response. Pointwise analyticity in tidal amplitudes at a fixed exterior point is not by itself a proof of uniform behavior at the horizon.

One provisional diagnostic sector uses aligned electric quadrupole and hexadecapole drivers. Their angular product permits a quadrupolar component:

$$
P_2(y)P_4(y)=\frac27P_2(y)+\frac{20}{77}P_4(y)+\frac5{11}P_6(y).
$$

This is only an angular allowance. It does not demonstrate a nonzero source in the complete gravitational equations, a nonzero matched response, or novelty. Denote the two dimensionless tidal amplitudes by $\eta_2,\eta_4$ and the dimensionless spin by $\chi=J/M^2$. A possible first rotation-dependent diagnostic is the aligned mass-quadrupole response at order $\eta_2\eta_4\chi^2$. The nonrotating quadratic response is already covered by [4]. A pure quadrupole driver can itself generate higher angular structure, so its higher multipoles alone should not be claimed as a new sector.

The prospective theorem concerns the vanishing of identifiable conservative-response combinations for allowed pairs of stationary axisymmetric tides at a declared spin order. A consistently matched nonzero channel could refute that restricted conjecture. Establishing one zero would not prove it for all channels. The tensor-operator basis and response definition must be fixed before assigning a physical coefficient or claiming this particular mixed channel is unpublished.

## Verification record

`verify_baseline.py` checks the two exact backgrounds, the two printed-formula counterchecks, the static reduction, low-order Legendre identities and limits, both perturbative source formulas, and the angular product above. These are exact symbolic calculations, not cluster simulations or numerical evidence for a Love coefficient.

Run from this directory with the versions in `requirements.txt`:

```sh
python3 verify_baseline.py
```

Use `--write` to regenerate `results/baseline.json`. The saved record includes the script hash, package version, expected values, and the limits of what was checked.

`verify_mixed_horizon.py` independently constructs a stationary orthonormal-frame curvature contraction, verifies its vacuum Ricci components, checks Schwarzschild and nonzero-spin Kerr controls, and tests the exact static mixed-field limit. Run it with `--write` to regenerate `results/mixed-horizon.json`.

The [mixed-horizon note](mixed-horizon.md) supplies the conditional rotating asymptotic argument. It recovers the published leading logarithmic divergence, without reproducing the full published prefactor or classifying a global event horizon. The remaining proof obligation is to solve the driven mixed-multipole boundary-value problem and identify the independent response through matching; exclusion of a singular seed branch alone does not determine that response.

## References

1. L.-R. Gounis, A. Kehagias and A. Riotto, *The vanishing of the non-linear static Love number of Kerr black holes and the role of symmetries*, JCAP 03 (2025) 002. [DOI](https://doi.org/10.1088/1475-7516/2025/03/002); [published PDF](https://access.archive-ouverte.unige.ch/access/metadata/6f750ab1-3a83-4f83-b11c-4d26903dce33/download); [repository record](https://archive-ouverte.unige.ch/unige:192552). Published version used for equation and page references.
2. M. J. Rodríguez, L. Santoni and A. R. Solomon, *Love numbers of black holes and compact objects*, [arXiv:2604.08653v1](https://arxiv.org/html/2604.08653v1), especially §§2.2.4 and 6.3.2. Invited-review preprint.
3. O. Combaluzier-Szteinsznaider et al., *Symmetries of vanishing nonlinear Love numbers of Schwarzschild black holes*, [JHEP 03 (2025) 124](https://link.springer.com/article/10.1007/JHEP03%282025%29124).
4. S. Iteanu et al., *Vanishing of quadratic Love numbers of Schwarzschild black holes*, [JHEP 02 (2025) 174](https://link.springer.com/article/10.1007/JHEP02%282025%29174).

Existing cluster-transport calculations are not evidence for this strong-field theorem. This working note records a separate analytical investigation and has not been incorporated into a manuscript or publication.
