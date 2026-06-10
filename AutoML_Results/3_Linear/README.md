# Summary of 3_Linear

[<< Go back](../README.md)


## Linear Regression (Linear)
- **n_jobs**: -1
- **explain_level**: 2

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True

## Optimized metric
rmse

## Training time

3.2 seconds

### Metric details:
| Metric   |          Score |
|:---------|---------------:|
| MAE      | 4298.61        |
| MSE      |    3.95162e+07 |
| RMSE     | 6286.19        |
| R2       |    0.755476    |
| MAPE     |    0.38894     |



## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature   |    Learner_1 |
|:----------|-------------:|
| smoker    |  0.801335    |
| age       |  0.319925    |
| bmi       |  0.177483    |
| children  |  0.0454285   |
| sex       |  0.000349028 |
| intercept |  8.81327e-17 |
| region    | -0.0483806   |


## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



## SHAP Importance
![SHAP Importance](shap_importance.png)

## SHAP Dependence plots

### Dependence (Fold 1)
![SHAP Dependence from Fold 1](learner_fold_0_shap_dependence.png)

## SHAP Decision plots

### Top-10 Worst decisions (Fold 1)
![SHAP worst decisions from fold 1](learner_fold_0_shap_worst_decisions.png)
### Top-10 Best decisions (Fold 1)
![SHAP best decisions from fold 1](learner_fold_0_shap_best_decisions.png)

[<< Go back](../README.md)
