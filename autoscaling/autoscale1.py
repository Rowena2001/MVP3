# File name: cpu_deployment.py
# This file deploys a translator application and a driver that calls it.
# The translator application uses a pre-trained model from the transformers library.
# It specifies that the deployment should use 0.2 CPU cores.

from starlette.requests import Request

from ray import serve

from transformers import pipeline

# Creates a Ray Serve deployment for a translator application.
# It specifies that the deployment should use 0.2 CPU cores.
# Refer to https://docs.ray.io/en/latest/serve/scaling-and-resource-allocation.html# for more information.
@serve.deployment(
    autoscaling_config={
        "min_replicas": 1,
        "initial_replicas": 2,
        "max_replicas": 10,
        "target_num_ongoing_requests_per_replica": 8,
        "upscale_delay_s": 5,
        "smoothing_factor": 1.5
    }
)
class Translator:
    def __init__(self):
        # Load model
        self.model = pipeline("translation_en_to_fr", model="t5-small")

    def translate(self, text: str) -> str:
        # Run inference
        model_output = self.model(text)

        # Post-process output to return only the translation text
        translation = model_output[0]["translation_text"]

        return translation

    # Asynchronously calls the translate function.
    async def __call__(self, http_request: Request) -> str:
        english_text: str = await http_request.json()
        translation = self.translate(english_text)
        return translation

# Binds the translator application and the driver to the same deployment.
translator_app = Translator.bind()