# PES 2015 AI Documentation: centeringGet.txt

This file governs "Centering" (Crossing) reception behavior—how attackers position themselves in the opponent's penalty area to receive a cross.

---

## 1. Receive Patterns (centeringGetPattern)
An array of weights defining the movement archetypes for players in the box.
- **centeringGetPattern[0..3]**: Each index likely corresponds to a specific tactical movement:
    - **Near Post Run**: Attacker sprints to the front edge of the 6-yard box.
    - **Far Post Run**: Attacker drifts to the back post to exploit space behind the defenders.
    - **Late Run (Cut-back)**: Midfielder arrives at the penalty spot or edge of the box.
    - **Holding Position**: Attacker stays stationary to shield defenders or wait for a direct header.

By adjusting these weights, the frequency of specific crossing tactics can be controlled at the team level.
