from pytube import YouTube
import os


def on_progress(stream, chunck, bytes_remaining):
    total_size = stream.filesize
    bytes_dowload = total_size - bytes_remaining

    percentage_of_complation = bytes_dowload / total_size * 100
    print(f"Descargando: {percentage_of_complation:.2f}% completado", end='\r')


def dowload_video(url, output_path):
    try:
        yt = YouTube(url, on_progress_callback=on_progress,
                     on_complete_callback=lambda stream, file_path: print(
                         f"Descarga completa: {file_path}"))

        # resolutions = yt.streams.all()
        resolutions = yt.streams.filter(
            progressive=True).order_by('resolution').desc()

        for i in range(len(resolutions)):
            print(f"{i+1} - {resolutions[i].resolution}")

        resolution = input("Elija una resolucion: ")
        resolution = resolutions[int(resolution) - 1].resolution

        yt.streams.filter(res=resolution).first().download(
            output_path=output_path)
    except Exception as e:
        print(f"No se pudo descargar el video: {str(e)}")


def main():
    url = input("Introduce la url del video a descargar: ")

    output_path = os.path.expanduser("~")

    ENG = "Dowloads"
    ESP = "Descargas"

    # Obtener la ruta del directorio del proyecto
    if not os.path.isdir(os.path.join(output_path, ENG)):
        output_path = os.path.join(output_path, ENG)
    else:
        output_path = os.path.join(output_path, ESP)

    dowload_video(url=url, output_path=output_path)


main()
