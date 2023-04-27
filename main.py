'''
Author: dfz
Date: 2023-04-27 22:29:40
LastEditTime: 2023-04-27 22:55:47
LastEditors: dfz
Description: 
FilePath: /mystudy/main.py
Software: vscode
'''

from extensions import CeleryApp,BaseCeleryTask
import celeryconfig 


def create_celeryapp() -> CeleryApp:
    celery_app = CeleryApp(__name__, task_cls=BaseCeleryTask)
    celery_app.config_from_object(celeryconfig)
    celery_app.set_default()
    return celery_app






celery_app = create_celeryapp()