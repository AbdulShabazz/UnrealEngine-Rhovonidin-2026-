- [ ] Outline foes to denote player focus. (strategic) Player can swap out weapons. The carousel lingers (not requiring interactivity) until the foe order settles: The player initiates the carousel, up to a point, then takes damage if he lingers too long.
- [ ] Add carousel sequence interludes for player to experience the action.
- [ ] Sideload ShakeOff SoundFX
- [ ] Strategic tall trees are climbable for the player to view terrain, as a form of game ambience and strategy.
- [ ] Carousel: up to 6 levels of damage (15%, 30%, 45%, 60%, 75%, 90%)
- [ ] Ensure NPC obj refs exit the carousel before memory free
- [ ] Bottom center justify the carousel to reduce the player distraction 
- [ ] In the environment, use Player-designated hotspots to better coordinate anims
- [ ] Bar-Hades (H) can cast flames against the cavern walls. If Lance hides, H swipes the smoldering brimstone across the landscape until Lance again reaches the center while fleeing again across the screen, where he swats his tail against the Hearth attempting to flatten him. Him Lance allows H’s eyes to fall from view (H) spawns an electrocution ball which stuns Lance long enough to fatally flatten him by again swatting his tail.
- [ ] AI NPCs can use Speed and or Strength plus optional Coordination/Strategy to devise maximum damage to Lance. H can open a crevasse and then shift the world for Lance to fall.
- [ ] AI-based Fuzzy range-based hierarchical dictionary keys (to speed up rewrites and search, guaranteed to halt deterministically) Search attributes based on context aware gameplay tags/anim notify tags
- [ ] Story Goal: Map the planet , eliminate threats on the ground.
- [ ] Choreograph subtle (Boss) animations to the game's soundtrack 
- [ ] Add a Captions folder!
- [ ] Music theme: open level (cinematic orchestra); Bosses den (Solo instruments); Boss lair (Death Metal/808-Trap)
- [ ] Once NPCs spot Lance (in cinematic) FADE TO BLACK and cue current level Death Metal theme before ultimate SMASH CUT
- [ ] Map Level Orchestral loops and Solos are unlocked for all levels once that level is defeated.
- [ ] In-game Orchestral loops are determined by the next waypoint (biome) targeted.
- [ ] There is only one save point (the crashed ship) in the game, Lance must successfully traverse back and forth further across the map to progress.
- [ ] Climate changes with each overriding theme 
- [ ] Revise Settings overlay to show realtime changes to viewport after adjusting in-game settings.
- [ ] The crashed recon starship (map) can teleport Lance anywhere on the island (continue gameplay)
- [ ] Adapt main character to meta human rig
- [ ] Perhaps employ an intermittent HP bar

NOTES

Combat loop
[ Attack Window ms ] >> [ Cooldown ms ] ) | [ Take Damage ]

To build (NPC) animation libraries, use Sequencer + Control Rig/Skeletal Mesh + blueprints to choreograph  and distill animations. 

Investigate one-off procedural PCG levels that are minimappable. Support savepoints (and control resets!); and support teleportation hotspots the player can earn. Perhaps use hash tables to index the PCG tile seeds, or regenerate the tiles in a deterministic manner (e.g., for each new radial tile set) Or perhaps: Assign stable PCG tile seeds -- radially, in a clockwise manner, starting from the North face, using biome/water lock rules.

Search for animNotifies
Try to catalog additional animations
Formalize boss battles for each biome
Prepare for soundtrack development 

Bar Hades grows 2,3,6 heads, based upon threat level.
Ultrawolf can slap Lance across the map, causing a one-hit kill.

UltraWolf specializes in ground & pound combat, wall tosses, throws, kicks, blocks, and shoves, and every fourth spawn is invincible -- a theatre shot-caller and master strategist. He should be avoided. He can interrupt Lance's bow when close enough.

The Bard NPC is an aerial sniper and long distance threat  He has rocket boots and has to land to reload. He hurls smoke, he stirs fog, wind, and dust. Rolling incendiary devices are a threat.

Queue atmospheric music near cooldown/level-up areas.
