import unittest
from economics import scenario

class EconomicsTests(unittest.TestCase):
    def test_unverified_default_has_no_reward(self):
        result = scenario(cash_cost=100, hours=4, hourly_cost=25)
        self.assertEqual(result["probability_weighted_liquid_tokens"], "0")
        self.assertIsNone(result["break_even_token_price"])
        self.assertIsNone(result["scenario_net_profit"])
        self.assertEqual(result["zero_reward_net_profit"], "-200")
        self.assertFalse(result["allocation_verified_by_this_tool"])

    def test_documented_example(self):
        result = scenario(100, 4, 25, 1000, ".25", ".5", 2)
        self.assertEqual(result["total_cost"], "200")
        self.assertEqual(float(result["probability_weighted_liquid_tokens"]), 125)
        self.assertEqual(float(result["break_even_token_price"]), 1.6)
        self.assertEqual(float(result["scenario_net_profit"]), 50)

    def test_locked_tokens_do_not_fund_costs(self):
        result = scenario(cash_cost=10, tokens=10000, liquid_fraction=0, realization_probability=1, token_price=100)
        self.assertEqual(float(result["scenario_net_profit"]), -10)
        self.assertIsNone(result["break_even_token_price"])

    def test_zero_probability_is_full_loss(self):
        result = scenario(cash_cost=10, tokens=10000, liquid_fraction=1, realization_probability=0, token_price=100)
        self.assertEqual(float(result["scenario_net_profit"]), -10)

    def test_probability_one_no_discount(self):
        result = scenario(cash_cost=10, tokens=100, liquid_fraction=1, realization_probability=1, token_price=".2")
        self.assertEqual(float(result["scenario_net_profit"]), 10)

    def test_reject_invalid_inputs(self):
        for key in ("cash_cost", "hours", "hourly_cost", "tokens", "liquid_fraction", "realization_probability", "token_price"):
            for bad in ("-1", "NaN", "Infinity", "not-a-number"):
                with self.subTest(key=key, bad=bad), self.assertRaises(ValueError):
                    scenario(**{key: bad})

    def test_fractions_cannot_exceed_one(self):
        for key in ("liquid_fraction", "realization_probability"):
            with self.assertRaises(ValueError):
                scenario(**{key: "1.01"})

    def test_known_zero_price_is_not_unknown(self):
        result = scenario(cash_cost=10, tokens=10, liquid_fraction=1, realization_probability=1, token_price=0)
        self.assertEqual(float(result["scenario_net_profit"]), -10)

    def test_additional_cost_always_reduces_profit(self):
        base = scenario(cash_cost=10, tokens=10, liquid_fraction=1, realization_probability=1, token_price=2)
        costlier = scenario(cash_cost=11, tokens=10, liquid_fraction=1, realization_probability=1, token_price=2)
        self.assertLess(float(costlier["scenario_net_profit"]), float(base["scenario_net_profit"]))

if __name__ == "__main__":
    unittest.main()
