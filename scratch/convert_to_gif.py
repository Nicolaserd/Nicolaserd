from moviepy import VideoFileClip

def process_gif():
    input_path = "assets/powerbi/Golden_spirals_faded.mp4"
    output_path = "assets/powerbi/Golden_spirals_faded.gif"
    
    print(f"Loading {input_path}")
    clip = VideoFileClip(input_path)
    
    # Resize to width 800 which is perfect for GitHub READMEs 
    print("Resizing video to 800px width...")
    clip_resized = clip.resized(width=800)
    
    print("Exporting as GIF. This may take a moment...")
    clip_resized.write_gif(output_path, fps=12)
    print("Done!")

if __name__ == "__main__":
    process_gif()
