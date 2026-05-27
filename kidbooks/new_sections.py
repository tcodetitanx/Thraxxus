#!/usr/bin/env python3
"""New 20 sections for The Engineers - to be integrated into generate_book.py"""

# This file defines the 20 new sections. Each has 3 pages: help, build, use.
# KEY RULES:
# - Mama and Dada NEVER look at camera - always engaged in action
# - Boys always SAME height
# - Neo = GREEN with letter N, Ender = BLUE with letter E
# - Wall-E = golden cockapoo puppy

PROMPT_PREFIX = (
    "Using the attached image as a strict reference for the character faces, "
    "hair, skin tones, and the warm painterly art style, generate a new wide "
    "landscape illustration. Both toddler boys must be the EXACT same height. "
    "No character should look at the viewer -- everyone is engaged in the action. "
)

# ============================================================
# ORDERING (easiest -> most amazing):
# 1. Tree House
# 2. Catapult
# 3. Greenhouse
# 4. Library
# 5. Tractor
# 6. School Bus
# 7. Semi Truck
# 8. Dump Truck (existing)
# 9. Firetruck
# 10. Bulldozer
# 11. Excavator (existing)
# 12. Wrecking Ball
# 13. Racecar
# 14. Monster Truck
# 15. Train (existing)
# 16. Helicopter (existing)
# 17. Airplane (existing)
# 18. Jet
# 19. Pirate Ship
# 20. Roller Coaster
# 21. Palace
# 22. Skyscraper
# 23. Castle (existing)
# 24. Rocket (existing)
# 25. UFO
# 26. Mech
# 27. Robot (existing)
# 28. Space Station
# ============================================================

NEW_SECTIONS = {

# ══════════════════════════════════════════════════════════════
# 1. TREE HOUSE
# ══════════════════════════════════════════════════════════════
"treehouse": [
{
    "id": "treehouse_01_help",
    "type": "story",
    "text": [
        "In the big oak forest, a family of squirrels",
        "chattered nervously on a branch.",
        "",
        "A storm had knocked down their acorn stash!",
        "Hundreds of acorns scattered everywhere!",
        "",
        '"Let us help!" said Neo.',
        "The family gathered every acorn",
        "into neat little piles.",
    ],
    "prompt": PROMPT_PREFIX + (
        "A big oak forest with golden sunlight filtering through. The family in lumberjack outfits "
        "(one boy: green flannel shirt with letter N and tiny tool belt, "
        "other boy: blue flannel shirt with letter E and tiny tool belt, "
        "Mama: red plaid shirt sleeves rolled up ponytail flowing, "
        "Dada: brown flannel shirt suspenders looking down gathering acorns) "
        "gathers scattered acorns into piles on the forest floor. "
        "Mama bends down scooping acorns into a basket. Dada stacks them into a neat pyramid. "
        "The boys fill their pockets and small buckets. "
        "Three worried squirrels watch from branches above. "
        "The puppy sniffs at an acorn pile. Fallen leaves, mossy ground, warm autumn light."
    ),
},
{
    "id": "treehouse_02_build",
    "type": "story",
    "text": [
        "The squirrels leaped with joy!",
        '"Our acorns! Thank you SO much!"',
        '"We know every branch -- let us help YOU!"',
        "",
        '"Help us build a TREE HOUSE!" said Ender.',
        "",
        "Squirrels ran ropes up the tallest oak!",
        "Dada sawed the boards. Mama hammered walls.",
        "Neo and Ender painted it together!",
    ],
    "prompt": PROMPT_PREFIX + (
        "In the oak forest, the family builds a wooden tree house high in a massive oak tree. "
        "Same lumberjack outfits (boy in green flannel with N, boy in blue flannel with E). "
        "Squirrels run along branches carrying small ropes and nails in their cheeks. "
        "Dada saws a board on a sawhorse, looking down at his work. Mama hammers a wall panel up in the tree. "
        "The two boys paint the railing side by side -- one green, one blue. "
        "The puppy sits in a bucket being hoisted up by a rope pulley. "
        "Half-built treehouse with ladder, platform, and one wall. Leafy canopy, dappled sunlight."
    ),
},
{
    "id": "treehouse_03_use",
    "type": "story",
    "text": [
        "The tree house was PERFECT!",
        "It had a rope ladder, a lookout tower,",
        "and a slide all the way to the ground!",
        "",
        "The squirrels stored acorns up top.",
        "Neo and Ender looked through a telescope.",
        "Wall-E slid down the slide!",
    ],
    "prompt": PROMPT_PREFIX + (
        "A magnificent wooden tree house built in a giant oak tree with a rope ladder, "
        "lookout tower with a flag, and a curving slide. "
        "The two boys peer through a brass telescope from the lookout (green with N, blue with E). "
        "Mama reads a book in a hammock strung between branches. "
        "Dada grills something on a tiny balcony, looking down at the grill. "
        "Squirrels run along rope bridges. The puppy slides down the slide with ears flapping. "
        "Autumn leaves, warm golden light, forest stretching to the horizon."
    ),
},
],

# ══════════════════════════════════════════════════════════════
# 2. CATAPULT
# ══════════════════════════════════════════════════════════════
"catapult": [
{
    "id": "catapult_01_help",
    "type": "story",
    "text": [
        "At the pumpkin farm, a group of goats",
        "and turkeys were in a tizzy.",
        "",
        "The hay bales had tumbled off the barn loft",
        "and blocked the barn door!",
        "",
        '"Stand back!" said Dada.',
        "The family pushed and rolled every bale",
        "until the door was clear!",
    ],
    "prompt": PROMPT_PREFIX + (
        "An autumn pumpkin farm with a red barn. The family in medieval fair outfits "
        "(one boy: green tunic with letter N and small leather belt, "
        "other boy: blue tunic with letter E and small leather belt, "
        "Mama: peasant dress with braided hair pushing a hay bale, "
        "Dada: leather vest and work gloves rolling a bale away from the barn door) "
        "clears fallen hay bales from the barn entrance. "
        "The boys push a bale together. Three goats and two turkeys wait anxiously nearby. "
        "The puppy tugs at loose hay. Pumpkins line the path, scarecrow in the field, "
        "golden autumn trees. Warm afternoon light."
    ),
},
{
    "id": "catapult_02_build",
    "type": "story",
    "text": [
        "The goats stomped their hooves happily!",
        '"BAA! You saved our barn!"',
        '"We are strong -- we can help pull anything!"',
        "",
        '"Help us build a CATAPULT!" said Neo.',
        "",
        "Goats dragged the heavy beams into place!",
        "Turkeys wove the rope basket.",
        "Ender carved the trigger. Neo tested the arm!",
    ],
    "prompt": PROMPT_PREFIX + (
        "On the pumpkin farm, the family builds a big wooden catapult. "
        "Same medieval outfits (boy in green tunic with N, boy in blue tunic with E). "
        "Two goats drag a heavy wooden beam with ropes tied to their harnesses. "
        "Turkeys weave a rope basket with their beaks. "
        "Dada bolts the pivot joint, bent over his work. Mama measures the throwing arm with a ruler. "
        "The boy in blue carves a trigger latch. The boy in green tests pushing the arm down. "
        "The puppy chews on a rope end. Half-built catapult, pumpkins everywhere, red barn behind."
    ),
},
{
    "id": "catapult_03_use",
    "type": "story",
    "text": [
        "FWOOOOSH! The catapult launched a pumpkin",
        "way up into the sky!",
        "",
        "SPLAT! It exploded into a million pieces!",
        "",
        "Everyone laughed and loaded another one.",
        "The goats wanted a turn too!",
        "Wall-E hid behind a hay bale!",
    ],
    "prompt": PROMPT_PREFIX + (
        "The wooden catapult launches an orange pumpkin high into the blue sky on the farm. "
        "The two boys cheer with arms up watching the pumpkin fly (green with N, blue with E). "
        "Mama and Dada high-five each other looking at the sky. "
        "A goat stands on the catapult arm ready for the next launch. "
        "Pumpkin pieces splattered on the ground from previous launches. "
        "Turkeys flap excitedly. The puppy hides behind a hay bale peeking out. "
        "Blue sky, autumn colors, pure silliness and joy."
    ),
},
],

# ══════════════════════════════════════════════════════════════
# 3. GREENHOUSE
# ══════════════════════════════════════════════════════════════
"greenhouse": [
{
    "id": "greenhouse_01_help",
    "type": "story",
    "text": [
        "In the village garden, ladybugs and bees",
        "buzzed around sadly.",
        "",
        "The frost had killed all the flowers!",
        "There was nothing left to pollinate.",
        "",
        '"We can fix this!" said Mama.',
        "The family planted new seeds in warm soil",
        "and covered them with soft blankets.",
    ],
    "prompt": PROMPT_PREFIX + (
        "A village garden in early spring with frost on the ground. The family in gardener outfits "
        "(one boy: green gardener apron with letter N and tiny watering can, "
        "other boy: blue gardener apron with letter E and seed packets, "
        "Mama: sun hat and floral gardening gloves planting seeds bent over the soil, "
        "Dada: brown apron covering seedlings with cloth looking down at his work) "
        "plants new seeds in garden beds and covers them. "
        "Ladybugs land on frosted dead flowers looking sad. Bees hover with droopy wings. "
        "The boys pour water and scatter seeds side by side. "
        "The puppy digs a hole. Frost on fences, but warm sunshine breaking through clouds."
    ),
},
{
    "id": "greenhouse_02_build",
    "type": "story",
    "text": [
        "The ladybugs twirled with gratitude!",
        '"New flowers! But how do we keep them warm?"',
        "",
        '"Help us build a GREENHOUSE!" said Ender.',
        "",
        "Bees measured the glass panels perfectly!",
        "Ladybugs polished every pane until it sparkled.",
        "Mama built the frame.",
        "Neo and Ender fitted the door together!",
    ],
    "prompt": PROMPT_PREFIX + (
        "In the village garden, the family builds a beautiful glass greenhouse. "
        "Same gardener outfits (boy in green apron with N, boy in blue apron with E). "
        "Bees fly holding tiny measuring tapes between them. "
        "Ladybugs polish glass panels making them shine. "
        "Dada lifts a glass panel into the frame, looking up at it. "
        "Mama bolts the metal frame together, focused on her wrench. "
        "The two boys hold a small glass door, fitting it into hinges together. "
        "The puppy has a ladybug on his nose. "
        "Half-built greenhouse with some panels in place. Seedlings visible inside. Bright day."
    ),
},
{
    "id": "greenhouse_03_use",
    "type": "story",
    "text": [
        "The greenhouse was warm and wonderful!",
        "Flowers bloomed in every color,",
        "even in the middle of winter!",
        "",
        "The bees made the sweetest honey ever.",
        "Ladybugs danced on the petals.",
        "Neo grew a sunflower taller than Dada!",
    ],
    "prompt": PROMPT_PREFIX + (
        "A beautiful completed glass greenhouse bursting with colorful flowers inside "
        "while snow falls gently outside. "
        "Through the glass: the family admiring the flowers. "
        "The boy in green (N) stands next to a HUGE sunflower taller than Dada, pointing up at it. "
        "The boy in blue (E) smells a rose. "
        "Mama arranges a bouquet, looking down at the flowers. Dada waters a plant, focused on it. "
        "Bees fly between flowers carrying pollen. Ladybugs sit on petals. "
        "The puppy rolls in a pile of flower petals. "
        "Warm glow inside, snowy landscape outside. Magical contrast."
    ),
},
],

# ══════════════════════════════════════════════════════════════
# 4. LIBRARY
# ══════════════════════════════════════════════════════════════
"library": [
{
    "id": "library_01_help",
    "type": "story",
    "text": [
        "Under the old willow tree, a wise old tortoise",
        "and a family of mice had a problem.",
        "",
        "The rain had soaked all their books!",
        "Pages were soggy and stuck together.",
        "",
        '"Oh no!" said Neo. "We love books too!"',
        "The family carefully dried every page",
        "in the warm sunshine.",
    ],
    "prompt": PROMPT_PREFIX + (
        "Under a large willow tree on a sunny day. The family in scholarly outfits "
        "(one boy: green sweater vest with letter N and round glasses, "
        "other boy: blue sweater vest with letter E and round glasses, "
        "Mama: cardigan and reading glasses on her head spreading books to dry, "
        "Dada: tweed jacket gently separating wet pages looking down at a book) "
        "dries soggy books in the sunshine. Books spread open on blankets and rocks. "
        "An old tortoise with a tiny monocle watches sadly. "
        "A family of mice tries to peel apart tiny wet pages. "
        "The boys carefully lay pages flat side by side. "
        "The puppy sits on an open book. Willow branches sway, puddles drying."
    ),
},
{
    "id": "library_02_build",
    "type": "story",
    "text": [
        "The tortoise smiled his slow smile.",
        '"You saved our stories! We know every tale --',
        'let us help you build something wonderful."',
        "",
        '"Help us build a LIBRARY!" said Mama.',
        "",
        "Mice organized books by color and size!",
        "The tortoise carved beautiful wood shelves.",
        "Ender built a cozy reading nook.",
    ],
    "prompt": PROMPT_PREFIX + (
        "Under the willow tree, the family builds a charming small wooden library. "
        "Same scholarly outfits (boy in green vest with N, boy in blue vest with E). "
        "Mice carry tiny books in lines like an assembly line. "
        "The old tortoise carefully carves a bookshelf with a small chisel. "
        "Dada frames the walls, hammering a nail looking at the board. "
        "Mama paints a sign that reads LIBRARY, focused on her brush. "
        "The boy in green arranges books on a shelf. "
        "The boy in blue builds a window seat with cushions. "
        "The puppy carries a book in his mouth. Half-built cozy library. Warm light."
    ),
},
{
    "id": "library_03_use",
    "type": "story",
    "text": [
        "The library was the coziest place ever!",
        "Books from floor to ceiling,",
        "a fireplace, and beanbag chairs!",
        "",
        "The tortoise read stories in his deep slow voice.",
        "The mice ran a tiny lending desk.",
        "Everyone came to read -- even Wall-E!",
    ],
    "prompt": PROMPT_PREFIX + (
        "A charming small wooden library filled with colorful books floor to ceiling. "
        "A stone fireplace glows warmly. The family enjoys reading. "
        "The two boys lie on beanbag chairs with books (green vest N, blue vest E). "
        "Mama curls in an armchair reading, absorbed in her book. "
        "Dada sits cross-legged on the floor reading to a group of mice. "
        "The old tortoise reads from a big book in a rocking chair. "
        "Mice run a tiny desk with a stamp and card catalog. "
        "The puppy sleeps on a pile of cushions by the fire. "
        "Warm lamplight, cozy rugs, fairy lights on the ceiling."
    ),
},
],

# ══════════════════════════════════════════════════════════════
# 5. TRACTOR
# ══════════════════════════════════════════════════════════════
"tractor": [
{
    "id": "tractor_01_help",
    "type": "story",
    "text": [
        "On the big farm, the cows and chickens",
        "mooed and clucked in alarm.",
        "",
        "The old fence had fallen down",
        "and the sheep were wandering away!",
        "",
        '"Round them up!" called Dada.',
        "The family herded every sheep back",
        "and fixed the fence good as new!",
    ],
    "prompt": PROMPT_PREFIX + (
        "A big sunny farm with a red barn. The family in farmer outfits "
        "(one boy: green overalls with letter N and straw hat, "
        "other boy: blue overalls with letter E and straw hat, "
        "Mama: denim overalls and bandana herding sheep with arms wide, "
        "Dada: plaid shirt and jeans hammering a fence post looking down at it) "
        "herds wandering sheep back through a broken fence. "
        "Cows watch from behind, chickens flap around. "
        "The boys guide sheep with gentle arms. "
        "The puppy nips at a sheep's heels playfully. "
        "Rolling green pastures, red barn, silo, blue sky with fluffy clouds."
    ),
},
{
    "id": "tractor_02_build",
    "type": "story",
    "text": [
        "The cows mooed with relief!",
        '"MOO-velous! Our sheep friends are safe!"',
        '"We are strong -- we can pull anything!"',
        "",
        '"Help us build a TRACTOR!" said Neo.',
        "",
        "The cows pulled heavy engine parts!",
        "Chickens pecked bolts into the right holes!",
        "Dada welded the plow. Ender turned the steering wheel!",
    ],
    "prompt": PROMPT_PREFIX + (
        "On the farm, the family builds a big green tractor. "
        "Same farmer outfits (boy in green overalls with N, boy in blue overalls with E). "
        "A cow pulls a heavy engine block with a chain. "
        "Chickens peck bolts into holes on the chassis. "
        "Dada welds the plow attachment, sparks flying, face shield down. "
        "Mama tightens the engine, bent over the hood. "
        "The boy in green oils the gears. "
        "The boy in blue sits at the steering wheel grinning. "
        "The puppy rides on a cow's back. Half-built green tractor, barn behind."
    ),
},
{
    "id": "tractor_03_use",
    "type": "story",
    "text": [
        "VROOM VROOM! The big green tractor roared!",
        "",
        "They plowed the field into perfect rows",
        "and planted seeds for every animal.",
        "",
        "Corn for the chickens! Hay for the cows!",
        "Carrots for the sheep!",
        "Wall-E dug up a bone instead!",
    ],
    "prompt": PROMPT_PREFIX + (
        "A big shiny green tractor plows a farm field into neat rows. "
        "Dada drives the tractor looking ahead at the field. "
        "Mama walks behind planting seeds, looking down at the furrow. "
        "The two boys ride on the back scattering seeds (green overalls N, blue overalls E). "
        "Cows watch from a fence. Chickens follow picking up bugs. "
        "Sheep munch in a nearby pasture. "
        "The puppy digs up a bone from the fresh dirt, tail wagging. "
        "Beautiful farm landscape, golden wheat field in the distance, sunset colors."
    ),
},
],

# ══════════════════════════════════════════════════════════════
# 6. SCHOOL BUS
# ══════════════════════════════════════════════════════════════
"schoolbus": [
{
    "id": "schoolbus_01_help",
    "type": "story",
    "text": [
        "By the schoolyard, a family of raccoons",
        "and some friendly foxes looked confused.",
        "",
        "All the playground swings were tangled up",
        "in one big knotted mess!",
        "",
        '"We are great with knots!" said Ender.',
        "The family untangled every chain",
        "and oiled the squeaky seats.",
    ],
    "prompt": PROMPT_PREFIX + (
        "A schoolyard playground on a bright morning. The family in casual school outfits "
        "(one boy: green polo shirt with letter N and shorts, "
        "other boy: blue polo shirt with letter E and shorts, "
        "Mama: casual dress reaching up untangling swing chains, "
        "Dada: jeans and t-shirt on a step ladder working on chains looking up at them) "
        "untangles horribly knotted playground swing chains. "
        "Two raccoons try to help with their clever paws. Two foxes watch. "
        "The boys pull chains straight together. "
        "The puppy sits on a swing seat. School building in background, trees, sandbox."
    ),
},
{
    "id": "schoolbus_02_build",
    "type": "story",
    "text": [
        "The raccoons washed their paws with pride!",
        '"Fixed! Our clever paws can build anything!"',
        "The foxes wagged their tails.",
        "",
        '"Help us build a SCHOOL BUS!" said Mama.',
        "",
        "Raccoons wired the engine with nimble fingers!",
        "Foxes painted it the brightest yellow!",
        "Neo installed the stop sign. Ender rang the bell!",
    ],
    "prompt": PROMPT_PREFIX + (
        "In the schoolyard, the family builds a big yellow school bus. "
        "Same school outfits (boy in green polo with N, boy in blue polo with E). "
        "Raccoons wire the engine compartment with their dexterous paws. "
        "Foxes paint the sides bright yellow with brushes in their mouths. "
        "Dada bolts on the wheels, crouching down focused on the lug nuts. "
        "Mama installs the windshield, concentrating on fitting it in. "
        "The boy in green attaches a fold-out stop sign. "
        "The boy in blue rings a silver bell on top. "
        "The puppy sits in the driver seat. Half-built yellow bus. Cheerful scene."
    ),
},
{
    "id": "schoolbus_03_use",
    "type": "story",
    "text": [
        "HONK HONK! The school bus was ready!",
        "",
        "They picked up ALL the animal kids",
        "for the very first day of school!",
        "",
        "Baby raccoons and fox cubs waved from windows.",
        "Neo and Ender shared their snacks!",
        "Wall-E was the bus monitor!",
    ],
    "prompt": PROMPT_PREFIX + (
        "A bright yellow school bus drives down a tree-lined country road. "
        "Dada drives the bus looking at the road ahead. "
        "Mama waves from the door greeting passengers. "
        "The two boys lean out windows waving (green polo N, blue polo E). "
        "Baby raccoons, fox cubs, and other animal babies peek from windows waving. "
        "The puppy wears a tiny crossing guard vest, standing at the bus door. "
        "A stop sign folds out from the side. Autumn trees, picket fences, cozy houses."
    ),
},
],

# ══════════════════════════════════════════════════════════════
# 7. SEMI TRUCK
# ══════════════════════════════════════════════════════════════
"semi": [
{
    "id": "semi_01_help",
    "type": "story",
    "text": [
        "At the mountain pass, a family of yaks",
        "and some mountain goats were stuck.",
        "",
        "A rockslide had blocked the only road!",
        "No one could get through!",
        "",
        '"Everybody push!" said Mama.',
        "The family moved rocks one by one",
        "until the road was clear again!",
    ],
    "prompt": PROMPT_PREFIX + (
        "A mountain pass road blocked by fallen rocks. The family in trucker outfits "
        "(one boy: green trucker jacket with letter N and baseball cap, "
        "other boy: blue trucker jacket with letter E and baseball cap, "
        "Mama: denim jacket sleeves rolled up pushing a boulder focused on it, "
        "Dada: leather vest and trucker cap lifting a rock looking down at it) "
        "clears fallen rocks from the road. "
        "Yaks with shaggy fur and mountain goats watch from behind the rockslide. "
        "The boys roll small rocks to the side together. "
        "The puppy barks at a pebble. Snowy mountain peaks, pine trees, winding road."
    ),
},
{
    "id": "semi_02_build",
    "type": "story",
    "text": [
        "The yaks bowed their big furry heads!",
        '"You cleared our path! We are the strongest',
        'in the mountains -- we will help!"',
        "",
        '"Help us build a SEMI TRUCK!" said Dada.',
        "",
        "Yaks pulled the enormous trailer into place!",
        "Mountain goats balanced on top to bolt the roof!",
        "Neo honked the air horn -- BRAAAAP!",
    ],
    "prompt": PROMPT_PREFIX + (
        "At the mountain pass, the family builds a massive red semi truck with trailer. "
        "Same trucker outfits (boy in green jacket with N, boy in blue jacket with E). "
        "Two yaks pull the enormous trailer on chains. "
        "Mountain goats stand on top of the trailer bolting the roof panels. "
        "Dada welds the chassis underneath, sparks visible. "
        "Mama tightens the hitch connecting cab to trailer, focused on the mechanism. "
        "The boy in green reaches for the air horn cord. "
        "The boy in blue paints flames on the cab. "
        "The puppy sleeps in the cab. Half-built semi, mountains behind."
    ),
},
{
    "id": "semi_03_use",
    "type": "story",
    "text": [
        "BRAAAAP! The mighty semi truck rolled out!",
        "",
        "They delivered supplies to every animal",
        "village in the mountains!",
        "",
        "Hay for the yaks! Salt licks for the goats!",
        "The truck echoed through the valleys!",
        "Wall-E was the co-driver!",
    ],
    "prompt": PROMPT_PREFIX + (
        "A massive red semi truck with flame decals drives along a winding mountain road. "
        "Dada drives looking at the road, Mama checks a map in the passenger seat. "
        "The two boys wave from the sleeper cab window (green with N, blue with E). "
        "The puppy sits on the dashboard looking out the windshield. "
        "The trailer is loaded with hay bales and supplies visible through an open side. "
        "Yaks and mountain goats wave from a village below. "
        "Snowy peaks, pine forests, eagles soaring, dramatic mountain scenery."
    ),
},
],

# ══════════════════════════════════════════════════════════════
# 8. FIRETRUCK
# ══════════════════════════════════════════════════════════════
"firetruck": [
{
    "id": "firetruck_01_help",
    "type": "story",
    "text": [
        "At the firehouse, the dalmatians",
        "and a brave little cat were panicking.",
        "",
        "Water was flooding the firehouse basement!",
        "All their gear was getting soaked!",
        "",
        '"Bucket brigade!" called Dada.',
        "The family bailed water all afternoon",
        "and saved every last piece of gear!",
    ],
    "prompt": PROMPT_PREFIX + (
        "A red firehouse with water flooding from the basement. The family in firefighter outfits "
        "(one boy: green firefighter coat with letter N and small helmet, "
        "other boy: blue firefighter coat with letter E and small helmet, "
        "Mama: firefighter turnout gear carrying a bucket of water, looking at where to dump it, "
        "Dada: firefighter gear working a hand pump focused on the pump handle) "
        "bails water from the flooded basement. A bucket brigade line. "
        "Two dalmatians carry buckets in their mouths. A tabby cat rescues a hose from the water. "
        "The boys pass buckets to each other. "
        "The puppy splashes in a puddle. Water streams, fire pole visible inside."
    ),
},
{
    "id": "firetruck_02_build",
    "type": "story",
    "text": [
        "The dalmatians barked with gratitude!",
        '"WOOF! You saved our station!"',
        '"We know all about firefighting -- let us help!"',
        "",
        '"Help us build a FIRETRUCK!" said Neo.',
        "",
        "Dalmatians polished every surface until it gleamed!",
        "The cat tested the siren -- WEEEE-OOOO!",
        "Ender coiled the hose. Neo rang the bell!",
    ],
    "prompt": PROMPT_PREFIX + (
        "At the firehouse, the family builds a big red firetruck. "
        "Same firefighter outfits (boy in green coat with N, boy in blue coat with E). "
        "Dalmatians polish the red hood with rags in their mouths making it gleam. "
        "A tabby cat sits on the roof testing the siren with a paw. "
        "Dada installs the water pump, head under the chassis looking at pipes. "
        "Mama attaches the ladder to the top, concentrating on the brackets. "
        "The boy in green rings a brass bell on top. "
        "The boy in blue coils a long hose neatly. "
        "The puppy wears a dalmatian-spotted bandana. Half-built firetruck, firehouse behind."
    ),
},
{
    "id": "firetruck_03_use",
    "type": "story",
    "text": [
        "WEEEE-OOOO! The firetruck raced down the road!",
        "",
        "They rescued a kitten from a tree,",
        "put out a campfire that got too big,",
        "and saved the day THREE times!",
        "",
        "The dalmatians rode on top proudly!",
        "Wall-E wore a tiny firefighter hat!",
    ],
    "prompt": PROMPT_PREFIX + (
        "A gleaming red firetruck races down a town street with lights flashing. "
        "Dada drives looking ahead, Mama operates the ladder from the back. "
        "The two boys hold on from the back step waving at townspeople "
        "(green coat with N, blue coat with E). "
        "Dalmatians ride on top with spots gleaming. "
        "A tabby cat sits in the passenger seat. "
        "The puppy wears a tiny red firefighter helmet. "
        "A saved kitten rides on top of the ladder. "
        "Townspeople wave, buildings with bunting, blue sky."
    ),
},
],

# ══════════════════════════════════════════════════════════════
# 9. BULLDOZER
# ══════════════════════════════════════════════════════════════
"bulldozer": [
{
    "id": "bulldozer_01_help",
    "type": "story",
    "text": [
        "In the rocky quarry, a family of armadillos",
        "and some tough little hedgehogs had trouble.",
        "",
        "A mudslide had buried their burrows!",
        "They had nowhere to sleep!",
        "",
        '"We will dig you out!" said Ender.',
        "The family shoveled mud all day long",
        "until every burrow was open again!",
    ],
    "prompt": PROMPT_PREFIX + (
        "A rocky quarry after a mudslide. The family in heavy construction gear "
        "(one boy: green work jumpsuit with letter N and hard hat, "
        "other boy: blue work jumpsuit with letter E and hard hat, "
        "Mama: yellow work jumpsuit shoveling mud away from a burrow entrance, "
        "Dada: orange jumpsuit using a pickaxe on packed mud looking down at his swing) "
        "digs out buried animal burrows. "
        "Armadillos in curled-up balls wait for their homes. Hedgehogs huddle together. "
        "The boys scoop mud with small shovels side by side. "
        "The puppy is covered in mud, digging furiously. "
        "Rocky cliffs, muddy terrain, cloudy sky clearing up."
    ),
},
{
    "id": "bulldozer_02_build",
    "type": "story",
    "text": [
        "The armadillos uncurled and danced!",
        '"Our homes! We can dig through ANYTHING --',
        'let us help you!"',
        "",
        '"Help us build a BULLDOZER!" said Dada.',
        "",
        "Armadillos tested the blade edge with their shells!",
        "Hedgehogs pushed pins into tight spots!",
        "Neo pulled the throttle. Ender steered!",
    ],
    "prompt": PROMPT_PREFIX + (
        "In the quarry, the family builds a massive yellow bulldozer. "
        "Same construction gear (boy in green jumpsuit with N, boy in blue with E). "
        "Armadillos roll their hard shells against the bulldozer blade to test its strength. "
        "Hedgehogs use their quills to push pins into tight crevices. "
        "Dada welds the blade, face shield down looking at the weld. "
        "Mama installs the hydraulic arms, focused on connecting hoses. "
        "The boy in green pulls a throttle lever. The boy in blue turns the steering controls. "
        "The puppy sits on the engine hood. Half-built yellow bulldozer, rocky quarry."
    ),
},
{
    "id": "bulldozer_03_use",
    "type": "story",
    "text": [
        "RRRUMMBLE! The bulldozer pushed forward!",
        "",
        "They flattened a whole hill of rocks",
        "and made a perfect playground!",
        "",
        "The armadillos went bowling with rocks!",
        "Hedgehogs played king of the dirt hill!",
        "Wall-E rode on the blade!",
    ],
    "prompt": PROMPT_PREFIX + (
        "A massive yellow bulldozer pushes a hill of rocks flat, creating a playground. "
        "Dada operates the bulldozer, looking ahead at the terrain. "
        "Mama directs with hand signals from the ground, facing the bulldozer. "
        "The two boys slide down a freshly made dirt ramp (green jumpsuit N, blue jumpsuit E). "
        "Armadillos bowl with round rocks on a flat area. "
        "Hedgehogs stand on top of a small dirt hill. "
        "The puppy rides on the front blade, ears flapping. "
        "Cleared flat area becoming a playground, rocky quarry walls behind."
    ),
},
],

# ══════════════════════════════════════════════════════════════
# 10. WRECKING BALL
# ══════════════════════════════════════════════════════════════
"wreckball": [
{
    "id": "wreckball_01_help",
    "type": "story",
    "text": [
        "At the old factory, a family of pigeons",
        "and some clever rats were upset.",
        "",
        "A rusty old gate was jammed shut",
        "and they could not get to their nests inside!",
        "",
        '"Let me try," said Mama.',
        "The family oiled the hinges and pried",
        "until the gate swung open with a CREAK!",
    ],
    "prompt": PROMPT_PREFIX + (
        "An old brick factory with a rusty gate. The family in demolition crew outfits "
        "(one boy: green safety vest with letter N and ear protectors, "
        "other boy: blue safety vest with letter E and ear protectors, "
        "Mama: work overalls using a crowbar on the rusty gate hinges, "
        "Dada: hard hat and vest spraying oil on the hinges from a can looking at them) "
        "pries open a jammed rusty gate. "
        "Pigeons crowd the top of the gate cooing anxiously. Rats peek from holes in the wall. "
        "The boys push on the gate together with all their might. "
        "The puppy tugs a rope tied to the gate. Old brick walls, ivy, rusty pipes."
    ),
},
{
    "id": "wreckball_02_build",
    "type": "story",
    "text": [
        "The pigeons cooed happily!",
        '"COO COO! We can fly anywhere!"',
        '"And we rats know every bolt and gear!"',
        "",
        '"Help us build a WRECKING BALL!" said Neo.',
        "",
        "Pigeons carried cables up to the crane arm!",
        "Rats tightened every gear inside!",
        "Dada forged the heavy iron ball!",
    ],
    "prompt": PROMPT_PREFIX + (
        "At the old factory, the family builds a wrecking ball crane. "
        "Same demolition outfits (boy in green vest with N, boy in blue vest with E). "
        "Pigeons carry steel cables up to the crane arm in their claws. "
        "Rats work inside the machinery tightening tiny gears. "
        "Dada hammers a massive iron ball at a forge, sparks flying, looking at the anvil. "
        "Mama operates the crane controls, focused on the levers. "
        "The boy in green paints caution stripes on the crane. "
        "The boy in blue welds chain links. "
        "The puppy watches from behind safety cones. Half-built crane, factory backdrop."
    ),
},
{
    "id": "wreckball_03_use",
    "type": "story",
    "text": [
        "CRASH! BOOM! SMASH!",
        "The wrecking ball swung through the old walls!",
        "",
        "Bricks flew everywhere!",
        "They knocked down the crumbly old building",
        "to make room for a brand new park!",
        "",
        "Everyone cheered! Wall-E hid under a hard hat!",
    ],
    "prompt": PROMPT_PREFIX + (
        "A wrecking ball crane smashes through an old brick wall sending bricks flying. "
        "Mama operates the crane from the cab, focused on the controls. "
        "Dada watches from a safe distance pointing at the impact zone. "
        "The two boys watch from behind a safety fence cheering with arms up "
        "(green vest N, blue vest E). "
        "Pigeons scatter from the dust cloud. Rats cheer from a safe spot. "
        "The puppy hides under a yellow hard hat. "
        "Dust cloud, flying bricks, dramatic action. Blue sky through the hole in the wall."
    ),
},
],

# ══════════════════════════════════════════════════════════════
# 11. RACECAR
# ══════════════════════════════════════════════════════════════
"racecar": [
{
    "id": "racecar_01_help",
    "type": "story",
    "text": [
        "At the racetrack, a family of cheetahs",
        "and some zippy roadrunners were sad.",
        "",
        "The track was full of potholes!",
        "Nobody could run fast anymore.",
        "",
        '"We can fix that!" said Dada.',
        "The family filled every pothole",
        "with gravel and smooth asphalt.",
    ],
    "prompt": PROMPT_PREFIX + (
        "A racing oval track with potholes everywhere. The family in racing outfits "
        "(one boy: green racing suit with letter N and racing gloves, "
        "other boy: blue racing suit with letter E and racing gloves, "
        "Mama: red racing jumpsuit shoveling gravel into a pothole, "
        "Dada: white racing suit smoothing asphalt with a roller looking down at the surface) "
        "repairs potholes on the track. "
        "Two sleek cheetahs sit by the track looking disappointed. Roadrunners pace nearby. "
        "The boys pour gravel into holes side by side. "
        "The puppy rolls a small tire around. Grandstands, finish line, checkered flags."
    ),
},
{
    "id": "racecar_02_build",
    "type": "story",
    "text": [
        "The cheetahs purred loudly!",
        '"The track is FAST again! We are the fastest --',
        'let us test your creation!"',
        "",
        '"Help us build a RACECAR!" said Ender.',
        "",
        "Cheetahs tested the aerodynamics with their speed!",
        "Roadrunners checked every wheel bearing!",
        "Neo mounted the spoiler! Ender waxed the hood!",
    ],
    "prompt": PROMPT_PREFIX + (
        "At the racetrack, the family builds a sleek red racecar. "
        "Same racing outfits (boy in green racing suit with N, boy in blue with E). "
        "Cheetahs run alongside to test the wind shape of the car. "
        "Roadrunners spin the wheels checking bearings. "
        "Dada installs the engine, head under the hood looking at parts. "
        "Mama tightens the roll cage, focused on the bolts. "
        "The boy in green mounts a big rear spoiler. "
        "The boy in blue waxes the shiny red hood. "
        "The puppy sits in the driver seat with a tiny helmet. Half-built red racecar on the track."
    ),
},
{
    "id": "racecar_03_use",
    "type": "story",
    "text": [
        "VROOOOM! The racecar blasted off the start line!",
        "",
        "They zoomed around the track so fast",
        "everything was a blur!",
        "",
        "They even raced a cheetah -- and TIED!",
        '"Fastest family EVER!" cheered Neo.',
        "Wall-E wore tiny racing goggles!",
    ],
    "prompt": PROMPT_PREFIX + (
        "A sleek red racecar zooms around a track at incredible speed with motion blur. "
        "Dada drives gripping the wheel looking at the track ahead. "
        "Mama navigates from the passenger seat, looking at a stopwatch. "
        "The two boys cheer from the back (green suit N, blue suit E). "
        "A cheetah runs alongside neck and neck with the car. "
        "Roadrunners race on the inside track. "
        "The puppy wears tiny racing goggles, fur blowing back. "
        "Checkered flags, tire smoke, speed lines, grandstands full of cheering animals."
    ),
},
],

# ══════════════════════════════════════════════════════════════
# 12. MONSTER TRUCK
# ══════════════════════════════════════════════════════════════
"monstertruck": [
{
    "id": "monstertruck_01_help",
    "type": "story",
    "text": [
        "In the muddy swamp, a family of hippos",
        "and some strong crocodiles were in trouble.",
        "",
        "A huge fallen tree blocked the river",
        "and the water was rising fast!",
        "",
        '"We need to move that tree!" said Neo.',
        "The family tied ropes and pulled together",
        "until the tree shifted and the water flowed!",
    ],
    "prompt": PROMPT_PREFIX + (
        "A muddy swamp with a river blocked by a massive fallen tree. The family in monster truck rally outfits "
        "(one boy: green monster truck jersey with letter N and bandana, "
        "other boy: blue monster truck jersey with letter E and bandana, "
        "Mama: mud-splattered overalls pulling a rope tied to the tree, "
        "Dada: muscle shirt and gloves heaving on a rope looking at the tree) "
        "pulls a fallen tree from the river. "
        "Hippos push from the water side. Crocodiles watch the rising water level. "
        "The boys pull a rope together. "
        "The puppy bites a small branch. Muddy water, lily pads, cypress trees, misty swamp."
    ),
},
{
    "id": "monstertruck_02_build",
    "type": "story",
    "text": [
        "The hippos splashed with happiness!",
        '"The river flows again!"',
        '"We are the STRONGEST -- we can lift anything!"',
        "",
        '"Help us build a MONSTER TRUCK!" said Ender.',
        "",
        "Hippos held up the frame while Dada welded!",
        "Crocodiles bit tire treads into shape!",
        "Neo and Ender bolted on the GIGANTIC wheels!",
    ],
    "prompt": PROMPT_PREFIX + (
        "In the swamp clearing, the family builds a massive monster truck. "
        "Same rally outfits (boy in green jersey with N, boy in blue jersey with E). "
        "Two hippos hold up the heavy truck frame on their backs. "
        "Crocodiles bite tire treads into deep grooves with their powerful jaws. "
        "Dada welds the frame from above, looking at the weld. "
        "Mama installs the suspension springs, concentrating on the bolts. "
        "The two boys together bolt on a wheel taller than they are. "
        "The puppy rides in a tire like a hamster wheel. "
        "Half-built monster truck with ENORMOUS wheels, swampy background."
    ),
},
{
    "id": "monstertruck_03_use",
    "type": "story",
    "text": [
        "CRUSH! CRUNCH! ROAAARR!",
        "The monster truck crushed old cars flat!",
        "",
        "It jumped over a ramp and flew through the air!",
        "",
        "The crowd went WILD!",
        '"AGAIN! AGAIN!" yelled Neo and Ender.',
        "Wall-E bounced around inside!",
    ],
    "prompt": PROMPT_PREFIX + (
        "A massive monster truck with flames painted on it soars through the air over a ramp "
        "in a packed mud arena. Cars crushed flat below. "
        "Dada drives gripping the wheel, looking up through the windshield. "
        "Mama holds on tight next to him. "
        "The two boys are strapped in the back cheering (green jersey N, blue jersey E). "
        "The puppy bounces in zero gravity inside the cab. "
        "Hippos and crocodiles cheer from the stands. Mud splashes, fireworks, spotlights. "
        "Dramatic action shot mid-jump, epic and exciting."
    ),
},
],

# ══════════════════════════════════════════════════════════════
# 13. JET
# ══════════════════════════════════════════════════════════════
"jet": [
{
    "id": "jet_01_help",
    "type": "story",
    "text": [
        "At the airfield, two peregrine falcons",
        "and a great albatross were grounded.",
        "",
        "An oil spill had gotten on their feathers!",
        "They could not fly at all!",
        "",
        '"Hold still," said Mama gently.',
        "The family washed every feather clean",
        "with warm soapy water.",
    ],
    "prompt": PROMPT_PREFIX + (
        "An airfield with a concrete runway. The family in jet pilot outfits "
        "(one boy: green flight suit with letter N and aviator helmet, "
        "other boy: blue flight suit with letter E and aviator helmet, "
        "Mama: white flight suit gently washing a falcon's wing with a soapy cloth, "
        "Dada: flight jacket drying an albatross's feathers with a towel focused on the bird) "
        "carefully cleans oil off birds' feathers. "
        "Two peregrine falcons sit in warm water basins. An albatross spreads its wide wings. "
        "The boys gently rinse feathers with warm water. "
        "The puppy carries a clean towel. Oil stains, soap bubbles, hangars in background."
    ),
},
{
    "id": "jet_02_build",
    "type": "story",
    "text": [
        "The falcons screeched with joy!",
        '"We can FLY again! We are the FASTEST birds --',
        'let us help you go even faster!"',
        "",
        '"Help us build a JET!" said Dada.',
        "",
        "Falcons shaped the delta wings to be super fast!",
        "The albatross tested the wingspan!",
        "Neo and Ender painted racing stripes!",
    ],
    "prompt": PROMPT_PREFIX + (
        "On the airfield, the family builds a sleek silver jet. "
        "Same flight suits (boy in green with N, boy in blue with E). "
        "Peregrine falcons dive past the delta wings testing the air flow. "
        "The albatross spreads its wings next to the jet wing comparing wingspan. "
        "Dada rivets fuselage panels, focused on the rivet gun. "
        "Mama wires the cockpit instruments, head inside the panel. "
        "The two boys paint racing stripes on the side -- green and blue stripes. "
        "The puppy sits in the ejection seat. Half-built silver jet, runway behind."
    ),
},
{
    "id": "jet_03_use",
    "type": "story",
    "text": [
        "WHOOOOSH! BOOM! The jet broke",
        "the sound barrier!",
        "",
        "They flew faster than anything EVER!",
        "Clouds whipped by like cotton candy!",
        "",
        '"We are going SO fast!" screamed Ender.',
        "Even the falcons could not keep up!",
    ],
    "prompt": PROMPT_PREFIX + (
        "A sleek silver jet with green and blue racing stripes breaks the sound barrier "
        "with a visible shock cone around it. "
        "Through the cockpit glass: Dada pilots looking at instruments, "
        "Mama co-pilots checking the altimeter. "
        "The two boys press their faces to side windows (green suit N, blue suit E). "
        "The puppy's cheeks ripple from the G-forces. "
        "Falcons try to keep up but fall behind. "
        "Clouds streak past, blue sky above, ocean below, sonic boom rings. Exhilarating speed."
    ),
},
],

# ══════════════════════════════════════════════════════════════
# 14. PIRATE SHIP
# ══════════════════════════════════════════════════════════════
"pirateship": [
{
    "id": "pirateship_01_help",
    "type": "story",
    "text": [
        "On the rocky shore, a pod of dolphins",
        "and a wise old sea turtle were in distress.",
        "",
        "A fishing net was tangled around",
        "the sea turtle's shell!",
        "",
        '"Be careful," said Dada.',
        "The family gently cut every strand",
        "until the turtle was free!",
    ],
    "prompt": PROMPT_PREFIX + (
        "A rocky tropical shore with turquoise water. The family in pirate outfits "
        "(one boy: green pirate vest with letter N and bandana, "
        "other boy: blue pirate vest with letter E and bandana, "
        "Mama: pirate captain coat and tricorn hat cutting net with scissors focused on the strands, "
        "Dada: striped pirate shirt gently lifting net off the turtle's shell looking at it) "
        "frees a sea turtle from a tangled fishing net. "
        "Dolphins swim close watching with concern. "
        "The boys hold the turtle steady gently. "
        "The puppy barks at the net. Rocky shore, tide pools, palm trees, sunset colors."
    ),
},
{
    "id": "pirateship_02_build",
    "type": "story",
    "text": [
        "The sea turtle nodded wisely.",
        '"I have sailed every ocean for 100 years.',
        'I will guide you anywhere!"',
        "",
        '"Help us build a PIRATE SHIP!" said Neo.',
        "",
        "Dolphins pushed planks through the waves!",
        "The turtle designed the perfect hull!",
        "Ender raised the Jolly Roger flag!",
    ],
    "prompt": PROMPT_PREFIX + (
        "On the shore, the family builds a wooden pirate ship in a dry dock. "
        "Same pirate outfits (boy in green vest with N, boy in blue vest with E). "
        "Dolphins push wooden planks through the shallow water to the dock. "
        "The old sea turtle points at hull blueprints with a flipper. "
        "Dada hammers planks onto the hull, looking at the nails. "
        "Mama sews the main sail with a big needle, focused on the stitching. "
        "The boy in green tarrs the hull. "
        "The boy in blue raises a Jolly Roger flag with a skull wearing a cute bow. "
        "The puppy has an eye patch. Half-built ship, ocean behind."
    ),
},
{
    "id": "pirateship_03_use",
    "type": "story",
    "text": [
        "ARRR! The pirate ship sailed the seven seas!",
        "",
        "They found a treasure island",
        "with a chest full of gold coins!",
        "",
        "Captain Neo and Captain Ender",
        "shared the treasure with everyone!",
        "Wall-E found a golden bone!",
    ],
    "prompt": PROMPT_PREFIX + (
        "A magnificent wooden pirate ship with billowing sails on a turquoise tropical sea. "
        "Mama steers the ship's wheel, hair blowing in the wind looking at the horizon. "
        "Dada climbs the rigging adjusting sails, looking up at the mast. "
        "The two boys stand at the bow pointing at a treasure island ahead "
        "(green pirate vest N, blue pirate vest E) with pirate hats. "
        "The puppy holds a golden bone in his mouth wearing an eye patch. "
        "Dolphins leap alongside. The sea turtle swims ahead. "
        "An open treasure chest of gold on the deck. Tropical island ahead, sunset sky."
    ),
},
],

# ══════════════════════════════════════════════════════════════
# 15. ROLLER COASTER
# ══════════════════════════════════════════════════════════════
"rollercoaster": [
{
    "id": "rollercoaster_01_help",
    "type": "story",
    "text": [
        "At the fairgrounds, a troop of monkeys",
        "and some playful otters were frustrated.",
        "",
        "The merry-go-round was broken!",
        "It would not spin at all!",
        "",
        '"Let me take a look," said Mama.',
        "The family fixed the motor and oiled the gears.",
        "The merry-go-round spun perfectly!",
    ],
    "prompt": PROMPT_PREFIX + (
        "A colorful fairground with a broken merry-go-round. The family in carnival worker outfits "
        "(one boy: green carnival vest with letter N and striped cap, "
        "other boy: blue carnival vest with letter E and striped cap, "
        "Mama: mechanic jumpsuit with wrench fixing the motor underneath the merry-go-round, "
        "Dada: tool belt oiling gears looking closely at the mechanism) "
        "repairs the merry-go-round. "
        "Monkeys hang from the carousel poles sadly. Otters tap the floor waiting. "
        "The boys hand tools to their parents. "
        "The puppy chases his tail near the carousel. Colorful tents, bunting, popcorn cart."
    ),
},
{
    "id": "rollercoaster_02_build",
    "type": "story",
    "text": [
        "The monkeys swung from the spinning horses!",
        '"EEEE! You fixed it! We love climbing things!"',
        '"And we otters love sliding!" squeaked the otters.',
        "",
        '"Help us build a ROLLER COASTER!" said Ender.',
        "",
        "Monkeys climbed the frame to bolt the top!",
        "Otters tested the slippery rails!",
        "Neo and Ender tightened the last track piece!",
    ],
    "prompt": PROMPT_PREFIX + (
        "At the fairground, the family builds an enormous wooden roller coaster. "
        "Same carnival outfits (boy in green vest with N, boy in blue vest with E). "
        "Monkeys climb the tall wooden frame bolting crossbeams at the top. "
        "Otters slide down the test rails to check smoothness. "
        "Dada hammers a support beam, looking at where the nail goes. "
        "Mama levels a section of track, checking with a spirit level. "
        "The two boys bolt the last piece of track together, connecting a loop. "
        "The puppy rides in a roller coaster car on the ground. "
        "Enormous wooden structure with loops and drops, fairground behind."
    ),
},
{
    "id": "rollercoaster_03_use",
    "type": "story",
    "text": [
        "CLICKETY CLACK... up, up, up they went...",
        "",
        "WHOOOOOOSH! Down the mega drop!",
        "Through the loop! Around the corkscrew!",
        "",
        '"WHEEEEE!" screamed the whole family.',
        "The monkeys rode with their arms up!",
        "Wall-E's ears flew straight behind him!",
    ],
    "prompt": PROMPT_PREFIX + (
        "A colorful roller coaster car plunges down an enormous drop with everyone screaming with joy. "
        "Mama and Dada in the front car, arms up, looking at the track ahead. "
        "The two boys behind them screaming with delight (green vest N, blue vest E). "
        "Monkeys ride with all four arms up. Otters slide along rails beside. "
        "The puppy's ears fly straight back, tongue out. "
        "The track loops, corkscrews, and spirals in the background. "
        "Fairground lights, cotton candy clouds, sunset sky. Pure thrill and excitement."
    ),
},
],

# ══════════════════════════════════════════════════════════════
# 16. PALACE
# ══════════════════════════════════════════════════════════════
"palace": [
{
    "id": "palace_01_help",
    "type": "story",
    "text": [
        "In the royal gardens, a flock of peacocks",
        "and some elegant swans were distraught.",
        "",
        "The ornamental pond had dried up",
        "and the beautiful lily pads were wilting!",
        "",
        '"We know just what to do!" said Ender.',
        "The family dug a channel from the creek",
        "and fresh water filled the pond!",
    ],
    "prompt": PROMPT_PREFIX + (
        "An elegant royal garden with a dried-up ornamental pond. The family in royal builder outfits "
        "(one boy: green royal tunic with letter N and gold trim, "
        "other boy: blue royal tunic with letter E and gold trim, "
        "Mama: elegant work dress and pearl headband digging a channel with a shovel, "
        "Dada: royal builder vest with gold buttons guiding water flow looking at the channel) "
        "digs a channel from a creek to refill the pond. "
        "Peacocks with drooping tail feathers stand by the dry pond. Swans look at the cracked mud. "
        "The boys dig with small shovels. "
        "The puppy splashes in the first trickle of water. "
        "Wilting lily pads, ornate stone edges, topiaries, rose bushes."
    ),
},
{
    "id": "palace_02_build",
    "type": "story",
    "text": [
        "The peacocks fanned their magnificent tails!",
        '"Glorious! We know everything about beauty!"',
        '"And we swans are master builders!" they said.',
        "",
        '"Help us build a PALACE!" said Mama.',
        "",
        "Peacocks designed the stained glass windows!",
        "Swans shaped the marble arches!",
        "Neo gilded the dome. Ender placed the throne!",
    ],
    "prompt": PROMPT_PREFIX + (
        "In the royal gardens, the family builds a magnificent white marble palace. "
        "Same royal outfits (boy in green tunic with N, boy in blue tunic with E). "
        "Peacocks arrange colorful feathers into stained glass window patterns. "
        "Swans glide carrying marble blocks balanced on their backs. "
        "Dada chisels a marble column, focused on the stone. "
        "Mama fits stained glass into a window frame, concentrating on the glass. "
        "The boy in green paints gold leaf on the dome. "
        "The boy in blue carries a small ornate throne. "
        "The puppy wears a tiny crown. Half-built white palace with columns and arches."
    ),
},
{
    "id": "palace_03_use",
    "type": "story",
    "text": [
        "The palace was BREATHTAKING!",
        "Crystal chandeliers, marble floors,",
        "and a throne room with TWO thrones!",
        "",
        "The peacocks danced in the grand ballroom!",
        "The swans swam in the palace fountain!",
        "Everyone had a royal ball!",
    ],
    "prompt": PROMPT_PREFIX + (
        "A magnificent white marble palace with gold domes and stained glass windows. "
        "In the grand ballroom with crystal chandeliers and marble floors: "
        "the family dances together. Mama and Dada waltz, looking at each other. "
        "The two boys sit on two small thrones side by side (green tunic N, blue tunic E) "
        "wearing golden crowns. Peacocks display full tail fans. "
        "Swans swim in an indoor fountain. "
        "The puppy slides across the marble floor in a tiny crown. "
        "Grand columns, red carpet, roses everywhere, golden light."
    ),
},
],

# ══════════════════════════════════════════════════════════════
# 17. SKYSCRAPER
# ══════════════════════════════════════════════════════════════
"skyscraper": [
{
    "id": "skyscraper_01_help",
    "type": "story",
    "text": [
        "In the big city, some pigeons",
        "and a family of cats were worried.",
        "",
        "The old water tower on the roof had cracked",
        "and the whole building had no water!",
        "",
        '"Let us climb up there!" said Dada.',
        "The family patched the tank",
        "and water flowed to every floor again!",
    ],
    "prompt": PROMPT_PREFIX + (
        "A city rooftop with a cracked wooden water tower. The family in ironworker outfits "
        "(one boy: green work shirt with letter N and tiny hard hat, "
        "other boy: blue work shirt with letter E and tiny hard hat, "
        "Mama: work overalls applying sealant to the crack, focused on the repair, "
        "Dada: ironworker gear tightening bands around the tank looking at the bolts) "
        "repairs a cracked rooftop water tower. "
        "Pigeons perch on nearby rooftops watching. Cats sit on fire escapes. "
        "The boys hand up tools from a ladder. "
        "The puppy peers over the rooftop edge. City skyline behind, water dripping."
    ),
},
{
    "id": "skyscraper_02_build",
    "type": "story",
    "text": [
        "The cats purred and the pigeons cooed!",
        '"Water! Wonderful water!"',
        '"We know every rooftop -- we can help up high!"',
        "",
        '"Help us build a SKYSCRAPER!" said Neo.',
        "",
        "Pigeons carried bolts up to the highest floors!",
        "Cats balanced on beams like acrobats!",
        "Floor by floor, it rose into the clouds!",
    ],
    "prompt": PROMPT_PREFIX + (
        "A city construction site. The family builds a glass and steel skyscraper. "
        "Same ironworker outfits (boy in green shirt with N, boy in blue shirt with E). "
        "Pigeons carry bolts in their beaks flying up to the top floors. "
        "Cats walk perfectly balanced on steel I-beams high up. "
        "Dada welds a beam, face shield down looking at the sparks. "
        "Mama operates a crane from the cab, focused on the controls. "
        "The two boys ride a construction elevator going up, looking at each other excitedly. "
        "The puppy sits in a steel bucket being hoisted up. "
        "Half-built skyscraper reaching into the clouds, city skyline around."
    ),
},
{
    "id": "skyscraper_03_use",
    "type": "story",
    "text": [
        "The skyscraper touched the CLOUDS!",
        "It was the tallest building in the whole city!",
        "",
        "From the top floor, they could see EVERYTHING --",
        "mountains, the ocean, and even their house!",
        "",
        '"There is our house!" pointed Ender.',
        "Wall-E pressed his nose to the window!",
    ],
    "prompt": PROMPT_PREFIX + (
        "A gleaming glass skyscraper reaches into the clouds. "
        "On the rooftop observation deck with a panoramic view: "
        "the two boys look through coin-operated binoculars (green shirt N, blue shirt E). "
        "Mama points at something in the distance, looking at the horizon. "
        "Dada holds the boys' shoulders, looking where they look. "
        "The puppy presses his nose against the glass railing. "
        "Pigeons perch on the railing. Cats lounge on rooftop furniture. "
        "Far below: a vast city. In the distance: mountains and ocean. "
        "Sunset sky, clouds at eye level. Breathtaking view."
    ),
},
],

# ══════════════════════════════════════════════════════════════
# 18. UFO
# ══════════════════════════════════════════════════════════════
"ufo": [
{
    "id": "ufo_01_help",
    "type": "story",
    "text": [
        "In a desert canyon, a family of coyotes",
        "and a pair of roadrunners were stranded.",
        "",
        "A flash flood had washed away the only path",
        "out of the canyon!",
        "",
        '"We will build a new path!" said Mama.',
        "The family stacked flat rocks into steps",
        "all the way up the canyon wall!",
    ],
    "prompt": PROMPT_PREFIX + (
        "A red desert canyon with steep walls. The family in sci-fi explorer outfits "
        "(one boy: green space explorer suit with letter N and visor, "
        "other boy: blue space explorer suit with letter E and visor, "
        "Mama: silver explorer suit stacking flat rocks into steps, looking at the placement, "
        "Dada: silver explorer suit lifting a heavy flat rock, focused on placing it) "
        "builds a rock staircase up the canyon wall. "
        "Coyotes howl at the top of the cliff. Roadrunners pace at the bottom. "
        "The boys carry flat rocks together. "
        "The puppy scrambles up the first few steps. "
        "Red canyon walls, dry riverbed from flash flood, blue desert sky, mesa in distance."
    ),
},
{
    "id": "ufo_02_build",
    "type": "story",
    "text": [
        "The coyotes howled with happiness!",
        '"AWOOO! You saved us!"',
        '"We know the desert like nobody else!"',
        "",
        '"Help us build a UFO!" said Neo.',
        "",
        "Coyotes dug up shiny metals from the ground!",
        "Roadrunners ran circuits to test the power!",
        "Ender installed the anti-gravity drive!",
    ],
    "prompt": PROMPT_PREFIX + (
        "In the desert canyon, the family builds a flying saucer UFO. "
        "Same sci-fi outfits (boy in green suit with N, boy in blue suit with E). "
        "Coyotes dig up shiny metal ore from the desert ground. "
        "Roadrunners run in circles on a treadmill powering up the UFO with electricity crackling. "
        "Dada welds the curved hull plates, bent over his work. "
        "Mama wires the glowing control panel, focused on the circuits. "
        "The boy in green bolts on a dome window. "
        "The boy in blue installs a glowing blue anti-gravity drive core. "
        "The puppy sniffs at a glowing crystal. Half-built silver disc, desert canyon, night sky with stars."
    ),
},
{
    "id": "ufo_03_use",
    "type": "story",
    "text": [
        "BZZZZZZ! The UFO hummed and lifted off!",
        "It hovered, then ZOOMED straight up!",
        "",
        "They visited Mars, Jupiter's rings,",
        "and even said hi to some friendly aliens!",
        "",
        "The aliens waved back!",
        "Wall-E floated in the zero-gravity cabin!",
    ],
    "prompt": PROMPT_PREFIX + (
        "A silver flying saucer UFO zips through deep space past colorful planets. "
        "Through the dome window: the family inside the glowing cockpit. "
        "Dada steers with a holographic wheel, looking at the star chart. "
        "Mama scans planets on a screen, looking at the display. "
        "The two boys wave out the window at small cute friendly green aliens in another UFO "
        "(green suit N, blue suit E). "
        "The puppy floats upside down in zero gravity. "
        "Mars, Jupiter with rings, a nebula, friendly aliens waving from their own ship. "
        "Stars everywhere, cosmic colors, wonder and awe."
    ),
},
],

# ══════════════════════════════════════════════════════════════
# 19. MECH
# ══════════════════════════════════════════════════════════════
"mech": [
{
    "id": "mech_01_help",
    "type": "story",
    "text": [
        "At the volcano's base, a family of iguanas",
        "and some fire salamanders were frightened.",
        "",
        "Lava rocks had blocked their cool cave!",
        "The heat was unbearable!",
        "",
        '"We need to clear those rocks!" said Dada.',
        "The family used long poles to pry",
        "the scorching rocks away from the cave!",
    ],
    "prompt": PROMPT_PREFIX + (
        "At the base of a smoking volcano with lava rocks blocking a cave. The family in mech pilot outfits "
        "(one boy: green pilot suit with letter N and cooling vest, "
        "other boy: blue pilot suit with letter E and cooling vest, "
        "Mama: heat-resistant suit using a long iron pole to pry rocks, focused on the lever, "
        "Dada: heat suit with visor pushing rocks with a pole, looking at the obstacle) "
        "clears hot lava rocks from a cave entrance. "
        "Iguanas huddle behind them panting. Fire salamanders glow orange from the heat. "
        "The boys pour water on rocks to cool them. "
        "The puppy wears tiny heat booties. Steam rises, orange glow, volcanic landscape."
    ),
},
{
    "id": "mech_02_build",
    "type": "story",
    "text": [
        "The iguanas basked in the cool cave!",
        '"AMAZING! We can withstand any heat --',
        'let us help you build something BIG!"',
        "",
        '"Help us build a MECH!" said Ender.',
        "",
        "Iguanas welded in the hottest spots!",
        "Salamanders tested heat shields by sitting on them!",
        "Neo wired the rocket fists! Ender built the jet boots!",
    ],
    "prompt": PROMPT_PREFIX + (
        "At the volcano base, the family builds a giant humanoid mech robot suit. "
        "Same pilot outfits (boy in green suit with N, boy in blue suit with E). "
        "Iguanas weld in spots too hot for humans, unfazed by the heat. "
        "Fire salamanders sit on heat shield panels testing them. "
        "Dada bolts the giant legs together, looking up at the towering mech. "
        "Mama installs the cockpit control systems, focused on the wiring. "
        "The boy in green wires a rocket-powered fist. "
        "The boy in blue assembles jet boots. "
        "The puppy sits in the giant mech's open hand. "
        "Half-built mech as tall as a house, volcano smoking behind."
    ),
},
{
    "id": "mech_03_use",
    "type": "story",
    "text": [
        "STOMP! STOMP! The mech suit walked!",
        "It was as tall as a BUILDING!",
        "",
        "They stomped through the jungle,",
        "stepped over rivers,",
        "and high-fived the treetops!",
        "",
        "Wall-E sat on the mech's shoulder!",
    ],
    "prompt": PROMPT_PREFIX + (
        "A giant green and blue humanoid mech robot stomps through a lush jungle. "
        "It is as tall as the trees. Through the chest cockpit window: "
        "Dada and Mama at the controls, looking at the jungle ahead. "
        "The two boys control the arms from side stations (green suit N, blue suit E). "
        "The mech's hand high-fives a tree canopy, leaves scattering. "
        "The puppy sits on the mech's shoulder like a parrot. "
        "Iguanas ride on the mech's back. Salamanders glow on its feet. "
        "The mech steps over a river. Jungle birds scatter, monkeys swing away. Epic scale."
    ),
},
],

# ══════════════════════════════════════════════════════════════
# 20. SPACE STATION
# ══════════════════════════════════════════════════════════════
"spacestation": [
{
    "id": "spacestation_01_help",
    "type": "story",
    "text": [
        "Floating in orbit, a team of space dogs",
        "and robot helpers sent a distress signal.",
        "",
        "A solar panel had broken off",
        "and the station was losing power!",
        "",
        '"We are on our way!" said Mama.',
        "The family space-walked outside",
        "and bolted the panel back into place!",
    ],
    "prompt": PROMPT_PREFIX + (
        "Outer space with Earth below. A damaged space station floats in orbit. "
        "The family in EVA space suits does a spacewalk outside "
        "(one boy: green-striped space suit with letter N on helmet, "
        "other boy: blue-striped space suit with letter E on helmet, "
        "Mama: white space suit with tethers bolting a solar panel back, focused on the repair, "
        "Dada: white space suit holding the panel steady, looking at the bolts) "
        "repairs a broken solar panel on the station. "
        "Two dogs in tiny space suits float nearby with tools. A small robot helper assists. "
        "The boys float connected by tethers passing bolts. "
        "The puppy floats in a space suit bubble. Earth glows blue below, stars everywhere."
    ),
},
{
    "id": "spacestation_02_build",
    "type": "story",
    "text": [
        "The space dogs barked in zero gravity!",
        '"Power restored! You saved us!"',
        '"We know how to build in space!"',
        "",
        '"Help us build a SPACE STATION!" said Neo.',
        "",
        "Space dogs towed modules into position!",
        "Robot helpers welded in the vacuum!",
        "It was the biggest thing they EVER built!",
    ],
    "prompt": PROMPT_PREFIX + (
        "In orbit around Earth, the family builds an enormous space station. "
        "Same space suits (boy in green-striped suit with N, boy in blue-striped with E). "
        "Space dogs in tiny suits tow cylindrical modules with jet packs. "
        "Small robot helpers weld in the vacuum, blue sparks floating. "
        "Dada connects two modules, focused on aligning the docking ports. "
        "Mama installs a giant solar array, looking at the brackets. "
        "The two boys float together installing a window module. "
        "The puppy floats in a space bubble chasing a floating wrench. "
        "Half-built station with solar panels, Earth below, stars. Grand scale."
    ),
},
{
    "id": "spacestation_03_use",
    "type": "story",
    "text": [
        "The space station was INCREDIBLE!",
        "A garden dome, a zero-gravity playground,",
        "and windows to watch Earth spin below!",
        "",
        "Neo and Ender did somersaults in mid-air!",
        "Everyone floated and laughed!",
        "",
        "It was their GREATEST build ever!",
    ],
    "prompt": PROMPT_PREFIX + (
        "Inside an enormous space station with a glass dome showing Earth and stars outside. "
        "A garden dome with floating plants and water globes. "
        "The two boys somersault in zero gravity laughing (green suit N, blue suit E). "
        "Mama tends floating garden plants, looking at a tomato. "
        "Dada looks through a giant window at Earth spinning below, pointing something out. "
        "Space dogs do flips. Robot helpers serve floating food globes. "
        "The puppy chases a water bubble. "
        "Earth through the dome window, sunrise in space, solar panels outside. "
        "The most amazing thing they ever built. Awe-inspiring."
    ),
},
],

}
