import subprocess

blenderPath = r"C:\Program Files\Blender Foundation\Blender 2.92\blender.exe"
projectPath = r"C:\Users\39347\Documents\GitHub\3D-Human-Body-Generator\humanproject.blend"
scriptPath = r"C:\Users\39347\Documents\GitHub\3D-Human-Body-Generator\bodyEditor.py"


def run_blender(blenderPath, projectPath, scriptPath):
    subprocess.run([blenderPath,
                    projectPath,
                    '--background',
                    '--python', scriptPath,
                    '--', '2', '1', '1', '1', '1', '1', '1', '1', '1'])
    #print(output.decode("utf-8"))

run_blender(blenderPath, projectPath, scriptPath)

head = input("Head size: ")
torso = input("Torso size: ")
hips = input("Hips size: ")
legs = input("Legs size: ")
calves = input("Calves size: ")
shoulders = input("Shoulders size: ")
arms = input("Arms size: ")
forearms = input("Forearms size: ")
height = input("Height: ")

print(height)