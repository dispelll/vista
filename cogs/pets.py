# Copyright © 2023 autosave
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""Used for /pets. """
import hikari
import lightbulb


# Establish the plugin.
pet = lightbulb.Plugin("cogs.pets")
# Quick references for embed colour/flags.
grista = "#207178"
ephemeral = hikari.MessageFlag.EPHEMERAL


@pet.command()
@lightbulb.command("pets", "Details the Pets in Horizon! ")
@lightbulb.implements(lightbulb.SlashCommand)
async def pets(ctx: lightbulb.Context) -> None:
    """The Pet command."""
    embed = hikari.Embed(
        title="Pets",
        description="Pets have three types: Companion, Bulwark, and Mount. Pets cannot have their rolls [Echoed](https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.vqovswl0d5j8), have 0 *Fortune*, and do not use forks. Caretakers (the individual a pet is loyal to) roll for their pets, though may not gain [Ability Points](https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.7m69jbg1eea) from these rolls. ",
        colour=grista,
        url="https://docs.google.com/document/d/1HDEeXMPuL2D_trFU0TYLrCQ1XdIysJk9z5Q_YdhF6Hc/edit#bookmark=id.j9vmz5jwaepy",
    )
    embed.add_field(
        name="Companion 🐶",
        value="A Companion pet cannot inflict or be inflicted Hurt, or used in combat at all.",
        inline=False,
    )
    embed.add_field(
        name="Bulwark 🐻",
        value="Hurt can be inflicted to Bulwark pets, and they may inflict it as well. Bulwark pets may be commanded in combat by their caretaker. Regardless of the pet, a Bulwark pet’s attributes are based on their caretaker’s. Bulwark pets have half (rounded up, a minimum of 1) the attribute values of their caretaker. \n\nA Bulwark pet’s caretaker can spend their own *Fortune* to alter the pet’s rolls as they would their own. \n\nWhen a caretaker’s turn arrives in Order, the caretaker can choose to either command a Bulwark pet On Act or On Move (but not both on the same turn). \n\nBulwark pets can move up to their Move value when commanded, and then Attack once with Body. Bulwark pets gain a second attack when their caretaker reaches Tier 3, and a third attack when their caretaker reaches Tier 5",
        inline=False,
    )
    embed.add_field(
        name="Mount 🐴",
        value="An individual riding a pet with the Mount type can move up to the mount’s Move value On Move. If the pet also has the Bulwark type, the pet can be commanded to Attack On Act or On Move as normal. The Mount type always coincides with either the Companion type, or the Bulwark type; a pet never has solely the Mount type. ",
        inline=False,
    )
    embed.add_field(
        name="Multiple Types",
        value="Pets often have multiple types, which interact in specific ways. \n\n🐶🐻\nA pet can never have both the Companion and Bulwark types. Hurt can either be inflicted to a pet (Companion), or it can’t be (Bulwark). \n\n🐶🐴\nHurt cannot be inflicted to a pet that has both the Companion and Mount types, but the pet can be ridden and used On Move by an individual. A pet that has both of these types that is ridden in combat acts erratically, as it is not trained for it. An individual riding a pet with the Mount and Companion types in combat has a -2 Contextual penalty to their Dodge rolls. \n\n🐻🐴\nA pet that has both the Bulwark and Mount types can be ridden in combat without issue, and commanded to Attack On Act or On Move. ",
        inline=False,
    )
    embed.add_field(
        name="Protection",
        value="A pet that has both the Bulwark and Mount types can benefit from protective gear in the same way their caretaker does, should a GM allow it. A pet requires custom-made protection (a suit of armor, leathers, etc.) made specifically for it to benefit from protective gear in combat.",
        inline=False,
    )
    embed.add_field(
        name="Bearing Burden",
        value="A pet with the Mount type can be used to tow and carry things. It is up to the GM what a pet could feasibly carry and/or tow but, if an exact number should be needed, base it on the mount’s **Strength** value times 25. ",
        inline=False,
    )
    embed.add_field(
        name="How Many Pets",
        value="An individual can only have a single pet of the Bulwark or Mount type at a time. There is no limit on the number of Companion pets an individual may have, however, unless the GM sets one. ",
        inline=False,
    )
    embed.set_author(icon=ctx.member.avatar_url, name=ctx.member.display_name)
    embed.set_footer(
        text="🔎 Horizon Rulebook | Pets (Page 23: Web Version; Page 13: PDF Version)"
    )
    await ctx.respond(embed=embed)


# Load the plugin.
def load(bot):
    bot.add_plugin(pet)


# Unload the plugin.
def unload(bot):
    bot.remove_plugin(pet)
