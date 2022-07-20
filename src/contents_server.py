import random
from dataclasses import dataclass
from typing import List

from numpy.random import beta


@dataclass
class Content:
    name: str


class ContentsServer:
    def __init__(self, contents: List[Content]) -> None:
        self.contents = contents
        self.clicks = {c.name: 0 for c in contents}
        self.impressions = {c.name: 0 for c in contents}
        self.ctrs = {c.name: 0 for c in contents}
        self.ctr = 0

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

    def get_content(self) -> Content:
        # content = self.algorithm_random()
        content = self.algorithm_thompson_sampling()
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

    def _show(self) -> None:
        self._update_ctrs()
        print(f"clicks     :\t{self.clicks}")
        print(f"server imps:\t{self.impressions}")
        print(f"CTRs       :\t{self.ctrs}")
        print(f"total CTR  :\t{self.ctr}")


@dataclass
class User:
    name: str
    preferences: List[Content]

    def click(self, content: Content) -> bool:
        prefer_content_now = random.sample(self.preferences, 1)[0]
        return prefer_content_now.name == content.name

if __name__ == "__main__":
    content_dog = Content("dog")
    content_cat = Content("cat")
    content_bird = Content("bird")

    count = {
        "dog": 0,
        "cat": 0,
        "bird": 0,
    }
    contents_server = ContentsServer([content_dog, content_cat, content_bird])
    userA_preferences = [content_dog] * 15 + [content_cat] * 80 + [content_bird] * 5
    userA = User("user", userA_preferences)
    for i in range(100000):
        content = contents_server.get_content()
        count[content.name] += 1
        user_clicked = userA.click(content)
        if user_clicked:
            contents_server.send_click(content)
        if i % 10000 == 0:
            print(f"===={i}====")
            contents_server._show()


