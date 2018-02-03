# -*- mode: python -*-

block_cipher = None


a = Analysis(['pdf_kindle_gui.py'],
             pathex=['/home/milton/bin/pythonscripts/pythonscripts/pdf_kindle_gui'],
             binaries=[],
             datas=[('icon.png', '.')],
             hiddenimports=["PyPDF2","Tkinter"],
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
          name='pdf_kindle_gui',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='icon.ico')
