FROM keimlink/sphinx-doc:1.7.1

RUN . .venv/bin/activate \
    && python -m pip install sphinx-autobuild sphinx_rtd_theme sphinx-version-warning

EXPOSE 8000

CMD ["sphinx-autobuild", "--host", "0.0.0.0", "--port", "8080", "/docs", "/home/python/_build/html"]