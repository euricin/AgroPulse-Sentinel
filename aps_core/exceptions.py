"""
Custom domain exceptions defining core architectural validation bounds for APS.
"""

class BiosecurityException(Exception):
    """Base domain exception for all structural runtime errors within the APS application layer."""
    pass


class InvalidSeverityScoreError(BiosecurityException):
    """Raised when an edge evaluation index score breaks the required structural boundaries [0.0, 1.0]."""
    pass


class LedgerTamperingError(BiosecurityException):
    """Raised when decentralized state engine validation finds an unauthenticated block state manipulation."""
    pass
