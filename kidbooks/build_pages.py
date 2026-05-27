#!/usr/bin/env python3
"""
Build the complete PAGES list for generate_book.py.
Combines existing sections with new sections, ordered easiest -> most amazing.
Outputs the Python code to paste into generate_book.py.
"""

# Import the new sections
from new_sections import NEW_SECTIONS, PROMPT_PREFIX

# ── Existing sections (from current generate_book.py) ──
# We redefine them here with the updated PROMPT_PREFIX (no camera looking)

EXISTING = {

"train": [
{
    "id": "train_01_help",
    "type": "story",
    "text": [
        "At the old train yard, two elephants",
        "and two horses looked very sad.",
        "",
        "Their wooden bridge had broken!",
        "They could not cross the river.",
        "",
        '"We can fix that!" said Neo.',
        "The family grabbed their tools and got to work.",
        "In no time, the bridge was good as new!",
    ],
    "prompt": PROMPT_PREFIX + (
        "An old train yard by a river. The family in railroad engineer outfits "
        "(Mama: denim overalls with red bandana, Dada: engineer outfit with striped cap, "
        "one boy: green striped overalls and green cap with letter N, "
        "other boy: blue striped overalls and blue cap with letter E) "
        "works together to fix a broken wooden bridge. Dada hammers a plank looking down at the nail. "
        "Mama holds a board in place focused on alignment. The boys hand nails to their parents. "
        "Two sad elephants and two horses wait on the other side of the river, watching hopefully. "
        "The puppy carries a small plank. Water tower and green hills in background. Warm sunshine."
    ),
},
{
    "id": "train_02_build",
    "type": "story",
    "text": [
        '"Thank you!" trumpeted the elephants.',
        '"How can we repay you?"',
        "",
        '"Help us build a TRAIN!" said Ender.',
        "",
        "Mama drew the plans. Dada hammered the wheels.",
        "Neo painted the engine bright green.",
        "Ender painted the caboose brilliant blue.",
        "The elephants carried the heavy parts!",
    ],
    "prompt": PROMPT_PREFIX + (
        "At the train yard, the family builds a big colorful steam train. "
        "Same railroad outfits (boy in green with N, boy in blue with E). "
        "Mama kneels studying a blueprint, focused on the drawing. Dada hammers a large iron wheel looking at it. "
        "The boy in green paints the engine green with a big brush. "
        "The boy in blue paints the caboose blue. "
        "An elephant carries a metal beam with its trunk. "
        "A horse pulls a rail into position with a rope. "
        "The puppy trots by with a nail in his mouth. "
        "The half-built train is bright and colorful. Warm busy scene."
    ),
},
{
    "id": "train_03_use",
    "type": "story",
    "text": [
        "CHOO CHOO! The train rolled down the tracks!",
        "",
        "Mama drove while Dada rang the bell.",
        "Neo and Ender waved from the windows.",
        "Wall-E barked with joy!",
        "",
        "All the animals rode along -- what a trip!",
    ],
    "prompt": PROMPT_PREFIX + (
        "A bright colorful steam train chugs through beautiful countryside. "
        "Mama drives from the engine cab looking at the tracks ahead. Dada rings a big brass bell. "
        "The two boys wave excitedly from open windows (green with N, blue with E). "
        "The puppy has his head out a window, ears flapping. "
        "An elephant rides happily in an open car behind. Horses trot alongside. "
        "The train puffs white steam. Green rolling hills, wildflowers, "
        "a river with ducks, a red barn in the distance. Blue sky, sunshine."
    ),
},
],

"rocket": [
{
    "id": "rocket_01_help",
    "type": "story",
    "text": [
        "At the hilltop observatory, two owls",
        "and an eagle were in trouble.",
        "",
        "A big storm had knocked their nest",
        "right out of the tallest tree!",
        "",
        '"Don\'t worry!" said Mama.',
        "The family climbed up and built",
        "the coziest new nest ever.",
    ],
    "prompt": PROMPT_PREFIX + (
        "A hilltop observatory at golden hour. The family in space suits "
        "(one boy: green suit with letter N, other boy: blue suit with letter E, "
        "Mama: white suit hair visible, Dada: white suit orange stripe) "
        "climbs a tall tree to rebuild a fallen nest. Dada is up on a branch "
        "securing sticks looking at the nest. Mama passes up soft moss. The boys hand up twigs from below. "
        "Two worried owls and an eagle watch from nearby branches. "
        "The puppy looks up from the base of the tree. "
        "A fallen nest on the ground. Starry twilight sky, telescope visible."
    ),
},
{
    "id": "rocket_02_build",
    "type": "story",
    "text": [
        '"Hoo-hoo! Thank you!" said the owls.',
        '"We will help you with anything!"',
        "",
        '"Help us build a ROCKET!" said Neo.',
        "",
        "The eagles carried pieces way up high!",
        "The owls read the blueprints with wise eyes.",
        "Neo tightened bolts. Ender attached the fins.",
    ],
    "prompt": PROMPT_PREFIX + (
        "Nighttime rocket-building scene. The family in space suits "
        "(boy in green with N, boy in blue with E) builds a tall silver rocket "
        "on a launch pad under the stars. An eagle carries a metal panel up high. "
        "An owl studies blueprints wearing tiny glasses. "
        "Mama welds a seam with sparks, focused on the joint. Dada bolts on a panel. "
        "The boy in green cranks a bolt with a wrench. "
        "The boy in blue attaches a silver fin. "
        "The puppy carries a wrench in his mouth. "
        "Scaffolding, moon and stars above. Exciting atmosphere."
    ),
},
{
    "id": "rocket_03_use",
    "type": "story",
    "text": [
        "5... 4... 3... 2... 1... BLAST OFF!",
        "",
        "The rocket zoomed past the moon and stars!",
        "",
        '"I can see the whole world!" cheered Ender.',
        '"Me too!" laughed Neo.',
        "",
        "Wall-E floated in zero gravity!",
    ],
    "prompt": PROMPT_PREFIX + (
        "A silver rocket soars through space. Through big round windows: "
        "the family in space suits, the boys pressing faces to the glass in wonder "
        "(green suit with N, blue suit with E). "
        "The puppy floats in zero gravity looking surprised and happy. "
        "Outside: bright blue Earth below, cratered moon nearby, "
        "Saturn with rings, a colorful nebula, a comet with glowing tail. "
        "Rocket trail of fire. Beautiful and awe-inspiring."
    ),
},
],

"airplane": [
{
    "id": "airplane_01_help",
    "type": "story",
    "text": [
        "At the sunny beach, pelicans and parrots",
        "were very upset.",
        "",
        "A big tangle of old fishing nets",
        "was wrapped around the pelicans' beaks!",
        "",
        '"Hold still," said Dada gently.',
        "The family carefully cut and untangled",
        "every last knot. The pelicans were free!",
    ],
    "prompt": PROMPT_PREFIX + (
        "A tropical beach on a sunny day. The family in aviator outfits "
        "(one boy: green aviator jacket with letter N and goggles, "
        "other boy: blue aviator jacket with letter E and goggles, "
        "Mama: brown leather jacket white scarf, Dada: bomber jacket) "
        "carefully untangles old fishing nets from two pelicans' beaks. "
        "Dada gently cuts a net with scissors looking at the knot. Mama holds a pelican still. "
        "The boys carefully pull net strands free. "
        "Three colorful parrots watch from a driftwood log. "
        "The puppy tugs on a loose net piece. "
        "Palm trees, blue ocean, warm bright light."
    ),
},
{
    "id": "airplane_02_build",
    "type": "story",
    "text": [
        '"SQUAWK! Thank you!" cried the pelicans.',
        '"We owe you one!"',
        "",
        '"Help us build an AIRPLANE!" said Mama.',
        "",
        "The pelicans shaped the big wide wings.",
        "Parrots painted it every color of the rainbow!",
        "Dada built the propeller.",
        "Neo and Ender glued on the windows.",
    ],
    "prompt": PROMPT_PREFIX + (
        "On the beach, the family builds a colorful biplane. Same aviator outfits "
        "(boy in green with N, boy in blue with E). "
        "Pelicans hold up a wing section with their beaks. "
        "Parrots paint rainbow stripes with brushes in their claws. "
        "Dada attaches a propeller, focused on the bolts. Mama rivets the fuselage. "
        "The two boys glue windows onto the side together. "
        "The puppy has paint splotches on his curly fur. "
        "Half-built rainbow airplane. Ocean and palm trees behind."
    ),
},
{
    "id": "airplane_03_use",
    "type": "story",
    "text": [
        "ZOOM! The rainbow airplane soared",
        "over the sparkling ocean!",
        "",
        "They flew past dolphins jumping",
        "and whales splashing far below.",
        "",
        "Wall-E stuck his head out,",
        "his curly ears flapping in the wind!",
    ],
    "prompt": PROMPT_PREFIX + (
        "A rainbow-painted biplane soars over a sparkling turquoise ocean. "
        "Mama pilots looking at the instruments, Dada co-pilots checking the map. "
        "The two boys sit in the back waving out the sides "
        "(green outfit N, blue outfit E). "
        "The puppy has his head over the side with ears flapping. "
        "Below: two dolphins leaping, a whale tail splashing. "
        "Parrots and a pelican fly alongside. "
        "Tropical island with palm trees in the distance. "
        "Blue sky, white clouds, golden sunshine. Joyful."
    ),
},
],

"helicopter": [
{
    "id": "heli_01_help",
    "type": "story",
    "text": [
        "In a beautiful garden, the hummingbirds",
        "and dragonflies were worried.",
        "",
        "The old stone fountain had cracked",
        "and all the water leaked out!",
        "The flowers were getting thirsty.",
        "",
        '"We know how to fix that!" said Ender.',
        "The family patched the fountain",
        "and the water flowed again!",
    ],
    "prompt": PROMPT_PREFIX + (
        "A beautiful flower garden. The family in explorer/flight outfits "
        "(one boy: green flight jumpsuit with letter N, "
        "other boy: blue flight jumpsuit with letter E, "
        "Mama: khaki explorer outfit with pith helmet, "
        "Dada: pilot jumpsuit with aviator sunglasses) "
        "repairs a cracked stone fountain. Dada applies mortar to a crack, focused on the repair. "
        "Mama holds the pieces together. The boys pour water from a bucket to test it. "
        "Hummingbirds hover nearby watching. Dragonflies zip around. "
        "Wilting flowers nearby, healthy flowers on the other side. "
        "The puppy drinks from a puddle. Dappled sunlight, garden path."
    ),
},
{
    "id": "heli_02_build",
    "type": "story",
    "text": [
        "The hummingbirds buzzed with happiness!",
        '"Our garden is saved! How can we help?"',
        "",
        '"Teach us to build a HELICOPTER!" said Neo.',
        "",
        "Hummingbirds showed how spinning blades work!",
        "Dragonflies helped attach the tail rotor.",
        "Mama welded the frame.",
        "Neo and Ender turned the big wrench together!",
    ],
    "prompt": PROMPT_PREFIX + (
        "In the garden, the family builds a red and yellow helicopter. "
        "Same flight outfits (boy in green with N, boy in blue with E). "
        "Hummingbirds hover next to the rotor blade demonstrating spin. "
        "A dragonfly carries a tiny bolt. "
        "Mama welds the frame with small sparks, focused on the joint. Dada bolts seats inside. "
        "The two boys grip a big wrench TOGETHER, turning a bolt as a team. "
        "The puppy sits in the pilot seat with paws on the controls. "
        "Half-built helicopter among the flowers. Cheerful scene."
    ),
},
{
    "id": "heli_03_use",
    "type": "story",
    "text": [
        "WHIRR WHIRR! The helicopter lifted",
        "straight up into the sky!",
        "",
        "They flew over a lush green jungle",
        "full of amazing animals.",
        "",
        '"Look at all the animals!" pointed Neo.',
        '"I see monkeys AND toucans!" said Ender.',
    ],
    "prompt": PROMPT_PREFIX + (
        "A red and yellow helicopter flies over a lush tropical jungle canopy. "
        "Through the glass: the family inside, the two boys pointing excitedly "
        "out the windows (green with N, blue with E), "
        "the puppy pressing his nose to the glass. "
        "Below: monkeys swinging on vines, a toucan with a rainbow beak, "
        "a sloth hanging from a branch. A waterfall into a pool. "
        "Hummingbirds fly alongside. Green, misty, beautiful."
    ),
},
],

"castle": [
{
    "id": "castle_01_help",
    "type": "story",
    "text": [
        "Deep in the forest, beavers and rabbits",
        "were splashing around in a panic.",
        "",
        "Their big dam had sprung a leak!",
        "Water was flooding their homes!",
        "",
        '"Quick, grab the logs!" said Dada.',
        "The family plugged the leak and packed it",
        "tight with mud. The homes were safe!",
    ],
    "prompt": PROMPT_PREFIX + (
        "A forest stream with a beaver dam. The family in medieval outfits "
        "(one boy: green knight tunic with letter N and small shield, "
        "other boy: blue knight tunic with letter E and small shield, "
        "Mama: medieval dress with flower crown, "
        "Dada: knight armor visor up showing beard) "
        "rushes to fix a leaking beaver dam. Dada pushes a big log into a gap, focused on it. "
        "Mama packs mud against the dam. The boys carry armfuls of sticks. "
        "Two beavers and three rabbits watch anxiously. "
        "Water sprays through the crack. The puppy stands in the shallow water. "
        "Mossy forest, ferns, dappled light."
    ),
},
{
    "id": "castle_02_build",
    "type": "story",
    "text": [
        "The beavers slapped their tails with joy!",
        '"You saved our homes! We will help YOU now!"',
        "",
        '"Help us build a CASTLE!" said Ender.',
        "",
        "The beavers cut perfect logs -- CHOMP CHOMP!",
        "Rabbits dug the moat all around.",
        "Neo stacked stones for the tower.",
        "Ender raised the drawbridge.",
    ],
    "prompt": PROMPT_PREFIX + (
        "In a forest clearing, the family builds a stone castle. "
        "Same medieval outfits (boy in green tunic with N, boy in blue with E). "
        "Beavers gnaw logs straight. Rabbits dig a moat, dirt flying. "
        "Mama mixes mortar, focused on the bucket. Dada lays stone blocks looking at the wall. "
        "The boy in green stacks stones on a tower. "
        "The boy in blue pulls a chain to raise a drawbridge. "
        "The puppy wears a tiny tin helmet. "
        "Half-built castle with walls, a round tower, battlements. Active scene."
    ),
},
{
    "id": "castle_03_use",
    "type": "story",
    "text": [
        "The castle was magnificent!",
        "Tall towers, colorful flags, and a real moat!",
        "",
        "They held a grand royal feast",
        "with ALL the animal friends!",
        "",
        "King Neo and King Ender wore golden crowns.",
        "Wall-E wore a tiny crown too!",
    ],
    "prompt": PROMPT_PREFIX + (
        "A magnificent stone castle with tall towers and colorful pennant flags. "
        "In the courtyard, the family sits at a long feast table. "
        "The two boys wear golden crowns on kid-sized thrones "
        "(green tunic with N, blue tunic with E). "
        "Mama wears a tiara, looking at Dada. Dada raises a goblet toward the crowd. "
        "The puppy wears a tiny crown on a cushion. "
        "Beavers and rabbits at the table. Cake, fruit, pies on the table. "
        "A banner reads HOORAY. Evening sky, torchlight, fairy lights."
    ),
},
],

"dump": [
{
    "id": "dump_01_help",
    "type": "story",
    "text": [
        "At the construction site, a little bear cub",
        "was stuck high up in a tree!",
        "",
        "The big bears paced below, worried.",
        "The raccoons tried to climb up but slipped.",
        "",
        '"I have an idea!" said Neo.',
        "The family stacked crates into steps",
        "and the cub climbed right down!",
    ],
    "prompt": PROMPT_PREFIX + (
        "A construction site near some trees. The family in construction outfits "
        "(one boy: green safety vest and green hard hat with letter N, "
        "other boy: blue safety vest and blue hard hat with letter E, "
        "Mama: yellow hard hat and work gloves, Dada: orange vest white hard hat) "
        "stacks wooden crates into makeshift stairs next to a tree. "
        "A small bear cub clings to a high branch looking scared. "
        "Two big bears pace below looking worried. Two raccoons watch. "
        "The boy in green directs where to put crates, pointing up. Mama steadies them. "
        "The puppy wears a tiny hard hat looking up. Sunny day, green grass."
    ),
},
{
    "id": "dump_02_build",
    "type": "story",
    "text": [
        "The mama bear gave everyone a big bear hug!",
        '"You saved my baby! We are SO grateful!"',
        "",
        '"Help us build a DUMP TRUCK!" said Mama.',
        "",
        "The bears lifted the ENORMOUS tires!",
        "Raccoons twisted every nut and bolt.",
        "Dada welded the huge dump bed.",
        "Neo and Ender painted it bright yellow!",
    ],
    "prompt": PROMPT_PREFIX + (
        "At the construction site, the family builds a massive yellow dump truck. "
        "Same construction outfits (boy in green vest with N, boy in blue vest with E). "
        "A bear hoists a giant tire onto the axle. "
        "A raccoon uses a tiny wrench on the engine. "
        "Dada welds the dump bed with orange sparks, face shield down. Mama checks the engine, head under the hood. "
        "The two boys paint the side bright yellow with big rollers, side by side. "
        "The puppy plays in a sand pile. "
        "Half-built enormous dump truck. Energetic, action-packed."
    ),
},
{
    "id": "dump_03_use",
    "type": "story",
    "text": [
        "BEEP BEEP BEEP! The dump truck backed up!",
        "",
        "WHOOOOSH! It dumped a mountain of sand!",
        "",
        "They built the biggest sandcastle",
        "the world had ever seen!",
        "Everyone jumped and played in the dirt.",
        "Even Wall-E dug a hole!",
    ],
    "prompt": PROMPT_PREFIX + (
        "A huge bright yellow dump truck tips its bed, dumping golden sand. "
        "The two boys slide down the sand mountain laughing "
        "(green outfit N, blue outfit E). "
        "Mama and Dada build a huge sandcastle together, focused on it. "
        "Bears make sand angels. A raccoon builds a tiny sand tower. "
        "The puppy digs furiously, sand flying behind him. "
        "Buckets, shovels, and sand molds on the ground. "
        "Blue sky, pure joy and laughter."
    ),
},
],

"excavator": [
{
    "id": "excav_01_help",
    "type": "story",
    "text": [
        '"Help! Help!" squeaked tiny voices',
        "from underground.",
        "",
        "The rain had collapsed the moles' tunnels!",
        "Moles and badgers were trapped inside!",
        "",
        '"Hang on!" called Ender.',
        "The family dug and dug with shovels",
        "until every last mole was safe.",
    ],
    "prompt": PROMPT_PREFIX + (
        "A grassy hillside after rain. The family in work gear "
        "(one boy: green coveralls and green hard hat with letter N, "
        "other boy: blue coveralls and blue hard hat with letter E, "
        "Mama: practical work clothes ponytail, Dada: brown coveralls goggles) "
        "digs with shovels to rescue trapped moles. "
        "Dada shovels dirt from a collapsed tunnel entrance, focused on digging. "
        "Mama pulls a mole gently from the mud. "
        "The boys dig with small shovels side by side. "
        "A badger peeks out from a partly cleared tunnel. "
        "The puppy digs with his paws. Muddy scene, puddles, cloudy sky clearing up."
    ),
},
{
    "id": "excav_02_build",
    "type": "story",
    "text": [
        "The moles blinked in the sunlight.",
        '"You saved us! We are the best diggers --',
        'let us help YOU now!"',
        "",
        '"Help us build an EXCAVATOR!" said Dada.',
        "",
        "Badgers welded the long strong arm.",
        'Ender tested the controls -- "It WORKS!"',
        "Neo gave a big thumbs up!",
    ],
    "prompt": PROMPT_PREFIX + (
        "On the hillside, the family builds a big orange excavator. "
        "Same work coveralls (boy in green with N, boy in blue with E). "
        "Moles dig small test holes, poking heads up. "
        "A badger welds the arm wearing a tiny welding mask, sparks flying. "
        "Mama installs a hydraulic cylinder, focused on the fitting. Dada attaches the treads. "
        "The boy in blue sits in the operator seat testing levers with a grin. "
        "The boy in green stands on the ground giving a big thumbs up. "
        "The puppy sits on a dirt pile, hard hat on. Half-built excavator."
    ),
},
{
    "id": "excav_03_use",
    "type": "story",
    "text": [
        "SCOOP! CRASH! The excavator dug up",
        "huge scoops of earth!",
        "",
        "They dug a giant swimming pool",
        "shaped like a STAR!",
        "",
        "All the animals splashed in the cool water.",
        "CANNONBALL!",
    ],
    "prompt": PROMPT_PREFIX + (
        "A big orange excavator beside an enormous star-shaped swimming pool "
        "filled with sparkling blue water. "
        "The two boys do cannonballs into the water -- big splashes "
        "(green shorts with N, blue shorts with E). "
        "Mama floats on a pool float looking at the sky. Dada operates the excavator looking at the bucket. "
        "A bear belly-flops in. Moles peek from the edge. "
        "The puppy shakes water off his fur. "
        "A diving board, beach balls in the water. Dirt piles around. "
        "Sunshine, summer fun."
    ),
},
],

"robot": [
{
    "id": "robot_01_help",
    "type": "story",
    "text": [
        "In the science lab, an octopus",
        "was very worried.",
        "",
        "His big glass tank had a crack",
        "and water was dripping out!",
        "The monkeys tried to plug it with bananas,",
        "but that did not work.",
        "",
        "The family mixed special glue",
        "and sealed the crack perfectly!",
    ],
    "prompt": PROMPT_PREFIX + (
        "A colorful science lab. The family in lab coats "
        "(one boy: green lab coat with letter N and safety goggles, "
        "other boy: blue lab coat with letter E and safety goggles, "
        "Mama: white lab coat hair in bun, Dada: lab coat pocket protector) "
        "repairs a cracked glass tank. Water drips from the crack. "
        "Dada applies special glue to the crack, focused on the repair. Mama holds a clamp. "
        "The boys pass supplies. A worried purple octopus inside the tank. "
        "Two monkeys hold bananas that clearly did not work as plugs. "
        "The puppy sniffs the water on the floor. "
        "Bubbling beakers, computer screens in background."
    ),
},
{
    "id": "robot_02_build",
    "type": "story",
    "text": [
        "The octopus waved all EIGHT arms!",
        '"Thank you! I have eight arms --',
        'I can help build anything!"',
        "",
        '"Help us build a ROBOT!" said Ender.',
        "",
        "The octopus wired circuits with all arms at once!",
        "Monkeys installed the legs, swinging from part to part.",
        "Neo programmed the brain.",
        "Ender designed its friendly face.",
    ],
    "prompt": PROMPT_PREFIX + (
        "In the lab, the family builds a big friendly silver robot on a workbench. "
        "Same lab coats (boy in green with N, boy in blue with E). "
        "A purple octopus solders eight different wires with all arms at once. "
        "A monkey swings from the ceiling installing the robot's arm. "
        "Mama checks the power core, peering into the chest cavity. Dada bolts on the chest plate. "
        "The boy in green types on a tablet with green code on screen. "
        "The boy in blue draws a happy face on the robot's head with a marker. "
        "The puppy wears safety goggles. Circuit boards, LEDs glowing."
    ),
},
{
    "id": "robot_03_use",
    "type": "story",
    "text": [
        "BEEP BOOP! The robot came alive!",
        "Its eyes lit up and it did a silly dance!",
        "",
        "It served cookies to EVERYONE",
        "and gave the BEST high-fives!",
        "",
        '"Best robot EVER!" laughed the whole family.',
        "Wall-E licked the robot's shiny foot!",
    ],
    "prompt": PROMPT_PREFIX + (
        "The lab is now a celebration. A big friendly silver robot with glowing "
        "blue eyes does a silly dance. The robot high-fives the boy in blue (E) "
        "and holds a tray of cookies. The boy in green (N) eats a cookie. "
        "Mama and Dada clap and laugh, looking at the robot. "
        "The octopus waves all arms in celebration. Monkeys dance. "
        "The puppy licks the robot's shiny foot. "
        "Confetti, a banner reading IT WORKS, a disco ball. "
        "LED lights glow rainbow. Pure joy."
    ),
},
],

}

# ── Build order (easiest -> most amazing) ──
SECTION_ORDER = [
    "treehouse",      # 1
    "catapult",        # 2
    "greenhouse",      # 3
    "library",         # 4
    "tractor",         # 5
    "schoolbus",       # 6
    "semi",            # 7
    "dump",            # 8
    "firetruck",       # 9
    "bulldozer",       # 10
    "excavator",       # 11
    "wreckball",       # 12
    "racecar",         # 13
    "monstertruck",    # 14
    "train",           # 15
    "helicopter",      # 16
    "airplane",        # 17
    "jet",             # 18
    "pirateship",      # 19
    "rollercoaster",   # 20
    "palace",          # 21
    "skyscraper",      # 22
    "castle",          # 23
    "rocket",          # 24
    "ufo",             # 25
    "mech",            # 26
    "robot",           # 27
    "spacestation",    # 28
]

# Pretty names for section headers
SECTION_NAMES = {
    "treehouse": "THE TREE HOUSE",
    "catapult": "THE CATAPULT",
    "greenhouse": "THE GREENHOUSE",
    "library": "THE LIBRARY",
    "tractor": "THE TRACTOR",
    "schoolbus": "THE SCHOOL BUS",
    "semi": "THE SEMI TRUCK",
    "dump": "THE DUMP TRUCK",
    "firetruck": "THE FIRETRUCK",
    "bulldozer": "THE BULLDOZER",
    "excavator": "THE EXCAVATOR",
    "wreckball": "THE WRECKING BALL",
    "racecar": "THE RACECAR",
    "monstertruck": "THE MONSTER TRUCK",
    "train": "THE TRAIN",
    "helicopter": "THE HELICOPTER",
    "airplane": "THE AIRPLANE",
    "jet": "THE JET",
    "pirateship": "THE PIRATE SHIP",
    "rollercoaster": "THE ROLLER COASTER",
    "palace": "THE PALACE",
    "skyscraper": "THE SKYSCRAPER",
    "castle": "THE CASTLE",
    "rocket": "THE ROCKET",
    "ufo": "THE UFO",
    "mech": "THE MECH",
    "robot": "THE ROBOT",
    "spacestation": "THE SPACE STATION",
}

# Merge all sections
ALL_SECTIONS = {}
ALL_SECTIONS.update(EXISTING)
ALL_SECTIONS.update(NEW_SECTIONS)

# Build list of all things for cover/ending text
ALL_THINGS = [SECTION_NAMES[s].replace("THE ", "").lower() for s in SECTION_ORDER]

if __name__ == "__main__":
    # Verify all sections exist
    for key in SECTION_ORDER:
        if key not in ALL_SECTIONS:
            print(f"MISSING SECTION: {key}")
        else:
            pages = ALL_SECTIONS[key]
            print(f"  {SECTION_NAMES[key]}: {len(pages)} pages, IDs: {[p['id'] for p in pages]}")

    print(f"\nTotal sections: {len(SECTION_ORDER)}")
    print(f"Total story pages: {len(SECTION_ORDER) * 3}")
    print(f"All things: {', '.join(ALL_THINGS)}")
