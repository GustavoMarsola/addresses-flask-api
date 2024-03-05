from src.main import app
from src.settings import get_settings



app.run(host=get_settings().app_settings.host,
        port=get_settings().app_settings.port,
        debug=True)

