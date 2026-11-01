import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    filename="demo.log",
    encoding="utf-8",
)

logger = logging.getLogger(__name__)

logger.debug("调试细节：只有排查问题时看")
logger.info("正常流程")
logger.warning("有点不对劲")
logger.error("出错了")