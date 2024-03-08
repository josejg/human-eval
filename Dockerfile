# docker run -v $(pwd):/app -w /app python:latest
FROM python:latest
RUN pip install git+https://github.com/josejg/human-eval@deduplicate
WORKDIR /app
ENTRYPOINT python -m human_eval.evaluate_functional_correctness /app/samples.jsonl
# docker build -t human-eval .
