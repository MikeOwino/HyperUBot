# My imports
from tg_userbot import HELP_DICT
from tg_userbot.include.watcher import watcher
from tg_userbot.include.language_processor import HelpText as msgRep

@watcher(outgoing=True, pattern=r"^\.help(?: |$)(.*)")
async def help(event):
    args = event.pattern_match.group(1) # Get specific module
    if args:
        if args in HELP_DICT:
            await event.edit(str(HELP_DICT[args]))
        else:
            await event.edit(msgRep.INVALID_NAME)
    else:
        string = msgRep.DEFAULT
        for i in HELP_DICT:
            string += "-> `" + str(i)
            string += "`\n"
        await event.edit(string)