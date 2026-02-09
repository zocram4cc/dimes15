# PES 2015 AI Documentation: setplayGuide... files

These files define the visual aids and the physics limitations during dead-ball situations (Corner Kicks, Free Kicks, Goal Kicks).

## 1. Common Logic (setplayGuideCommon.txt)
- **freekickDebug**: Toggle for internal visualization of kick trajectories.
- **goalKickBackSpin**: Base backspin applied to goal-kick clearances.
- **thinkDistFar / Middle / Near**: The distance categories the AI uses to scan for eligible receivers during a set piece.

## 2. Corner & Free Kicks (CornerKick.txt, FreeKickFar.txt, etc.)
- **gage**: The sensitivity of the power bar. Lower values make the bar fill faster.
- **rot**: A bit-packed cluster (HEX) controlling:
    - **addBackSpin / addHigh**: Modifiers for trajectory arc and ball-lift.
    - **adjustDist**: Dynamic scaling of the kick's target point based on distance.
- **topSpinRot**: Rotation coefficient for "dipping" free kicks.
- **kickPowerParameter**: Min/Max thresholds for shot velocity.
- **sideSpin / reverse**: Coefficients for swerve and "unnatural" curve (Magnus effect multipliers).

## 3. throwin.txt (Throw-ins)
- **longThrowSupport**: Distance and weight for the "Long Throw" trait.
- **distFar / Middle / Near**: Scanning radius for teammates during a throw-in.
- **gageMiddle**: Optimal power bar point for a chest-height throw.
- **speed / adjustDist**: The velocity of the throw-in animation.
