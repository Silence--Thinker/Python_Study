#!/usr/bin/python
#-*- coding: utf-8 -*-

from enum import Enum, unique # pip install --upgrade pip enum34

# 枚举
@unique
class Team(Enum):
    B = 0
    C = 1
# 枚举
@unique
class CodeLanguage(Enum):
    JS = 0
    iOS = 1
    Android = 2
# 枚举
@unique
class Source(Enum):
    name = 0
    git = 1
    branch = 2
    type = 3
    chdir = 4 # 目标目录
    team = 5
@unique
class Table(Enum):
    team ='Team'
    platform = '平台'
    codeRatePlatform = '有效代码率(代码行/总行数)'
    commentRatePlatform ='注释率(注释行/总行数)'
    gitName = '库名称'
    branch = '分支'
    lineCount = '代码总行数'
    codeCount = '有效代码行数'
    commentCount = '注释总行数'
    spaceCount = '空行总数'
    codeRate = '有效代码比'

FILETYPE_DICT = {
    CodeLanguage.iOS: '\.h$|\.m$|\.mm$',
    CodeLanguage.Android: '\.java$',
    CodeLanguage.JS: '\.tsx$|\.js$|\.jsx$|\.ts$'
}

# 测试代码配置
sourceList = [
    ################### C端 #####################
    #iOS
    {Source.name: "supermarket_ios_channel", Source.git: "ssh://git@git.sankuai.com/reco/supermarket_ios_channel.git", 
     Source.branch: "7.38/development", Source.type: CodeLanguage.iOS, Source.team: Team.C, Source.chdir: "/Classes"},

    {Source.name: "supermarket_ios_search", Source.git: "ssh://git@git.sankuai.com/reco/supermarket_ios_search.git", 
     Source.branch: "7.38/development", Source.type: CodeLanguage.iOS, Source.team: Team.C, Source.chdir: "/Classes"},
    
    {Source.name: "supermarket_ios_kit", Source.git: "ssh://git@git.sankuai.com/reco/supermarket_ios_kit.git", 
     Source.branch: "7.38/development", Source.type: CodeLanguage.iOS, Source.team: Team.C, Source.chdir: "/Classes"},
    
    {Source.name: "supermarket_ios_mediator", Source.git: "ssh://git@git.sankuai.com/reco/supermarket_ios_mediator.git", 
     Source.branch: "7.38/development", Source.type: CodeLanguage.iOS, Source.team: Team.C, Source.chdir: "/Classes"},

    {Source.name: "supermarket_ios_platform", Source.git: "ssh://git@git.sankuai.com/reco/supermarket_ios_platform.git", 
     Source.branch: "7.38/development", Source.type: CodeLanguage.iOS, Source.team: Team.C, Source.chdir: "/Classes"},

    # Android
    {Source.name: "waimai_android_store", Source.git: "ssh://git@git.sankuai.com/wm/waimai_android_store.git", 
     Source.branch: "develop", Source.type: CodeLanguage.Android, Source.team: Team.C, Source.chdir: "/library"},
    
    {Source.name: "reco_android_c_im", Source.git: "ssh://git@git.sankuai.com/reco/reco_android_c_im.git", 
     Source.branch: "develop", Source.type: CodeLanguage.Android, Source.team: Team.C, Source.chdir: "/library"},
    
    {Source.name: "reco_android_c_search", Source.git: "ssh://git@git.sankuai.com/reco/reco_android_c_search.git", 
     Source.branch: "develop", Source.type: CodeLanguage.Android, Source.team: Team.C, Source.chdir: "/library"},

    {Source.name: "reco_android_c_platform", Source.git: "ssh://git@git.sankuai.com/reco/reco_android_c_platform.git", 
     Source.branch: "develop", Source.type: CodeLanguage.Android, Source.team: Team.C, Source.chdir: "/library"},

    {Source.name: "reco-android-common-core", Source.git: "ssh://git@git.sankuai.com/reco/reco-android-common-core.git", 
     Source.branch: "master", Source.type: CodeLanguage.Android, Source.team: Team.C, Source.chdir: "/library"},

    #JS
    {Source.name: "flashbuy_mrn", Source.git: "ssh://git@git.sankuai.com/reco/flashbuy_mrn.git", 
     Source.branch: "developer", Source.type: CodeLanguage.JS, Source.team: Team.C, Source.chdir: "/src"},
    
    {Source.name: "flashbuy_mrn_common", Source.git: "ssh://git@git.sankuai.com/reco/flashbuy_mrn_common.git", 
     Source.branch: "developer", Source.type: CodeLanguage.JS, Source.team: Team.C, Source.chdir: "/src"},

    ################### B端 #####################
    #iOS
    {Source.name: "waimai_ios_e_retail_kit", Source.git: "ssh://git@git.sankuai.com/wm/waimai_ios_e_retail_kit.git", 
     Source.branch: "master", Source.type: CodeLanguage.iOS, Source.team: Team.B, Source.chdir: ""},
    
    {Source.name: "reco_ios_e_retail_platform", Source.git: "ssh://git@git.sankuai.com/reco/reco_ios_e_retail_platform.git", 
     Source.branch: "master", Source.type: CodeLanguage.iOS, Source.team: Team.B, Source.chdir: "/Classes"},
    
    {Source.name: "reco_ios_e_retail_channel", Source.git: "ssh://git@git.sankuai.com/reco/reco_ios_e_retail_channel.git", 
     Source.branch: "development", Source.type: CodeLanguage.iOS, Source.team: Team.B, Source.chdir: "/Classes"},
    
    {Source.name: "reco_ios_e_retail_order", Source.git: "ssh://git@git.sankuai.com/reco/reco_ios_e_retail_order.git", 
     Source.branch: "master", Source.type: CodeLanguage.iOS, Source.team: Team.B, Source.chdir: "/Classes"},

    {Source.name: "reco_ios_e_retail_shop", Source.git: "ssh://git@git.sankuai.com/reco/reco_ios_e_retail_shop.git", 
     Source.branch: "development", Source.type: CodeLanguage.iOS, Source.team: Team.B, Source.chdir: "/Classes"},

    #Android
    {Source.name: "waimai_sc_android_b_product", Source.git: "ssh://git@git.sankuai.com/reco/waimai_sc_android_b_product.git", 
     Source.branch: "master", Source.type: CodeLanguage.Android, Source.team: Team.B, Source.chdir: ""},

    {Source.name: "reco_sc_android_b_order", Source.git: "ssh://git@git.sankuai.com/reco/reco_sc_android_b_order.git", 
     Source.branch: "master", Source.type: CodeLanguage.Android, Source.team: Team.B, Source.chdir: ""},

    {Source.name: "reco_sc_android_b_common", Source.git: "ssh://git@git.sankuai.com/reco/reco_sc_android_b_common.git", 
     Source.branch: "master", Source.type: CodeLanguage.Android, Source.team: Team.B, Source.chdir: ""},

    {Source.name: "reco_android_uppershelf", Source.git: "ssh://git@git.sankuai.com/reco/reco_android_uppershelf.git", 
     Source.branch: "master", Source.type: CodeLanguage.Android, Source.team: Team.B, Source.chdir: ""},

    {Source.name: "reco_android_shelf_controller", Source.git: "ssh://git@git.sankuai.com/set/reco_android_shelf_controller.git", 
     Source.branch: "master", Source.type: CodeLanguage.Android, Source.team: Team.B, Source.chdir: ""},
    
    {Source.name: "reco_android_store_order", Source.git: "ssh://git@git.sankuai.com/reco/reco_android_store_order.git", 
     Source.branch: "master", Source.type: CodeLanguage.Android, Source.team: Team.B, Source.chdir: ""},
    
    {Source.name: "reco_energize_android", Source.git: "ssh://git@git.sankuai.com/reco/reco_energize_android.git", 
     Source.branch: "master", Source.type: CodeLanguage.Android, Source.team: Team.B, Source.chdir: ""},
    
    {Source.name: "reco_energize_kit_android", Source.git: "ssh://git@git.sankuai.com/reco/reco_energize_kit_android.git", 
     Source.branch: "master", Source.type: CodeLanguage.Android, Source.team: Team.B, Source.chdir: ""},
     
    #JS
    {Source.name: "reco_sc_mrn_b", Source.git: "ssh://git@git.sankuai.com/reco/reco_sc_mrn_b.git", 
     Source.branch: "development", Source.type: CodeLanguage.JS, Source.team: Team.B, Source.chdir: "/src"},
]
