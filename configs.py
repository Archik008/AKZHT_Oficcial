positions = {
    "before_M6": (100, 250),
    "M6": (150, 250),
    "Ч4": (400, 300),
    "Ч2": (420, 250),
    "H4": (250, 300),
    "H2": (250, 250),
    "1_AK":(100, 190),
    "M8": (230, 190),
    "M10": (220, 140),
    "before_M10": (150, 140),
    "H5": (290, 80),
    "H3": (290, 140),
    "H1": (300, 190),
    "Ч1": (440, 190),
    "Ч3": (420, 140),
    "Ч5": (420, 80),
    "M7": (520, 140),
    "M9": (670, 140),
    "M5": (520, 250),
    "M3": (650, 250),
    "6": (850, 250),
    "4": (980, 250),
    "M1": (650, 190),
    "H": (750, 190),
    "1":(880, 190),
    "3":(990, 190),
    "Mb_depo":(790, 140),
    "Turn_14_J": (190, 250),
    # "M3": (, 230),
    # "M1": (),
    # "H5": ()
    # "M1": (1000, 330),
    # "M8": (850, 330),
    # "M8mid": (970, 330),
    # "H1": (500, 330),
    # "1STR": (380, 330),
    # "M2": (150, 330),
    # "M6H2": (445, 230),
    # "M10": (850, 430),
    # "H3": (390, 430),
    # "M6": (300, 230),
    # "H2": (620, 230),
    # "1": (760, 330),
    # "2": (760, 230),
    # "3": (760, 430),
    # "4": (760, 130),
    # "H4": (620, 130),
    # "past4": (970, 130),
    # "Ч": (70, 330),
    # "past2": (970, 230),
    # "pastM1": (1090, 330),
    # "beforeM6": (230, 230),
    # "M2H1_mid": (260, 330),
    # "M2H1_third": (340, 330),
    # "ALB_Sect0": (80, 500),
    # "ALB_Sect1": (325, 500),
    # "ALB_Sect2": (175,500),
    # "ALB_Sect1-2":(250,500),
    # "ALB_Sect1-2_2":(250,500)
}
segments = [
    # 3 line
    ("before_M10", "M10"),
    ("M10", "H3"),
    ("M8", "H1"),
    ("H3", "Ч3"),
    ("Ч3", "M7"),
    ("M7", "M9"),
    ("M9", "Mb_depo"),

    # 5 line
    ("H5", "Ч5"),


    # 1 line
    ("1_AK", "M8"),
    ("M8", "H1"),
    ("H1", "Ч1"),
    ("Ч1", "H"),
    ("H", "1"),
    ("1", "3"),

    # 2 line
    ("before_M6", "M6"),
    ("M6", "Turn_14_J"),
    ("Turn_14_J", "H2"),
    ("H2", "Ч2"),
    ("Ч2", "M5"),
    ("M5", "M3"), 
    ("M3", "6"),
    ("6", "4"),

    # 4 line
    ("H4", "Ч4")
]
DRAW_TRACKS = True


SEGMENT_ORDER = [
    # Твои 6 реальных сегментов (названия строго как в ключах кортежей)
    ("M6", "beforeM6"),
    ("M2", "Ч"),
    ("M10", "H3"),
    ("M8", "H1"),
    ("M10", "H3"),
    ("M8mid", "M8"),
    ("M2", "M2H1_mid"),
    ("ALB_Sect1", "ALB_Sect1-2"),
    ("M6H2", "M6"),


    # И 18 пустых заглушек, чтобы цикл в Python не упал
    "EMPTY", "EMPTY", "EMPTY", "EMPTY",
    "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY",
    "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY"
]

segment_to_block = {}
segment_to_block_type = {}


segment_groups = {
    "block_M2_H1": [
        {"type": "segment", "id": ("M2","M2H1_mid")},
        {"type": "segment", "id": ("M2H1_mid", "M2H1_third")},
        {"type": "segment", "id": ("M2H1_third","H1")},
        {"type": "diag", "name": "ALB_Turn6"},
        {"type": "diag", "name": "ALB_Turn2"},

    ],
    "block_M6_H2_Turns": [
        {"type": "segment", "id": ("H2", "M6H2")},
        {"type": "segment", "id": ("M6H2", "M6")},
        {"type": "diag", "name": "ALB_Turn4"},
        {"type": "diag", "name": "ALB_Turn8"},
    ],
    "block_M8_M1":[
        {"type": "segment", "id": ("M8mid", "M8")},
        {"type": "segment", "id": ("M8mid", "M1")},
        {"type": "diag", "name": "ALB_Turn1"},
    ],

}

split_parts_map = {
    "ALB_Turn4-6": {
        "partA": "ALB_Turn6",
        "partB": "ALB_Turn4"
    }
}
switch_list = ["ALB_Turn1", "ALB_Turn2", "ALB_Turn8", "ALB_Turn4-6", "Turn_14", "Turn_16"]

default_switch_mode = {
    "ALB_Turn1": "left",
    "ALB_Turn2": "left",
    "ALB_Turn8":  "left",
    "ALB_Turn4-6":  "left",
    "Turn_16": "left",
    "Turn_14": "left",
}

# Толщина прямых сегментов при положении стрелки: left = «+», right = «-»
TRACK_WIDTH_MAIN = 6
TRACK_WIDTH_THIN = 2

switch_segment_width = {
    "Turn_14": {
        "left": {
            ("M6", "Turn_14_J"): 6,
            ("Turn_14_J", "H2"): 6,
        },
        "right": {
            ("M6", "Turn_14_J"): 6,      # ход на стрелку / в H4 — толстый
            ("Turn_14_J", "H2"): 2,      # отворот к H2 — тонкий (не по маршруту)
        },
    },
}

segment_to_signal = {
    ('M8', 'M8mid'): "M8",
    ('M1', 'M8mid'): "M8",
    ("M2", "Ч"): "Ч",
    ("M2", "M2H1_mid"): "H1",
    ("M2H1_mid", "M2H1_third"): "H1",
    ("M2H1_third", "H1"): "H1",

    ('M1', 'M8mid'): "M1",
    ('M8mid', 'M8'): "M1",
    #("pastM1", "M1"): "M1",
    #("M10", "H3"): "H3",
    ("M2", "M2H1_mid"): "M2",
    ("M2H1_mid", "M2H1_third"): "M2",
    ("M2H1_third", "H1"): "M2",
    ("H2", "M6H2"): "H2",
    ("M6", "M6H2"): "M6",

}

diag_to_signal = {
    "ALB_Turn1": "M10",
    "ALB_Turn8": "H4",
    "ALB_Turn2": "H3",

}
diagonal_config = {
    "ALB_Turn1": {
        "left":  {"exists": True, "connected": 0,  "disconnected": 0},
        "right": {"exists": True, "connected": -5, "disconnected": +5},
        "default": "both"
    },
    "ALB_Turn2": {
        "left":  {"exists": True, "connected": 0,  "disconnected": 0},
        "right": {"exists": True, "connected": -5, "disconnected": +5},
        "default": "both"
    },

    "ALB_Turn8": {
        "left":  {"exists": True, "connected": -5, "disconnected": +5},
        "right": {"exists": True, "connected": 0,  "disconnected": 0},
        "default": "both"
    },

    "ALB_Turn4-6": {
        "left":  {"exists": True, "connected": +5, "disconnected": 0},
        "right": {"exists": True, "connected": +5, "disconnected": 0},
        "default": "both"
    },
    "Turn_14": {
        "left":  {"exists": True, "connected": 0, "disconnected": 0},
        "right": {"exists": True, "connected": 0, "disconnected": 0},
        "default": "both",
    },
}

signals_config_simple = {
    "Ч": {
        "mount": "bottom",
        "pack_side": "right",
        "count": 2,
        "colors": ["red", "white", "yellow"],
        "position_map": {
            "red": [0],
            "white": [0],
            "green": [0],
            "yellow1": [0, 1],
            "yellow2": [0, 1],
        }
    },
    "M2": {
        "mount": "bottom",
        "pack_side": "right",
        "count": 1,
        "colors": ["grey", "white"],
        "single": True,
    },

    "H1": {
        "mount": "top",
        "pack_side": "left",
        "count": 1,
        "colors": ["grey", "white"],
        "single": True,
    },
    "H2": {
        "mount": "top",
        "pack_side": "left",
        "count": 1,
        "colors": ["grey", "white"],
        "single": True
    },
    "H3": {
        "mount": "top",
        "pack_side": "left",
        "count": 1,
        "colors": ["grey", "white"],
        "single": True
    },
    "H4": {
        "mount": "top",
        "pack_side": "left",
        "count": 1,
        "colors": ["grey", "white"],
        "single": True
    },

    "M6": {
        "mount": "bottom",
        "pack_side": "right",
        "count": 1,
        "colors": ["grey", "white"],
        "single": True
    },
    "M8": {
        "mount": "bottom",
        "pack_side": "right",
        "count": 1,
        "colors": ["grey", "white"],
        "single": True
    },
    "M10": {
        "mount": "bottom",
        "pack_side": "right",
        "count": 1,
        "colors": ["grey", "white"],
        "single": True
    },
    "M1": {
        "mount": "top",
        "pack_side": "left",
        "count": 1,
        "colors": ["grey", "white"],
        "single": True
    },
    "ALB_Sect1-2": {
        "mount": "top",
        "pack_side": "left",
        "count": 1,
        "colors": ["grey", "white"],
    },
    "ALB_Sect1-2_2": {
        "mount": "bottom",
        "pack_side": "right",
        "count": 1,
        "colors": ["grey", "white"],
    },
    "ALB_Sect2": {
        "mount": "top",
        "pack_side": "left",
        "count": 2,
        "colors": ["red", "white"],
    }
}




signals_config = {
    "Ч": {
        "mount": "bottom",
        "pack_side": "right",
        "count": 5,
        "colors": ["white", "yellow", "red", "green", "yellow1"],
    },
    "M2": {
        "mount": "bottom",
        "pack_side": "right",
        "count": 2,
        "colors": ["blue", "white"],
        "type": "maneuver"
    },
    "H1": {
        "mount": "top",
        "pack_side": "left",
        "count": 4,
        "colors": ["white", "red", "green", "yellow"],
        "type": "train"
    },
    "H2": {
        "mount": "top",
        "pack_side": "left",
        "count": 4,
        "colors": ["white", "red", "green", "yellow"],
        "type": "train"
    },
    "H3": {
        "mount": "top",
        "pack_side": "left",
        "count": 4,
        "colors": ["white", "red", "green", "yellow"],
        "type": "train"
    },
    "H4": {
        "mount": "top",
        "pack_side": "left",
        "count": 4,
        "colors": ["white", "red", "green", "yellow"],
        "type": "train"
    },
    "M6": {
        "mount": "bottom",
        "pack_side": "right",
        "count": 2,
        "colors": ["red", "white"],
        "type": "maneuver"
    },
    "M8": {
        "mount": "bottom",
        "pack_side": "right",
        "count": 2,
        "colors": ["red", "white"],
        "type": "maneuver"
    },
    "M10": {
        "mount": "bottom",
        "pack_side": "right",
        "count": 2,
        "colors": ["red", "white"],
        "type": "maneuver"
    },
    "M1": {
        "mount": "top",
        "pack_side": "left",
        "count": 2,
        "colors": ["white", "red"],
        "type": "maneuver"
    },
    "ALB_Sect1-2": {
        "mount": "top",
        "pack_side": "left",
        "count": 3,
        "colors": ["yellow", "green", "red"],
        "type": "none"
    },
    "ALB_Sect1-2_2": {
        "mount": "bottom",
        "pack_side": "right",
        "count": 3,
        "colors": ["yellow", "green", "red"],
        "type": "none"
    },
    "ALB_Sect2": {
        "mount": "top",
        "pack_side": "left",
        "count": 5,
        "colors": ["yellow", "green", "red", "black", "white"],
        "type": "none"
    }
}
ROUTE_SIGNAL_MAP: dict[tuple[str, str], dict[str, dict[str, object]]] = {
    ("M1", "M8"): {
        "M1": {"lamps": {"white": {"on": True, "blink": False}, }, },
    },
    ("M1", "H1"): {
        "M1": {"lamps": {"white": {"on": True, "blink": False}, }, },
    },
    ("M1", "M10"): {
        "M1": {"lamps": {"white": {"on": True, "blink": False}, }, },
    },
    ("M1", "M2"): {
        "M1": {"lamps": {"white": {"on": True, "blink": False}, }, },
        "H1": { "lamps": { "green": {"on": True, "blink": False},} },
    },
    ("M2", "H3"): {
        "M2": { "lamps": { "white": {"on": True, "blink": False}, } },
    },
    ("M2", "M10"): {
        "M2": {"lamps": { "white": {"on": True, "blink": False},} },
    },
    ("M2", "H1"):{
        "M2": {"lamps": { "white": {"on": True, "blink": False}, } },
    },
    ("M2", "M8"): {
        "M2": {"lamps": {"white": {"on": True, "blink": False}, }}, },
    ("M2", "M1"): {
        "M2": {"lamps": {"white": {"on": True, "blink": False}, }, },
        "M8": {"lamps": {"white": {"on": True, "blink": False}, }, },
    },
    ("M2", "H2"): {
        "M2": {"lamps": {"white": {"on": True, "blink": False}, }, },
    },
    ("M2", "H1"): {
        "M2": {"lamps": {"white": {"on": True, "blink": False}, }},
    },
    ("M2", "H4"): {
        "M2": {"lamps": {"white": {"on": True, "blink": False}, }},
    },
    ("H4", "M2"): {
        "H4": {"lamps": { "green": {"on": False, "blink": False}, "yellow": {"on": True, "blink": False}, }, },
    },
    ("M2", "2"): {
        "M2": {"lamps": {"white": {"on": True, "blink": False}, }},
    },
    ("M2", "4"): {
        "M2": {"lamps": {"white": {"on": True, "blink": False}, }},
    },
    ("M2", "1"): {
        "M2": {"lamps": {"white": {"on": True, "blink": False}, }},
    },
    ("M6", "H2"): {
        "M6": {"lamps": {"white": {"on": True, "blink": False},} },},
    ("M6", "H4"): {
        "M6": {"lamps": {"white": {"on": True, "blink": False}, }, },
    },
    ("M8", "M1"): {
        "M8": { "lamps": { "white": {"on": True, "blink": False}, "red": {"on": False, "blink": False},} },
    },

    ("M10", "M1"): {
        "M10": {"lamps": {"white": {"on": True, "blink": False}, "red": {"on": False, "blink": False}, }}, },
    ("M1", "H3"): {
        "M1": {"lamps": {"white": {"on": True, "blink": False}, "red": {"on": False, "blink": False}, }}, },

    ("H1", "M2"): {
        "H1": {"lamps": {"green": {"on": True, "blink": False}, }, },
    },
    ("H2", "M2"):{
        "H2": {"lamps": { "green": {"on": True, "blink": False}, "yellow": {"on": True, "blink": False}, }, },
    },
    ("H2", "M6"):{
        "H2": {"lamps": { "green": {"on": True, "blink": False} }, },
    },
    ("H4", "M6"):{
        "H4": {"lamps": { "green": {"on": True, "blink": False}, "yellow": {"on": True, "blink": False}, }, },
    },
    ("H3", "M2"): {
        "H3": {"lamps": {"green": {"on": True, "blink": False}, "yellow": {"on": True, "blink": False}, }, },
    },
    ("H3", "M10"): {
        "M10": {"lamps": {"white": {"on": True, "blink": False}, }, },
    },
    ("M6", "4"): {
        "M6": {"lamps": {"white": {"on": True, "blink": False} }, },
    },

    ("Ч", "1"): {
        "Ч": {"lamps": {"yellow1": {"on": True, "blink": False}, } },
        #"M2": {"lamps": {"white": {"on": True, "blink": False}, }, },
    },
    ("Ч", "2"): {
        "Ч": {"lamps": {"yellow": {"on": True, "blink": False}, "yellow1": {"on": True, "blink": False}, } },
       # "M2": {"lamps": {"white": {"on": True, "blink": False}, }, },
    },
    ("Ч", "3"): {
        "Ч": {"lamps": {"yellow": {"on": True, "blink": False}, "yellow1": {"on": True, "blink": False}, }   },
        #"M2": {"lamps": {"white": {"on": True, "blink": False}, }, },
    },
    ("Ч", "4"): {
        "Ч": {"lamps": {"yellow": {"on": True, "blink": False}, "yellow1": {"on": True, "blink": False}, }},
       # "M2": {"lamps": {"white": {"on": True, "blink": False}, }, },
    },
    ("Ч", "M1"):{
        "Ч": {"lamps": {"green": {"on": True, "blink": False}, "yellow": {"on": True, "blink": False}, }, },
    },
    ("H3", "Ч"):{
        "H3": {"lamps": {"green": {"on": True, "blink": False}, "yellow": {"on": True, "blink": False}, }, },
    },
    ("H1", "Ч"): {
        "H1": {"lamps": {"green": {"on": True, "blink": False}, "yellow": {"on": True, "blink": False}, }, },
    },
    ("H2", "Ч"): {
        "H2": {"lamps": {"green": {"on": True, "blink": False}, "yellow": {"on": True, "blink": False}, }, },
    },
    ("H4", "Ч"): {
        "H4": {"lamps": {"green": {"on": True, "blink": False}, "yellow": {"on": True, "blink": False}, }, },
    },


}

routes_dir = {
    ("M2", "H3"): "right",
    ("M2", "H1"): "right",
    ("M2", "M8"): "right",
    ("M2", "M1"): "right",
    ("M2", "M10"): "right",
    ("M2", "H2"): "right",
    ("M2", "H4"): "right",
    ("M2", "1"): "right",
    ("M2", "2"): "right",
    ("M2", "4"): "right",
    ("H2", "M6"): "left",
    ("H2", "M2"): "left",
    ("H4", "M6"): "left",
    ("H4", "M2"): "left",
    ("M6", "H4"): "right",
    ("M6", "H2"): "right",
    ("M6", "4"): "right",
    # ("H3", "M10"): [
    #     {"type": "segment", "id": ("H3", "M10")},
    #     {"type": "diag", "name": "ALB_Turn1"},
    #
    # ],
    ("H1", "M2"): "left",
    #
    # ("H3", "M1"): [
    #     {"type": "segment", "id": ("H3", "M10")},
    #     {"type": "diag", "name": "ALB_Turn1"},
    #     {"type": "segment", "id": ("M8", "M1")},
    #     {"type": "segment", "id": ("M8mid", "M1")},
    #     {"type": "segment", "id": ("M1", "pastM1")},
    # ],
    ("M10", "M1"): "right",
    ("M1", "M2"): "left",
    ("M1", "M8"): "left",
    ("M1", "H3"): "left",
    ("M8", "M1"): "right",
    ("M1", "H1"): "left",
    ("M1", "M10"): "left",
    ("H3", "M2"): "left",
}
routes = {
    # МАНЕВРОВЫЕ
    ("M2", "H3"): [
        {"type": "segment", "id": ("M2", "M2H1_mid")},
        {"type": "diag", "name": "ALB_Turn2"},
    ],
    ("M2", "H1"): [
        {"type": "segment", "id": ("M2", "M2H1_mid")},
        {"type": "segment", "id": ("M2H1_mid", "M2H1_third")},
        {"type": "segment", "id": ("M2H1_third", "H1")},
    ],
    ("M2", "M8"): [
        {"type": "segment", "id": ("M2", "M2H1_mid")},
        {"type": "segment", "id": ("M2H1_mid", "M2H1_third")},
        {"type": "segment", "id": ("M2H1_third", "H1")},
        {"type": "segment", "id": ("H1", "M8")},
    ],
    ("M2", "M1"): [
        {"type": "segment", "id": ("M2", "M2H1_mid")},
        {"type": "segment", "id": ("M2H1_mid", "M2H1_third")},
        {"type": "segment", "id": ("M2H1_third", "H1")},
        {"type": "segment", "id": ("H1", "M8")},
        {"type": "segment", "id": ("M8mid", "M8")},
        {"type": "segment", "id": ("M8mid", "M1")},
        {"type": "segment", "id": ("M1", "pastM1")},
    ],
    ("M2", "M10"): [
        {"type": "segment", "id": ("M2", "M2H1_mid")},
        {"type": "segment", "id": ("M2H1_mid", "M2H1_third")},
        {"type": "diag", "name": "ALB_Turn2"},
        {"type": "segment", "id": ("H3", "M10")},
    ],
    ("M2", "H2"): [
        {"type": "segment", "id": ("M2","M2H1_mid")},
        {"type": "segment", "id": ("M2H1_mid", "M2H1_third")},
        {"type": "diag", "name": "ALB_Turn4"},
        {"type": "diag", "name": "ALB_Turn6"},
        {"type": "segment", "id": ("H2", "M6H2")},
    ],
    ("M2", "H4"): [
        {"type": "segment", "id": ("M2","M2H1_mid")},
        {"type": "segment", "id": ("M2H1_mid", "M2H1_third")},
        {"type": "diag", "name": "ALB_Turn4"},
        {"type": "diag", "name": "ALB_Turn6"},
        {"type": "segment", "id": ("H2", "M6H2")},
        {"type": "diag", "name": "ALB_Turn8"},

    ],
    ("M2", "1"): [
        {"type": "segment", "id": ("M2", "M2H1_mid")},
        {"type": "segment", "id": ("M2H1_mid", "M2H1_third")},
        {"type": "segment", "id": ("H1", "M2H1_third")},
        {"type": "segment", "id": ("H1", "M8")},
    ],
    ("M2", "2"): [
        {"type": "segment", "id": ("M2", "M2H1_mid")},
        {"type": "segment", "id": ("M2H1_mid", "M2H1_third")},
        {"type": "diag", "name": "ALB_Turn4"},
        {"type": "diag", "name": "ALB_Turn6"},
        {"type": "segment", "id": ("H2", "M6H2")},
        {"type": "segment", "id": ("H2", "past2")},
    ],
    ("M2", "4"): [
        {"type": "segment", "id": ("M2H1_mid", "M2H1_third")},
        {"type": "segment", "id": ("M2", "M2H1_mid")},
        {"type": "diag", "name": "ALB_Turn4"},
        {"type": "diag", "name": "ALB_Turn6"},
        {"type": "diag", "name": "ALB_Turn8"},
        {"type": "segment", "id": ("M8", "M1")},
        {"type": "segment", "id": ("past4", "H4")},
    ],
    ("H2", "M6"): [
        {"type": "segment", "id": ("H2", "M6H2")},
        {"type": "segment", "id": ("M6H2", "M6")},
        {"type": "segment", "id": ("M6", "beforeM6")},
    ],
    ("H2", "M2"): [
        {"type": "segment", "id": ("H2", "M6H2")},
        {"type": "diag", "name": "ALB_Turn4"},
        {"type": "diag", "name": "ALB_Turn6"},
        {"type": "segment", "id": ("M2H1_mid", "M2H1_third")},
        {"type": "segment", "id": ("M2","M2H1_mid")}
    ],
    ("H4", "M6"): [
        {"type": "diag", "name": "ALB_Turn8"},
        {"type": "segment", "id": ("M6H2", "M6")},
        {"type": "segment", "id": ("M6", "beforeM6")},
    ],
    ("H4", "M2"): [
        {"type": "diag", "name": "ALB_Turn8"},
        {"type": "diag", "name": "ALB_Turn4"},
        {"type": "diag", "name": "ALB_Turn6"},
        {"type": "segment", "id": ("M2H1_mid", "M2H1_third")},
        {"type": "segment", "id": ("M2", "M2H1_mid")},
    ],
    ("M6", "H4"): [
        {"type": "segment", "id": ("M6", "Turn_14_J")},
        {"type": "diag", "name": "Turn_14"},
    ],
    ("M6", "H2"): [
        {"type": "segment", "id": ("M6", "Turn_14_J")},
        {"type": "segment", "id": ("Turn_14_J", "H2")},
    ],
    ("M6", "4"): [
        {"type": "segment", "id": ("M6H2", "M6")},
        {"type": "diag", "name": "ALB_Turn8"},
        {"type": "segment", "id": ("past4", "H4")},
    ],
    # ("H3", "M10"): [
    #     {"type": "segment", "id": ("H3", "M10")},
    #     {"type": "diag", "name": "ALB_Turn1"},
    #
    # ],
    ("H1", "M2"): [
        {"type": "segment", "id": ("M2H1_third", "H1")},
        {"type": "segment", "id": ("M2H1_mid", "M2H1_third")},
        {"type": "segment", "id": ("M2", "M2H1_mid")},
    ],
    #
    # ("H3", "M1"): [
    #     {"type": "segment", "id": ("H3", "M10")},
    #     {"type": "diag", "name": "ALB_Turn1"},
    #     {"type": "segment", "id": ("M8", "M1")},
    #     {"type": "segment", "id": ("M8mid", "M1")},
    #     {"type": "segment", "id": ("M1", "pastM1")},
    # ],
    ("M10", "M1"): [
        {"type": "diag", "name": "ALB_Turn1"},
        {"type": "segment", "id": ("M8mid", "M1")},
        {"type": "segment", "id": ("M1", "pastM1")},
    ],
    ("M1", "M2"): [
        {"type": "segment", "id": ("M8mid", "M1")},
        {"type": "segment", "id": ("M8mid", "M8")},
        {"type": "segment", "id": ("M8", "H1")},
        {"type": "segment", "id": ("M2H1_third", "H1")},
        {"type": "segment", "id": ("M2H1_mid", "M2H1_third")},
        {"type": "segment", "id": ("M2", "M2H1_mid")},
    ],
    ("M1", "M8"): [
        {"type": "segment", "id": ("M1", "pastM1")},
        {"type": "segment", "id": ("M8mid", "M1")},
        {"type": "segment", "id": ("M8mid", "M8")},
    ],
    ("M1", "H3"): [
        {"type": "segment", "id": ("M8mid", "M1")},
        {"type": "segment", "id": ("M8mid", "M8")},
        {"type": "diag", "name": "ALB_Turn1"},
        {"type": "segment", "id": ("H3", "M10")},
    ],
    ("M8", "M1"): [
        {"type": "segment", "id": ("M8mid", "M8")},
        {"type": "segment", "id": ("M8mid", "M1")},
        {"type": "segment", "id": ("M1", "pastM1")},
    ],
    ("M1", "H1"): [
        {"type": "segment", "id": ("M1", "pastM1")},
        {"type": "segment", "id": ("M8mid", "M1")},
        {"type": "segment", "id": ("M8mid", "M8")},
        {"type": "segment", "id": ("M8", "H1")},
    ],
    ("M1", "M10"): [
        {"type": "segment", "id": ("M8mid", "M1")},
        {"type": "segment", "id": ("M8mid", "M8")},
        {"type": "diag", "name": "ALB_Turn1"},
    ],
    ("H3", "M2"): [
        {"type": "diag", "name": "ALB_Turn2"},
        {"type": "segment", "id": ("M2", "M2H1_mid")},
    ]
}

train_routes = {
    ("Ч", "4"): [
        {"type": "segment", "id": ("Ч", "M2")},
        {"type": "segment", "id": ("M2H1_mid", "M2H1_third")},
        {"type": "segment", "id": ("M2", "M2H1_mid")},
        {"type": "diag", "name": "ALB_Turn4"},
        {"type": "diag", "name": "ALB_Turn6"},
        {"type": "diag", "name": "ALB_Turn8"},
        {"type": "segment", "id": ("past4", "H4")},
    ],
    ("Ч", "3"): [
        {"type": "segment", "id": ("Ч", "M2")},
        {"type": "segment", "id": ("M2", "M2H1_mid")},
        {"type": "segment", "id": ("M2H1_mid", "M2H1_third")},
        {"type": "diag", "name": "ALB_Turn2"},
        {"type": "segment", "id": ("H3", "M10")},
    ],
    ("Ч", "2"): [
        {"type": "segment", "id": ("Ч", "M2")},
        {"type": "segment", "id": ("M2", "M2H1_mid")},
        {"type": "segment", "id": ("M2H1_mid", "M2H1_third")},
        {"type": "diag", "name": "ALB_Turn4"},
        {"type": "diag", "name": "ALB_Turn6"},
        {"type": "segment", "id": ("H2", "M6H2")},
        {"type": "segment", "id": ("H2", "past2")},
    ],
    ("Ч", "1"): [
        {"type": "segment", "id": ("Ч", "M2")},
        {"type": "segment", "id": ("M2", "M2H1_mid")},
        {"type": "segment", "id": ("M2H1_mid", "M2H1_third")},
        {"type": "segment", "id": ("H1", "M2H1_third")},
        {"type": "segment", "id": ("H1", "M8")},
    ],
    ("Ч", "M1"): [
        {"type": "segment", "id": ("Ч", "M2")},
        {"type": "segment", "id": ("M2", "M2H1_mid")},
        {"type": "segment", "id": ("M2H1_mid", "M2H1_third")},
        {"type": "segment", "id": ("H1", "M2H1_third")},
        {"type": "segment", "id": ("H1", "M8")},
        {"type": "segment", "id": ("M8mid", "M8")},
        {"type": "segment", "id": ("M8mid", "M1")},
        {"type": "segment", "id": ("M1", "pastM1")},
    ],
    ("H3", "Ч"): [
        {"type": "diag", "name": "ALB_Turn2"},
        {"type": "segment", "id": ("M2", "M2H1_mid")},
        {"type": "segment", "id": ("Ч", "M2")},
    ],
    ("H1", "Ч"): [
        {"type": "segment", "id": ("H1", "M2H1_third")},
        {"type": "segment", "id": ("M2H1_mid", "M2H1_third")},
        {"type": "segment", "id": ("M2", "M2H1_mid")},
        {"type": "segment", "id": ("Ч", "M2")},
    ],
    ("H2", "Ч"): [
        {"type": "segment", "id": ("H2", "M6H2")},
        {"type": "segment", "id": ("M6H2", "M6")},
        {"type": "diag", "name": "ALB_Turn4"},
        {"type": "diag", "name": "ALB_Turn6"},
        {"type": "segment", "id": ("M2H1_mid", "M2H1_third")},
        {"type": "segment", "id": ("M2", "M2H1_mid")},
        {"type": "segment", "id": ("Ч", "M2")},
    ],
    ("H4", "Ч"): [
        {"type": "diag", "name": "ALB_Turn8"},
        {"type": "segment", "id": ("H2", "M6H2")},
        {"type": "segment", "id": ("M6H2", "M6")},
        {"type": "diag", "name": "ALB_Turn4"},
        {"type": "diag", "name": "ALB_Turn6"},
        {"type": "segment", "id": ("M2H1_mid", "M2H1_third")},
        {"type": "segment", "id": ("M2", "M2H1_mid")},
        {"type": "segment", "id": ("Ч", "M2")},
    ],



}
route_switch_modes = {
    ("M6", "H2"): {"Turn_14": "left"},   # «+»
    ("M6", "H4"): {"Turn_14": "right"},  # «-»
    ("M2", "H3"): {"ALB_Turn2": "right"},
    ("M2", "M10"): {"ALB_Turn2": "right"},
    ("H3", "M1"): {"ALB_Turn1": "right"},
    ("H3","M10"):{},
    ("M10", "M1"): {"ALB_Turn1": "right"},
    ("M2", "H1"): {"ALB_Turn2": "left","ALB_Turn4-6":  "left"},
    ("M2", "M8"): {"ALB_Turn2": "left", "ALB_Turn4-6":  "left"},
    ("M2", "M1"): {"ALB_Turn1": "left","ALB_Turn2": "left","ALB_Turn4-6":  "left"},
    ("M2", "1"):  {"ALB_Turn4-6": "left", "ALB_Turn2": "left"},
    ("M2", "2"): {"ALB_Turn2": "left", "ALB_Turn4-6": "right", "ALB_Turn8": "left"},
    ("M2", "4"): {"ALB_Turn2": "left","ALB_Turn4-6": "right", "ALB_Turn8": "right"},
    ("M1", "M2"): {"ALB_Turn1": "left", "ALB_Turn2": "left", "ALB_Turn4-6": "left"},
    ("M1", "M8"): {"ALB_Turn1": "left"},
    ("M1", "H1"): {"ALB_Turn1": "left"},
    ("M2", "H2"): {"ALB_Turn4-6": "right", "ALB_Turn8":  "left", "ALB_Turn2": "left"},
    ("H1", "M8"): {},
    ("Ч", "4"): {"ALB_Turn2": "left","ALB_Turn4-6": "right", "ALB_Turn8": "right"},
    ("Ч", "3"): {"ALB_Turn2": "right"},
    ("Ч", "2"): {"ALB_Turn2": "left", "ALB_Turn4-6": "right", "ALB_Turn8": "left"},
    ("Ч", "1"): {"ALB_Turn4-6": "left", "ALB_Turn2": "left"},
    ("Ч", "M1"): {"ALB_Turn4-6": "left", "ALB_Turn2": "left", "ALB_Turn1": "left"},
    ("M2", "H4"): {"ALB_Turn2": "left", "ALB_Turn4-6": "right", "ALB_Turn8": "right"},
    ("H2", "M2"): {"ALB_Turn8": "left", "ALB_Turn4-6": "right", "ALB_Turn2": "left"},
    ("M6", "4"): {"ALB_Turn4-6": "left", "ALB_Turn8": "right"},
    ("H3", "Ч"): {"ALB_Turn2": "right"},
    ("H1", "Ч"): {"ALB_Turn2": "left", "ALB_Turn4-6": "left"},
    ("H2", "Ч"): {"ALB_Turn4-6": "right", "ALB_Turn2": "left",},
    ("H4", "Ч"): {"ALB_Turn4-6": "right", "ALB_Turn2": "left", "ALB_Turn8": "right"},

}

#Arduino Configs
ROUTE_SIGNAL_ASPECTS = {
    None: {
        "Ч": "red",
        "H1": "red",
        "H2": "red",
        "H3": "red",
        "H4": "red",
    },
    "1": {   # Ч → 1 (главный путь)
        "Ч": "one_yellow",
        "H1": "red",
        "H2": "red",
        "H3": "red",
        "H4": "red",
    },
    "2": {   # Ч → 2 (боковой)
        "Ч": "two_yellow",
        "H1": "red",
        "H2": "red",
        "H3": "red",
        "H4": "red",
    },
    "3": {   # CH → 3
        "Ч": "two_yellow",
        "H1": "red",
        "H2": "red",
        "H3": "red",
        "H4": "red",
    },
    "4": {   # CH → 4
        "Ч": "two_yellow",
        "H1": "red",
        "H2": "red",
        "H3": "red",
        "H4": "red",
    },
}
# УЧАСТКИ, КОТОРЫЕ «ЗАЩИЩАЕТ» ВХОДНОЙ СВЕТОФОР CH
ROUTE_PROTECT_SEGMENTS_FOR_CH = {
    None: [],
    "1": [("M2", "Ч")],
    "2": [("M2", "Ч")],
    "3": [("M2", "Ч")],
    "4": [("M2", "Ч")],
}