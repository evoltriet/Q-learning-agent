
from maze_env import Maze
import time
import pandas as pd

def update():
    for episode in range(100):
        # initial observation
        observation = env.reset()
        trained_q_table = pd.read_pickle("trained_q_table")

        while True:
            #activate sleep to slow down simulation
            time.sleep(.2)
            
            # fresh env
            env.render()

            # Choose best action based on observation
            action = choose_best_action(str(observation), trained_q_table)

            # take action and get next observation
            observation_, reward, done = env.step(action)

            # swap observation
            observation = observation_
            
            # break while loop when end of this episode
            if done:
                print("episode:"+str(episode)+" reward:"+str(reward))
                print(trained_q_table)
                break

     # end of game
    print('game over')
    env.destroy()

def choose_best_action(observation, q_table):
        # choose best action
        state_action = q_table.ix[observation, :]
        action = state_action.values.argmax()
        return action

if __name__ == "__main__":
    env = Maze()
    env.after(100, update)
    env.mainloop()
