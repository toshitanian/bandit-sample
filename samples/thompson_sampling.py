from numpy.random import beta

from arm import Arm


def thompson_sampling(arms, T):
    reward = 0
    for i in range(T):
        # 事後分布から乱数を生成。これをpの推定値として扱う
        rand_gened_params = [beta(a=arm.success+1, b=arm.fail+1) for arm in arms]
        # 推定値が一番高いアームを選択
        max_index = rand_gened_params.index(max(rand_gened_params))
        reward += arms[max_index].play()
        if i % 100 == 0:
            print(f"{i}:{reward}")
    return reward

if __name__ == "__main__":
    T = 1000000
    arms = [Arm(i/200 + 0.5) for i in range(100)]
    r = thompson_sampling(arms, T)
    print(f"reward={r}")
