###############################first iteration###############################

# FROM python:3.9

# RUN pip install pandas

# ENTRYPOINT [ "bash" ]

###############################second iteration###############################

FROM python:3.9

RUN pip install pandas

# create a directory called app
WORKDIR /app 

# copy the pipeline.py file from the current directory to the app directory in the container (target)
COPY pipeline.py pipeline.py

ENTRYPOINT [ "bash" ]