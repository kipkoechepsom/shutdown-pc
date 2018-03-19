# -*- mode: python -*-

block_cipher = None


a = Analysis(['shut.py'],
             pathex=['C:\\Users\\kevo\\Desktop\\newwww py'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='shut',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='C:\\Users\\kevo\\Desktop\\newwww py\\label.ico')
