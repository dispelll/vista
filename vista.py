# Copyright © 2023 autosave
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""Starts the bot, loads extensions, and creates button views. """
import hikari
import lightbulb
import miru
import random


bot = lightbulb.BotApp(
    # Starts the bot, sets intents, turns off default help slash so we can replace it with /vista.
    token="TOKEN",
    intents=hikari.Intents.ALL,
    help_slash_command=None,
)
# Load the extensions via lightbulb.
bot.load_extensions(
    "cogs.roll",
    "cogs.rules",
    "cogs.hazards",
    "cogs.echo",
    "cogs.pets",
    "cogs.phases",
    "cogs.talents",
    "cogs.roles",
)
# Installs miru.
miru.install(bot)
# Quick references for embed colour/flags.
grista = "#207178"
ephemeral = hikari.MessageFlag.EPHEMERAL
# Sets the build for /vista so users know what version of Horizon the bot is on.
BUILD = "2.5.0"


class VistaView(miru.View):
    """Class for the /vista buttons."""

    def __init__(self) -> None:
        super().__init__(timeout=None)

    @miru.button(label="Roll D6", custom_id="d6")
    async def roll_d6(self, button: miru.Button, ctx: miru.ViewContext) -> None:
        roll = random.randint(1, 6)
        success = 0
        if roll == 4:
            success += 1
        elif roll == 5:
            success += 1
        elif roll == 6:
            success += 2

        embed = hikari.Embed(
            title="Rolling... 🎲",
            description=f"{ctx.member.mention}, you rolled a `{roll}`. You got a total of **{success}** successes. ",
            colour=grista,
        )
        embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
        await ctx.respond(embed=embed, flags=ephemeral)

    @miru.button(label="Roll D100", custom_id="d100")
    async def roll_d100(self, button: miru.Button, ctx: miru.ViewContext) -> None:
        roll = random.randint(1, 100)
        embed = hikari.Embed(
            title="Rolling... 🎲",
            description=f"{ctx.member.mention}, you rolled `{roll}`. ",
            colour=grista,
        )
        embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
        await ctx.respond(embed=embed, flags=ephemeral)

    @miru.button(label="Rules", custom_id="rules")
    async def rules(self, button: miru.Button, ctx: miru.ViewContext) -> None:
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
            name="`/rules dodge`",
            value="Use this command to detail Dodge. ",
            inline=False,
        )
        embed.add_field(
            name="`/rules order`",
            value="Use this command to detail Order. ",
            inline=False,
        )
        embed.add_field(
            name="`/rules player_advancement`",
            value="Use this command to detail Order. ",
            inline=False,
        )
        embed.add_field(
            name="`/rules fight`",
            value="Use this command to detail Fight. ",
            inline=False,
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
            name="`/rules stuff`",
            value="Use this command to detail Stuff. ",
            inline=False,
        )
        embed.add_field(
            name="`/rules light`",
            value="Use this command to detail Light. ",
            inline=False,
        )
        await ctx.respond(embed=embed, flags=ephemeral)

    @miru.button(label="Talents", custom_id="talent")
    async def talents(self, button: miru.Button, ctx: miru.ViewContext) -> None:
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
        await ctx.respond(embed=embed, flags=ephemeral)

    @miru.button(label="On Act", custom_id="act")
    async def on_act(self, button: miru.Button, ctx: miru.ViewContext) -> None:
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
            name="Use 👏",
            value="You use an object with special properties. ",
            inline=False,
        )
        embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
        embed.set_footer(
            text="🔎 Horizon Rulebook | Phases Of A Turn (Page 8: Web Version; Page 4: PDF Version)"
        )
        await ctx.respond(embed=embed, flags=ephemeral)

    @miru.button(label="On Move", custom_id="move")
    async def on_move(self, button: miru.Button, ctx: miru.ViewContext) -> None:
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
        await ctx.respond(embed=embed, flags=ephemeral)

    @miru.button(
        label="Add to Server", style=hikari.ButtonStyle.SECONDARY, custom_id="server"
    )
    async def add_to_server(self, button: miru.Button, ctx: miru.ViewContext) -> None:
        embed = hikari.Embed(
            title="Add Vista To Your Server! 🏔",
            description="Use [this link](https://discord.com/api/oauth2/authorize?client_id=1063989203479834734&permissions=277025507392&scope=bot%20applications.commands) to invite Vista to your server! ",
            colour=grista,
        )
        embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
        await ctx.respond(embed=embed, flags=ephemeral)


@bot.listen()
async def start_views(event: hikari.StartedEvent) -> None:
    """Starts the button view."""
    view = VistaView()
    await view.start()


@bot.command()
@lightbulb.command("vista", "Tells you how to use Vista! ")
@lightbulb.implements(lightbulb.SlashCommand)
async def vista(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(
        title="Hi! :wave: I'm Vista! ",
        description=f"You can use Vista to look up rules and roll dice for [The Horizon Framework!](https://bit.ly/3XHIqlf) \n\nThe buttons below can be used for some of the most common commands, but respond only to the user that clicked them. ",
        colour=grista,
    )
    embed.add_field(
        name="Rule Lookup 📚",
        value="You can use `/rules` to look up rules. This command has a number of subcommands, but the most used are `/rules player_advancement`, `/rules fortune`, `/rules modifiers`, and `/rules fight`. ",
        inline=False,
    )
    embed.add_field(
        name="Roll Dice 🎲",
        value="You can use `/roll d6` and `/roll d100` to roll dice. You can also use `/roll ability` to roll on the Ability table, and `/roll aspect` to roll on the Aspect table. ",
        inline=False,
    )
    embed.add_field(
        name="Talents 🪩",
        value="You can use `/talents` to look up talents by their Tier with `/talents tier_1`, `/talents tier_2`, and so on. ",
        inline=False,
    )
    embed.add_field(
        name="Roles 📋", value="You can use `/roles` to look up roles. ", inline=False
    )
    embed.add_field(
        name="Phases 🎭",
        value="You can use `/phases act` and `/phases move` to detail the options individuals have when Order is declared. ",
        inline=False,
    )
    embed.add_field(
        name="Hazards ☢️",
        value="You can use `/hazards` to detail Hazards. ",
        inline=False,
    )
    embed.add_field(
        name="Pets 🐶", value="You can use `/pets` to detail Pets. ", inline=False
    )
    embed.add_field(
        name="Echo 🗣",
        value="You can use `/echo` to detail the Echo optional rule. ",
        inline=False,
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.set_footer(
        text=f"No relation to the Windows operating system. Currently compatible with Horizon {BUILD}. "
    )
    await ctx.respond(embed=embed, components=VistaView())


# Run the bot.
bot.run(
    status=hikari.Status.ONLINE,
    activity=hikari.Activity(
        name="Horizon! | /vista", type=hikari.ActivityType.PLAYING
    ),
)
