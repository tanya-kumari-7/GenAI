import time
from google import genai
from google.genai import types

# Initialize client with API key
client = genai.Client(api_key="YOUR_API_KEY")

prompt = """A close up of two people staring at a cryptic drawing on a wall, torchlight flickering.
A man murmurs, 'This must be it. That's the secret code.' The woman looks at him and whispering excitedly, 'What did you find?'"""

# Request video generation
operation = client.models.generate_videos(
    model="veo-3.0-generate-preview",
    prompt=prompt,
)

# Poll until the video is ready
while not operation.done:
    print("Waiting for video generation to complete...")
    time.sleep(10)
    operation = client.operations.get(name=operation.name)

# Get generated video
generated_video = operation.response.generated_videos[0]

# Download the video file
file = client.files.download(name=generated_video.video.uri)

with open("dialogue_example.mp4", "wb") as f:
    f.write(file)

print("✅ Generated video saved to dialogue_example.mp4")

####################
