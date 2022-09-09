import imp
from importlib import import_module,reload
from django.core.management.base import BaseCommand, CommandError
import time

class Command(BaseCommand):
    help = '启动任务界面'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=str)

    def handle(self, *args, **options):  

       self.stdout.write(self.style.HTTP_INFO("启动任务界面"))

       from myquest.qt_frames import QuestWindow
       windows=QuestWindow("任务")
       windows.run()

