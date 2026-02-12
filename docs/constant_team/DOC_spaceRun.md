# constant_team: spaceRun (Chance Creation)

Governs how teammates move into space to receive passes or create goal-scoring opportunities.

## Hole Player & Enhanced Runs (_good)

Variables suffixed with `_good` are primarily activated by the **Hole Player** Playing Style when the player is in a compatible position (AMF, CMF, LMF, RMF). They can also be triggered temporarily for all players during certain match states (e.g., counter-attacks).

This was previously thought to be linked to the "Incisive Run" COM style, but code tracing has proven this incorrect.

| Variable | Description | Default | _good (Hole Player) |
| :--- | :--- | :--- | :--- |
| `chanceScore` | Minimum quality score to trigger a "Chance" run. | 100 | 85 (More frequent) |
| `checkAngleWidthSector` | The width of the cone the player scans for space. | 30 | 50 (+67% wider) |
| `checkAreaNum` | Number of potential run paths evaluated by the AI. | 2 | 4 (+100% options) |
| `searchCount` | Number of times the AI re-evaluates its run path. | 4 | 6 (+50% re-evaluations)|
| `supportTime` | Frames until a support run is initiated. | 3 | 2 (33% Quicker) |

## Strategic Implications

*   **The "Hole Player" Advantage**: The `_good` system is what makes Hole Players so effective at finding space. They scan wider areas, consider more options, and react faster than any other playing style.
*   **Situational Boosts**: Because these values are also triggered situationally for all players, increasing the gap between `base` and `_good` values will make counter-attacks more explosive for the entire team, while still giving Hole Players a permanent edge.