from enum import IntEnum, unique

@unique
class MultiWiiBox(IntEnum):
    """Represents the various boxes that can be checked."""
    Arm       = 0
    Angle     = 1
    Horizon   = 2
    Baro      = 3
    Vario     = 4
    Mag       = 5
    HeadFree  = 6
    HeadAdj   = 7
    CamStab   = 8
    CamTrig   = 9
    GpsHome   = 10
    GpsHold   = 11
    Passthru  = 12
    Beeper    = 13
    LedMax    = 14
    LedLow    = 15
    LLights   = 16
    Calib     = 17
    Governor  = 18
    OsdSwitch = 19
    Mission   = 20
    Land      = 21

@unique
class MultiWiiBoxState(IntEnum):
    """Represents the aux state values for an MSP box item."""
    Empty = 0
    Low   = 1
    Mid   = 2
    High  = 3
