# PES 2015 AI Documentation: basePosition.txt

This file defines the tactical "skeleton" of the team. It controls the base coordinates where players stand relative to the ball, the opponent, and each other.

## Coordinate System
- **X-Axis**: Longitudinal (Goal-to-Goal). Positive usually moves toward the opponent's goal.
- **Z-Axis**: Lateral (Width). Positive/Negative defines distance from the center-line of the pitch.
- **Y-Axis**: Height (not used in this file).

---

## 1. Defensive Line (D-Line) & Offside Logic
Controls the depth of the defense and how it reacts to pressure.
- **dfLine**: The base height of the defensive line.
- **adjustDefenceLine_ForeCheck / _Retreat**: Modifiers for when the team is pressing high or dropping deep.
- **backOffsideLine**: Prioritizes maintaining a flat line for the offside trap over tracking individual runners.
- **dfLineBack / dfLineRate / dfLineCloseRate**: Speeds and thresholds for the line dropping back when an opponent carries the ball forward.
- **dfLineCenterAdjustMax / Min**: Flexibility allowed for Center Backs (CBs) to step out or drop relative to the Fullbacks.

## 2. Compactness & Width (Lateral Shape)
Controls the side-to-side distance between players.
- **adjustZCompact / adjustZMinCompact**: General lateral compactness (how "tight" the block is).
- **minWidth / minWidth_GoalKick**: Hard floors for team width to prevent overlapping or thinning.
- **adjustSideZ / adjustSideZ_concept_side**: Defines the "width" of Fullbacks (SB) and Wingers.
- **closeSideZRate**: Speed at which the team "slides" laterally toward the wing when the ball is on the flank.
- **adjustZOneSideCut**: Amount of lateral shift applied when a winger is instructed to cut off a passing lane.

## 3. Line Aggression & Vertical Movement
How the lines (DF, MF, FW) push and pull vertically.
- **adjustFwLine**: Base height of the striker line.
- **mfPushUpRate / mfPushUpRate_offencive**: The aggression of the midfield. High values cause the MF line to join the attack faster, potentially leaving gaps.
- **sideBackPushUpRate**: Frequency and depth of Fullback overlaps.
- **minDistMF_DF / minDistMF_FW**: Buffer zones to prevent different lines from colliding or getting too close.

## 4. Transition Logic
What happens during the "Moment of Transition" (Turnovers).
- **transitionOpenZ**: How much the team spreads out laterally to create passing lanes the moment possession is won.
- **transitionPriorityX**: Determines if players should prioritize vertical sprinting (Counter-attack) or maintaining shape (Possession).
- **transitionSec / transitionSmooth**: Timers and curves for shifting from a defensive block to an attacking shape.

## 5. Set-Play Positioning
Overrides for static ball situations.
- **adjustAngle_FreeKickSupport**: Angle of support players relative to the FK taker.
- **adjustX_FreeKick / adjustZ_FreeKick**: Longitudinal/Lateral offsets for the team block during a FK.
- **gklBaseX / gksBaseX**: Team height during Long (gkl) and Short (gks) Goal Kicks.
- **throwinLengthDf / throwinWidthZ**: Team shape during opponent throw-ins.

## 6. Player Awareness & Connection
- **upperConnectionParam / lowerConnectionParam**: "Tethers" that define the maximum distance between lines. If the ball exceeds this distance, the whole team shifts.
- **adjustReturnDist**: The "leash" distance—how far a player can wander before being forced back to his base position.
- **adjustSpaceCoverRate**: Weighting between marking an opponent and covering empty space.

## 7. State & Technical Hooks
- **isAdverse**: Multiplier triggered when the team is losing or under heavy pressure.
- **isUseDashSituation**: Speed threshold for when players are allowed to sprint to reach their positions.
- **xposiRateCustom**: End-of-file hook likely for individual Player-Style overrides from the EXE.
- **defenceFormationTest1 / Test2**: Legacy development flags for formation logic.
