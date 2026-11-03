"""
MCP Server for Cutaneous Microvascular PORH Skill.
Exposes JSON-RPC Model Context Protocol tools for evaluating reactive hyperemia ratios, time-to-peak, and endothelial scores.
"""

import sys
import json
from typing import Dict, Any
from client import CutaneousMicrovascularPORHClient


def get_tools_manifest() -> Dict[str, Any]:
    return {
        "tools": [
            {
                "name": "evaluate_porh",
                "description": "Calculates Cutaneous Post-Occlusive Reactive Hyperemia (PORH) amplification ratio (PU_peak/PU_base), time to peak (s), and microvascular endothelial reserve score.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "baseline_flux_pu": {
                            "type": "number",
                            "description": "Baseline cutaneous Laser Doppler perfusion units (e.g. 15.0 PU)."
                        },
                        "peak_hyperemic_flux_pu": {
                            "type": "number",
                            "description": "Peak post-occlusive hyperemic perfusion units (e.g. 68.0 PU)."
                        },
                        "time_to_peak_sec": {
                            "type": "number",
                            "description": "Time from cuff release to peak hyperemic flow in seconds (e.g. 7.5 s, normative 5-10 s)."
                        },
                        "recovery_time_sec": {
                            "type": "number",
                            "description": "Time from cuff release to baseline perfusion recovery in seconds (e.g. 75.0 s)."
                        },
                        "occlusion_duration_min": {
                            "type": "number",
                            "description": "Duration of suprasystolic arterial occlusion in minutes (default: 3.0 min).",
                            "default": 3.0
                        }
                    },
                    "required": ["baseline_flux_pu", "peak_hyperemic_flux_pu", "time_to_peak_sec", "recovery_time_sec"]
                }
            }
        ]
    }


def handle_request(client: CutaneousMicrovascularPORHClient, req: Dict[str, Any]) -> Dict[str, Any]:
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": get_tools_manifest()
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})

        if name == "evaluate_porh":
            res = client.evaluate_porh(
                baseline_flux_pu=float(args.get("baseline_flux_pu", 15.0)),
                peak_hyperemic_flux_pu=float(args.get("peak_hyperemic_flux_pu", 68.0)),
                time_to_peak_sec=float(args.get("time_to_peak_sec", 7.5)),
                recovery_time_sec=float(args.get("recovery_time_sec", 75.0)),
                occlusion_duration_min=float(args.get("occlusion_duration_min", 3.0))
            )
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(res, indent=2)
                        }
                    ]
                }
            }
        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32601,
                    "message": f"Method not found: {name}"
                }
            }
    else:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {
                "code": -32600,
                "message": f"Invalid Request: Unsupported method {method}"
            }
        }


def main():
    client = CutaneousMicrovascularPORHClient()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(client, req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {
                    "code": -32700,
                    "message": f"Parse error or exception: {str(e)}"
                }
            }
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
