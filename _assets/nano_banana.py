"""
Nano Banana: Simple image generation script
Similar to Google Gemini multimodal generation
"""

from google import genai
from google.genai import types
from PIL import Image

GOOGLE_API_KEY = "AIzaSyAFROK2tVDFBlsRHZQA1A9BbDhKdblN27o"

# Define the prompt
prompt = "A WIDE HORIZONTAL 16:9 fight poster of these people i provided one in one side and the other on the opposite side, they are magic rivals each with their own unique magical abilities, the blue monkey use ice magic and the white human use fire magic, only V.S text, they are in a fight pose face to face, in a fantasy art style. LANDSCAPE ORIENTATION, WIDE FORMAT."

# Initialize the client
client = genai.Client(api_key=GOOGLE_API_KEY)

# Generate content with images
response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents=[
        prompt,
        Image.open('b-Jacobo.png'),
        Image.open('b-cornelius.png'),
    ],
    config=types.GenerateContentConfig(
        response_modalities=['TEXT', 'IMAGE'],
    )
)

# Process the response
for part in response.parts:
    if part.text is not None:
        print(part.text)
    elif image := part.as_image():
        image.save("magic_rivals_poster.png")
        print("Image saved as magic_rivals_poster.png")