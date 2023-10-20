import os
import click
import platform
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
import mlflow
import mlflow.keras
from tabulate import tabulate
import utils

print("MLflow Version:", mlflow.__version__)
print("Tracking URI:", mlflow.tracking.get_tracking_uri())
client = mlflow.tracking.MlflowClient()
print("Operating System:", platform.system() + " - " + platform.release())
tmp_dir = "out"


# def predict_keras(model_uri, data):
def predict_tensorflow_model(model_uri, data):
    print(f"\nmlflow.keras.load_model\nModel URI: {model_uri}")
    model = mlflow.keras.load_model(model_uri)
    print("model.type:", type(model))
    predictions = model.predict(data)
    display(predictions)


def _predict_tensorflow_model(run_id, data):
    model_name = "tensorflow-model"
    print(f"\nkeras.models.load_model\nModel name:{model_name}\nRun ID:{run_id}")
    client.download_artifacts(run_id, model_name, tmp_dir)
    model = keras.models.load_model(os.path.join(tmp_dir, model_name))
    print("model.type:", type(model))
    predictions = model.predict(data)
    display(predictions)


def predict_pyfunc(model_uri, data, msg):
    print(f"\nmlflow.pyfunc.load_model - {msg}\nModel URI: {model_uri}")
    model = mlflow.pyfunc.load_model(model_uri)
    print("model.type:", type(model))
    predictions = model.predict(data)
    display(predictions)


def display(predictions):
    print("predictions.shape:", predictions.shape)
    df = pd.DataFrame(data=predictions, columns=["prediction"])
    df = df.head(2)
    print(tabulate(df, headers="keys", tablefmt="psql", showindex=False))


def artifact_exists(run_id, path):
    return len(client.list_artifacts(run_id, path)) > 0


@click.command()
@click.option("--run_id", help="RunID", default=None, type=str)
@click.option("--data_path", help="Data path", default="../data/train/wine-quality-white.csv", type=str)
@click.option("--score_as_pyfunc", help="Score as PyFunc", default=True, type=bool)
def main(run_id, data_path, score_as_pyfunc):
    print("Options:")
    for k, v in locals().items():
        print(f"  {k}: {v}")

    utils.dump(run_id)
    data, _, _, _ = utils.build_data(data_path)

    model_uri = f"runs:/{run_id}/tensorflow-model"
    predict_tensorflow_model(model_uri, data)
    if score_as_pyfunc:
        predict_pyfunc(model_uri, data, "tensorflow-model")


if __name__ == "__main__":
    main()
