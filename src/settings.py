import os
from pathlib           import Path
from functools         import lru_cache
from pydantic          import Field
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    environment: str = Field("api-brazilian-addresses", validation_alias='ENVIRONMENT')
    app:         str = Field("development", validation_alias='APP')

    @property
    def app_name(self) -> str:
        return f"{self.environment}.{self.app}"


class LoggingSettings(BaseSettings):
    log_format_datetime:    str = Field('%Y-%m-%d %H:%M:%S', validation_alias='LOG_FORMAT_DATETIME')
    log_level:              str = Field('INFO', validation_alias='LOG_LEVEL')


class DatabaseSettings(BaseSettings):
    database_pool_size:             int = Field(20, env='DATABASE_POOL_SIZE')
    database_pool_timeout_seconds:  int = Field(2, env='DATABASE_POOL_TIMEOUT_SECONDS')
    database_max_overflow:          int = Field(50, env='DATABASE_MAX_OVERFLOW')
    database_pool_recicle_seconds:  int = Field(3600, env='DATABASE_POOL_RECICLE_SECONDS')
    database_echo_sql_option:       str = Field(None, env='DATABASE_ECHO_SQL')
    database_port:                  int = Field(5432, env='DATABASE_PORT')
    database_page_size:             int = Field(1, env='PAGE_SIZE')
    
    database_project_root: Path = Path(__file__).resolve().parent.parent
    database_project_path: str  = "src/database/api-brazilian-addresses.db"

    @property
    def database_uri(self):
        return f'sqlite:///{os.path.join(self.database_project_root, self.database_project_path)}'


class GeneralSettings:
    app_settings      = AppSettings()
    logging_settings  = LoggingSettings()    
    database_settings = DatabaseSettings()


@lru_cache
def get_settings() -> GeneralSettings:
    return GeneralSettings()