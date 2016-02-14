import agent
import domain
import policy
import representation

def run(num_episodes = 500, dt = 0.01):
    whiff_world = domain.WhiffWorld(dt)
    whiff_rep = representation.LinearApproximation(whiff_world)
    whiff_policy = policy.eGreedy(whiff_rep)
    whiff = agent.QLearner(whiff_policy, whiff_rep)
    for episode in range(num_episodes):
        while not whiff_world.is_terminal(whiff_world.state):
            state = whiff_world.state
            possible_actions = whiff_world.possible_actions

            # choose an action
            action = whiff_policy.pi(state, possible_actions, whiff.weights)
            # execute that action on the simulator and
            # observe new state
            next_state = whiff_world.step(state, action)
            if whiff_world.is_terminal(next_state):
                reward = -10
            else:
                reward = 0
            # update the rewards
            whiff.learn(state, action, reward, next_state, is_terminal)

        whiff_world.reinitialize()


if __name__ == '__main__':
    run()