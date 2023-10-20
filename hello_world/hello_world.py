import time
import platform
from argparse import ArgumentParser
import mlflow
from mlflow.entities import Param, Metric, RunTag

print("MLflow Version:", mlflow.__version__)
print("Tracking URI:", mlflow.tracking.get_tracking_uri())
client = mlflow.tracking.MlflowClient()


def run(alpha, run_origin):
    with mlflow.start_run(run_name=run_origin) as run:
        # Show thông tin về lần chạy
        print("runId:", run.info.run_id)
        print("experiment_id:", run.info.experiment_id)
        print("experiment_name:", client.get_experiment(run.info.experiment_id).name)
        print("artifact_uri:", mlflow.get_artifact_uri())
        print("alpha:", alpha)
        print("run_origin:", run_origin)
        # Log các param
        mlflow.log_param("alpha", alpha)
        mlflow.log_metric("rmse", 0.789)
        # Set value cho các tag lưu trữ các thông tin về dự án và lần chạy
        mlflow.set_tag("run_origin", run_origin)
        mlflow.set_tag("version.mlflow", mlflow.__version__)
        mlflow.set_tag("version.python", platform.python_version())
        mlflow.set_tag("version.platform", platform.system())
        # Log artifact ở đây là log 1 file text, có thể log nhiều dạng file khác như json, yaml, ...
        with open("info.txt", "w") as f:
            f.write("Hello world")
        mlflow.log_artifact("info.txt")
        # Ngoài cách log đơn lẻ như trên ta có thể dùng func log_batch để tránh bị overhead khi logging
        params = [Param("p1", "0.1"), Param("p2", "0.2")]
        now = round(time.time())
        metrics = [Metric("m1", 0.1, now, 0), Metric("m2", 0.2, now, 0)]
        tags = [RunTag("tag1", "hi1"), RunTag("tag2", "hi2")]
        client.log_batch(run.info.run_id, metrics, params, tags)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--experiment_name", dest="experiment_name",
                        help="Experiment name", default=None, type=str)
    parser.add_argument("--alpha", dest="alpha", help="alpha", default=0.1, type=float)
    parser.add_argument("--run_origin", dest="run_origin", help="run_origin", default="")
    args = parser.parse_args()
    print("Arguments:")
    for arg in vars(args):
        print(f"  {arg}: {getattr(args, arg)}")
    # Set experiment cho lần chạy, nếu chưa có experiment nào có tên được set thì MLflow sẽ tự tạo mới,
    # nếu đã có rồi thì sẽ tạo thêm 1 version mới
    # mlflow.set_experiment('hello_word')
    run(args.alpha, args.run_origin)
