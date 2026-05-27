import unittest

from src.image_item import ImageItem
from src.core import create_tier_list, rename_tier_list, rename_tier, add_image_item, move_image_to_tier, get_unassigned_images, delete_image_item, reorder_image_in_tier


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

        result = add_image_item(tierlist, image_item)

        self.assertEqual(result.image_items[0], image_item)
    
    def test_core_moves_image_to_tier_by_id(self):
        tierlist = create_tier_list()
        image_item = ImageItem(
            id="8f2b5f2e-1471-4f7f-83cb-8c6b98e67a12",
            path="assets/images/test.png",
            original_name="test.png"
            )
        tierlist = add_image_item(tierlist, image_item)

        result = move_image_to_tier(tierlist, image_item.id, 0)

        self.assertEqual(result.tiers[0].images, [image_item.id])

    def test_core_moves_image_between_tiers(self):
        tierlist = create_tier_list()
        image_item = ImageItem(
            id="8f2b5f2e-1471-4f7f-83cb-8c6b98e67a12",
            path="assets/images/test.png",
            original_name="test.png"
            )
        tierlist = add_image_item(tierlist, image_item)

        move_image_to_tier(tierlist, image_item.id, 0)

        result = move_image_to_tier(tierlist, image_item.id, 1)

        self.assertEqual(result.tiers[0].images, [])
        self.assertEqual(result.tiers[1].images, [image_item.id])
    
    def test_core_does_not_duplicate_image_when_moved_to_same_tier(self):
        tierlist = create_tier_list()
        image_item = ImageItem(
            id="8f2b5f2e-1471-4f7f-83cb-8c6b98e67a12",
            path="assets/images/test.png",
            original_name="test.png"
            )
        tierlist = add_image_item(tierlist, image_item)

        move_image_to_tier(tierlist, image_item.id, 0)

        result = move_image_to_tier(tierlist, image_item.id, 0)

        self.assertEqual(result.tiers[0].images, [image_item.id])
    
    def test_core_can_retrieve_unassigned_images(self):
        tierlist = create_tier_list()
        image_item1 = ImageItem(
            id="123",
            path="assets/images/test1.png",
            original_name="test1.png"
            )
        image_item2 = ImageItem(
            id="321",
            path="assets/images/test2.png",
            original_name="test2.png"
            )
        tierlist = add_image_item(tierlist, image_item1)
        tierlist = add_image_item(tierlist, image_item2)
        
        move_image_to_tier(tierlist, image_item1.id, 0)

        result = get_unassigned_images(tierlist)

        self.assertEqual(result, [image_item2])
    
    def test_core_can_delete_image_items(self):
        tierlist = create_tier_list()
        image_item = ImageItem(
            id="8f2b5f2e-1471-4f7f-83cb-8c6b98e67a12",
            path="assets/images/test.png",
            original_name="test.png"
            )
        tierlist = add_image_item(tierlist, image_item)

        move_image_to_tier(tierlist, image_item.id, 0)

        result = delete_image_item(tierlist, image_item.id)

        self.assertEqual(result.image_items, [])
        self.assertEqual(result.tiers[0].images, [])
    
    def test_core_preserves_image_order_in_tier(self):
        tierlist = create_tier_list()
        image_item1 = ImageItem(
            id="123",
            path="assets/images/test1.png",
            original_name="test1.png"
            )
        image_item2 = ImageItem(
            id="321",
            path="assets/images/test2.png",
            original_name="test2.png"
            )
        tierlist = add_image_item(tierlist, image_item1)
        tierlist = add_image_item(tierlist, image_item2)
        
        move_image_to_tier(tierlist, image_item1.id, 0)

        result = move_image_to_tier(tierlist, image_item2.id, 0)

        self.assertEqual(result.tiers[0].images, [image_item1.id,image_item2.id])
    
    def test_core_can_reorder_images_within_tier(self):
        tierlist = create_tier_list()
        image_item1 = ImageItem(
            id="111",
            path="assets/images/test1.png",
            original_name="test1.png"
            )
        image_item2 = ImageItem(
            id="222",
            path="assets/images/test2.png",
            original_name="test2.png"
            )
        image_item3 = ImageItem(
            id="333",
            path="assets/images/test3.png",
            original_name="test3.png"
            )
        tierlist = add_image_item(tierlist, image_item1)
        tierlist = add_image_item(tierlist, image_item2)
        tierlist = add_image_item(tierlist, image_item3)

        move_image_to_tier(tierlist, image_item1.id, 0)
        move_image_to_tier(tierlist, image_item2.id, 0)
        move_image_to_tier(tierlist, image_item3.id, 0)

        result = reorder_image_in_tier(tierlist, 0, image_item3.id, 0)

        self.assertEqual(result.tiers[0].images, [image_item3.id, image_item1.id, image_item2.id])




if __name__ == "__main__":
    unittest.main()