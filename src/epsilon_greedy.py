from numpy.random import binomial, randint

from arm import Arm


def calc_success_ratio(arm):
    if arm.success + arm.fail == 0:
        return 0
    return arm.success / (arm.success + arm.fail)

def epsilon_greedy(arms, T, epsilon):
    reward = 0
    for i in range(T):
        if binomial(n=1, p=epsilon) == 1:
            # exploration(探索): アームを一様ランダムに選ぶ
            index = randint(0, len(arms))
        else:
            # exploitation(活用) : 今までで一番成功確率の高いアームを選ぶ
            avgs = [calc_success_ratio(arm) for arm in arms]
            index = avgs.index(max(avgs))
        reward += arms[index].play()
    return reward

if __name__ == "__main__":
    T = 1000
    arms = [Arm(i/100) for i in range(100)]
    for e in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
        r = epsilon_greedy(arms, T, e)
        print(f"epsilon={e}, reward={r}")
