# PES 2015 AI Documentation: Defensive Actions (Tackle & Sliding)

These files control the physical execution and risk assessment of defensive interventions.

## 1. tackle.txt
- **animeAccelLimitSpeed**: Speed multiplier for the tackle animation.
- **animePlaybackSpeedHighest / Lowest**: Limits on animation speed to ensure physical realism.
- **animePressTackleEnableAngle**: The required body orientation relative to the ball to allow a standing tackle.
- **animeShoulderCutFrame**: The specific frame where shoulder-to-shoulder contact transitions into a potential foul or ball recovery.
- **animeStepMoveAutoTackle**: Probability of the AI performing an automatic lunge from a medium or long distance.

## 2. sliding.txt
- **animeAccelLimitSpeed**: The speed threshold required to trigger a sliding tackle.
- **animeAdjustLimitAngle**: The allowed directional correction during the slide animation.
- **animeEnterSpeed**: The momentum carryover when entering the slide.

## 3. block.txt (Defensive Blocking)
- **check_SaftyRate**: Internal calculation of "Risk vs Reward." High values mean the AI will only tackle if it is 100% sure of getting the ball.
- **saftyRate_FarDist / NearDist**: Proximity modifiers for the safety calculation.
- **tackleThinkDisableToTrap**: A flag that prevents the AI from attempting a tackle while it is still processing a ball-trapping animation.
