# Q-Learning Agent

This repo is a small reinforcement-learning demo that trains a Q-learning agent to navigate a toy maze. It is a learning experiment, not a production RL system or a generalized path planner.

## Problem

The goal is to teach an agent to move from a start position to a goal while avoiding terminal states. The maze is deliberately small so the repo can focus on the learning loop, state representation, and policy reuse.

## Approach

- `maze_env.py` defines the 4x4 Tkinter environment, the start state, the goal, two terminal "hell" states, and the reward function.
- `RL_brain.py` implements the Q-table, epsilon-greedy action selection, and the standard Q-learning update rule.
- `train.py` runs 1000 training episodes, learns from each transition, and saves the resulting table to `trained_q_table`.
- `solve.py` loads the saved table and replays the learned policy for 100 episodes.

The Q-table is the core artifact of the repo. It acts as a compact memory of what action looks best in each observed state, which is why the project is often useful as an "intelligent agent" teaching example.

## Outcome

After training, the agent can replay a learned policy and reach the goal more reliably than a random policy. The saved `trained_q_table` file is the main output of the training run, and `qtable.png` documents the learned table visually.

## How To Run

Install the lightweight dependencies used by the scripts:

- `numpy`
- `pandas`
- `tkinter` from the standard Python distribution

Then run training first, followed by the solver:

```bash
python train.py
python solve.py
```

The training script writes `trained_q_table` into the repo root, and the solver reads that file back in for greedy replay.

## Limitations

- The code uses older pandas APIs such as `.ix` and `DataFrame.append`, so it may require an older pandas release or a small modernization pass.
- The maze is intentionally tiny and does not represent a real navigation problem.
- The reward structure is simple and hand-tuned for demonstration purposes.
- The saved policy is only as good as the toy environment it was trained on.
