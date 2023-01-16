ALGORITHM = "brain_age"

ERROR = "error"
WARNING = "warning"

# Data sources
DB_POSTGRES = "POSTGRES"
DB_CSV = "CSV"

DB_USER = 'DB_USER'
DB_PASSWORD = 'DB_PASSWORD'
DB_HOST = 'DB_HOST'
DB_PORT = 'DB_PORT'
DB_DATABASE = 'DB_DATABASE'
DB_CNN_DATABASE = 'DB_CNN_DATABASE'

TASK_TABLE = "TASK"

XNAT_URL = "XNAT_URL"
XNAT_USER = "XNAT_USER"
XNAT_PASSWORD = "XNAT_PASSWORD"
XNAT_PROJECT = "XNAT_PROJECT"

ID = "id"
SEX = "sex"
AGE = "age"
CLINICAL_ID = "clinical_id"
IMAGING_ID = "imaging_id"
IS_TRAINING_DATA = "is_training_data"

# Path
DATA_FOLDER = "DATA_FOLDER"
IMAGES_FOLDER = "IMAGES_FOLDER"
MODEL_FOLDER = "MODEL_FOLDER"

IMAGE_SUFFIX = "IMAGE_SUFFIX"
DEFAULT_IMAGE_NAME = "_aseg_GM_to_template_GM_mod.nii.gz"

TASK = "TASK"
CHECK = "check"
TRAIN = "train"
VALIDATION = "validation"
TEST = "test"
PREDICT = "predict"
PREDICTIONS = "predictions"
MODEL_ID = "MODEL_ID"
SAVE_MODEL = "SAVE_MODEL"
ORGANIZATION_ID = "ORGANIZATION_ID"
RESULT = "RESULT"
METRICS = "METRICS"

# CNN options
PADDING_SAME="same"
RELU = "relu"

INPUT_SHAPE = "INPUT_SHAPE"
USE_MASK = "USE_MASK"
MASK_FILENAME = "MASK_FILENAME"
MODEL = "MODEL"
MODEL_SELECTION = "MODEL_SELECTION"

TRAINING_IDS = "TRAINING_IDS"
VALIDATION_IDS = "VALIDATION_IDS"
TESTING_IDS = "TESTING_IDS"
DATASET = "DATASET"

SEED = "seed"
DATA_SEED = "data_seed"
DATA_SPLIT = "data_split"
DEFAULT_SPLIT = 0.8

# Hyperparameters - Master
ROUNDS = "ROUNDS"
ROUND = "ROUND"
MASTER = "MASTER"
NODE = "NODE"

# Hyperparameteres
LEARNING_RATE = "LEARNING_RATE"
BETA1 = "BETA1"
BETA2 = "BETA2"
EPSILON = "EPSILON"
DECAY = "DECAY"
USE_PADDING = "USE_PADDING"
CROP_INDEXES = "CROP_INDEXES"
AUGMENT_TRAIN = "AUGMENT_TRAIN"
IMG_SCALE = "IMG_SCALE"
BATCH_SIZE = "BATCH_SIZE"
PATIENTS_PER_EPOCH = "PATIENTS_PER_EPOCH"
EPOCHS = "EPOCHS"
DROPOUT = "DROPOUT"
STARTING_STEP = "STARTING_STEP"
DECAY_STEPS = "DECAY_STEPS"
EARLY_STOPPING = "EARLY_STOPPING"

# Other configurations
GPU_COUNT = "GPU_COUNT"
DB_TYPE = "DB_TYPE"
MAX_NUMBER_TRIES = "MAX_NUMBER_TRIES"
SLEEP_TIME = "SLEEP_TIME"
RETURN_WEIGTHS="RETURN_WEIGTHS"
DEFAULT_MAX_NUMBER_TRIES = 100
DEFAULT_SLEEP_TIME = 120

# Outcome
SAMPLE_SIZE = "SAMPLE_SIZE"
WEIGHTS = "weights"
MAE = "mae"
MSE = "mse"
VAL_MAE = "val_mae"
VAL_MSE = "val_mse"
LOSS = "loss"
HISTORY = "HISTORY"
GLOBAL = "global"

NUMBER_SCANS = "NUMBER_SCANS"
MISSING_SCANS = "MISSING_SCANS"
MESSAGE = "MESSAGE"

# POSTGRES
MODELS_TABLE = "models"
RUNS_TABLE = "runs"
WEIGHTS_TABLE = "weights"
