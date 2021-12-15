class UnsuportedOperationException(Exception):
    pass


def get_type_name(variable: any) -> str:
    """get the `name` of the `type` of your variable"""
    return type(variable).__name__
