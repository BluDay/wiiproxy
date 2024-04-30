from .  import _MultiWiiData, command_code, struct_format
from .. import MSP_BOX

from typing import NoReturn

@command_code(MSP_BOX)
@struct_format('H', has_variable_size=True)
class MspBox(_MultiWiiData):
    """Represents data values for the MSP_BOX command."""

    """
    # ---------------------------------- INSTANCE VARIABLES ------------------------------------

    _values: tuple[int]

    # ------------------------------------- MAGIC METHODS --------------------------------------

    def __init__(self) -> NoReturn:
        \"""Initializes a new instance with default values.\"""
        self._values = None

    # -------------------------------------- PROPERTIES ----------------------------------------

    @property
    def values(self) -> tuple[int]:
        \"""Gets the main values.\"""
        return self._values

    # ----------------------------------- INSTANCE METHODS -------------------------------------

    def _evaluate_raw_data(self) -> NoReturn:
        \"""Updates the current values by the provided unserialized data bytes.\"""
        pass
    """
    pass