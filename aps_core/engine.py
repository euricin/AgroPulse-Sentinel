"""
Deterministic localized math validation engine for the Veterinary Log Matrix.
"""

import time
from typing import Tuple
from .exceptions import InvalidSeverityScoreError


class CompoundBiosecurityEngine:
    """
    Edge Evaluation Engine running execution loops directly on resource-constrained devices.
    Applies strict heuristic rules formulated by Dr. Kalimuddin Khan.
    """
    
    # Strict architectural weight coefficients
    W1_TEMPERATURE: float = 0.50
    W2_MORPHOMETRICS: float = 0.35
    W3_LATENCY: float = 0.15

    def __init__(self, consignment_id: str, operator_id: str) -> None:
        if not consignment_id or not operator_id:
            raise ValueError("Initialization parameters cannot contain null fields.")
        self.consignment_id: str = consignment_id
        self.operator_id: str = operator_id
        self.timestamp: float = time.time()

    def _validate_score(self, score: float, vector_name: str) -> None:
        """Enforces mathematical normalization boundaries [0.0, 1.0]."""
        if not (0.0 <= score <= 1.0):
            raise InvalidSeverityScoreError(
                f"Vector Matrix validation breach on '{vector_name}'. Value [{score}] "
                f"falls outside normalized system operational index [0.0, 1.0]."
            )

    def evaluate_threat_matrix(self, s1: float, s2: float, s3: float) -> Tuple[float, str]:
        """
        Executes structural mathematical logic at the node checkpoint.
        Transforms raw vector evaluations into an unambiguous System State classification.
        """
        # Run input sanitization checks at runtime
        self._validate_score(s1, "Core Consignment Telemetry (S1)")
        self._validate_score(s2, "Lymph Node/Tissue Morphometrics (S2)")
        self._validate_score(s3, "Spatiotemporal Logistics Latency (S3)")

        # Execute deterministic state mapping equation
        cbi: float = round(
            (s1 * self.W1_TEMPERATURE) + 
            (s2 * self.W2_MORPHOMETRICS) + 
            (s3 * self.W3_LATENCY), 
            4
        )

        # Finite State Machine routing rules
        if cbi < 0.40:
            state = "SAFE"
        elif 0.40 <= cbi <= 0.65:
            state = "WARNING"
        else:
            state = "CRITICAL_ALERT"

        return cbi, state
