@echo off
echo.
echo 🚀 HTML to PDF Converter - Quick Start Script
echo ==============================================
echo.

REM Check if running in project directory
if not exist "README.md" (
    echo ❌ Error: Please run this script from the project root directory
    exit /b 1
)

REM Check for Node.js
where node >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Node.js is not installed. Please install it first:
    echo    https://nodejs.org/
    exit /b 1
)

REM Check for Python
where python >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Python is not installed. Please install it first:
    echo    https://www.python.org/downloads/
    exit /b 1
)

echo ✅ Prerequisites check passed!
echo.

REM Install Static Web Apps CLI if not installed
where swa >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo 📦 Installing Azure Static Web Apps CLI...
    call npm install -g @azure/static-web-apps-cli
    echo ✅ SWA CLI installed!
) else (
    echo ✅ SWA CLI already installed
)

REM Install Azure Functions Core Tools if not installed
where func >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo 📦 Installing Azure Functions Core Tools...
    call npm install -g azure-functions-core-tools@4
    echo ✅ Functions Core Tools installed!
) else (
    echo ✅ Functions Core Tools already installed
)

REM Install Python dependencies
echo.
echo 📦 Installing Python dependencies...
cd api
python -m pip install -r requirements.txt
cd ..
echo ✅ Python dependencies installed!

echo.
echo 🎉 Setup complete!
echo.
echo To start the development server, run:
echo    swa start public --api-location api
echo.
echo Then open: http://localhost:4280
echo.
pause
