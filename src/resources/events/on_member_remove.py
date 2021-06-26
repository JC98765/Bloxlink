from ..structures.Bloxlink import Bloxlink # pylint: disable=import-error
from ..constants import DEFAULTS # pylint: disable=import-error
from ..exceptions import UserNotVerified, RobloxDown, RobloxAPIError # pylint: disable=import-error
import discord

get_guild_value = Bloxlink.get_module("cache", attrs=["get_guild_value"])
guild_obligations = Bloxlink.get_module("roblox", attrs=["guild_obligations"])


@Bloxlink.module
class MemberRemoveEvent(Bloxlink.Module):
    def __init__(self):
        pass

    async def __setup__(self):

        @Bloxlink.event
        async def on_member_remove(member):
            await guild_obligations(member, member.guild, join=False, event=True)
