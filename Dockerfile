FROM python:3.14.0rc2-alpine3.22

COPY main.py .

RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install --upgrade Pillow

ENV  AM_I_IN_A_DOCKER_CONTAINER="YES"

ENTRYPOINT ["python", "main.py"]

CMD ["--help"]
