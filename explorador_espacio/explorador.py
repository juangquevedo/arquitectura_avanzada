import subprocess
import itertools
from mcpat_out import *
from separar_datos import *

def run_commd(MOREOPTIONS):
    # Definir el directorio base y rutas
    GEM5PATH = "~/mySimTools/gem5/build/ARM"
    SCRIPTDIR = "../scripts/CortexA76_scripts_gem5"

    # Definir los comandos
    commands = [
        f"{GEM5PATH}/gem5.fast -d h264_dec/m5out {SCRIPTDIR}/CortexA76.py --cmd=h264_dec/h264_dec --options='h264_dec/h264dec_testfile.264 h264_dec/h264dec_outfile.yuv' {MOREOPTIONS}",
        f"{GEM5PATH}/gem5.fast -d h264_enc/m5out {SCRIPTDIR}/CortexA76.py --cmd=h264_enc/h264_enc --options='h264_enc/h264enc_configfile.cfg' {MOREOPTIONS}",
        f"{GEM5PATH}/gem5.fast -d jpeg2k_dec/m5out {SCRIPTDIR}/CortexA76.py --cmd=jpeg2k_dec/jpg2k_dec --options='-i jpeg2k_dec/jpg2kdec_testfile.j2k -o jpeg2k_dec/jpg2kdec_outfile.bmp' {MOREOPTIONS}",
        f"{GEM5PATH}/gem5.fast -d jpeg2k_enc/m5out {SCRIPTDIR}/CortexA76.py --cmd=jpeg2k_enc/jpg2k_enc --options='-i jpeg2k_enc/jpg2kenc_testfile.bmp -o jpeg2k_enc/jpg2kenc_outfile.j2k' {MOREOPTIONS}",
        f"{GEM5PATH}/gem5.fast -d mp3_dec/m5out {SCRIPTDIR}/CortexA76.py --cmd=mp3_dec/mp3_dec --options='-w mp3_dec/mp3dec_outfile.wav mp3_dec/mp3dec_testfile.mp3' {MOREOPTIONS}",
        f"{GEM5PATH}/gem5.fast -d mp3_enc/m5out {SCRIPTDIR}/CortexA76.py --cmd=mp3_enc/mp3_enc --options='mp3_enc/mp3enc_testfile.wav mp3_enc/mp3enc_outfile.mp3' {MOREOPTIONS}"
    ]

    # Ejecutar todos los comandos en paralelo
    processes = [subprocess.Popen(command, shell=True) for command in commands]

    # Esperar a que todos los procesos terminen
    for process in processes:
        process.wait()

    print("Todos los procesos han terminado.")

params = {
    'l1i_size': ["32kB", "64kB", "128kB"],
    'l1d_size': ["32kB", "64kB", "128kB"],
    'issue_width': [4, 8, 12],
    'rob_entries': [64, 128, 256],
    'num_fu_intALU': [2, 4]
}

# MOREOPTIONS = "--num_fu_intALU=4 --num_fu_cmp=2 --l1i_size=128kB"

# Obtener las llaves (parámetros)
param_keys = list(params.keys())

# Generar todas las combinaciones de valores de los parámetros
combinations = itertools.product(*(params[key] for key in param_keys))

c=0

# Generar los strings de opciones
for combination in combinations:
    # Crear el string para cada combinación
    MOREOPTIONS = " ".join(f"--{key}={value}" for key, value in zip(param_keys, combination))
    run_commd(MOREOPTIONS)
    gen_mcpat()
    ext_dat(MOREOPTIONS)

