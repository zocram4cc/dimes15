# PES 2015 AI Constants Tool & Tactical Patch

This repository contains both the definitive AI constants tool for Pro Evolution Soccer 2015 and a comprehensive tactical overhaul of the game's defensive and transition logic.

## Overview

The PES AI constants are stored in binary files located in `dt18_win.cpk` (specifically in the `common/match/constant/` folder). These `.bin` files control the game's fundamental artificial intelligence.

The variable names are mapped internally within `PES2015.exe`. This tool uses a **Dynamic Triple-Signature Locking** mechanism to extract those names and align them with the binary data, bypassing unrelated networking and UI strings.

## Included Tactical Patch

This repository includes a pre-applied tactical overhaul in the `data/` directory. Key changes include:
- **Higher Defensive Block**: Increased line height and restricted retreat distance.
- **Aggressive Challenge Logic**: Expanded sliding range and reduced observation delays.
- **Tightened Marking**: Increased proximity and expanded zonal alertness.
- **Vertical Urgency**: Maximum priority for forward runs upon winning possession.

See [PATCH_NOTES.md](PATCH_NOTES.md) for detailed technical specifications of the changes.

## Prerequisites

- `PES2015.exe`: The game's main executable (required for variable name extraction).
- `bins/common/match/constant/`: A folder containing the unzlibbed `.bin` files:
  - `constant_match.bin`
  - `constant_player.bin`
  - `constant_team.bin`

## Usage

The tool has two main modes: `unpack` and `pack`.

### Unpacking AI Constants

To extract the constants into editable text files:

```bash
python3 ai_tool_15.py unpack
```

- **Output Directory**: `data/`
- **Structure**: The files are organized by category (`match`, `player`, `team`). Each `.txt` file contains values with their corresponding variable names as comments.
- **PlayStyle Overrides**: The tool automatically extracts behavioral "Recipes" for specific player cards into `data/player/output/playStyle_recipes/`.

### Packing AI Constants

After modifying the values in the `.txt` files, you can pack them back into the binary files:

```bash
python3 ai_tool_15.py pack
```

- **Effect**: Updates the `.bin` files in the `bins/` directory.
- **Header Updates**: The tool automatically recalculates file lengths and offsets in the `.bin` header.

## Technical Details

### Variable Mapping
The tool utilizes a **14-step stride** identified within the `ScriptBind` property blocks of the PES 2015 executable. It uses unique variable signatures (e.g., `airRegistNormal` for Ball, `adjustAngle_FreeKickSupport` for Team) to definitively lock onto the correct memory blocks regardless of EXE version or regional differences.

### Bit-Packed Booleans (HEX)
Some variables are bit-packed into a single 4-byte slot. The tool identifies these via a `PACKING_MAP` and represents them as:
`0.0 //HEX 0x..., contains var1, var2, var3, NULL`

### Shadow Arrays
The tool identifies repeated data structures (like the 9 difficulty levels in `cpuLevel`) and labels them semantically:
`128 //bpDirectPlay[0]`

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits

Tomato
