class KollieException(Exception):
    """
    Base exception for all Kollie exceptions
    """

    def __init__(self, message, app_name, env_name):
        self.app_name = app_name
        self.env_name = env_name

        super().__init__(message)


class KollieConfigError(KollieException):
    """
    Raised when there is a problem with the Kollie configuration
    """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class KollieImagePolicyException(KollieException):
    """
    Raised when there is a problem with the image policy
    """

    def __init__(self, app_name, env_name):
        super().__init__("ImagePolicyException", app_name, env_name)

    def __str__(self):
        return f"Failed to create ImagePolicy for {self.app_name} in {self.env_name}"


class KollieKustomizationException(KollieException):
    """
    Raised when there is a problem with the kustomization
    """

    def __init__(self, action, app_name, env_name):
        super().__init__("KollieKustomizationException", app_name, env_name)
        self.action = action

    def __str__(self):
        return (
            f"Failed to {self.action} Kustomization "
            f"for {self.app_name} in {self.env_name}"
        )


class CreateCustomObjectsApiException(Exception):
    """
    Raised when there is a problem creating a custom object
    """

    def __init__(self, custom_object, request_body):
        self.custom_object = custom_object
        self.request_body = request_body

        super().__init__(
            f"Failed to create {self.custom_object} custom object"
        )


class GetCustomObjectsApiException(Exception):
    """
    Raised when there is a problem retrieving a custom object
    """

    def __init__(self, custom_object, name):
        self.custom_object = custom_object
        self.name = name

        super().__init__(
            f"Failed to get {self.custom_object} custom object: {self.name}"
        )
