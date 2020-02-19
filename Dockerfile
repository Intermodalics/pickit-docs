FROM keimlink/sphinx-doc:1.7.1

RUN . .venv/bin/activate \
    && python -m pip install sphinx-autobuild sphinx_rtd_theme

EXPOSE 8080

COPY docs docs
RUN /home/python/.venv/bin/sphinx-build docs dist
WORKDIR /home/python/dist

CMD ["sphinx-autobuild", "-W", "--host", "0.0.0.0", "--port", "8080", "/home/python/docs", "/home/python/dist"]
