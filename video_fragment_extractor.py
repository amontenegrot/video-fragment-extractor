import os, time, math

import chime

from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


def clear_terminal():
    if os.name == 'posix':
        os.system('clear')  # Unix/Linux/MacOS/BSD
    elif os.name == 'ce' or os.name == 'nt' or os.name == 'dos':
        os.system('cls')  # DOS/Windows

def status_parameters(video:str, status_duration:int):
    clip = VideoFileClip(video)
    duration = math.ceil(clip.duration)
    number_status = math.ceil(duration/status_duration)

    return number_status

def output_name(file_name:str):
    extension = file_name.split('.')[1]
    if extension != 'mp4': print('Verifique que el formato sea .mp4')

    full_name = file_name.split('.')[0]
    full_name = full_name.split(' ')

    concat_name = ''

    for word in full_name:
        word.capitalize()
        concat_name = concat_name + word
    
    return concat_name, extension


video = 'video.mp4'  # Video file in the same folder as the script
final_name, extension = output_name(video)
counter = 1
start = 0
end = 30
number_status = status_parameters(video, end)

while counter <= number_status:
    print(f'Fragmento {counter}; faltando {number_status-counter} fragmentos.')
    ffmpeg_extract_subclip(
        video, start, end, 
        targetname=f'{str(counter).zfill(2)} {final_name}.{extension}'
        )
    start += 30
    end += 30
    counter += 1
    time.sleep(5)
    clear_terminal()

chime.success()
print('Proceso de corte de videos terminado con éxito.')
