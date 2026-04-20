from moviepy import VideoFileClip

def process_gif():
    input_path = "assets/powerbi/Golden_spirals_faded.mp4"
    output_path = "assets/powerbi/Golden_spirals_faded.gif"
    
    print(f"Loading {input_path}")
    clip = VideoFileClip(input_path)
    
    print("Resizing video to 800px width...")
    clip_resized = clip.resized(width=800)
    
    print(f"Original resized height: {clip_resized.size[1]}. Cropping 30px from bottom...")
    # Cut 30px from the bottom
    clip_cropped = clip_resized.cropped(x1=0, y1=0, x2=clip_resized.size[0], y2=clip_resized.size[1]-30)
    
    print("Exporting as GIF. This may take a moment...")
    clip_cropped.write_gif(output_path, fps=12)
    print("Done!")

if __name__ == "__main__":
    process_gif()
