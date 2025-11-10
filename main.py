import os
import subprocess


def run_streamlit_app():
    """
    Ejecuta la aplicación de streamilit
    como un subproceso.
    """
    # Obtener la ruta absoluta del directorio donde está el script.
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Contruimos la ruta completa al archivo app.py
    app_path = os.path.join(script_dir, "app.py")

    # Definimos el comando que queremos ejecutar.
    command = ["streamlit", "run", app_path]

    print("Lanzando la aplicación")

    try:
        # Ejecutamos el comando. El scipt esperará hasta que Streamlit termine
        subprocess.run(command, check=True)

    except FileNotFoundError:
        print("\n El comando 'streamlit' no se encontró")

    except subprocess.CalledProcessError as e:
        print(f"Ocurrió un erro al ejecutarse la aplicación de Streamlit: {e}")

    except KeyboardInterrupt:
        print("\nAplicación detenida por el usuario")


if __name__ == "__main__":
    run_streamlit_app()
