

import subprocess

def run_script(script_name):
    result = subprocess.run(["python3", script_name], capture_output=True, text=True)
    print(result)
    print(f"Running {script_name}")
    print("Output:")
    print(result.stdout)
    if result.stderr:
        print("Errors:")
        print(result.stderr)

if __name__ == "__main__":
    scripts = ["1ObtencionEquiposLiga.py", "2ObtencionPlantillasEquipos.py", "3ObtencionPartidos.py","4ObtencionDatosJugadoresPartido.py","5ObtencionDatosPartidoJugado.py","6ObtencionIndicadoresEquiposHistorico.py","7PreparacionModelo.py"]

    for script in scripts:
        run_script(script)
