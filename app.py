from src.main import _app
from src.settings import get_settings



_app.run(host=get_settings().app_settings.host,
        port=get_settings().app_settings.port,
        debug=True)

