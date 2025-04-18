class FileUploadException(Exception):
    def __init__(self, message="File upload error."):
        super().__init__(message)
