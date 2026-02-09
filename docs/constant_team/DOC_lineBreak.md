# PES 2015 AI Documentation: lineBreak.txt

This file defines the behavior of "Goal Poachers" and "Line Breakers"—players who focus on beating the offside trap and making runs behind the defensive line.

---

## 1. Gap Analysis
- **searchCount / _lineBreaker**: The frequency and depth of the AI's search for gaps in the opponent's defensive line.
- **checkAreaScore / _lineBreaker**: The scoring system used to evaluate the potential of a run. High scores = high-risk, high-reward space.

## 2. Stealth & Visual Awareness
- **checkBodyAngleEyesOff / _lineBreaker**: The orientation of the runner's body to move into a defender's blind spot.
- **checkSideAngleEyesOff**: The "shoulder check" logic used to track the last defender while preparing a sprint.

## 3. Interception Prediction
- **checkInterceptScore**: An evaluation of whether a through-pass is likely to be intercepted. Strikers with higher intelligence stats will only run if the pass "lane" is statistically viable.
- **checkDistEyesOff**: The proximity threshold where the runner stops looking at the ball and starts looking only at the "breakaway" point.
