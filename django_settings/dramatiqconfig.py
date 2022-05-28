from dramatiq.middleware import Prometheus
from dramatiq.results import Results
from dramatiq.results.backends import RedisBackend
from dramatiq.brokers.redis import RedisBroker
from django.conf import settings

from django_settings.middlewares import PatchedPrometheus


broker = RedisBroker(
    host=settings.REDIS_HOST, port=settings.REDIS_PORT,
    db=settings.REDIS_DB, password=settings.REDIS_PASSWORD
)

backend = RedisBackend(client=broker.client)

# Middlewares
broker.middleware = list(filter(lambda x: not isinstance(x, Prometheus),
                                broker.middleware))
broker.middleware.insert(0, PatchedPrometheus())
broker.add_middleware(Results(backend=backend))
