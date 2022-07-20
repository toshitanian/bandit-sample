import random
from dataclasses import dataclass
from typing import List


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

    def get_content(self) -> Content:
        content = random.sample(self.contents, 1)[0]
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
        print(f"totaol CTR :\t{self.ctr}")


@dataclass
class User:
    name: str
    preferences: List[Content]

    def click(self, content: Content) -> bool:
        prefer_content_now = random.sample(self.preferences, 1)[0]
        return prefer_content_now.name == content.name

if __name__ == "__main__":
    contentDog = Content("dog")
    contentCat = Content("cat")
    contentBird = Content("bird")

    count = {
        "dog": 0,
        "cat": 0,
        "bird": 0,
    }
    contents_server = ContentsServer([contentDog, contentCat, contentBird])
    userA = User("user", [contentDog, contentCat, contentCat])
    for i in range(100000):
        content = contents_server.get_content()
        count[content.name] += 1
        user_clicked = userA.click(content)
        if user_clicked:
            contents_server.send_click(content)
        if i % 1000 == 0:
            print(f"===={i}====")
            print(f"server imps:\t{count}")
            contents_server._show()


