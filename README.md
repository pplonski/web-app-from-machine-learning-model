# Create a Web App for Machine Learning model

[MLJAR AutoML](https://github.com/mljar/mljar-supervised) can automaticall train a Machine Learning pipeline for you and create a **Web App** so you can easily share your models with non-technical users.

## What is good in it?

- AutoML model for predicting medical insurance charges based on demographic data (`age`, `sex`, `bmi`, `children`, `smoker`, `region`).
- Web App created automatically with `automl.app()`



![](https://raw.githubusercontent.com/pplonski/web-app-from-machine-learning-model/refs/heads/main/media/mercury-apps.png)

![](https://raw.githubusercontent.com/pplonski/web-app-from-machine-learning-model/refs/heads/main/media/predict-single-sample.png)

![](https://raw.githubusercontent.com/pplonski/web-app-from-machine-learning-model/refs/heads/main/media/batch-prediction.png)

Main columns:

- `age` - age of the person
- `sex` - gender
- `bmi` - body mass index
- `children` - number of children/dependents
- `smoker` - smoking status
- `region` - residential region
- `charges` - medical insurance charges

```
AutoML directory: AutoML_Results
The task is regression with evaluation metric rmse
AutoML will use algorithms: ['Baseline', 'Linear', 'Decision Tree', 'Random Forest', 'Xgboost', 'Neural Network']
AutoML will ensemble available models
AutoML steps: ['simple_algorithms', 'default_algorithms', 'ensemble']
* Step simple_algorithms will try to check up to 3 models
1_Baseline rmse 12736.255075 trained in 0.25 seconds
2_DecisionTree rmse 5017.671212 trained in 3.54 seconds
3_Linear rmse 6286.19264 trained in 3.25 seconds
* Step default_algorithms will try to check up to 3 models
4_Default_Xgboost rmse 5105.238656 trained in 3.54 seconds
5_Default_NeuralNetwork rmse 5304.191718 trained in 2.51 seconds
6_Default_RandomForest rmse 4906.421265 trained in 4.31 seconds
* Step ensemble will try to check up to 1 model
Ensemble rmse 4852.221625 trained in 0.16 seconds
AutoML fit time: 22.28 seconds
AutoML best model: Ensemble
```