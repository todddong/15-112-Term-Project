from cmu_graphics import *
import random
import copy
import time

def onAppStart(app):
    app.width = 1000
    app.height = 1000
    app.rows = 1000
    app.screenRows = 6
    app.cols = 5
    app.shift = 0
    # PLAYER BOARD
    app.playerBoardLeft = 150
    app.playerBoardTop = 75
    app.playerBoardWidth = 250
    app.playerBoardHeight = 300
    app.playerBorderWidth = 1

    #COMPUTER BOARD
    app.computerBoardLeft = 600
    app.computerBoardTop = 75
    app.computerBoardWidth = 250
    app.computerBoardHeight = 300
    app.computerBorderWidth = 1

    #KEYBOARD
    app.keyBoardLeft = 200
    app.keyBoardTop = 500
    app.keyWidth = 60
    app.keyHeight = 80
    app.keyBorderWidth = 3

    app.over = False
    app.words =[]
    app.level = None
    app.keyboard = [
        ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
        ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L','enter'],
        ['','Z', 'X', 'C', 'V', 'B', 'N', 'M', 'back', '']
    ]
    app.keys = [['' for i in range(app.cols)] for j in range(app.rows)]
    app.currentRow = 0
    app.currentCol = 0
    app.words = [
    # list copied from online wordle word list https://www.wordunscrambler.net/word-list/wordle-word-list 
    'ABACK', 'ABASE', 'ABATE', 'ABBEY', 'ABBOT', 'ABHOR', 'ABIDE', 'ABLED', 'ABODE', 'ABORT',
    'ABOUT', 'ADIEU', 'ABOVE', 'ABUSE', 'ABYSS', 'ACORN', 'ACRID', 'ACTOR', 'ACUTE', 'ADAGE', 
    'ADAPT',
    'ADEPT', 'ADMIN', 'ADMIT', 'ADOBE', 'ADOPT', 'ADORE', 'ADORN', 'ADULT', 'AFFIX', 'AFIRE',
    'AFOOT', 'AFOUL', 'AFTER', 'AGAIN', 'AGAPE', 'AGATE', 'AGENT', 'AGILE', 'AGING', 'AGLOW',
    'AGONY', 'AGREE', 'AHEAD', 'AIDER', 'AISLE', 'ALARM', 'ALBUM', 'ALERT', 'ALGAE', 'ALIBI',
    'ALIEN', 'ALIGN', 'ALIKE', 'ALIVE', 'ALLAY', 'ALLEY', 'ALLOT', 'ALLOW', 'ALLOY', 'ALOFT',
    'ALONE', 'ALONG', 'ALOOF', 'ALOUD', 'ALPHA', 'ALTAR', 'ALTER', 'AMASS', 'AMAZE', 'AMBER',
    'AMBLE', 'AMEND', 'AMISS', 'AMITY', 'AMONG', 'AMPLE', 'AMPLY', 'AMUSE', 'ANGEL', 'ANGER',
    'ANGLE', 'ANGRY', 'ANGST', 'ANIME', 'ANKLE', 'ANNEX', 'ANNOY', 'ANNUL', 'ANODE', 'ANTIC',
    'ANVIL', 'AORTA', 'APART', 'APHID', 'APING', 'APNEA', 'APPLE', 'APPLY', 'APRON', 'APTLY',
    'ARBOR', 'ARDOR', 'ARENA', 'ARGUE', 'ARISE', 'ARMOR', 'AROMA', 'AROSE', 'ARRAY', 'ARROW',
    'ARSON', 'ARTSY', 'ASCOT', 'ASHEN', 'ASIDE', 'ASKEW', 'ASSAY', 'ASSET', 'ATOLL', 'ATONE',
    'ATTIC', 'AUDIO', 'AUDIT', 'AUGUR', 'AUNTY', 'AVAIL', 'AVERT', 'AVIAN', 'AVOID', 'AWAIT',
    'AWAKE', 'AWARD', 'AWARE', 'AWASH', 'AWFUL', 'AWOKE', 'AXIAL', 'AXIOM', 'AXION', 'AZURE',
    'BACON', 'BADGE', 'BADLY', 'BAGEL', 'BAGGY', 'BAKER', 'BALER', 'BALMY', 'BANAL', 'BANJO',
    'BARGE', 'BARON', 'BASAL', 'BASIC', 'BASIL', 'BASIN', 'BASIS', 'BASTE', 'BATCH', 'BATHE',
    'BATON', 'BATTY', 'BAWDY', 'BAYOU', 'BEACH', 'BEADY', 'BEARD', 'BEAST', 'BEECH', 'BEEFY',
    'BEFIT', 'BEGAN', 'BEGAT', 'BEGET', 'BEGIN', 'BEGUN', 'BEING', 'BELCH', 'BELIE', 'BELLE',
    'BELLY', 'BELOW', 'BENCH', 'BERET', 'BERRY', 'BERTH', 'BESET', 'BETEL', 'BEVEL', 'BEZEL',
    'BIBLE', 'BICEP', 'BIDDY', 'BIGOT', 'BILGE', 'BILLY', 'BINGE', 'BINGO', 'BIOME', 'BIRCH',
    'BIRTH', 'BISON', 'BITTY', 'BLACK', 'BLADE', 'BLAME', 'BLAND', 'BLANK', 'BLARE', 'BLAST',
    'BLAZE', 'BLEAK', 'BLEAT', 'BLEED', 'BLEEP', 'BLEND', 'BLESS', 'BLIMP', 'BLIND', 'BLINK',
    'BLISS', 'BLITZ', 'BLOAT', 'BLOCK', 'BLOKE', 'BLOND', 'BLOOD', 'BLOOM', 'BLOWN', 'BLUER',
    'BLUFF', 'BLUNT', 'BLURB', 'BLURT', 'BLUSH', 'BOARD', 'BOAST', 'BOBBY', 'BONEY', 'BONGO',
    'BONUS', 'BOOBY', 'BOOST', 'BOOTH', 'BOOTY', 'BOOZE', 'BOOZY', 'BORAX', 'BORNE', 'BOSOM',
    'BOSSY', 'BOTCH', 'BOUGH', 'BOULE', 'BOUND', 'BOWEL', 'BOXER', 'BRACE', 'BRAID', 'BRAIN',
    'BRAKE', 'BRAND', 'BRASH', 'BRASS', 'BRAVE', 'BRAVO', 'BRAWL', 'BRAWN', 'BREAD', 'BREAK',
    'BREED', 'BRIAR', 'BRIBE', 'BRICK', 'BRIDE', 'BRIEF', 'BRINE', 'BRING', 'BRINK', 'BRINY',
    'BRISK', 'BROAD', 'BROIL', 'BROKE', 'BROOD', 'BROOK', 'BROOM', 'BROTH', 'BROWN', 'BRUNT',
    'BRUSH', 'BRUTE', 'BUDDY', 'BUDGE', 'BUGGY', 'BUGLE', 'BUILD', 'BUILT', 'BULGE', 'BULKY',
    'BULLY', 'BUNCH', 'BUNNY', 'BURLY', 'BURNT', 'BURST', 'BUSED', 'BUSHY', 'BUTCH', 'BUTTE',
    'BUXOM', 'BUYER', 'BYLAW',
    'CABAL', 'CABBY', 'CABIN', 'CABLE', 'CACAO', 'CACHE', 'CACTI', 'CADDY', 'CADET', 'CAGEY',
    'CAIRN', 'CAMEL', 'CAMEO', 'CANAL', 'CANDY', 'CANNY', 'CANOE', 'CANON', 'CAPER', 'CAPUT',
    'CARAT', 'CARGO', 'CAROL', 'CARRY', 'CARVE', 'CASTE', 'CATCH', 'CATER', 'CATTY', 'CAULK',
    'CAUSE', 'CAVIL', 'CEASE', 'CEDAR', 'CELLO', 'CHAFE', 'CHAFF', 'CHAIN', 'CHAIR', 'CHALK',
    'CHAMP', 'CHANT', 'CHAOS', 'CHARD', 'CHARM', 'CHART', 'CHASE', 'CHASM', 'CHEAP', 'CHEAT',
    'CHECK', 'CHEEK', 'CHEER', 'CHESS', 'CHEST', 'CHICK', 'CHIDE', 'CHIEF', 'CHILD', 'CHILI',
    'CHILL', 'CHIME', 'CHINA', 'CHIRP', 'CHOCK', 'CHOIR', 'CHOKE', 'CHORD', 'CHORE', 'CHOSE',
    'CHUCK', 'CHUMP', 'CHUNK', 'CHURN', 'CHUTE', 'CIDER', 'CIGAR', 'CINCH', 'CIRCA', 'CIVIC',
    'CIVIL', 'CLACK', 'CLAIM', 'CLAMP', 'CLANG', 'CLANK', 'CLASH', 'CLASP', 'CLASS', 'CLEAN',
    'CLEAR', 'CLEAT', 'CLEFT', 'CLERK', 'CLICK', 'CLIFF', 'CLIMB', 'CLING', 'CLINK', 'CLOAK',
    'CLOCK', 'CLONE', 'CLOSE', 'CLOTH', 'CLOUD', 'CLOUT', 'CLOVE', 'CLOWN', 'CLUCK', 'CLUED',
    'CLUMP', 'CLUNG', 'COACH', 'COAST', 'COBRA', 'COCOA', 'COLON', 'COLOR', 'COMET', 'COMFY',
    'COMIC', 'COMMA', 'CONCH', 'CONDO', 'CONIC', 'COPSE', 'CORAL', 'CORER', 'CORNY', 'COUCH',
    'COUGH', 'COULD', 'COUNT', 'COUPE', 'COURT', 'COVEN', 'COVER', 'COVET', 'COVEY', 'COWER',
    'COYLY', 'CRACK', 'CRAFT', 'CRAMP', 'CRANE', 'CRANK', 'CRASH', 'CRASS', 'CRATE', 'CRAVE',
    'CRAWL', 'CRAZE', 'CRAZY', 'CREAK', 'CREAM', 'CREDO', 'CREED', 'CREEK', 'CREEP', 'CREME',
    'CREPE', 'CREPT', 'CRESS', 'CREST', 'CRICK', 'CRIED', 'CRIER', 'CRIME', 'CRIMP', 'CRISP',
    'CROAK', 'CROCK', 'CRONE', 'CRONY', 'CROOK', 'CROSS', 'CROUP', 'CROWD', 'CROWN', 'CRUDE',
    'CRUEL', 'CRUMB', 'CRUMP', 'CRUSH', 'CRUST', 'CRYPT', 'CUBIC', 'CUMIN', 'CURIO', 'CURLY',
    'CURRY', 'CURSE', 'CURVE', 'CURVY', 'CUTIE', 'CYBER', 'CYCLE', 'CYNIC',
    'DADDY', 'DAILY', 'DAIRY', 'DAISY', 'DALLY', 'DANCE', 'DANDY', 'DATUM', 'DAUNT', 'DEALT',
    'DEATH', 'DEBAR', 'DEBIT', 'DEBUG', 'DEBUT', 'DECAL', 'DECAY', 'DECOR', 'DECOY', 'DECRY',
    'DEFER', 'DEIGN', 'DEITY', 'DELAY', 'DELTA', 'DELVE', 'DEMON', 'DEMUR', 'DENIM', 'DENSE',
    'DEPOT', 'DEPTH', 'DERBY', 'DETER', 'DETOX', 'DEUCE', 'DEVIL', 'DIARY', 'DICEY', 'DIGIT',
    'DILLY', 'DIMLY', 'DINER', 'DINGO', 'DINGY', 'DIODE', 'DIRGE', 'DIRTY', 'DISCO', 'DITCH',
    'DITTO', 'DITTY', 'DIVER', 'DIZZY', 'DODGE', 'DODGY', 'DOGMA', 'DOING', 'DOLLY', 'DONOR',
    'DONUT', 'DOPEY', 'DOUBT', 'DOUGH', 'DOWDY', 'DOWEL', 'DOWNY', 'DOWRY', 'DOZEN', 'DRAFT',
    'DRAIN', 'DRAKE', 'DRAMA', 'DRANK', 'DRAPE', 'DRAWL', 'DRAWN', 'DREAD', 'DREAM', 'DRESS',
    'DRIED', 'DRIER', 'DRIFT', 'DRILL', 'DRINK', 'DRIVE', 'DROIT', 'DROLL', 'DRONE', 'DROOL',
    'DROOP', 'DROSS', 'DROVE', 'DROWN', 'DRUID', 'DRUNK', 'DRYER', 'DRYLY', 'DUCHY', 'DULLY',
    'DUMMY', 'DUMPY', 'DUNCE', 'DUSKY', 'DUSTY', 'DUTCH', 'DUVET', 'DWARF', 'DWELL', 'DWELT',
    'DYING',
    'EAGER', 'EAGLE', 'EARLY', 'EARTH', 'EASEL', 'EATEN', 'EATER', 'EBONY', 'ECLAT', 'EDICT',
    'EDIFY', 'EERIE', 'EGRET', 'EIGHT', 'EJECT', 'EKING', 'ELATE', 'ELBOW', 'ELDER', 'ELECT',
    'ELEGY', 'ELFIN', 'ELIDE', 'ELITE', 'ELOPE', 'ELUDE', 'EMAIL', 'EMBED', 'EMBER', 'EMCEE',
    'EMPTY', 'ENACT', 'ENDOW', 'ENEMA', 'ENEMY', 'ENJOY', 'ENNUI', 'ENSUE', 'ENTER', 'ENTRY',
    'ENVOY', 'EPOCH', 'EPOXY', 'EQUAL', 'EQUIP', 'ERASE', 'ERECT', 'ERODE', 'ERROR', 'ERUPT',
    'ESSAY', 'ESTER', 'ETHER', 'ETHIC', 'ETHOS', 'ETUDE', 'EVADE', 'EVENT', 'EVERY', 'EVICT',
    'EVOKE', 'EXACT', 'EXALT', 'EXCEL', 'EXERT', 'EXILE', 'EXIST', 'EXPEL', 'EXTOL', 'EXTRA',
    'EXULT', 'EYING',
    'FABLE', 'FACET', 'FAINT', 'FAIRY', 'FAITH', 'FALSE', 'FANCY', 'FANNY', 'FARCE', 'FATAL',
    'FATTY', 'FAULT', 'FAUNA', 'FAVOR', 'FEAST', 'FECAL', 'FEIGN', 'FELLA', 'FELON', 'FEMME',
    'FEMUR', 'FENCE', 'FERAL', 'FERRY', 'FETAL', 'FETCH', 'FETID', 'FETUS', 'FEVER', 'FEWER',
    'FIBER', 'FICUS', 'FIELD', 'FIEND', 'FIERY', 'FIFTH', 'FIFTY', 'FIGHT', 'FILER', 'FILET',
    'FILLY', 'FILMY', 'FILTH', 'FINAL', 'FINCH', 'FINER', 'FIRST', 'FISHY', 'FIXER', 'FIZZY',
    'FJORD', 'FLACK', 'FLAIL', 'FLAIR', 'FLAKE', 'FLAKY', 'FLAME', 'FLANK', 'FLARE', 'FLASH',
    'FLASK', 'FLECK', 'FLEET', 'FLESH', 'FLICK', 'FLIER', 'FLING', 'FLINT', 'FLIRT', 'FLOAT',
    'FLOCK', 'FLOOD', 'FLOOR', 'FLORA', 'FLOSS', 'FLOUR', 'FLOUT', 'FLOWN', 'FLUFF', 'FLUID',
    'FLUKE', 'FLUME', 'FLUNG', 'FLUNK', 'FLUSH', 'FLUTE', 'FLYER', 'FOAMY', 'FOCAL', 'FOCUS',
    'FOGGY', 'FOIST', 'FOLIO', 'FOLLY', 'FORAY', 'FORCE', 'FORGE', 'FORGO', 'FORTE', 'FORTH',
    'FORTY', 'FORUM', 'FOUND', 'FOYER', 'FRAIL', 'FRAME', 'FRANK', 'FRAUD', 'FREAK', 'FREED',
    'FREER', 'FRESH', 'FRIAR', 'FRIED', 'FRILL', 'FRISK', 'FRITZ', 'FROCK', 'FROND', 'FRONT',
    'FROST', 'FROTH', 'FROWN', 'FROZE', 'FRUIT', 'FUDGE', 'FUGUE', 'FULLY', 'FUNGI', 'FUNKY',
    'FUNNY', 'FUROR', 'FURRY', 'FUSSY', 'FUZZY',
    'GAFFE', 'GAILY', 'GAMER', 'GAMMA', 'GAMUT', 'GASSY', 'GAUDY', 'GAUGE', 'GAUNT', 'GAUZE',
    'GAVEL', 'GAWKY', 'GAYER', 'GAYLY', 'GAZER', 'GECKO', 'GEEKY', 'GEESE', 'GENIE', 'GENRE',
    'GHOST', 'GHOUL', 'GIANT', 'GIDDY', 'GIPSY', 'GIRLY', 'GIRTH', 'GIVEN', 'GIVER', 'GLADE',
    'GLAND', 'GLARE', 'GLASS', 'GLAZE', 'GLEAM', 'GLEAN', 'GLIDE', 'GLINT', 'GLOAT', 'GLOBE',
    'GLOOM', 'GLORY', 'GLOSS', 'GLOVE', 'GLYPH', 'GNASH', 'GNOME', 'GODLY', 'GOING', 'GOLEM',
    'GOLLY', 'GONAD', 'GONER', 'GOODY', 'GOOEY', 'GOOFY', 'GOOSE', 'GORGE', 'GOUGE', 'GOURD',
    'GRACE', 'GRADE', 'GRAFT', 'GRAIL', 'GRAIN', 'GRAND', 'GRANT', 'GRAPE', 'GRAPH', 'GRASP',
    'GRASS', 'GRATE', 'GRAVE', 'GRAVY', 'GRAZE', 'GREAT', 'GREED', 'GREEN', 'GREET', 'GRIEF',
    'GRILL', 'GRIME', 'GRIMY', 'GRIND', 'GRIPE', 'GROAN', 'GROIN', 'GROOM', 'GROPE', 'GROSS',
    'GROUP', 'GROUT', 'GROVE', 'GROWL', 'GROWN', 'GRUEL', 'GRUFF', 'GRUNT', 'GUARD', 'GUAVA',
    'GUESS', 'GUEST', 'GUIDE', 'GUILD', 'GUILE', 'GUILT', 'GUISE', 'GULCH', 'GULLY', 'GUMBO',
    'GUMMY', 'GUPPY', 'GUSTO', 'GUSTY', 'GYPSY',
    'HABIT', 'HAIRY', 'HALVE', 'HANDY', 'HAPPY', 'HARDY', 'HAREM', 'HARPY', 'HARRY', 'HARSH',
    'HASTE', 'HASTY', 'HATCH', 'HATER', 'HAUNT', 'HAUTE', 'HAVEN', 'HAVOC', 'HAZEL', 'HEADY',
    'HEARD', 'HEART', 'HEATH', 'HEAVE', 'HEAVY', 'HEDGE', 'HEFTY', 'HEIST', 'HELIX', 'HELLO',
    'HENCE', 'HERON', 'HILLY', 'HINGE', 'HIPPO', 'HIPPY', 'HITCH', 'HOARD', 'HOBBY', 'HOIST',
    'HOLLY', 'HOMER', 'HONEY', 'HONOR', 'HORDE', 'HORNY', 'HORSE', 'HOTEL', 'HOTLY', 'HOUND',
    'HOUSE', 'HOVEL', 'HOVER', 'HOWDY', 'HUMAN', 'HUMID', 'HUMOR', 'HUMPH', 'HUMUS', 'HUNCH',
    'HUNKY', 'HURRY', 'HUSKY', 'HUSSY', 'HUTCH', 'HYDRO', 'HYENA', 'HYMEN', 'HYPER',
    'ICILY', 'ICING', 'IDEAL', 'IDIOM', 'IDIOT', 'IDLER', 'IDYLL', 'IGLOO', 'ILIAC', 'IMAGE',
    'IMBUE', 'IMPEL', 'IMPLY', 'INANE', 'INBOX', 'INCUR', 'INDEX', 'INEPT', 'INERT', 'INFER',
    'INGOT', 'INLAY', 'INLET', 'INNER', 'INPUT', 'INTER', 'INTRO', 'IONIC', 'IRATE', 'IRONY',
    'ISLET', 'ISSUE', 'ITCHY', 'IVORY',
    'JAUNT', 'JAZZY', 'JELLY', 'JERKY', 'JETTY', 'JEWEL', 'JIFFY', 'JOINT', 'JOIST', 'JOKER',
    'JOLLY', 'JOUST', 'JUDGE', 'JUICE', 'JUICY', 'JUMBO', 'JUMPY', 'JUNTA', 'JUNTO', 'JUROR',
    'KAPPA', 'KARMA', 'KAYAK', 'KEBAB', 'KHAKI', 'KINKY', 'KIOSK', 'KITTY', 'KNACK', 'KNAVE',
    'KNEAD', 'KNEED', 'KNEEL', 'KNELT', 'KNIFE', 'KNOCK', 'KNOLL', 'KNOWN', 'KOALA', 'KRILL',
    'LABEL', 'LABOR', 'LADEN', 'LADLE', 'LAGER', 'LANCE', 'LANKY', 'LAPEL', 'LAPSE', 'LARGE',
    'LARVA', 'LASSO', 'LATCH', 'LATER', 'LATHE', 'LATTE', 'LAUGH', 'LAYER', 'LEACH', 'LEAFY',
    'LEAKY', 'LEANT', 'LEAPT', 'LEARN', 'LEASE', 'LEASH', 'LEAST', 'LEAVE', 'LEDGE', 'LEECH',
    'LEERY', 'LEFTY', 'LEGAL', 'LEGGY', 'LEMON', 'LEMUR', 'LEPER', 'LEVEL', 'LEVER', 'LIBEL',
    'LIEGE', 'LIGHT', 'LIKEN', 'LILAC', 'LIMBO', 'LIMIT', 'LINEN', 'LINER', 'LINGO', 'LIPID',
    'LITHE', 'LIVER', 'LIVID', 'LLAMA', 'LOAMY', 'LOATH', 'LOBBY', 'LOCAL', 'LOCUS', 'LODGE',
    'LOFTY', 'LOGIC', 'LOGIN', 'LOOPY', 'LOOSE', 'LORRY', 'LOSER', 'LOUSE', 'LOUSY', 'LOVER',
    'LOWER', 'LOWLY', 'LOYAL', 'LUCID', 'LUCKY', 'LUMEN', 'LUMPY', 'LUNAR', 'LUNCH', 'LUNGE',
    'LUPUS', 'LURCH', 'LURID', 'LUSTY', 'LYING', 'LYMPH', 'LYRIC',
    'MACAW', 'MACHO', 'MACRO', 'MADAM', 'MADLY', 'MAFIA', 'MAGIC', 'MAGMA', 'MAIZE', 'MAJOR',
    'MAKER', 'MAMBO', 'MAMMA', 'MAMMY', 'MANGA', 'MANGE', 'MANGO', 'MANGY', 'MANIA', 'MANIC',
    'MANLY', 'MANOR', 'MAPLE', 'MARCH', 'MARRY', 'MARSH', 'MASON', 'MASSE', 'MATCH', 'MATEY',
    'MAUVE', 'MAXIM', 'MAYBE', 'MAYOR', 'MEALY', 'MEANT', 'MEATY', 'MECCA', 'MEDAL', 'MEDIA',
    'MEDIC', 'MELEE', 'MELON', 'MERCY', 'MERGE', 'MERIT', 'MERRY', 'METAL', 'METER', 'METRO',
    'MICRO', 'MIDGE', 'MIDST', 'MIGHT', 'MILKY', 'MIMIC', 'MINCE', 'MINER', 'MINIM', 'MINOR',
    'MINTY', 'MINUS', 'MIRTH', 'MISER', 'MISSY', 'MOCHA', 'MODAL', 'MODEL', 'MODEM', 'MOGUL',
    'MOIST', 'MOLAR', 'MOLDY', 'MONEY', 'MONTH', 'MOODY', 'MOOSE', 'MORAL', 'MORON', 'MORPH',
    'MOSSY', 'MOTEL', 'MOTIF', 'MOTOR', 'MOTTO', 'MOULT', 'MOUND', 'MOUNT', 'MOURN', 'MOUSE',
    'MOUTH', 'MOVER', 'MOVIE', 'MOWER', 'MUCKY', 'MUCUS', 'MUDDY', 'MULCH', 'MUMMY', 'MUNCH',
    'MURAL', 'MURKY', 'MUSHY', 'MUSIC', 'MUSKY', 'MUSTY', 'MYRRH',
    'NADIR', 'NAIVE', 'NANNY', 'NASAL', 'NASTY', 'NATAL', 'NAVAL', 'NAVEL', 'NEEDY', 'NEIGH',
    'NERDY', 'NERVE', 'NEVER', 'NEWER', 'NEWLY', 'NICER', 'NICHE', 'NIECE', 'NIGHT', 'NINJA',
    'NINNY', 'NINTH', 'NOBLE', 'NOBLY', 'NOISE', 'NOISY', 'NOMAD', 'NOOSE', 'NORTH', 'NOSEY',
    'NOTCH', 'NOVEL', 'NUDGE', 'NURSE', 'NUTTY', 'NYLON', 'NYMPH',
    'OAKEN', 'OBESE', 'OCCUR', 'OCEAN', 'OCTAL', 'OCTET', 'ODDER', 'ODDLY', 'OFFAL', 'OFFER',
    'OFTEN', 'OLDEN', 'OLDER', 'OLIVE', 'OMBRE', 'OMEGA', 'ONION', 'ONSET', 'OPERA', 'OPINE',
    'OPIUM', 'OPTIC', 'ORBIT', 'ORDER', 'ORGAN', 'OTHER', 'OTTER', 'OUGHT', 'OUNCE', 'OUTDO',
    'OUTER', 'OUTGO', 'OVARY', 'OVATE', 'OVERT', 'OVINE', 'OVOID', 'OWING', 'OWNER', 'OXIDE',
    'OZONE',
    'PADDY', 'PAGAN', 'PAINT', 'PALER', 'PALSY', 'PANEL', 'PANIC', 'PANSY', 'PAPAL', 'PAPER',
    'PARER', 'PARKA', 'PARRY', 'PARSE', 'PARTY', 'PASTA', 'PASTE', 'PASTY', 'PATCH', 'PATIO',
    'PATSY', 'PATTY', 'PAUSE', 'PAYEE', 'PAYER', 'PEACE', 'PEACH', 'PEARL', 'PECAN', 'PEDAL',
    'PENAL', 'PENCE', 'PENNE', 'PENNY', 'PERCH', 'PERIL', 'PERKY', 'PESKY', 'PESTO', 'PETAL',
    'PETTY', 'PHASE', 'PHONE', 'PHONY', 'PHOTO', 'PIANO', 'PICKY', 'PIECE', 'PIETY', 'PIGGY',
    'PILOT', 'PINCH', 'PINEY', 'PINKY', 'PINTO', 'PIPER', 'PIQUE', 'PITCH', 'PITHY', 'PIVOT',
    'PIXEL', 'PIXIE', 'PIZZA', 'PLACE', 'PLAID', 'PLAIN', 'PLAIT', 'PLANE', 'PLANK', 'PLANT',
    'PLATE', 'PLAZA', 'PLEAD', 'PLEAT', 'PLIED', 'PLIER', 'PLUCK', 'PLUMB', 'PLUME', 'PLUMP',
    'PLUNK', 'PLUSH', 'POESY', 'POINT', 'POISE', 'POKER', 'POLAR', 'POLKA', 'POLYP', 'POOCH',
    'POPPY', 'PORCH', 'POSER', 'POSIT', 'POSSE', 'POUCH', 'POUND', 'POUTY', 'POWER', 'PRANK',
    'PRAWN', 'PREEN', 'PRESS', 'PRICE', 'PRICK', 'PRIDE', 'PRIED', 'PRIME', 'PRIMO', 'PRINT',
    'PRIOR', 'PRISM', 'PRIVY', 'PRIZE', 'PROBE', 'PRONE', 'PRONG', 'PROOF', 'PROSE', 'PROUD',
    'PROVE', 'PROWL', 'PROXY', 'PRUDE', 'PRUNE', 'PSALM', 'PUBIC', 'PUDGY', 'PUFFY', 'PULPY',
    'PULSE', 'PUNCH', 'PUPIL', 'PUPPY', 'PUREE', 'PURER', 'PURGE', 'PURSE', 'PUSHY', 'PUTTY',
    'PYGMY', 'QUACK', 'QUAIL', 'QUAKE', 'QUALM', 'QUARK', 'QUART', 'QUASH', 'QUASI', 'QUEEN',
    'QUEER', 'QUELL', 'QUERY', 'QUEST', 'QUEUE', 'QUICK', 'QUIET', 'QUILL', 'QUILT', 'QUIRK',
    'QUITE', 'QUOTA', 'QUOTE', 'QUOTH',
    'RABBI', 'RABID', 'RACER', 'RADAR', 'RADII', 'RADIO', 'RAINY', 'RAISE', 'RAJAH', 'RALLY',
    'RALPH', 'RAMEN', 'RANCH', 'RANDY', 'RANGE', 'RAPID', 'RARER', 'RASPY', 'RATIO', 'RATTY',
    'RAVEN', 'RAYON', 'RAZOR', 'REACH', 'REACT', 'READY', 'REALM', 'REARM', 'REBAR', 'REBEL',
    'REBUS', 'REBUT', 'RECAP', 'RECUR', 'RECUT', 'REEDY', 'REFER', 'REFIT', 'REGAL', 'REHAB',
    'REIGN', 'RELAX', 'RELAY', 'RELIC', 'REMIT', 'RENAL', 'RENEW', 'REPAY', 'REPEL', 'REPLY',
    'RERUN', 'RESET', 'RESIN', 'RETCH', 'RETRO', 'RETRY', 'REUSE', 'REVEL', 'REVUE', 'RHINO',
    'RHYME', 'RIDER', 'RIDGE', 'RIFLE', 'RIGHT', 'RIGID', 'RIGOR', 'RINSE', 'RIPEN', 'RIPER',
    'RISEN', 'RISER', 'RISKY', 'RIVAL', 'RIVER', 'RIVET', 'ROACH', 'ROAST', 'ROBIN', 'ROBOT',
    'ROCKY', 'RODEO', 'ROGER', 'ROGUE', 'ROOMY', 'ROOST', 'ROTOR', 'ROUGE', 'ROUGH', 'ROUND',
    'ROUSE', 'ROUTE', 'ROVER', 'ROWDY', 'ROWER', 'ROYAL', 'RUDDY', 'RUDER', 'RUGBY', 'RULER',
    'RUMBA', 'RUMOR', 'RUPEE', 'RURAL', 'RUSTY',
    'SADLY', 'SAFER', 'SAINT', 'SALAD', 'SALLY', 'SALON', 'SALSA', 'SALTY', 'SALVE', 'SALVO',
    'SANDY', 'SANER', 'SAPPY', 'SASSY', 'SATIN', 'SATYR', 'SAUCE', 'SAUCY', 'SAUNA', 'SAUTE',
    'SAVOR', 'SAVOY', 'SAVVY', 'SCALD', 'SCALE', 'SCALP', 'SCALY', 'SCAMP', 'SCANT', 'SCARE',
    'SCARF', 'SCARY', 'SCENE', 'SCENT', 'SCION', 'SCOFF', 'SCOLD', 'SCONE', 'SCOOP', 'SCOPE',
    'SCORE', 'SCORN', 'SCOUR', 'SCOUT', 'SCOWL', 'SCRAM', 'SCRAP', 'SCREE', 'SCREW', 'SCRUB',
    'SCRUM', 'SCUBA', 'SEDAN', 'SEEDY', 'SEGUE', 'SEIZE', 'SEMEN', 'SENSE', 'SEPIA', 'SERIF',
    'SERUM', 'SERVE', 'SETUP', 'SEVEN', 'SEVER', 'SEWER', 'SHACK', 'SHADE', 'SHADY', 'SHAFT',
    'SHAKE', 'SHAKY', 'SHALE', 'SHALL', 'SHALT', 'SHAME', 'SHANK', 'SHAPE', 'SHARD', 'SHARE',
    'SHARK', 'SHARP', 'SHAVE', 'SHAWL', 'SHEAR', 'SHEEN', 'SHEEP', 'SHEER', 'SHEET', 'SHEIK',
    'SHELF', 'SHELL', 'SHIED', 'SHIFT', 'SHINE', 'SHINY', 'SHIRE', 'SHIRK', 'SHIRT', 'SHOAL',
    'SHOCK', 'SHONE', 'SHOOK', 'SHOOT', 'SHORE', 'SHORN', 'SHORT', 'SHOUT', 'SHOVE', 'SHOWN',
    'SHOWY', 'SHREW', 'SHRUB', 'SHRUG', 'SHUCK', 'SHUNT', 'SHUSH', 'SHYLY', 'SIEGE', 'SIEVE',
    'SIGHT', 'SIGMA', 'SILKY', 'SILLY', 'SINCE', 'SINEW', 'SINGE', 'SIREN', 'SISSY', 'SIXTH',
    'SIXTY', 'SKATE', 'SKIER', 'SKIFF', 'SKILL', 'SKIMP', 'SKIRT', 'SKULK', 'SKULL', 'SKUNK',
    'SLACK', 'SLAIN', 'SLANG', 'SLANT', 'SLASH', 'SLATE', 'SLEEK', 'SLEEP', 'SLEET', 'SLEPT',
    'SLICE', 'SLICK', 'SLIDE', 'SLIME', 'SLIMY', 'SLING', 'SLINK', 'SLOOP', 'SLOPE', 'SLOSH',
    'SLOTH', 'SLUMP', 'SLUNG', 'SLUNK', 'SLURP', 'SLUSH', 'SLYLY', 'SMACK', 'SMALL', 'SMART',
    'SMASH', 'SMEAR', 'SMELL', 'SMELT', 'SMILE', 'SMIRK', 'SMITE', 'SMITH', 'SMOCK', 'SMOKE',
    'SMOKY', 'SMOTE', 'SNACK', 'SNAIL', 'SNAKE', 'SNAKY', 'SNARE', 'SNARL', 'SNEAK', 'SNEER',
    'SNIDE', 'SNIFF', 'SNIPE', 'SNOOP', 'SNORE', 'SNORT', 'SNOUT', 'SNOWY', 'SNUCK', 'SNUFF',
    'SOAPY', 'SOBER', 'SOGGY', 'SOLAR', 'SOLID', 'SOLVE', 'SONAR', 'SONIC', 'SOOTH', 'SOOTY',
    'SORRY', 'SOUND', 'SOUTH', 'SOWER', 'SPACE', 'SPADE', 'SPANK', 'SPARE', 'SPARK', 'SPASM',
    'SPAWN', 'SPEAK', 'SPEAR', 'SPECK', 'SPEED', 'SPELL', 'SPELT', 'SPEND', 'SPENT', 'SPERM',
    'SPICE', 'SPICY', 'SPIED', 'SPIEL', 'SPIKE', 'SPIKY', 'SPILL', 'SPILT', 'SPINE', 'SPINY',
    'SPIRE', 'SPITE', 'SPLAT', 'SPLIT', 'SPOIL', 'SPOKE', 'SPOOF', 'SPOOK', 'SPOOL', 'SPOON',
    'SPORE', 'SPORT', 'SPOUT', 'SPRAY', 'SPREE', 'SPRIG', 'SPUNK', 'SPURN', 'SPURT', 'SQUAD',
    'SQUAT', 'SQUIB', 'STACK', 'STAFF', 'STAGE', 'STAID', 'STAIN', 'STAIR', 'STAKE', 'STALE',
    'STALK', 'STALL', 'STAMP', 'STAND', 'STANK', 'STARE', 'STARK', 'START', 'STASH', 'STATE',
    'STAVE', 'STEAD', 'STEAK', 'STEAL', 'STEAM', 'STEED', 'STEEL', 'STEEP', 'STEER', 'STEIN',
    'STERN', 'STICK', 'STIFF', 'STILL', 'STILT', 'STING', 'STINK', 'STINT', 'STOCK', 'STOIC',
    'STOKE', 'STOLE', 'STOMP', 'STONE', 'STONY', 'STOOD', 'STOOL', 'STOOP', 'STORE', 'STORK',
    'STORM', 'STORY', 'STOUT', 'STOVE', 'STRAP', 'STRAW', 'STRAY', 'STRIP', 'STRUT', 'STUCK',
    'STUDY', 'STUFF', 'STUMP', 'STUNG', 'STUNK', 'STUNT', 'STYLE', 'SUAVE', 'SUGAR', 'SUING',
    'SUITE', 'SULKY', 'SULLY', 'SUMAC', 'SUNNY', 'SUPER', 'SURER', 'SURGE', 'SURLY', 'SUSHI',
    'SWAMI', 'SWAMP', 'SWARM', 'SWASH', 'SWATH', 'SWEAR', 'SWEAT', 'SWEEP', 'SWEET', 'SWELL',
    'SWEPT', 'SWIFT', 'SWILL', 'SWINE', 'SWING', 'SWIRL', 'SWISH', 'SWOON', 'SWOOP', 'SWORD',
    'SWORE', 'SWORN', 'SWUNG', 'SYNOD', 'SYRUP',
    'TABBY', 'TABLE', 'TABOO', 'TACIT', 'TACKY', 'TAFFY', 'TAINT', 'TAKEN', 'TAKER', 'TALLY',
    'TALON', 'TAMER', 'TANGO', 'TANGY', 'TAPER', 'TAPIR', 'TARDY', 'TAROT', 'TASTE', 'TASTY',
    'TATTY', 'TAUNT', 'TAWNY', 'TEACH', 'TEARY', 'TEASE', 'TEDDY', 'TEETH', 'TEMPO', 'TENET',
    'TENOR', 'TENSE', 'TENTH', 'TEPEE', 'TEPID', 'TERRA', 'TERSE', 'TESTY', 'THANK', 'THEFT',
    'THEIR', 'THEME', 'THERE', 'THESE', 'THETA', 'THICK', 'THIEF', 'THIGH', 'THING', 'THINK',
    'THIRD', 'THONG', 'THORN', 'THOSE', 'THREE', 'THREW', 'THROB', 'THROW', 'THRUM', 'THUMB',
    'THUMP', 'THYME', 'TIARA', 'TIBIA', 'TIDAL', 'TIGER', 'TIGHT', 'TILDE', 'TIMER', 'TIMID',
    'TIPSY', 'TITAN', 'TITHE', 'TITLE', 'TOAST', 'TODAY', 'TODDY', 'TOKEN', 'TONAL', 'TONGA',
    'TONIC', 'TOOTH', 'TOPAZ', 'TOPIC', 'TORCH', 'TORSO', 'TORUS', 'TOTAL', 'TOTEM', 'TOUCH',
    'TOUGH', 'TOWEL', 'TOWER', 'TOXIC', 'TOXIN', 'TRACE', 'TRACK', 'TRACT', 'TRADE', 'TRAIL',
    'TRAIN', 'TRAIT', 'TRAMP', 'TRASH', 'TRAWL', 'TREAD', 'TREAT', 'TREND', 'TRIAD', 'TRIAL',
    'TRIBE', 'TRICE', 'TRICK', 'TRIED', 'TRIPE', 'TRITE', 'TROLL', 'TROOP', 'TROPE', 'TROUT',
    'TROVE', 'TRUCE', 'TRUCK', 'TRUER', 'TRULY', 'TRUMP', 'TRUNK', 'TRUSS', 'TRUST', 'TRUTH',
    'TRYST', 'TUBAL', 'TUBER', 'TULIP', 'TULLE', 'TUMOR', 'TUNIC', 'TURBO', 'TUTOR', 'TWANG',
    'TWEAK', 'TWEED', 'TWEET', 'TWICE', 'TWINE', 'TWIRL', 'TWIST', 'TWIXT', 'TYING',
    'UDDER', 'ULCER', 'ULTRA', 'UMBRA', 'UNCLE', 'UNCUT', 'UNDER', 'UNDID', 'UNDUE', 'UNFED',
    'UNFIT', 'UNIFY', 'UNION', 'UNITE', 'UNITY', 'UNLIT', 'UNMET', 'UNSET', 'UNTIE', 'UNTIL',
    'UNWED', 'UNZIP', 'UPPER', 'UPSET', 'URBAN', 'URINE', 'USAGE', 'USHER', 'USING', 'USUAL',
    'USURP', 'UTILE', 'UTTER',
    'VAGUE', 'VALET', 'VALID', 'VALOR', 'VALUE', 'VALVE', 'VAPID', 'VAPOR', 'VAULT', 'VAUNT',
    'VEGAN', 'VENOM', 'VENUE', 'VERGE', 'VERSE', 'VERSO', 'VERVE', 'VICAR', 'VIDEO', 'VIGIL',
    'VIGOR', 'VILLA', 'VINYL', 'VIOLA', 'VIPER', 'VIRAL', 'VIRUS', 'VISIT', 'VISOR', 'VISTA',
    'VITAL', 'VIVID', 'VIXEN', 'VOCAL', 'VODKA', 'VOGUE', 'VOICE', 'VOILA', 'VOMIT', 'VOTER',
    'VOUCH', 'VOWEL', 'VYING',
    'WACKY', 'WAFER', 'WAGER', 'WAGON', 'WAIST', 'WAIVE', 'WALTZ', 'WARTY', 'WASTE', 'WATCH',
    'WATER', 'WAVER', 'WAXEN', 'WEARY', 'WEAVE', 'WEDGE', 'WEEDY', 'WEIGH', 'WEIRD', 'WELCH',
    'WELSH', 'WHACK', 'WHALE', 'WHARF', 'WHEAT', 'WHEEL', 'WHELP', 'WHERE', 'WHICH', 'WHIFF',
    'WHILE', 'WHINE', 'WHINY', 'WHIRL', 'WHISK', 'WHITE', 'WHOLE', 'WHOOP', 'WHOSE', 'WIDEN',
    'WIDER', 'WIDOW', 'WIDTH', 'WIELD', 'WIGHT', 'WILLY', 'WIMPY', 'WINCE', 'WINCH', 'WINDY',
    'WISER', 'WISPY', 'WITCH', 'WITTY', 'WOKEN', 'WOMAN', 'WOMEN', 'WOODY', 'WOOER', 'WOOLY',
    'WOOZY', 'WORDY', 'WORLD', 'WORRY', 'WORSE', 'WORST', 'WORTH', 'WOULD', 'WOUND', 'WOVEN',
    'WRACK', 'WRATH', 'WREAK', 'WRECK', 'WREST', 'WRING', 'WRIST', 'WRITE', 'WRONG', 'WROTE',
    'WRUNG', 'WRYLY',
    'YACHT', 'YEARN', 'YEAST', 'YIELD', 'YOUNG', 'YOUTH',
    'ZEBRA', 'ZESTY', 'ZONAL'
    # LIST OF MOST COMMON https://www.dictionary.com/e/wordle/
    'ADIEU', 'AISLE', 'ALIEN', 'ALTER', 'ANIME', 'AORTA', 'ARISE', 'ASIDE',
    'AUDIO', 'BACON', 'BEAUT', 'BORED', 'CAUSE', 'CRATE', 'CRACK', 'CREST',
    'EARNS', 'EIGHT', 'FEAST', 'GREAT', 'HARPY', 'HOIST', 'IDEAL', 'IDEAS',
    'INGOT', 'IRATE', 'LEARN', 'LEAST', 'LOYAL', 'MEANY', 'MEATS', 'MEDIA',
    'MOUSY', 'NICHE', 'NOTES', 'OMEGA', 'OPERA', 'PEACE', 'PEARS', 'PILOT',
    'PITHY', 'PLANT', 'POINT', 'PORTS', 'POWER', 'PRIOR', 'QUEST', 'RAGES',
    'RATES', 'RATIO', 'RENTS', 'ROUSE', 'SCALE', 'SHAPE', 'SHORE', 'SNARE',
    'SPORT', 'STARE', 'STEAK', 'STERN', 'STOIC', 'STONY', 'STORE', 'STRAP',
    'TABLE', 'TEAMS', 'TEARS', 'THOSE', 'TIRED', 'TOUCH', 'TRAIN', 'WATER',
    'YEAST', 'YOUTH']
    app.lengthOfWords = len(app.words)
    app.targetWord = getWord(app)
    app.greenLetters = []
    app.yellowLetters = []
    app.grayLetters = []
    app.cellColors = [['black' for i in range(app.cols)] for j in range(app.rows)]
    app.computerCellColors = [['black' for i in range(app.cols)] for j in range(app.rows)]
    app.keyColors = dict()
    app.paused = True
    app.computerGuess = None
    app.stepsPerSecond = 1
    app.computerCurrentRow = 0
    app.computerCurrentCol = 0
    app.computerGuesses = []
    app.playerGuesses = []
    app.counter = 0
    app.guess = None

    # INPUT BOARD
    app.inputBoardLeft = 100
    app.inputBoardTop = 560
    app.inputBoardWidth = 800
    app.inputBoardHeight = 200
    app.inputBorderWidth = 1
    app.mode = None

    # SINGLE PLAYER BOARD
    app.singlePlayerBoardWidth = 250
    app.singlePlayerBoardHeight = 300
    app.singlePlayerBoardLeft = 375
    app.singlePlayerBoardTop = 75
    app.singlePlayerBorderWidth = 1
    app.possibleWords = copy.copy(app.words)
    app.playerPossibleWords = copy.copy(app.words)
    app.hardPossibleWords = copy.copy(app.words)
    app.nextWord = 'ADIEU'
    app.time = 30
    app.constraints = {}
    
    # HINTS FROM https://www.dictionary.com/e/wordle/
    app.hints = ['ADIEU', 'AISLE', 'ALIEN', 'ALTER', 'ANIME', 'AORTA', 'ARISE', 'ASIDE',
             'AUDIO', 'BACON', 'BEAUT', 'BORED', 'CAUSE', 'CRATE', 'CRACK', 'CREST',
             'EARNS', 'EIGHT', 'FEAST', 'GREAT', 'HARPY', 'HOIST', 'IDEAL', 'IDEAS',
             'INGOT', 'IRATE', 'LEARN', 'LEAST', 'LOYAL', 'MEANY', 'MEATS', 'MEDIA',
             'MOUSY', 'NICHE', 'NOTES', 'OMEGA', 'OPERA', 'PEACE', 'PEARS', 'PILOT',
             'PITHY', 'PLANT', 'POINT', 'PORTS', 'POWER', 'PRIOR', 'QUEST', 'RAGES',
             'RATES', 'RATIO', 'RENTS', 'ROUSE', 'SCALE', 'SHAPE', 'SHORE', 'SNARE',
             'SPORT', 'STARE', 'STEAK', 'STERN', 'STOIC', 'STONY', 'STORE', 'STRAP',
             'TABLE', 'TEAMS', 'TEARS', 'THOSE', 'TIRED', 'TOUCH', 'TRAIN', 'WATER',
             'YEAST', 'YOUTH']

    app.hint = None
    app.add = True
    # Wordlist including words that end with s from 
    # https://www.merriam-webster.com/wordfinder/classic/ends/common/5/s/2
    app.wordlist = app.words + [
        'ABBAS', 'ABYSS', 'ACHES', 'ACIDS', 'ACRES', 'AEGIS', 'AIDES', 'ALIAS', 'AMASS', 'AMISS', 
        'AREAS', 'ARIAS', 'ASHES', 'ASSES', 'ATLAS', 'ATOMS', 'AUNTS', 'AUTOS', 'BABES', 'BACKS', 
        'BALLS', 'BANDS', 'BANGS', 'BANKS', 'BARKS', 'BARNS', 'BASES', 'BASIS', 'BATES', 'BATHS', 
        'BEADS', 'BEAMS', 'BEANS', 'BEARS', 'BEATS', 'BEERS', 'BEETS', 'BELLS', 'BELTS', 'BENDS', 
        'BIGGS', 'BIKES', 'BILLS', 'BINDS', 'BIRDS', 'BITES', 'BLESS', 'BLISS', 'BLOGS', 'BLOWS', 
        'BLUES', 'BOATS', 'BOGUS', 'BOILS', 'BOLTS', 'BOMBS', 'BONDS', 'BONES', 'BONUS', 'BOOBS', 
        'BOOKS', 'BOOTS', 'BOUTS', 'BOWLS', 'BOXES', 'BRASS', 'BRITS', 'BROWS', 'BUCKS', 'BUFFS', 
        'BULBS', 'BULLS', 'BUMPS', 'BURNS', 'BUSES', 'BUSTS', 'BUTTS', 'BYTES', 'CAFES', 'CAGES', 
        'CAKES', 'CALLS', 'CAMPS', 'CANES', 'CARBS', 'CARDS', 'CARES', 'CARTS', 'CASES', 'CASTS', 
        'CAVES', 'CELLS', 'CENTS', 'CHAOS', 'CHAPS', 'CHATS', 'CHEFS', 'CHESS', 'CHIPS', 'CHOPS', 
        'CITES', 'CLAMS', 'CLANS', 'CLASS', 'CLAWS', 'CLIPS', 'CLUBS', 'CLUES', 'COATS', 'COCKS', 
        'CODES', 'COILS', 'COINS', 'COLES', 'COLTS', 'COMBS', 'COMES', 'CONES', 'COOKS', 'COOLS', 
        'CORDS', 'CORES', 'CORPS', 'COSTS', 'CRABS', 'CRASS', 'CRESS', 'CREWS', 'CRIES', 'CROPS', 
        'CROSS', 'CROWS', 'CUBES', 'CUFFS', 'CULTS', 'CURES', 'CURLS', 'DARES', 'DARTS', 'DATES', 
        'DEALS', 'DEANS', 'DEBTS', 'DECKS', 'DEEDS', 'DEEMS', 'DEMOS', 'DESKS', 'DICKS', 'DIETS', 
        'DISCS', 'DISKS', 'DIVAS', 'DOCKS', 'DOLLS', 'DOORS', 'DOSES', 'DOVES', 'DOWNS', 'DRAGS', 
        'DRAWS', 'DRESS', 'DRIES', 'DROPS', 'DROSS', 'DRUGS', 'DRUMS', 'DUCKS', 'DUCTS', 'DUDES', 
        'DUKES', 'DUMPS', 'DUNES', 'EARNS', 'EDGES', 'EDITS', 'ELVES', 'EMITS', 'ETHOS', 'EUROS', 
        'EVILS', 'EXAMS', 'EXECS', 'EXITS', 'FACES', 'FACTS', 'FADES', 'FAILS', 'FAIRS', 'FAKES', 
        'FALLS', 'FANGS', 'FARES', 'FARMS', 'FARTS', 'FATES', 'FEARS', 'FEATS', 'FECES', 'FEEDS', 
        'FEELS', 'FERNS', 'FETUS', 'FICUS', 'FILES', 'FILLS', 'FILMS', 'FINDS', 'FINES', 'FIRES', 
        'FIRMS', 'FISTS', 'FIVES', 'FIXES', 'FLAGS', 'FLAPS', 'FLATS', 'FLAWS', 'FLEAS', 'FLIES', 
        'FLIPS', 'FLOPS', 'FLOSS', 'FLOWS', 'FOCUS', 'FOLDS', 'FOLKS', 'FONTS', 'FOODS', 'FOOLS', 
        'FORKS', 'FORMS', 'FORTS', 'FOULS', 'FOURS', 'FOXES', 'FREES', 'FRIES', 'FROGS', 'FUELS', 
        'FUMES', 'FUNDS', 'FUSES', 'GAINS', 'GAMES', 'GANGS', 'GASES', 'GATES', 'GEARS', 'GEEKS', 
        'GENES', 'GENTS', 'GENUS', 'GERMS', 'GIFTS', 'GILLS', 'GIRLS', 'GIVES', 'GLASS', 'GLOSS', 
        'GOALS', 'GOATS', 'GOERS', 'GOLDS', 'GOODS', 'GOONS', 'GOWNS', 'GRABS', 'GRAMS', 'GRASS', 
        'GRIDS', 'GRIPS', 'GROSS', 'GROWS', 'GUESS', 'GUSTS', 'HACKS', 'HAILS', 'HAIRS', 'HALLS', 
        'HANDS', 'HANGS', 'HANKS', 'HARMS', 'HATES', 'HAWKS', 'HAYES', 'HEADS', 'HEALS', 'HEAPS', 
        'HEARS', 'HEATS', 'HEELS', 'HEIRS', 'HELLS', 'HELPS', 'HERBS', 'HERDS', 'HERES', 'HICKS', 
        'HIDES', 'HIGHS', 'HIKES', 'HILLS', 'HINES', 'HINTS', 'HIRES', 'HIVES', 'HOLDS', 'HOLES', 
        'HOMES', 'HOODS', 'HOOKS', 'HOOPS', 'HOPES', 'HORNS', 'HOSTS', 'HOURS', 'HUMUS', 'HUNTS', 
        'HURTS', 'HYMNS', 'ICONS', 'IDEAS', 'IDOLS', 'IRONS', 'ISLES', 'ITEMS', 'JACKS', 'JAILS', 
        'JEANS', 'JERKS', 'JOHNS', 'JOINS', 'JOKES', 'JONES', 'JUMPS', 'KEEPS', 'KICKS', 'KILLS', 
        'KILOS', 'KINDS', 'KINKS', 'KNEES', 'KNOBS', 'KNOTS', 'KNOWS', 'KUDOS', 'LACES', 'LACKS', 
        'LAKES', 'LAKHS', 'LAMBS', 'LAMPS', 'LANDS', 'LANES', 'LASTS', 'LAWNS', 'LEADS', 'LEAFS', 
        'LEAKS', 'LEANS', 'LEAPS', 'LEEDS', 'LENDS', 'LEWIS', 'LIARS', 'LICKS', 'LIFTS', 'LIKES', 
        'LIMBS', 'LINES', 'LINKS', 'LINUS', 'LIONS', 'LISTS', 'LIVES', 'LOADS', 'LOANS', 'LOBES', 
        'LOCKS', 'LOCUS', 'LONGS', 'LOOKS', 'LOOMS', 'LOOPS', 'LOSES', 'LOTUS', 'LOVES', 'LUMPS', 
        'LUNGS', 'LUPUS', 'MACOS', 'MAIDS', 'MAILS', 'MAINS', 'MAKES', 'MALES', 'MALLS', 'MARKS', 
        'MASKS', 'MATES', 'MATHS', 'MEALS', 'MEANS', 'MEATS', 'MEETS', 'MELTS', 'MEMES', 'MENUS', 
        'MILES', 'MILLS', 'MINDS', 'MINES', 'MINTS', 'MINUS', 'MITES', 'MIXES', 'MOANS', 'MOCKS', 
        'MODES', 'MOLDS', 'MOTES', 'MOLLS', 'MOLDS', 'MOLES', 'MONKS', 'MOODS', 'MOONS', 'MOORS', 
        'MOTHS', 'MOVES', 'MUCKS', 'MULES', 'MUSES', 'MYTHS', 'NAILS', 'NAMES', 'NECKS', 'NEEDS', 
        'NERDS', 'NESTS', 'NEXUS', 'NICKS', 'NODES', 'NORMS', 'NOSES', 'NOTES', 'NOUNS', 'NUDES', 
        'NUKES', 'OASIS', 'OPENS', 'OVENS', 'OVERS', 'PACES', 'PACKS', 'PAGES', 'PAINS', 'PAIRS', 
        'PALMS', 'PANTS', 'PARKS', 'PARTS', 'PATHS', 'PEAKS', 'PEARS', 'PEEPS', 'PEERS', 'PENIS', 
        'PERKS', 'PESOS', 'PESTS', 'PICKS', 'PIERS', 'PILES', 'PILLS', 'PINES', 'PINTS', 'PIOUS', 
        'PIPES', 'PLANS', 'PLAYS', 'PLEAS', 'PLOTS', 'PLUGS', 'POEMS', 'POETS', 'POLES', 'POLLS', 
        'PONDS', 'POOLS', 'POPES', 'PORES', 'PORTS', 'POSES', 'POSTS', 'POURS', 'PRAYS', 'PRESS', 
        'PRIUS', 'PROPS', 'PUFFS', 'PULLS', 'PUMPS', 'QUITS', 'RACES', 'RACKS', 'RAGES', 'RAIDS', 
        'RAILS', 'RAINS', 'RAMPS', 'RANKS', 'RANTS', 'RAPES', 'RATES', 'RAZES', 'READS', 'REALS', 
        'REAPS', 'REARS', 'REBELS', 'RENTS', 'RESTS', 'RIDES', 
        'RINGS', 'RISES', 'RISKS', 'ROADS', 'ROBES', 'ROCKS', 'ROLES', 'ROLLS', 'ROOTS', 'ROPES', 
        'ROSES', 'ROUNDS', 'RUINS', 'RULES', 'RUNS', 'SACKS', 'SAILS', 'SAINTS', 'SAVES', 'SCANS', 
        'SCARS', 'SCENES', 'SCENTS', 'SCREWS', 'SEALS', 'SEEDS', 'SEEMS', 'SEES', 'SELLS', 'SENDS', 
        'SEVERS', 'SHAPES', 'SHARES', 'SHIFTS', 'SHIRTS', 'SHOES', 'SHORES', 'SHOTS', 'SHOWS', 'SHUTS', 
        'SIDES', 'SIFTS', 'SIGNS', 'SINGS', 'SITES', 'SIZES', 'SKINS', 'SLABS', 'SLAMS', 'SLIPS', 
        'SLOTS', 'SLOWS', 'SNAPS', 'SOCKS', 'SONGS', 'SORTS', 'SOULS', 'SPACES', 'SPANS', 'SPINS', 
        'SPOTS', 'SPURS', 'STAFFS', 'STARS', 'STATS', 'STEMS', 'STEPS', 'STIRS', 'STORES', 'STOVES', 
        'STRIPS', 'STROKES', 'STUDS', 'STYLES', 'SUITS', 'SWINGS', 'SWIPES', 'TALES', 'TANKS', 'TAPES', 
        'TASTES', 'TEAMS', 'TEARS', 'TERMS', 'TESTS', 'TEXTS', 'THINKS', 'TIES', 'TIMES', 'TONES', 
        'TOOLS', 'TOONS', 'TOURS', 'TRACES', 'TRACKS', 'TRAINS', 'TRAPS', 'TRENDS', 'TRIES', 'TRIPS', 
        'TUNES', 'TURNS', 'TYPES', 'UNITS', 'USERS', 'VASES', 'VIEWS', 'VOTES', 'WAGES', 'WALLS', 
        'WALKS', 'WANTS', 'WAVES', 'WEEKS', 'WHEELS', 'WHIPS', 'WINDS', 'WINGS', 'WIRES', 'WIVES', 
        'WOODS', 'WORKS', 'WORMS', 'WRAPS', 'YARDS', 'YIELDS', 'ZONES'
    ]
    app.win = None
    app.timerPaused = True
    app.invalid = False
    app.advancedHint = None
    app.easyLevelFill = 'gray'
    app.mediumLevelFill = 'gray'
    app.hardLevelFill = 'gray'
    app.impossibleLevelFill = 'gray'
    app.traditionalFill = 'gray'
    app.computerFill = 'gray'
    app.instructionsFill = 'gray'
    app.backFill = 'gray'
    app.hintFill = 'gray'
    app.advancedHintFill = 'gray'
    app.pauseFill = 'gray'
    
def redrawAll(app):
    drawRect(0,0,1000,1000,fill = 'black')
    if not app.over:
        # SELECT MODE
        if app.mode == None: # rgb found online
            drawRect(400, 200, 200, 100, fill = rgb(106,170,100))
            drawRect(400, 350, 200, 100, fill = rgb(201, 180, 88))
            drawRect(400, 500, 200, 100, fill = 'lightGray')
            drawRect(400, 200, 200, 100, fill = None, border = app.traditionalFill, borderWidth = 4)
            drawRect(400, 350, 200, 100, fill = None, border = app.computerFill, borderWidth = 4)
            drawRect(400, 500, 200, 100, fill = None, border = app.instructionsFill, borderWidth = 4)
            drawLabel('Traditional', 500, 250, size = 30, font = 'Noto Sans', fill = 'white')
            drawLabel('Computer', 500, 400, size = 30, font = 'Noto Sans', fill = 'white')
            drawLabel('Instructions', 500, 550, size = 30, font = 'Noto Sans', fill = 'white')
            drawLabel('AI Wordle Blitz: Select Game Mode', 500, 100, align = 'center', size = 50, 
                        font = 'Noto Sans', fill = 'white')
        # INSTRUCTIONS
        if app.mode == 'Instructions':
            drawLabel('TRADITIONAL', 500, 100, align = 'center', size = 50, fill = 'white')
            drawLabel('Normal Wordle with 6 guesses', 500, 150, align = 'center', size = 30, fill = 'white')
            drawLabel('*Hints do count as a guess', 500, 200, align = 'center', size = 30, fill = 'white')
            drawLabel('COMPUTER', 500, 350, align = 'center', size = 50, fill = 'white')
            drawLabel('Unlimited guesses', 500, 400, align = 'center', size = 30, fill = 'white')
            drawLabel('Use up and down arrow keys to scroll to see previous guesses', 500, 450, align = 'center', 
                        size = 30, fill = 'white')
            drawLabel('If time runs out, you lose', 500, 500, align = 'center', size = 30, fill = 'white')
            drawLabel('*No hints, pausing, or computer coloring in impossible mode', 500, 550, align = 'center', 
                        size = 30, fill = 'white')

            # HOME
            drawRect(10, 10, 100, 50, fill = 'lightGray')
            drawRect(10, 10, 100, 50, fill = None, border = app.backFill, borderWidth = 4)
            drawLabel('Home', 60, 35, size = 30, font = 'Noto Sans', fill = 'white')
        # COMPUTER - rgb found online
        if app.mode == 'Computer' and app.level == None:
            drawLabel('Select Level', 500, 150, align = 'center', size = 40, fill = 'white')
            # BUTTONS
            drawRect(400, 200, 200, 100, fill = 'paleGreen')
            drawRect(400, 350, 200, 100, fill = 'orange')
            drawRect(400, 500, 200, 100, fill = 'red')
            drawRect(400, 650, 200, 100, fill = 'indigo')

            drawRect(400, 200, 200, 100, fill = None, border = app.easyLevelFill, borderWidth = 4)
            drawRect(400, 350, 200, 100, fill = None, border = app.mediumLevelFill, borderWidth = 4)
            drawRect(400, 500, 200, 100, fill = None, border = app.hardLevelFill, borderWidth = 4)
            drawRect(400, 650, 200, 100, fill = None, border = app.impossibleLevelFill, borderWidth = 4)

            drawLabel('Easy', 500, 250, size = 30, font = 'Noto Sans', fill = 'white')
            drawLabel('Medium', 500, 400, size = 30, font = 'Noto Sans', fill = 'white')
            drawLabel('Hard', 500, 550, size = 30, font = 'Noto Sans', fill = 'white')
            drawLabel('Impossible', 500, 700, size = 30, font = 'Noto Sans', fill = 'white')

            # BACK
            drawRect(10, 10, 100, 50, fill = 'lightGray')
            drawRect(10, 10, 100, 50, fill = None, border = app.backFill, borderWidth = 4)
            drawLabel('Home', 60, 35, size = 30, font = 'Noto Sans', fill = 'white')

        # SELECT LEVEL
        if app.level != None:
            color = 'White'
            if app.level == 'Easy':
                color = 'paleGreen'
            elif app.level == 'Medium':
                color = 'orange'
            elif app.level == 'Hard':
                color = 'red'
            elif app.level == 'Impossible':
                color = 'indigo'
            drawLabel('Player', 275, 50, align = 'center', size = 40, fill = 'white')
            drawLabel('Computer', 725, 50, align = 'center', size = 40, fill = 'white')
            # drawLabel('Use up and down arrow keys to scroll', 500, 17.5, 
            #               align = 'center', size = 16, fill = 'white')
            drawLabel(f'Level: {app.level}', 500, 50, align = 'center', size = 30, fill = color)
            drawLabel(f'{app.time}', 500, 100, align = 'center', size = 50, fill = 'red')
            
            drawPlayerBoard(app)
            drawPlayerBorder(app)
            drawComputerBoard(app)
            drawComputerBorder(app)
            drawKeyboard(app)
           
            # BACK
            drawRect(10, 10, 100, 50, fill = 'lightGray')
            drawRect(10, 10, 100, 50, fill = None, border = app.backFill, borderWidth = 4)
            drawLabel('Home', 60, 35, size = 30, font = 'Noto Sans', fill = 'white')

            if app.level != 'Impossible':
                # HINT
                drawRect(875, 30, 100, 50, fill = rgb(106,170,100)) # rgb found online
                drawRect(875, 30, 100, 50, fill = None, border = app.hintFill, borderWidth = 4)
                drawLabel('Hint', 925, 55, align = 'center', font = 'Noto Sans', fill = 'white')
                # ADVANCED HINT
                drawRect(875, 90, 100, 50, fill = rgb(106,170,100)) # rgb found online
                drawRect(875, 90, 100, 50, fill = None, border = app.advancedHintFill, borderWidth = 4)
                drawLabel('Advanced Hint', 925, 115, font = 'Noto Sans', align = 'center', fill = 'white')
                # PAUSE
                drawRect(875, 150, 100, 50, fill = rgb(201, 180, 88)) # rgb found online
                drawRect(875, 150, 100, 50, fill = None, border = app.pauseFill, borderWidth = 4)
                drawLabel('Pause', 925, 175, font = 'Noto Sans', align = 'center', fill = 'white')
        # SINGLE
        elif app.mode == 'Single':
            drawSinglePlayerBoard(app)
            drawSinglePlayerBorder(app)
            drawKeyboard(app)
            drawKeyboardBorder(app)
            # drawInputBoard(app)
            # BACK
            drawRect(10, 10, 100, 50, fill = 'lightGray')
            drawRect(10, 10, 100, 50, fill = None, border = app.backFill, borderWidth = 4)
            drawLabel('Home', 60, 35, size = 30, font = 'Noto Sans', fill = 'white')
            # HINT
            drawRect(875, 30, 100, 50, fill = rgb(106,170,100)) # rgb found online
            drawRect(875, 30, 100, 50, fill = None, border = app.hintFill, borderWidth = 4)
            drawLabel('Hint', 925, 55, align = 'center', font = 'Noto Sans', fill = 'white')
            # ADVANCED HINT
            drawRect(875, 90, 100, 50, fill = rgb(106,170,100)) # rgb found online
            drawRect(875, 90, 100, 50, fill = None, border = app.advancedHintFill, borderWidth = 4)
            drawLabel('Advanced Hint', 925, 115, font = 'Noto Sans', align = 'center', fill = 'white')
        
        if app.invalid == True:
            drawRect(400, 200, 200, 100, fill = rgb(120, 124, 126)) # rgb found online
            drawRect(400, 200, 200, 100, fill = None, border = 'white')
            drawLabel('Invalid Word', 500, 250, align = 'center', font = 'Noto Sans', fill = 'white', size = 30)
            drawRect(580, 200, 20, 20, fill = 'salmon')
            drawRect(580, 200, 20, 20, fill = None, border = 'white')
            drawLabel('x', 590, 210, align = 'center', font = 'Noto Sans', fill = 'white', size = 30)

    # COMPUTER OVER
    elif app.over and app.mode == 'Computer':
        if app.win == True:
                drawLabel('You Win!', 500, 35, align = 'center', size = 40, fill = 'white')
        else:
            drawLabel(f'You Lose, the word was {app.targetWord}', 500, 35, align = 'center', size = 40, fill = 'white')
        drawPlayerBoard(app)
        drawPlayerBorder(app)
        drawComputerBoard(app)
        drawComputerBorder(app)
        drawKeyboard(app)
        drawKeyboardBorder(app)
        # drawInputBoard(app)
        drawRect(10, 10, 100, 50, fill = 'lightGray')
        drawRect(10, 10, 100, 50, fill = None, border = app.backFill, borderWidth = 4)
        drawLabel('Home', 60, 35, size = 30, font = 'Noto Sans', fill = 'white')
    # SINGLE
    if app.over and app.mode == 'Single':
            if app.win == True:
                drawLabel('You Win!', 500, 35, align = 'center', size = 40, fill = 'white')
            else:
                drawLabel(f'You Lose, the word was {app.targetWord}', 500, 35, align = 'center', size = 40, fill = 'white')
            drawSinglePlayerBoard(app)
            drawSinglePlayerBorder(app)
            drawKeyboard(app)
            drawKeyboardBorder(app)
            # drawInputBoard(app)
            drawRect(10, 10, 100, 50, fill = 'lightGray')
            drawRect(10, 10, 100, 50, fill = None, border = app.backFill, borderWidth = 4)
            drawLabel('Home', 60, 35, size = 30, font = 'Noto Sans', fill = 'white')
        
def drawInputBoard(app):
    drawRect(app.inputBoardLeft, app.inputBoardTop, app.inputBoardWidth, app.inputBoardHeight, 
                fill = None, borderWidth = app.inputBorderWidth, border = 'black')

# DRAW 2D BOARD FOR TRADITIONAL WORDLE
def drawSinglePlayerBoard(app):
    for row in range(6):
        for col in range(app.cols):
            drawSinglePlayerCell(app, row, col)
            
def drawSinglePlayerCell(app, row, col):
    color = app.cellColors[row][col]
    letter = app.keys[row][col]
    left, top = getSinglePlayerLeftTop(app, row, col)
    width, height = getSinglePlayerSize(app)
    # RGB VALUE FOR GRAY FOUND ONLINE
    drawRect(left, top, width, height, fill = color, border = rgb(120, 124, 126), borderWidth = app.playerBorderWidth) 
    drawLabel(letter, left + width / 2, top + height / 2, align = 'center', size = 30, font = 'Noto Sans', fill = 'white')

def getSinglePlayerSize(app):
    width = app.singlePlayerBoardWidth / app.cols
    height = app.singlePlayerBoardHeight / 6
    return (width, height)

def getSinglePlayerLeftTop(app, row, col):
    width , height = getSinglePlayerSize(app)
    left = app.singlePlayerBoardLeft + col * width
    top = app.singlePlayerBoardTop + row * height
    return (left, top)

def drawSinglePlayerBorder(app): # RGB VALUE FOR GRAY FOUND ONLINE
    drawRect(app.singlePlayerBoardLeft, app.singlePlayerBoardTop, app.singlePlayerBoardWidth, 
            app.singlePlayerBoardHeight, fill = None, border = rgb(120, 124, 126), borderWidth = 2 * app.singlePlayerBorderWidth)

# DRAW MULTIPLAYER PLAYER BOARD
def drawPlayerBoard(app):
    for row in range(app.shift, app.shift + 6):
        for col in range(app.cols):
            drawPlayerCell(app, row, col)
            
def drawPlayerCell(app, row, col): # rgb found online
    color = app.cellColors[row][col]
    letter = app.keys[row][col]
    left, top = getPlayerLeftTop(app, row, col)
    width, height = getPlayerSize(app)
    drawRect(left, top, width, height, fill = color, border = rgb(120, 124, 126), borderWidth = app.playerBorderWidth)
    if app.level != None:
        drawLabel(letter, left + width / 2, top + height / 2, align = 'center', size = 30, fill = 'white')

def getPlayerSize(app):
    width = app.playerBoardWidth / app.cols
    height = app.playerBoardHeight / 6
    return (width, height)

def getPlayerLeftTop(app, row, col):
    width , height = getPlayerSize(app)
    visibleRow = row - app.shift
    left = app.playerBoardLeft + col * width
    top = app.playerBoardTop + visibleRow * height
    return (left, top)

    
def drawPlayerBorder(app): #rgb found online 
    drawRect(app.playerBoardLeft, app.playerBoardTop, app.playerBoardWidth, app.playerBoardHeight, 
                fill = None, border = rgb(120, 124, 126), borderWidth = 2 * app.playerBorderWidth)

# DRAW MULTIPLAYER COMPUTER BOARD
def drawComputerBoard(app):
    for row in range(app.shift, app.shift + 6):
        for col in range(app.cols):
            drawComputerCell(app, row, col)
            
def drawComputerCell(app, row, col): # rgb colors found online
    color = app.computerCellColors[row][col]
    left, top = getComputerLeftTop(app, row, col)
    width, height = getComputerSize(app)
    if row < len(app.computerGuesses):
        word = app.computerGuesses[row]
        letter = word[col]
        if app.level == 'Impossible':
            if word != app.targetWord:
                color = 'gray'
            else:
                color = rgb(106,170,100) 
        drawRect(left, top, width, height, fill = color, border = rgb(120, 124, 126), 
                    borderWidth = app.computerBorderWidth) 
        drawLabel(letter, left + width / 2, top + height / 2, align = 'center',
                    size = 30, font = 'Neue Helvetica', fill = 'white')
    else:
        drawRect(left, top, width, height, fill = None, border = rgb(120, 124, 126), 
                borderWidth = app.computerBorderWidth)
    
def getComputerSize(app):
    width = app.computerBoardWidth / app.cols
    height = app.computerBoardHeight / app.screenRows
    return (width, height)

def getComputerLeftTop(app, row, col):
    width , height = getComputerSize(app)
    visibleRow = row - app.shift
    left = app.computerBoardLeft + col * width
    top = app.computerBoardTop + visibleRow * height
    return (left, top)
    
def drawComputerBorder(app): # rgb found online
    drawRect(app.computerBoardLeft, app.computerBoardTop, app.computerBoardWidth, app.computerBoardHeight, 
                fill = None, border = rgb(120, 124, 126), borderWidth = 2 * app.computerBorderWidth)

# DRAW KEYBOARD
def drawKeyboard(app):
    for row in range(len(app.keyboard)):
        for col in range(len(app.keyboard[row])):
            drawKey(app, row, col)

def drawKey(app, row, col):
    letter = app.keyboard[row][col]
    color = app.keyColors.get(letter, rgb(120, 124, 126)) # COLOR FOUND ONLINE
    left, top = getKeyLeftTop(app, row, col)
    width, height = getKeySize(app)
    drawRect(left, top, width, height, fill = color, border = 'black', borderWidth = app.keyBorderWidth)
    drawLabel(letter, left + width / 2, top + height / 2, align = 'center', font = 'Noto Sans', 
                fill = 'white', bold = True, size = 20)

def getKeyLeftTop(app, row, col):
    width , height = getKeySize(app)
    left = app.keyBoardLeft + col * width
    top = app.keyBoardTop + row * height
    return (left, top)

def getKeySize(app):
    return app.keyWidth, app.keyHeight

def drawKeyboardBorder(app):
    width = len(app.keyboard[0]) * app.keyWidth
    height = 3 * app.keyHeight
    drawRect(app.keyBoardLeft, app.keyBoardTop, width, height, fill = None, border = 'black', borderWidth = 2 * app.keyBorderWidth)

def onKeyPress(app, key):
    # BACKSPACE
    if app.paused == True:
        if key == 'backspace' and app.currentCol > 0:
            app.currentCol -= 1
            app.keys[app.currentRow][app.currentCol] = ''
        # LETTERS
        elif key.isalpha() and len(key) == 1 and app.currentCol < app.cols:
            if app.mode == 'Computer' and app.level != None: 
                app.timerPaused = False
                app.keys[app.currentRow][app.currentCol] = key.upper()
                app.currentCol += 1
            elif app.mode == 'Single': 
                app.keys[app.currentRow][app.currentCol] = key.upper()
                app.currentCol += 1
        # ENTER
        elif key == 'enter' and app.currentCol == app.cols:
            guess = getGuess(app)
            app.playerGuesses.append(guess)
            checkWord(app)
            if guess == app.targetWord:
                app.win = True
                app.over = True
            elif app.currentRow >= 5 and app.mode == 'Single':
                app.win = False
                app.over = True
            if not app.over:
                if guess in app.wordlist:
                    # MOVE TO THE NEXT ROW
                    if app.currentRow < app.rows - 1:
                        app.currentRow += 1
                        app.currentCol = 0
                        # BOARD IS FILLED SHIFT EVERYTHING UP
                        if app.currentRow >= app.shift + 6:
                            app.shift += 1
                    # else:
                    #     app.over = True
                    # MAKE COMPUTER GUESS THEN RESET TIMER AND START IT AGAIN
                    if app.mode == 'Computer':
                        app.paused = not app.paused
                        makeGuess(app)
                        checkComputerWord(app)
                    app.time = 30 
                # WORD NOT IN WORDLIST
                else:
                    app.invalid = True
        # SCROLLING
        elif key == 'up':
            if app.shift > 0:
                app.shift -= 1
        elif key == 'down':
            app.shift += 1

def onMousePress(app, mouseX, mouseY):
    x,y = mouseX, mouseY
    # SELECT MODE
    if app.mode == None:
        if x <= 600 and x >= 400 and y <= 300 and y >= 200:
            app.mode = 'Single'
        elif x <= 600 and x >= 400 and y <= 450 and y >= 350:
            app.mode = 'Computer'
        elif x <= 600 and x >= 400 and y <= 600 and y >= 500:
            app.mode = 'Instructions'

    else:
        # BACK
        if x <= 110 and x >= 10 and y <= 60 and y >= 10:
            onAppStart(app)
        # HINTS
        if (app.level != None or app.mode == 'Single') and app.level != 'Impossible':
            if x <= 975 and x >= 875 and y <= 80 and y >= 30 and app.over == False:
                makeHint(app)
            elif x <= 975 and x >= 875 and y <= 140 and y >= 90 and app.over == False:
                makeAdvancedHint(app)
                
        # PAUSE
        if app.level != None and app.level != 'Impossible' and app.mode == 'Computer':
            if x <= 975 and x >= 875 and y <= 200 and y >= 150:
                app.timerPaused = not app.timerPaused
        # X OUT OF INVALID WORD MESSAGE
        if app.invalid == True:
            if x <= 600 and x >= 580 and y <= 220 and y >= 200:
                app.invalid = not app.invalid

        # LEVEL
        elif app.mode == 'Computer' and app.level == None:
            if x <= 600 and x >= 400 and y <= 300 and y >= 200:
                app.level = 'Easy'
            elif x <= 600 and x >= 400 and y <= 450 and y >= 350:
                app.level = 'Medium'
            elif x <= 600 and x >= 400 and y <= 600 and y >= 500:
                app.level = 'Hard'
            elif x <= 600 and x >= 400 and y <= 750 and y >= 650:
                app.level = 'Impossible'

def onMouseMove(app, mouseX, mouseY):
    x,y = mouseX, mouseY
    if app.mode == None:
        # MODE
        if x <= 600 and x >= 400 and y <= 300 and y >= 200:
            app.traditionalFill = 'white'
        else:
            app.traditionalFill = 'gray'
        if x <= 600 and x >= 400 and y <= 450 and y >= 350:
            app.computerFill = 'white'
        else:
            app.computerFill = 'gray'
        if x <= 600 and x >= 400 and y <= 600 and y >= 500:
            app.instructionsFill = 'white'
        else:
            app.instructionsFill = 'gray'

    else:
        # BACK
        if x <= 110 and x >= 10 and y <= 60 and y >= 10:
            app.backFill = 'white'
        else:
            app.backFill = 'gray'

        # HINTS
        if (app.level != None or app.mode == 'Single') and app.level != 'Impossible':
            if x <= 975 and x >= 875 and y <= 80 and y >= 30 and app.over == False:
                app.hintFill = 'white'
            else:
                app.hintFill = 'gray'
            if x <= 975 and x >= 875 and y <= 140 and y >= 90 and app.over == False:
                app.advancedHintFill = 'white'
            else:
                app.advancedHintFill = 'gray'
                
        # PAUSE
        if app.level != None and app.level != 'Impossible' and app.mode == 'Computer':
            if x <= 975 and x >= 875 and y <= 200 and y >= 150:
                app.pauseFill = 'white'
            else:
                app.pauseFill = 'gray'

        # LEVEL
        if app.mode == 'Computer':
                if x <= 600 and x >= 400 and y <= 300 and y >= 200:
                    app.easyLevelFill = 'white'
                else:
                    app.easyLevelFill = 'gray'
                if x <= 600 and x >= 400 and y <= 450 and y >= 350:
                    app.mediumLevelFill = 'white'
                else:
                    app.mediumLevelFill = 'gray'
                if x <= 600 and x >= 400 and y <= 600 and y >= 500:
                    app.hardLevelFill = 'white'
                else:
                    app.hardLevelFill = 'gray'
                if x <= 600 and x >= 400 and y <= 750 and y >= 650:
                    app.impossibleLevelFill = 'white'
                else:
                    app.impossibleLevelFill = 'gray'

def makeHint(app):
    index = random.randint(0, len(app.hints) - 1)
    app.hint = app.hints[index].upper()
    app.keys[app.currentRow] = list(app.hint)
    app.playerGuesses.append(app.hint)
    checkWord(app)
    app.currentRow += 1
    app.currentCol = 0

    if app.hint == app.targetWord:
        app.win = True
        app.over = True
    if app.mode == 'Single':
        if app.currentRow > 5 and app.hint != app.targetWord:  
            app.win = False
            app.over = True
    else:
        if app.currentRow >= app.shift + 6:
            app.shift += 1

    app.time = 30

def makeAdvancedHint(app):
    if app.playerGuesses == []:
        index = random.randint(0, len(app.playerPossibleWords) - 1)
        tempGuess = app.playerPossibleWords[index]
        app.playerGuesses.append(tempGuess)
    currGuess = app.playerGuesses[-1]
    app.playerPossibleWords = hintSort(app, currGuess)
    app.playerPossibleWords = list(set(app.playerPossibleWords) - set(app.playerGuesses))

    index = random.randint(0, len(app.playerPossibleWords) - 1)
    app.advancedHint = app.playerPossibleWords[index]
    app.playerGuesses.append(app.advancedHint)

    app.keys[app.currentRow] = list(app.advancedHint)
    checkWord(app)
    app.playerGuesses.append(app.advancedHint)
    app.currentRow += 1
    app.currentCol = 0
    if len(app.playerGuesses) > app.rows:
        app.currentRow = 1

    if app.advancedHint == app.targetWord:
        app.win = True
        app.over = True

    if app.mode == 'Single':
        if app.currentRow > 5 and app.advancedHint != app.targetWord:  
            app.win = False
            app.over = True

    else:
        if app.currentRow >= app.shift + 6:
            app.shift += 1

    app.time = 30

# COPIED FORMAT FROM MEDIUM SORT ALORITHM BELOW - MEDIUM SORT REFERENCED CHAT GPT (SEE BELOW)
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
def hintSort(app, guess):
    newPossibleWords = []
    targetWord = list(app.targetWord)
    for word in app.playerPossibleWords:
        add = True  
        for i in range(5): 
            letter = guess[i]
            if not isValid(letter, targetWord, i, word): 
                add = False
                break  
        if add:
            newPossibleWords.append(word)
    return newPossibleWords
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

def getWord(app):
    index = random.randint(0, (app.lengthOfWords) - 1)
    return app.words[index]

# COLOR WORD ON PLAYER BOARD AND KEYBOARD
def checkWord(app):
    guess = getGuess(app)
    if guess in app.wordlist:
        targetWord = list(app.targetWord)
        for i in range(len(app.targetWord)):
            if guess[i] == targetWord[i]:
                makeGreen(app, i)
                makeKeyboardGreen(app, guess[i])
            elif guess[i] in targetWord:
                makeYellow(app, i)
                makeKeyboardYellow(app, guess[i])
            else:
                makeGray(app, i)
                makeKeyboardGray(app, guess[i])
# COLOR WORD ON COMPUTER BOARD AND KEYBOARD
def checkComputerWord(app):
    guess = app.computerGuess
    targetWord = list(app.targetWord)
    for i in range(len(app.targetWord)):
        if guess[i] == targetWord[i]:
            makeComputerGreen(app, i)
        elif guess[i] in targetWord:
            makeComputerYellow(app, i)
        else:
            makeComputerGray(app, i)

# TURN LETTERS IN BOARD ROW INTO A WORD
def getGuess(app):
    return ''.join(app.keys[app.currentRow])

# MAKE BOARD COLORED
# COLORS FOUND RGB VALUES ONLINE
def makeGreen(app, i):
    row, col = app.currentRow, i
    app.cellColors[row][col] = rgb(106,170,100)

def makeComputerGreen(app, i):
    row, col = app.computerCurrentRow - 1, i
    app.computerCellColors[row][col] = rgb(106,170,100)

def makeYellow(app, i):
    row, col = app.currentRow, i
    app.cellColors[row][col] = rgb(201, 180, 88)

def makeComputerYellow(app, i):
    row, col = app.computerCurrentRow - 1, i
    app.computerCellColors[row][col] = rgb(201, 180, 88)

def makeGray(app, i):
    row, col = app.currentRow, i
    app.cellColors[row][col] = rgb(58,58,60)

def makeComputerGray(app, i):
    row, col = app.computerCurrentRow - 1, i
    app.computerCellColors[row][col] = rgb(58,58,60)

def makeKeyboardGreen(app, char):
    app.keyColors[char] = rgb(106,170,100)

def makeKeyboardYellow(app, char):
    app.keyColors[char] = rgb(201, 180, 88)

def makeKeyboardGray(app, char):
    app.keyColors[char] = rgb(58,58,60)

# COMPUTER GUESSING
def makeGuess(app):
    if app.paused == False and not app.over and app.mode == 'Computer':
        # EASY
        if app.level == 'Easy':
            app.computerGuess = makeEasyGuess(app)
            app.computerGuesses.append(app.computerGuess)
            app.computerCurrentRow += 1
            if app.computerGuess == app.targetWord:
                app.win = False
                app.over = True
            else:
                if len(app.computerGuesses) > app.rows:
                    # app.computerGuesses = []
                    app.computerCurrentRow = 1
        # MEDIUM
        if app.level == 'Medium':
            makeMediumGuess(app)

        # HARD
        if app.level == 'Hard':
            makeHardGuess(app)

        # IMPOSSIBLE
        if app.level == 'Impossible':
            makeHardGuess(app)

        app.paused = not app.paused
# EASY
def makeEasyGuess(app):
    unseen = list(set(app.words).difference(set(app.computerGuesses)))
    index = random.randint(0, len(unseen) - 1)
    return unseen[index]

# MEDIUM
def makeMediumGuess(app):
    if app.computerGuess == None:
        app.possibleWords = copy.copy(app.words)
    else:
        currGuess = app.computerGuesses[-1]
        app.possibleWords = mediumSort(app, currGuess)
        app.possibleWords = list(set(app.possibleWords) - set(app.computerGuesses))

    index = random.randint(0, len(app.possibleWords) - 1)
    app.computerGuess = app.possibleWords[index]
    app.computerGuesses.append(app.computerGuess)
    app.computerCurrentRow += 1

    if app.computerGuess == app.targetWord:
        app.win = False
        app.over = True

    else:
        if len(app.computerGuesses) > app.rows:
            app.computerGuesses = []
            app.computerCurrentRow = 1
# REFERENCED FORMAT AND STRUCTURE FROM CHAT GPT CODE BELOW, CODED ALGORITHM MYSELF 
# REFERENCED SETTING A VARIABLE TO TRUE INITIALLY AND CHECKING ALL CONDITIONS AND ADDING AT END IF VALID, 
# AND MAKING TEMPORARY LIST
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
def mediumSort(app, guess):
    newPossibleWords = []
    targetWord = list(app.targetWord)

    for word in app.possibleWords:
        add = True  
        for i in range(5): 
            letter = guess[i]
            if not isValid(letter, targetWord, i, word): 
                add = False
                break  
        if add:
            newPossibleWords.append(word)

    return newPossibleWords
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# CHECK EACH LETTER FOR CONSISTENCY
def isValid(letter, targetWord, i, word):
    if letter == targetWord[i]:  
        if word[i] == letter:
            return True
        return False
    elif letter in targetWord:  
        if letter in word and word[i] != letter:
            return True
        return False
    else:  
        if letter not in word:
            return True
        return False
    
# HARD
def makeHardGuess(app):
    if app.computerGuess == None:
        app.hardPossibleWords = copy.copy(app.words)
    else:
        # TAKE INTO ACCOUNT PLAYER GUESSES AS WELL
        currGuess = app.computerGuesses[-1]
        currPlayerGuess = app.playerGuesses[-1]
        app.hardPossibleWords = hardSort(app, currGuess)
        app.hardPossibleWords = hardSort(app, currPlayerGuess)
        app.hardPossibleWords = list(set(app.hardPossibleWords) - set(app.computerGuesses) - set(app.playerGuesses)) 

    index = random.randint(0, len(app.hardPossibleWords) - 1)
    app.computerGuess = app.hardPossibleWords[index]
    app.computerGuesses.append(app.computerGuess)
    app.computerCurrentRow += 1

    if app.computerGuess == app.targetWord:
        app.win = False
        app.over = True

    else:
        if len(app.computerGuesses) > app.rows:
            app.computerGuesses = []
            app.computerCurrentRow = 1

# COPIED FORMAT FROM MY MEDIUM SORT ALORITHM ABOVE - MEDIUM SORT REFERENCED CHAT GPT (SEE ABOVE)
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

def hardSort(app, guess):
    newPossibleWords = []
    targetWord = list(app.targetWord)

    for word in app.hardPossibleWords:
        add = True  
        for i in range(5): 
            letter = guess[i]
            if not isValid(letter, targetWord, i, word): 
                add = False
                break  
        if add:
            newPossibleWords.append(word)

    return newPossibleWords

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

def onStep(app):
    app.counter += 1
    if app.paused == True and app.level != None and app.over == False and app.timerPaused == False:
        app.time -= 1
    if app.time == 0:
        app.win = False
        app.over = True

def main():
    runApp(app.width, app.height)

main() 