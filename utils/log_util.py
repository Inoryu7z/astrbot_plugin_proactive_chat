"""精简日志控制模块。"""
from __future__ import annotations

from astrbot.api import logger as ast_logger

_verbose_enabled = False


def set_verbose(enabled: bool) -> None:
    global _verbose_enabled
    _verbose_enabled = enabled


class PluginLogger:
    def verbose(self, msg, *args, **kwargs):
        """非 debug_mode 时降级为 debug，仅 debug_mode 开启时以 info 输出。"""
        if _verbose_enabled:
            ast_logger.info(msg, *args, **kwargs)
        else:
            ast_logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        ast_logger.info(msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        ast_logger.debug(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        ast_logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        ast_logger.error(msg, *args, **kwargs)


plog = PluginLogger()