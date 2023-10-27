Use fastapi as framework, Uvicorn as web server

pip install fastapi "uvicorn[standard]"
pip install pytest-cov pytest
mkdir src
mkdir tests
cd src
uvicorn main:app --reload

pytest --cov=src tests/

python3 -m venv venv
source venv/bin/activate

pytest -s
deactivate
