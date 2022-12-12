{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "import joblib\n",
    "def predict(data):\n",
    "    clf = joblib.load(\"rf_model.sav\")\n",
    "    return clf.predict(data)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting package metadata (current_repodata.json): ...working... done\n",
      "Solving environment: ...working... failed with initial frozen solve. Retrying with flexible solve.\n",
      "Collecting package metadata (repodata.json): ...working... done\n",
      "Solving environment: ...working... failed with initial frozen solve. Retrying with flexible solve.\n",
      "\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "PackagesNotFoundError: The following packages are not available from current channels:\n",
      "\n",
      "  - prediction\n",
      "\n",
      "Current channels:\n",
      "\n",
      "  - https://conda.anaconda.org/anaconda/win-64\n",
      "  - https://conda.anaconda.org/anaconda/noarch\n",
      "  - https://repo.anaconda.com/pkgs/main/win-64\n",
      "  - https://repo.anaconda.com/pkgs/main/noarch\n",
      "  - https://repo.anaconda.com/pkgs/r/win-64\n",
      "  - https://repo.anaconda.com/pkgs/r/noarch\n",
      "  - https://repo.anaconda.com/pkgs/msys2/win-64\n",
      "  - https://repo.anaconda.com/pkgs/msys2/noarch\n",
      "\n",
      "To search for alternate channels that may provide the conda package you're\n",
      "looking for, navigate to\n",
      "\n",
      "    https://anaconda.org\n",
      "\n",
      "and use the search bar at the top of the page.\n",
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "conda install -c anaconda prediction"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Collecting predictionNote: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "    ERROR: Command errored out with exit status 1:\n",
      "     command: 'c:\\ProgramData\\Anaconda3\\python.exe' -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '\"'\"'C:\\\\Users\\\\HP\\\\AppData\\\\Local\\\\Temp\\\\pip-install-js6ifui6\\\\uwsgi_ba7a5e9f56a14197a57361c407cfa5d6\\\\setup.py'\"'\"'; __file__='\"'\"'C:\\\\Users\\\\HP\\\\AppData\\\\Local\\\\Temp\\\\pip-install-js6ifui6\\\\uwsgi_ba7a5e9f56a14197a57361c407cfa5d6\\\\setup.py'\"'\"';f = getattr(tokenize, '\"'\"'open'\"'\"', open)(__file__) if os.path.exists(__file__) else io.StringIO('\"'\"'from setuptools import setup; setup()'\"'\"');code = f.read().replace('\"'\"'\\r\\n'\"'\"', '\"'\"'\\n'\"'\"');f.close();exec(compile(code, __file__, '\"'\"'exec'\"'\"'))' egg_info --egg-base 'C:\\Users\\HP\\AppData\\Local\\Temp\\pip-pip-egg-info-hhqscenx'\n",
      "         cwd: C:\\Users\\HP\\AppData\\Local\\Temp\\pip-install-js6ifui6\\uwsgi_ba7a5e9f56a14197a57361c407cfa5d6\\\n",
      "    Complete output (7 lines):\n",
      "    Traceback (most recent call last):\n",
      "      File \"<string>\", line 1, in <module>\n",
      "      File \"C:\\Users\\HP\\AppData\\Local\\Temp\\pip-install-js6ifui6\\uwsgi_ba7a5e9f56a14197a57361c407cfa5d6\\setup.py\", line 3, in <module>\n",
      "        import uwsgiconfig as uc\n",
      "      File \"C:\\Users\\HP\\AppData\\Local\\Temp\\pip-install-js6ifui6\\uwsgi_ba7a5e9f56a14197a57361c407cfa5d6\\uwsgiconfig.py\", line 8, in <module>\n",
      "        uwsgi_os = os.uname()[0]\n",
      "    AttributeError: module 'os' has no attribute 'uname'\n",
      "    ----------------------------------------\n",
      "WARNING: Discarding https://files.pythonhosted.org/packages/bb/0a/45e5aa80dc135889594bb371c082d20fb7ee7303b174874c996888cc8511/uwsgi-2.0.15.tar.gz#sha256=572ef9696b97595b4f44f6198fe8c06e6f4e6351d930d22e5330b071391272ff (from https://pypi.org/simple/uwsgi/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.\n",
      "ERROR: Cannot install prediction==0.0.2 and prediction==0.0.3 because these package versions have conflicting dependencies.\n",
      "ERROR: ResolutionImpossible: for help visit https://pip.pypa.io/en/latest/user_guide/#fixing-conflicting-dependencies\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "  Using cached prediction-0.0.3-py3-none-any.whl (20 kB)\n",
      "Collecting djangorestframework==3.7.7\n",
      "  Using cached djangorestframework-3.7.7-py2.py3-none-any.whl (1.1 MB)\n",
      "Collecting django-rest-framework==0.1.0\n",
      "  Using cached django-rest-framework-0.1.0.tar.gz (969 bytes)\n",
      "Collecting uWSGI==2.0.15\n",
      "  Using cached uwsgi-2.0.15.tar.gz (795 kB)\n",
      "Collecting prediction\n",
      "  Using cached prediction-0.0.2.tar.gz (5.9 kB)\n",
      "Collecting dj-database-url==0.4.2\n",
      "  Using cached dj_database_url-0.4.2-py2.py3-none-any.whl (5.6 kB)\n",
      "Collecting Django==2.0\n",
      "  Using cached Django-2.0-py3-none-any.whl (7.1 MB)\n",
      "Collecting django-cors-headers==2.1.0\n",
      "  Using cached django_cors_headers-2.1.0-py2.py3-none-any.whl (18 kB)\n",
      "Collecting django-filter==1.1.0\n",
      "  Using cached django_filter-1.1.0-py2.py3-none-any.whl (45 kB)\n",
      "Collecting djangorestframework-filters==0.10.2\n",
      "  Using cached djangorestframework_filters-0.10.2-py2.py3-none-any.whl (18 kB)\n",
      "Collecting pytz==2017.3\n",
      "  Using cached pytz-2017.3-py2.py3-none-any.whl (511 kB)\n",
      "\n",
      "The conflict is caused by:\n",
      "    prediction 0.0.3 depends on uWSGI==2.0.15\n",
      "    prediction 0.0.2 depends on uWSGI==2.0.15\n",
      "\n",
      "To fix this you could try to:\n",
      "1. loosen the range of package versions you've specified\n",
      "2. remove package versions to allow pip attempt to solve the dependency conflict\n",
      "\n"
     ]
    }
   ],
   "source": [
    "pip install prediction"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'prediction'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32mc:\\Users\\HP\\Desktop\\FaceDetectionModel\\FaceDetectionModel\\prediction.ipynb Cellule 4\u001b[0m in \u001b[0;36m<cell line: 2>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      <a href='vscode-notebook-cell:/c%3A/Users/HP/Desktop/FaceDetectionModel/FaceDetectionModel/prediction.ipynb#W2sZmlsZQ%3D%3D?line=0'>1</a>\u001b[0m \u001b[39mimport\u001b[39;00m \u001b[39mstreamlit\u001b[39;00m \u001b[39mas\u001b[39;00m \u001b[39mst\u001b[39;00m\n\u001b[1;32m----> <a href='vscode-notebook-cell:/c%3A/Users/HP/Desktop/FaceDetectionModel/FaceDetectionModel/prediction.ipynb#W2sZmlsZQ%3D%3D?line=1'>2</a>\u001b[0m \u001b[39mfrom\u001b[39;00m \u001b[39mprediction\u001b[39;00m \u001b[39mimport\u001b[39;00m predict\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'prediction'"
     ]
    }
   ],
   "source": [
    "\n",
    "import streamlit as st\n",
    "from prediction import predict\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2022-11-13 23:39:13.612 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run c:\\ProgramData\\Anaconda3\\lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "\n",
    "if st.button(\"Predict type of Iris\"):\n",
    "    result = predict(np.array([[sepal_l, sepal_w, petal_l, petal_w]]))\n",
    "    st.text(result[0])"
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
