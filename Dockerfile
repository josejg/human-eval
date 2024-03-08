FROM python:latest
RUN pip install git+https://github.com/josejg/human-eval
WORKDIR /app
ENTRYPOINT python -m human_eval.evaluate_functional_correctness /app/samples.jsonl
# docker build -t human-eval .
# docker run -v $(pwd):/app human-eval:latest
