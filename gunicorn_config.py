command = '/usr/html/MVK_Apps/env/bin/gunicorn'
pythonpath = '/usr/html/MVK_Apps/MVK_Apps'
bind = '127.0.0.1:8001'
workers =9
user = 'ipcamer'
limit_request_fieds = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=MVK_Apps.settings'
