# PES 2015 AI Documentation: command.txt

This file controls the sensitivity, timing, and cancellation logic for user and AI inputs.

## 1. Input Buffering & Cancellation
- **burstR1PullDelete**: Sensitivity for the R1/RB sprint burst. It defines the threshold for "deleting" or overriding a previous move command in favor of a burst.
- **trap**: Logic for "trapping" the ball. Controls if a command can be issued while the player is in a receiving animation.
- **kickCommandCreateButtonPull**: The stick "pull" distance or duration required to trigger a context-sensitive kick type.

## 2. Kick Direction & Timing
- **kickAngleChangeOfferTimer**: The "window" of opportunity (in frames or seconds) for the player to change the direction of a shot or pass after the power gauge has been filled.
- **kickAngleChangeOfferNowAnimeKick**: A specific override flag that allows for directional changes even during the early frames of the kicking animation.
- **shootKickAngleChangeOfferTimer**: Specifically defines the directional adjustment window for shots, which is usually tighter than for passes.
