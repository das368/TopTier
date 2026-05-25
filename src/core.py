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