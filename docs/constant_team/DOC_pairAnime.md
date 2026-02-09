# PES 2015 AI Documentation: pairAnime.txt

This file governs "Pair Animations"—physical interactions where two players collide or interact, including jostling, shielding, and aerial duels.

---

## 1. Interaction Physics
- **moveContact**: The proximity threshold that triggers a physical interaction state rather than standard movement.
- **paraDiff / paraDown**: Calculation weights for player stats (Strength, Balance) that determine who wins a physical collision or shoulder-barge.
- **defenceIdealRot**: Target orientation for defenders to maximize their leverage during a jostle.

## 2. Timing & Persistence
- **decideTiming**: The interval at which the AI recalculates the outcome of a physical struggle.
- **moveSec / minSec / maxSec**: Constraints on how long two players can be "locked" in a contact animation.
- **margin**: Hitbox buffer to prevent players from clipping through each other during animations.

## 3. Specialized States
- **highballEnable**: Activates physical interaction logic for headers and aerial duels.
- **dropOut**: Decides when a player should give up on a physical interaction (e.g., if they are significantly weaker or the ball is moving away).
- **pes15Test...**: Legacy test values from the transition to the PES 2015 physics engine.
