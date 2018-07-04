from .handler import Handler


class DeletedMessagesHandler(Handler):
    """The deleted Messages handler class. Used to handle deleted messages coming from any chat
    (private, group, channel). It is intended to be used with
    :meth:`add_handler() <pyrogram.Client.add_handler>`
    For a nicer way to register this handler, have a look at the
    :meth:`on_deleted_messages() <pyrogram.Client.on_deleted_messages>` decorator.
    Args:
        callback (``callable``):
            Pass a function that will be called when one or more Messages have been deleted.
            It takes *(client, messages)* as positional arguments (look at the section below for a detailed description).
        filters (:obj:`Filters <pyrogram.Filters>`):
            Pass one or more filters to allow only a subset of messages to be passed
            in your callback function.
    Other parameters:
        client (:obj:`Client <pyrogram.Client>`):
            The Client itself, useful when you want to call other API methods inside the message handler.
        messages (:obj:`Messages <pyrogram.Messages>`):
            The deleted messages.
    """

    def __init__(self, callback: callable, filters=None):
        super().__init__(callback, filters)

    def check(self, messages):
        return (
            self.filters(messages.messages[0])
            if self.filters
            else True
        )
