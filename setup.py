import cx_Freeze

executables=[cx_Freeze.Executable("main.py")]
cx_Freeze.setup(
    name='A bit Racey',
    options={'build_exe': {'packages':['pygame'],
                           'include_files':['car.png','Crash.wav','icon.png','Jazz_In_Paris.wav']}},
    executables=executables
    )
