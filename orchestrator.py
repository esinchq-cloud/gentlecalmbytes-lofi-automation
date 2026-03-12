import importlib

def load_channel(channel_name):
    """
    Dynamically loads a channel module.
    Tries upload.py first, then post.py.
    """
    try:
        return importlib.import_module(f"channels.{channel_name}.upload")
    except ModuleNotFoundError:
        try:
            return importlib.import_module(f"channels.{channel_name}.post")
        except ModuleNotFoundError:
            raise ValueError(f"Channel '{channel_name}' not found or missing upload/post file.")

def dispatch(channel, action, **kwargs):
    """
    Calls the correct function inside the channel module.
    Example: dispatch('twitter', 'post', text='Hello')
    """
    module = load_channel(channel)

    if not hasattr(module, action):
        raise ValueError(f"Action '{action}' not found in channel '{channel}'.")

    func = getattr(module, action)
    return func(**kwargs)
