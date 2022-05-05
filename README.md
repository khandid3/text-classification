# Welcome to my repository about text classification!

## Description of the project 

In this project, we want to predict the difficulty of a given french text using Google Cloud Natual Language. 

The labels are {A1, A2, B1, B2, C1, C2}.

## Methodology

I trained the model on a dataset which contains almost 4800 labelled sentences. You can access this dataset in the folder [dataset](github.com/khandid3/text-classification/tree/main/data). 
The data set is called original_training_data.csv. I cleaned this data set and create the new data set clean_training_data.csv. The operations I made to clean it were:
  * Deleting the 1st colum "id". To do so, we can just copy-paste our data [here](https://www.browserling.com/tools/delete-column), insert the column number we want to delete (in our case it is 1), select the option "delete column", copy the new data generated and paste it on a new csv file. Another way to do, it is to code it. You can for example create a dataframe with pandas and then delete the column and download the new data set (see an example [here](https://github.com/khandid3/text-classification/tree/main/docs/delete_idcolumn.png)),
  * I deleted the first row which contained the columns names, i.e. "sentence" and "difficulty". For that, we simply open the csv file with an editor and deleted the first line, e.g. you can just open the file with vim in the terminal,
  * I deleted the duplicated items (actually Google Cloud does it by itself, so it is not necessary to do it).

## Refresher for evaluation metrics

Let TP be true positive, TN be true negative, FP be false positive, FN be false negative.

 * Accuracy = (TP + TN) / (TP + TN + FP + FN)
 * Precision = TP / (TP + FP)
 * Recall = TP / (TP + FN)
 * F1-score = (2 * Precision * Recall) / (Precision + Recall) 

## Evaluation of the model

I present you the different evaluation matrics for my model trained in Google Cloud. 

The confusion matrix is present below

![confusion matrix](https://github.com/khandid3/text-classification/blob/main/docs/confusion_matrix.png "confusion matrix")

We observe that the best label predicted is A1, because 63 % of A1 difficulty items were predicted correctly, whereas other difficulty levels were predicted with a lower accuracy.  The worst label predicted is A2.

Now I present you an animation of the evaluation matrix where I play with the onfidence threshold

https://user-images.githubusercontent.com/66648452/167023008-7fbabf6d-67f2-48b5-9334-bc910f5fc6d4.mov

We observe than when the recall dicreases, the precision increases, and vice-versa.
We can also point out the  intersection between recall score and precision score when the confidence threshold value is 0.4.
At this stage, the precision equlas 49.78% and the recall equals 48.02%.

We can compute the F1-score whit the confidence threshold at 0.4. It gives use:
(2 * 0.4978 * 0.4802) / (0.4978 + 0.4802) = 0.49.

## Next steps

Now I want to call this model from my notebook in Google Colab. However, I got an error when I want to import automl_v1 from google.cloud package. I was not able to fix it yet. [Access to the notebook](https://github.com/khandid3/text-classification/blob/main/code/text_classification.ipynb)



