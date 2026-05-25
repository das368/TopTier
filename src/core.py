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