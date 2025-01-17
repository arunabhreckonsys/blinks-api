# import os
#
# from opentelemetry import trace
# from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
# from opentelemetry.sdk.resources import Resource
# from opentelemetry.sdk.trace import TracerProvider
# from opentelemetry.sdk.trace.export import BatchSpanProcessor
#
#
# def post_fork(server, worker):
#     server.log.info("Worker spawned (pid: %s)", worker.pid)
#
#     resource = Resource.create(attributes={
#         "service.name": "blinks-api"
#     })
#
#     trace.set_tracer_provider(TracerProvider(resource=resource))
#     span_processor = BatchSpanProcessor(
#         OTLPSpanExporter(endpoint=os.environ.get('OTEL_EXPORTER_OTLP_ENDPOINT'))
#     )
#     trace.get_tracer_provider().add_span_processor(span_processor)
#
#
# def post_fork(server, worker):
#     server.log.info("Worker spawned (pid: %s)", worker.pid)
#     configure_opentelemetry()

# from gevent import monkey
#
# monkey.patch_all(thread=False, ssl=False)