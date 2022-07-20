import random
from dataclasses import dataclass
from typing import List, Optional

from numpy.random import beta, binomial


@dataclass
class Content:
    name: str


class ContentsServer:
    ALGO_TYPE_RANDOM = "random"
    ALGO_TYPE_THOMPSON_SAMPLING = "thompson_sampling"
    ALGO_TYPE_EPSILON_GREEDY = "epsilon_greedy"


    def __init__(self, contents: List[Content], algo_type: str, exploration_rate: Optional[float] = None) -> None:
        self.contents = contents
        self.clicks = {c.name: 0 for c in contents}
        self.impressions = {c.name: 0 for c in contents}
        self.ctrs = {c.name: 0 for c in contents}
        self.ctr = 0

        self.algo_type = algo_type
        self.exploration_rate = exploration_rate

    def algorithm_random(self) -> None:
        return random.sample(self.contents, 1)[0]

    def algorithm_thompson_sampling(self) -> None:
        scores = []
        for content in self.contents:
            success = self.clicks[content.name]
            fails = self.impressions[content.name] - success
            score = beta(a=success + 1, b=fails+1)
            scores.append(score)
        max_index = scores.index(max(scores))
        return self.contents[max_index]

    def algorithm_epsilon_greedy(self, exploration_rate: float) -> None:
        # exploration
        if binomial(n=1, p=exploration_rate) == 1:
            index = random.randint(0, len(self.contents)-1)
            return self.contents[index]

        # exploitation
        # Get content with highest CTR
        ctr_values = list(self.ctrs.values())
        max_index = ctr_values.index(max(ctr_values))
        return self.contents[max_index]

    def _get_content(self) -> Content:
        if self.algo_type == self.ALGO_TYPE_RANDOM:
            return self.algorithm_random()
        if self.algo_type == self.ALGO_TYPE_THOMPSON_SAMPLING:
            return self.algorithm_thompson_sampling()
        if self.algo_type == self.ALGO_TYPE_EPSILON_GREEDY:
            return self.algorithm_epsilon_greedy(self.exploration_rate)
        raise ValueError(f"Unknown algo_type: {self.algo_type}")

    def get_content(self) -> Content:
        content = self._get_content()
        self.impressions[content.name] += 1
        return content

    def send_click(self, content: Content) -> None:
        self.clicks[content.name] += 1

    def _update_ctrs(self) -> None:
        for c in self.contents:
            if self.impressions[c.name] == 0:
                self.ctrs[c.name] = 0
            else:
                ctr = self.clicks[c.name] / self.impressions[c.name]
                self.ctrs[c.name] = ctr
        total_clicks = sum(self.clicks.values())
        total_impressions = sum(self.impressions.values())
        self.ctr = total_clicks / total_impressions

    def _show_stats(self) -> None:
        self._update_ctrs()
        print(f"clicks     :\t{self.clicks}")
        print(f"server imps:\t{self.impressions}")
        print(f"CTRs       :\t{self.ctrs}")
        print(f"total CTR  :\t{self.ctr}")


@dataclass
class User:
    name: str
    preferences: List[List[Content]]

    def does_click(self, content: Content) -> bool:
        prefer_content_now = random.sample(self.preferences, 1)[0]
        return prefer_content_now.name == content.name

if __name__ == "__main__":
    algo_type = ContentsServer.ALGO_TYPE_THOMPSON_SAMPLING
    content_dog = Content("dog")
    content_cat = Content("cat")
    content_bird = Content("bird")
    master_contents = [content_dog, content_cat, content_bird]
    contents_server = ContentsServer(master_contents, algo_type)

    user_preferences1 = [content_dog] * 15 + [content_cat] * 80 + [content_bird] * 5
    user_preferences2 = [content_dog] * 70 + [content_cat] * 25 + [content_bird] * 5
    user_preferences3 = [content_dog] * 30 + [content_cat] * 30 + [content_bird] * 40
    user1 = User("user-cat", user_preferences1)
    user2 = User("user-dog", user_preferences2)
    user3 = User("user-bird", user_preferences3)
    users = [user1, user2, user3]
    initial_user = random.sample(users, 1)[0]

    user = initial_user

    for i in range(100000000):
        content = contents_server.get_content()
        user_clicked = user.does_click(content)
        if user_clicked:
            contents_server.send_click(content)
        if i % 10_000 == 0:
            print(f"===={i}:{user.name}====")
            contents_server._show_stats()
        if i % 100_000 == 0:
            new_user = random.sample(users, 1)[0]
            user = new_user


