# PES 2015 AI Documentation: diagonalRun.txt

This file controls diagonal attacking runs, primarily used by forwards and wingers to exploit gaps between center-backs and fullbacks.

---

## 1. Run Geometry
- **angleBase**: The target angle for the diagonal sprint relative to the opponent's goal.
- **fanAngle / Margin**: The "cone" of allowed movement, preventing runs from being rigid straight lines.
- **deltaZMax / Min**: Maximum lateral pitch coverage allowed for a single run.

## 2. Trigger Thresholds
- **distXBpMax**: The distance to the ball carrier beyond which a diagonal run will not be attempted.
- **distXOffsideLineMax / Min**: The required proximity to the last defender to initiate the run (the "danger zone").
- **moveKPHMin**: The speed requirement for the buildup play; diagonal runs aren't triggered if the game pace is too slow.
- **scoreMin**: A tactical "quality" threshold that ensures the AI doesn't waste energy on low-percentage runs.

## 3. Decoy Movement
- **..._dummyRunner**: Variables governing "dummy" or decoy runs. These are typically wider and intended to create space for other teammates rather than to receive the ball directly.
