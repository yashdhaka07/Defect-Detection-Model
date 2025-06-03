@echo off
setlocal

REM Set the name of the virtual environment
set VENV_NAME=myenv

REM Check if virtual environment already exists
if not exist "%VENV_NAME%\Scripts\activate.bat" (
    echo Creating virtual environment...
    python -m venv %VENV_NAME%
    
    echo Activating and installing packages...
    call %VENV_NAME%\Scripts\activate
    python -m pip install --upgrade pip
    pip install -r requirements.txt
) else (
    echo Virtual environment already exists.
)

REM Activate the environment
call %VENV_NAME%\Scripts\activate

REM Run Streamlit app
echo Starting Streamlit app...
streamlit run ui.py

endlocal