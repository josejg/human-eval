FROM python:latest
COPY . /human_eval
RUN pip install /human_eval
WORKDIR /app
ENTRYPOINT python -m human_eval.evaluate_functional_correctness /app/samples.jsonl
# docker build -t human-eval .
# docker run -v $(pwd):/app human-eval:latest
