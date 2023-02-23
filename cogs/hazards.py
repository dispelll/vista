# Copyright © 2023 autosave
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""Used for /hazards. """
import hikari
import lightbulb


# Establish the plugin.
hazard = lightbulb.Plugin("cogs.hazards")
# Quick references for embed colour/flags.
grista = "#207178"
ephemeral = hikari.MessageFlag.EPHEMERAL


@hazard.command()
@lightbulb.command("hazards", "Details Hazards in Horizon! ")
@lightbulb.implements(lightbulb.SlashCommand)
async def hazards(ctx: lightbulb.Context) -> None:
    """Hazards command."""
    embed = hikari.Embed(
        title="Hazards",
        description="Sometimes, individuals encounter obstacles hazardous to them. How this occurs mechanically depends on the situation. See some examples below.",
        colour=grista,
        url="https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.e7nnwxvb03w4",
    )
    embed.add_field(
        name="Drowning",
        value="An individual can hold their breath a number of minutes equal to their **Moxie** value. Should an individual exceed this time, they are inflicted 1D6 Hurt each turn until they are able to breathe freely once more. ",
        inline=False,
    )
    embed.add_field(
        name="Poison",
        value="An individual that is exposed to poison rolls **Moxie**, requiring a number of successes based on the strength of the poison (as determined by the GM). Should the individual fail the roll, they are inflicted 1D6 Hurt per the number of successes they failed by. \n\nFor example, if Twyla was shot with a poison arrow, their GM may tell them to roll **Moxie** on their turn. The GM states that Twyla needs 5 successes, as this is a strong poison. Twyla rolls, but gets only 1 success, so is inflicted 4 Hurt from the poison. ",
        inline=False,
    )
    embed.add_field(
        name="Sensory Deprivation",
        value="When surrounded by an effect that obscures the senses, players have Contextual modifiers to certain attribute rolls. The GM decides the extent of these modifiers, but standard examples include: partial darkness/fog (-2 to **Observe**), total darkness (-3 to **Observe** and **Finesse**, +1 to **Obfuscate**), and sensory overload (-3 to all attributes). ",
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.set_footer(
        text="🔎 Horizon Rulebook | Hazards (Page 21: Web Version; Page 12: PDF Version)"
    )
    await ctx.respond(embed=embed)


# Load the plugin.
def load(bot):
    bot.add_plugin(hazard)


# Unload the plugin.
def unload(bot):
    bot.remove_plugin(hazard)
