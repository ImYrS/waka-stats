"""
    @Author: ImYrS Yang
    @Date: 2022/6/20
    @Copyright: ImYrS Yang
    @Description: 
"""

import os
import datetime

from github import Github
from github.GithubException import *

from config import GITHUB_TOKEN

if os.name == 'nt':
    # 设置 HTTP 和 HTTPS 代理
    os.environ['http_proxy'] = 'http://127.0.0.1:1080'
    os.environ['https_proxy'] = 'http://127.0.0.1:1080'

g = Github(GITHUB_TOKEN)

me = g.get_user()

for repo in me.get_repos():
    if repo.owner.login != me.login:
        continue

    repo_printed = False

    try:
        for commit in repo.get_commits():
            if commit.author:
                # print(
                #     commit.commit.author.date,
                #     datetime.datetime(2022, 6, 20),
                #     commit.commit.author.date < datetime.datetime(2022, 6, 1),
                #     commit.author.login
                # )

                # 获取 commit 时间
                if commit.commit.author.date < datetime.datetime(2022, 5, 20):
                    break
                if commit.author.login == me.login:
                    if not repo_printed:
                        print(f'\n{repo.name}')
                        repo_printed = True

                    print('\t-->', commit.commit.message.ljust(50), 'at', commit.commit.author.date)
    except GithubException:
        pass
