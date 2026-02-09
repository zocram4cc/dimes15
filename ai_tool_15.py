import struct
import os
import re

# PES 2015 Tactical Engine - Definitive Restoration Tool
# Stride 14 Stride Alignment: Match (5393), Player (5645), Team (6065)

PACKING_MAP = {
    "ball": { "rotationCustom": 2 },
    "blockDebug": {
        "defence": 3, "moveKind": 1, "parameter": 3, "fishDive": 3, "heel": 3,
        "offence": 2, "kickAuto": 3, "kickDebug": 8, "kickPointBall": 2,
        "kickPointDirect": 2, "kickPointGoal": 2, "kickPosition": 6, "retry": 3
    },
    "inplayDemo": { "isHard": 2 },
    "pes15Test": { "enable": 2, "pressUpdateTimer": 8, "waitTimer": 10, "projectKick": 7 },
    "setplayGuideCornerKick": { "rot": 6, "speed": 7, "spin": 10 },
    "setplayGuideFreeKickFar": { "rot": 6, "speed": 7, "spin": 10 },
    "setplayGuideFreeKickMiddle": { "rot": 6, "speed": 7, "spin": 10 },
    "setplayGuideFreeKickNear": { "rot": 6, "speed": 7, "spin": 10 },
    "setplayGuideGoalKick": { "rot": 6, "speed": 7, "spin": 10 },
    "ballplayerDribble": { "DashCheckSecotor": 2, "MatchUp": 14, "Nomal": 5, "Safety": 10 },
    "ballplayerGk": { "ClearInfo": 2, "LongPassInfo": 5, "ShortPassInfo": 6 },
    "ballplayerSetplay": { "FreekickShoot": 5, "Throwin": 3 },
    "ballplayerShoot": { "rangeAngleGoalFront": 6 },
    "block": { "press": 8, "touchAfterSec": 2, "centering": 4 },
    "centering": { "debugDisp": 4, "isSkillLowLob": 2, "searchTest": 3 },
    "dribble": { "adjustAngleFlag": 3, "slowDribble": 4, "staggerDribble": 2 },
    "flypass": { "height": 13, "manual": 8, "search": 12 },
    "freemove": { "runLoopBank": 3, "stepMoveFront": 6 },
    "gk": { "anime": 18 },
    "grounderpass": { "calcRecieveSpeed": 4, "debug": 4, "lob": 7, "manual": 5, "search": 5 },
    "passget": { "autoFrontMove": 7, "inputMoveAir": 9, "thinkPressFilterUntilTargetBallThrough": 4 },
    "shoot": { "advanceLoop": 6, "control_dy": 3, "loop": 4, "normal_dy": 3 },
    "sliding": { "animeAccelLimitSpeed": 5 },
    "tackle": { "anime": 32, "stepMoveAutoTackleFarEnable": 3 },
    "throughpass": { "debugDisp": 2, "gageTest1": 4, "searchTest": 4 },
    "basePosition": { "defenceFormationTest1": 3, "dfCoverAdjustX": 3 },
    "pullAway": { "eyeOff": 4 }
}

STYLE_NAMES = {
    0: "GoalPoacher", 1: "DummyRunner", 2: "AnchorMan", 3: "HolePlayer",
    4: "CreativePlaymaker", 5: "OffensiveFullback", 6: "TrackBack",
    7: "TargetMan", 8: "LongBallExpert", 9: "ClassicNo10",
    10: "ProlificWinger", 11: "Destroyer", 12: "ExtraFrontman",
    13: "FullbackFinisher", 14: "FoxInTheBox", 15: "BoxToBox",
    16: "TheOrchestrator", 17: "WingMidfielder", 18: "InceptiveWinger",
    19: "DefensiveFullback", 20: "OffensiveGK", 21: "DefensiveGK"
}

def extract_blocks_from_exe(exe_path):
    if not os.path.exists(exe_path): return [], -1, -1, -1
    with open(exe_path, 'rb') as f: data = f.read()
    tokens = re.findall(b'ScriptBind|[a-zA-Z0-9_]{3,}', data)
    blocks = []; cur = []
    for t in tokens:
        t_d = t.decode('ascii', 'ignore')
        if t_d == 'ScriptBind':
            blocks.append(cur[:]); cur = []
        else: cur.append(t_d)
    if cur: blocks.append(cur)
    rev = blocks[::-1]
    
    # Precise markers for tactical section, bypassing networking
    ball_idx = -1; avoid_idx = -1; base_pos_idx = -1
    for i, b in enumerate(rev):
        if 'msgid' in b or 'rqid' in b or 'svrtype' in b: continue
        if 'airRegistNormal' in b and len(b) > 30 and ball_idx == -1: ball_idx = i
        if 'angleDelta' in b and len(b) == 18 and avoid_idx == -1: avoid_idx = i
        if 'adjustAngle_FreeKickSupport' in b and base_pos_idx == -1: base_pos_idx = i
            
    return rev, ball_idx, avoid_idx, base_pos_idx

def get_names_from_bin(bin_path):
    with open(bin_path, 'rb') as f: data = f.read()
    count = struct.unpack('<I', data[0:4])[0]
    num_vals = 3 * count + 1
    names = re.findall(b'([a-zA-Z0-9_]+)\.o\x00', data)
    return [n.decode('ascii') for n in names[:count]], data, count, num_vals

def unpack_bin(bin_path, exe_blocks, category, start_idx):
    names, data, count, num_vals = get_names_from_bin(bin_path)
    vals = struct.unpack('<' + 'I' * num_vals, data[4:4+num_vals*4])
    output_dir = f"data/{category}/output"
    os.makedirs(output_dir, exist_ok=True)
    file_map = {i: name for i, name in enumerate(names)}
    
    print(f"Unpacking {bin_path}...")
    for i, name in enumerate(names):
        start = vals[1] if i == 0 else vals[1 + i*3]
        length = vals[2 + i*3]
        file_data = data[start : start + length]
        n_bin = len(file_data) // 4
        block_idx = start_idx + (i * 14)
        var_names = exe_blocks[block_idx] if block_idx < len(exe_blocks) else []
        
        if name == "playStyle":
            unpack_to_file(os.path.join(output_dir, name + ".txt"), file_data, var_names, len(var_names), n_bin, name)
            recipe_dir = os.path.join(output_dir, "playStyle_recipes")
            os.makedirs(recipe_dir, exist_ok=True)
            for sid in range(156):
                s_ptr = struct.unpack('<i', file_data[sid*4 : sid*4+4])[0]
                if 156 < s_ptr < len(file_data) - 88:
                    recipe_name = STYLE_NAMES.get(sid, f"Style_{sid}")
                    with open(os.path.join(recipe_dir, f"{recipe_name}.txt"), 'w') as rf:
                        rf.write(f"// --- RECIPE FOR {recipe_name} ---\n")
                        sub_ptrs = struct.unpack('<' + 'i'*22, file_data[s_ptr : s_ptr + 88])
                        for pid, pval in enumerate(sub_ptrs):
                            target_file = file_map.get(pid, "UNKNOWN")
                            rf.write(f"{pval} // Pointer to {target_file} Template\n")
                            if 0 < pval < len(file_data) - 80:
                                t_data = file_data[pval : pval + 80]
                                t_dir = os.path.join(recipe_dir, recipe_name)
                                os.makedirs(t_dir, exist_ok=True)
                                # Player templates are based on block 5645
                                t_vars = exe_blocks[5645 + (pid * 14)] if (5645 + (pid * 14)) < len(exe_blocks) else []
                                unpack_to_file(os.path.join(t_dir, f"{target_file}.txt"), t_data, t_vars, len(t_vars), 20, target_file)
            continue
        unpack_to_file(os.path.join(output_dir, name + ".txt"), file_data, var_names, len(var_names), n_bin, name)

def unpack_to_file(output_path, file_data, var_names, n_exe, n_bin, name):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        bin_ptr = 0; name_ptr = 0
        file_packing = PACKING_MAP.get(name, {})
        n_vars_available = len(var_names)
        while bin_ptr < n_bin:
            # Difficulty array logic (32 vars x 9 levels)
            if name == "cpuLevel" and n_vars_available == 32:
                f.write(f"{struct.unpack('<i', file_data[bin_ptr*4:(bin_ptr+1)*4])[0]} //{var_names[bin_ptr % 32]}[{bin_ptr // 32}]\n")
                bin_ptr += 1; continue
            
            if bin_ptr > 0 and n_exe > 1 and bin_ptr % n_exe == 0:
                f.write(f"\n// --- SHADOW ARRAY INSTANCE {bin_ptr // n_exe} ---\n")
                name_ptr = 0
            if name_ptr < n_vars_available:
                cur_name = var_names[name_ptr]
                chunk = file_data[bin_ptr*4 : (bin_ptr+1)*4]
                ival = struct.unpack('<i', chunk)[0]; fval = struct.unpack('<f', chunk)[0]
                if cur_name in file_packing:
                    num_to_pack = file_packing[cur_name]
                    p_vars = var_names[name_ptr:name_ptr+num_to_pack]
                    f.write(f"0.0 //HEX 0x{chunk.hex()}, contains {', '.join(p_vars)}, NULL\n")
                    name_ptr += num_to_pack; bin_ptr += 1
                else:
                    if ival == 0: val_str = "0"
                    elif abs(ival) < 100000 and abs(fval) % 1.0 < 0.00001: val_str = str(ival)
                    elif 0.0001 < abs(fval) < 1000000:
                        val_str = f"{fval:.6f}".rstrip('0')
                        if val_str.endswith('.'): val_str += '0'
                    else: val_str = str(ival)
                    f.write(f"{val_str} //{cur_name}\n")
                    bin_ptr += 1; name_ptr += 1
            else:
                chunk = file_data[bin_ptr*4 : (bin_ptr+1)*4]
                ival = struct.unpack('<i', chunk)[0]; fval = struct.unpack('<f', chunk)[0]
                if abs(ival) < 100000 and (fval == 0.0 or ival != 0): val_str = str(ival)
                else:
                    val_str = f"{fval:.6f}".rstrip('0')
                    if val_str.endswith('.'): val_str += '0'
                f.write(f"{val_str} //UNKNOWN_{bin_ptr}\n")
                bin_ptr += 1

def repack_bin(bin_path, input_dir):
    if not os.path.exists(bin_path): return
    names, original_data, count, num_vals = get_names_from_bin(bin_path)
    vals = list(struct.unpack('<' + 'I' * num_vals, original_data[4 : 4 + num_vals * 4]))
    data_start_offset = vals[1]
    new_data_sections = []
    new_lengths = []
    print(f"Repacking {bin_path}...")
    for name in names:
        txt_path = os.path.join(input_dir, name + ".txt")
        if not os.path.exists(txt_path):
            new_data_sections.append(b""); new_lengths.append(0); continue
        file_bytes = b""
        with open(txt_path, 'r') as tf:
            for line in tf:
                if "//" in line:
                    comment = line.split("//")[-1].strip()
                    if "HEX 0x" in comment:
                        hex_val = comment.split("HEX 0x")[-1].split(",")[0].strip()
                        file_bytes += bytes.fromhex(hex_val)
                    elif "--- SHADOW ARRAY" in line: continue
                    else:
                        val_part = line.split("//")[0].strip()
                        if val_part:
                            if "." in val_part: file_bytes += struct.pack('<f', float(val_part))
                            else:
                                try: file_bytes += struct.pack('<i', int(val_part))
                                except: file_bytes += struct.pack('<f', float(val_part))
        new_data_sections.append(file_bytes); new_lengths.append(len(file_bytes))
    current_offset = data_start_offset
    for i in range(count):
        vals[2 + i*3] = new_lengths[i]
        if i < count - 1: current_offset += new_lengths[i]; vals[4 + i*3] = current_offset
    final_bin = struct.pack('<I', count) + struct.pack('<' + 'I' * num_vals, *vals) + original_data[4+num_vals*4:data_start_offset] + b"".join(new_data_sections)
    with open(bin_path, 'wb') as f: f.write(final_bin)

def main():
    import sys
    if len(sys.argv) < 2: return
    mode = sys.argv[1].lower()
    
    # Try to find EXE in current or parent directory
    exe_path = 'PES2015.exe'
    if not os.path.exists(exe_path):
        exe_path = '../PES2015.exe'

    if mode == "unpack":
        blocks, b_idx, a_idx, t_idx = extract_blocks_from_exe(exe_path)
        if not blocks:
            print(f"Error: {exe_path} not found.")
            return
        print(f"Indices: Match={b_idx}, Player={a_idx}, Team={t_idx}")
        unpack_bin('bins/common/match/constant/constant_match.bin', blocks, 'match', b_idx)
        unpack_bin('bins/common/match/constant/constant_player.bin', blocks, 'player', a_idx)
        unpack_bin('bins/common/match/constant/constant_team.bin', blocks, 'team', t_idx)
    elif mode == "pack":
        repack_bin('bins/common/match/constant/constant_match.bin', 'data/match/output')
        repack_bin('bins/common/match/constant/constant_player.bin', 'data/player/output')
        repack_bin('bins/common/match/constant/constant_team.bin', 'data/team/output')

if __name__ == "__main__": main()
