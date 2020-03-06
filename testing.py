import simulator as sim
import pickle
import statistics

if __name__ == "__main__":
    simulator = sim.Simulator(30, 3000, 1.0, [1. / 30] * 12, 8, False)  # /!\ nb_episodes = 1500
    while simulator.step(None):
        '''if simulator.get_curr_nb_iterations() < 50:
            print("STEP " + str(simulator.get_curr_nb_iterations()))
            print(simulator.detectedCarCnt)
            print(simulator.distanceNearestDetectedVeh)
            print(simulator.normCurrPhaseTime)
            print(simulator.amberPhase)
            print(simulator.currDayTime)
            print(simulator.reward)'''

    reward = statistics.mean(simulator.averageRewards)
    waiting_time = statistics.mean(simulator.averageWaitingTimes)
    print("Average reward:", str(reward))
    print("Average waiting time:", str(waiting_time))

    with open("uniform1over30_baseline_r.txt", "wb") as file:
        pickle.dump(reward, file)
    with open("uniform1over30_baseline_w.txt", "wb") as file:
        pickle.dump(waiting_time, file)
