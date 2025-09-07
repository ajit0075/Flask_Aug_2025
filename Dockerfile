FROM python:3.13.5-slim-bullseye
WORKDIR /mydocker

# install the application dependences 
COPY requirement.txt ./
RUN pip install -r requirement.txt

# copy all the folder from my system to docker 

COPY . .

#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["python3", "-m","flask","--app" , "loan","run", "0.0.0.0", "--port", "8000"]

