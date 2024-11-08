import json
import boto3
import base64
import random
from fastapi import HTTPException
from io import BytesIO
from PIL import Image

class StabilityAIClient:
    def __init__(self, region_name="us-east-1"):
        #self.api_key = api_key
        self.region_name = region_name
        self.client = boto3.client('bedrock-runtime', region_name=self.region_name)

    def generate_image(self, prompt: str) -> BytesIO:
        try:
            # Define the payload for the model
            payload = {
               "text_prompts": [{"text": prompt}],
                "style_preset": "photographic",
                "seed": random.randint(0, 4294967295),
                "cfg_scale": 10,
                "steps": 30,       # Customize as needed
            }

            # Invoke the endpoint
            response = self.client.invoke_model( 
                modelId = 'stability.stable-diffusion-xl-v1', # Replace with your endpoint name
                contentType='application/json',
                body=json.dumps(payload)
            )

            # Check the response status
            if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                model_response = json.loads(response["body"].read())
                # Extract the image data.
                base64_image_data = model_response["artifacts"][0]["base64"]
                image_data = base64.b64decode(base64_image_data)
                return self.convert_to_image_stream(image_data)
            else:
                raise HTTPException(status_code=500, detail="Failed to generate image")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error occurred: {e}")

    def convert_to_image_stream(self, image_data: bytes) -> BytesIO:
        try:
            # Convert the byte data into an image
            image = Image.open(BytesIO(image_data))
            # Create a byte stream for FastAPI response
            img_stream = BytesIO()
            image.save(img_stream,format="PNG")
            img_stream.seek(0)
            return img_stream
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error processing image: {e}")