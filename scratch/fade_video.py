import os
import numpy as np
from moviepy import VideoFileClip, ImageClip, CompositeVideoClip
from PIL import Image

def process_video():
    input_path = r"assets/powerbi/Golden_spirals_on_202604192119.mp4"
    output_path = r"assets/powerbi/Golden_spirals_faded.mp4"
    
    print(f"Loading video from {input_path}...")
    video = VideoFileClip(input_path)
    w, h = video.size
    print(f"Video size: {w}x{h}")
    
    fade_height = int(h * 0.25) # Fade the bottom 25%
    
    print("Generating gradient overlay...")
    gradient = np.zeros((h, w, 4), dtype=np.uint8)
    
    for y in range(h):
        if y < h - fade_height:
            alpha = 0
        else:
            progress = (y - (h - fade_height)) / fade_height
            alpha = int(255 * progress)
        
        gradient[y, :, 0] = 19
        gradient[y, :, 1] = 19
        gradient[y, :, 2] = 19
        gradient[y, :, 3] = alpha
        
    img = Image.fromarray(gradient, 'RGBA')
    overlay_path = "scratch/overlay.png"
    img.save(overlay_path)
    print("Saved overlay.")
    
    print("Compositing video...")
    overlay = ImageClip(np.array(img)).with_duration(video.duration)
    final_video = CompositeVideoClip([video, overlay])
    
    print("Writing output video...")
    final_video.write_videofile(output_path, codec="libx264", audio=False)
    print("Completed!")

if __name__ == "__main__":
    process_video()
