# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:\\Users\\buyid\\AppData\\Local\\Temp\\.pyxel\\app2exe\\Create.py'],
    pathex=[],
    binaries=[],
    datas=[('..\\Create.pyxapp', '.')],
    hiddenimports=['math', 'os', 'pyxel', 'random'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Create',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
