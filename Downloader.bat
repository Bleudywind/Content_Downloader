@echo off
@if not exist src/Musiques md "src\Musiques"
@if not exist src/Video md "src\Video"
@if not exist target/Musiques md "target\Musiques"
@if not exist target/Video md "target\Video"

docker run -it --rm -v %cd%/src:/app yt-converter

@robocopy ./src/Musiques ./target/Musiques /s /e /r:0 /z /njh /njs /ndl /nc /ns
@robocopy ./src/Video ./target/Video /s /e /r:0 /z /njh /njs /ndl /nc /ns
@cd /d src/Musiques
@for /F "delims=" %%i in ('dir /b') do (rmdir "%%i" /s/q || del "%%i" /s/q)
@cd ..
@cd ..
@cd /d src/Video
@for /F "delims=" %%i in ('dir /b') do (rmdir "%%i" /s/q || del "%%i" /s/q)
@cd ..
@cd ..

@echo on
@echo:
@echo:
@echo Done everything as been downloaded !