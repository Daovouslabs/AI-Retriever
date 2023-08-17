import os
from sentence_transformers import SentenceTransformer, util
import logging

logger = logging.getLogger(__name__)

class Models:
	embedder = None
	dim = 768

	@classmethod
	def load(cls):
		model_path = os.environ.get("EMBEDDING_MODEL_PATH")
		if model_path:
			# load model
			logger.info(f"Load embedding model from {model_path}")
			cls.embedder = SentenceTransformer(model_path)
