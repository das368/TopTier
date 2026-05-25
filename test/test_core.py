import unittest

from src.tierlist import TierList
from src.tier import Tier
from src.image_item import ImageItem
from src.core import create_tier_list, rename_tier_list, rename_tier, add_image_item_to_tierlist, move_image_to_tier


class CoreTests(unittest.TestCase):
    def test_core_creates_default_tier_list(self):
        result = create_tier_list()

        self.assertEqual(result.name, "Untitled")
        self.assertEqual([tier.name for tier in result.tiers], ["S", "A", "B", "C", "D"])
    
    def test_core_creates_default_tier_list_with_name(self):
        result = create_tier_list("My Tierlist")

        self.assertEqual(result.name, "My Tierlist")
        self.assertEqual([tier.name for tier in result.tiers], ["S", "A", "B", "C", "D"])
    
    def test_core_renames_tierlist(self):
        tierlist = create_tier_list("Old Tierlist")

        result = rename_tier_list(tierlist, "New Tierlist")

        self.assertEqual(result.name, "New Tierlist")
    
    def test_core_renames_tier(self):
        tierlist = create_tier_list()

        result = rename_tier(tierlist, 0, "New Tier")

        self.assertEqual(result.tiers[0].name, "New Tier")
    
    def test_core_adds_image_to_tierlist(self):
        tierlist = create_tier_list()
        image_item = ImageItem(
            id="8f2b5f2e-1471-4f7f-83cb-8c6b98e67a12",
            path="assets/images/test.png",
            original_name="test.png"
            )

        result = add_image_item_to_tierlist(tierlist, image_item)

        self.assertEqual(result.image_items[0], image_item)
    
    def test_core_moves_image_to_tier_by_id(self):
        tierlist = create_tier_list()
        image_item = ImageItem(
            id="8f2b5f2e-1471-4f7f-83cb-8c6b98e67a12",
            path="assets/images/test.png",
            original_name="test.png"
            )
        tierlist = add_image_item_to_tierlist(tierlist, image_item)

        result = move_image_to_tier(tierlist, image_item.id, 0)

        self.assertEqual(result.tiers[0].images[0], image_item.id)

    

if __name__ == "__main__":
    unittest.main()