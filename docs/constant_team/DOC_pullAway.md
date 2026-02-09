# PES 2015 AI Documentation: pullAway.txt

This file governs "Pulling Away" behavior—offensive runs designed to shed a marker and create a clean passing lane, usually in the midfield or final third.

---

## 1. Proximity Thresholds
- **checkBallDist / _good**: Distance from the ball carrier allowed to initiate a pull-away run. Players with "Incisive Run" traits use the "good" values.
- **checkLastLineDist / _good**: Proximity to the defensive line; prevents runs from being made too deep or too shallow to be effective.
- **checkBallDistBP**: Tether distance to the player's base tactical position.

## 2. Lateral Movement
- **checkZ / _good**: Lateral deviation allowed during the run to find a pocket of space.

## 3. Run Logic
- **angleDiff / _good**: Target angle for the run relative to the marker's current position.
- **eyeOff**: Determines if the player scans the field instead of tracking only the ball during the run.
- **lastLine**: A toggle prioritizing runs made against the opponent's last defender.
