pyinstaller --onefile your_script.py



#Warning

IF you see the cmd in exe file use this trick :

Find the exe line in the spec file, it will look something like this:

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='your_script',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )


Change console=False to console=True

Then

pyinstaller your_script.spec


Now Send the exe file in dist folder to the target 
