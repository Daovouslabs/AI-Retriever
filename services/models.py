import os
import logging
logger = logging.getLogger(__name__)

class Models:
	embedder = None
	dim = 768

	@classmethod
	def load(cls):
		model_path = os.environ.get("EMBEDDING_MODEL_PATH")
		# load model
		logger.info(f"Load embedding model from {model_path} {os.listdir(model_path)}")
		if model_path:
			try:
				from sentence_transformers import SentenceTransformer, util
			except:
				raise ModuleNotFoundError("module sentence_transformers not found")
			cls.embedder = SentenceTransformer(model_path)
			return cls.embedder.get_sentence_embedding_dimension()
		else: 
			return 1536
