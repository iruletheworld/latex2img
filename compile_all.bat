@echo off
REM compile all the demos

for %%i in (compile_to_*.bat) do (

    call %%i

)
