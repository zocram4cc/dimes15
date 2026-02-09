# PES 2015 AI Documentation: selectorVision.txt

This file acts as a traffic controller for offensive movement, determining the priority and maximum frequency of different types of attacking runs.

---

## 1. Run Offering Quotas (offerNum)
Defines the maximum participation for specific movement patterns to maintain team shape.
- **offerNum_diagonalRun**: Priority/quota for diagonal cutting runs.
- **offerNum_lineBreak**: Priority/quota for poacher runs behind the defensive line.
- **offerNum_pullAway**: Priority/quota for runs that create passing lanes by shedding markers.
- **offerNum_spaceRunChance**: Participation limit for general runs into open space during possession.
- **offerNum_spaceRunCounter**: Participation limit for explosive runs into space during a counter-attack.
- **offerNum_spaceRunSecondLine**: Controls late runs from midfield into the opponent's box.

## 2. Priority Logic
- The integer values assigned to these variables represent weights within the AI's selection engine. Higher weights ensure that certain run types (like counter-attack runs) take precedence over others when tactical conditions are met.
