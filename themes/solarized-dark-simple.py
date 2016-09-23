class Color(DefaultColor):
    USERNAME_FG = 15
    USERNAME_BG = 4
    USERNAME_ROOT_BG = 1

    HOSTNAME_FG = 15
    HOSTNAME_BG = 10

    HOME_SPECIAL_DISPLAY = False
    PATH_FG = 7
    PATH_BG = 10
    CWD_FG = 15
    SEPARATOR_FG = 14

    READONLY_BG = 1
    READONLY_FG = 7

    REPO_CLEAN_FG = 14
    REPO_CLEAN_BG = 0
    REPO_DIRTY_FG = 3
    REPO_DIRTY_BG = 0

    JOBS_FG = 4
    JOBS_BG = 8

    CMD_PASSED_FG = 15
    CMD_PASSED_BG = 2
    CMD_FAILED_FG = 15
    CMD_FAILED_BG = 1

    SVN_CHANGES_FG = REPO_DIRTY_FG
    SVN_CHANGES_BG = REPO_DIRTY_BG

    VIRTUAL_ENV_BG = 15
    VIRTUAL_ENV_FG = 2


class Symbol(DefaultSymbol):
    """
    This class should have the default symbol for every segment.
    Please test every new segment with this theme first.
    """
    symbols = {
        'generic': {
            'compatible': {
                'lock': 'RO',
                'network': 'SSH',
                'separator': u'\u25B6',
                'separator_thin': u'\u276F'
            },
            'patched': {
                'lock': u'\uE0A2',
                'network': u'\uE0A2',
                'separator': u'\uE0B0',
                'separator_thin': u'\uE0B1'
            },
            'flat': {
                'lock': '',
                'network': '',
                'separator': '',
                'separator_thin': ''
            }
        },
        'repo' : {
            'branch': u'\uE0A0',
            'detached': u'\u2693',
            'ahead': u'\u21E1',
            'behind': u'\u21E3',
            'staged': u'\u2714',
            'not_staged': u'\u270E',
            'untracked': '+',
            'conflicted': u'\u273C'
        }
    }

    # Show Count Statics on modified/added files
    count = False



