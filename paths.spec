# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['paths', 'd:\\Python Projects\\cherepashka-i-drova\\venv\\Lib\\site-packages" cherepashka-i-drova.py '],
             pathex=['d:\\Python Projects\\cherepashka-i-drova'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='paths',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='turtle.ico')
