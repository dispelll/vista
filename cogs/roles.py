# Copyright © 2023 autosave
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""Used for /roles. """
import hikari
import lightbulb


# Establish the plugin.
role = lightbulb.Plugin("cogs.roles")
# Quick references for embed colour/flags.
grista = "#207178"
ephemeral = hikari.MessageFlag.EPHEMERAL


@role.command()
@lightbulb.command("roles", "Details Role options for Horizon! ")
@lightbulb.implements(lightbulb.SlashCommand)
async def roles(ctx: lightbulb.Context) -> None:
    """/Roles command."""
    embed = hikari.Embed(
        title="Roles (Optional)",
        description="You have the following options if aligning with a Role. ",
        colour=grista,
        url="https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.vz7jqag2ql1z",
    )
    embed.add_field(
        name="Boxer",
        value="**Fast, Pugilist, Bob & Weave, Parry, Hit Me** \nThe Boxer Role usually represents a fisticuffs- or martial-arts wielding brawler. This Role is focused on melee combat.",
        inline=False,
    )
    embed.add_field(
        name="Brainiac",
        value="**Elementary, Glyphs, Diplomat, Craft, Focus** \nThe Brainiac Role usually represents a knowledge-seeking intellectual. This Role is focused on gaining information, crafting, and communication. ",
        inline=False,
    )
    embed.add_field(
        name="Covert",
        value="**Hidden Steps, I See You, Climber/Swimmer, I Am The Night, Sniper** \nThe Covert Role usually represents a character that prefers to sneak and keep their distance during conflict. This Role is focused on stealth and inflicting Hurt from a distance. ",
        inline=False,
    )
    embed.add_field(
        name="Dancer",
        value="**I Can't Turn It Off, Agile, Not Today, Can't Touch This/Sonic Speed, Stay Close** \nThe Dancer Role usually represents an agile and elusive support character. This Role is focused on distraction, Hurt avoidance, and healing. ",
        inline=False,
    )
    embed.add_field(
        name="Face",
        value="**Charming, Watch This, Cunning Not Smarts, Catchphrase!, Truthseer** \nThe Face Role usually represents a charming and cunning character. This Role is focused on charismatic roleplay interactions and support. ",
        inline=False,
    )
    embed.add_field(
        name="Medic",
        value="**Healer, Support Beacon, Not Today, Sonic Speed, Stay Close** \nThe Medic Role usually represents a support and healing character. This Role is focused on restoring Life and keeping the party alive. ",
        inline=False,
    )
    embed.add_field(
        name="Soothsayer",
        value="**Observant, Portent, Fate Weaver, Guiding Influence/'Tis The Will Not The Way, Desperate Times** \nThe Soothsayer Role usually represents a character that molds the world to their will. This Role is focused on the Fortune resource and reality manipulation. ",
        inline=False,
    )
    embed.add_field(
        name="Warden",
        value="**Tank, Get Behind Me, Can't Touch This/Parry/Sonic Speed, Hit Me/Stay Close/Where Are You Going** \nThe Warden Role usually represents a character that protects others in combat. This Role is focused on defense and survival, depending on how you build it. ",
        inline=False,
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.set_footer(
        text="🔎 Horizon Rulebook | Roles (Page 35: Web Version; Page 19: PDF Version)"
    )
    await ctx.respond(embed=embed)


# Load the plugin.
def load(bot):
    bot.add_plugin(role)


# Unload the plugin.
def unload(bot):
    bot.remove_plugin(role)
