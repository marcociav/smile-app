# model-creation

## Setup Env and Packages

### Using pip

create venv (one time)

```console
python -m venv samc_venv
```

activate venv

```console
samc_venv\Scripts\activate.bat
```

install requirements (one time)

```console
pip install -r requirements.txt
```

enable jupyter_http_over_ws (one time)

```console
jupyter serverextension enable --py jupyter_http_over_ws
```

add venv to jupyter (one time)

```console
python -m ipykernel install --user --name=samc_venv
```

## Run jupyter notebook in Google Colab

execute command:

```console
jupyter notebook --NotebookApp.allow_origin=https://colab.research.google.com --NotebookApp.port_retries=0 --port=8888 --no-browser
```

copy the link from the terminal and paste it into Google Colab -> Connect -> Connect to a local runtime

## ETL

run the etl.py script

```console
python etl.py
```

to create 2 new folders, containing smiling faces and non smiling faces

/data/transformed/smile
/data/transformed/non_smile
