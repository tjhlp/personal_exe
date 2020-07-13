# -*- coding: utf-8 -*-
# File              : models.py
# Author            : tjh
# Create Date       : 2020/07/02
# Last Modified Date: 2020/07/02
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************


class ModelInfo(models.Model):
    model_id = models.CharField("模型id", max_length=36)  # uuid
    model_name = models.CharField("模型名称", max_length=30)
    user_node = models.ForeignKey(
        Node, on_delete=models.CASCADE, related_name="model_user", verbose_name="模型使用方"
    )
    provider_node = models.ForeignKey(
        Node,
        on_delete=models.SET_NULL,
        related_name="model_provider",
        null=True,
        verbose_name="数据提供方",
    )
    config = models.TextField("模型配置")

    objects = models.Manager()

    def _get_config(self):
        """
        获取 config 的数据进行解密后返回
        :return: 解密后，字符串转回json
        """
        if self.config:
            return loads(rsa_decrypt(self.config), encoding="utf-8")
        else:
            return None

    def _set_config(self, config):
        """
        设置 config 的值
        :return: json转字符串，加密后存储
        """
        self.config = rsa_encrypt(dumps(config, ensure_ascii=False))

    model_config = property(_get_config, _set_config)

    class Meta:
        verbose_name = "模型"
        verbose_name_plural = "模型管理表"
        ordering = ["id"]

    def __str__(self):
        return self.model_id