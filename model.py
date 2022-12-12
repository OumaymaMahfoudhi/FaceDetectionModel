{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (3049325002.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Input \u001b[1;32mIn [5]\u001b[1;36m\u001b[0m\n\u001b[1;33m    pip install  scikit-learn\u001b[0m\n\u001b[1;37m        ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "\n",
    "pip install  scikit-learn\n",
    "import joblib as job "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: joblib in c:\\programdata\\anaconda3\\lib\\site-packages (1.1.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: pandas in c:\\programdata\\anaconda3\\lib\\site-packages (1.4.2)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from pandas) (2021.3)\n",
      "Requirement already satisfied: python-dateutil>=2.8.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from pandas) (2.8.2)\n",
      "Requirement already satisfied: numpy>=1.18.5 in c:\\programdata\\anaconda3\\lib\\site-packages (from pandas) (1.21.5)\n",
      "Requirement already satisfied: six>=1.5 in c:\\programdata\\anaconda3\\lib\\site-packages (from python-dateutil>=2.8.1->pandas) (1.16.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install pandas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\HP\\AppData\\Local\\Temp\\ipykernel_87428\\1196425358.py:19: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples,), for example using ravel().\n",
      "  clf.fit(X_train, y_train)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy: 0.9555555555555556\n"
     ]
    }
   ],
   "source": [
    "# Read original dataset\n",
    "\n",
    "import pandas as pd\n",
    "import random\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.metrics import accuracy_score\n",
    "iris_df = pd.read_csv(\"data/iris.csv\")\n",
    "iris_df.sample(frac=1, random_state=random.seed())\n",
    "# selecting features and target data\n",
    "X = iris_df[['sepal.length' , 'sepal.width' , 'petal.length' , 'petal.width']]\n",
    "y = iris_df[['variety']]\n",
    "# split data into train and test sets\n",
    "# 70% training and 30% test\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=random.seed(), stratify=y)\n",
    "# create an instance of the random forest classifier\n",
    "clf = RandomForestClassifier(n_estimators=100)\n",
    "# train the classifier on the training data\n",
    "clf.fit(X_train, y_train)\n",
    "# predict on the test set\n",
    "y_pred = clf.predict(X_test)\n",
    "# calculate accuracy\n",
    "accuracy = accuracy_score(y_test, y_pred)\n",
    "print(f\"Accuracy: {accuracy}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting package metadata (current_repodata.json): ...working... done\n",
      "Solving environment: ...working... done\n",
      "\n",
      "## Package Plan ##\n",
      "\n",
      "  environment location: c:\\ProgramData\\Anaconda3\n",
      "\n",
      "  added / updated specs:\n",
      "    - joblib\n",
      "\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "EnvironmentNotWritableError: The current user does not have write permissions to the target environment.\n",
      "  environment location: c:\\ProgramData\\Anaconda3\n",
      "\n",
      "\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "The following packages will be UPDATED:\n",
      "\n",
      "  conda                               4.12.0-py39haa95532_0 --> 22.9.0-py39haa95532_0\n",
      "\n",
      "\n",
      "Preparing transaction: ...working... done\n",
      "Verifying transaction: ...working... failed\n"
     ]
    }
   ],
   "source": [
    "conda install joblib\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['rf_model.sav']"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# save the model to disk\n",
    "\n",
    "\n",
    "import joblib as job \n",
    "job.dump(clf, \"rf_model.sav\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "     sepal.length  sepal.width  petal.length  petal.width     variety\n",
      "24            4.8          3.4           1.9          0.2      Setosa\n",
      "67            5.8          2.7           4.1          1.0  Versicolor\n",
      "141           6.9          3.1           5.1          2.3   Virginica\n",
      "129           7.2          3.0           5.8          1.6   Virginica\n",
      "83            6.0          2.7           5.1          1.6  Versicolor\n",
      "..            ...          ...           ...          ...         ...\n",
      "39            5.1          3.4           1.5          0.2      Setosa\n",
      "97            6.2          2.9           4.3          1.3  Versicolor\n",
      "56            6.3          3.3           4.7          1.6  Versicolor\n",
      "27            5.2          3.5           1.5          0.2      Setosa\n",
      "128           6.4          2.8           5.6          2.1   Virginica\n",
      "\n",
      "[150 rows x 5 columns]\n",
      "     sepal.length  sepal.width  petal.length  petal.width    variety\n",
      "0             5.1          3.5           1.4          0.2     Setosa\n",
      "1             4.9          3.0           1.4          0.2     Setosa\n",
      "2             4.7          3.2           1.3          0.2     Setosa\n",
      "3             4.6          3.1           1.5          0.2     Setosa\n",
      "4             5.0          3.6           1.4          0.2     Setosa\n",
      "..            ...          ...           ...          ...        ...\n",
      "145           6.7          3.0           5.2          2.3  Virginica\n",
      "146           6.3          2.5           5.0          1.9  Virginica\n",
      "147           6.5          3.0           5.2          2.0  Virginica\n",
      "148           6.2          3.4           5.4          2.3  Virginica\n",
      "149           5.9          3.0           5.1          1.8  Virginica\n",
      "\n",
      "[150 rows x 5 columns]\n"
     ]
    }
   ],
   "source": [
    "print(iris_df.sample(frac=1, random_state= random.seed()))\n",
    "print(iris_df)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.9.12 ('base')",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "ad2bdc8ecc057115af97d19610ffacc2b4e99fae6737bb82f5d7fb13d2f2c186"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
