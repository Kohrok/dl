conf = {
    'xtype': 'melee', 

    'x1.dmg': 75 / 100.0,
    'x1.sp': 144,
    'x1.startup': 12 / 60.0,
    'x1.recovery': 22 / 60.0,
    'x1.hit': 1,

    'x2.dmg': 38*2 / 100.0,
    'x2.sp': 144,
    'x2.startup': 0,
    'x2.recovery': 41 / 60.0,
    'x2.hit': 2,

    'x3.dmg': 54*2 / 100.0,
    'x3.sp': 264,
    'x3.startup': 0 / 60.0,
    'x3.recovery': 25 / 60.0,
    'x3.hit': 2,

    'x4.dmg': 119 / 100.0,
    'x4.sp': 288,
    'x4.startup': 0,
    'x4.recovery': 36 / 60.0,
    'x4.hit': 1,

    'x5.dmg': 119 / 100.0,
    'x5.sp': 288,
    'x5.startup': 0,
    'x5.recovery': 40 / 60.0,
    'x5.hit': 1,

    'fs.dmg': 47*3 / 100.0,
    'fs.sp': 288,
    'fs.startup': 38 / 60.0,
    'fs.recovery': 14 / 60.0,
    'fs.hit': 3,

    'x1fs.startup': 50 / 60.0, # 12 delay + 38
    # 'x2fs.startup': 52 / 60.0,
    # 'x3fs.startup': 56 / 60.0,
    # 'x4fs.startup': 54 / 60.0,
    # 'x5fs.startup': 64 / 60.0,

    'dodge.startup': 36 / 60.0,
    'dodge.recovery': 0 / 60.0,
}

lv2 = {
    'x1.dmg': 90 / 100.0,
    'x2.dmg': 45.6*2 / 100.0,
    'x3.dmg': 64.8*2 / 100.0,
    'x4.dmg': 142.8 / 100.0,
    'x5.dmg': 142.8 / 100.0,
}

# Dagger FS Framedata - MsNyara
# Roll: 36
# FS: 8 (Charge) + 8 (FS1) + 8 (FS2) + 14 (FS3) + 14 (Recovery)

# C1FS: 12 (C1) + 12 (FS Delay) + FS
# C2AFS: 12 (C1) + 14 (C2A) + 2 (FS Delay) + FS
# C2BFS: 12 (C1) + 14 (C2A) + 8 (C2B) + FS
# Roll FS: Roll + FS, no interactions.

# I suspect C3FS and onwad have no FS delay.