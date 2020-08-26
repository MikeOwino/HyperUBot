# My stuff
from tg_userbot.include.language_processor import GitHubText as msgRep, HelpDesignations as helpRep
import tg_userbot.include.git_api as api
from tg_userbot import tgclient, HELP_DICT

# Telethon stuff
from telethon.events import NewMessage


def getData(url, index):
    if not api.getData(url):
        return msgRep.INVALID_URL
    recentRelease = api.getReleaseData(api.getData(url), index)
    if recentRelease is None:
        return msgRep.NO_RELEASE
    author = api.getAuthor(recentRelease)
    authorUrl = api.getAuthorUrl(recentRelease)
    assets = api.getAssets(recentRelease)
    releaseName = api.getReleaseName(recentRelease)
    message = msgRep.AUTHOR_STR.format(authorUrl, author)
    message += msgRep.RELEASE_NAME + releaseName + "\n\n"
    for asset in assets:
        message += msgRep.ASSET
        fileName = api.getReleaseFileName(asset)
        fileURL = api.getReleaseFileURL(asset)
        assetFile = "<a href='{}'>{}</a>".format(fileURL, fileName)
        sizeB = ((api.getSize(asset)) / 1024) / 1024
        size = "{0:.2f}".format(sizeB)
        downloadCount = api.getDownloadCount(asset)
        message += assetFile + "\n"
        message += msgRep.SIZE + size + " MB"
        message += msgRep.DL_COUNT + str(downloadCount) + "\n\n"
    return message


@tgclient.on(NewMessage(pattern=r"^\.git(?: |$)(.*)", outgoing=True))
async def get_release(event):
    commandArgs = event.text.split(" ")
    if len(commandArgs) != 2 or not "/" in commandArgs[1]:
        await event.edit(msgRep.INVALID_ARGS)
        return
    index = 0  # later will support going back in time!
    url = commandArgs[1]
    text = getData(url, index)
    await event.edit(text, parse_mode="html")
    return


HELP_DICT.update({"github":helpRep.GITHUB_HELP})