from prometheus_client import Counter, Histogram

error_counter = Counter('app_errors_total', 'Total errors encountered')
ocr_latency = Histogram('ocr_latency_seconds', 'OCR processing latency')
llm_latency = Histogram('llm_latency_seconds', 'LLM reasoning latency')
