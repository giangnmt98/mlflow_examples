# Ví dụ XGBoost
Ví dụ này train mô hình XGBoost phân loại hoa Iris và log lại các hyperparameter, metric, and trained model.

## Launch MLflow Tracking server
```
mlflow server --host localhost --port 5000
```

## Running the code

```
python train.py --learning-rate 0.2 --colsample-bytree 0.8 --subsample 0.9
```

Có thể thử nghiệm với các giá trị tham số khác nhau như:

```
python train.py --learning-rate 0.4 --colsample-bytree 0.7 --subsample 0.8
```

## Running the code as a MLproject

```
mlflow run . -P learning_rate=0.2 -P colsample_bytree=0.8 -P subsample=0.9
```



I