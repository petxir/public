docker run -d -p 6070:6070 -p 6969:6969 --name gganco petirg/gganco && docker exec gganco websockify -D --web=novnc/ --cert=/etc/ssl/novnc.pem --key=/etc/ssl/novnc.pem 6969 localhost:5901 
