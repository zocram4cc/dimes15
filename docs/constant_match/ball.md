# PES 2015 AI Documentation: ball.txt

This file contains the constants for the ball physics engine, controlling aerodynamics, bounce, roll, and spin.

## 1. Aerodynamics & Drag
- **airRegistNormal**: Base air resistance. Determines how quickly the ball loses velocity while traveling through the air.
- **dragSpeedMax / Min**: Speed thresholds for drag calculation.
- **magnusRate**: Global multiplier for the Magnus Effect (ball swerve). Controls how much the ball curves during flight.

## 2. Bounce & Rebound (The "Bound" cluster)
- **boundRate**: Coefficient of restitution. High values make the ball "bouncier."
- **boundBoundSpeedMax / Min**: Speed limits for vertical bounce energy retention.
- **boundCheckBoundAddRate / FrictionAddRate**: Modifiers for energy loss when the ball strikes the pitch at an angle.
- **boundRotationDecRate**: How much spin is lost upon ground impact.

## 3. Surface Interaction & Roll
- **bitchCondition**: Likely a typo for "Pitch Condition." Controls friction multipliers based on weather (dry/wet).
- **frictionBoundRate / frictionRollRate**: Surface friction modifiers.
- **grounderSpeed / grounderCTan**: Physics for low-trajectory "grounder" balls.
- **naturalRoll / rollToBoundAdd**: The transition from a bouncing ball to a rolling ball.

## 4. Spin Dynamics
- **backSpinBuoyancyRate / backSpinLogRate**: The "lift" effect of backspin on long balls.
- **topSpinChangeSpeed / DownDecRate / RiseDecRate**: How top-spin affects the ball's dip and speed.
- **nonSpinMax / Min / Rate**: Physics for "knuckleballs" or low-spin shots, determining erratic movement.

## 5. Technical Controls
- **rotationCustom / speedCustom**: Bit-packed hooks for specific physics overrides.
- **stopSpeed**: The velocity floor below which the ball is considered stationary.
