# Prediction interface for Cog ⚙️
# https://github.com/replicate/cog/blob/main/docs/python.md

from cog import BasePredictor, Input, Path


class Predictor(BasePredictor):
    def setup(self):
        """Load the model into memory to make running multiple predictions efficient"""
        # self.model = torch.load("./weights.pth")

    def predict(
        self,
        audio_query: str = Input(description="Files to be searched for Expected S3://bucket/path/to/folder/"),
        audio_search: str = Input(description="Path to audio file to be searched for Expected S3://bucket/path/to/file.wav"),
        conversation: str = Input(description="Files with conversation Expected S3://bucket/path/to/folder/conversation.jsonl"),
    ) -> str:
        """
        Run a single prediction on the model
        """
        
        return "s3://bucket/path/to/folder/speaker_aware_conversation.jsonl"