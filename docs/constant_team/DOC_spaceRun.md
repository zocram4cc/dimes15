# PES 2015 AI Documentation: spaceRun.txt

This file defines the primary offensive logic for finding and exploiting open space. It is divided into scenarios: Chance (Buildup), Counter (Fast break), Flow (Circulation), and Second (Late box arrival).

---

## 1. Scenario Modifiers
- **_chance**: Thresholds for runs during sustained possession in the final third.
- **_counter**: Thresholds for high-speed runs during transitions.
- **_second**: Logic for "late arrivals"—usually midfielders making runs into the box while forwards occupy the defense.
- **_flow**: Soft runs intended to keep the ball moving when no penetration is possible.

## 2. Spatial Constraints
- **angleDiff / angleWidth**: Geographic rules for the run to ensure it provides a clear passing lane from the ball carrier.
- **checkBallDist**: Radius around the carrier; prevents teammates from cluttering the ball carrier's space.
- **checkOffsideLineDistX**: How close the runner is allowed to get to the last defender before curving or slowing down.
- **checkZ**: Lateral width requirements for the run.

## 3. Decision Metrics
- **checkScore / _flow / _good**: Internal ratings for "space quality." Factors in the distance to defenders and the "openness" of the receiving sector.
- **checkInterceptScore**: Rejection threshold; if an opponent is likely to intercept the pass, the run is cancelled.
- **supportTime**: The "patience" of the runner—how long they will hold an attacking position before resetting.

## 4. Search & Vision
- **searchCount / _good**: The frequency of the AI's "scouting" scans for open space.
- **sectorDist**: The resolution of the AI's space grid; determines how granularly it analyzes the pitch for holes.
