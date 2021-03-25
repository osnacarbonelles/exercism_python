class HighScores(object):
    """Manage scores for a single player.
    Attributes:
        scores {list}--Sequence of the players scores
    """

    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[-1]

    def personal_best(self):
        return max(self.scores)

    def personal_top_three(self):
        return sorted(self.scores, reverse=True)[:3]
