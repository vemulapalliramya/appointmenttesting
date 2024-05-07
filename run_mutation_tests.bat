<<<<<<< HEAD
@echo off
setlocal
FOR %%F in (mutants/*.py) DO (
    echo Running tests against %%F
    copy /Y %%F appointment.py
    pytest test_appointment.py
    echo.
)
endlocal
=======
@echo off
setlocal
FOR %%F in (mutants/*.py) DO (
    echo Running tests against %%F
    copy /Y %%F appointment.py
    pytest test_appointment.py
    echo.
)
endlocal
>>>>>>> master
