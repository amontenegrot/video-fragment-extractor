import os, time, math

from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


def clear_terminal(text:str=''):
    dos_windows = ['ce', 'nt', 'dos']
    if os.name == 'posix':
        os.system('clear')  # Unix/Linux/MacOS/BSD
        print(text)
    elif os.name in dos_windows:
        os.system('cls')  # DOS/Windows
        print(text)

def whatsapp_parameters(video:str, status_duration:int):
    clip = VideoFileClip(video)
    duration = math.ceil(clip.duration)
    number_status = math.ceil(duration/status_duration)

    return number_status

def output_name(file_name:str):
    extension = file_name.split('.')[1]
    valid_extensions = ['mp4', 'MP4']
    if extension not in valid_extensions: print('Verifique que la extensión sea mp4.')

    name = file_name.split('.')[0]
    name = name.capitalize()
    
    return name, extension

def video_cutter(input_folder:str, video:str, output_folder:str):
    video_path = f'{input_folder}/{video}'
    video_name, file_extension = output_name(video)
    counter, start, end = 1, 0, 29
    number_status = whatsapp_parameters(video_path, end)
    new_folder = video.split('.')[0]
    output_folder = f'{output_folder}/{new_folder.capitalize()}'
    os.makedirs(output_folder, exist_ok=True)  # Create folder

    while counter <= number_status:
        print(f'Fragmento {counter}; faltando {number_status-counter} fragmentos.')        
        ffmpeg_extract_subclip(
            video_path, start, end, 
            targetname=f'{output_folder}/{str(counter).zfill(2)} {video_name}.{file_extension}'
            )
        start += 29
        end += 29
        counter += 1
        time.sleep(1)


# Variables and constants of execution
clear_terminal('Inicializando, por favor espere.')
PATH = os.path.abspath(os.getcwd()) + '/'
PATH = PATH.replace('\\', '/')

input_folder = PATH + 'videos'
output_folder = PATH + 'salidas'
list_videos = []

# Extract name files
clear_terminal('Obteniendo listado de videos a procesar.')

content = os.listdir(input_folder)

for file in content:
    if os.path.isfile(os.path.join(input_folder, file)) and file.endswith('.mp4'):
        list_videos.append(file)

# Extract videoclips
for file in list_videos:
    clear_terminal('Realizando el proceso de corte.')
    print(f'\tProceso de corte para {file} iniciado.')
    video_cutter(input_folder, file, output_folder)
    print(f'\tProceso de corte para {file} terminado con éxito.')

# End
clear_terminal('Proceso completado con éxito.')
print('\n')
os.system('pause')  # Press any key to continue
