import subprocess
import shutil

def gen_mcpat():
    tareas = ["h264_dec","h264_enc","jpeg2k_dec","jpeg2k_enc","mp3_dec","mp3_enc"]

    for task in tareas:
        # Definir el comando de bash que quieres ejecutar
        command_1 = f"python3 ../scripts/McPAT/gem5toMcPAT_cortexA76.py {task}/m5out/stats.txt {task}/m5out/config.json ../scripts/McPAT/ARM_A76_2.1GHz.xml"
        command_2 = f"~/mySimTools/mcpat/mcpat -infile {task}/m5out/config.xml"

        # Ejecutar el comando usando subprocess
        try:
            result = subprocess.run(command_1, shell=True, check=True, text=True, capture_output=True)
            shutil.move("config.xml",f"{task}/m5out/config.xml")

            result = subprocess.run(command_2, shell=True, check=True, text=True, capture_output=True)

            # Guardar la salida en un archivo de texto
            with open(f"{task}/m5out/output.txt", "w") as file:
                file.write("STDOUT:\n")
                file.write(result.stdout)  # Guardar la salida estándar
                file.write("\n\nSTDERR:\n")
                file.write(result.stderr)  # Guardar los errores si los hubo
            print(f"salida de mcpat guardado en {task}/m5out/output.txt")
        except subprocess.CalledProcessError as e:
            print(f"Error al ejecutar el comando: {e}")

