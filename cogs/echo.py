# Copyright © 2023 autosave
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""Used for /echo. """
import hikari
import lightbulb


# Establish the plugin.
echoes = lightbulb.Plugin("cogs.echo")
# Quick references for embed colour/flags.
grista = "#207178"
ephemeral = hikari.MessageFlag.EPHEMERAL


@echoes.command()
@lightbulb.command("echo", "Details the Echo optional rule in Horizon! ")
@lightbulb.implements(lightbulb.SlashCommand)
async def echo(ctx: lightbulb.Context) -> None:
    """Echo command."""
    embed = hikari.Embed(
        title="Echo (Optional)",
        description="An optional rule, Echo is a mechanic that allows individuals to save a roll for future use. Once per in-game day, when an individual makes an attribute roll that resulted in at least 2 successes and that no *Fortune* was spent on, they can choose to Echo it. When an individual Echoes a role, they replace the number of successes it resulted in with 0, making a note of the number of successes that were replaced. \n\nUntil the end of the in-game day the roll was echoed on, the individual can change one future roll they make with the amount of successes of the one that was echoed. \n\nFor example, a player negotiating with an NPC rolls **Charm**, and gets 5 successes. The player decides that they would rather save those successes for something more important, and chooses to Echo it. The player replaces their 5 successes with 0, failing to negotiate with the NPC, and makes a note that they have an Echoed roll of 5 successes for the remainder of the day. That night, the player fails another roll with only 2 successes, and opts to swap it with their Echoed roll. ",
        colour=grista,
        url="https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.vqovswl0d5j8",
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.set_footer(
        text="🔎 Horizon Rulebook | Echo (Optional) (Page 22: Web Version; Page 12: PDF Version)"
    )
    await ctx.respond(embed=embed)


# Load the plugin.
def load(bot):
    bot.add_plugin(echoes)


# Unload the plugin.
def unload(bot):
    bot.remove_plugin(echoes)
