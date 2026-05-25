import unittest

from src.tierlist import TierList
from src.tier import Tier
from src.core import create_tier_list, rename_tier_list, rename_tier


class CoreTests(unittest.TestCase):
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

        self.assertEqual(result.name, tierlist.name)
        self.assertEqual([tier.name for tier in result.tiers], ["S", "A", "B", "C", "D"])
    
    def test_core_creates_default_tier_list_with_name(self):
        tierlist = TierList(
            name="My Tierlist",
            tiers=[
                Tier("S"),
                Tier("A"),
                Tier("B"),
                Tier("C"),
                Tier("D")
                ]
            )

        result = create_tier_list("My Tierlist")

        self.assertEqual(result.name, tierlist.name)
        self.assertEqual([tier.name for tier in result.tiers], ["S", "A", "B", "C", "D"])
    
    def test_core_renames_tierlist(self):
        tierlist = create_tier_list("Old Tierlist")

        result = rename_tier_list(tierlist, "New Tierlist")

        self.assertEqual(result.name, "New Tierlist")
    
    def test_core_renames_tier(self):
        tierlist = create_tier_list()

        result = rename_tier(tierlist, 0, "New Tier")

        self.assertEqual(result.tiers[0].name, "New Tier")
    
    

if __name__ == "__main__":
    unittest.main()