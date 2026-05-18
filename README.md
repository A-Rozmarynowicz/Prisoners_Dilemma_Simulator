![IT](https://img.shields.io/badge/IT-purple)
![Game_Theory](https://img.shields.io/badge/Game_Theory-red)

![Software](https://img.shields.io/badge/Software-lightblue)

# Prisoner's Dilemma Simulator
Simulation of the Prisoner's Dilemma with various strategies (including a Reinforcement Learning strategy) in a flexible framework.

## General information
- Developed a flexible framework that enables simulating different games, rules, and strategies.
- Trained a Q-Learning model to win most of the time against bot players.
- Implemented various strategies, such as:
    - Q-Learning,
    - Always Cooperate/Betray,
    - Forgiving/Unforgiving,
    - Copycat,
    - and more.
- Ran tournaments, compared strategies' effectiveness, and analysed the results.

## Results
Q-Learning and the Unforgiving strategy (one that always cooperates until the opponent betrays, after which it betrays until the end of the game) managed to outperform all other strategies in most of the games. By analysing the Q-table, however, one can see that the Q-Learning has learned to mimic the Unforgiving strategy. This contradicts the results obtained by [Veritasium](https://www.youtube.com/watch?v=mScpHTIi-kM), where its team found out that the Forgiving strategy tends to do better. The reason for this is the fact that the optimal strategy depends on who the other players are.

Please refer to the [main.ipynb](./source/main.ipynb) file to see dataframes with more information.

*This README is under construction.*