import subprocess

blenderPath = r"C:\Program Files\Blender Foundation\Blender 2.92\blender.exe"
projectPath = r"..\blenderfiles\humanproject.blend"
scriptPath = r"bodyEditor.py"


def run_blender(blenderPath, projectPath, scriptPath, measures):
    subprocess.run([blenderPath,
                    projectPath,
                    '--background',
                    '--python', scriptPath,
                    '--', measures['head'], measures['torso'], measures['legs'], measures['calves'],
                    measures['shoulders'], measures['arms'], measures['forearms'], measures['hips'],
                    measures['height']])

def execute(measures):
    run_blender(blenderPath, projectPath, scriptPath, measures)

