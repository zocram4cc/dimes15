# constant_team: lineBreak (Attacking Runs)

Governs the logic for players making forward runs behind the defensive line.

## Hole Player Triggers (_good)

This file contains several variables suffixed with `_good`. These are primarily activated when a player has the **Hole Player** Playing Style and is in a compatible position. They can also be activated temporarily for the entire team during specific advantageous game states.

The previous community assumption was that these were linked to the "Incisive Run" COM style; this has been proven incorrect by code tracing.

| Variable | Description | Default | _good (Hole Player) |
| :--- | :--- | :--- | :--- |
| `checkBallDist` | Base trigger distance for a run. | 60.0 | 90.0 (+50% Range) |
| `checkBallDistBP` | Trigger distance from the ball possession point. | 80.0 | 60.0 (Closer, more precise) |
| `angleDiff` | Permissive angle for the run. | 90.0 | 70.0 (Stricter, more direct) |
| `checkZ` | Lateral check distance. | 70 | 40 (Tighter, more central) |
| `checkLastLineDist`| Distance to the defensive line to trigger a run.| 15.0 | 25.0 (+67% Range) |


## Tactical Notes

*   **Hole Player Precision**: The `_good` values for Hole Players are not simply "better"; they are different. They trigger runs from further away (`checkBallDist_good`) but require the player to be closer to the ball (`checkBallDistBP_good`) and run at a more direct, less forgiving angle (`angleDiff_good`). This creates the signature "late, darting run" that characterizes the style.
*   **Situational vs. Permanent**: A key part of balancing the game is deciding how much of a bonus to give Hole Players versus the team as a whole. Increasing the `_good` values buffs both, but only Hole Players will benefit from them consistently.