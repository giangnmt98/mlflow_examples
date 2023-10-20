
# mlflow-example - hello_world

Simple Hello World hướng dẫn các cách khởi chạy MLflow experiment.


## Setup

**External tracking server**
```
export MLFLOW_TRACKING_URI=http://localhost:5000
```


## Running

### Command-line python
```
python hello_world.py
```


### Using mlflow run
##### Note: Set  --env-manager=local nếu muốn chạy trực tiếp trên local env

```
mlflow run . -P alpha=.01 -P run_origin=LocalRun 
```
Có thể chọn một experiment name (or ID) cụ thể:
```
mlflow run . \
  --experiment-name=hello_world --version=master \
  -P alpha=.01 -P run_origin=LocalRun
```

### Kiểm tra kết quả logging qua Tracking UI
```
# Khởi chạy Tracking UI.
mlflow ui
```
Sau đó truy cập vào http://localhost:5000 để vào Tracking UI. Lưu ý phải chạy command-line trên trong thư mục chứa MLproject