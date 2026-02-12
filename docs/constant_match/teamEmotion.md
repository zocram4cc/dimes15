# constant_match: teamEmotion (Event-Based Momentum)

The `teamEmotion` system is an event-driven momentum engine. It maps specific match actions to psychological "Heart" shifts, which are then translated into stat modifiers by `motivation.o`.

## Home vs. Away Gauge Logic

The variables `home_` and `away_` in this file do **not** refer to the stadium location. They refer to the direction the momentum gauge is swinging:

*   **`home_`**: Controls the **positive** momentum swing (e.g., after scoring a goal).
*   **`away_`**: Controls the **negative** momentum swing (e.g., after conceding).

The game simulates "Home Field Advantage" by giving the designated home team more generous positive swings and less punishing negative swings.

## Event Triggers & Structure

The file is a lookup table indexed by 4-byte ASCII strings for 21 unique match events. When an event like `'GOAL'` occurs, the engine applies the momentum values defined in its corresponding block.

| Event Key | Description |
| :--- | :--- |
| `'GOAL'` | Scoring a goal. |
| `'GOAL_OWN'` | Conceding an own goal. |
| `'SHOOT'` | Attempting a shot. |
| `'COUNTER'`| Initiating a counter-attack. |
| `'TAKING_BALL'`| Winning possession. |

Each event block contains a scaling struct:

*   **`home_max / away_max`**: The momentum "burst" for a positive/negative event.
*   **`home_mid / away_mid`**: The neutral equilibrium point.
*   **`home_lmt / away_lmt`**: The absolute cap for that event's impact.
*   **`gage`**: The fill/decay rate of the meter.
*   **`downPointMin`**: The minimum momentum penalty for a negative event.

## Connection to `motivation.o`

`teamEmotion` tracks the gauge, while `motivation.o` applies the effects.
*   **`motivation.o,effect_up` (1.05)**: Applies a +5% stat boost when the gauge is in the positive (`home_`) zone.
*   **`motivation.o,effect_down` (0.95)**: Applies a -5% stat penalty when the gauge is in the negative (`away_`) zone.