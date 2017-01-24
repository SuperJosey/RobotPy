sudo pkill uv4l
sudo uv4l -nopreview --auto-video_nr --driver raspicam --encoding mjpeg --width 420 --height 300 --framerate 15 --server-option '--port=9090' --server-option '--max-queued-connections=2' --server-option '--max-streams=2' --server-option '--max-threads=29'
python ./server.py
