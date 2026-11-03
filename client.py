"""
Cutaneous Post-Occlusive Reactive Hyperemia (PORH) & Microvascular Endothelial Engine.
Provides deterministic, zero-dependency modeling of Laser Doppler flux,
peak hyperemic amplification ratio (PU_peak / PU_base), time-to-peak (sec), and endothelial nitric oxide (NO) reserve.
"""

from typing import Dict, Any, List, Optional


class CutaneousMicrovascularPORHClient:
    """
    Deterministic client for calculating Cutaneous Post-Occlusive Reactive Hyperemia (PORH).
    Assesses microvascular endothelial shear stress response, nitric oxide (NO) / prostacyclin release,
    precapillary sphincter recruitment kinetics, and peripheral vascular disease vulnerability.
    """

    def __init__(self):
        pass

    def evaluate_porh(
        self,
        baseline_flux_pu: float,
        peak_hyperemic_flux_pu: float,
        time_to_peak_sec: float,
        recovery_time_sec: float,
        occlusion_duration_min: float = 3.0
    ) -> Dict[str, Any]:
        """
        Calculates PORH amplification ratio and microvascular endothelial health score.
        Normative values (3 min arterial occlusion):
        - Baseline flux: 10.0 - 25.0 PU
        - Peak hyperemic flux: 45.0 - 140.0 PU
        - Hyperemic Ratio (PU_peak / PU_base): 3.2 - 6.5x
        - Time to Peak: 5.0 - 10.0 s (delayed > 14.0 s indicates endothelial dysfunction)
        - Recovery Time: 50.0 - 120.0 s
        """
        if baseline_flux_pu <= 0 or peak_hyperemic_flux_pu <= 0 or time_to_peak_sec <= 0 or recovery_time_sec <= 0:
            return {"error": "Flux values and time parameters must be strictly positive"}
        if peak_hyperemic_flux_pu <= baseline_flux_pu:
            return {"error": "Peak hyperemic flux must exceed baseline perfusion flux"}

        # 1. Hyperemic Amplification Ratio
        porh_ratio = round(peak_hyperemic_flux_pu / baseline_flux_pu, 2)

        # 2. Perfusion Deficit / Rebound Delta (PU)
        delta_flux_pu = round(peak_hyperemic_flux_pu - baseline_flux_pu, 1)

        # 3. Microvascular Endothelial Health Score (0 - 100)
        score = 80.0
        if 3.4 <= porh_ratio <= 6.5:
            score += 12.0
        elif 2.6 <= porh_ratio < 3.4 or 6.5 < porh_ratio <= 8.0:
            score += 5.0
        elif porh_ratio < 1.8:
            score -= 30.0  # Profound endothelial blunting
        elif porh_ratio < 2.5:
            score -= 15.0

        if time_to_peak_sec <= 8.5:
            score += 8.0
        elif time_to_peak_sec <= 11.0:
            score += 3.0
        elif time_to_peak_sec > 16.0:
            score -= 22.0  # Sluggish endothelial shear recruitment
        elif time_to_peak_sec > 12.5:
            score -= 10.0

        if recovery_time_sec <= 110.0:
            score += 5.0
        elif recovery_time_sec > 180.0:
            score -= 12.0

        endothelial_score = round(min(100.0, max(5.0, score)), 1)

        if endothelial_score >= 85.0 and porh_ratio >= 3.2 and time_to_peak_sec <= 10.0:
            tier = "OPTIMAL_MICROVASCULAR_ENDOTHELIAL_FUNCTION"
            interp = f"Brisk post-occlusive reactive hyperemia (Ratio {porh_ratio}x, Time to peak {time_to_peak_sec} s, Delta {delta_flux_pu} PU); robust endothelial NO synthesis."
            guidance = "Superior microvascular reserve and endothelial shear stress responsiveness. Optimal peripheral tissue perfusion defense."
        elif porh_ratio < 2.3 or time_to_peak_sec > 15.0:
            tier = "IMPAIRED_ENDOTHELIAL_FLOW_MEDIATED_DILATION"
            interp = f"Blunted or sluggish reactive hyperemia (Ratio {porh_ratio}x < 2.5x, Time to peak {time_to_peak_sec} s > 12 s); reflects microvascular endothelial dysfunction, capillary rarefaction, or vascular stiffness."
            guidance = "Reduced microvascular reserve. Screen for systemic cardiometabolic risk, subclinical atherosclerosis, and maintain regular zone 2 aerobic exercise."
        else:
            tier = "MODERATE_MICROVASCULAR_PERFUSION_RESERVE"
            interp = f"Moderate hyperemic response (Ratio {porh_ratio}x, Time to peak {time_to_peak_sec} s, Recovery {recovery_time_sec} s); preserved basal microvascular tone."
            guidance = "Adequate microvascular elasticity. Maintain dietary nitrate intake and avoid prolonged limb immobility."

        return {
            "occlusion_duration_min": occlusion_duration_min,
            "baseline_flux_pu": baseline_flux_pu,
            "peak_hyperemic_flux_pu": peak_hyperemic_flux_pu,
            "delta_flux_pu": delta_flux_pu,
            "porh_amplification_ratio": porh_ratio,
            "time_to_peak_sec": time_to_peak_sec,
            "recovery_time_sec": recovery_time_sec,
            "microvascular_endothelial_score": endothelial_score,
            "classification": tier,
            "physiological_interpretation": interp,
            "actionable_guidance": guidance
        }
