# Copyright © 2023 autosave
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""Used for /phases. """
import hikari
import lightbulb


# Establish the plugin.
phase = lightbulb.Plugin("cogs.phases")
# Quick references for embed colour/flags.
grista = "#207178"
ephemeral = hikari.MessageFlag.EPHEMERAL


@phase.command()
@lightbulb.command("phases", "Phases command group. ")
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def phases(ctx: lightbulb.Context) -> None:
    """Phases Group command."""
    embed = hikari.Embed(
        title="Phases Of A Turn",
        description="When Order is declared, each individual gets two phases on their turn: Act, and Move. Minor tasks like speaking a short phrase, drawing a weapon, or dropping or picking up an object can be done before, during, or after either of these phases on a turn. \n\nA rule or Talent description that prefaces either of these phases with “On” (i.e. On Act..., On Move...) allows individuals to do special things on their turn. Typically, however, individuals will choose one of the options listed below during their phases. No matter which option an individual chooses for a phase, it takes the entire phase to enact.",
        colour=grista,
        url="https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.azas05lu17d9",
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.set_footer(
        text="🔎 Horizon Rulebook | Phases Of A Turn (Page 8: Web Version; Page 4: PDF Version)"
    )
    await ctx.respond(embed=embed)


@phases.child()
@lightbulb.command("act", "Details what can be done On Act. ")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def act(ctx: lightbulb.Context) -> None:
    """The Act subcommand."""
    embed = hikari.Embed(
        title="The Act Phase",
        description="When you Act, you can do one of the following.",
        colour=grista,
        url="https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.azas05lu17d9",
    )
    embed.add_field(
        name="Aim 🎯",
        value="You aim a projectile or thrown weapon at an individual. This is made as a normal attack with the weapon, but only allows you to make 1 attack regardless of the weapon, and skips your Move phase this turn. Aiming a weapon starts that attack at 1 success. ",
        inline=False,
    )
    embed.add_field(
        name="Attack 🤺",
        value="You attack with a weapon. The number of attacks you can make is determined by the weapon, but can be changed by Talents. ",
        inline=False,
    )
    embed.add_field(
        name="Better The Odds 🍀",
        value="You attempt to will fate to allow for another individual’s roll to go better. The way you roleplay this depends on the situation, but allows you to spend your own *Fortune* and give it to another individual. \n\nYou can spend no more than 3 *Fortune* when you Better The Odds, increasing the individual’s current *Fortune* by the same amount. \n\nThis option cannot be used to increase an individual’s Fortune above their maximum, and the individual must be within 6 spaces to benefit from this Act. This Act can be chosen once per player per session. ",
        inline=False,
    )
    embed.add_field(
        name="Disarm 💪",
        value="You attempt to take something from an adjacent individual. Make a contested **Strength** roll against the individual. If you are the victor, the individual drops whatever you were reaching for. \n\nYou may attempt to Disarm with a projectile or thrown weapon from a distance by rolling **Finesse** contested with the individual’s **Strength** instead, so long as they are within the weapon’s range. ",
        inline=False,
    )
    embed.add_field(
        name="Hide 🫥",
        value="You attempt to hide yourself or an object. Roll **Obfuscate**, making a note of the number of successes. An individual looking for you or a hidden object makes a contested **Observe** roll against those successes, noticing you or the object if they are the victor. \n\nYou cannot Hide simply by declaring it. To attempt to Hide, you must have a place to hide yourself or an object, or another means of concealing yourself. ",
        inline=False,
    )
    embed.add_field(
        name="Impose 🛡",
        value="You attempt to defend an adjacent individual. So long as you remain imposing, choosing to do so On Act each turn, the individual gains a benefit when dodging. The individual rolls Dodge as normal when they Dodge, while you roll **Moxie** at the same time. The individual then uses whichever roll (yours or theirs) results in the higher number of successes to Dodge. ",
        inline=False,
    )
    embed.add_field(
        name="Negotiate 🗣",
        value="You attempt to convince an individual to hear you out. Roll **Charm** contested with the individual’s **Observe**. If you are the victor, the individual is more likely to listen to you. The extent of this depends greatly on the situation at hand, along with those involved, and is detailed by your GM. \n\nSucceeding in negotiating does not magically make a foe become a friend, nor drastically change an individual’s ideals, but merely contributes to their willingness to listen. ",
        inline=False,
    )
    embed.add_field(
        name="Use 👏", value="You use an object with special properties. ", inline=False
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.set_footer(
        text="🔎 Horizon Rulebook | Phases Of A Turn (Page 8: Web Version; Page 4: PDF Version)"
    )
    await ctx.respond(embed=embed)


@phases.child()
@lightbulb.command("move", "Details what can be done On Move. ")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def move(ctx: lightbulb.Context) -> None:
    """The Move subcommand."""
    embed = hikari.Embed(
        title="The Move Phase",
        description="You can travel 4 spaces during this phase, or do one of the following. ",
        colour=grista,
        url="https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.azas05lu17d9",
    )
    embed.add_field(
        name="Climb/Swim 🧗‍♀️🏊‍♀️",
        value="You climb a scalable object or swim a number of spaces equal to your **Strength** value. If climbing an especially difficult surface, or swimming in a fast or toxic liquid, your GM may require you to roll **Strength** to swim or climb successfully.",
        inline=False,
    )
    embed.add_field(
        name="Dive 🙇",
        value="You dive below, onto, or behind a surface within a number of spaces equal to half (rounded up) your Move value (typically 2). If you Dive behind a solid object that is larger than you, it becomes more difficult to hit you, granting you +2 to Dodge. If you Dive beneath an opaque liquid, this bonus is instead +1.",
        inline=False,
    )
    embed.add_field(
        name="Jump 💨",
        value="You jump vertically or horizontally a number of spaces equal to your **Strength** value.",
        inline=False,
    )
    embed.add_field(
        name="Saunter 💃",
        value="You travel up to half (rounded up) your Move value, attempting to draw the attention of those nearby. Up to 3 individuals of your choice who can see you make a contested **Observe** roll against your **Charm**. Individuals you are victorious against who Attack On Act next turn must do so against you (if possible). ",
        inline=False,
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.set_footer(
        text="🔎 Horizon Rulebook | Phases Of A Turn (Page 8: Web Version; Page 4: PDF Version)"
    )
    await ctx.respond(embed=embed)


# Load the plugin.
def load(bot):
    bot.add_plugin(phase)


# Unload the plugin.
def unload(bot):
    bot.remove_plugin(phase)
