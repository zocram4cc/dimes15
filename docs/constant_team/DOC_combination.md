# PES 2015 AI Documentation: combination.txt

This file controls "Combination Play"—the tactical logic that triggers one-twos (wall passes), overlaps, and complex teammate runs. It defines the distance and FOV requirements for the AI to "see" a potential passing combination.

---

## 1. Trigger Conditions (The "Wedge" Logic)
The ball carrier looks for partners within a triangular "wedge" zone to initiate a combo.
- **checkDist**: Maximum distance to a teammate allowed to trigger a combination.
- **checkWedgeAngle**: The horizontal angle (FOV) the ball carrier scans for teammates.
- **checkWedgeFarX / NearX**: The longitudinal (depth) boundaries relative to the carrier where the receiver must be.
- **checkWedgeOffsideX**: Safety margin to prevent combinations that would lead to an immediate offside call.
- **checkZ**: The maximum lateral (width) distance allowed between carrier and partner.

## 2. Combination Patterns (combs Arrays)
Specific patterns defined for different contexts.
- **combsCom**: Computer-specific patterns used when the AI is in control.
- **combsSide**: Logic specific to wing-play and overlaps by fullbacks or wingers.
- **area**: Pitch zone where the move is valid (e.g., Final Third).
- **kind**: The specific move type:
    - *Common Mapping*: Overlap, Wall Pass (One-Two), Inner Run, Third Man Run.
- **combs**: General index for the move definitions.

## 3. System Variables
- **useJson**: Toggle for external configuration loading (usually disabled).
- **UNKNOWN**: Internal indices for animations or hard-coded movement style overrides.
