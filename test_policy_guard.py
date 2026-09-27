import unittest
from types import SimpleNamespace

import policy_guard
from policy_guard import is_blocked_forecast_topic, should_block_question


class PolicyGuardTests(unittest.TestCase):
    def test_publish_gate_defaults_closed_and_requires_exact_true(self):
        gate = getattr(policy_guard, "allow_metaculus_posts", lambda env: True)

        self.assertFalse(gate({}))
        self.assertFalse(gate({"ALLOW_METACULUS_POSTS": "false"}))
        self.assertFalse(gate({"ALLOW_METACULUS_POSTS": "1"}))
        self.assertTrue(gate({"ALLOW_METACULUS_POSTS": "true"}))

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

    def test_blocks_eu_exit_question_that_triggered_smoke_run(self):
        q = SimpleNamespace(
            question_text=(
                "Will any of Belgium, France, Italy, Luxembourg, Netherlands, "
                "and/or Germany leave the EU before 2027?"
            ),
            background_info="",
            resolution_criteria="Resolves on formal withdrawal from the European Union.",
            fine_print="",
        )
        self.assertTrue(should_block_question(q))

    def test_blocks_policy_and_government_question(self):
        self.assertTrue(
            is_blocked_forecast_topic(
                "Will the government pass the proposed legislation this year?"
            )
        )

    def test_blocks_metadata_category_even_if_title_is_neutral(self):
        q = SimpleNamespace(
            question_text="Will event X happen by December?",
            background_info="",
            resolution_criteria="",
            fine_print="",
            category="Geopolitics",
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
