# Command & Conquer: Generals – Shinobi Wars Mod

> A comprehensive total-conversion mod framework for **Command & Conquer: Generals / Zero Hour** where the military factions are replaced by the Great Ninja Villages of *Naruto*.

---

## 1. Overview & Core Solution

In the *Naruto* world, traditional mechanized vehicles (tanks, helicopters, artillery trucks) do not exist. Rather than awkwardly shoehorning modern tanks into the ninja world or giving ninja modern rocket launchers, **Shinobi Wars** maps the tactical RTS combat roles of C&C Generals directly to lore-accurate ninja disciplines:

```
+-----------------------------------------------------------------------------------------+
| RTS Classic Role     | Shinobi Wars Translation       | In-Engine Role & Mechanics      |
+----------------------+--------------------------------+---------------------------------+
| Light Skirmish / APC | Kugutsu (Puppet) Operators     | Rapid poison needle Gatling;    |
|                      | Inuzuka Hound Cavalry          | transport slots; immunity to    |
|                      |                                | poison; hardwood armor          |
+----------------------+--------------------------------+---------------------------------+
| Medium Battle Tank   | Akimichi Human Boulder         | Kinetic crushing momentum;      |
|                      | Lightning Chakra Cloak Elite   | anti-fortification; crushes     |
|                      |                                | regular infantry                |
+----------------------+--------------------------------+---------------------------------+
| Heavy / Super Tank   | Giant Summons (Kuchiyose)      | Massive health pool; water      |
|                      | - Gamabunta & Giant Toads      | cannons & giant iron cleavers;  |
|                      | - Sand Golems & Giant Rhinos   | cliff-leaping locomotor         |
+----------------------+--------------------------------+---------------------------------+
| Long-Range Artillery | Elemental Master Batteries     | Long-range explosive fireballs, |
|                      | - Fūton Wind Scythes (Suna)    | vacuum blades, and lightning    |
|                      | - Kumo Chakra Cannon Carriage  | beams; fragile in melee         |
+----------------------+--------------------------------+---------------------------------+
| Aircraft / Bombers   | Chōjū Giga (Ink Birds - Sai)   | Aerial strafing runs, dropping  |
|                      | Deidara C2 Clay Dragons        | explosive tags and clay bombs   |
+----------------------+--------------------------------+---------------------------------+
```

---

## 2. Playable Factions

### 🍃 Konohagakure (The Hidden Leaf)
- **Role Model**: Balanced, clan synergies, versatile tactical toolkit (USA counterpart).
- **Core Units**: Genin Squad, Hyuga Gentle Fist Specialist, Inuzuka Hound Scout, Akimichi Human Boulder, Kuchiyose Giant Battle Toad, Chōjū Giga Ink Birds, Gamabunta.
- **Forbidden Jutsu (Superweapon)**: *Mokuton: Deep Forest Emergence (Jukai Kōtan)*.

### ⏳ Sunagakure (The Hidden Sand)
- **Role Model**: Fortified defense, deadly poisons, puppet swarms, wind artillery (GLA/China hybrid).
- **Core Units**: Desert Genin, Wind Scythe Snipers, Karasu (Crow) Needle Skirmisher, Sanshōuo (Salamander) Armored Carrier, Sand Golem.
- **Economy Perk**: Gold Dust Extractors passively sift Ryo over time.
- **Forbidden Jutsu (Superweapon)**: *Desert Sand Imperial Funeral (Sabaku Taisō)*.

### ⚡ Kumogakure (The Hidden Cloud)
- **Role Model**: Blitzkrieg shock assault, kenjutsu masters, high-tech chakra artillery.
- **Core Units**: Dual Swordsmen, Lightning Armor Raikage Disciples, Mobile Chakra Cannon Platform.
- **Forbidden Jutsu (Superweapon)**: *Guiding Thunder Cannon / Kirin*.

### ☁️ Akatsuki (The Rogue Syndicate)
- **Role Model**: Asymmetric warfare, expendable bio-clones, suicide traps, brutal summons (GLA counterpart).
- **Core Units**: White Zetsu Workers, Rogue Nukenin, Kibaku Nendo Clay Spiders, C2 Clay Dragons, Giant Rhino Battering Ram.
- **Forbidden Jutsu (Superweapon)**: *Planetary Devastation (Chibaku Tensei)*.

---

## 3. Economy: The Ryo & Mission System

- **Primary Currency**: **Ryo (両)**.
- **Mission Outposts**: Neutral Daimyo outposts replace Supply Docks. **Courier Shinobi** run high-speed courier routes to bring mission compensation scrolls back to the village Headquarters.
- **Capturable Springs**: Tech Chakra Springs provide continuous income and heal nearby chakra-depleted ninja.

---

## 4. Mod Directory Structure

```
NarutoShinobiWars/
├── Data/
│   ├── INI/
│   │   ├── Armor.ini              # Damage matrix (Cloth, Flak, Hardwood, Beast Hide)
│   │   ├── Weapon.ini             # Kunai, paper bombs, jutsus, giant summon weapons
│   │   ├── PlayerTemplate.ini     # Faction registration for skirmish/multiplayer
│   │   ├── Locomotor.ini          # Speed, agility, and leaping physics
│   │   ├── Upgrade.ini            # Village tech tree & clan jutsus
│   │   ├── CommandSet.ini         # UI build & recruit grids
│   │   ├── CommandButton.ini      # Actions, costs, and buttons
│   │   ├── Science.ini            # Shinobi Rank powers (Generals Powers)
│   │   ├── SpecialPower.ini       # Kinjutsu cooldowns & triggers
│   │   └── Object/
│   │       ├── Konoha/            # Leaf infantry, heavy units, buildings
│   │       ├── Suna/              # Sand infantry, puppets, buildings
│   │       ├── Kumo/              # Cloud units & lightning cannons
│   │       ├── Akatsuki/          # Rogue ninja & clay bombers
│   │       └── Neutral/           # Daimyo outposts & chakra springs
```

---

## 5. How to Install & Test

1. **Option A: Loose Files (Direct Development Mode)**:
   - Navigate to your *Command & Conquer: Generals - Zero Hour* installation directory (e.g. `C:\Games\Command and Conquer Generals Zero Hour`).
   - Copy the `Data/` folder from `NarutoShinobiWars` directly into your Zero Hour folder.
   - Run the game executable (`generals.exe`).

2. **Option B: `.big` Archive Packaging**:
   - Open **FinalBIG** (standard C&C modding tool).
   - Create a new archive named `!!!NarutoShinobiWars.big`.
   - Add the `Data/` folder into the archive.
   - Drop `!!!NarutoShinobiWars.big` into your game root. The triple exclamation points ensure it loads with priority over default game files.

---

## 6. Recommended Workspace Setting

Set this directory as your active workspace in Antigravity:
`C:\Users\court\.gemini\antigravity\scratch\NarutoShinobiWars`
