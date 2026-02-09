# Dimes15 - Patch Notes

This patch focuses on enhancing team positioning, defensive integrity, and transition urgency. By refining the underlying tactical constants, we have eliminated passive AI behaviors and enforced a more aggressive, cohesive unit structure.

## 1. Defensive Line & Positional Integrity

*   **Depth & Retreat Limits**: 
    *   Base line height (`dfLine`) increased from **10** to **12**.
    *   Maximum retreat distance (`adjustDefenceLine_Retreat`) restricted from **-7.0** to **-4.0**.
    *   **Intended Effect**: Maintains a permanently higher block and prevents defenders from dropping too deep into their own box under pressure.
*   **Retreat Inertia & Closing Rate**: 
    *   Retreat weight (`dfLineBack`) reduced from **10.0** to **6.0**.
    *   Forward closing rate (`dfLineCloseRate`) increased from **0.5** to **0.65**.
    *   **Intended Effect**: Eliminates the "bottling" behavior where defenders sprint away from approaching strikers; forces the line to actively "squeeze" the ball carrier once they enter the defensive third.
*   **Block Compactness**: 
    *   Lateral width of the backline (`dfLineWidth`) reduced across all formations (approx. 15%).
    *   Vertical connection tethers (`lowerConnectionParam` / `upperConnectionParam`) tightened and optimized. `upperConnectionParam` refined to **78.0**.
    *   **Intended Effect**: Clogs the center of the pitch to force the opponent wide and ensures the three lines (DF, MF, FW) move as a single, cohesive unit.

## 2. Physical Engagement & Challenge Logic

*   **Extended Sliding Range**: 
    *   Maximum AI slide distance (`slideDistMax`) increased from **25.0** to **30.0**.
    *   Lateral tackle width (`slideWidth`) expanded from **3.0** to **4.5**.
    *   **Intended Effect**: Enables the "murderslide"—allowing AI to attempt and win sliding tackles from distances previously considered impossible or out of range.
*   **Engagement Speed**: 
    *   Observation delay before challenging a dribbler (`adjustDribbleWaitTimer`) reduced from **10.0** to **8.0**.
    *   Global challenge wait time (`maxWaitTime`) diminished to **28.0**.
    *   **Intended Effect**: Forces defenders to commit to a tackle or press immediately, removing the passive "standing off" phase.
*   **Jockeying Thresholds**: 
    *   Vertical coordinate for the "Match-Up" stance (`matchUpStartLine`) pushed from **10.0** to **15.0**.
    *   Safety margins for sliding (`slideJudgeWidthMargin`) increased to **13.0**.
    *   AI prediction window (`predictionFrame`) refined to **39**.
    *   **Intended Effect**: Defenders begin jockeying strikers much earlier in the midfield and are significantly more willing to attempt risky lunges with sharper predictive timing.

## 3. Marking & Zonal Discipline

*   **Proximity & Pick-up**: 
    *   Base proximity to the mark (`approachRateMax`) increased from **50.0** to **55.0**.
    *   "Alertness" radius for runners (`zoneMarkXLimit` / `zoneMarkZLimit`) expanded from **15.0** to **17.0**.
    *   **Intended Effect**: Ensures defenders "cling" to strikers more tightly and recognize overlapping runs much sooner.
*   **Tracking Discipline**: 
    *   Defensive tracking persistence (`markContinueDist`) set to **16.0**.
    *   Double-teaming proximity (`maxSandDist`) expanded to **16.0**.
    *   **Intended Effect**: Maintains defensive shape by ensuring tracking discipline while allowing for coordinated pressure within a wider radius when appropriate.

## 4. Transition & Vertical Urgency

*   **Maximum Verticality**: 
    *   Transition priority on the X-axis (`transitionPriorityX`) increased from **1** to **3**.
    *   **Intended Effect**: Instructs the entire team to ignore horizontal regrouping upon winning possession. All available players immediately trigger maximum-speed sprints toward the opponent's goal to facilitate rapid, overwhelming counter-attacks.