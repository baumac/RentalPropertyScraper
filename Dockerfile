FROM python:3.8-buster

WORKDIR /usr/src/app

RUN apt-get update && apt-get -y upgrade && apt-get -y install curl

RUN apt-get install -y wget xvfb unzip

# Set up the Chrome PPA
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list

RUN apt-get update && apt-get install -y google-chrome-stable

RUN export version=$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE); wget -q "https://chromedriver.storage.googleapis.com/${version}/chromedriver_linux64.zip"
RUN unzip chromedriver_linux64.zip
RUN mv chromedriver /usr/bin/chromedriver

RUN apt-get update && apt-get install -yq libgconf-2-4

COPY ./ ./

RUN chmod +x ./entrypoint.sh
RUN chmod +x ./main.py

RUN pip install -r requirements.txt

ENTRYPOINT ["./entrypoint.sh"]