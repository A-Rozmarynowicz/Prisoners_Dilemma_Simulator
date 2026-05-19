![IT](https://img.shields.io/badge/IT-purple)
![Game_Theory](https://img.shields.io/badge/Game_Theory-red)

![Software](https://img.shields.io/badge/Software-lightblue)

# Prisoner's Dilemma Simulator
Simulation of the Prisoner's Dilemma with various strategies (including a Reinforcement Learning strategy) in a flexible framework. Inspired by a video on Game Theory by [Veritasium](https://www.youtube.com/watch?v=mScpHTIi-kM).

Development time: 05.2026

## General information
- Developed a flexible framework that enables simulating different games, rules, and strategies.
- Trained a Q-Learning model to win most of the time against bot players.
- Ran tournaments, compared strategies' effectiveness, and analysed the results.

## Context
The Prisonner's Dilemma is a very famous Game Strategy problem, where two players make decisions simultaneously, and their reward depends on the combination of their choices. Namely, their reward is given by Table 1:

<!-- |   | 2nd player decision | *Cooperate* | *Betray* |
| --- | --- | --- | --- |
| **1st player decision**  |   |  |  |
| ***Cooperate***  |   |  | asdas |
| ***Betray***  |   | asd  | dasd | -->

<table>
    <caption style="caption-side: bottom; padding-top: 8px;">
    Table 1: Prisoner's Dilemma reward matrix
    </caption>

  <tr>
    <th></th>
    <th style="border-left:1px solid white;">2nd player decision</th>
    <th style="border-left:1px solid white;"><i>Cooperate</i></th>
    <th style="border-left:1px solid white; border-right:1px solid white;"><i>Betray</i></th>
  </tr>
  <tr >
    <th><b>1st player decision</b></th>
    <td style="border-left:1px solid white;"></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <th><i>Cooperate</i></th>
    <td style="border-left:1px solid white;"></td>
    <td> (3, 3) </td>
    <td> (0, 5)</td>
  </tr>
  <tr>
    <th><i>Betray</i></th>
    <td style="border-left:1px solid white;"></td>
    <td>(5, 0)</td>
    <td>(1, 1)</td>
  </tr>

</table>

The table suggests that betraying is always more profitable, regardless of the opponent's move. However, when playing multiple games with the same opponent, it becomes profitable to cooperate in the hope the other side will do the same.

The task is to find a strategy that maximizes its reward over a span of multiple games, with multiple opponents.

## Implemented strategies
### Always Cooperate
As name suggests, a very naive policy.

### Always Betray
A pretty unfriendly player.

### Patient Unforgiving
It tries to always cooperate, until the opponent betrays 'k' times (k is a patience parameter), after which it betrays until the end.

### Forgiving
Similar to the [Unforgiving](#unforgiving) strategy, but after being betrayed it cooperates again with a probability 'p' (a parameter). It gives the opponent a chance to redeem.

### Copycat
Copies the opponent's last move. Cooperates in the 1st round.

### Periodic
Oscillates between actions with a period k.

### Random
Cooperates with a probability 'p' (parameter), else betrays.

### Q-Learning
Its choices are determined by a q-table generated during traning. It was trained in tournaments against the same players it was tested with. Its observation were opponents past 'k' actions, and its own past 'k' actions. During the training it showed that in this scenario, it only needs one pair of past choices.


## Results
Q-Learning and the Unforgiving strategy (one that always cooperates until the opponent betrays, after which it betrays until the end of the game) managed to outperform all other strategies in most of the games. By analysing the Q-table, however, one can see that the Q-Learning has learned to mimic the Unforgiving strategy. This contradicts the results obtained by [Veritasium](https://www.youtube.com/watch?v=mScpHTIi-kM), where its team found out that the Forgiving strategy tends to do better. The reason for this is the fact that the optimal strategy depends on who the other players are.

Please refer to the [main.ipynb](./source/main.ipynb) file to see dataframes with more information.

*This README is under construction.*

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Place</th>
      <th>Name</th>
      <th>Average score</th>
      <th>Fraction of Co-ops</th>
    </tr>

  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Q-Learning</td>
      <td>2.27</td>
      <td>0.51</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Unforgiving (patience=1)</td>
      <td>2.22</td>
      <td>0.51</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Forgiving (p_forgive=0.1)</td>
      <td>2.16</td>
      <td>0.60</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Copycat</td>
      <td>2.08</td>
      <td>0.63</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Always Betray</td>
      <td>1.90</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Random (p_coop=0.1)</td>
      <td>1.81</td>
      <td>0.09</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Always Cooperate</td>
      <td>1.68</td>
      <td>1.00</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Periodic (period=1)</td>
      <td>1.39</td>
      <td>0.50</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Random (p_coop=0.5)</td>
      <td>1.38</td>
      <td>0.48</td>
    </tr>
  </tbody>
</table>
</div>

## Technologies used
- Python
- numpy
- pandas