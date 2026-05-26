from src.tierlist import TierList
from src.tier import Tier

def create_tier_list(name="Untitled"):
    tierlist = TierList(
        name = name,
        tiers = [
            Tier(name="S"),
            Tier(name="A"),
            Tier(name="B"),
            Tier(name="C"),
            Tier(name="D")
            ]
        )
    return tierlist

def rename_tier_list(tierlist, new_name):
    tierlist.name = new_name
    return tierlist

def rename_tier(tierlist, index, new_name):
    tierlist.tiers[index].name = new_name
    return tierlist

def add_image_item(tierlist, image_item):
    tierlist.image_items.append(image_item)
    return tierlist

def move_image_to_tier(tierlist, image_id, index):
    for tier in tierlist.tiers:
        if image_id in tier.images:
            tier.images.remove(image_id)
    
    tierlist.tiers[index].images.append(image_id)
    return tierlist

def get_unassigned_images(tierlist):
    assigned_ids = []

    for tier in tierlist.tiers:
        assigned_ids.extend(tier.images)
    
    return [
        image_item
        for image_item in tierlist.image_items
        if image_item.id not in assigned_ids
    ]

def delete_image_item(tierlist, image_id):
    for tier in tierlist.tiers:
        if image_id in tier.images:
            tier.images.remove(image_id)
    tierlist.image_items = [
        image_item
        for image_item in tierlist.image_items
        if image_item.id != image_id
    ]
    return tierlist