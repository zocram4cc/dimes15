# PES 2015 AI Documentation: support.txt

This file governs "Support" logic—how teammates position themselves relative to the ball carrier to create passing lanes and maintain possession.

---

## 1. Proximity & Tethers
- **supportDist / supportDistSituation**: The optimal distance a teammate maintains from the ball carrier to be an "easy" option.
- **baseDistMax / distMax**: The radius within which a player is active in the "support" role. Players outside this distance prioritize their Base Position coordinate instead.
- **distRequestPass**: Proximity threshold for the "call for ball" animation and logic.

## 2. Geometric FOV
- **angleMax / angleMaxFront**: The horizontal boundaries for support. Teammates will move laterally to stay within the ball carrier's vision and out of a defender's cover shadow.
- **angleSubAbsMax**: The maximum allowed deviation from the carrier's direct line of sight.

## 3. Movement Intensity
- **distDash / Jog / Run**: Distance-based locomotion rules. Determines the physical effort a player uses to keep pace with the buildup play.
- **distDashQuick / distXDashQuick**: "Panic" or "Urgency" thresholds used during rapid counter-attacks or solo sprints by the ball carrier.

## 4. Line Connection
- **upperConnectionParam / lowerConnectionParam**: Vertical links between team lines. These ensure that if a striker pushes forward, the midfield follows closely enough to provide a second ball option.
- **spaceRectLength / thicknessPillar**: Internal geometry definitions used to define the "passing lane" volume.
