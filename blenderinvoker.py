import subprocess

blenderPath = r"C:\Program Files\Blender Foundation\Blender 2.92\blender.exe"
projectPath = r"C:\Users\39347\Documents\GitHub\3D-Human-Body-Generator\humanproject.blend"
scriptPath = r"C:\Users\39347\Documents\GitHub\3D-Human-Body-Generator\bodyEditor.py"


def run_blender(blenderPath, projectPath, scriptPath):
    subprocess.run([blenderPath,
                    projectPath,
                    '--background',
                    '--python', scriptPath,
                    '--', '0.57', '0.76', '0.59', '0.36', '0.95', '0.28', '0.25', '0.86', '1.55'])
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