from django.urls import include, path

from .data_sync import urls as data_sync_urls
from .export import urls as export_urls
from .fields import urls as field_urls
from .formula import urls as formula_urls
from .rows import urls as row_urls
from .tables import urls as table_urls
from .tokens import urls as token_urls
from .views import urls as view_urls
from .webhooks import urls as webhook_urls
from baserow.contrib.database.api.commerce_api import (
    create_order_or_subscription, stripe_webhook, paypal_webhook
)

app_name = "baserow.contrib.database.api"

urlpatterns = [
    path("tables/", include(table_urls, namespace="tables")),
    path("views/", include(view_urls, namespace="views")),
    path("fields/", include(field_urls, namespace="fields")),
    path("webhooks/", include(webhook_urls, namespace="webhooks")),
    path("rows/", include(row_urls, namespace="rows")),
    path("tokens/", include(token_urls, namespace="tokens")),
    path("export/", include(export_urls, namespace="export")),
    path("formula/", include(formula_urls, namespace="formula")),
    path("data-sync/", include(data_sync_urls, namespace="data_sync")),
    path('commerce/order/', create_order_or_subscription, name='create_order_or_subscription'),
    path('commerce/webhook/stripe/', stripe_webhook, name='stripe_webhook'),
    path('commerce/webhook/paypal/', paypal_webhook, name='paypal_webhook'),
]
