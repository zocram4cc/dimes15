# PES 2015 AI Documentation: defenceMark.txt

This file controls tight man-marking, zonal boundaries, and the logic for handing off markers between teammates.

---

## 1. Marking Intensity
- **approachRateMax / _buildUp / _side**: Controls how tightly a defender "clings" to an opponent.
- **markContinueDist / _BoxToBox**: The distance a defender will track a runner before letting them go or passing them to a teammate.
- **needMarkDistGKShort**: Marking proximity during short goal-kick situations.

## 2. Positioning & Release
- **backAngleLimitGoal / Side**: Body orientation limits to ensure defenders don't lose sight of the ball/goal while marking.
- **releaseCheckTargetMarkedAngle / Dist**: Thresholds for when a defender decides an opponent is no longer a primary threat or is "covered" by someone else.
- **remainMarkXLimit / ZLimit**: Safety limits to prevent a defender from being lured infinitely far from their base position by a decoy runner.

## 3. Movement & Speed
- **distDash / Jog / Run**: Determines the movement intensity (sprint, jog, or walk) required to keep up with a mark.
- **distDash_course**: Speed logic for "cutting across" to intercept a run.

## 4. Marking Zones
- **zoneMarkXLimit / ZLimit**: The dimensions of the "active zone." Opponents outside this box are ignored in favor of maintaining formation.
- **dfZZoneRange / mfZZoneRange**: Specific zonal widths for Defenders and Midfielders.
- **zoneZRangeAlone**: Expanded marking range for isolated players.
