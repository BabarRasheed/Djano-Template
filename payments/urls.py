# urls.py

from django.urls import path
# from .views import PaymentView, payment_success
from .views import SuccessView, CancelView, ProductLandingPageView, CreateCheckoutSessionView, stripe_webhook, StripeIntentView

urlpatterns = [
    # path('payment/', PaymentView.as_view(), name='payment'),
    # path('success/', payment_success, name='payment_success'),
    path('create-payment-intent/<pk>/', StripeIntentView.as_view(), name='create-payment-intent'),
    path('webhooks/stripe/', stripe_webhook, name='stripe-webhook'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('landing/', ProductLandingPageView.as_view(), name='landing-page'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session')
]
