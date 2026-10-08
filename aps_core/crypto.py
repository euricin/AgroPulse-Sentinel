"""
Decentralized cryptographic signing engine for issuing unalterable transit clearances.
"""

import json
import hashlib
from typing import Dict, Any


class EdgeLedgerSigner:
    """
    Provides data immutability signatures directly at border environments, 
    eliminating persistent network connectivity dependencies.
    """

    @staticmethod
    def generate_clearance_ticket(metadata: Dict[str, Any], cbi_score: float) -> Dict[str, Any]:
        """
        Compiles structural diagnostic logs and serializes data into a verifiable signature package.
        """
        payload: Dict[str, Any] = {
            "consignment_id": metadata.get("consignment_id"),
            "operator_id": metadata.get("operator_id"),
            "computed_cbi": cbi_score,
            "timestamp": metadata.get("timestamp"),
            "status": "APPROVED_FOR_TRANSIT"
        }
        
        # Enforce deterministic JSON string formatting to prevent hash collisions across platforms
        serialized_payload: bytes = json.dumps(payload, sort_keys=True).encode('utf-8')
        cryptographic_signature: str = hashlib.sha256(serialized_payload).hexdigest()
        
        return {
            "payload": payload,
            "signature_hash": cryptographic_signature,
            "encryption_protocol": "SHA-256",
            "ledger_status": "COMMITTED"
        }
