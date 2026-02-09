# PES 2015 AI Documentation: blockDebug.txt

This file defines internal parameters for physical interactions and decision-making for both attacking and defensive scenarios. It contains many bit-packed variables (HEX).

## 1. Defensive Parameters
- **fishDive**: Parameters controlling the goalkeeper's or defender's "diving" physics during a block or save attempt.
- **heel**: Specific logic for "heel" touches or defensive clearances using the back of the foot.
- **keeperCheck / keeperCheckStyle / keeperStartParam**: Evaluation logic for goalkeeper positioning and reaction starting points.
- **moveKind / moveMode**: The internal locomotion archetype used by the AI during a block attempt.

## 2. Offensive (Kick) Parameters
- **kickAuto**: Automatic kick logic, including range checks (`checkXRate`, `checkZ`) and a general enable flag.
- **kickDebug**: Parameters for simulating and testing kick physics (`adjustY`, `adjustZ`).
- **kickPointBall / kickPointDirect / kickPointGoal**: Geometry for target selection—where on the ball to strike, whether to hit first-time (Direct), and the target point within the goal frame.
- **kickPosition**: The required body orientation (`angle`) and proximity (`dist`) to the ball to initiate a kick.
- **shootKind**: Categorization of the shot (e.g., power shot, placed shot, chip).
- **shootKpDist**: Kick Point Distance—how far the foot travels during the striking animation.

## 3. General Logic
- **dribbleAiThink / dribbleStart**: Decision thresholds for when the AI should transition from carrying the ball to attempting a shot or pass.
- **retry**: Logic for re-calculating a physical interaction if the first attempt fails due to collision or clipping.
