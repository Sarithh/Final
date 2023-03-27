from pydantic import BaseSettings

class Settings(BaseSettings):
  app_name: str = "Awesome API"
  username: str = None
  password: str = None
  host: str = None
   
  class Config:
    env_file = ".env"

settings = Settings()