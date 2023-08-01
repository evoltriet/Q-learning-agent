
from maze_env import Maze
from RL_brain import QLearningTable
import time

def update():
    for episode in range(1000):
        # initial observation
        observation = env.reset()

        while True:
            #activate sleep to slow down simulation
            time.sleep(.2)
            
            # fresh env
            env.render()

            # RL choose action based on observation
            action = RL.choose_action(str(observation))

            # RL take action and get next observation and reward
            observation_, reward, done = env.step(action)

            # RL learn from this transition
            RL.learn(str(observation), action, reward, str(observation_))
            # swap observation
            observation = observation_
            
            # break while loop when end of this episode
            if done:
                print("episode:"+str(episode)+" reward:"+str(reward))
                print(RL.q_table)
                break

     # end of game
    print('game over')
    RL.q_table.to_pickle("trained_q_table")
    env.destroy()

if __name__ == "__main__":
    env = Maze()
    RL = QLearningTable(actions=list(range(env.n_actions)))

    env.after(100, update)
    env.mainloop()
