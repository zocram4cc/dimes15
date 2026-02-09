# PES 2015 AI Documentation: Offensive Skills & Goalkeeping

## 1. shoot.txt (Skill Shots)
- **chipElevation / chipSpeed**: The vertical arc and velocity of chip shots (L1/LB + Shoot).
- **loopElevation / loopSpeed**: Physics for high-arcing lobs or long-distance "rainbow" crosses.
- **nutmegSpeed**: Velocity required to trigger a "panna" animation through an opponent's legs.
- **outAngle / outTrapezoid**: Logic for shots that use the "outside" of the foot.

## 2. passget.txt (Receiving)
- **autoFrontMove**: Determines if the receiver automatically steps toward the ball to meet the pass.
- **pressure**: Bit-packed modifiers for first-touch composure.
- **circleDist**: The radius around the receiver; if a defender is inside this circle, first-touch error is drastically increased.

## 3. gk.txt (Individual Goalkeeping)
- **basePosRateClassicalGk / OffensiveGk**: Positioning bias. Offensive keepers (Sweeper GKs) maintain a higher line.
- **checkFreeRangeGKLongThrow**: Logic for finding an open teammate for a counter-attack throw.
- **throwRangeLong / Normal**: The hard distance limit for goalkeeper distribution by hand.
- **waitTimeAddMax / Min**: The delay the GK uses before clearing the ball to simulate scanning the field.
