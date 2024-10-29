import pandas as pd
import os

def ext_dat(cambios):
    tareas = ["h264_dec","h264_enc","jpeg2k_dec","jpeg2k_enc","mp3_dec","mp3_enc"]
    p_save = "utiles.csv"
    
    lista_stats = []
    
    for n in tareas:
        path = n + "/m5out/stats.txt"
    
        with open(path) as file:
            contenido = file.readlines()
        
        contenido = contenido[2:-2]
        stats = {}
        
        for i in contenido:
            c = i.find("#")
            a = i[:c].split()
            stats[a[0]] = a[1:]
        
        p_mc = n + "/m5out/output.txt"
    
        with open(p_mc) as file:
            contenido = file.readlines()
    
        contenido = contenido[13:20]
    
        for i in contenido:
            a = i.split("=")
            a[0] = a[0][2:-1]
            a[1] = a[1][1:-1].split()[0]
            stats[a[0]] = [a[1]]
    
        utiles = {
            "system.cpu.cpi"    : stats["system.cpu.cpi"],
            "system.cpu.ipc"    : stats["system.cpu.ipc"],
            "system.cpu.statFuBusy::IntAlu"     : stats["system.cpu.statFuBusy::IntAlu"],
            "system.cpu.statFuBusy::IntMult"    : stats["system.cpu.statFuBusy::IntMult"] ,
            "system.cpu.statFuBusy::IntDiv"     : stats["system.cpu.statFuBusy::IntDiv"],
            "system.cpu.statIssuedInstType_0::IntAlu"   : stats["system.cpu.statIssuedInstType_0::IntAlu"],
            "system.cpu.statIssuedInstType_0::IntMult"  : stats["system.cpu.statIssuedInstType_0::IntMult"],
            "system.cpu.statIssuedInstType_0::IntDiv"   : stats["system.cpu.statIssuedInstType_0::IntDiv"],
            "system.cpu.branchPred.ras.used"        : stats["system.cpu.branchPred.ras.used"],
            "system.cpu.branchPred.ras.correct"     : stats["system.cpu.branchPred.ras.correct"],
            "system.cpu.branchPred.ras.incorrect"   : stats["system.cpu.branchPred.ras.incorrect"],
            "system.cpu.dcache.overallHits::total"   : stats["system.cpu.dcache.overallHits::total"],
            "system.cpu.dcache.overallMisses::total" : stats["system.cpu.dcache.overallMisses::total"],
            "system.cpu.dcache.overallMissLatency::total" : stats["system.cpu.dcache.overallMissLatency::total"],
            "system.cpu.dcache.overallAccesses::total" : stats["system.cpu.dcache.overallAccesses::total"],
            "system.cpu.dcache.overallMissRate::total" : stats["system.cpu.dcache.overallMissRate::total"],
            "system.cpu.icache.overallHits::total"   : stats["system.cpu.dcache.overallHits::total"],
            "system.cpu.icache.overallMisses::total" : stats["system.cpu.dcache.overallMisses::total"],
            "system.cpu.icache.overallMissLatency::total" : stats["system.cpu.dcache.overallMissLatency::total"],
            "system.cpu.icache.overallAccesses::total" : stats["system.cpu.dcache.overallAccesses::total"],
            "system.cpu.icache.overallMissRate::total" : stats["system.cpu.dcache.overallMissRate::total"],
            "Area"                  : stats["Area"],
            "Peak Power"            : stats["Peak Power"],
            "Total Leakage"         : stats["Total Leakage"],
            "Peak Dynamic"          : stats["Peak Dynamic"],
            "Subthreshold Leakage"  : stats["Subthreshold Leakage"],
            "Gate Leakage"          : stats["Gate Leakage"],
            "Runtime Dynamic"       : stats["Runtime Dynamic"]
            }
        lista_stats.append(utiles)
    
        
    data = [["stat"]+tareas+["promedio"],
            [cambios,"","","","","",""]] 
    
    for i in utiles.keys():
        temp = [i]
        suma = 0
        for j in lista_stats:
            suma += float(j[i][0])
            temp.append(j[i][0])
        temp.append(suma/6)
        data.append(temp)
    
    p_save = "utiles.xlsx"
    
    # Convertir los datos a un DataFrame
    df_nuevos = pd.DataFrame(data[1:], columns=data[0])
    
    # Si el archivo existe, leer el archivo Excel existente y combinarlo con los nuevos datos
    if os.path.exists(p_save):
        df_existente = pd.read_excel(p_save)
        df_combinado = pd.concat([df_existente, df_nuevos], ignore_index=True)
    else:
        df_combinado = df_nuevos
    
    # Guardar el DataFrame combinado en un archivo Excel
    df_combinado.to_excel(p_save, index=False)