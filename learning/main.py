import agent
import domain
import policy
import representation
import matplotlib.pyplot as plt

def run(num_episodes = 200, dt = 0.01):
    whiff_world = domain.WhiffWorld(dt)
    whiff_rep = representation.LinearApproximation(whiff_world)
    whiff_policy = policy.eGreedy(whiff_rep)
    whiff = agent.QLearner(whiff_policy, whiff_rep)
    lifetimes = []
    for episode in range(num_episodes):
        count = 0
        while not whiff_world.is_terminal(whiff_world.state):
            count += 1
            state = whiff_world.state
            possible_actions = whiff_world.possible_actions

            # choose an action
            action = whiff_policy.pi(state, possible_actions, whiff.weights)
            # execute that action on the simulator and
            # observe new state
            next_state = whiff_world.step(state, action)

            if count > 5000: break

            if whiff_world.is_terminal(next_state):
                reward = -10
            elif count%500 == 0:
                reward = 60
            else:
                if (state[0] > 0 and action[2]) or (state[0] < 0 and action[0]):
                    reward = -0.1
                else:
                    reward = 0.9
            # update the rewards
            whiff.learn(state, action, reward, next_state, possible_actions)
            print action

        print count
        lifetimes.append(count)
        whiff_world.reinitialize()

        print whiff.weights

    print lifetimes
    plt.plot(lifetimes)
    plt.show()

if __name__ == '__main__':
    run()
