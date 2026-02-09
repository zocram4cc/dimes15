# PES 2015 AI Documentation: defenceCover.txt

This file governs "Covering" behavior—the logic that triggers an AI player to leave their designated zone to support a beaten teammate or fill a tactical gap.

---

## 1. Covering Parameters
- **coverAngle / coverDfAngle**: The FOV/Angle within which a defender will detect a need to provide cover.
- **coverAdjustDist / coverDist**: The maximum range a player is allowed to move from his base coordinate to support a teammate.
- **minCoverDist**: The minimum size of a tactical "hole" required to trigger a covering run.
- **adjustAngleRate**: The speed/sensitivity of body re-orientation when shifting into a covering stance.

## 2. Lane & Run Cutting
- **baseAngleCutLongitudinal / Side**: Orientation rules for the defender depending on whether the threat is central or wide.
- **baseAngleOneSideCutRev**: Body rotation weighting when the AI is trying to force an attacker toward a specific direction (usually the sideline).

## 3. Line Discipline
- **limitDistX_MfLine**: A hard longitudinal (depth) limit to prevent midfielders from "crashing" into the defensive line while covering.
- **mfLimitRate**: Urgency multiplier for midfielders when performing defensive cover duties.
- **diffTargetLineX / Continue**: Allowed deviation from the base D-Line height while the player is actively covering a run.
