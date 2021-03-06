# from pprint import pprint
# import json
import asyncio
# import operator
# import os
import dateparser
from datetime import datetime
from pytz import timezone
import re
import discord
# from discord.ext import commands

from utils.db import initialize_db
from utils.channel import get_channel

from gspread.exceptions import APIError


class Scheduler:
    """a cog for scheduling stuff"""

    def __init__(self, bot):
        self.bot = bot
        self.db = initialize_db()

    async def check_gms_schedule(self, delay=30):

        print('[GMS Schedule Checker] Waiting for ready state...')

        await self.bot.wait_until_ready()

        print('[GMS Schedule Checker] Ready and running!')
        server = self.bot.get_guild(id=453555802670759947)
        gms_noti_role = discord.utils.get(server.roles, name='Notify GMS')

        while not self.bot.is_closed():
            # print('Schedule Check for GMS: ...')
            try:
                schedule_db = self.db.worksheet('schedules_ms')
                data = schedule_db.get_all_records()
                for row_index, row in enumerate(data, start=2):
                    en = row['event_name'].lower()
                    # pass if posted
                    if row['posted']:
                        pass
                    # pass events of GMSM
                    elif en.startswith('[gmsm]') or en.startswith('.gmsm.'):
                        pass
                    elif en.startswith('[gms]') or en.startswith('.gms.'):
                        # parse and convert to UTC, order set to DMY
                        dt = dateparser.parse(row['date_time'], settings={'TIMEZONE': 'UTC', 'DATE_ORDER': 'DMY'})
                        # get UTC now and convert to timezone-aware
                        now = datetime.utcnow().replace(tzinfo=timezone('UTC'))

                        time_diff = (dt - now).total_seconds()
                        # event incoming, just pass
                        if time_diff > 0:
                            pass
                        # event has started
                        else:
                            # send the notification here!
                            channel = get_channel(bot=self.bot, id=461067276980977674)

                            tag_re = re.compile('(\[|\.)*gms(\]|\.)*\s*', re.IGNORECASE)
                            event_name = tag_re.sub('', row['event_name'], 1).title()

                            await gms_noti_role.edit(mentionable=True)
                            await channel.send(f'{gms_noti_role.mention} {event_name}.')
                            await gms_noti_role.edit(mentionable=False)
                            schedule_db.update_cell(row_index, 3, 'x')
                            print(f'Schedule Check for GMS: Posted `{event_name}` to channel {channel.id}')
            except APIError:
                pass
            # print('Schedule Check for GMS: Done.')
            await asyncio.sleep(delay)

    async def check_gmsm_schedule(self, delay=30):

        print('[GMSM Schedule Checker] Waiting for ready state...')

        await self.bot.wait_until_ready()

        print('[GMSM Schedule Checker] Ready and running!')

        server = self.bot.get_guild(id=453555802670759947)
        gmsm_noti_role = discord.utils.get(server.roles, name='Notify GMSM')

        while not self.bot.is_closed():
            # print('Schedule Check for GMSM: ...')
            try:
                schedule_db = self.db.worksheet('schedules_ms')
                data = schedule_db.get_all_records()
                for row_index, row in enumerate(data, start=2):
                    en = row['event_name'].lower()
                    # pass if posted
                    if row['posted']:
                        pass
                    # pass events of GMSM
                    elif en.startswith('[gms]') or en.startswith('.gms.'):
                        pass
                    elif en.startswith('[gmsm]') or en.startswith('.gmsm.'):
                        # parse and convert to UTC, order set to DMY
                        dt = dateparser.parse(row['date_time'], settings={'TIMEZONE': 'UTC', 'DATE_ORDER': 'DMY'})
                        # get UTC now and convert to timezone-aware
                        now = datetime.utcnow().replace(tzinfo=timezone('UTC'))

                        time_diff = (dt - now).total_seconds()
                        # event incoming, just pass
                        if time_diff > 0:
                            pass
                        # event has started
                        else:
                            # send the notification here!
                            channel = get_channel(bot=self.bot, id=461067191735943168)

                            tag_re = re.compile('(\[|\.)*gmsm(\]|\.)*\s*', re.IGNORECASE)
                            event_name = tag_re.sub('', row['event_name']).title()
                            await gmsm_noti_role.edit(mentionable=True)
                            await channel.send(f'{gmsm_noti_role.mention} {event_name}.')
                            await gmsm_noti_role.edit(mentionable=False)
                            schedule_db.update_cell(row_index, 3, 'x')
                            print(f'Schedule Check for GMSM: Posted `{event_name}` to channel {channel.id}')
            except APIError:
                pass
            # print('Schedule Check for GMSM: Done.')
            await asyncio.sleep(delay)

    async def check_dawn_schedule(self, delay=30):

        print('[Dawn SAOMD Schedule Checker] Waiting for ready state...')

        await self.bot.wait_until_ready()

        print('[Dawn SAOMD Schedule Checker] Ready and running!')

        while not self.bot.is_closed():
            # print('Schedule Check for Dawn - SAOMD: ...')
            try:
                schedule_db = self.db.worksheet('schedules_saomd')
                data = schedule_db.get_all_records()
                for row_index, row in enumerate(data, start=2):
                        # pass if posted
                    if row['posted']:
                        pass
                    # pass events of GMSM
                    else:
                        # parse and convert to UTC, order set to DMY
                        dt = dateparser.parse(row['date_time'], settings={'TIMEZONE': 'UTC', 'DATE_ORDER': 'DMY'})
                        # get UTC now and convert to timezone-aware
                        now = datetime.utcnow().replace(tzinfo=timezone('UTC'))

                        time_diff = (dt - now).total_seconds()
                        # event incoming, just pass
                        if time_diff > 0:
                            pass
                        # event has started
                        else:
                            # send the notification here!
                            channel = get_channel(bot=self.bot, id=373663985368563717)

                            event_name = row['event_name'].title()
                            await channel.send(f'{event_name}.')
                            schedule_db.update_cell(row_index, 3, 'x')
                            print(f'Schedule Check for Dawn - SAOMD: Posted `{event_name}` to channel {channel.id}')
            except APIError:
                pass
            # print('Schedule Check for Dawn - SAOMD: Done.')
            await asyncio.sleep(delay)


def setup(bot):
    bot.add_cog(Scheduler(bot))
