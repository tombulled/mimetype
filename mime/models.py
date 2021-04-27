import pydantic

import typing

from . import enums

class BaseModel(pydantic.BaseModel): pass

class MimeType(BaseModel):
    type:       enums.MediaType
    subtype:    enums.MediaSubtype
    suffix:     typing.Optional[enums.MediaSuffix]
    parameters: typing.Optional[typing.Dict[str, str]]

    def __str__(self, suffix = True, parameters = True) -> str:
        return ''.join \
        (
            (
                f'{self.type}/',
                f'{self.subtype}',
                f'+{self.suffix}' if suffix and self.suffix else '',
                '; ' if parameters and self.parameters else '',
                '; '.join \
                (
                    f'{key}="{value}"'
                    for key, value in self.parameters.items()
                ) if parameters and self.parameters else '',
            ),
        )
