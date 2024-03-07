import os

from pathlib           import Path
from functools         import lru_cache
from pydantic          import Field
from pydantic_settings import BaseSettings
from sqlalchemy.engine.url import URL


class ServerSettings(BaseSettings):
	environment: str  = Field('dev', validation_alias='ENVIRONMENT')
	app:         str  = Field('api-brazilian-addresses', validation_alias='APP')
	host:        str  = Field('localhost', validation_alias='APP_HOST')
	port:        str  = Field('5000', validation_alias='APP_PORT')
	debug:       bool = Field(True, validation_alias='DEBUG')

	@property
	def app_name(self) -> str:
		return f"{self.environment}.{self.app}"


class LoggingSettings(BaseSettings):
	log_format_datetime:    str = Field('%Y-%m-%d %H:%M:%S', validation_alias='LOG_FORMAT_DATETIME')
	log_level:              str = Field('INFO', validation_alias='LOG_LEVEL')


class DatabaseSettings(BaseSettings):
	database_autoflush:             bool = Field(False, validation_alias='DATABASE_AUTOFLUSH')
	database_autocommit:            bool = Field(False, validation_alias='DATABASE_COMMIT')
	database_expire_on_commit:      bool = Field(False, validation_alias='DATABASE_EXPIRE_ON_COMMIT')
	database_future:                bool = Field(True, validation_alias='DATABASE_FUTURE')

	database_pool_size:             int = Field(20, validation_alias='DATABASE_POOL_SIZE')
	database_pool_timeout_seconds:  int = Field(2, validation_alias='DATABASE_POOL_TIMEOUT_SECONDS')
	database_max_overflow:          int = Field(50, validation_alias='DATABASE_MAX_OVERFLOW')
	database_pool_recicle_seconds:  int = Field(3600, validation_alias='DATABASE_POOL_RECICLE_SECONDS')
	database_echo_sql_option:       bool = Field(False, validation_alias='DATABASE_ECHO_SQL')
	database_port:                  int = Field(5432, validation_alias='DATABASE_PORT')
	database_page_size:             int = Field(1, validation_alias='PAGE_SIZE')
	
	database_username: str = Field('postgres', env='DATABASE_USERNAME')
	database_password: str = Field('postgres', env='DATABASE_PASSWORD')
	database_host:     str = Field('localhost', env='DATABASE_HOST')
	database_port:     int = Field(5432, env='DATABASE_PORT')
	database_name:     str = Field('postgres', env='DATABASE_NAME')
	database_driver:   str = Field('postgresql+psycopg2', env='DATABASE_DRIVER')

	database_project_root: Path = Path(__file__).resolve().parent.parent
	database_project_path: str  = r"src\database\api-brazilian-addresses.db"


	@property
	def database_uri(self) -> URL:
		return URL.create(
			drivername=self.database_driver,
			username=self.database_username,
			password=self.database_password,
			host=self.database_host,
			port=self.database_port,
			database=self.database_name
		)
	

	@property
	def testing_database_uri(self):
		return f'sqlite:///{os.path.join(self.database_project_root, self.database_project_path)}'


class GeneralSettings:
	server_settings   = ServerSettings()
	logging_settings  = LoggingSettings()    
	database_settings = DatabaseSettings()


@lru_cache
def get_settings() -> GeneralSettings:
	return GeneralSettings()