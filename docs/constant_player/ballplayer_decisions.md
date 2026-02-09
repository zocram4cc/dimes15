# PES 2015 AI Documentation: Ball Carrier Decision Making

These files handle how the player in possession of the ball evaluates their options for dribbling, passing, and shooting.

## 1. ballplayerDribble.txt
- **DashCheckSecotor**: The field of view scanned for defenders while the sprint button is held.
- **enemySearchAngle**: Sensitivity to nearby markers. High angles cause the AI to abandon a dribble sooner if pressured.
- **distDecideAngle**: The distance at which the AI locks in a dribbling exit vector.
- **MatchUp / Burst**: Logic for one-on-one duels:
    - **angleSubMax**: Maximum allowed deviation from the goal-line while trying to beat a man.
    - **enemyFutureFrame**: Prediction window for defender movement.
    - **startDist**: Distance required to trigger a sprint burst.

## 2. ballplayerPass.txt
- **BackSpaceInfo**: Preference for safe, backward recycling passes.
- **CrossInfo / EarlyCrossInfo**: Weighting for different crossing archetypes.
- **OneTwoInfo**: Evaluation of wall-pass viability.
- **SideChangeInfo**: Propensity for long, horizontal "switch" passes to the opposite wing.

## 3. ballplayerShoot.txt
- **CourseEvaluateInfo**: Internal scoring logic for shot quality.
- **radiusEnemyCircleMax / Min**: Pressure zones. Defines how close a defender must be to apply a penalty to the shot's accuracy and composure.
- **rateAddGKCircle**: Intimidation multiplier for a rushing goalkeeper.
- **GoalFrontInfo / LongRangeInfo**: Power and type thresholds based on distance to goal.
- **LoopInfo**: Conditions for attempting a lob or chip finish.