# PES 2015 AI Documentation: playStyle.txt (Playing Styles)

This file contains the statistical weighting for individual **Playing Styles** (Target Man, Hole Player, etc.).

## 1. Style Priorities
The values in the `style[]` array are weights that override the team's base tactical setup (`basePosition.txt`).
- **High Weights**: Force the player to prioritize their card-specific behavior (e.g., a "Goal Poacher" ignoring the `dfLine` to stay forward).
- **Style Archetypes**:
    - **Target Man**: Increases the weight of the "Long Ball Support" and "Shielding" logic.
    - **Hole Player**: Increases the weight of `spaceRun_chance` and `pullAway` logic.
    - **Anchor Man**: Decreases the weight of `mfPushUpRate`, keeping the player between the defense and midfield.

## 2. Statistical Thresholds (kind[])
The `kind[]` array likely maps to specific attribute requirements. Players only use their playing style if their relevant attributes (e.g., Attacking Prowess, Defensive Awareness) exceed these internal thresholds.