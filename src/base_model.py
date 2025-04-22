from tensorflow.python.keras.models import Model
from tensorflow.keras.layers import Input, Embedding, Flatten, Dense, Activation, BatchNormalization
from utils.common_functions import read_yaml
from src.logger import get_logger
from tensorflow.python.keras.optimizers import Adam
from src.custom_exception import CustomException
import os
import yaml



logger = get_logger(__name__)

class BaseModel:
    def __init__(self,config_path):
        try:
            self.config = read_yaml(config_path)
            logger.info("Loaded configuration from config.yaml")
        except Exception as e:
            raise CustomException("Error loading configuration",e)
    
    def RecommenderNet(n_users, n_anime):
        try:
            # Try to load config or use default values
            embedding_size = 50
            try:
                # Load config file if exists
                config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'model_config.yaml')
                if os.path.exists(config_path):
                    with open(config_path, 'r') as file:
                        config = yaml.safe_load(file)
                    embedding_size = config.get("model", {}).get("embedding_size", 50)
            except Exception:
                # Continue with default if config loading fails
                pass
            
            # Define inputs
            user_input = Input(shape=(1,), name='user_input')
            anime_input = Input(shape=(1,), name='anime_input')
            
            # User embedding
            user_embedding = Embedding(input_dim=n_users, output_dim=embedding_size, name='user_embedding')(user_input)
            user_vector = Flatten(name='flatten_user')(user_embedding)
            
            # Anime embedding
            anime_embedding = Embedding(input_dim=n_anime, output_dim=embedding_size, name='anime_embedding')(anime_input)
            anime_vector = Flatten(name='flatten_anime')(anime_embedding)
            
            # Concatenate vectors
            concat = tf.keras.layers.Concatenate()([user_vector, anime_vector])
            
            # Dense layers
            dense1 = Dense(128, activation='relu')(concat)
            bn1 = BatchNormalization()(dense1)
            dense2 = Dense(64, activation='relu')(bn1)
            bn2 = BatchNormalization()(dense2)
            output = Dense(1, activation='sigmoid')(bn2)
            
            # Create model
            model = Model(inputs=[user_input, anime_input], outputs=output)
            
            # Compile model
            model.compile(
                loss='binary_crossentropy',
                optimizer=Adam(learning_rate=0.001),
                metrics=['accuracy']
            )
            
            return model
            
        except Exception as e:
            raise CustomException("Failed to create model", e)