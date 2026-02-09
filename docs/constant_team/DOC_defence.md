# PES 2015 AI Documentation: defence.txt

This file handles individual and small-group defensive behavior, specifically focusing on "Match-Up" (jockeying), lane cutting, and pressing intensity.

---

## 1. Match-Up Logic (Jockeying)
Controls the stance and positioning of a defender tracking a ball carrier.
- **matchUpStartLine / Max**: The pitch height where defenders begin prioritizing the "Match-Up" (L2/RT) stance.
- **matchUpLimitDistDefensiveAwareness0 / 1**: Stat-based scaling for how close a defender gets before engaging.
- **matchUpBackFollowAngle**: The maximum angle a defender can turn away from the ball to track a runner while remaining in a defensive state.
- **matchUp...XLimit / ZLimit**: Positional boundaries that prevent a defender from being pulled too far out of position while man-marking.

## 2. Lane Cutting & Interception
- **courseCutCheckRange**: The distance within which a defender actively attempts to block potential passing lanes.
- **courseCutTargetDistFar / Near**: The desired "buffer" distance between the defender and the carrier when shadowing a pass.
- **predictionFrame**: How many frames into the future the AI projects player/ball movement to calculate interceptions.

## 3. Group Pressing ("Sandwich" Logic)
- **adjustSandDist / maxSandDist**: Thresholds for the "Sandwich" press, where two AI defenders converge on a single opponent.
- **adjustDribbleWaitTimer**: The "observation" period before an AI defender commits to a lunge or a tackle against a dribbler.

## 4. Systems & Tethers
- **upperConnectionParam / lowerConnectionParam**: Vertical "tethers" between the DF-MF and MF-FW lines specifically during defensive phases. Higher values create a more rigid block.
- **continueAdvantageDelay / Press**: Behavior modifiers used when the referee allows play to continue after a foul.
