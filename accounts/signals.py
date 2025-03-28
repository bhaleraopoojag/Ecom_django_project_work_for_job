from django.dispatch import Signal

# object_viewed_signal = Signal(providing_args=['instance','request'])(here providing args has been deprecated)
# user_logged_in = Signal(providing_args=['instance','request'])

user_logged_in = Signal()
