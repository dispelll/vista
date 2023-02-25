# Copyright © 2023 autosave
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""Used for /roll to roll dice. """
import hikari
import lightbulb
import random

# Establish the plugin.
roller = lightbulb.Plugin("cogs.roll")
# Quick references for embed colour/flags.
grista = "#207178"
ephemeral = hikari.MessageFlag.EPHEMERAL


@roller.command()
@lightbulb.command("roll", "Roll D6s or D100s! ")
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def roll(ctx: lightbulb.Context) -> None:
    """/Roll command group."""
    embed = hikari.Embed(
        title="Throw Math Rocks! 🎲",
        description="Use `/roll d6` to roll D6s, `/roll d100` to roll a D100, `/roll ability` to roll on the Ability table, and `/roll aspect` to roll on the Aspect table! ",
        colour=grista,
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    await ctx.respond(embed=embed)


@roll.child()
@lightbulb.option("amount", "The number of D6s (1-10) you wish to roll! ")
@lightbulb.command("d6", "Roll 1-10 D6s! ")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def D6(ctx: lightbulb.Context) -> None:
    """Rolls 1-10 D6s."""
    # Throw an error if more than 10 dice are rolled, because that's the max in Horizon, or if amount is not an int.
    rollError = embed = hikari.Embed(
        title="Your Dice Fell Off The Table! (╯°□°)╯︵ ┻━┻",
        description=f"{ctx.member.mention}, you got a roll error! This is usually because you tried to roll greater than 10 dice, or entered something other than a number in the amount field. Try rolling again, putting a number between 1 and 10 in amount. ",
        colour=grista,
    )
    try:
        roll = [random.randint(1, 6) for i in range(int(ctx.options.amount))]
        joinRoll = ",".join(str(i) for i in roll)
        success = roll.count(4) + roll.count(5)
        triumph = roll.count(6)
        successes = success + triumph * 2

        if int(ctx.options.amount) > 10:
            await ctx.respond(embed=rollError, flags=ephemeral)
            return

        embed = hikari.Embed(
            title="Rolling... 🎲",
            description=f"{ctx.member.mention}, you rolled `{joinRoll}`. You got a total of **{successes}** successes. ",
            colour=grista,
        )
        embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
        await ctx.respond(embed=embed)

    except ValueError:
        await ctx.respond(embed=rollError, flags=ephemeral)
        return


@roll.child()
@lightbulb.option("amount", "The number (1-10) of D100s you wish to roll! ")
@lightbulb.command("d100", "Rolls 1-10 D100s! ")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def D100(ctx: lightbulb.Context) -> None:
    """Rolls 1-10 D100s."""
    # Throw an error if more than 10 dice are rolled, or if amount is not an int.
    rollError = embed = hikari.Embed(
        title="Your Dice Fell Off The Table! (╯°□°)╯︵ ┻━┻",
        description=f"{ctx.member.mention}, you got a roll error! This is usually because you tried to roll greater than 10 dice, or entered something other than a number in the amount field. Try rolling again, putting a number between 1 and 10 in amount. ",
        colour=grista,
    )
    try:
        roll = [random.randint(1, 100) for i in range(int(ctx.options.amount))]
        roll.sort()
        joinRoll = ",".join(str(i) for i in roll)

        if int(ctx.options.amount) > 10:
            await ctx.respond(embed=rollError, flags=ephemeral)
            return

        embed = hikari.Embed(
            title="Rolling... 🎲",
            description=f"{ctx.member.mention}, you rolled `{joinRoll}`. ",
            colour=grista,
        )
        embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
        await ctx.respond(embed=embed)
    except ValueError:
        await ctx.respond(embed=rollError, flags=ephemeral)
        return


@roll.child()
@lightbulb.command("ability", "Rolls on the Ability table! ")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def ability(ctx: lightbulb.Context) -> None:
    """Rolls on the Ability table."""
    # List to roll on.
    abilityList = [
        "***Vanish:*** You can turn invisible On Act. You can remain invisible for up to 10 minutes, or until you inflict or are inflicted Hurt. While invisible, you have +2 to **Obfuscate**. ",
        "***Clone Step:*** You can choose to leave a duplicate of yourself behind after leaving a space On Move. The duplicate is an illusion, revealed as such should an individual interact with it physically, or roll greater than 3 successes with **Observe** while adjacent to it. The duplicate remains for up to 10 minutes, vanishing early should you choose to dismiss it. The duplicate is inanimate while active. ",
        "***Fire Breath:*** You can breathe fire when you Attack On Act. The breath uses **Moxie**, has 1 attack, a 1-space range, and inflicts 5 Hurt to individuals that fail to Dodge it. ",
        "***Meditate:*** When your turn arrives in Order, you can choose to spend both phases meditating. If you do, roll **Fate**. If you roll at least one **Triumph**, you instantly regain 1D6 Life. ",
        "***Avian:*** You can transform into a hawk, eagle, or raven (your choice) On Act. Your attribute values remain the same for the duration of this transformation, but you gain the ability to fly 8 spaces On Move. While transformed in this way, you cannot benefit from protective gear, and anything you are wearing or carrying vanishes and cannot be used. This transformation lasts for up to 10 minutes, or until you inflict or are inflicted Hurt. ",
        "***I'm In:*** You can choose an adjacent lock and instantly unlock it On Act.",
        "***Wall Climb:*** On Move, you can travel on vertical surfaces until your turn ends. ",
        "***Flameshot:*** The next time you fire a projectile with a weapon, it catches fire. If an individual fails to Dodge the projectile, they are inflicted 3 more Hurt than usual. ",
        "***Night Vision:*** On Act, you can grant yourself the ability to see in the dark for the next, able to ignore the penalties of partial and total darkness. ",
        "***Treeshift:*** On Act, you can transform yourself into a tree. Your Move phase is skipped for the duration of this transformation, though your attribute values remain the same. While transformed in this way, you cannot benefit from protective gear, and anything you are wearing or carrying vanishes and cannot be used. This transformation lasts for up to 10 minutes, or until you inflict or are inflicted Hurt.",
        "***Ready:*** When Order is declared, you can replace your roll with your **Finesse** value.",
        "***Revenge:*** When inflicted Hurt by failing a Dodge roll, you can choose to inflict the attacker 3 Hurt. ",
        "***Laser Sight:*** You can fire lasers from your eyes On Act. The lasers use **Observe**, have 1 attack, a 5-space range, and inflict 3 (5-space line) to individuals that fail to Dodge it. ",
        "***Leap:*** When you Jump On Move, you can choose to travel triple the normal distance. ",
        "***Sow Discord:*** On Act, you can choose an individual within 5 spaces and cause a thought of betrayal about someone they trust. You choose the individual the thought is about. ",
        "***Flight:*** On Act, you can give yourself the ability to fly up to 8 spaces On Move. This flight lasts up to 10 minutes, or until you dismiss it. ",
        "***Barrier:*** You can create a barrier around yourself On Act. This barrier acts as protection with 5 Life. ",
        "***Drop Eaves:*** On Act, you can grant yourself the ability to hear across great distances for the next 10 minutes. While this ability is active, you can pinpoint the origin of any sounds within 20 spaces, and hear through adjacent thin surfaces such as: doors, walls not made of stone, and walls made of metal. ",
        "***Bioluminescent:*** On Act, you can emit light in a 3-space radius. The color, direction, shape, pattern, and brightness of the light is up to you and can be changed on your turn. The light persists for up to 1 hour, or until you dismiss it. ",
        "***Understand:*** When you hear or read a language you don’t know, you can choose to gain the ability to understand and communicate in it for 1 hour On Act. ",
        "***Heal:*** On Act, you can choose an individual that is not dead within 5 spaces to regain 2 Life. ",
        "***Teleport:*** You can choose to teleport into a space within 20 spaces On Move. If the space is occupied by another individual, roll **Fate** contested with theirs. If you are the victor, the individual teleports into the space you left. If they are the victor, you don’t teleport. ",
        "***Converse:*** On Act, you can choose any individual you’ve met. If the individual is not dead and is willing, an illusory image of them appears in an adjacent space to you. You may then have a conversation with the individual, with them understanding you regardless of language, for up to 1 hour. The conversation ends early if you or the individual wish it to. ",
        "***Detonate:*** You can choose 3 spaces within 10 spaces On Act, causing three small explosions to erupt in each space. Individuals inside the explosions that fail to Dodge are inflicted 5 Hurt. ",
        "***Eject:*** When your turn arrives in Order, you can spend both phases focusing on this ability. Choose up to 5 willing, adjacent individuals as you describe a location. At the start of your next turn, each chosen individual instantly teleports to the location you described (regardless of their distance from you). The GM decides where you teleport to based on the accuracy of your description. ",
    ]
    embed = hikari.Embed(
        title="Rolling On The Ability Table... 🎲",
        description=f"{ctx.member.mention}, you rolled the following ability on the Ability table. \n\n{random.choice(abilityList)}",
        colour=grista,
        url="https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.buj66qtw3d57",
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.set_footer(
        text="🔎 Horizon Rulebook | Player Advancement (Page 11: Web Version; Page 6: PDF Version)"
    )
    await ctx.respond(embed=embed)


@roll.child()
@lightbulb.command(
    "aspect", "Rolls on the Aspect table! (Sends temporary response only you can see. )"
)
@lightbulb.implements(lightbulb.SlashSubCommand)
async def aspect(ctx: lightbulb.Context) -> None:
    """Rolls on the Aspect table."""
    # List to roll on.
    aspectList = [
        "***Gone:*** On Act, the NPC can turn invisible. This invisible ends early if the NPC inflicts or is inflicted Hurt. ",
        "***Undead:*** The NPC does not breathe nor eat. ",
        "***Winged:*** The NPC can fly On Move. ",
        "***Lifedrinker:*** When the NPC inflicts Hurt with Body, they regain 2 Life. ",
        "***Water Dweller:*** The NPC can breathe water, but not air. ",
        "***Amphibious:*** The NPC can breathe both water and air. ",
        "***Fluid Steps:*** On Move, the NPC can walk on liquid surfaces. ",
        "***Elemental Breath:*** The NPC can exhale a 5 (5-space cone) of fire, ice, stone, or air On Act. ",
        "***Mind Reader:*** On Act, the NPC can focus on an individual within 5 spaces, and attempt to read their thoughts. The NPC rolls **Intellect** contested with the individual’s **Moxie**. If the NPC is the victor, they learn the thoughts of the individual for the next minute. ",
        "***Blur:*** The NPC can Move twice, rather than once, On Move. ",
        "***Night Sight:*** The NPC can see in the dark, able to ignore the penalties of partial and total darkness. ",
        "***Electric Eyes:*** Electric Eyes: On Act, the NPC can shoot a 4 (4-space line) of lightning from their eyes.",
        "***Regeneration:*** The NPC regains 1 Life at the start of each turn. ",
        "***Extra Turn:*** The NPC rolls twice when Order is declared, and gets one turn for each roll. ",
        "***Bampf:*** The NPC can teleport to an empty space within 6 spaces On Move.",
        "***Hunter:*** The NPC can use an item taken from an individual to track them without rolling. ",
        "***Explosive:*** When the NPC is reduced to 0 Life, they explode in a 3-space sphere. ",
        "***Corrosive:*** Any individual that is adjacent to the NPC when Hurt is inflicted to them is hit with a terrible acid, and inflicted 2 Hurt. ",
        "***Plant:*** The NPC can subsist solely on photosynthesis and water. ",
        "***Hive Mind:*** The NPC can communicate mentally with other NPCs that have this Aspect. ",
        "***Illusionist:*** The NPC can create an illusion in an empty space within 5 spaces On Act. Individuals adjacent to it that roll 3 or more successes, or interact with it physically, are made aware that the image is an illusion. The illusion can speak as the NPCs wishes, but remains stationary. ",
        "***Evasive:*** When the NPC rolls Dodge and gets a 1, it counts as a success. ",
        "***Escape Artist:*** The NPC cannot be slowed down or stopped On Move, nor can its Move phase be skipped. ",
        "***Extra Turns:*** The NPC rolls three times when Order is declared, and gets one turn for each roll. ",
        "***Shapeshifter:*** The NPC can turn into another individual it has seen before On Act. ",
        "***Fortune Breaker:*** Individuals within 5 spaces of the NPC (other than the NPC themself) cannot spend Fortune. ",
        "***Godly Might:*** The NPC has 10 in Strength and Moxie. ",
    ]
    embed = hikari.Embed(
        title="Rolling On The Aspect Table... 🎲",
        description=f"{ctx.member.mention}, you rolled the following Aspect on the Aspect table. \n\n{random.choice(aspectList)}",
        colour=grista,
        url="https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.irilf82zf65b",
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.set_footer(
        text="🔎 Horizon Rulebook | Combatant NPCs (Page 39: Web Version; Page 24: PDF Version)"
    )
    await ctx.respond(embed=embed, flags=ephemeral)


# Load the plugin.
def load(bot):
    bot.add_plugin(roller)


# Unload the plugin.
def unload(bot):
    bot.remove_plugin(roller)
