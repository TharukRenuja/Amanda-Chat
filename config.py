from os import environ

ENV = True # make it false for heruko

# List of supported languages >>
# https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages

if not ENV:
  bot_token = "16901971:AAFqdM_SQE1PB2P1xLr67k"
  ARQ_API_KEY = "Get this from @ARQRobot"
  LANGUAGE = "en"
  api_id =  # your api id
  api_hash = "" # your apihash
  # Leave it as it is
  ARQ_API_BASE_URL = "https://thearq.tech"
else:
  bot_token = str(environ.get("bot_token", None))
  ARQ_API_KEY = str(environ.get("ARQ_API_KEY", None))
  LANGUAGE = str(environ.get("LANGUAGE", "en"))
  api_id = int(environ.get("api_id", 6)) # your api id
  api_hash = str(environ.get("api_hash", "eb06d4abfb49dc3eeb1aeb98ae0f581e")) # your apihash
  # Leave it as it is
  ARQ_API_BASE_URL = str(environ.get("ARQ_API_BASE_URL", None))
