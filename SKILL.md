---
name: genpark-personal-agent-cutaneous-microvascular-post-occlusive-reactive-hyperemia-skill
version: 1.0.0
description: Zero-dependency sovereign personal agent skill for calculating Cutaneous Post-Occlusive Reactive Hyperemia (PORH) amplification ratio (PU_peak/PU_base), time to peak, and endothelial nitric oxide reserve.
author: AlphaPark Inc.
license: Apache-2.0
tags:
  - personal-agent
  - ai-agent
  - openclaw
  - genpark
  - mcp
  - mcp-server
  - model-context-protocol
  - python
  - zero-dependency
  - wellness
  - productivity
  - production-ready
metadata:
  openclaw_compatible: true
  hermes_compatible: true
  zero_dependency: true
---

# Cutaneous Microvascular Reactive Hyperemia (PORH) Skill

A sovereign personal agent capability for evaluating peripheral microvascular endothelial function, shear stress nitric oxide (NO) generation, Laser Doppler Post-Occlusive Reactive Hyperemia (PORH), and precapillary sphincter recruitment.

## Core Capabilities
- **Hyperemic Amplification Ratio (PORH)**: Computes the flow multiplier ($PU_{peak} / PU_{baseline}$, normative: $3.2 - 6.5\times$).
- **Time to Peak Hyperemia ($t_{peak}$)**: Measures the speed of endothelial vasodilatory recruitment post-deflation (normative: $5.0 - 10.0\text{ s}$).
- **Microvascular Endothelial Health Scoring**: Detects early loss of microvascular elasticity and capillary rarefaction before overt systemic hypertension.
- **Nitric Oxide & Perfusion Coaching**: Prescribes dietary nitrate foods (beetroot, arugula), post-occlusion contrast baths, and active movement intervals.

## Fast Invocation
```python
from client import CutaneousMicrovascularPORHClient

client = CutaneousMicrovascularPORHClient()
res = client.evaluate_porh(
    baseline_flux_pu=14.2,
    peak_hyperemic_flux_pu=72.5,
    time_to_peak_sec=7.2,
    recovery_time_sec=78.0
)
print("PORH Ratio:", res["porh_amplification_ratio"], "x")
print("Endothelial Score:", res["microvascular_endothelial_score"], "/ 100")
```
