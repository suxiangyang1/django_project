from django.db import models
# 导入内建的User模型
from django.contrib.auth.models import User
# timezone 用于处理时间相关事务
from django.utils import timezone


# 博客文章类型
class ArticlePost(models.Model):
    # 文章 作者。 参数on_delete 用于指定数据删除的方式
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # 文章标题。 models.CharField 为字符串字段, 用于保存较短的字符串, 比如标题
    title = models.CharField(max_length=100)

    # 文章正文保存大量文本使用 TextField
    body = models.TextField()

    # 文章创建时间。 参数 default=timezone.now 指定其在创建数据时将默认写入当前的时间
    created = models.DateTimeField(default=timezone.now)

    # 文章更新时间. 参数 auto_now = True 指定每次数据更新时自动写入当前时间
    updated = models.DateTimeField(auto_now=True)

    # 内部类 class Meta 用于给model 定义元数据
    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        # '-created' 表面数据应该以倒序的排列
        # ordering 是元组, 括号中只含一个元素时不要忘记末尾的逗号
        ordering = ('-created',)

    # 函数__str__ 定义当前对象的str() 方法时的返回值内容
    def __str__(self):
        # return self.title 将文章标题返回
        return self.title


