# Copyright © 2023 autosave
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""Used for /talents. """
import hikari
import lightbulb


# Establish the plugin.
talent = lightbulb.Plugin("cogs.talents")
# Quick references for embed colour/flags.
grista = "#207178"
ephemeral = hikari.MessageFlag.EPHEMERAL


@talent.command()
@lightbulb.command("talents", "Talents command group. ")
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def talents(ctx: lightbulb.Context) -> None:
    """Talents command group."""
    embed = hikari.Embed(
        title="Talents",
        description="You gain one Talent per Tier. You can choose the Talents yourself, or align with a Role (a preset selection of Talents). Talents grow in strength as you do, and are separated by Tier. If your character is Tier 1, choose one Tier 1 Talent. If they are Tier 2, choose one Tier 1 Talent and one Tier 2 Talent, and so on. \n\nTalents cannot be changed once chosen, but aligning with a Role doesn’t mean you can’t deviate from that Role’s Talents later. If your Talent has a Contextual modifier, tick the Contextual box. If it has an Eternal modifier, tick the Eternal box. Your Talent tells you which modifiers it has. See [Modifiers](https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.ua74dox36vlf) for more information. ",
        color=grista,
        url="https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.quxd8c66uhju",
    )
    embed.add_field(
        name="Look Up Talents & Roles",
        value="Use `/talents tier_1`, `/talents tier_2`, `/talents tier 3`, `/talents tier_4`, and `/talents tier_5` to look up Talents by Tier. You can also use `/roles` to get a list of Roles available to players. ",
        inline=False,
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.set_footer(
        text="🔎 Horizon Rulebook | Pages 3 & 4: The Conflict Pages  (Page 28: Web Version; Page 16: PDF Version)"
    )
    await ctx.respond(embed=embed)


@talents.child()
@lightbulb.command("tier_1", "Details the options for Tier 1 Talents. ")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def tier1(ctx: lightbulb.Context) -> None:
    """Tier 1 Talents subcommand."""
    embed = hikari.Embed(
        title="Tier 1 Talents",
        description="You can choose one of the following Talents at Tier 1. ",
        colour=grista,
        url="https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.quxd8c66uhju",
    )
    embed.add_field(
        name="CHARMING",
        value="Contextual\nWhen you roll **Charm** and get a 1, it counts as a success.",
        inline=False,
    )
    embed.add_field(
        name="ELEMENTARY", value="Eternal\n+1 to **Intellect**. ", inline=False
    )
    embed.add_field(
        name="FAST",
        value="Contextual\nYou can travel an additional 2 spaces On Move. ",
        inline=False,
    )
    embed.add_field(
        name="HEALER",
        value="Contextual\nYou can choose an adjacent individual and restore 1D6 to their Life On Act.",
        inline=False,
    )
    embed.add_field(
        name="HIDDEN STEPS",
        value="Contextual Eternal\n+1 to **Obfuscate**, and you can Hide On Move if you travel no more than 1 space.",
        inline=False,
    )
    embed.add_field(
        name="I CAN'T TURN IT OFF",
        value="Contextual\nWhen you Saunter On Move, you can travel 4 spaces, rather than 2. ",
        inline=False,
    )
    embed.add_field(
        name="MARTIALIST",
        value="Contextual\nYou inflict +1 Hurt with weapons that have a 1-space range. ",
        inline=False,
    )
    embed.add_field(
        name="OBSERVANT", value="Eternal\n+1 to **Observe**. ", inline=False
    )
    embed.add_field(
        name="TANK",
        value="Contextual Eternal\nWhen you Impose On Act, you gain a +1 to **Moxie**. You also gain 5 to your maximum Life.",
        inline=False,
    )
    embed.add_field(
        name="TRANSLATOR",
        value="Eternal\nYou learn three languages of your choice. ",
        inline=False,
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.set_footer(
        text="🔎 Horizon Rulebook | Talents (Page 29: Web Version; Page 16: PDF Version)"
    )
    await ctx.respond(embed=embed)


@talents.child()
@lightbulb.command("tier_2", "Details the options for Tier 2 Talents. ")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def tier2(ctx: lightbulb.Context) -> None:
    """Tier 2 Talents subcommand."""
    embed = hikari.Embed(
        title="Tier 2 Talents",
        description="You can choose one of the following Talents at Tier 2. ",
        colour=grista,
        url="https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.quxd8c66uhju",
    )
    embed.add_field(name="AGILE", value="Eternal\n+1 to Dodge. ", inline=False)
    embed.add_field(
        name="DOWNTOWN",
        value="Contextual\n+3 to **Strength** when determining thrown distance. ",
        inline=False,
    )
    embed.add_field(
        name="GLYPHS",
        value="Eternal\nYou can read and understand all text. ",
        inline=False,
    )
    embed.add_field(
        name="GET BEHIND ME",
        value="Contextual\nWhen you Impose On Act, you can attempt to protect two individuals instead of one. ",
        inline=False,
    )
    embed.add_field(
        name="I SEE YOU",
        value="Contextual\nWhen you Aim On Act, you have a minimum of 2 successes, rather than 1. ",
        inline=False,
    )
    embed.add_field(
        name="PORTENT",
        value="Contextual\nWhen you roll for Order, you can roll twice and choose either result. ",
        inline=False,
    )
    embed.add_field(
        name="PUGILIST",
        value="Contextual\nWhen you Attack with Body, you gain an additional attack, and inflict +4 Hurt. ",
        inline=False,
    )
    embed.add_field(
        name="STRONGER THAN",
        value="Contextual Eternal\n+2 to **Strength**, and you automatically succeed on rolls to climb and swim.",
        inline=False,
    )
    embed.add_field(
        name="SUPPORT BEACON",
        value="Contextual\nYou can choose an individual within 10 spaces and restore 3 Life to them On Move. ",
        inline=False,
    )
    embed.add_field(name="WATCH THIS", value="Eternal\n+2 to **Charm**. ", inline=False)
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.set_footer(
        text="🔎 Horizon Rulebook | Talents (Page 30: Web Version; Page 17: PDF Version)"
    )
    await ctx.respond(embed=embed)


@talents.child()
@lightbulb.command("tier_3", "Details the options for Tier 3 Talents. ")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def tier3(ctx: lightbulb.Context) -> None:
    """Tier 3 Talent subcommand."""
    embed = hikari.Embed(
        title="Tier 3 Talents",
        description="You can choose one of the following Talents at Tier 3. ",
        colour=grista,
        url="https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.quxd8c66uhju",
    )
    embed.add_field(
        name="BOB & WEAVE",
        value="Eternal\nYou reduce Hurt inflicted by adjacent individuals by 1. ",
        inline=False,
    )
    embed.add_field(
        name="CLIMBER",
        value="Contextual\nWhen you Climb On Move, the distance you can travel is doubled.",
        inline=False,
    )
    embed.add_field(
        name="CUNNING NOT SMARTS",
        value="Contextual\nWhen you roll **Intellect**, you can spend 1 *Fortune* to roll **Charm** instead. ",
        inline=False,
    )
    embed.add_field(
        name="DIPLOMAT",
        value="Contextual\nWhen you Negotiate On Act and are speaking a language that is not your first, you have a +2 to **Charm**.",
        inline=False,
    )
    embed.add_field(
        name="FATE WEAVER",
        value="Contextual\nWhen you reroll a die by spending *Fortune*, you treat any 1s as successes. ",
        inline=False,
    )
    embed.add_field(
        name="I KNOW WHAT I'M DOING",
        value="Eternal\n+2 to attribute rolls to repair or craft objects with tools.",
        inline=False,
    )
    embed.add_field(
        name="NOT TODAY",
        value="Eternal\nYou have a +2 to **Intellect** rolls made to help a dying individual return to life. ",
        inline=False,
    )
    embed.add_field(
        name="PARKOUR",
        value="Eternal\nYou reduce any Hurt inflicted from falling by half (rounded up; a minimum of 1 Hurt). ",
        inline=False,
    )
    embed.add_field(
        name="SURVIVOR",
        value="Contextual Eternal\n+2 to **Survival**, and you can roll **Survival** instead of **Fate** when rolling to avoid death while dying.",
        inline=False,
    )
    embed.add_field(
        name="SWIMMER",
        value="Contextual\nWhen you Swim On Move, the distance you can travel is doubled, as well as the duration you may hold your breath before drowning. ",
        inline=False,
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.set_footer(
        text="🔎 Horizon Rulebook | Talents (Page 31: Web Version; Page 17: PDF Version)"
    )
    await ctx.respond(embed=embed)


@talents.child()
@lightbulb.command("tier_4", "Details the options for Tier 4 Talents. ")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def tier4(ctx: lightbulb.Context) -> None:
    """Tier 4 Talent subcommand."""
    embed = hikari.Embed(
        title="Tier 4 Talents",
        description="You can choose one of the following Talents at Tier 4. ",
        colour=grista,
        url="https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.quxd8c66uhju",
    )
    embed.add_field(
        name="CAN'T TOUCH THIS", value="Eternal\n+2 to Dodge. ", inline=False
    )
    embed.add_field(
        name="CATCHPHRASE!",
        value="Contextual\nWhen you use your catchphrase to regain spent *Fortune*, you can choose to regain 1D6, rather than 2.",
        inline=False,
    )
    embed.add_field(
        name="CRAFTY",
        value="Eternal\nYou require half the normal amount of time to craft objects with tools. ",
        inline=False,
    )
    embed.add_field(
        name="GUIDING INFLUENCE",
        value="Contextual\nWhen an individual within 10 spaces rolls 0 successes and doesn’t spend *Fortune* on the roll, you can spend your *Fortune* to allow them to reroll.",
        inline=False,
    )
    embed.add_field(
        name="INTIMIDATING",
        value="Contextual Eternal\n+2 to **Fear**, and +2 to **Moxie** for Contested Rolls against Fear. ",
        inline=False,
    )
    embed.add_field(
        name="I AM THE NIGHT", value="Eternal\n+3 to **Obfuscate**. ", inline=False
    )
    embed.add_field(
        name="OW", value="Eternal\nYou inflict +2 Hurt with all weapons. ", inline=False
    )
    embed.add_field(
        name="PARRY",
        value="Contextual\nWhen you are the victor in a contested Dodge roll against an adjacent individual’s attack, you can spend 1 *Fortune* to Attack them once. This attack can be made with any weapon that has a 1-space range. ",
        inline=False,
    )
    embed.add_field(
        name="SONIC SPEED",
        value="Eternal\nYou can forgo your Act phase to take two Move phases (allowing for a total of 3 Move phases on your turn). ",
        inline=False,
    )
    embed.add_field(
        name="'TIS THE WILL NOT THE WAY",
        value="Eternal\n+3 to **Fate**. ",
        inline=False,
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.set_footer(
        text="🔎 Horizon Rulebook | Talents (Page 32: Web Version; Page 18: PDF Version)"
    )
    await ctx.respond(embed=embed)


@talents.child()
@lightbulb.command("tier_5", "Details the options for Tier 5 Talents. ")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def tier5(ctx: lightbulb.Context) -> None:
    """Tier 5 Talent subcommand."""
    embed = hikari.Embed(
        title="Tier 5 Talents",
        description="You can choose one of the following Talents at Tier 5. ",
        colour=grista,
        url="https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.quxd8c66uhju",
    )
    embed.add_field(
        name="DESPERATE TIMES",
        value="Contextual\nWhile you have 0 *Fortune*, you can choose to spend 3 Life to reroll a die as you would when spending 1 *Fortune*. ",
        inline=False,
    )
    embed.add_field(
        name="FOCUS",
        value="Eternal\nYou can have a minimum of 2 successes on an **Intellect** roll.",
        inline=False,
    )
    embed.add_field(
        name="HIT ME",
        value="Contextual\nWhen your Life is below 10, your attacks inflict 2 additional Hurt. ",
        inline=False,
    )
    embed.add_field(
        name="SNIPER",
        value="Contextual\nWhen you Aim On Act, you can Attack twice instead of once. ",
        inline=False,
    )
    embed.add_field(
        name="STAY CLOSE",
        value="Eternal\nOther individuals who are not inert, dying, or dead that start their turn within 5 spaces of you regain 1D6 Life (should you wish them to). ",
        inline=False,
    )
    embed.add_field(
        name="SPECIALIZED",
        value="Eternal\nChoose one attribute’s value to become 7. ",
        inline=False,
    )
    embed.add_field(
        name="TALENTED", value="Eternal\n+1 to all attributes. ", inline=False
    )
    embed.add_field(
        name="TRUTHSEER",
        value="Eternal\nYou require no roll to know if an individual is lying, regardless if you know the language they are communicating in. ",
        inline=False,
    )
    embed.add_field(
        name="UNSTOPPABLE",
        value="Contextual\nThe first time each session you are reduced to 0 Life, you are reduced to 1D6 Life instead. ",
        inline=False,
    )
    embed.add_field(
        name="WHERE ARE YOU GOING",
        value="Contextual\nWhen an adjacent individual attempts to move into non-adjacent space, you can roll **Strength** contested with their **Finesse**. If you are the victor, their Move phase is skipped that turn. ",
        inline=False,
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.set_footer(
        text="🔎 Horizon Rulebook | Talents (Page 33: Web Version; Page 19: PDF Version)"
    )
    await ctx.respond(embed=embed)


# Load the plugin.
def load(bot):
    bot.add_plugin(talent)


# Unload the plugin.
def unload(bot):
    bot.remove_plugin(talent)
