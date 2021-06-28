# -*- mode: python -*-

block_cipher = None


a = Analysis(['21_환율계산기.py'],
             pathex=['/Users/admin/PycharmProjects/Online_Basic_Course'],
             binaries=None,
             datas=None,
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
          name='21_환율계산기',
          debug=False,
          strip=False,
          upx=True,
          console=False )
app = BUNDLE(exe,
             name='21_환율계산기.app',
             icon=None,
             bundle_identifier=None)
