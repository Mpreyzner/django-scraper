import django.dispatch

post_saved = django.dispatch.Signal(providing_args=["post"])
