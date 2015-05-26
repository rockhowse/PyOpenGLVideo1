import cx_Freeze

executables = [cx_Freeze.Executable("16_GD_Py3_PyGame~ButtonEvents.py")]

cx_Freeze.setup(
    name="A bit Raceye",
    options={
        "build_exe": {"packages": ["pygame"],
                      "include_files": ["racecar.png"]
                      }
    },
    executables=executables
)
