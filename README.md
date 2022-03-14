# Dialect_prediction

In this repo you will find:

a-	Data fetching script 

Define your path and maximum batch, in our case the maximum batch is defined by 1000 it can be changed and the code still can handle that. Also, the ids are fetched to the last one handling the last batch. The input to this script is a CSV file given (dialect_dataset.csv) and the output is saved under the name (fetched_data.csv) to be ready for the second phase of preprocessing.

Note: in case of saving the CSV file and cannot clearly see the Arabic language which is a common problem in some versions follow these steps in the excel program: Data->  From Text -> select the CSV file -> File_origin to "Unicode (UTF-8) ->select the delimiter used -> Finish

b-	Data preprocessing script

After revising the fetched data and according to the needed task of dialect prediction, the needed preprocessing are:
For the Arabic data:
-remove punctuation
       -remove English letters and numbers
-remove emojis
-remove duplicate spaces
- tokenize each sentence into words
       - vectorize them to be suitable as an input to the model
For labels:
-convert dialect labels from categorical into numerical

c-	Model training notebook

The used models are Arabert as a deep learning model and SVM as a machine learning model. I chose the models from the paper introduced in the task. 
Two notebooks are available:

The SVM notebook for the machine learning model.
The AraBERT notebook for the deep learning model. 

Also, I applied their own preprocessing technique as according to their claims they already trained the model for tasks similar to dialect classification for Arabic language.

For the Arabert model, the accuracy is 60.2641 % after training for one epoch with F1 score of 0.574415 and a validation loss of 1.246825.
For the SVM model, the accuracy of the trained model is 46.5889 %.

