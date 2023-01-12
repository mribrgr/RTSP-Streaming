#!/bin/bash

# es wird die Verzeichnisstruktur von IntelliJ IDEA angenommen
# für Eclipse sind die Verzeichnisse entsprechend anzupassen

host=localhost
# port=$2
# video=$3

port=8554
video=htw.mjpeg
# video=mystream
# video=../../Contents/htw.mjpeg

src=src
bin=out/production/RTSP-Streaming


# Kompilierung
echo "compile classes..."
javac -cp $src ${src}/Client.java  -d $bin 

# Start
echo "start classes..."
java -cp $bin  Client $host $port $video 
