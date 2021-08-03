# ( 3 Minute Python shorts )
# Extract Audio from Video 

# Required Library : MoviePy
# pip install moviepy

import moviepy.editor as mp  

def extract_audio(video_path, savename):
	clip = mp.VideoFileClip(video_path)
	clip.audio.write_audiofile(savename)

video_path = 'My Soldiers Rage.mp4'
savename = 'extracted.wav'
extract_audio(video_path, savename)
print('Done')