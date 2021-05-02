# set base image (host OS)
FROM python:3.9.4-alpine3.13

# set the working directory in the container
WORKDIR /code

# copy the content of the local src directory to the working directory
COPY src/ .

# Install requirements for building multidict
RUN apk add gcc musl-dev

# install dependencies
RUN pip install -r requirements.txt

# command to run on container start
CMD [ "python", "./bot.py" ]

