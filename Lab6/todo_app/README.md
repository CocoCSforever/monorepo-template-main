Use fastapi as framework, Uvicorn as web server  

`pip install fastapi "uvicorn[standard]"`  
`pip install pytest-cov pytest`  
`mkdir src`  
`mkdir tests`  
`cd src`  
`uvicorn main:app --reload`

To run pytest coverage, please locate at todo_app directory and run: `pytest --cov=src tests/`  

Within tests folder, run(may encounter "cannot find module"): `pytest --cov=src test_main.py`  

create virtual environment: `python3 -m venv venv`  
activate virtual environment: `source venv/bin/activate`  

print out info when running pytest:`pytest -s`  

deactivate virtual environment: `deactivate`  


<!-- Notes for reference -->
coverage html
content type header
curl default content type for a request
ps aux | grep 8000