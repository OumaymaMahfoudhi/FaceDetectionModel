{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "  WARNING: The script cmark.exe is installed in 'C:\\Users\\HP\\AppData\\Roaming\\Python\\Python39\\Scripts' which is not on PATH.\n",
      "  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.\n",
      "  WARNING: The script pysemver.exe is installed in 'C:\\Users\\HP\\AppData\\Roaming\\Python\\Python39\\Scripts' which is not on PATH.\n",
      "  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.\n",
      "  WARNING: The script plasma_store.exe is installed in 'C:\\Users\\HP\\AppData\\Roaming\\Python\\Python39\\Scripts' which is not on PATH.\n",
      "  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.\n",
      "  WARNING: The script streamlit.exe is installed in 'C:\\Users\\HP\\AppData\\Roaming\\Python\\Python39\\Scripts' which is not on PATH.\n",
      "  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Collecting streamlit\n",
      "  Using cached streamlit-1.14.1-py2.py3-none-any.whl (9.2 MB)\n",
      "Collecting pympler>=0.9\n",
      "  Using cached Pympler-1.0.1-py3-none-any.whl (164 kB)\n",
      "Requirement already satisfied: watchdog in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (2.1.6)\n",
      "Collecting gitpython!=3.1.19\n",
      "  Using cached GitPython-3.1.29-py3-none-any.whl (182 kB)\n",
      "Requirement already satisfied: pillow>=6.2.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (9.0.1)\n",
      "Collecting blinker>=1.0.0\n",
      "  Using cached blinker-1.5-py2.py3-none-any.whl (12 kB)\n",
      "Requirement already satisfied: toml in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: click>=7.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (8.0.4)\n",
      "Collecting tzlocal>=1.1\n",
      "  Using cached tzlocal-4.2-py3-none-any.whl (19 kB)\n",
      "Requirement already satisfied: numpy in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (1.21.5)\n",
      "Requirement already satisfied: typing-extensions>=3.10.0.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (4.1.1)\n",
      "Requirement already satisfied: tornado>=5.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (6.1)\n",
      "Requirement already satisfied: pandas>=0.21.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (1.4.2)\n",
      "Requirement already satisfied: importlib-metadata>=1.4 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (4.11.3)\n",
      "Collecting pyarrow>=4.0\n",
      "  Downloading pyarrow-10.0.0-cp39-cp39-win_amd64.whl (20.0 MB)\n",
      "Requirement already satisfied: requests>=2.4 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (2.27.1)\n",
      "Collecting rich>=10.11.0\n",
      "  Using cached rich-12.6.0-py3-none-any.whl (237 kB)\n",
      "Collecting altair>=3.2.0\n",
      "  Using cached altair-4.2.0-py3-none-any.whl (812 kB)\n",
      "Requirement already satisfied: cachetools>=4.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (4.2.2)\n",
      "Requirement already satisfied: protobuf<4,>=3.12 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (3.19.1)\n",
      "Collecting semver\n",
      "  Using cached semver-2.13.0-py2.py3-none-any.whl (12 kB)\n",
      "Collecting validators>=0.2\n",
      "  Using cached validators-0.20.0.tar.gz (30 kB)\n",
      "Requirement already satisfied: packaging>=14.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (21.3)\n",
      "Requirement already satisfied: python-dateutil in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (2.8.2)\n",
      "Collecting pydeck>=0.1.dev5\n",
      "  Using cached pydeck-0.8.0-py2.py3-none-any.whl (4.7 MB)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from altair>=3.2.0->streamlit) (4.4.0)\n",
      "Requirement already satisfied: jinja2 in c:\\programdata\\anaconda3\\lib\\site-packages (from altair>=3.2.0->streamlit) (2.11.3)\n",
      "Requirement already satisfied: entrypoints in c:\\programdata\\anaconda3\\lib\\site-packages (from altair>=3.2.0->streamlit) (0.4)\n",
      "Requirement already satisfied: toolz in c:\\programdata\\anaconda3\\lib\\site-packages (from altair>=3.2.0->streamlit) (0.11.2)\n",
      "Requirement already satisfied: colorama in c:\\programdata\\anaconda3\\lib\\site-packages (from click>=7.0->streamlit) (0.4.4)\n",
      "Collecting gitdb<5,>=4.0.1\n",
      "  Downloading gitdb-4.0.9-py3-none-any.whl (63 kB)\n",
      "Collecting smmap<6,>=3.0.1\n",
      "  Downloading smmap-5.0.0-py3-none-any.whl (24 kB)\n",
      "Requirement already satisfied: zipp>=0.5 in c:\\programdata\\anaconda3\\lib\\site-packages (from importlib-metadata>=1.4->streamlit) (3.7.0)\n",
      "Requirement already satisfied: attrs>=17.4.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (21.4.0)\n",
      "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (0.18.0)\n",
      "Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in c:\\programdata\\anaconda3\\lib\\site-packages (from packaging>=14.1->streamlit) (3.0.4)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from pandas>=0.21.0->streamlit) (2021.3)\n",
      "Requirement already satisfied: MarkupSafe>=0.23 in c:\\programdata\\anaconda3\\lib\\site-packages (from jinja2->altair>=3.2.0->streamlit) (2.0.1)\n",
      "Requirement already satisfied: six>=1.5 in c:\\programdata\\anaconda3\\lib\\site-packages (from python-dateutil->streamlit) (1.16.0)\n",
      "Requirement already satisfied: charset-normalizer~=2.0.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests>=2.4->streamlit) (2.0.4)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests>=2.4->streamlit) (2021.10.8)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests>=2.4->streamlit) (3.3)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests>=2.4->streamlit) (1.26.9)\n",
      "Collecting commonmark<0.10.0,>=0.9.0\n",
      "  Downloading commonmark-0.9.1-py2.py3-none-any.whl (51 kB)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.6.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from rich>=10.11.0->streamlit) (2.11.2)\n",
      "Collecting tzdata\n",
      "  Downloading tzdata-2022.6-py2.py3-none-any.whl (338 kB)\n",
      "Collecting pytz-deprecation-shim\n",
      "  Downloading pytz_deprecation_shim-0.1.0.post0-py2.py3-none-any.whl (15 kB)\n",
      "Requirement already satisfied: decorator>=3.4.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from validators>=0.2->streamlit) (5.1.1)\n",
      "Building wheels for collected packages: validators\n",
      "  Building wheel for validators (setup.py): started\n",
      "  Building wheel for validators (setup.py): finished with status 'done'\n",
      "  Created wheel for validators: filename=validators-0.20.0-py3-none-any.whl size=19582 sha256=203d7a190cbae2e5a2eb79a620b0a4af20c29da90797dc59ea1ab07f0de187f5\n",
      "  Stored in directory: c:\\users\\hp\\appdata\\local\\pip\\cache\\wheels\\2d\\f0\\a8\\1094fca7a7e5d0d12ff56e0c64675d72aa5cc81a5fc200e849\n",
      "Successfully built validators\n",
      "Installing collected packages: tzdata, smmap, pytz-deprecation-shim, gitdb, commonmark, validators, tzlocal, semver, rich, pympler, pydeck, pyarrow, gitpython, blinker, altair, streamlit\n",
      "Successfully installed altair-4.2.0 blinker-1.5 commonmark-0.9.1 gitdb-4.0.9 gitpython-3.1.29 pyarrow-10.0.0 pydeck-0.8.0 pympler-1.0.1 pytz-deprecation-shim-0.1.0.post0 rich-12.6.0 semver-2.13.0 smmap-5.0.0 streamlit-1.14.1 tzdata-2022.6 tzlocal-4.2 validators-0.20.0\n",
      "^C\n",
      "\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "conda install streamlit"
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
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 4,
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
    "conda install prediction"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import numpy as np\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2022-11-13 22:58:08.446 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run c:\\ProgramData\\Anaconda3\\lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator(_root_container=0, _provided_cursor=None, _parent=None, _block_type=None, _form_data=None)"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.title('Classifying Iris Flowers')\n",
    "st.markdown('Toy model to play to classify iris flowers into \\\n",
    "setosa, versicolor, virginica')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "st.header(\"Plant Features\")\n",
    "col1, col2 = st.columns(2)\n",
    "with col1:\n",
    "    st.text(\"Sepal characteristics\")\n",
    "    sepal_l = st.slider('Sepal lenght (cm)', 1.0, 8.0, 0.5)\n",
    "    sepal_w = st.slider('Sepal width (cm)', 2.0, 4.4, 0.5)\n",
    "with col2:\n",
    "    st.text(\"Pepal characteristics\")\n",
    "    petal_l = st.slider('Petal lenght (cm)', 1.0, 7.0, 0.5)\n",
    "    petal_w = st.slider('Petal width (cm)', 0.1, 2.5, 0.5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.button(\"Predict type of Iris\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: streamlit in c:\\users\\hp\\appdata\\roaming\\python\\python39\\site-packages (1.14.1)\n",
      "Requirement already satisfied: pandas>=0.21.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (1.4.2)\n",
      "Requirement already satisfied: watchdog in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (2.1.6)\n",
      "Requirement already satisfied: importlib-metadata>=1.4 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (4.11.3)\n",
      "Requirement already satisfied: python-dateutil in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (2.8.2)\n",
      "Requirement already satisfied: pillow>=6.2.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (9.0.1)\n",
      "Requirement already satisfied: gitpython!=3.1.19 in c:\\users\\hp\\appdata\\roaming\\python\\python39\\site-packages (from streamlit) (3.1.29)\n",
      "Requirement already satisfied: cachetools>=4.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (4.2.2)\n",
      "Requirement already satisfied: altair>=3.2.0 in c:\\users\\hp\\appdata\\roaming\\python\\python39\\site-packages (from streamlit) (4.2.0)\n",
      "Requirement already satisfied: requests>=2.4 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (2.27.1)\n",
      "Requirement already satisfied: pyarrow>=4.0 in c:\\users\\hp\\appdata\\roaming\\python\\python39\\site-packages (from streamlit) (10.0.0)\n",
      "Requirement already satisfied: pympler>=0.9 in c:\\users\\hp\\appdata\\roaming\\python\\python39\\site-packages (from streamlit) (1.0.1)\n",
      "Requirement already satisfied: packaging>=14.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (21.3)\n",
      "Requirement already satisfied: pydeck>=0.1.dev5 in c:\\users\\hp\\appdata\\roaming\\python\\python39\\site-packages (from streamlit) (0.8.0)\n",
      "Requirement already satisfied: toml in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: tornado>=5.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (6.1)\n",
      "Requirement already satisfied: tzlocal>=1.1 in c:\\users\\hp\\appdata\\roaming\\python\\python39\\site-packages (from streamlit) (4.2)\n",
      "Requirement already satisfied: semver in c:\\users\\hp\\appdata\\roaming\\python\\python39\\site-packages (from streamlit) (2.13.0)\n",
      "Requirement already satisfied: validators>=0.2 in c:\\users\\hp\\appdata\\roaming\\python\\python39\\site-packages (from streamlit) (0.20.0)\n",
      "Requirement already satisfied: rich>=10.11.0 in c:\\users\\hp\\appdata\\roaming\\python\\python39\\site-packages (from streamlit) (12.6.0)\n",
      "Requirement already satisfied: typing-extensions>=3.10.0.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (4.1.1)\n",
      "Requirement already satisfied: click>=7.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (8.0.4)\n",
      "Requirement already satisfied: protobuf<4,>=3.12 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (3.19.1)\n",
      "Requirement already satisfied: numpy in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (1.21.5)\n",
      "Requirement already satisfied: blinker>=1.0.0 in c:\\users\\hp\\appdata\\roaming\\python\\python39\\site-packages (from streamlit) (1.5)\n",
      "Requirement already satisfied: jinja2 in c:\\programdata\\anaconda3\\lib\\site-packages (from altair>=3.2.0->streamlit) (2.11.3)\n",
      "Requirement already satisfied: toolz in c:\\programdata\\anaconda3\\lib\\site-packages (from altair>=3.2.0->streamlit) (0.11.2)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from altair>=3.2.0->streamlit) (4.4.0)Note: you may need to restart the kernel to use updated packages.\n",
      "\n",
      "Requirement already satisfied: entrypoints in c:\\programdata\\anaconda3\\lib\\site-packages (from altair>=3.2.0->streamlit) (0.4)\n",
      "Requirement already satisfied: colorama in c:\\programdata\\anaconda3\\lib\\site-packages (from click>=7.0->streamlit) (0.4.4)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in c:\\users\\hp\\appdata\\roaming\\python\\python39\\site-packages (from gitpython!=3.1.19->streamlit) (4.0.9)\n",
      "Requirement already satisfied: smmap<6,>=3.0.1 in c:\\users\\hp\\appdata\\roaming\\python\\python39\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19->streamlit) (5.0.0)\n",
      "Requirement already satisfied: zipp>=0.5 in c:\\programdata\\anaconda3\\lib\\site-packages (from importlib-metadata>=1.4->streamlit) (3.7.0)\n",
      "Requirement already satisfied: attrs>=17.4.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (21.4.0)\n",
      "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (0.18.0)\n",
      "Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in c:\\programdata\\anaconda3\\lib\\site-packages (from packaging>=14.1->streamlit) (3.0.4)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from pandas>=0.21.0->streamlit) (2021.3)\n",
      "Requirement already satisfied: MarkupSafe>=0.23 in c:\\programdata\\anaconda3\\lib\\site-packages (from jinja2->altair>=3.2.0->streamlit) (2.0.1)\n",
      "Requirement already satisfied: six>=1.5 in c:\\programdata\\anaconda3\\lib\\site-packages (from python-dateutil->streamlit) (1.16.0)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests>=2.4->streamlit) (1.26.9)\n",
      "Requirement already satisfied: charset-normalizer~=2.0.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests>=2.4->streamlit) (2.0.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests>=2.4->streamlit) (3.3)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests>=2.4->streamlit) (2021.10.8)\n",
      "Requirement already satisfied: commonmark<0.10.0,>=0.9.0 in c:\\users\\hp\\appdata\\roaming\\python\\python39\\site-packages (from rich>=10.11.0->streamlit) (0.9.1)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.6.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from rich>=10.11.0->streamlit) (2.11.2)\n",
      "Requirement already satisfied: tzdata in c:\\users\\hp\\appdata\\roaming\\python\\python39\\site-packages (from tzlocal>=1.1->streamlit) (2022.6)\n",
      "Requirement already satisfied: pytz-deprecation-shim in c:\\users\\hp\\appdata\\roaming\\python\\python39\\site-packages (from tzlocal>=1.1->streamlit) (0.1.0.post0)\n",
      "Requirement already satisfied: decorator>=3.4.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from validators>=0.2->streamlit) (5.1.1)\n"
     ]
    }
   ],
   "source": [
    "pip install streamlit"
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
   "version": "3.9.12 (main, Apr  4 2022, 05:22:27) [MSC v.1916 64 bit (AMD64)]"
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
