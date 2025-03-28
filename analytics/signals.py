from django.dispatch import Signal

# object_viewed_signal = Signal(providing_args=['instance','request'])(here providing args has been deprecated)
object_viewed_signal = Signal()
