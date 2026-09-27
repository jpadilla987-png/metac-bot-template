import unittest
from types import SimpleNamespace

from policy_guard import is_blocked_forecast_topic, should_block_question


class PolicyGuardTests(unittest.TestCase):
    def test_blocks_election_forecast(self):
        self.assertTrue(is_blocked_forecast_topic("Who will win the presidential election?"))

    def test_blocks_candidate_question(self):
        q = SimpleNamespace(
            question_text="Will Candidate X win the mayoral race?",
            background_info="",
            resolution_criteria="",
            fine_print="",
        )
        self.assertTrue(should_block_question(q))

    def test_allows_nonpolitical_science_question(self):
        q = SimpleNamespace(
            question_text="Will a reusable launch vehicle reach orbit by 2027?",
            background_info="Spaceflight technology",
            resolution_criteria="Resolves yes if the vehicle reaches orbit.",
            fine_print="",
        )
        self.assertFalse(should_block_question(q))

    def test_allows_nonpolitical_market_question(self):
        self.assertFalse(is_blocked_forecast_topic("Will copper exceed $5 per pound by year end?"))


if __name__ == "__main__":
    unittest.main()
