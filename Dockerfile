FROM python:3.6.4-alpine3.7@sha256:10bd7a59cfac2a784bedd1e6d89887995559f00b61f005a101845ed736bed779
RUN apk add --no-cache git

ENV PIP_DISABLE_PIP_VERSION_CHECK True
ENV PIP_NO_CACHE_DIR False
ENV PYTHONUNBUFFERED True

RUN python -m pip install sphinx-autobuild sphinx_rtd_theme sphinx-version-warning sphinx-multiversion

EXPOSE 8000
WORKDIR /workdir

COPY docs ./docs
RUN ["sphinx-build", "/workdir/docs", "/workdir/_build"]

CMD ["sphinx-autobuild", "-W", "--host", "0.0.0.0", "--port", "8000", "/workdir/docs", "/workdir/_build"]
