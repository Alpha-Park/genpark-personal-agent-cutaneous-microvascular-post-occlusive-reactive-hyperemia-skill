"""
Example Usage: Cutaneous Microvascular Post-Occlusive Reactive Hyperemia (PORH).
Demonstrates zero-dependency calculation of PORH ratio, time-to-peak, and endothelial nitric oxide reserve scoring.
"""

from client import CutaneousMicrovascularPORHClient


def main():
    client = CutaneousMicrovascularPORHClient()
    print("=== Cutaneous Microvascular PORH Demo ===")

    # Test Case 1: Healthy vigorous endothelial flow-mediated hyperemic surge
    res1 = client.evaluate_porh(
        baseline_flux_pu=14.2,
        peak_hyperemic_flux_pu=72.5,
        time_to_peak_sec=7.2,
        recovery_time_sec=78.0,
        occlusion_duration_min=3.0
    )
    print("\nTest Case 1: Optimal Microvascular PORH Response")
    print(f"  Baseline Flux: {res1['baseline_flux_pu']} PU | Peak Hyperemic Flux: {res1['peak_hyperemic_flux_pu']} PU (Delta: {res1['delta_flux_pu']} PU)")
    print(f"  PORH Amplification Ratio: {res1['porh_amplification_ratio']}x | Time to Peak: {res1['time_to_peak_sec']} s")
    print(f"  Recovery Time: {res1['recovery_time_sec']} s")
    print(f"  Endothelial Score: {res1['microvascular_endothelial_score']} / 100")
    print(f"  Classification: {res1['classification']}")
    print(f"  Physiological Interpretation: {res1['physiological_interpretation']}")
    print(f"  Actionable Guidance: {res1['actionable_guidance']}")

    # Test Case 2: Blunted / delayed PORH (microvascular endothelial dysfunction)
    res2 = client.evaluate_porh(
        baseline_flux_pu=12.5,
        peak_hyperemic_flux_pu=24.0,
        time_to_peak_sec=16.8,
        recovery_time_sec=135.0,
        occlusion_duration_min=3.0
    )
    print("\nTest Case 2: Blunted Endothelial Reactive Hyperemia Pattern")
    print(f"  PORH Ratio: {res2['porh_amplification_ratio']}x | Time to Peak: {res2['time_to_peak_sec']} s")
    print(f"  Endothelial Score: {res2['microvascular_endothelial_score']} / 100")
    print(f"  Classification: {res2['classification']}")
    print(f"  Actionable Guidance: {res2['actionable_guidance']}")


if __name__ == "__main__":
    main()
