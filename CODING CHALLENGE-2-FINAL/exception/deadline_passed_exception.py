class DeadlinePassedException(Exception):
    def __init__(self, message="Application deadline has passed."):
        super().__init__(message)
