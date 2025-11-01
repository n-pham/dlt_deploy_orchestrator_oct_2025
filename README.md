# Set up

```bash
uv pip install -r pyproject.toml -c constraints.txt
uv sync
```

# Airflow

```bash
dlt deploy chess_pipeline.py airflow-composer
```

Edit generated code to be able to import existing dlt source
```python
# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from chess import source
```

Run Airflow locally
```bash
export AIRFLOW__CORE__DAGS_FOLDER=./dags
airflow standalone
# Open http://localhost:8080, look for the password from this log line `Login with username: admin  password: `

# To skip example dags
# edit ~/airflow/airflow.cfg
# [core]
# load_examples = False

```

