# Part 1: Q-Learning

## Question 1
reward of around -20 to -15 after 500k steps, -15 to -10 after 1m steps, -10 to -5 after 1.5m steps, and around
+10 after 2m steps on Pong. The maximum score of around +20 is reached
after about 4-5m steps. However, there is considerable variation between runs.
For Q1, you must run the algorithm for at least 3m timesteps (and you are encouraged to run for more), and you must achieve a final reward of at least +10
(i.e. your trained agent beats the opponent by an average of 10 points).

### recommend using LunarLander-v2 to check the correctness of your code before running longer experiments with PongNoFrameSkip-v4
```
python cs285\scripts\run_hw3_dqn.py --env_name PongNoFrameskip-v4 --exp_name q1
```

## Question 2: double Q-learning (DDQN)
150 reward after 500k timesteps, but there is considerable variation between runs, and the method
sometimes experience instabilities (i.e. the reward goes down after achieving
150)
```
python run_hw3_dqn.py --env_name LunarLander-v2 --exp_name q2_dqn_1 --seed 1
python run_hw3_dqn.py --env_name LunarLander-v2 --exp_name q2_dqn_2 --seed 2
python run_hw3_dqn.py --env_name LunarLander-v2 --exp_name q2_dqn_3 --seed 3
```
```
python run_hw3_dqn.py --env_name LunarLander-v2 --exp_name q2_doubledqn_1 --double_q --seed 1
python run_hw3_dqn.py --env_name LunarLander-v2 --exp_name q2_doubledqn_2 --double_q --seed 2
python run_hw3_dqn.py --env_name LunarLander-v2 --exp_name q2_doubledqn_3 --double_q --seed 3
```

## Question 3: experimenting with hyperparameters
Examples include: learning rates, neural network architecture, exploration schedule or exploration rule (e.g. you
may implement an alternative to e-greedy), etc.

Note: you might consider performing a hyperparameter sweep for getting good results in Question 1, in
which case it’s fine to just include the results of this sweep for Question 3 as
well
```
python run_hw3_dqn.py --env_name PongNoFrameskip-v4 --exp_name q3_hparam1
python run_hw3_dqn.py --env_name PongNoFrameskip-v4 --exp_name q3_hparam2
python run_hw3_dqn.py --env_name PongNoFrameskip-v4 --exp_name q3_hparam3
```

# Part 2: Actor-Critic

## Question 4: Sanity check with Cartpole 
```
python run_hw3_actor_critic.py --env_name CartPole-v0 -n 100 -b 1000 --exp_name 1_1 -ntu 1 -ngsptu 1
python run_hw3_actor_critic.py --env_name CartPole-v0 -n 100 -b 1000 --exp_name 100_1 -ntu 100 -ngsptu 1
python run_hw3_actor_critic.py --env_name CartPole-v0 -n 100 -b 1000 --exp_name 1_100 -ntu 1 -ngsptu 100
python run_hw3_actor_critic.py --env_name CartPole-v0 -n 100 -b 1000 --exp_name 10_10 -ntu 10 -ngsptu 10
```

## Question 5: Run actor-critic with more difficult tasks
```
python run_hw3_actor_critic.py --env_name InvertedPendulum-v2 --ep_len 1000 --discount 0.95 -n 100 -l 2 -s 64 -b 5000 -lr 0.01 --exp_name <>_<> -ntu <> -ngsptu <>
```
```
python run_hw3_actor_critic.py --env_name HalfCheetah-v2 --ep_len 150 --discount 0.90 --scalar_log_freq 1 -n 150 -l 2 -s 32 -b 30000 -eb 1500 -lr 0.02 --exp_name <>_<> -ntu <> -ngsptu <>
```