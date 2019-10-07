from disco.types.base import (
    SlottedModel, Field,
    snowflake, text, cached_property,
)


class Emoji(SlottedModel):
    """
    Represents either a standard or custom Discord emoji.

    Attributes
    ----------
    id : snowflake?
        The emoji ID (will be none if this is not a custom emoji).
    name : str
        The name of this emoji.
    animated : bool
        Whether this emoji is animated.
    """
    id = Field(snowflake)
    name = Field(text)
    animated = Field(bool)

    @cached_property
    def custom(self):
        return bool(self.id)

    def __eq__(self, other):
        if isinstance(other, Emoji):
            return self.id == other.id and self.name == other.name
        raise NotImplementedError

    def to_string(self):
        if self.id:
            return '{}:{}'.format(self.name, self.id)
        return self.name
