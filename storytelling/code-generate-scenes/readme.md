# Visual Storyboard Generator

![DALL-E Generated Example](scene_01.png)  
*Example output from DALL-E 3 (PNG format)*

A CLI tool to automate visual storytelling using OpenAI's DALL-E. Converts text prompts into sequenced PNG images for product narratives, user journeys, and agile storyboarding.

## Features

- **Batch Processing**: Generate multiple images from a text file (1 prompt/line)
- **Filename Safety**: Outputs follow `[input_prefix]_scene_[num].png` pattern
- **Dynamic Scaling**: Handles any number of scenes (5? 50? 500? Your choice)
- **Error Resilience**: Continues past failed generations with clear warnings
- **Style Control**: Maintain visual consistency through prompt engineering

## Quick Start

### Installation
```bash
pip install openai requests
export DeanOpenAITest="your-api-key"  # Add to ~/.zshrc/bashrc
```

### Usage
```bash
# Default (uses scene.txt)
python generate_scenes.py

# Custom input file
python generate_scenes.py my_project_scenes.txt

# Example output files:
# my_project_scene_01.png, my_project_scene_02.png...
```

### Customization
1. **Image Sizes**: Modify `image_size` in script (supports DALL-E 3 resolutions)
2. **Model Switching**: Change `model` to `dall-e-2` for lower costs
3. **SVG Conversion**: Add post-processing step with ImageMagick/Inkscape

## Input File Structure
Create a text file with prompts like:
```text
minimal B&W icon, overwhelmed project manager...
minimal B&W icon, frustrated project manager...
--SNIP--
minimal B&W icon, cheerful project manager trains new hire...
```

## Version History
- **v1.0**: Initial release (CLI input, dynamic naming, error handling)

## Contributing
PRs welcome for:
- Rate limit handling
- SVG pipeline integration
- Alternative AI backends

---

*Requires OpenAI API access with DALL-E permissions. Not affiliated with OpenAI.*
