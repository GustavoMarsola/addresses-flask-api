from flask import Flask

from src.settings import get_settings
from src.controllers.routes.v1 import v1
from src.controllers.routes.health_check import router as health_check

if get_settings().server_settings.environment in ['test', 'local', 'dev']:
	from src.logs.settings import printing_log, log_config, custom_print
	log_config()
	custom_print()
	printing_log()

def create_app():
	app = Flask(__name__)
	app.register_blueprint(health_check)
	app.register_blueprint(v1)
	
	return app

def run_app():
	_app = create_app()
	_run_app = _app.run(host  = get_settings().server_settings.host, 
						port  = get_settings().server_settings.port,
						debug = get_settings().server_settings.debug)
	
	return _run_app
