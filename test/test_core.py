import unittest

from src.tierlist import TierList
from src.tier import Tier
from src.core import create_tier_list


class TestCore(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)

    def test_core_creates_default_tier_list(self):
        tierlist = TierList(
            name="Untitled",
            tiers=[
                Tier("S"),
                Tier("A"),
                Tier("B"),
                Tier("C"),
                Tier("D")
                ]
            )

        result = create_tier_list()

        self.assertEqual(result, tierlist)

if __name__ == "__main__":
    unittest.main()