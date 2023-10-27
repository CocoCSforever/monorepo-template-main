Use fastapi as framework, Uvicorn as web server

pip install fastapi "uvicorn[standard]"
pip install pytest-cov pytest
mkdir src
mkdir tests
cd src
uvicorn main:app --reload


pytest --cov=src tests/
pytest --cov=src test_main.py

python3 -m venv venv
source venv/bin/activate

pytest -s
deactivate

To run pytest coverage, please locate at todo_app directory and run:
pytest --cov=src tests/



<!-- Notes for reference -->
coverage html
content type header
curl default content type for a request
ps aux | grep 8000