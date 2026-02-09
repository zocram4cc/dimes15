# PES 2015 AI Documentation: overlap.txt

This file governs Fullback (Side Back) overlaps, determining the conditions under which defensive players join the attacking phase on the wings.

---

## 1. Trigger Depth
- **checkTopLineX / checkMiddleLineX**: The vertical position of the ball carrier required to trigger a fullback's forward run.
- **..._adverse**: Modified triggers for "Under Pressure" or "Losing" states, typically making overlaps rarer to prioritize defense.

## 2. Participation Limits
- **addCount**: The limit on how many players can perform an overlapping run at the same time.
- **addCount_adverse**: Usually lower than standard, restricting attacking runs during high-pressure phases.

## 3. Movement Logic
- **style**: Determines the run path (e.g., sticking to the touchline vs. underlapping into the half-space).
