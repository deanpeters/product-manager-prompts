"""
Visual Storyboard Bot v1.0

Transforms text prompts into DALL-E generated images. Designed for product storytellers
who want to automate visual narrative creation without manual design work.

Usage:
python story_gen.py [input_file.txt]  # Uses scene.txt if no file specified
"""

import openai
import os
import requests
import argparse

# Configuration - Customize these for your needs
openai.api_key = os.getenv("DeanOpenAITest")  # API key from environment variable
output_dir = "./"          # Output directory for generated images
image_size = "1024x1024"   # Supported sizes: 1024x1024, 1792x1024 (DALL-E 3)
model = "dall-e-3"         # Switch to "dall-e-2" for older model

def generate_images(input_file):
    # Generate filename prefix from input file
    base_name = os.path.basename(input_file)
    base_prefix = os.path.splitext(base_name)[0]  # Remove file extension
    
    # Read and clean input prompts
    with open(input_file, "r") as f:
        scenes = [line.strip() for line in f.readlines() if line.strip()]
    
    total_scenes = len(scenes)
    print(f"Loading {total_scenes} scenes from {input_file}...")
    
    # Main generation loop
    for i, prompt in enumerate(scenes, 1):  # Start counting at 1
        try:
            # Show progress with prompt preview
            print(f"\nScene {i}/{total_scenes}: {prompt[:50]}...")
            
            # Generate image via DALL-E API
            response = openai.images.generate(
                model=model,
                prompt=prompt,
                n=1,                    # Single image per prompt
                size=image_size,
                quality="standard"      # Use "hd" for enhanced quality
            )
            
            # Download and save image
            image_url = response.data[0].url
            image_data = requests.get(image_url).content
            
            filename = os.path.join(output_dir, f"{base_prefix}_scene_{i:02d}.png")
            with open(filename, "wb") as img_file:
                img_file.write(image_data)
            
            print(f"Saved: {filename}")

        except Exception as e:
            # Error handling with helpful message
            print(f"Error in scene {i}: {str(e)}")
            print("Tip: Check prompt guidelines if errors persist")

if __name__ == "__main__":
    # Configure command-line arguments
    parser = argparse.ArgumentParser(description='Generate visual storyboards from text')
    parser.add_argument('input_file', nargs='?', default='scene.txt',
                       help='Text file containing prompts (default: scene.txt)')
    args = parser.parse_args()
    
    # Start generation process
    generate_images(args.input_file)
    print("\nGeneration complete! Use your new assets wisely.")
