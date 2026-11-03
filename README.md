# Cutaneous Microvascular Reactive Hyperemia (PORH) Skill

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/zero--dependencies-standard--lib-brightgreen.svg)](requirements.txt)
[![MCP Protocol Ready](https://img.shields.io/badge/mcp-protocol--ready-orange.svg)](mcp_server.py)
[![OpenClaw Certified](https://img.shields.io/badge/openclaw-certified-purple.svg)](SKILL.md)

Zero-dependency sovereign personal agent skill for non-invasive evaluation of Cutaneous Post-Occlusive Reactive Hyperemia (PORH), Laser Doppler flowmetry, time-to-peak, and endothelial nitric oxide reserve.

```mermaid
flowchart TD
    Baseline["Resting Cutaneous Perfusion Flux Baseline (PU_base)"] --> Occlusion["3-Min Suprasystolic Arterial Occlusion Challenge"]
    Occlusion --> Deflation["Cuff Release -> Sudden Shear Stress Surge"]
    Deflation --> NORelease["Endothelial Nitric Oxide Synthase (eNOS) & Prostacyclin Surge"]
    NORelease --> PeakHyperemia["Peak Reactive Hyperemic Perfusion (PU_peak)"]
    PeakHyperemia --> PORHMetrics["PORH Ratio (PU_peak/PU_base) & Time-to-Peak (sec)"]
    PORHMetrics --> EndothelialScore["Microvascular Endothelial & Vascular Elasticity Score"]
    EndothelialScore --> Agent["OpenClaw / Hermes Personal Agent Lifestyle Prescriptions"]
```

## Features
- **Deterministic Math**: Pure Python standard library implementation with zero external dependencies.
- **Vascular Physiology Standards**: Implements validated equations for Laser Doppler flux, hyperemic amplification ratio, and time-to-peak kinetics.
- **Microvascular Endothelial Dysfunction Detection**: Early sensitive screening for subclinical vascular stiffening and endothelial decay.
- **Model Context Protocol (MCP)**: Native JSON-RPC tool integration for LLMs and autonomous agents.

## Quickstart

```python
from client import CutaneousMicrovascularPORHClient

client = CutaneousMicrovascularPORHClient()
result = client.evaluate_porh(
    baseline_flux_pu=14.2,
    peak_hyperemic_flux_pu=72.5,
    time_to_peak_sec=7.2,
    recovery_time_sec=78.0
)
print("PORH Ratio:", result["porh_amplification_ratio"], "x")
print("Endothelial Score:", result["microvascular_endothelial_score"])
print("Classification:", result["classification"])
```

## License
Apache-2.0
