import html
import os

from requests import get
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.utils import get_input_location

from jepthon import jepiq
from JepIQ.razan.resources.strings import *
from telethon import events
from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers import get_user_from_event, reply_id
from . import spamwatch
from telethon.utils import get_display_name
from ..helpers.utils import reply_id, _catutils, parse_pre, yaml_format, install_pip, get_user_from_event, _format

plugin_category = "utils"



#كـتابة المـلف وتعديل.    :   السيد حسين.   اخمط وسمي روحك مطور فرخي 😂
# اذا انت ابن حرام اخمط 😂
# اي بعدك تريد تخمط ترا من تخمط مراح تنجح

@jepiq.on(admin_cmd(pattern="رفع مرتي(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    jepthon = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"🚻 ** ⌯︙ المستخدم => • ** [{jepthon}](tg://user?id={user.id}) \n ☑️ **⌯︙ تم رفعها مرتك بواسطه  :**{my_mention} 👰🏼‍♀️.\n**⌯︙ يلا حبيبي امشي نخلف بيبي 👶🏻🤤** ")

@jepiq.on(admin_cmd(pattern="رفع جلب(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5582470474:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    jepthon = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**⌯︙المستخدم** [{jepthon}](tg://user?id={user.id}) \n**⌯︙ تـم رفعـه جلب 🐶 بواسطة :** {my_mention} \n**⌯︙ خليه خله ينبح 😂**")

@jepiq.on(admin_cmd(pattern="رفع تاج(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    jepthon = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"⌯︙المستخدم [{jepthon}](tg://user?id={user.id}) \n**⌯︙ تـم رفعـه تاج بواسطة :** {my_mention} 👑🔥")

@jepiq.on(admin_cmd(pattern="رفع قرد(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    jepthon = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"⌯︙المستخدم [{jepthon}](tg://user?id={user.id}) \n**⌯︙ تـم رفعـه قرد واعطائه موزة 🐒🍌 بواسطة :** {my_mention}")

@jepiq.on(admin_cmd(pattern="رفع بكلبي(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    jepthon = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**⌯︙المستخدم** [{jepthon}](tg://user?id={user.id}) \n**⌯︙ تـم رفعـه بكلـبك 🤍 بواسطة :** {my_mention} \n**⌯︙ انت حبي الابدي 😍**")
    
    

@jepiq.on(admin_cmd(pattern="رفع مطي(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5582470474:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    jepthon = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**⌯︙المستخدم** [{jepthon}](tg://user?id={user.id}) \n**⌯︙ تـم رفعـه مطي 🐴 بواسطة :** {my_mention} \n**⌯︙ تعال حبي استلم العربانه **")
    
#كـتابة المـلف وتعديل.    :   السيد حسين.   اخمط وسمي روحك مطور فرخي 😂
# اذا انت ابن حرام اخمط 😂
# اي بعدك تريد تخمط ترا من تخمط مراح تنجح


@jepiq.on(admin_cmd(pattern="رفع زوجي(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5582470474:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    jepthon = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**⌯︙المستخدم** [{jepthon}](tg://user?id={user.id}) \n**⌯︙ تـم رفعـه زوجج بواسطة :** {my_mention} \n**⌯︙ يلا حبيبي امشي نخلف 🤤🔞**")
    

@jepiq.on(admin_cmd(pattern="رفع زاحف(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5582470474:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    jepthon = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**⌯︙المستخدم** [{jepthon}](tg://user?id={user.id}) \n**⌯︙ تـم رفع المتهم زاحف اصلي بواسطة :** {my_mention} \n**⌯︙ ها يلزاحف شوكت تبطل سوالفك حيوان 😂🐍**")

@jepiq.on(admin_cmd(pattern="رفع كحبة(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5582470474:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    jepthon = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**⌯︙المستخدم** [{jepthon}](tg://user?id={user.id}) \n**⌯︙ تـم رفع المتهم كحبة 👙 بواسطة :** {my_mention} \n**⌯︙ ها يلكحبة طوبز خلي انيجك/ج**")

@jepiq.on(admin_cmd(pattern="رفع فرخ(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5582470474:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    jepthon = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**⌯︙المستخدم** [{jepthon}](tg://user?id={user.id}) \n**⌯︙ تـم رفعـه فرخ الكروب بواسطة :** {my_mention} \n**⌯︙ لك الفرخ استر على خمستك ياهو اليجي يزورهاً 👉🏻👌🏻**")

@jepiq.ar_cmd(
    pattern="رزله(?:\s|$)([\s\S]*)",
    command=("رزله", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5582470474:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 5582470474:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 5582470474:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور **")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(mention, f"⌯︙ولك [{tag}](tg://user?id={user.id}) \n⌯︙ هيو لتندك بسيادك لو بهاي 👞👈")

@jepiq.on(admin_cmd(pattern="رفع حاته(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5582470474:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    jepthon = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**⌯︙المستخدم** [{jepthon}](tg://user?id={user.id}) \n**⌯︙ تـم رفعـها حاته الكروب 🤤😻 بواسطة :** {my_mention} \n**⌯︙ تعاي يعافيتي اريد حضن دافي 😽**")

@jepiq.on(admin_cmd(pattern="رفع هايشة(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5582470474:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    jepthon = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**⌯︙المستخدم** [{jepthon}](tg://user?id={user.id}) \n**⌯︙ تـم رفعـه المتهم هايشة 🐄 بواسطة :** {my_mention} \n**⌯︙ ها يلهايشة خوش بيك حليب تعال احلبك 😂**")

@jepiq.on(admin_cmd(pattern="رفع صاك(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    jepthon = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**⌯︙المستخدم** [{jepthon}](tg://user?id={user.id}) \n**⌯︙ تـم رفعـه صاك 🤤 بواسطة :** {my_mention} \n**⌯︙ تعال يلحلو انطيني بوسة من رگبتك 😻🤤**")

@jepiq.ar_cmd(
    pattern="مصه(?:\s|$)([\s\S]*)",
    command=("مصه", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5582470474:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 5582470474:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 5582470474:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور **")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(mention, f"** ⣠⡶⠚⠛⠲⢄⡀\n⣼⠁      ⠀⠀⠀⠳⢤⣄\n⢿⠀⢧⡀⠀⠀⠀⠀⠀⢈⡇\n⠈⠳⣼⡙⠒⠶⠶⠖⠚⠉⠳⣄\n⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄\n⠀⠀⠀⠘⣆       ⠀⠀⠀⠀⠀⠈⠓⢦⣀\n⠀⠀⠀⠀⠈⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠲⢤\n⠀⠀⠀⠀⠀⠀⠙⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧\n⠀⠀⠀⠀⠀⠀⠀    ⠓⠦⠀⠀⠀⠀**\n**🚹 ¦ تعال مصه عزيزي ** [{tag}](tg://user?id={user.id})")

@jepiq.on(admin_cmd(pattern="روجر(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    await edit_or_reply(mention, f"سماحة روجر مطور سورس ريبثون @Jepthon - @ZQ_LO")

@jepiq.on(admin_cmd(pattern="رفع ايجة(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 705475246:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    jepthon = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**⌯︙المستخدم** [{jepthon}](tg://user?id={user.id}) \n**⌯︙ تـم رفعـه ايچة 🤤 بواسطة :** {my_mention} \n**⌯︙ ها يلأيچة تطلعين درب بـ$25 👙**")

@jepiq.on(admin_cmd(pattern="رفع زبال(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5582470474:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    jepthon = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**⌯︙المستخدم** [{jepthon}](tg://user?id={user.id}) \n**⌯︙ تـم رفعـه زبال الكروب 🧹 بواسطة :** {my_mention} \n**⌯︙ تعال يلزبال اكنس الكروب لا أهينك 🗑😹**")

@jepiq.on(admin_cmd(pattern="رفع كواد(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5582470474:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    jepthon = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**⌯︙المستخدم** [{jepthon}](tg://user?id={user.id}) \n**⌯︙ تـم رفعه كواد بواسطة :** {my_mention} \n**⌯︙ تعال يكواد عرضك مطشر اصير حامي عرضك ؟😎**")

@jepiq.on(admin_cmd(pattern="رفع ديوث(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5582470474:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    jepthon = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**⌯︙المستخدم** [{jepthon}](tg://user?id={user.id}) \n**⌯︙ تـم رفعه ديوث الكروب بواسطة :** {my_mention} \n**⌯︙ تعال يلديوث جيب اختك خلي اتمتع وياها 🔞**")

@jepiq.on(admin_cmd(pattern="رفع مميز(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5582470474:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    jepthon = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**⌯︙الحلو** 「[{jepthon}](tg://user?id={user.id})」 \n**⌯︙ تـم رفعه مميز بواسطة :** {my_mention}")

@jepiq.on(admin_cmd(pattern="رفع ادمن(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5582470474:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    jepthon = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**⌯︙الحلو** 「[{jepthon}](tg://user?id={user.id})」 \n**⌯︙ تـم رفعه ادمن بواسطة :** {my_mention}")

@jepiq.on(admin_cmd(pattern="رفع منشئ(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5582470474:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    jepthon = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**⌯︙الحلو** 「[{jepthon}](tg://user?id={user.id})」 \n**⌯︙ تـم رفعه منشئ بواسطة :** {my_mention}")

@jepiq.on(admin_cmd(pattern="رفع مالك(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5582470474:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    jepthon = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**⌯︙الحلو** 「[{jepthon}](tg://user?id={user.id})」 \n**⌯︙ تـم رفعه مالك الكروب بواسطة :** {my_mention}")

@jepiq.on(admin_cmd(pattern="رفع مجنب(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    jepthon = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f" ** ⌯︙ المستخدم => • ** [{jepthon}](tg://user?id={user.id}) \n ☑️ **⌯︙ تم رفعه مجنب بواسطه  :**{my_mention} .\n**⌯︙ كوم يلمجنب اسبح مو عيب تضرب جلغ 😹** ")

@jepiq.on(admin_cmd(pattern="رفع وصخ(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    jepthon = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"** ⌯︙ المستخدم => • ** [{jepthon}](tg://user?id={user.id}) \n ☑️ **⌯︙ تم رفعه وصخ الكروب 🤢 بواسطه  :**{my_mention} .\n**⌯︙ لك دكوم يلوصخ اسبح مو ريحتك كتلتنا 🤮 ** ")

@jepiq.on(admin_cmd(pattern="زواج(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    jepthon = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"⌯︙** لقد تم زواجك/ج من : **[{jepthon}](tg://user?id={user.id}) 💍\n**⌯︙ الف الف مبروك الان يمكنك اخذ راحتك ** ")

@jepiq.on(admin_cmd(pattern="طلاك(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    jepthon = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**⌯︙ انتِ طالق طالق طالق 🙎🏻‍♂️ من  :**{my_mention} .\n**⌯︙ لقد تم طلاقها بلثلاث وفسخ زواجكما الان الكل حر طليق ** ")
ownersayed_id = 5582470474
@jepiq.on(events.NewMessage(outgoing=False, pattern='منصب؟'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownersayed_id or sender.id == 1887927704:
        order = await event.reply('يب منصب ✓')
ownersayed1_id = 5582470474
@jepiq.on(events.NewMessage(outgoing=False, pattern='منو يحبني؟'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownersayed1_id :
        order = await event.reply('منو مايحبك ورده ❤️')
