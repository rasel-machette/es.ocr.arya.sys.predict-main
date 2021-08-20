FROM tiangolo/uvicorn-gunicorn:python3.8
WORKDIR /es.ocr.arya.sys.predict
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
COPY / /es.ocr.arya.sys.predict/
RUN ls -la /es.ocr.arya.sys.predict/*
RUN apt update &&  apt install -y sudo tesseract-ocr poppler-utils libxext-dev libsm-dev libxrender-dev
RUN pip3 install virtualenv
RUN virtualenv env -p python3
RUN source /es.ocr.arya.sys.predict/env/bin/activate
RUN pip3 install .
RUN pip3 install -r /es.ocr.arya.sys.predict/requirements.txt
EXPOSE 8000
CMD ["python3", "prediction_http_server.py"]
