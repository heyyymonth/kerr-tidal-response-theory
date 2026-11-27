# An identifiable aligned response: tensor algebra and matching prescription

Venkata Hemanth Athota · 20 November 2026

This note derives the algebraic electric-tidal sector and the coefficient
combination selected by alignment. Its physical value, the full EFT reduction
and a Kerr solution calibrated to the external data below remain open.

The [linear](linear-construction.md) and [mixed](mixed-construction.md)
constructions solve a mathematical boundary problem through spin squared. Their
spin-linked odd growing data have not been converted to this note's pure-electric
external convention, so their seed amplitudes cannot yet be used as the matched
variables defined here.

## 1. External variables and normalization

Work in four-dimensional vacuum GR near a subextremal Kerr background, with
stationary, axisymmetric applied electric tides and reflection symmetry. Use
geometric units and an orthonormal spatial frame at a mass-centered reference
worldline. The external background is the regular field after the object's
self field is separated in a declared matching prescription. Its nonlinear
completion must itself obey the vacuum equations in the overlap region.

Let the electric quadrupolar moment be the Weyl projection
$\mathcal E_{ij}=\bar C_{i0j0}$ with signature $(-+++)$ and curvature sign fixed
so its weak-field limit is $\partial_i\partial_j\Phi$ in vacuum. Choose
$\mathcal E_{ijkl}$ to be the symmetric trace-free (STF) projection of the
symmetrized second covariant derivatives of that Weyl tensor, with the frame
vectors and four-velocity multiplying outside the derivatives. Bars denote the
regular external geometry. This chooses a curvature-derivative convention;
its relation to other nonlinear moment conventions must be included in matching.

Explicitly, with external frame $e_i^{\alpha}$ and four-velocity $u^\mu$,

```math
\mathcal E_{ijkl}=\mathrm{STF}_{ijkl}\left[
e_i^\alpha e_j^\beta e_k^\gamma e_l^\delta u^\mu u^\nu
\bar\nabla_{(\gamma}\bar\nabla_{\delta)}\bar C_{\alpha\mu\beta\nu}
\right].
```

Define the dimensionless tensors

```math
A_{ij}=M^2\mathcal E_{ij},\qquad
B_{ijkl}=M^4\mathcal E_{ijkl},\qquad s_i=J_i/M^2.
```

For a unit spin-axis vector $n_i$, put $N_L=n_{\langle L\rangle}$, with brackets
denoting STF projection, and impose alignment only **after** classifying tensors:

```math
A_{ij}=\eta_2N_{ij},\quad B_{ijkl}=\eta_4N_{ijkl},\quad s_i=\chi n_i.
```

Here $N_{ij}=n_i n_j-\delta_{ij}/3$, $N_{ij}N_{ij}=2/3$, and
$N_{ijkl}N_{ijkl}=8/35$. These fix the amplitudes' normalization.
In the linear weak-field Taylor convention
$\Phi_{\rm ext}=\sum_{\ell\ge2}\mathcal E_L X^L/\ell!$, they imply

```math
\Phi_{\rm ext}^{(1)}=\frac{\eta_2}{3}(R/M)^2P_2(\cos\theta)
+\frac{\eta_4}{105}(R/M)^4P_4(\cos\theta).
```

Thus $\eta_2,\eta_4$ are not raw coefficients multiplying Legendre potentials.
This equation calibrates the linear external data, not the complete nonlinear
Kerr field. Independent applied magnetic moments may be set to zero in this
test; spin-generated twist and magnetic curvature in the solution must remain.

## 2. Three scalars in the declared algebraic sector

Consider real, parity-even scalars formed from two identical $A$ tensors, one
$B$, and two spins, with no derivatives beyond those already defining $B$.
Repeated spatial indices are contracted with $\delta_{ij}$. A basis is

```math
I_0=(s_i s_i)A_{jk}A_{lm}B_{jklm},
```
```math
I_1=s_i s_j B_{ijkl}A_{km}A_{lm},\qquad
I_2=s_i A_{ij}B_{jklm}A_{kl}s_m.
```

There are exactly three in this sector. To see completeness, the symmetric
product of two spin-2 representations contains angular momenta $0,2,4$; the
symmetric product of two spin-1 representations contains $0,2$. Coupling also
to $B$ (angular momentum 4) leaves three scalar channels:
$(j_{AA},j_{ss})=(4,0),(2,2),(4,2)$, each with multiplicity one.
Two Levi-Civita tensors reduce to Kronecker deltas, and a single one cannot
contract the even total number of indices into a scalar here.

Independence is proved by evaluating these contractions at three exact tensor
configurations. Set $B=z_{\langle ijkl\rangle}$ throughout:

| $A$ | $s$ | $I_0$ | $I_1$ | $I_2$ |
|---|---|---|---|---|
| $\mathrm{diag}(-1/3,-1/3,2/3)$ | $z$ | $8/35$ | $8/105$ | $16/105$ |
| Same | $x$ | $8/35$ | $-4/105$ | $4/105$ |
| $\mathrm{diag}(1,-1,0)$ | $z$ | $4/35$ | $-8/35$ | $0$ |

The determinant is $-128/25725\ne0$. Together with the multiplicity count,
this proves an algebraic basis. The nonaligned rows are tensor probes, not
claimed stationary nonaligned Kerr solutions.

This does **not** prove completeness of a covariant worldline EFT modulo field
redefinitions, equations of motion, integration by parts, magnetic operators,
or different distributions of derivatives. That reduction remains a matching
prerequisite. The spin-independent cubic scalar also exists and belongs to the
lower-spin calculation; it has not been erased by restricting this table to $s^2$.

## 3. Alignment measures one coefficient combination

Let the target local conservative Lagrangian term be

```math
L_{224,s^2}=M w,\qquad w=c_0I_0+c_1I_1+c_2I_2.
```

No factorial is included in the definitions of $c_a$. The coefficient of the
dimensional product $\mathcal E_2^2\mathcal E_4 s^2$ scales as $M^9$.
The $c_a$ denote coefficients at the displayed spin order, with possible $M,\mu$
dependence, not additional unexpanded functions of $\chi$. In particular,
$c_0$ includes the scalar spin-squared correction to the zero-spin contraction.
Alignment gives exactly

```math
(I_0,I_1,I_2)=\eta_2^2\eta_4\chi^2(8/35,8/105,16/105),
```
```math
w_{\parallel}=\frac8{105}(3c_0+c_1+2c_2)\eta_2^2\eta_4\chi^2.
```

The map from $(c_0,c_1,c_2)$ to aligned data has rank one. Both directions
$(1,-3,0)$ and $(0,-2,1)$ are invisible to it. Consequently even a successful
zero-result in alignment would not imply $c_0=c_1=c_2=0$.

Use the response convention

```math
Q_{\rm resp}^{ij}=-2\frac{\partial L_{224,s^2}}{\partial\mathcal E_{ij}}
=-2M^3\frac{\partial w}{\partial A_{ij}},
```

where the derivative is within STF tensors, holding the renormalized $M,J_i$,
external frame, $B$, and subtraction scale $\mu$ fixed. This is the contribution
from the target term, not the total quadrupole including intrinsic Kerr and
lower-order contributions. For $Q_{\rm resp}^{ij}=q N^{ij}$, the norm of $N$
gives $q/M^3=-3\partial w_{\parallel}/\partial\eta_2$. Therefore define

```math
\frac{q}{M^3}=\kappa_{\parallel}\eta_2\eta_4\chi^2,\qquad
\kappa_{\parallel}=-\frac{16}{35}(3c_0+c_1+2c_2).
```

Equivalently $w_{\parallel}=-\kappa_{\parallel}\eta_2^2\eta_4\chi^2/6$.
The square on $\eta_2$ in the **action** becomes one power in the **response**
upon differentiation: a cubic tidal action produces quadratic tidal response.
These are definitions and exact contractions. No $c_a$ or $\kappa_{\parallel}$
has been evaluated for a black hole.

## 4. A necessary coordinate calibration already checked

Let $k=\sigma/M$, $R^2/M^2=k^2(x^2+y^2-1)$ and $z/M=kxy$. Define
$H_\ell=(R/M)^\ell P_\ell(z/R)$. Exact harmonic-polynomial identities give

```math
P_2(x)P_2(y)=\frac{3}{2k^2}H_2-\frac12,
```
```math
P_4(x)P_4(y)=\frac{35}{8k^4}H_4-\frac{15}{4k^2}H_2+\frac38.
```

A raw prolate $\ell=4$ seed therefore also contains a spherical $\ell=2$
piece and a constant. To prescribe exactly $\psi=u_2H_2+u_4H_4$, choose
$\psi=\alpha_0+\alpha_2P_2(x)P_2(y)+\alpha_4P_4(x)P_4(y)$ with

```math
\alpha_4=\frac8{35}k^4u_4,\quad
\alpha_2=\frac23k^2u_2+\frac47k^4u_4,\quad
\alpha_0=\frac13k^2u_2+\frac15k^4u_4.
```

For the Kerr coordinate scale, $k^2=1-\chi^2$, so keeping $u_2,u_4$ fixed
requires spin-dependent changes in the raw coefficients. The constant also
requires consistent time normalization when a seed is embedded in a metric.
These identities prevent a coordinate artifact from being counted as a mixed
response. They are a harmonic-seed calibration, **not** the physical rotating
source map. Only in the stated linear static weak-field convention can one
directly use $u_2=\eta_2/3$, $u_4=\eta_4/105$.

## 5. Matching prescription and the remaining work

The conditional target is $\kappa_{\parallel}^{\rm Kerr}=0$ in the convention
above, provided the full EFT reduction identifies this projection as the
complete coefficient combination at the declared order. A nonzero value is an
equally admissible research outcome. The following steps remain necessary:

1. **Complete the external definition.** Construct the nonlinear regular
   external background with independently controlled moments; specify the
   mass-centered worldline, spin supplementary condition and frame. Audit
   other derivative/magnetic terms and allowed field redefinitions. If they
   contribute to this projection, enlarge or transform the definition above.
2. **Calibrate the actual Kerr linear tidal fields.** Solve for the $\ell=2$
   and $\ell=4$ drivers through the required spin orders at fixed external
   moments. Convert to the same $M,J$, time and radial conventions. Section 4
   supplies a necessary algebraic check, not these solutions.
3. **Solve the mixed sourced equations.** Retain lower spin orders, since
   $\mathcal L^{(0)}H^{(2)}=S^{(2)}-\mathcal L^{(1)}H^{(1)}
   -\mathcal L^{(2)}H^{(0)}$. Impose smoothness of the full reconstructed
   metric in horizon-penetrating coordinates and elementary flatness on the
   relevant axis segments. Horizon location and angular velocity may shift;
   fixed external $M,J$ does not mean fixed isolated horizon area or angular velocity.
4. **Construct the reference prediction independently.** Include the mass,
   spin, intrinsic Kerr multipoles, lower-order response couplings already
   matched in the same convention, and nonlinear gravitational iterations.
   Defining the reference as the entire answer from step 3 would make the
   comparison circular.
5. **Match in a common region** $M\ll R\ll\mathcal R_{\rm ext}$. Fix the
   gauge map, regularization and finite-subtraction convention on both sides.
   A candidate is dimensional regularization with minimal subtraction at
   $\mu=1/M$, but its implementation has not been done here. Retain any
   logarithms and scale dependence found; a zero at one arbitrary scale or
   after a finite redefinition is not automatically a universal vanishing law.
6. **Extract and cross-check.** At fixed parameters, extract the coefficient
   of $\eta_2\eta_4\chi^2$ in $q/M^3$ after the reference contribution has
   been accounted for. In a formal analytic expansion this coefficient equals
   one half of the second derivative with respect to $\chi$ and the first
   derivative with respect to each of $\eta_2,\eta_4$, evaluated at zero.
   Check the zero-spin quadratic response against the published Schwarzschild
   matching. Audit novelty for the final, fully defined quantity.

Physical matching remains open. It first requires the external-definition
audit and calibration of the linear fields in steps 1–2. Horizon regularity
alone assigns no value to the matched coefficient.

## 6. Evidence and primary sources

[verify_response_basis.py](../verify_response_basis.py) performs 33 exact checks:
STF traces/norms, Taylor normalization, the three aligned contractions,
independence witness, representation count, rank/null directions, rotation
covariance, all five STF variations of the response, and harmonic-coordinate
calibration. [The saved record](../results/response-basis.json) contains its
hash and exact expected values. The representation-theory completeness argument
is given above; a few numeric tensor probes alone would not prove completeness.

The distinction between aligned combinations and full operator coefficients is
already explicit in [Combaluzier-Szteinsznaider et al., section 4.1 and appendix D](https://arxiv.org/html/2410.10952v2).
The requirement to match a consistent nonlinear external geometry is illustrated
by [Iteanu et al., sections 4.2, 5.3 and 6.2](https://arxiv.org/html/2410.03542v2).
[Saketh, Zhou and Ivanov, section 2](https://arxiv.org/html/2307.10391v2)
restrict their tidal expansion to linear external perturbations: their
quadrupole--octupole mixing is not this cubic-action sector.
These papers motivate the prescription; they do not compute our $c_a$.
The [literature audit](literature-audit.md#20-november-2026-channel-audit)
records the scope of these comparisons and a challenge to broader vanishing
claims. No novelty is claimed for this algebraic reconstruction.
