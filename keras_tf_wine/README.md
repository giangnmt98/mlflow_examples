# mlflow-examples - Keras/TensorFlow - Wine Quality


## Overview

* Keras TensorFlow 2.x 
* Train and predict with a number of model flavors and formats
* Algorithm: KerasRegressor
* Dataset: Wine quality
* Model flavors and formats
  * Logs model as MLflow Keras flavor 
  * Saves model in a number of other TensorFlow formats (non-flavors) such as SavedModel
* Real-time scoring
 * Launches an MLflow scoring server either as a local web server.
## Setup

`conda env create -f conda.yaml`

`conda activate mlflow-examples-keras_tf_wine`

## Training

Source: [train.py](train.py).

### Options

|Name | Required | Default | Description|
|-----|----------|---------|------------|
| experiment_name | no | none | Experiment name|
| model_name | no | None | Registered model name|
| epochs | no | 5 | Number of epochs |
| batch_size | no | 128 | Batch size |
| mlflow_custom_log | no | True | Explicitly log params and metrics with mlflow.log |
| keras_autolog | no | False | Automatically log params and metrics with mlflow.keras.autolog |
| tensorflow_autolog | no | False | Automatically log params and metrics with mlflow.tensorflow.autolog |


### Run
```
mlflow run -P experiment_name=keras_wine -P epochs3 -P batch_size=128
```
or
```
python train.py --experiment_name keras_wine --epochs 3 --batch_size 128
```

## Batch Scoring

Source: [predict.py](predict.py).

### Options

|Name | Required | Default | Description|
|-----|----------|---------|------------|
| run_id | yes | none | run_id |
| score_as_pyfunc | no | True | Score as PyFunc  |
| score_as_tensorflow_lite | no | False | Score as TensorFlow Lite  |

### Run
```
python predict.py --run_id 7e674524514846799310c41f10d6b99d
```

## Real-time Scoring - MLflow

### Data
[../data/score/wine-quality.json](../../data/score/wine-quality.json)

### Web server

Launch the web server.
```
mlflow models serve -m runs:/{run_id}/tensorflow-model --env-manager local --host 127.0.0.1 --port 5002
```


### Score 
```
curl -X POST -H "Content-Type:application/json" \
  -d @../data/score/wine-quality.json \
  http://localhost:5002/invocations
```