from django.db import models

# Create your models here.
class Quest(models.Model):
    CHOICE_STATUS = (
        (0, '启用'),
        (1, '弃用'),
        (2, '测试'),
    )
    CHOICE_LEVEL = (
        (0, '日常'),
        (1, '周常'),
        (2, '月常'),
        (3, '季常'),
    )
    name = models.CharField(max_length=50, verbose_name='任务名称')
    status = models.IntegerField(choices=CHOICE_STATUS, default=0, verbose_name='任务状态')
    level = models.IntegerField(choices=CHOICE_LEVEL, default=0, verbose_name='任务等级')
    remark = models.CharField(max_length=50, verbose_name='任务备注')
    description = models.CharField(max_length=50, verbose_name='任务描述')
    award=models.CharField(max_length=50,verbose_name='任务奖励')

    class Meta:
        verbose_name = '任务'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

