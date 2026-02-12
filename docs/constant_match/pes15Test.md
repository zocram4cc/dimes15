# constant_match: pes15Test (1vs1 & Kick Physics)

The `pes15Test` system is a relational tactical table governing the logic for 1vs1 physical engagements and the timing of user-controlled kick gauges. 

## Structure

Unlike standard tactical files, `pes15Test` uses a pointer-based structure where the header defines offsets to specific behavioral sub-blocks.

### 1. 1vs1 Engagement Logic (`p1vs1`)

These variables control how the AI reacts to dribblers and how it manages defensive pressure.

| Offset | Functional Mapping | Description |
| :--- | :--- | :--- |
| `Data_48-76` | **Press Update** | Determines the frequency of AI positional adjustments during defensive pressing. Higher values cause a more "stuttery" press, while lower values are more fluid. |
| `Data_80-108` | **Wait Timer** | The "observation delay" before an AI defender commits to a physical challenge. Lowering these values makes the AI more aggressive and decisive in 1vs1s. |
| `Data_80` | `decelerateThreshold` | The speed at which a defender begins to slow down to enter a "Match-Up" or jockeying stance. |

### 2. Kick Gauge Physics (`projectKick`)

Governs the visual and physical behavior of the power bar during passes and shots.

| Offset | Functional Mapping | Description |
| :--- | :--- | :--- |
| `Data_112` | `gageSpeed.cross` | The fill rate of the power bar during crosses. |
| `Data_120` | `gageSpeed.shoot` | The fill rate of the power bar during shots. Higher values = faster power build-up. |
| `Data_128` | `gageSpeed.through` | The fill rate for through balls. |

## Strategic Editing

*   **Aggressive AI**: To make the AI more challenging in defense, focus on the `Wait Timer` section (Data 80-108). Reducing these values eliminates the "standing off" behavior often seen in lower difficulties.
*   **Responsive Kicking**: If the power bar feels too sluggish or too sensitive, adjust the `projectKick` values (Data 112+) to match your preferred gameplay pace.
