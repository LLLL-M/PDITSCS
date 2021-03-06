from simulator import Simulator
from DQN import Agent
import statistics

if __name__ == "__main__":
    h_probs = [[0.0003 / 3] * 3 + [0.0011 / 3] * 3 + [0.0015 / 3] * 3 + [0.0029 / 3] * 3,
               [0.0005 / 3] * 3 + [0.002 / 3] * 3 + [0.0016 / 3] * 3 + [0.002 / 3] * 3,
               [0.0005 / 3] * 3 + [0.0019 / 3] * 3 + [0.0018 / 3] * 3 + [0.0027 / 3] * 3,
               [0.0003 / 3] * 3 + [0.0024 / 3] * 3 + [0.0016 / 3] * 3 + [0.0023 / 3] * 3,
               [0.0035 / 3] * 3 + [0.0032 / 3] * 3 + [0.004 / 3] * 3 + [0.0061 / 3] * 3,
               [0.0197 / 3] * 3 + [0.012 / 3] * 3 + [0.0094 / 3] * 3 + [0.0186 / 3] * 3,
               [0.05 / 3] * 3 + [0.0296 / 3] * 3 + [0.0229 / 3] * 3 + [0.0481 / 3] * 3,
               [0.0717 / 3] * 3 + [0.0507 / 3] * 3 + [0.0375 / 3] * 3 + [0.0653 / 3] * 3,
               [0.0756 / 3] * 3 + [0.0529 / 3] * 3 + [0.0434 / 3] * 3 + [0.0742 / 3] * 3,
               [0.0696 / 3] * 3 + [0.0393 / 3] * 3 + [0.0331 / 3] * 3 + [0.0603 / 3] * 3,
               [0.0541 / 3] * 3 + [0.025 / 3] * 3 + [0.0212 / 3] * 3 + [0.0406 / 3] * 3,
               [0.0284 / 3] * 3 + [0.0208 / 3] * 3 + [0.0184 / 3] * 3 + [0.0293 / 3] * 3,
               [0.0419 / 3] * 3 + [0.0331 / 3] * 3 + [0.0294 / 3] * 3 + [0.0540 / 3] * 3,
               [0.0569 / 3] * 3 + [0.0373 / 3] * 3 + [0.0327 / 3] * 3 + [0.0522 / 3] * 3,
               [0.0465 / 3] * 3 + [0.0263 / 3] * 3 + [0.0244 / 3] * 3 + [0.0542 / 3] * 3,
               [0.0157 / 3] * 3 + [0.0198 / 3] * 3 + [0.0214 / 3] * 3 + [0.0313 / 3] * 3,
               [0.0132 / 3] * 3 + [0.0426 / 3] * 3 + [0.0374 / 3] * 3 + [0.0517 / 3] * 3,
               [0.0156 / 3] * 3 + [0.0594 / 3] * 3 + [0.0575 / 3] * 3 + [0.0702 / 3] * 3,
               [0.0234 / 3] * 3 + [0.0616 / 3] * 3 + [0.0725 / 3] * 3 + [0.0712 / 3] * 3,
               [0.0163 / 3] * 3 + [0.0556 / 3] * 3 + [0.0572 / 3] * 3 + [0.0668 / 3] * 3,
               [0.0087 / 3] * 3 + [0.0363 / 3] * 3 + [0.0328 / 3] * 3 + [0.0387 / 3] * 3,
               [0.0063 / 3] * 3 + [0.0224 / 3] * 3 + [0.0259 / 3] * 3 + [0.0271 / 3] * 3,
               [0.0044 / 3] * 3 + [0.0183 / 3] * 3 + [0.0165 / 3] * 3 + [0.0274 / 3] * 3,
               [0.0037 / 3] * 3 + [0.0171 / 3] * 3 + [0.0196 / 3] * 3 + [0.0256 / 3] * 3]

    mem_size = 3000000
    nb_init = 10000  # Number of samples in the replay buffer before learning starts
    nb_inputs = 11
    nb_actions = 2  # Either stay at current phase or switch to the next one
    nb_episodes = 10
    nb_episode_steps = 86400
    detection_rate = 1.0  # Percentage of vehicles that can be detected by the algorithm
    min_phase_duration = 10
    gui = True
    alpha = 0.0001
    gamma = 0.9
    policy = "epsilon-greedy"
    epsilon = 1
    epsilon_end = 0.05
    decay_steps_ep = 100000
    temp = 1
    temp_end = 0.05
    decay_steps_temp = 100000
    batch_size = 32
    target_update_frequency = 3000
    hour_of_the_day = 0
    # Probability for a car to be generated on a particular route at a certain step
    route_probabilities = [1. / 60] * 12
    file_name = "model_100_real_3000targup_test.pt"

    simulator = Simulator(nb_episodes, nb_episode_steps, detection_rate, min_phase_duration, route_probabilities,
                          hour_of_the_day, gui, h_probs)
    agent = Agent(alpha, gamma, policy, epsilon, epsilon_end, decay_steps_ep, temp, temp_end, decay_steps_temp,
                  batch_size, nb_inputs, nb_actions, mem_size, file_name)
    agent.load_net()
    while simulator.step(agent.select_action(simulator.get_state(), True)):
        print("Reward for step", str(simulator.get_curr_nb_iterations()) + ":", str(simulator.get_reward()))
    print("Total average reward:", statistics.mean(simulator.averageRewards))
    print("Total average waiting time:", statistics.mean(simulator.averageWaitingTimes))
