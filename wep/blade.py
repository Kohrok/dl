conf = {
    'xtype': 'melee',

    'x1.dmg': 97 / 100.0,
    'x1.sp': 130,
    'x1.startup': 10 / 60.0,
    'x1.recovery': 23 / 60.0,
    'x1.hit': 1,

    'x2.dmg': 97 / 100.0,
    'x2.sp': 130,
    'x2.startup': 0,
    'x2.recovery': 41 / 60.0,
    'x2.hit': 1,

    'x3.dmg': 63*2 / 100.0,
    'x3.sp': 220,
    'x3.startup': 6 / 60.0,
    'x3.recovery': 37 / 60.0,
    'x3.hit': 2,

    'x4.dmg': 129 / 100.0,
    'x4.sp': 360,
    'x4.startup': 0,
    'x4.recovery': 65 / 60.0,
    'x4.hit': 1,

    'x5.dmg': 194 / 100.0,
    'x5.sp': 660,
    'x5.startup': 0,
    'x5.recovery': 33 / 60.0,
    # 'x5.recovery': 62 / 60.0,
    'x5.hit': 1,

    'fs.dmg': 92 / 100.0,
    'fs.sp': 200,
    'fs.startup': 17 / 60.0,
    'fs.recovery': 42 / 60.0,
    'fs.hit': 1,

    'x1fs.startup': 31 / 60.0, # 14 delay + 17
    'x2fs.startup': 19 / 60.0, # 2 delay + 17

    'fsf.startup': 0,
    'fsf.recovery': 33 / 60,

    'dodge.startup': 36 / 60.0,
    'dodge.recovery': 0 / 60.0,
}

lv2 = {
    'x1.dmg': 106.7 / 100,
    'x2.dmg': 106.7 / 100,
    'x3.dmg': 69.3*2/ 100,
    'x4.dmg': 141.9 / 100,
    'x5.dmg': 213.4 / 100
}

# Blade FS Framedata - MsNyara
# Roll: 36
# FS: 9 (Charge) + 8 (Hit) + 42 (Recovery)

# C1FS: 10 (Hit) + 14 (FS Delay) + FS
# C2FS: 10 (Hit 1) + 23 (Hit 2) + 2 (FS Delay) + FS
# Roll FS: Roll... +... FS, again, no delay or interactions.

# Again suspected C3FS and onward have no FS delay, again C2FS might have or not FS delay, but that is the best I achieved (thrice).

# Extra since it was in the footage:
# 10 (C1) +23 (C2) + 42 (C3A) + 5 (C3B) + 38 (C4)