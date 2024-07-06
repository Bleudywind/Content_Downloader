docker build -t yt-converter .
@if not exist src/Musiques md "src\Musiques"
@if not exist src/Video md "src\Video"
@if not exist target/Musiques md "target\Musiques"
@if not exist target/Video md "target\Video"