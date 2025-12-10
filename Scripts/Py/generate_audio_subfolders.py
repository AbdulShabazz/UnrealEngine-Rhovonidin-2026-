
import os

STRUCTURE = """
Content/Audio/SFX/Ambient/Coliseum/Crowd_Murmur
Content/Audio/SFX/Ambient/Coliseum/Arena_Wind
Content/Audio/SFX/Ambient/Coliseum/Stone_Echo
Content/Audio/SFX/Ambient/City_Marketplace/Market_Chatter
Content/Audio/SFX/Ambient/City_Marketplace/Vendors
Content/Audio/SFX/Ambient/City_Marketplace/Bells
Content/Audio/SFX/Ambient/City_Marketplace/Street_Ambience
Content/Audio/SFX/Ambient/Forest/Forest_Day
Content/Audio/SFX/Ambient/Forest/Forest_Night
Content/Audio/SFX/Ambient/Forest/Birds
Content/Audio/SFX/Ambient/Forest/Wind
Content/Audio/SFX/Ambient/Dungeon_Cave/Drips
Content/Audio/SFX/Ambient/Dungeon_Cave/Low_Wind
Content/Audio/SFX/Ambient/Dungeon_Cave/Insects
Content/Audio/SFX/Ambient/Temple_Sacred/Chants
Content/Audio/SFX/Ambient/Temple_Sacred/Choir
Content/Audio/SFX/Ambient/Temple_Sacred/Organ
Content/Audio/SFX/Ambient/Weather/Wind_Generic
Content/Audio/SFX/Ambient/Weather/Storm_Thunder_Rain
Content/Audio/SFX/Ambient/Fire/Campfire
Content/Audio/SFX/Ambient/Fire/Torches
Content/Audio/SFX/Ambient/Water/River_Flow
Content/Audio/SFX/Ambient/Water/Stream
Content/Audio/SFX/Foley/Footsteps/Stone_Marble
Content/Audio/SFX/Foley/Footsteps/Sand_Dust
Content/Audio/SFX/Foley/Footsteps/Wood_Plank
Content/Audio/SFX/Foley/Footsteps/Grass_Meadow
Content/Audio/SFX/Foley/Footsteps/Water_Shallow
Content/Audio/SFX/Foley/Movement/Walk
Content/Audio/SFX/Foley/Movement/Run
Content/Audio/SFX/Foley/Movement/Sprint
Content/Audio/SFX/Foley/Movement/Dodge_Roll
Content/Audio/SFX/Foley/Movement/Jump
Content/Audio/SFX/Foley/Movement/Land
Content/Audio/SFX/Foley/Movement/Horse_Ride
Content/Audio/SFX/Foley/Movement/Vehicle_Engine
Content/Audio/SFX/Combat/Weapons/Sword/Swings
Content/Audio/SFX/Combat/Weapons/Sword/Impacts_Armor
Content/Audio/SFX/Combat/Weapons/Sword/Impacts_Flesh
Content/Audio/SFX/Combat/Weapons/Spear/Swings
Content/Audio/SFX/Combat/Weapons/Spear/Impacts
Content/Audio/SFX/Combat/Weapons/Axe/Swings
Content/Audio/SFX/Combat/Weapons/Axe/Impacts
Content/Audio/SFX/Combat/Weapons/Mace_Flail/Swings
Content/Audio/SFX/Combat/Weapons/Mace_Flail/Impacts
Content/Audio/SFX/Combat/Weapons/Parry_Counter
Content/Audio/SFX/Combat/Weapons/Weapon_Clash_Heavy
Content/Audio/SFX/Combat/Weapons/Weapon_Clash_Light
Content/Audio/SFX/Combat/Weapons/Unsheathe_Sheathe
Content/Audio/SFX/Combat/Impacts_Damage/Armor_Clank
Content/Audio/SFX/Combat/Impacts_Damage/Shield_Block
Content/Audio/SFX/Combat/Impacts_Damage/Critical_Hit
Content/Audio/SFX/Combat/Impacts_Damage/Blood_Gore
Content/Audio/SFX/Combat/Impacts_Damage/Body_Falls
Content/Audio/SFX/Combat/Vocals/Grunts_Pain
Content/Audio/SFX/Combat/Vocals/Effort_Attack
Content/Audio/SFX/Combat/Vocals/Death_Cries
Content/Audio/SFX/Magic_Spells/Cast_Initiation
Content/Audio/SFX/Magic_Spells/Charge_Buildup
Content/Audio/SFX/Magic_Spells/Projectile_Travel
Content/Audio/SFX/Magic_Spells/Impact_Explosion
Content/Audio/SFX/Magic_Spells/Buff_Debuff_Auras
Content/Audio/SFX/Magic_Spells/Teleport_Portal
Content/Audio/SFX/Magic_Spells/UI_Cast_Success_Fail
Content/Audio/SFX/Items_Interaction/Item_Pickup
Content/Audio/SFX/Items_Interaction/Item_Equip_Unequip
Content/Audio/SFX/Items_Interaction/Potion_Use
Content/Audio/SFX/Items_Interaction/Chest_Open
Content/Audio/SFX/Items_Interaction/Container_Open
Content/Audio/SFX/Items_Interaction/Coin_Gold_Jingle
Content/Audio/SFX/Items_Interaction/Weapon_Armor_Break
Content/Audio/SFX/Items_Interaction/Crafting_Upgrade
Content/Audio/SFX/Environment_Interaction/Door_Open
Content/Audio/SFX/Environment_Interaction/Door_Close
Content/Audio/SFX/Environment_Interaction/Object_Break_Wood
Content/Audio/SFX/Environment_Interaction/Object_Break_Stone
Content/Audio/SFX/Environment_Interaction/Switch_Lever
Content/Audio/SFX/Creatures/Dragon/Roar
Content/Audio/SFX/Creatures/Dragon/Wing_Flap
Content/Audio/SFX/Creatures/Dragon/Fire_Breath
Content/Audio/SFX/Creatures/Dragon/Footsteps
Content/Audio/SFX/Creatures/Ogre/Grunts_Roars
Content/Audio/SFX/Creatures/Ogre/Footsteps
Content/Audio/SFX/Creatures/Mystical_Beast/Roars
Content/Audio/SFX/Creatures/Mystical_Beast/Vocals
Content/Audio/UI/Menu/Open
Content/Audio/UI/Menu/Close
Content/Audio/UI/Buttons/Click_Confirm
Content/Audio/UI/Buttons/Cancel_Back
Content/Audio/UI/Buttons/Error_Invalid
Content/Audio/UI/Inventory/Slot_Select
Content/Audio/UI/Inventory/Item_Pickup
Content/Audio/UI/Notifications/Alert
Content/Audio/UI/Notifications/Skill_Unlock_LevelUp
Content/Audio/UI/Notifications/General_Confirmation
Content/Audio/UI/Notifications/General_Cancel
Content/Audio/Dialogue/NPC/Greeting
Content/Audio/Dialogue/NPC/Farewell
Content/Audio/Dialogue/NPC/Quest_Completion
Content/Audio/Dialogue/NPC/Quest_Offer
Content/Audio/Dialogue/Narration_VO/Story_VO
Content/Audio/Dialogue/Narration_VO/Tutorial_VO
Content/Audio/Music/Loops_Ambient/Arena_Theme
Content/Audio/Music/Loops_Ambient/Exploration_Theme
Content/Audio/Music/Loops_Ambient/Boss_Fight_Theme
Content/Audio/Music/Loops_Ambient/Victory_Triumph
Content/Audio/Music/Loops_Ambient/Defeat_GameOver
Content/Audio/Music/Cinematic_Cues/Cinematic_Music_Cue
Content/Audio/Music/Cinematic_Cues/Stingers_Transitions
Content/Audio/Cinematic_SFX/Transition_Swish
Content/Audio/Cinematic_SFX/Impact_Sweeteners
Content/Audio/Cinematic_SFX/Trailer_Whooshes
""".strip().split('\n')

def main():
    for path in STRUCTURE:
        os.makedirs(path, exist_ok=True)
        folder_name = os.path.basename(path)
        readme_path = os.path.join(path, "README.md")
        with open(readme_path, 'w') as f:
            f.write(f"# {folder_name.replace('_', ' ')}\n\nPlace audio assets here.\n")
    print(f"Created {len(STRUCTURE)} folders with README.md files.")

if __name__ == "__main__":
    main()