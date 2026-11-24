# From a regular horizon to a physically matched response

Venkata Hemanth Athota · Learning and proof-obligation note · 13 November 2026

This note explains the next step. It does not solve the mixed Kerr problem.
The established calculations and their limits are in [CLAIMS.md](../CLAIMS.md).

**23 November continuation:** [Mixed construction](mixed-construction.md) now
solves the driven mathematical problem for the chosen linear fields through
spin squared. It exhibits a regular nonzero interaction and nonzero coordinate
tails, with a proof of uniqueness for complete declared data. The distinction
between forced deformation and an independently defined response remains.

**22 November continuation:** [Linear construction](linear-construction.md)
now implements a mathematical regularity problem for two declared driver
families. The original pure-electric matching problem below is a distinct
later interpretation task, not a condition for that restricted construction lemma.

**20 November continuation:** [Response definition](response-definition.md)
now classifies the declared algebraic sector, fixes its aligned normalization,
and checks harmonic-source calibration. The full EFT reduction and physical
matching described below remain necessary.

## 1. State the candidate conjecture

A quadrupolar tide describes one angular pattern of external gravitational
curvature; a hexadecapolar tide describes another. Their interaction can have a
quadrupolar angular component. The identity checked in the baseline is

```math
P_2(y)P_4(y)=\frac27P_2(y)+\frac{20}{77}P_4(y)+\frac5{11}P_6(y).
```

This allows a channel; it does not establish the full gravitational source or
the response. We want to determine whether the independently matched conservative
mass-quadrupole response in the aligned configuration vanishes, including the
contribution of order $\eta_2\eta_4\chi^2$, where $\chi=J/M^2$.
The dimensionless amplitudes still need a precise external-field normalization.

Conservative response means the part encoded by conservative tidal couplings,
rather than energy absorption. It is distinct from the pre-existing multipoles
of an isolated Kerr black hole and from a change in horizon shape.
The intended setting is four-dimensional vacuum general relativity in the local
region, with external matter outside it, stationary axisymmetric electric-type
drivers aligned with the spin, and a subextremal background.

The desired statement is a conjecture about an **identifiable coefficient
combination**. Its definition must precede a proof of its value. One aligned
experiment may not separate every tensor coupling.

## 2. Why horizon regularity matters

A regular event horizon is not a material surface or a wall. A freely falling
observer should be able to cross it without encountering a curvature singularity.
Coordinates can fail there even when the geometry is smooth. Consequently, a
divergent coordinate component alone is insufficient evidence of a physical
singularity. Conversely, a divergent curvature invariant along an approach to a
putative smooth horizon obstructs that smooth extension. Finite scalar invariants
alone are not a complete sufficiency test for smoothness.

The existing [curvature note](../mixed-horizon.md) proves such a local obstruction
for a specified reflected family and fixed nonzero decaying seed. It does not
locate every possible global event horizon or prove nakedness. Its local frame
uses $f>0$; that restriction is not a condition on the entire physical Kerr
exterior. The stationary limit where $g_{tt}=0$ and the event horizon are different
surfaces in rotating Kerr. A future boundary construction must handle the
ergoregion and demonstrate regularity in suitable coordinates or frames.

Axis regularity is a separate condition: one must also exclude conical defects
on the relevant axis segments, with a consistent azimuthal period.

## 3. Homogeneous solutions and driven solutions

At first order, a perturbation obeys a homogeneous equation. At mixed second
order the interacting first-order fields produce a source:

```math
\mathcal L_0\mathcal E_{AB}=S[\mathcal E_A,\mathcal E_B].
```

Once the first-order fields are fixed, the source is fixed. Formally, a solution is

```math
\mathcal E_{AB}=\mathcal E_p+\sum_i c_i h_i,
\qquad
\mathcal L_0\mathcal E_p=S,
\qquad
\mathcal L_0h_i=0.
```

The particular solution accounts for the forcing. Homogeneous solutions are the
freedom left before imposing all boundary conditions and parameter conventions.
Regularity constrains the **total** field. A particular solution may already be
regular, or its singular terms may require cancellation by homogeneous terms.
It is therefore unsafe to delete a named homogeneous basis function before
examining the total solution.

Even the particular/homogeneous split is not unique. For any homogeneous $h$,

```math
\mathcal E_p\longmapsto\mathcal E_p+b h,
\qquad c\longmapsto c-b
```

leaves $\mathcal E_p+c h$ unchanged. The bare number $c$ cannot be declared a
physical response without specifying how the split and normalization were fixed.
Full boundary data might select a unique solution; uniqueness by itself does not
compute the response extracted from that solution.

## 4. A small exact example of the logical gap

Consider the illustrative ordinary differential operator

```math
L_2 u=\frac{d}{dx}\left[(x^2-1)\frac{du}{dx}\right]-6u,
\qquad x>1.
```

Its homogeneous solutions are $P_2(x)$ and $Q_2(x)$. The first is bounded at
$x=1$ and grows at infinity; the second diverges logarithmically at $x=1$ and
decays at infinity. Now prescribe a source:

```math
L_2 u=-\frac{18}{(x+1)^4}.
```

The exact particular solution is

```math
u_p=(x+1)^{-3},\qquad
u_p'=-3(x+1)^{-4},\qquad
u_p''=12(x+1)^{-5}.
```

Substitution gives

```math
(x^2-1)u_p''+2xu_p'-6u_p
=\frac{12(x-1)-6x-6(x+1)}{(x+1)^4}
=-\frac{18}{(x+1)^4}.
```

It is regular at the endpoint, $u_p(1)=1/8$, and has a nonzero decaying tail,
$\lim_{x\to\infty}x^3u_p=1$. Requiring regularity and no growing contribution
sets both homogeneous coefficients to zero, yet this forced tail remains.

This is a teaching example with a deliberately chosen source, **not a Kerr
metric or a Love-number counterexample**. Its lesson is exact: excluding a
singular homogeneous mode does not imply that a driven regular solution has
no decaying terms. Here the tail is completely fixed by the prescribed source.

## 5. How matching identifies an independent response

Matching compares two descriptions of the same geometry in a common region,
schematically $M\ll R\ll\mathcal R_{\rm ext}$. Here $R$ is a buffer-region
distance, not the equatorial dimensionless radius of the curvature note.
The external scale and amplitudes must permit this overlap.

In the near description, solve the gravitational equations with a regular
horizon and axis. In the far description, replace the hole by a spinning compact
object carrying its established background couplings, together with possible
additional tidal couplings. This is the worldline effective field theory (EFT).
Both descriptions include the applied fields and ordinary nonlinear gravitational
interactions.

Fix the same mass and spin conventions, time normalization, reference worldline,
field normalization, and gauge mapping on both sides. Include the intrinsic
spin-induced multipoles and all lower-order interactions contributing at the
target order. Then determine which extra tidal coupling combination, if any, is
needed for the two expansions to agree. In schematic form, in a fixed convention,

```math
\text{matched GR field}
=\text{field from established background and external couplings}
+\sum_A C_A\,\text{field generated by tidal operator }A.
```

The $C_A$ are fixed by this comparison; their numerical values require a declared
operator basis and normalization. A coordinate change may reshuffle metric
coefficients while leaving consistently matched predictions unchanged. Do not
define the reference field as the full Kerr answer and then claim that the
resulting zero proves the conjecture: the reference contribution must be
independently specified from the established couplings.

This distinction is motivated by [Gralla's definition analysis](https://arxiv.org/html/1710.11096v3)
and implemented in the nonlinear Schwarzschild calculations of
[Combaluzier-Szteinsznaider et al.](https://doi.org/10.1007/JHEP03(2025)124)
and [Iteanu et al.](https://doi.org/10.1007/JHEP02(2025)174).
Their results do not supply the missing rotating calculation here.

## 6. The next proof obligation, before solving the proposed channel

| Required ingredient | What must be established | Current status |
|---|---|---|
| Response definition | Specify the spin-dependent tidal operator basis and its independent structures before imposing alignment; identify the combination probed by the aligned mass quadrupole. | Three algebraic scalars and their aligned combination derived in the continuation; full EFT reduction unresolved. No coefficient value assigned. |
| External data and parameters | Define $\eta_2,\eta_4$, mass/spin labels and their perturbative shifts, time and azimuthal normalization, and which other applied moments vanish. | Mathematical seed and boundary data now specified; physical calibration remains open. |
| Boundary conditions | Give regular horizon/axis conditions for the full reconstructed metric, including gauge and parameter modes. | Constructed for the declared mathematical family in [the mixed note](mixed-construction.md); not yet calibrated to pure-electric physical data. |
| Driven solution | Obtain both linear tidal solutions and all lower spin orders needed by the mixed source. Solve the real-linear Ernst system. | Both linear fields and their driven mixed solution constructed through spin squared for the declared data. |
| Matching | Compute the reference EFT contribution, map fields/gauges, and extract the identifiable response combination. | Not performed. |
| Interpretation | Check the Schwarzschild limit against published matching and audit novelty for the final defined channel. | Foundational literature checked; channel-specific novelty unresolved. |

For example, once a common coordinate and parameter convention is fixed, expand
$\mathcal L_0=\mathcal L^{(0)}+\chi\mathcal L^{(1)}+\chi^2\mathcal L^{(2)}+\cdots$
and $\mathcal E_{AB}=H^{(0)}+\chi H^{(1)}+\chi^2H^{(2)}+\cdots$. The spin-squared
equation is then

```math
\mathcal L^{(0)}H^{(2)}
=S^{(2)}-\mathcal L^{(1)}H^{(1)}-\mathcal L^{(2)}H^{(0)}.
```

Thus the lower spin orders cannot simply be skipped. Coordinate dependence of
the prolate scale must also be accounted for when defining this expansion. This
recursion has now been executed for the mathematical seed family, as recorded
in [the mixed construction](mixed-construction.md). A response functional must
still be specified independently of its value, with physical matching a later
task. A consistently defined nonzero result is as admissible as a vanishing proof.
