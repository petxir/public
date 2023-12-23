FROM ubuntu:latest
WORKDIR home
RUN DEBIAN_FRONTEND=noninteractive apt-get -y update
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install tigervnc-standalone-server tigervnc-common xfce4 novnc websockify unzip nodejs npm wget xfce4-terminal bzip2
CMD ["node","index.js"]
