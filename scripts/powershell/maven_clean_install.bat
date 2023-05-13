@echo on

setlocal

set FOLDER_1=C:\dev\code\A
set FOLDER_2=C:\dev\code\B
set FOLDER_3=C:\dev\code\C

echo Running Maven clean install in Folders...
cd %FOLDER_1%
call "%M2%\mvn" clean install -DskipTests
if errorlevel 1 (
    echo Error: Maven clean install failed in Folder 1.
    exit /b 1
)

cd %FOLDER_2%
call "%M2%\mvn" clean install -DskipTests
if errorlevel 1 (
    echo Error: Maven clean install failed in Folder 2.
    exit /b 1
)

cd %FOLDER_3%
call "%M2%\mvn" clean install -DskipTests
if errorlevel 1 (
    echo Error: Maven clean install failed in Folder 3.
    exit /b 1
)

@REM echo Running Maven clean install in Folder 1...
@REM start cmd /c "cd %FOLDER_1% && call "%M2%\mvn" clean install -DskipTests"
@REM
@REM echo Running Maven clean install in Folder 3...
@REM start cmd /c "cd %FOLDER_3% && call "%M2%\mvn" clean install -DskipTests"
@REM
@REM REM Wait for all commands to complete
@REM wait

echo Maven clean install completed in all folders.

endlocal