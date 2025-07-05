from pathlib import Path

def listar_directorio(base_dir, prefijo=""):
    for path in sorted(base_dir.iterdir()):
        if path.name.startswith("__pycache__"):
            continue
        print(f"{prefijo}├── {path.name}")
        if path.is_dir():
            listar_directorio(path, prefijo + "│   ")

# Cambia aquí si tu raíz no es 'mlops_equipo1'
raiz = Path("mlops_equipo1")

if raiz.exists():
    print(f"{raiz}/")
    listar_directorio(raiz)
else:
    print("❌ No se encontró la carpeta 'mlops_equipo1'. ¿Estás en el directorio correcto?")
