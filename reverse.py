__version__ = (0,0,2)
#meta developer: skil3, lite, endy
from .. import loader, utils
from telethon.tl.types import Message
import logging

logger = logging.getLogger(__name__)

def get_reply_message(message: Message) -> str:
    if not (message := getattr(message, "message", message)):
        return False
    if len(args := message.split(maxsplit=1)) > 1:
        return args[0]+" "+args[1]
    return ""

class ReverseTextMod(loader.Module):
	strings = {
		"name": "Reverse",
	}
	def __init__(self):
		self.config = loader.ModuleConfig(
			loader.ConfigValue(
				"encoding",
				"none",
				lambda: "code, u, em, del это варианты вида текста, введите одно из них и увидите результат. 'none' что бы убрать кодировку",
				validator=loader.validators.Choice(["code", "u", "em", "del", "none"]),
				),
			)

	async def revcmd(self, message: Message):
		reply = await message.get_reply_message()
		try:
			args = get_reply_message(reply)
			rev = list(args)
			rev.reverse()
			await utils.answer(message, f'{"".join(rev)}')
		except TypeError:
			args = utils.get_args_raw(message)
			rev = list(args)
			rev.reverse()
			await utils.answer(message, f'{"".join(rev)}')
