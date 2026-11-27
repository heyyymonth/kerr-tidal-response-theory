import KerrRadial
import Lean.Util.CollectAxioms

open Lean Elab Command

/-!
Audit every theorem in the project namespace. Fail if any project axiom is declared,
or a theorem depends on anything beyond Lean's standard classical foundations.
In particular, this rejects `sorryAx`, custom axioms, and native decision oracles.
The audit is metaprogramming; the mathematical theorems themselves are kernel-checked.
-/

run_cmd do
  let env ← getEnv
  let allowed : Array Name := #[``propext, ``Classical.choice, ``Quot.sound]
  let declarations := env.constants.toList.filter fun (name, _) =>
    (`KerrRadial).isPrefixOf name
  let mut checked : Array Name := #[]
  for (name, info) in declarations do
    match info with
    | .axiomInfo _ => throwError "Project axiom is forbidden: {name}"
    | .thmInfo _ =>
      let axioms ← collectAxioms name
      let unexpected := axioms.filter fun ax => !allowed.contains ax
      unless unexpected.isEmpty do
        throwError "{name} uses unexpected axioms: {unexpected.toList}"
      checked := checked.push name
    | _ => pure ()
  if checked.isEmpty then
    throwError "No project theorems found; the audit did not run."
  for name in checked.qsort Name.lt do
    let axioms ← collectAxioms name
    logInfo m!"{name}: {axioms.qsort Name.lt |>.toList}"
  logInfo m!"Axiom audit passed for {checked.size} project theorems."
