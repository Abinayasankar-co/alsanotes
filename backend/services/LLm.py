import boto3
import json
import datetime
from botocore.exceptions import ClientError

class LLMConfig:
    def __init__(self) -> None:
        self.client = boto3.client("bedrock-runtime", region_name="us-east-1")
        self.model_id = "amazon.titan-text-premier-v1:0"
        self.embed_model_id = "amazon.titan-embed-image-v1"

    def llm_request(self,prompt):
        prompt = prompt
        native_request = {
        "inputText": prompt,
        "textGenerationConfig": {
          "maxTokenCount": 2000,
          "temperature": 0.5,
          },
        }
        request = json.dumps(native_request)

        try:
            start_time = datetime.datetime.now()
            response = self.client.invoke_model_with_response_stream(
                    modelId=self.model_id, body=request, contentType= "application/json"
                )

            end_time = datetime.datetime.now()
            total_time = end_time - start_time

        except (ClientError, Exception) as e:
            print(f"ERROR: Can't invoke '{self.model_id}'. Reason: {e}")
            exit(1)

        final_result = " "
        for event in response["body"]:
                chunk = json.loads(event["chunk"]["bytes"])
                if "outputText" in chunk:
                       final_result += chunk["outputText"]

        return final_result , total_time
    
    def llm_embedding(self, text_description: str = None, image_base64: str = None):
        if not text_description and not image_base64:
            raise ValueError("At least one of 'image_base64' or 'text_description' must be provided.")
        input_data = {}
        if image_base64 is not None:
            input_data["inputImage"] = image_base64
        if text_description is not None:
            input_data["inputText"] = text_description        
        body = json.dumps(input_data)
        try:
            response = self.client.invoke_model(
                body=body,
                modelId=self.embed_model_id,
                accept="application/json",
                contentType="application/json"
            )
            
            response_body = json.loads(response.get("body").read())
            embedding = response_body.get("embedding")  
            if embedding is None:
                raise ValueError("No embedding found in the response.")       
            return embedding 
        except Exception as e:
            raise RuntimeError(f"Failed to generate embedding: {e}")

         

# Example Usage
def main():
    llmResponse = LLMConfig()
    response = llmResponse.llm_request(prompt="What's your name")
    print(response[0])

if __name__ == '__main__':
    main()
    