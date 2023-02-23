# Copyright © 2023 autosave
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""Used for /rules for rule lookup. """
import hikari
import lightbulb


# Establish the plugin.
rule = lightbulb.Plugin("cogs.rules")
# Quick references for embed colour/flags.
grista = "#207178"
ephemeral = hikari.MessageFlag.EPHEMERAL


@rule.command()
@lightbulb.command("rules", "Look up rules! ")
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def rules(ctx: lightbulb.Context) -> None:
    """Command group for /rules."""
    embed = hikari.Embed(
        title="Look Up Rules! 👩‍⚖️",
        description="The `/rule` command has the following subcommands to look up rules. ",
        colour=grista,
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.add_field(
        name="`/rules attributes`",
        value="This command details attributes and their forks. ",
        inline=False,
    )
    embed.add_field(
        name="`/rules standard_roll`",
        value="This command details Standard Rolls. ",
        inline=False,
    )
    embed.add_field(
        name="`/rules contested_roll`",
        value="This command details Contested Rolls. ",
        inline=False,
    )
    embed.add_field(
        name="`/rules group_roll`",
        value="Use this command to detail Group Rolls. ",
        inline=False,
    )
    embed.add_field(
        name="`/rules fortune`",
        value="Use this command to detail *Fortune*. ",
        inline=False,
    )
    embed.add_field(
        name="`/rules modifiers`",
        value="Use this command to detail Modifiers (+/-). ",
        inline=False,
    )
    embed.add_field(
        name="`/rules catchphrase`",
        value="Use this command to detail Catchphrase. ",
        inline=False,
    )
    embed.add_field(
        name="`/rules connections`",
        value="Use this command to detail Connections & Owes Me One. ",
        inline=False,
    )
    embed.add_field(
        name="`/rules spaces`",
        value="Use this command to detail Spaces (Distance). ",
        inline=False,
    )
    embed.add_field(
        name="`/rules life`",
        value="Use this command to detail Get A Life & Hurt. ",
        inline=False,
    )
    embed.add_field(
        name="`/rules dodge`", value="Use this command to detail Dodge. ", inline=False
    )
    embed.add_field(
        name="`/rules order`", value="Use this command to detail Order. ", inline=False
    )
    embed.add_field(
        name="`/rules player_advancement`",
        value="Use this command to detail Order. ",
        inline=False,
    )
    embed.add_field(
        name="`/rules fight`", value="Use this command to detail Fight. ", inline=False
    )
    embed.add_field(
        name="`/rules falling`",
        value="Use this command to detail Falling. ",
        inline=False,
    )
    embed.add_field(
        name="`/rules death`",
        value="Use this command to detail Dying & Death. ",
        inline=False,
    )
    embed.add_field(
        name="`/rules render_inert`",
        value="Use this command to detail Render Inert. ",
        inline=False,
    )
    embed.add_field(
        name="`/rules player_inventory`",
        value="Use this command to detail Player Inventory. ",
        inline=False,
    )
    embed.add_field(
        name="`/rules protection`",
        value="Use this command to detail Protective Gear. ",
        inline=False,
    )
    embed.add_field(
        name="`/rules object_life`",
        value="Use this command to detail Object Life. ",
        inline=False,
    )
    embed.add_field(
        name="`/rules intoxication`",
        value="Use this command to detail Intoxication. ",
        inline=False,
    )
    embed.add_field(
        name="`/rules currency`",
        value="Use this command to detail Cost & Worth (Currency). ",
        inline=False,
    )
    embed.add_field(
        name="`/rules tools_crafting_repair`",
        value="Use this command to detail Tools, Crafting, & Repair. ",
        inline=False,
    )
    embed.add_field(
        name="`/rules stuff`", value="Use this command to detail Stuff. ", inline=False
    )
    embed.add_field(
        name="`/rules light`", value="Use this command to detail Light. ", inline=False
    )
    await ctx.respond(embed=embed)


@rules.child()
@lightbulb.command("attributes", "Detail attributes in Horizon! ")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def att(ctx: lightbulb.Context) -> None:
    """Command to detail attributes."""
    embed = hikari.Embed(
        title="Attributes",
        description="Horizon uses 10 attributes to measure an individual’s (the framework’s general term that describes both players and NPCs) ability, potential, and luck.\n\n• **Strength:** a measure of physical power. \n• **Intellect:** a measure of logic and reasoning. \n• **Finesse:** a measure of agility and dexterity. \n• **Observe:** a measure of situational awareness. \n• **Charm:** a measure of personality and nature. \n• **Obfuscate:** a measure of ability to hide things. \n• **Fate:** a measure of luck and destiny. \n• **Survival:** a measure of potential to remain living. \n• **Moxie:** a measure of stability and fortitude. \n• **Fear:** a measure of ability to intimidate and scare. ",
        colour=grista,
        url="https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.wz4newlvcvpi",
    )
    embed.add_field(
        name="Attribute Forks (Optional)",
        value="Games in need of more crunch and complexity can utilize attribute forks for more specialized challenges. Each forked attribute starts with a value equal to the attribute it is forked from, with the ability to be modified independently thereafter. \n\n• **Strength:** Brawl, Drag, Grab, Lift, Push, Throw \n• **Intellect:** Construct, Focus, Retort, Heal, Sanity \n• **Finesse:** Craft, Dance, Draw, Drive, Pick Lock \n• **Observe:** Discern, Doubt, Find, Listen, Keep Watch \n•**Charm:** Convince, Deceive, Distract, Seduce \n• **Obfuscate:** Hide Object, Hide Self, Steal, Withhold \n• **Fate:** Chance, Gamble, Predict, Will \n• **Survival:** Forage, Hunt, Track, Trap \n• **Moxie:** Defend, Endure, Guts, Nerve \n • **Fear:** Dare, Frighten, Intimidate ",
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.set_footer(
        text="🔎 Horizon Rulebook | Attributes (Page 3: Web Version; Page 1: PDF Version)"
    )
    await ctx.respond(embed=embed)


@rules.child()
@lightbulb.command("standard_roll", "Detail Standard Rolls in Horizon! ")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def sr(ctx: lightbulb.Context) -> None:
    """Command for Standard Rolls."""
    embed = hikari.Embed(
        title="Standard Roll",
        description="When the GM calls for a Standard Roll, the individual rolls a number of D6s (six-sided dice) equal to the applicable attribute’s value. \n\nFor example, if Larry is attempting to move a heavy object, the GM may call for Larry to roll **Strength**. Larry has a 3 in his **Strength** attribute, meaning his **Strength** value is 3, so he rolls 3D6. \n\nThe individual then counts the number of dice that resulted in 4 or above, referring to the total as the number of successes. If a die results in a 6, it’s a **Triumph**, which counts as 2 successes. The GM then details the results. ",
        colour=grista,
        url="https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.lrz83saiozz",
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.set_footer(
        text="🔎 Horizon Rulebook | Standard Roll (Page 4: Web Version; Page 1: PDF Version)"
    )
    await ctx.respond(embed=embed)


@rules.child()
@lightbulb.command("contested_roll", "Details Contested Rolls in Horizon! ")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def cr(ctx: lightbulb.Context) -> None:
    """Command for Contested Rolls."""
    embed = hikari.Embed(
        title="Contested Roll",
        description="When the GM calls for a Contested Roll, opposing individuals each roll a number of D6s equal to their value in an applicable attribute. The GM may tell each individual to roll different attributes. Some common examples of which attributes are contested with others include: \n\n• **Strength vs. Finesse:** When an individual is trying to escape another’s grasp. \n• **Observe vs. Obfuscate:** When an individual is attempting to find something hidden by another. \n• **Fear vs. Moxie:** When an individual is trying to scare another. \n• **Intellect vs. Survival:** When an individual is trying to break or free themselves from a trap. \n• **Charm vs. Observe:** When one individual is attempting to lie to another. \n• **Fate vs. Survival:** When an individual is trying to remain alive through sheer dumb luck or force of will. \n\nAfter both opposing individuals roll, they each count the number of dice that resulted in 4 or above, referring to the total as the number of successes. If a die results in a 6, it’s a **Triumph**, which counts as 2 successes. The GM then details the results, with the individual that rolled the higher number of successes being the victor. \n\nShould a Contested Roll result in a Stalemate (each individual rolls an equal number of successes), there is no victor, and nothing happens. \n\nIf using forks, Contested Rolls become more specific. Examples of what forks are used for, and what they are typically contested with can be found in the For The GM chapter. ",
        colour=grista,
        url="https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.za44rf530dkm",
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.set_footer(
        text="🔎 Horizon Rulebook | Contested Roll (Page 4: Web Version; Page 2: PDF Version)"
    )
    await ctx.respond(embed=embed)


@rules.child()
@lightbulb.command("group_roll", "Details Group Rolls in Horizon! ")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def gr(ctx: lightbulb.Context) -> None:
    """Command for Group Rolls."""
    embed = hikari.Embed(
        title="Group Roll",
        description="When more than one individual is working to achieve the same goal, the GM may call for a Group Roll. Each individual making the roll does so as a Standard Roll, but only the highest number of successes is used. A Group Roll can also be contested by another individual or group. \n\nFor example, if Avery and Diane are both trying to move a guard away from a doorway, the GM may call for a Group Roll. Avery wishes to sneak behind the guard, and catch them off balance, so the GM tells Avery to roll **Obfuscate**. Diane, however, wishes to use brute force, so the GM tells Diane to roll **Strength**. \n\nAvery has a 4 in **Obfuscate**, so rolls 4D6 and gets a 1, 2, **4**, and **4** for a total of 2 successes. \n\nDiane has a 5 in **Strength**, so rolls 5D6 and gets a 2, 2, 3, **4**, **5**, and **6** for a total of 4 successes. \n\nAs Diane rolled more successes, her 4 successes are used for the Group Roll against the guard. \n\nFinally, the guard rolls Strength to avoid being moved, rolling 3D6. The guard rolls a **4**, **4**, and **5** for a total of 3 successes. \n\nDiane and Avery rolled a greater number of successes, so the guard is moved. ",
        colour=grista,
        url="https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.6skany4n7lmm",
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.set_footer(
        text="🔎 Horizon Rulebook | Group Roll (Page 5: Web Version; Page 2: PDF Version)"
    )
    await ctx.respond(embed=embed)


@rules.child()
@lightbulb.command("fortune", "Details Fortune in Horizon! ")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def fortune(ctx: lightbulb.Context) -> None:
    """Command that details Fortune."""
    embed = hikari.Embed(
        title="*Fortune*",
        description="*Fortune* is a resource that represents an individual’s influence on the world around them. An individual’s maximum *Fortune* is equal to their **Fate** attribute + 3. \n\n*Fortune* can be spent after making an attribute roll—be it Standard, Contested, or Group—to reroll any of the dice rolled. *Fortune* cannot be spent on Echoed rolls, or when making Ability Rolls. \n\n*Fortune* is spent in a 1:1 ratio, meaning each point spent allows the spender to reroll an equal number of dice. An individual can only spend *Fortune* once per roll, after deciding how much they wish to spend. \n\nIn a [Contested Roll](https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.za44rf530dkm), *Fortune* cannot be spent after the individual knows what an opposing party rolled. Individuals regain 1D6 *Fortune* per in-game day. ",
        colour=grista,
        url="https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.f9zcb6hkl910",
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.set_footer(
        text="🔎 Horizon Rulebook | Fortune (Page 5: Web Version; Page 2: PDF Version)"
    )
    await ctx.respond(embed=embed)


@rules.child()
@lightbulb.command("modifiers", "Details Modifiers in Horizon! ")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def mod(ctx: lightbulb.Context) -> None:
    """Command for Modifiers."""
    embed = hikari.Embed(
        title="Modifiers (+/-)",
        description="There are two types of modifiers: Contextual, and Eternal. In either case, a plus or minus sign before a number indicates that the applicable roll is made with more or less dice than usual. Regardless of modifiers, an individual can’t roll less than 1 die, or greater than 10.  ",
        colour=grista,
        url="https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.ua74dox36vlf",
    )
    embed.add_field(
        name="Contextual",
        value="A Contextual modifier only applies in a specific context. For example, “When you Impose On Act, you gain a +1 to **Moxie**” indicates that only when Imposing On Act would an individual add an additional D6 to their **Moxie** rolls. ",
        inline=False,
    )
    embed.add_field(
        name="Eternal",
        value="​​An Eternal modifier lasts indefinitely, and offers little to no context. For example, “+1 to **Observe**” means that the individual permanently increases their **Observe** value (along with its forks, if using them) by 1. ",
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.set_footer(
        text="🔎 Horizon Rulebook | Modifiers (+/-) (Page 6: Web Version; Page 3: PDF Version)"
    )
    await ctx.respond(embed=embed)


@rules.child()
@lightbulb.command("catchphrase", "Details Catchphrase in Horizon! ")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def catch(ctx: lightbulb.Context) -> None:
    """Catchphrase command."""
    embed = hikari.Embed(
        title="Catchphrase",
        description="Once per session, a player can say their Catchphrase to regain 2 spent *Fortune*. If in Order, a player can only say their catchphrase during their turn.",
        colour=grista,
        url="https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.tzzz5df3hnrn",
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.set_footer(
        text="🔎 Horizon Rulebook | Catchphrase (Page 6: Web Version; Page 3: PDF Version)"
    )
    await ctx.respond(embed=embed)


@rules.child()
@lightbulb.command("connections", "Details Connections in Horizon! ")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def conn(ctx: lightbulb.Context) -> None:
    """Connections & OMO command."""
    embed = hikari.Embed(
        title="Connections & Owes Me One",
        description="Connections are a mechanical representation of player relationships in roleplay, and exist to symbolize a bond. While making characters, players will likely have previously established connections. Should the GM allow this, a maximum of 2 starting connections is recommended per player. \n\nWhen a situation occurs that would warrant an individual owing another a favor, the individual then Owes Them One. When a player is owed a favor by a connection, they tick “OMO” (Owes Me One) next to that connection. When a player instead owes a connection a favor, they tick “OTO” (Owe Them One). OMO and OTO work the same mechanically. \n\nA connection may only owe one favor to the same individual, and the way that favor is called upon is up to the connection, and only works should the GM find the favor feasible. Favors can be represented more specifically mechanically by allowing a temporary or permanent advantage once called in. ",
        colour=grista,
        url="https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.wb7rpjida2x3",
    )
    embed.add_field(
        name="Temporary Advantage",
        value="A temporary advantage, when called, grants a positive mechanical consequence of some sort (e.g. the player gains a +1 Contextual bonus to an attribute for a short time, borrows a special item, gains useful advice, etc.). ",
        inline=False,
    )
    embed.add_field(
        name="Permanent Advantage",
        value="A permanent advantage should be granted by the GM very rarely, justified in the owing of extreme favors or connections (saving a life, a long-term close relationship, etc.). Permanent advantages are…permanent. Examples include: learning a new language, an Eternal attribute bump, or gaining very important game-changing knowledge. ",
        inline=False,
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.set_footer(
        text="🔎 Horizon Rulebook | Connections & Owes Me One (Page 6: Web Version; Page 3: PDF Version)"
    )
    await ctx.respond(embed=embed)


@rules.child()
@lightbulb.command("spaces", "Details Spaces (Distance) in Horizon! ")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def spaces(ctx: lightbulb.Context) -> None:
    """Spaces command."""
    embed = hikari.Embed(
        title="Spaces (Distance)",
        description="Distance is measured in spaces. 1 space is roughly 1 meter (~3 feet) in all dimensions. On a gridded or hex map, each player occupies 1 space. NPCs and objects, however, can be larger and may occupy more spaces.",
        colour=grista,
        url="https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.yw4tzw33jsqj",
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.set_footer(
        text="🔎 Horizon Rulebook | Spaces (Distance) (Page 7: Web Version; Page 3: PDF Version)"
    )
    await ctx.respond(embed=embed)


@rules.child()
@lightbulb.command("life", "Details Get A Life & Hurt in Horizon! ")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def life(ctx: lightbulb.Context) -> None:
    """Get A Life & Hurt command."""
    embed = hikari.Embed(
        title="Get A Life & Hurt",
        description="Get A Life (or Life) is how much Hurt (damage) an individual can have inflicted upon them. An individual’s Life is equal to their **Moxie** + **Survival** + 5. When Hurt is inflicted to an individual, they subtract the amount from their current Life. \n\nLife is recovered at a rate of 1D6 per in-game day (without the help of Talents, or other outside influences). ",
        colour=grista,
        url="https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.3ny2y3hvvjwp",
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.set_footer(
        text="🔎 Horizon Rulebook | Get A Life & Hurt (Page 7: Web Version; Page 4: PDF Version)"
    )
    await ctx.respond(embed=embed)


@rules.child()
@lightbulb.command("dodge", "Details Dodge in Horizon! ")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def dodge(ctx: lightbulb.Context) -> None:
    """Dodge command."""
    embed = hikari.Embed(
        title="Dodge",
        description="When an individual wishes to avoid Hurt (and is conscious), they can choose to Dodge. An individual’s Dodge value is equal to their **Finesse** or **Intellect**, whichever is higher. \n\nDodging is always a [Contested Roll](https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.za44rf530dkm) against the thing being dodged. If the dodger rolls a number of successes equal to or greater than the effect being dodged (usually an attack), no Hurt is inflicted on them. ",
        colour=grista,
        url="https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.ls8t7h70rmln",
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.set_footer(
        text="🔎 Horizon Rulebook | Dodge (Page 7: Web Version; Page 4: PDF Version)"
    )
    await ctx.respond(embed=embed)


@rules.child()
@lightbulb.command("order", "Details Order in Horizon! ")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def order(ctx: lightbulb.Context) -> None:
    """Order command."""
    embed = hikari.Embed(
        title="Order",
        description="The GM declares Order when two or more parties are involved in resolving a situation that would be chaotic otherwise. Most often, Order is declared during complex debates—to allow everyone a turn to speak—or during combat, to allow everyone a chance to inflict some Hurt. \n\nWhen Order is declared, each involved individual rolls a D100 (a 100-sided die or a pair of percentile dice). Turns are taken sequentially, from 1-100, then start over from the beginning when all individuals have had a turn. Order ends when the GM decides the situation is resolved. \n\nA turn taken during Order can last minutes or moments. During a discussion, a turn in Order should last no longer than 1 minute. In combat, a turn in Order should last no longer than 10 seconds. \n\nIn the rare case that two or more individuals roll the same number when Order is declared, giving them the same place in Order, the GM chooses who goes first; having each party roll a D6, with the higher roll going first. If the tied individuals are allies, the GM may allow them to choose who goes first. ",
        colour=grista,
        url="https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.f9afcpdmhm0i",
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.set_footer(
        text="🔎 Horizon Rulebook | Order (Page 7: Web Version; Page 4: PDF Version)"
    )
    await ctx.respond(embed=embed)


@rules.child()
@lightbulb.command("player_advancement", "Details Player Advancement in Horizon! ")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def pa(ctx: lightbulb.Context) -> None:
    """Player Advancement command."""
    embed = hikari.Embed(
        title="Player Advancement",
        description="Players advance by increasing their Tier (what a traditional “level” is called in Horizon). Tiers range from 1-5 by default, though a GM may choose to add more. The GM decides when their players advance, granting each of them a new Tier at the same time, typically after major group achievements.",
        colour=grista,
        url="https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.loed86igj2fb",
    )
    embed.add_field(
        name="Talents & Roles",
        value="Each time a player gains a Tier, they [choose a Talent](https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#heading=h.csx40y4e1udt). Players that wish to make character creation as easy as possible, however, may instead [align with a Role](https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#heading=h.neeuzouy5bo6) (a preset selection of Talents). \n\nChoosing a Role does not mean a player can’t deviate to other Talents at future Tiers. Roles exist to represent standard class/specialty combinations that can be found across many genres. Once chosen, a Talent cannot be changed. ",
        inline=False,
    )
    embed.add_field(
        name="Ability Points",
        value="The first time each attribute roll a player rolls a **Triumph** (a 6 on a D6), they gain an Ability Point (AP). AP can never exceed 4 for the same attribute.\n\nAt the end of each session, players that have 4 AP in an attribute can spend them to make an Ability Roll with that attribute. Ability Rolls are made as a [Contested Roll](https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.za44rf530dkm) against the attribute a player is trying to increase. *Fortune* cannot be spent on Ability Rolls. If an Ability Roll results in a number of successes greater than the attribute’s current value, its value increases by 1, to a maximum of 10 (see [Modifiers](https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.ua74dox36vlf)). ",
        inline=False,
    )
    embed.add_field(
        name="Using Ability Points For Abilities",
        value="Rather than rolling to increase an attribute when their AP reaches 4, a player can instead choose to wait until they reach a total of 20 AP across all attributes, and spend them to gain a new ability.\n\nAbilities are always Contextual, and are chosen randomly by rolling a D100 on the [Ability table](https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.buj66qtw3d57) (`/roll ability`). If a player rolls and gets an ability they already have, they reroll until receiving another result. \n\nA player can use one ability per in-game day at Tier 1, two abilities per in-game day at Tier 3, and three abilities per in-game day at Tier 5. ",
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.set_footer(
        text="🔎 Horizon Rulebook | Player Advancement (Page 11: Web Version; Page 6: PDF Version)"
    )
    await ctx.respond(embed=embed)


@rules.child()
@lightbulb.command("fight", "Details combat in Horizon! ")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def fight(ctx: lightbulb.Context) -> None:
    """Fight command."""
    embed = hikari.Embed(
        title="Fight",
        description="When diplomacy fails, or isn’t an option, combat can occur. In combat, all rolls are [Contested Rolls](https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.za44rf530dkm) (usually Attack vs. Dodge). Examples of the attributes rolled when using a weapon to attack, the number of attacks a weapon has, its range, and whether or not its single use or uses ammunition (expends) can be found in the Fight table. When an individual expends their last of a weapon’s ammunition, they can’t Attack with it again. \n\nA weapon that has a parenthetical in its Hurt column deals that Hurt to those who can’t Dodge it in a certain shape area (sphere, cone, or line). \n\nIf an individual wants to throw something feasible, they can do so a number of spaces equal to their **Strength** value. If an individual grabs something that is not technically a weapon and uses it as one, they attack with it as they would with Body. ",
        colour=grista,
        url="https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.rrrig1ea3xz0",
    )
    embed.set_image(
        "https://cdn.discordapp.com/attachments/926990804877185076/1078351625166536784/image.png"
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.set_footer(
        text="🔎 Horizon Rulebook | Fight (Page 13: Web Version; Page 8: PDF Version)"
    )
    await ctx.respond(embed=embed)


@rules.child()
@lightbulb.command("falling", "Details Falling in Horizon! ")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def falling(ctx: lightbulb.Context) -> None:
    """Falling command."""
    embed = hikari.Embed(
        title="Falling",
        description="After falling, an individual is inflicted 1 Hurt per space they fell.",
        colour=grista,
        url="https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.n1deneltk89y",
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.set_footer(
        text="🔎 Horizon Rulebook | Falling (Page 14: Web Version; Page 8: PDF Version)"
    )
    await ctx.respond(embed=embed)


@rules.child()
@lightbulb.command("death", "Details Dying & Death in Horizon! ")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def death(ctx: lightbulb.Context) -> None:
    """Dying & Death command."""
    embed = hikari.Embed(
        title="Dying & Death",
        description="An individual with 0 Life is dying. If in Order, a dying individual can only move 1 space On Move, and can only roll **Survival** On Act. The individual must roll at least 1 success to stay alive while dying. As with most rolls, remember that *Fortune* can still be spent while dying. A dying individual that rolls a **Triumph** regains 1 Life. \n\nAn individual adjacent to a dying one can attempt to help them by rolling **Intellect** contested with the dying individual’s **Fate**. If the helper is the victor, the dying individual is no longer dying, and gains Life equal to the number of successes the helper rolled. ",
        colour=grista,
        url="https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.6tlsicmm77cj",
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.set_footer(
        text="🔎 Horizon Rulebook | Dying & Death (Page 14: Web Version; Page 8: PDF Version)"
    )
    await ctx.respond(embed=embed)


@rules.child()
@lightbulb.command("render_inert", "Details Render Inert in Horizon! ")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def render(ctx: lightbulb.Context) -> None:
    """Render Inert command."""
    embed = hikari.Embed(
        title="Render Inert",
        description="So long as they are adjacent to an individual and using a blunt weapon (hand, arm, pommel of a sword, etc.), an individual who reduces another to 0 Life may declare that they wish to render them inert, rather than deal fatal Hurt. \n\nRendering an individual inert effectively knocks them unconscious. For each in-game hour an individual is rendered inert they roll **Moxie**. If at least 2 successes are rolled, the individual becomes conscious once more.",
        colour=grista,
        url="https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.yis81a1ou9po",
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.set_footer(
        text="🔎 Horizon Rulebook | Render Inert (Page 15: Web Version; Page 8: PDF Version)"
    )
    await ctx.respond(embed=embed)


@rules.child()
@lightbulb.command("player_inventory", "Details Player Inventory in Horizon! ")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def pi(ctx: lightbulb.Context) -> None:
    """Player Inventory command."""
    embed = hikari.Embed(
        title="Player Inventory",
        description="The amount players can carry with them can be kept simple by keeping it realistic. Could you carry 15 weapons, a giant statue, a broken guitar, and a zombie leg at the same time? No? Well, it would stand to reason that a player couldn’t do that either. \n\nKeeping track of things based on their weight is doable, but not fun for (most) players. However, should a capacity calculation be needed, determine it based on the character’s **Strength** value times 25. ",
        colour=grista,
        url="https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.kj1jrbq015cw",
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.set_footer(
        text="🔎 Horizon Rulebook | Player Inventory (Page 15: Web Version; Page 9: PDF Version)"
    )
    await ctx.respond(embed=embed)


@rules.child()
@lightbulb.command("protection", "Details Protective Gear in Horizon! ")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def protect(ctx: lightbulb.Context) -> None:
    """Protective Gear command."""
    embed = hikari.Embed(
        title="Protective Gear",
        description="Gear that offers additional protection does so by adding additional Life on top of the individual’s current Life. An individual may benefit from multiple sources of protection simultaneously only if the GM allows them to. \n\nWhen Hurt is inflicted to an individual wearing protective gear, they subtract it from their gear’s Life, rather than their own. Should a piece of gear be reduced to 0 Life, the gear is broken, with any remaining Hurt inflicted to the individual, as normal. \n\nThe amount of Life a piece of protective gear has can vary greatly, and common examples can be found on [the Protection table](https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.rb59wl4lplb7). Gear can typically, depending on the GM and game, be repaired via a special set of tools or service. See the [Tools, Crafting, & Repair](https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.urjrmgljt8yf) section for more details.  ",
        colour=grista,
        url="https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.len5nre6gmow",
    )
    embed.add_field(
        name="Shields",
        value="An individual can only wield one shield at a time and, while doing so, may Impose On Move (able to continue doing so On Move on future turns), as well as On Act. While wielding a shield, an individual has a +1 Contextual bonus to Dodge. The amount of protection gained by a shield varies based on what it's made of. ",
        inline=False,
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.set_footer(
        text="🔎 Horizon Rulebook | Protective Gear (Page 15: Web Version; Page 9: PDF Version)"
    )
    await ctx.respond(embed=embed)


@rules.child()
@lightbulb.command("object_life", "Details Object Life in Horizon! ")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def object_life(ctx: lightbulb.Context) -> None:
    """Object Life command."""
    embed = hikari.Embed(
        title="Object Life",
        description="A carriable object has 5 Life, a wearable object has 2, and larger objects have Life equal to the number of spaces they occupy times 5",
        colour=grista,
        url="https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.szh20l86e2dw",
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.set_footer(
        text="🔎 Horizon Rulebook | Object Life (Page 16: Web Version; Page 9: PDF Version)"
    )
    await ctx.respond(embed=embed)


@rules.child()
@lightbulb.command("intoxication", "Details Intoxication in Horizon! ")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def intoxication(ctx: lightbulb.Context) -> None:
    """Intoxication command."""
    embed = hikari.Embed(
        title="Intoxication",
        description="An individual subjected to the effects of an intoxicant bases how they are affected on their **Moxie** value. An individual that consumes alcohol, for example, can imbibe a number of drinks equal to double their **Moxie** value before becoming obviously drunk. \n\nA GM may rule that a substance is stronger, however, and decrease the amount required to become intoxicated to an individual’s **Moxie** value (instead of double it). On the opposing end, a GM may increase the amount of a substance an individual can consume without noticeable effects due to tolerance. \n\nThe way an individual behaves while intoxicated depends on the intoxicant but, regardless, has the following Contextual modifiers until the intoxication ends: -1 to **Intellect**, **Finesse**, **Observe**, and **Obfuscate**; +1 to **Fate** and **Charm**. ",
        colour=grista,
        url="https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.dhvmiatyrtrn",
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.set_footer(
        text="🔎 Horizon Rulebook | Intoxication (Page 16: Web Version; Page 9: PDF Version)"
    )
    await ctx.respond(embed=embed)


@rules.child()
@lightbulb.command("currency", "Details Cost & Worth (Currency) in Horizon! ")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def currency(ctx: lightbulb.Context) -> None:
    """Currency command."""
    embed = hikari.Embed(
        title="Cost & Worth (Currency)",
        description="Currency depends entirely on setting (cash for modern games, credits for sci-fi, pounds for mysteries in London, etc.), but it is recommended to minimize the types of currencies available to avoid the players and GM having to keep track of too many things.",
        colour=grista,
        url="https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.jacvcbt2fcgf",
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.set_footer(
        text="🔎 Horizon Rulebook | Cost & Worth (Currency) (Page 17: Web Version; Page 9: PDF Version)"
    )
    await ctx.respond(embed=embed)


@rules.child()
@lightbulb.command(
    "tools_crafting_repair", "Details Tools, Crafting, & Repair in Horizon! "
)
@lightbulb.implements(lightbulb.SlashSubCommand)
async def tools(ctx: lightbulb.Context) -> None:
    """Tools command."""
    embed = hikari.Embed(
        title="Tools, Crafting, & Repair",
        description="A tool can be anything an individual uses to assist in…anything. For example, an individual picking a lock will likely require a lock-pick, and one creating armor may need an anvil and forge. \n\n**Crafting**\nSee [the Tools table](https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.sjr1vh414hey) for examples of which attributes are rolled for which tools, and [the Crafting table](https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.ntisfqclhxda) for examples of crafted items. Crafting is based on the number of successes rolled over a number of hours. \n\nFor each hour an individual spends crafting, they make one check with the applicable tool. For each success rolled, the individual reduces the total number of successes required to craft the item. When an individual rolls all of the successes required to craft an item, and has spent at least the required number of hours crafting it, they craft it successfully. \n\nAn individual that exceeds the number of successes normally required to craft an item increases its quality, whereas one that fails to meet them within the time required does not craft it and must start over. \n\n When an item is crafted, the materials used to craft it are expended. Crafted item quality is measured in three levels: Suitable, Impressive, and Flawless. ",
        colour=grista,
        url="https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.urjrmgljt8yf",
    )
    embed.add_field(
        name="Suitable (Required Number of Successes)",
        value="The item looks and functions as intended. The item is worth the normal amount. ",
        inline=False,
    )
    embed.add_field(
        name="Impressive (1-5 Additional Successes)",
        value="The item is well made and functions beautifully. The item is worth more than usual. If the item is a weapon or weapon projectile, it inflicts 1 more Hurt than usual. If the item is protective gear, it has 2 more Life than usual. ",
        inline=False,
    )
    embed.add_field(
        name="Flawless (6+ Additional Successes)",
        value="The item is of the highest quality, and is worth far more than usual. If the item is a weapon or weapon projectile, it inflicts 3 more Hurt than usual. If the item is protective gear, it has 5 more Life than usual.",
        inline=False,
    )
    embed.add_field(
        name="Repair",
        value="When repairing an object with tools, the amount of Life restored should be based on the number of successes rolled. For each success rolled, an object is restored 1D6 Life.",
        inline=False,
    )
    embed.add_field(
        name="Improvised Tools",
        value="An individual may attempt to use an object that is not technically a tool to do something a tool is usually needed for. When an individual rolls with an improvised tool, they have a -2 Contextual penalty to attribute rolls made with it. ",
        inline=False,
    )
    embed.add_field(
        name="Material Hierarchy",
        value="The specific amount of a material required to craft something can be kept vague for simplicity, or specified by a GM whose players prefer crunchy crafting. In either case, the order of the materials should be listed by which is most required to which is least required. \n\nFor example, making a backpack requires leather, cloth, and metal. Because a backpack (usually) requires more leather than cloth, leather is listed first. ",
        inline=False,
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.set_footer(
        text="🔎 Horizon Rulebook | Tools, Crafting, & Repair (Page 17: Web Version; Page 10: PDF Version)"
    )
    await ctx.respond(embed=embed)


@rules.child()
@lightbulb.command("stuff", "Details Stuff in Horizon! ")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def stuff(ctx: lightbulb.Context) -> None:
    """Stuff command."""
    embed = hikari.Embed(
        title="Stuff",
        description="Things that are considered general gear used during adventuring are simply referred to as Stuff. Stuff is dependent on setting, but some examples can be found in the Stuff category of [the Crafting table](https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.ntisfqclhxda).",
        colour=grista,
        url="https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.2oeog78qwt5x",
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.set_footer(
        text="🔎 Horizon Rulebook | Stuff (Page 21: Web Version; Page 12: PDF Version)"
    )
    await ctx.respond(embed=embed)


@rules.child()
@lightbulb.command("light", "Details Light in Horizon! ")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def light(ctx: lightbulb.Context) -> None:
    """Light command."""
    embed = hikari.Embed(
        title="Light",
        description="Some items emit light when used or lit. The amount of light emitted is different for each item, and some examples can be found in [the Light table](https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.wyp3n3ond052). ",
        colour=grista,
        url="https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.9bvtuvx4ikfd",
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.set_footer(
        text="🔎 Horizon Rulebook | Light (Page 21: Web Version; Page 12: PDF Version)"
    )
    await ctx.respond(embed=embed)


# Load the plugin.
def load(bot):
    bot.add_plugin(rule)


# Unload the plugin.
def unload(bot):
    bot.remove_plugin(rule)
