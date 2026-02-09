# PES 2015 AI Documentation: avoid.txt & Locomotion

This file handles collision avoidance and basic physical locomotion constraints for individual players.

## 1. Physical Turning & Agility
- **angleDelta / angleVelocity**: The maximum degrees per frame a player can rotate while maintaining speed. High values result in "twitchy" movement; low values simulate physical inertia.
- **subtleAngleSub**: Small adjustment buffer for precision movement in tight spaces.

## 2. Distance Buffers (Clipping Avoidance)
- **distDefence**: The minimum personal space maintained when near an opponent.
- **distInner**: The "hitbox" radius for teammates. Helps prevent players from walking through each other.
- **distShort**: Threshold for switching from jogging to walking/precision touch.

## 3. State Transition Timers
- **cornerKickTime / goalKickTime / penaltyKickTime**: The delay (in seconds) between the ball stopping and the set-piece animation state becoming active.
- **transitionTime2 / 3**: Timers controlling how quickly a player can shift between high-intensity states (e.g., from a fall to a recovery sprint).
