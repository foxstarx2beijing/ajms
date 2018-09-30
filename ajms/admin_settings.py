# suit configuration
SUIT_CONFIG = {  # suit页面配置
    'ADMIN_NAME': '需求管理平台',  #登录界面提示
    'LIST_PER_PAGE': 20,
    'SHOW_REQUIRED_ASTERISK': True, 
    'CONFIRM_UNSAVED_CHANGES': True, 
    'MENU': (
        {'label': u'配置', 'icon':'icon-cog', 'app': 'demand', 'models': ('priority', 'human_type', 'human', 'demand', 'demand_status')},  #每一个字典表示左侧菜单的一栏
             # {'label': u'SQL管理', 'app': 'web_sso', 'models': ('web_sso.Sql', 'web_sso.PreSql', 'web_sso.Direction')},  # 可以是多个字典
        # Reorder app models
        {'app': 'auth', 'models': ('user', 'group')},
             ),
    # label表示name，app表示上边的install的app，models表示用了哪些models
}