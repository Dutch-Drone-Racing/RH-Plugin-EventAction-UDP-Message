# RH-Plugin-EventAction-UDP-Message
Add UDP Messaging to Rotorhazard Event Actions

# Documentation
* Install the EventAction UDP Message Plugin like any other plugin ([RH Plugin Documentation](https://github.com/RotorHazard/RotorHazard/blob/main/doc/Plugins.md))
* The UDP Message option is now available under EventActions in Rotorhazard UI.



Variables to use:

| Variable                  | Description                                                             |
|---------------------------|-------------------------------------------------------------------------|
| %PILOT%                   | Pilot callsign                                                          |
| %HEAT%                    | Current heat name or ID value                                           |
| %ROUND%                   | Current round number                                                    |
| %ROUND_CALL%              | Current round number (with prompt)                                      |
| %RACE_FORMAT%             | Current race format                                                     |
| %LAP_COUNT%               | Current lap number                                                      |
| %LAST_LAP%                | Last lap time for pilot                                                 |
| %AVERAGE_LAP%             | Average lap time for pilot                                              |
| %FASTEST_LAP%             | Fastest lap time                                                        |
| %TIME_BEHIND_CALL%        | Amount of time behind race leader (with prompt)                         |
| %TIME_BEHIND_FINPOS_CALL% | Pilot NAME finished at position X, MM:SS.SSS behind                     |
| %TIME_BEHIND_FINPLACE_CALL% | Pilot NAME finished in X place, MM:SS.SSS behind                      |
| %FASTEST_SPEED%           | Fastest speed for pilot                                                 |
| %CONSECUTIVE%             | Fastest consecutive laps for pilot                                      |
| %TOTAL_TIME%              | Total time since start of race for pilot                                |
| %TOTAL_TIME_LAPS%         | Total time since start of first lap for pilot                           |
| %POSITION%                | Race position for pilot                                                 |
| %POSITION_CALL%           | Race position for pilot (with prompt)                                   |
| %POSITION_PLACE%          | Race position (first, second, etc) for pilot                            |
| %POSITION_PLACE_CALL%     | Race position (first, second, etc) for pilot (with prompt)              |
| %FASTEST_RACE_LAP%        | Pilot/time for fastest lap in race                                      |
| %FASTEST_RACE_LAP_CALL%   | Pilot/time for fastest lap in race (with prompt)                        |
| %FASTEST_RACE_SPEED%      | Pilot/speed for fastest speed in race                                   |
| %FASTEST_RACE_SPEED_CALL% | Pilot/speed for fastest speed in race (with prompt)                     |
| %WINNER%                  | Pilot callsign for winner of race                                       |
| %WINNER_CALL%             | Pilot callsign for winner of race (with prompt)                         |
| %PREVIOUS_WINNER%         | Pilot callsign for winner of previous race                              |
| %PREVIOUS_WINNER_CALL%    | Pilot callsign for winner of previous race (with prompt)                |
| %PILOTS%                  | List of pilot callsigns (read out slower)                               |
| %LINEUP%                  | List of pilot callsigns (read out faster)                               |
| %FREQS%                   | List of pilot callsigns and frequency assignments                       |
| %LEADER%                  | Callsign of pilot currently leading race                                |
| %LEADER_CALL%             | Callsign of pilot currently leading race, in the form "NAME is leading" |
| %SPLIT_TIME%              | Split time for pilot (see [Secondary / Split Timers](../doc/Cluster.md) doc)  |
| %SPLIT_SPEED%             | Split speed for pilot (see [Secondary / Split Timers](../doc/Cluster.md) doc) |
| %CURRENT_TIME_AP%         | Current time (12-hour clock)                                            |
| %CURRENT_TIME_24%         | Current time (24-hour clock)                                            |
| %CURRENT_TIME_SECS_AP%    | Current time, with seconds (12-hour clock)                              |
| %CURRENT_TIME_SECS_24%    | Current time, with seconds (24-hour clock)                              |
| %DELAY_#_SECS%            | Delay voice callout by given number of seconds                          |
