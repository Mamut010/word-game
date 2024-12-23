import random
from itertools import product
from collections.abc import Iterable
from pathlib import Path

type Board = list[list[str | None]]
type FilledBoard = list[list[str]]
type Position = tuple[int, int]
type Direction = tuple[int, int]

def init_board(board_size: int) -> Board:
    return [[None for _ in range(board_size)] for _ in range(board_size)]

def get_vocabulary() -> Iterable[str]:
    vocabulary = [
        "SEA", "BASE", "LINE", "PLANE", "SUN", "TUNE", "PINE", "LENS", "NEARS", "SENSE",
        "ARRAY", "FOCUS", "HORIZON", "TRAVEL", "CLEAR", "WAVES", "STREAM", "BRIGHT", "SHADOW",
        "GLOW", "TRACE", "POINT", "VECTOR", "CIRCUIT", "LIGHT", "SHORE", "DEPTH", "CROSS",
        "SILENCE", "SOUND", "PATH", "TRACK", "MARK", "RANGE", "PEAK", "VALLEY", "SPACE",
        "TIME", "FIELD", "CLOUD", "STORM", "WIND", "TREE", "FIRE", "EARTH", "MOON", "STAR",
        "RIVER", "MOUNTAIN", "OCEAN", "DESERT", "CAVE", "ROCK", "FLOOD", "DREAM", "NIGHT",
        "DAY", "SKY", "BRIDGE", "FLOW", "SOURCE", "FALL", "RISE", "ARC", "SPHERE", "PLANE",
        "SHAPE", "FORM", "COLOR", "WALL", "GATE", "DOOR", "WINDOW", "TOWER", "ROAD", "SIGN",
        "PATHWAY", "PORT", "ANCHOR", "SAIL", "WHEEL", "CIRCLE", "FOCUS", "BEAM", "RAIL",
        "AXIS", "POINT", "LEVEL", "LINE", "ANGLE", "CURVE", "LOOP", "CHAIN", "BRANCH",
        "ROOT", "LEAF", "BARK", "STEM", "FRUIT", "SEED", "BLOOM", "PETAL", "CROWN",
        "STONE", "SHELL", "WAVE", "TIDE", "CURRENT", "SHORE", "BEACH", "CLIFF", "BAY",
        "HARBOR", "PORTAL", "CHANNEL", "PILLAR", "ARCH", "COLUMN", "LANTERN", "FIREPLACE",
        "CAMP", "OUTPOST", "FORT", "CASTLE", "CITADEL", "PALACE", "HALL", "ARENA", "DOME",
        "GALLERY", "VAULT", "LAB", "STATION", "BASE", "HUB", "CENTER", "GRID", "NETWORK",
        "FRAME", "MESH", "LATTICE", "SPINE", "CORE", "NODE", "BOND", "LINK", "WIRE", "CABLE",
        "ABILITY", "ABANDON", "ABDUCT", "ABHOR", "ABIDE", "ABNORMAL", "ABOLISH", "ABOUND", "ABRASIVE", "ABSENT",
        "ABSOLUTE", "ABSORB", "ABSTRACT", "ABUNDANT", "ACADEMY", "ACCELERATE", "ACCENT", "ACCEPT", "ACCESS", "ACCIDENT",
        "ACCOMMODATE", "ACCOMPANY", "ACCOMPLISH", "ACCORD", "ACCOUNT", "ACCUSE", "ACQUIRE", "ADDRESS", "ADVANCE", "ADVERSE",
        "ADVICE", "AESTHETIC", "AFFECTION", "AFFIRM", "AFFORD", "AGGRESSIVE", "ALLEGRO", "ALREADY", "AMAZING", "ANCIENT",
        "ANGRY", "ANIMAL", "ANALYZE", "ANCIENT", "ANXIETY", "APPEAL", "APPOINT", "APPROVE", "ARCADE", "ARRANGE",
        "ARRIVE", "ARTISTIC", "ASSEMBLE", "ASSAULT", "ASSERT", "ASSESS", "ASSIGN", "ASSIST", "ASSUME", "ASTRONOMY",
        "ATHLETE", "ATROCITY", "BALANCE", "BARRIER", "BEACON", "BENEFIT", "BICYCLE", "BLESSING", "BORROW", "BRAVERY",
        "BREATHE", "BROTHER", "CAUTION", "CENTER", "CHAMBER", "CLIMATE", "COGNITIVE", "COMBINE", "COMPASS", "CREATE",
        "CRYSTAL", "CURIOUS", "CYLINDER", "DARING", "DEFEND", "DECENT", "DELICATE", "DILIGENT", "DISEASE", "DISCARD",
        "DOMINATE", "DOUBT", "DYNAMIC", "EDUCATION", "ENDURE", "ELASTIC", "ELEVATE", "ENLIGHTEN", "ESSENCE", "EXCITED",
        "FAMOUS", "FASHION", "FREEDOM", "FRAGILE", "FROSTED", "GATHER", "GENUINE", "GRATEFUL", "GROUND", "GROWTH",
        "HARMONY", "HEAVEN", "HERITAGE", "IMAGINE", "IMPROVE", "INSPIRE", "INVADE", "JOURNEY", "JUSTICE", "JUNGLE",
        "KITCHEN", "KINGDOM", "LABORATORY", "LEGACY", "Lighthouse", "LIBERTY", "LIVELY", "MODERN", "MOTIVE", "MYSTIC",
        "NATURAL", "NOBLE", "NUCLEUS", "OPPOSITE", "ORGANIC", "ORIGIN", "PEACEFUL", "PLANET", "PLENTY", "PROGRESS",
        "QUALITY", "QUAINT", "REFORM", "REFLECT", "REPOSE", "REVEAL", "RESTORE", "RESCUE", "RICH", "SECURE", 
        "SENTENCE", "SIMPLE", "SOLUTION", "SPIRITUAL", "STORMY", "STRIVE", "SUCCESS", "SYNERGY", "THEORY", "THRIVING",
        "TIGER", "TOPICAL", "TRIUMPH", "TURBINE", "UNFOLD", "UNITE", "UNIQUE", "VACANT", "VIBRANT", "VISION",
        "WHOLESOME", "WONDER", "WORTH", "YEARNING", "ZEALOUS", "ZENITH", "ZEPHYR", "ABACUS", "ABDUCTED", "ABDUCTS", 
        "ABIDING", "ABSENT", "ABSENTS", "ABSORB", "ABSORBED", "ABSORBS", "ACCIDENT", "ACCIDENTALLY", "ACCIDENTS", 
        "ACCLAIM", "ACCLAIMED", "ACCLAIMS", "ACCOMMODATE", "ACCOMMODATED", "ACCOMMODATES", "ACCOMPANY", "ACCOMPANIED", 
        "ACCOMPANIES", "ACCOMPANYING", "ACCOUNTABLE", "ACCOUNTABLY", "ACCOUNTED", "ACCOUNTING", "ACCRETION", 
        "ACCREDITED", "ACCREDITS", "ACCUMULATE", "ACCUMULATED", "ACCUMULATES", "ACCUMULATING", "ACCURACY", "ACCURATELY",
        "ACCUSE", "ACCUSED", "ACCUSES", "ACCUSE", "ACCUSES", "ACQUIRER", "AFFAIR", "AFFAIRS", "AFFECTION", "AFFILIATED",
        "AFFILIATE", "AFFIRM", "AFFORDABLE", "AFFORDING", "AFFORDS", "AFFIX", "AFFIRMATION", "AFFIRMATIVE", 
        "AFRAID", "AGENT", "AGENT", "AGENTS", "AGGRESSIVE", "AGITATE", "AGILITY", "AGREE", "AGREEING", "AGREEMENT",
        "AGREEMENTS", "AGREEABLE", "AGREEABLES", "ALLEGRO", "ANALYSIS", "ANALYZE", "AFFECT", "AFFECTED", "AFFECTS",
        "AFFECTIONATE", "AGGRESSIVE", "AGAINST", "AGITATED", "ASSAULTED", "ATHLETE", "ATHLETES", "AGITATING", 
        "ABOMINABLE", "ABHORRENT", "AFRICAN", "AGGRAVATE", "ABRUPT", "ANALOGY", "ANALYSIS", "GROWTH", "GROWING", 
        "GUSHING", "GUSH", "GRADUAL", "GENIUS", "GENERATE", "GENUINE", "GENERATION", "GENERATIONAL", "GAINFUL",
        "GALVANIZE", "GAMBLE", "GATHERING", "GENUINELY", "GREAT", "GRIT", "GRIND", "GRACEFUL", "GLASS", "GENOME", 
        "GROUND", "GALLANT", "GENERATOR", "GRATEFUL", "GAS", "GAME", "GUSH", "GIGANTIC", "GLOW", "GUTS", 
        "GENUINE", "GRANITE", "GROWL", "GOAL", "GARMENT", "GLASS", "GLIMMER", "GUILD", "GARISH", "GARNISH",
        "GATE", "GRAND", "GILD", "GLOWING", "GIVE", "GASOLINE", "GADGET", "GAMING", "GAMES", "GOODS", 
        "GOLD", "GABBLE", "GIBBERISH", "GAZE", "GRACE", "GIVEAWAY", "GREATNESS", "GRAND", "GLOOMY", "GOOD",
        "GUARANTEE", "GIFT", "GRAND", "GENETIC", "GLOSS", "GLOW", "GRIMM", "GAY",
        "Thane", "Alms", "Bane", "Grim", "Fate", "Wyrm", "Laird", "Sire", "Knight", "Sword",
        "Fealty", "Crest", "Vale", "Loom", "Fief", "Wit", "Hearth", "Rune", "Pagan", "Moot",
        "Wit", "Froth", "Glen", "Harold", "Lance", "Bane", "Vane", "Wold", "Lamb", "Hallow",
        "Gale", "Valkyrie", "Foe", "Doom", "Myth", "Rook", "Briar", "Trove", "Grave", "Lore",
        "Vow", "Oath", "Fleet", "Mire", "Spire", "Gloom", "Thane", "Cleave", "Sear", "Wane",
        "Vast", "Elder", "Stone", "Mead", "Forge", "Rage", "Valkyr", "Mist", "Wraith", "Henge",
        "Fate", "Thrift", "Cairn", "Fled", "Cleave", "Raven", "Rogue", "Warden", "Vile", "Ash",
        "Weald", "Gore", "Grim", "Keen", "Wrath", "Blight", "Crown", "Vail", "Thorn", "Flesh",
        "Troll", "Scorn", "Blade", "Ghoul", "Fell", "Jarl", "Fey", "Dread", "Reeve", "Purge",
        "Frost", "Vile", "Seer", "Vane", "Fodder", "Prowl", "Mire", "Stray", "Doom", "Rook",
        "Pale", "Reck", "Thorn", "Moth", "Hag", "Ravine", "Ruin", "Gale", "Rook", "Plague",
        "Rime", "Haunt", "Hound", "Purge", "Cairn", "Altar", "Ashen", "Rage", "Flare", "Pest",
        "Shade", "Thrift", "Ravage", "Loom", "Mark", "Grit", "Sever", "Tale", "Witch", "Worm",
        "Glade", "Skull", "Crux", "Veld", "Gloom", "Crypt", "Blaze", "Grave", "Forge", "Vanquish",
        "ABILITY", "ACCESS", "ACCOUNT", "ACHIEVE", "ACQUIRE", "ACTION", "ACTIVITY", "ADDITION", "ADDRESS",
        "ADVANCE", "ADVENTURE", "ADVICE", "AFFECT", "AGENCY", "AGREE", "AIRPORT", "ALERT", "ALIGN", "ALIVE",
        "AMAZING", "ANALYZE", "ANCIENT", "ANGER", "ANIMAL", "ANSWER", "APPEAL", "APPLY", "APPROACH", "ARCHIVE",
        "AREA", "ARGUMENT", "ARRANGE", "ARREST", "ARRIVAL", "ARTICLE", "ARTIST", "ASPECT", "ASSIGN", "ASSIST",
        "ASSUME", "ASSURE", "ATTACH", "ATTACK", "ATTEMPT", "ATTEND", "ATTRACT", "AUTHENTIC", "AUTHORITY",
        "AWESOME", "BALANCE", "BANDAGE", "BARRIER", "BATTLE", "BEAUTY", "BECOME", "BELIEVE", "BENEFIT",
        "BETRAY", "BIRTHDAY", "BLADE", "BLANKET", "BLESS", "BLOCK", "BOARD", "BOMBARD", "BONUS", "BORDER",
        "BOTTLE", "BRAIN", "BRANCH", "BREATH", "BRIDGE", "BRIGHT", "BROKEN", "BUDGET", "BULLET", "BUNDLE",
        "BURDEN", "BUTTON", "CABINET", "CAMERA", "CAMPAIGN", "CANDIDATE", "CAPACITY", "CAPTURE", "CAREER",
        "CARRIAGE", "CARRIER", "CAUTION", "CELEBRATE", "CENTER", "CENTRAL", "CEREMONY", "CHAIR", "CHALLENGE",
        "CHAMBER", "CHANGE", "CHANNEL", "CHARGE", "CHARITY", "CHARTER", "CHASE", "CHECK", "CHIEF", "CHOICE",
        "CIRCLE", "CITIZEN", "CLARIFY", "CLASSIC", "CLEANSE", "CLIENT", "CLIMATE", "CLOSURE", "CLUSTER",
        "COLLECT", "COLLEGE", "COLONY", "COLOR", "COMBAT", "COMEDY", "COMMAND", "COMMENT", "COMMIT",
        "COMMON", "COMMUNICATE", "COMPARE", "COMPANY", "COMPETE", "COMPILE", "COMPLEX", "COMPLY", "CONCEPT",
        "CONCERN", "CONCLUDE", "CONDUCT", "CONFERENCE", "CONFIRM", "CONFLICT", "CONFRONT", "CONGRESS",
        "CONNECT", "CONQUER", "CONSENT", "CONSIDER", "CONSIST", "CONSTANT", "CONSTRUCT", "CONSULT", "CONTACT",
        "CONTAIN", "CONTENT", "CONTEST", "CONTEXT", "CONTINUE", "CONTRACT", "CONTROL", "CONVERT", "CONVINCE",
        "COOPERATE", "COPYRIGHT", "CORNER", "CORRECT", "CORRIDOR", "COUNTRY", "COURAGE", "COURSE", "CREATE",
        "CREATOR", "CREDIT", "CRISIS", "CRITICAL", "CROWD", "CULTURE", "CUSTOM", "CYCLE", "DAMAGE", "DANGER",
        "DATABASE", "DEADLINE", "DEBATE", "DECIDE", "DECLARE", "DECLINE", "DEDICATE", "DEFEAT", "DEFEND",
        "DEFENSE", "DEFINE", "DEGREE", "DELAY", "DELETE", "DELIVER", "DEMAND", "DEMONSTRATE", "DENY",
        "DEPART", "DEPEND", "DEPOSIT", "DEPRESS", "DERIVE", "DESCRIBE", "DESERT", "DESIGN", "DESIRE",
        "DETECT", "DETERMINE", "DEVELOP", "DEVICE", "DIAGNOSE", "DIFFER", "DIGITAL", "DIGNITY", "DIRECT",
        "DISABLE", "DISAGREE", "DISAPPEAR", "DISARM", "DISCOUNT", "DISCOVER", "DISCUSS", "DISMISS", "DISPLAY",
        "DISPOSE", "DISTANCE", "DISTURB", "DIVIDE", "DIVORCE", "DOCTOR", "DOCUMENT", "DOMAIN", "DOMINATE",
        "DONATE", "DOUBLE", "DOUBT", "DOWNLOAD", "DRAMA", "DREAM", "DRESS", "DRIVE", "DROUGHT", "DURABLE",
        "DYNAMIC", "EAGER", "EARLY", "EARNEST", "EARTH", "EASE", "EAST", "EASY", "ECONOMIC", "EDITION",
        "EDITOR", "EDUCATE", "EFFECT", "EFFORT", "ELABORATE", "ELECTION", "ELECTRIC", "ELEVATE", "ELIMINATE",
        "EMERGENCY", "EMOTION", "EMPHASIS", "EMPOWER", "ENABLE", "ENACT", "ENCOUNTER", "ENDANGER", "ENDLESS",
        "ENDORSE", "ENDURE", "ENERGY", "ENGAGE", "ENGINE", "ENHANCE", "ENJOY", "ENLARGE", "ENLIST", "ENRICH",
        "ENSURE", "ENTERPRISE", "ENTIRE", "ENTITLE", "ENTRY", "ENVIRONMENT", "EPISODE", "EQUALITY", "EQUATION",
        "EQUIP", "ESSENCE", "ESTABLISH", "ESTIMATE", "ETHICS", "EVACUATE", "EVALUATE", "EVENT", "EVIDENCE",
        "EVOLVE", "EXACT", "EXAMPLE", "EXCEED", "EXCEL", "EXCEPT", "EXCHANGE", "EXCITE", "EXECUTE", "EXEMPT",
        "EXERCISE", "EXHAUST", "EXHIBIT", "EXIST", "EXPAND", "EXPECT", "EXPENSE", "EXPERIENCE", "EXPLAIN",
        "EXPLORE", "EXPORT", "EXPOSE", "EXPRESS", "EXTEND", "EXTREME", "EYEWITNESS", "FABRIC", "FACTORY",
        "FAILURE", "FAITH", "FAMILY", "FAMOUS", "FANTASY", "FARMLAND", "FASHION", "FEATURE", "FEDERAL",
        "FEELING", "FESTIVAL", "FIBER", "FICTION", "FIELD", "FIERCE", "FIGHTER", "FIGURE", "FILM", "FILTER",
        "FINALIZE", "FINANCE", "FINDING", "FIREWORK", "FIRST", "FIXTURE", "FLAVOR", "FLEXIBLE", "FLIGHT",
        "FLORA", "FLOURISH", "FOCUS", "FOLLOW", "FOOTBALL", "FOREIGN", "FORGE", "FORMAL", "FORMULA", "FORTUNE",
        "ABLE", "ABUSE", "ACE", "ACID", "ACT", "ADD", "AIR", "AIM", "ALONE", "AND",
        "ANGER", "ANIMAL", "APPLE", "AREA", "ARM", "ART", "ASLEEP", "AWAKE", "BACK", "BALL",
        "BAND", "BANK", "BAR", "BASE", "BEAM", "BEAR", "BELL", "BILL", "BIRD", "BRAIN",
        "BROOK", "BUS", "CAGE", "CAP", "CAR", "CAST", "CAT", "COLD", "COLOR", "CROWN",
        "DART", "DAY", "DOG", "DOOR", "DOWN", "DREAM", "EAR", "EDGE", "EGG", "ELBOW",
        "EYE", "FALL", "FARM", "FAST", "FEAR", "FIRE", "FIGHT", "FOOT", "GAME", "GLOW",
        "GOLD", "GRASS", "GROUND", "HAND", "HILL", "HOME", "HOPE", "HURT", "JUMP", "JUDGE",
        "KING", "KISS", "KNIFE", "LACE", "LAND", "LION", "LAMP", "LINE", "LIST", "LOST",
        "MAP", "MATCH", "MOUSE", "NOISE", "NIGHT", "OPEN", "OPINION", "PARK", "PEN", "PINE",
        "PLACE", "PLANT", "PLUG", "RACE", "RAIN", "ROAD", "RISE", "RING", "SAND", "SING",
        "SEA", "BASE", "LINE", "PLANE", "SUN",
        "TUNE", "PINE", "LENS", "NEARS", "SENSE",
    ]
    vocabulary = [word.upper() for word in list(set(vocabulary))]
    random.shuffle(vocabulary)
    return vocabulary

def create_all_directions() -> list[Direction]:
    '''Create a list of horizontal, vertical and diagonal directions'''
    return [direction for direction in product([-1, 0, 1], [-1, 0, 1]) if direction[0] != 0 and direction[1] != 0]

def populate_board(board: Board, board_size: int, vocabulary: Iterable[str], directions: list[Direction]):
    """Populate the board with words randomly"""
    positions = list[Position](product(range(0, board_size - 1), range(0, board_size - 1)))
    pop_positions = list[Position]()
    words = list[str]()
    max_length = 0
    for word in vocabulary:
        positions += pop_positions
        pop_positions.clear()
        random.shuffle(positions)
        placed = False
        while not placed and len(positions) != 0:
            position = positions.pop()
            pop_positions.append(position)
            direction = random.choice(directions)
            if can_place_word(board, board_size, word, position, direction):
                place_word(board, word, position, direction)
                words.append(word)
                max_length = max(len(word), max_length)
                placed = True
    return (words, max_length)

def can_place_word(board: Board, board_size: int, word: str, position: Position, direction: Direction):
    """Check if a word can be placed starting at pos=(row, col) in the given direction."""
    row, col = position
    d_row, d_col = direction
    for i, char in enumerate(word):
        r, c = row + i * d_row, col + i * d_col
        if r < 0 or r >= board_size or c < 0 or c >= board_size:
            return False
        if board[r][c] not in (None, char):  # Conflict check
            return False
    return True

def place_word(board: Board, word: str, position: Position, direction: Direction):
    """Place a word on the board."""
    row, col = position
    d_row, d_col = direction
    for i, char in enumerate(word):
        r, c = row + i * d_row, col + i * d_col
        board[r][c] = char

def fill_empty_cells(board: Board, board_size: int) -> FilledBoard:
    '''Fill empty cells with random letters'''
    start_codepoint = ord('A')
    end_codepoint = ord('Z')
    for row in range(board_size):
        for col in range(board_size):
            if board[row][col] is None:
                board[row][col] = chr(random.randint(start_codepoint, end_codepoint))
    return board

def board_to_heredoc(board: FilledBoard):
    '''Convert board to heredoc format'''
    return "\n".join(" ".join(row) for row in board)

def words_to_formatted_2d(words: list[str], n_words_per_row: int,\
                                  word_justified_length: int, display: bool|None = None):
    '''Convert words list to a formatted string of 2d array'''
    word_rows = list[list[str]]()
    displayed_word_rows = list[list[str]]()
    n_words = len(words)
    n_inserted_words = 0
    while n_inserted_words < n_words:
        n_row_words = min(n_words - n_inserted_words, n_words_per_row)
        inserted_words = words[n_inserted_words : n_inserted_words+n_row_words]
        row = [f"'{word}'".ljust(word_justified_length + 2) for word in inserted_words]
        word_rows.append(row)
        if display:
            displayed_row = [word.ljust(word_justified_length) for word in inserted_words]
            displayed_word_rows.append(displayed_row)
        n_inserted_words += n_row_words
    formatted_words = ",\n".join(", ".join(row) for row in word_rows) + ","
    displayed_words = "\n".join("      ".join(row) for row in displayed_word_rows) if display else ''
    return (formatted_words, displayed_words)

def save_text_file(filepath: str, text: str):
    file = Path(filepath)
    file.parent.mkdir(exist_ok=True, parents=True)
    file.write_text(text)

def main():
    BOARD_DISPLAY_THRESHOLD = 20
    WORDS_DISPLAY_THRESHOLD = 300
    n_words_per_row = 7
    board_size = 20

    board = init_board(board_size)
    vocabulary = get_vocabulary()
    directions = create_all_directions()
    words, max_length = populate_board(board, board_size, vocabulary, directions)
    board = fill_empty_cells(board, board_size)

    words.sort()
    n_words = len(words)
    should_display_words = n_words <= WORDS_DISPLAY_THRESHOLD

    heredoc_board = board_to_heredoc(board)
    formatted_words, displayed_words = words_to_formatted_2d(words, n_words_per_row, max_length, should_display_words)

    board_path = "./out/word-search-board.txt"
    words_path = "./out/word-search-words.txt"
    save_text_file(board_path, heredoc_board)
    save_text_file(words_path, formatted_words)

    print(f"Board {board_size}x{board_size}:")
    if board_size <= BOARD_DISPLAY_THRESHOLD:
        print(heredoc_board)
        print()
    print(f"Words (count = {n_words}):")
    if should_display_words:
        print(displayed_words)

if __name__ == '__main__':
    main()