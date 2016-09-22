class Color(DefaultColor):
    """
    This subclass is required when the user chooses to use 'default' theme.
    Because the segments require a 'Color' class for every theme.
    """
    GIT_UNTRACKED_BG = 23
    GIT_UNTRACKED_FG = 15


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
            'branch': u'\uE0A0',        # branch symbol
            'detached': u'\u2693',      #
            'ahead': u'\u2B06',         #
            'behind': u'\u2B07',
            'staged': u'\u2714',
            'not_staged': u'\u270E',    # pencil
            # 'untracked': u'\u2753',
            'untracked': u'\u2363',
            # 'untracked': u'\u2618',
            'conflicted': u'\u273C'
            # 'conflicted': u'\u2694'
        }
    }