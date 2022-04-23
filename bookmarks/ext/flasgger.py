from flasgger import (
    Swagger
)
from bookmarks.docs import (
    swagger_config,
    template
)


def init_app(app):
    Swagger(app, config=swagger_config, template=template)
