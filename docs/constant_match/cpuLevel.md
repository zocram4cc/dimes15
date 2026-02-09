# PES 2015 AI Documentation: cpuLevel.txt

This file defines the AI's tactical competency across the game's difficulty levels. Each variable is an array where the index corresponds to the difficulty level (e.g., 0=Beginner, 1=Amateur, ..., 5=Superstar).

## 1. Offensive Decision Making
- **bpDirectPlay**: Propensity for vertical, direct attacking play. Higher levels prioritize penetration over lateral safety.
- **bpDribbleAddWait**: The "thinking time" penalty applied to the AI ball carrier. Higher difficulties have lower wait times, making the CPU react faster to defender movements.
- **bpDribbleBreakThrough**: Weighting for attempting a solo run or sprint-burst past a defender.
- **bpPassAddWait**: Decision-making latency for passing.
- **bpPassBackSpace**: Weighting for playing safe passes backward to maintain possession.
- **bpShootControlCurve**: Accuracy bias for controlled/finesse shots.

## 2. Defensive Engagement
- **dfMark**: Defensive marking tightness. Controls the proximity at which AI defenders stick to their marks.
- **dfPress**: Aggression of the AI's physical pressing.
- **dfSlidingTackle**: Probability of the AI attempting a sliding tackle. Increases significantly at higher difficulty levels.
- **dfPassCourseCut**: Sensitivity to passing lanes. Controls how often the AI attempts to step in and intercept.

## 3. Team Dynamics
- **obCounterRun**: Frequency of supporting runs during fast transitions.
- **obLineBreak**: Bias for strikers to sit on the shoulder of the last defender.
- **tmSubConcept**: Weighting for advanced tactical sub-concepts (e.g., Target Man support, Wing play).