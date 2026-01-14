# plant_database.py

PLANT_DISEASE_INFO = {
    # --- APPLE ---
    'Apple___Apple_scab': {
        'name': 'Apple Scab',
        'description': 'A severe fungal disease (Venturia inaequalis) that causes dark, scabby lesions on leaves and fruit. It overwinters in fallen leaves and releases spores during spring rains.',
        'urgency_level': 'Medium',
        'urgency_text': 'Treat immediately to prevent fruit deformation and future yield loss.',
        'symptoms': [
            'Olive-green velvety spots on leaves that turn black.',
            'Yellowing and premature dropping of leaves.',
            'Brown, corky, scabby spots on the fruit surface.',
            'Fruit may crack or become misshapen.'
        ],
        'natural_control': [
            'Apply a baking soda solution (1 tbsp per gallon of water).',
            'Spray Neem oil or compost tea during early fungal development.',
            'Rake and destroy all fallen leaves in autumn to remove overwintering spores.',
            'Use bio-fungicides containing Bacillus subtilis.'
        ],
        'chemical_control': [
            'Fungicides containing Myclobutanil or Captan.',
            'Difenoconazole sprays applied at the "green tip" stage.',
            'Copper-based sprays before blossoming.'
        ],
        'prevention': [
            'Prune trees to open the canopy and improve airflow (rapid drying reduces infection).',
            'Plant resistant varieties like Honeycrisp, Liberty, or Enterprise.',
            'Avoid overhead irrigation.'
        ],
        'integrated_farming': 'Gardenland Model: Horticulture + Duckery + Apiary. Ducks forage for pests and snails in the orchard floor, reducing biological vectors, while bees ensure high pollination rates for the apple crop.',
        'ifs_link': '/static/IFS/IFS_Systems/garden-mixed.html'
    },
    'Apple___Black_rot': {
        'name': 'Black Rot (Apple)',
        'description': 'A fungal disease (Botryosphaeria obtusa) causing leaf spots, limb cankers, and fruit rot. The fruit rot phase is often called "Botryosphaeria rot".',
        'urgency_level': 'High',
        'urgency_text': 'Can destroy the entire fruit harvest and damage tree structure.',
        'symptoms': [
            'Small, purple spots on leaves that enlarge into circular "frog-eye" spots.',
            'Fruit develops a firm, brown rot that turns black.',
            'Infected fruit shrivels into hard "mummies" that stay on the tree.',
            'Reddish-brown cankers on branches and limbs.'
        ],
        'natural_control': [
            'Rigorous sanitation: Remove all mummified fruit from the tree and ground.',
            'Prune out cankers 15cm below the visible damage.',
            'Burn pruned wood immediately (do not compost).'
        ],
        'chemical_control': [
            'Thiophanate-methyl fungicides.',
            'Captan or Sulfur sprays applied during the growing season.'
        ],
        'prevention': [
            'Keep trees healthy to resist infection (water during drought).',
            'Protect trees from mechanical injury and insect damage.',
            'Remove dead wood and brush piles from the orchard.'
        ],
        'integrated_farming': 'Gardenland Model: Horticulture + Poultry. Chickens can be grazed under apple trees (in rotation) to eat larvae and break disease cycles in leaf litter, while their manure enriches the soil phosphorus.',
        'ifs_link': '/static/IFS/IFS_Systems/garden-mixed.html'
    },
    'Apple___Cedar_apple_rust': {
        'name': 'Cedar Apple Rust',
        'description': 'A fungal disease (Gymnosporangium juniperi-virginianae) that requires two hosts: apple trees and Eastern red cedar (juniper) trees. It cannot spread from apple to apple.',
        'urgency_level': 'Medium',
        'urgency_text': 'Mainly cosmetic on leaves, but severe defoliation weakens the tree.',
        'symptoms': [
            'Bright yellow-orange "oil spots" on the upper surface of apple leaves.',
            'Tiny black fungal bodies appear in the spots.',
            'Tube-like structures on the underside of leaves release spores.',
            'Premature leaf drop.'
        ],
        'natural_control': [
            'Remove Eastern Red Cedar trees within a 1-mile radius if possible.',
            'Prune "cedar galls" (brown, brain-like growths) from nearby junipers in late winter.'
        ],
        'chemical_control': [
            'Fungicides containing Myclobutanil (Immunox).',
            'Mancozeb or Sulfur sprays applied when blossoms start to show pink.'
        ],
        'prevention': [
            'Plant rust-resistant apple varieties (e.g., Red Delicious, McIntosh).',
            'Monitor nearby landscaping for juniper infections.'
        ],
        'integrated_farming': 'Gardenland Model: Horticulture + Apiary. Since this disease is airborne between hosts, livestock integration focuses on maintaining general tree health via bee pollination and manure fertilization from nearby cattle/goats.',
        'ifs_link': '/static/IFS/IFS_Systems/garden-mixed.html'
    },
    'Apple___healthy': {
        'name': 'Healthy Apple Tree',
        'description': 'The tree is vigorous with glossy green leaves, no spots, and smooth bark.',
        'urgency_level': 'Low',
        'urgency_text': 'Maintain current care routine.',
        'symptoms': [],
        'natural_control': [],
        'chemical_control': [],
        'prevention': [
            'Mulch around the base to retain moisture.',
            'Annual pruning in late winter.',
            'Balanced fertilization in early spring.'
        ],
        'integrated_farming': 'Gardenland Model: High-Density Orchard + Sheep. Sheep can graze the alleyways between apple rows (managed grazing) to control weeds and reduce mowing costs.',
        'ifs_link': '/static/IFS/IFS_Systems/garden-mixed.html'
    },

    # --- BACKGROUND ---
    'Background_without_leaves': {
        'name': 'No Plant Detected',
        'description': ' The image does not appear to contain a recognized plant leaf.',
        'urgency_level': 'Low',
        'urgency_text': 'Please upload a clear image of a plant leaf.',
        'symptoms': [],
        'natural_control': [],
        'chemical_control': [],
        'prevention': [],
        'integrated_farming': 'N/A',
        'ifs_link': '/static/IFS/IFS_Home.html'
    },

    # --- BLUEBERRY ---
    'Blueberry___healthy': {
        'name': 'Healthy Blueberry',
        'description': 'The bush is thriving with dark green foliage. Blueberries require acidic soil (pH 4.5-5.5).',
        'urgency_level': 'Low',
        'urgency_text': 'Good condition.',
        'symptoms': [],
        'natural_control': [],
        'chemical_control': [],
        'prevention': [
            'Test soil pH annually; add elemental sulfur if needed.',
            'Mulch with pine needles or sawdust to maintain acidity.'
        ],
        'integrated_farming': 'Gardenland Model: Horticulture + Apiculture. Blueberries are highly dependent on bees for fruit set. Keeping hives nearby increases yield by up to 30%.',
        'ifs_link': '/static/IFS/IFS_Systems/garden-mixed.html'
    },

    # --- CHERRY ---
    'Cherry___Powdery_mildew': {
        'name': 'Powdery Mildew (Cherry)',
        'description': 'A fungal disease (Podosphaera clandestina) that covers leaves and fruit in white fungal growth, typically in warm, dry climates with high humidity.',
        'urgency_level': 'Medium',
        'urgency_text': 'Can deform fruit and stunt shoot growth.',
        'symptoms': [
            'Circular white, powdery patches on leaves.',
            'Leaves curl upward and become distorted.',
            'White felt-like patches on fruit.',
            'Stunted twig growth.'
        ],
        'natural_control': [
            'Spray with a mixture of milk and water (1:10 ratio).',
            'Potassium bicarbonate sprays.',
            'Neem oil or horticultural oil.'
        ],
        'chemical_control': [
            'Sulfur dust or wettable sulfur.',
            'Myclobutanil or Fenbuconazole fungicides.'
        ],
        'prevention': [
            'Prune to improve light penetration and air circulation.',
            'Avoid nitrogen fertilizers late in the season (promotes susceptible tender growth).',
            'Water at the base to avoid wetting foliage.'
        ],
        'integrated_farming': 'Gardenland Model: Horticulture + Vermiculture. Use cherry orchard leaf litter in worm farms to create vermicompost, which is then returned to the trees as a nutrient-rich top dressing.',
        'ifs_link': '/static/IFS/IFS_Systems/garden-mixed.html'
    },
    'Cherry___healthy': {
        'name': 'Healthy Cherry',
        'description': 'Vibrant green leaves without curling or spots.',
        'urgency_level': 'Low',
        'urgency_text': 'Maintain monitoring.',
        'symptoms': [],
        'natural_control': [],
        'chemical_control': [],
        'prevention': ['Regular watering during fruit formation.', 'Bird netting to protect harvest.'],
        'integrated_farming': 'Gardenland Model: Orchard + Poultry. Chickens act as natural pest control for the cherry fruit fly larvae in the soil.',
        'ifs_link': '/static/IFS/IFS_Systems/garden-mixed.html'
    },

    # --- CORN ---
    'Corn___Cercospora_leaf_spot Gray_leaf_spot': {
        'name': 'Gray Leaf Spot (Corn)',
        'description': 'A major fungal disease (Cercospora zeae-maydis) favored by warm, humid weather. It limits the plant\'s photosynthetic capacity.',
        'urgency_level': 'High',
        'urgency_text': 'Can severely reduce yield if it reaches the ear leaf during tasseling.',
        'symptoms': [
            'Small, pinpoint lesions surrounded by yellow halos.',
            'Lesions elongate into rectangular, gray-to-tan spots running parallel to leaf veins.',
            'Entire leaves may turn gray and die (blight).'
        ],
        'natural_control': [
            'Deep tillage to bury infected crop residue (accelerates decomposition).',
            'Crop rotation (at least 2 years without corn).'
        ],
        'chemical_control': [
            'Fungicides with Azoxystrobin or Pyraclostrobin.',
            'Propiconazole applied at the onset of disease.'
        ],
        'prevention': [
            'Plant resistant corn hybrids (most effective method).',
            'Manage residue in no-till systems carefully.'
        ],
        'integrated_farming': 'Dryland/Wetland Model: Agri-Silviculture (Crops + Trees). Trees act as windbreaks to reduce spore spread, while leaf litter adds organic matter.',
        'ifs_link': '/static/IFS/IFS_Systems/dryland-agrisilvi.html'
    },
    'Corn___Common_rust': {
        'name': 'Common Rust (Corn)',
        'description': 'A fungal disease (Puccinia sorghi) that produces rust-colored pustules. Spores are carried by wind over long distances.',
        'urgency_level': 'Medium',
        'urgency_text': 'Usually manageable unless infection starts very early.',
        'symptoms': [
            'Small, circular to elongated brown/cinnamon pustules on both leaf surfaces.',
            'Pustules turn black as the plant matures.',
            'Yellowing of leaf tissue around pustules.'
        ],
        'natural_control': [
            'Usually not economically viable to treat organically in large fields.',
            'Early planting allows corn to mature before rust spores arrive.'
        ],
        'chemical_control': [
            'Fungicides containing Mancozeb or Strobilurins.',
            'Apply only if pustules cover significant leaf area before grain fill.'
        ],
        'prevention': [
            'Plant resistant hybrids.',
            'Avoid excessive nitrogen which promotes soft, susceptible growth.'
        ],
        'integrated_farming': 'Dryland Model: Silvi-Pasture (Crop + Goat). Corn residue (stover) can be grazed by cattle or goats after harvest.',
        'ifs_link': '/static/IFS/IFS_Systems/dryland-goat.html'
    },
    'Corn___Northern_Leaf_Blight': {
        'name': 'Northern Leaf Blight',
        'description': 'Caused by the fungus Exserohilum turcicum. It thrives in cool, wet weather.',
        'urgency_level': 'High',
        'urgency_text': 'Can cause significant grain loss if upper leaves are infected early.',
        'symptoms': [
            'Long, cigar-shaped lesions (1 to 6 inches) on leaves.',
            'Lesions are gray-green eventually turning tan.',
            ' lesions may coalesce, killing whole leaves.'
        ],
        'natural_control': [
            'Bio-fungicides containing Trichoderma harzianum.',
            'Crop rotation with non-host crops (soybeans, alfalfa).'
        ],
        'chemical_control': [
            'Mancozeb, Propiconazole, or Pyraclostrobin.',
            'Spray at the first sign of disease.'
        ],
        'prevention': [
            'Tillage to reduce surface residue.',
            'Plant resistant varieties.'
        ],
        'integrated_farming': 'Dryland Model: Crop + Goat + Agroforestry. Goats can eat the corn stover. The manure is composted and used. Trees provide microclimate regulation.',
        'ifs_link': '/static/IFS/IFS_Systems/dryland-agrisilvi.html'
    },
    'Corn___healthy': {
        'name': 'Healthy Corn',
        'description': 'Strong stalks, deep green leaves, and developing ears.',
        'urgency_level': 'Low',
        'urgency_text': 'Monitor for pests like armyworms.',
        'symptoms': [],
        'natural_control': [],
        'chemical_control': [],
        'prevention': ['Maintain consistent irrigation during silking.'],
        'integrated_farming': 'Wetland/Dryland: Crop + Dairy. The "Zero Waste" model where corn feeds cattle, cattle dung generates biogas for energy, and slurry fertilizes the next corn crop.',
        'ifs_link': '/static/IFS/IFS_Systems/garden-dairy.html'
    },

    # --- GRAPE ---
    'Grape___Black_rot': {
        'name': 'Black Rot (Grape)',
        'description': 'A devastating fungal disease (Guignardia bidwellii) attacking fruit and leaves. It thrives in warm, humid weather.',
        'urgency_level': 'High',
        'urgency_text': 'Can cause 100% crop loss if untreated.',
        'symptoms': [
            'Small yellowish spots on leaves with dark borders.',
            'Fruit turns brown, soft, then shrivels into hard black "mummies".',
            'Tiny black fungal dots (pycnidia) on fruit and leaf spots.'
        ],
        'natural_control': [
            'Sanitation is key: Remove all mummies from vines and ground in winter.',
            'Proper canopy management to increase airflow.'
        ],
        'chemical_control': [
            'Mancozeb or Ziram.',
            'Myclobutanil (Immunox) is highly effective.'
        ],
        'prevention': [
            'Plant in sunny locations with good air drainage.',
            'Weed control under vines to reduce humidity.'
        ],
        'integrated_farming': 'Gardenland Model: Vineyard + Geese/Ducks. "Weeder Geese" manage grass and weeds without herbicides, reducing humidity around the vines which prevents Black Rot.',
        'ifs_link': '/static/IFS/IFS_Systems/garden-mixed.html'
    },
    'Grape___Esca_(Black_Measles)': {
        'name': 'Esca (Black Measles)',
        'description': 'A complex fungal trunk disease affecting older vines. It blocks water transport and releases toxins.',
        'urgency_level': 'Critical',
        'urgency_text': 'No cure. Incurable and fatal to the vine part.',
        'symptoms': [
            'Leaves show "tiger stripes" (yellow/red distinct bands between veins).',
            'Small dark spots on berries ("measles").',
            'Sudden wilting of whole branches (apoplexy).'
        ],
        'natural_control': [
            'Remove infected vines and burn them.',
            'Trunk renewal: Cut the trunk below the infected area and train a new sucker.'
        ],
        'chemical_control': [
            'Wound sealants (paint/paste) on pruning cuts to prevent infection.',
            'No chemical cures established infection.'
        ],
        'prevention': [
            'Disinfect pruning tools between vines.',
            'Avoid pruning during wet weather.'
        ],
        'integrated_farming': 'Gardenland Model: Horticulture + Biogas. Use removed infected wood (carefully handled) or other farm waste for biogas generation, ensuring pathogens are destroyed by heat.',
        'ifs_link': '/static/IFS/IFS_Systems/garden-mixed.html'
    },
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': {
        'name': 'Isariopsis Leaf Spot',
        'description': 'Fungal disease causing spotting and premature defoliation, weakening the vine.',
        'urgency_level': 'Medium',
        'urgency_text': 'Reduces vine vigor and next year\'s yield.',
        'symptoms': [
            'Irregular reddish-brown spots on leaves.',
            'Fuzzy olive-brown fungal growth on the underside of spots.',
            'Leaves turn yellow and drop early.'
        ],
        'natural_control': [
            'Copper-based organic fungicides.',
            'Improve air circulation.'
        ],
        'chemical_control': [
            'Mancozeb spray.',
            'Chlorothalonil.'
        ],
        'prevention': [
            'Collect and burn fallen leaves.',
            'Dormant spray with Lime Sulfur.'
        ],
        'integrated_farming': 'Gardenland Model: Vineyard + Sheep. Sheep graze the vineyard floor in winter (when vines are dormant) to eat fallen leaves and weeds, reducing fungal carryover.',
        'ifs_link': '/static/IFS/IFS_Systems/garden-mixed.html'
    },
    'Grape___healthy': {
        'name': 'Healthy Grape Vine',
        'description': 'Vines are robust with green, intact leaves.',
        'urgency_level': 'Low',
        'urgency_text': 'Excellent.',
        'symptoms': [],
        'natural_control': [],
        'chemical_control': [],
        'prevention': ['Regular pruning and training.'],
        'integrated_farming': 'Gardenland Model: Vineyard + Agritourism. Healthy vineyards are ideal for integrating tourism, wine tasting, and selling byproduct jams/jellies.',
        'ifs_link': '/static/IFS/IFS_Systems/garden-mixed.html'
    },

    # --- ORANGE ---
    'Orange___Haunglongbing_(Citrus_greening)': {
        'name': 'Citrus Greening (HLB)',
        'description': 'A bacterial disease (Candidatus Liberibacter) spread by the Asian Citrus Psyllid. It blocks phloem, starving the roots.',
        'urgency_level': 'Critical',
        'urgency_text': 'Global threat to citrus. Trees usually die within 5 years.',
        'symptoms': [
            'Asymmetrical blotchy mottling (yellowing) on leaves.',
            'Yellow veins and corky veins.',
            'Fruit stays green at the bottom (greening) and tastes bitter/salty.',
            'Misshapen, lopsided fruit.'
        ],
        'natural_control': [
            'There is NO CURE. Infected trees must be removed.',
            'Release parasitic wasps (Tamarixia radiata) to control the psyllid vector.'
        ],
        'chemical_control': [
            'Systemic insecticides (Imidacloprid) to kill psyllids.',
            'Antibiotic injections (Oxytetracycline) can suppress symptoms but not cure.'
        ],
        'prevention': [
            'Use only certified disease-free nursery stock.',
            'Aggressive monitoring and control of psyllids.'
        ],
        'integrated_farming': 'Gardenland Model: Citrus + Apiculture. While battling greening, maintaining high biodiversity is key. Beehives support pollination of cover crops that attract beneficial insects (predators of psyllids).',
        'ifs_link': '/static/IFS/IFS_Systems/garden-mixed.html'
    },

    # --- PEACH ---
    'Peach___Bacterial_spot': {
        'name': 'Bacterial Spot (Peach)',
        'description': 'Caused by Xanthomonas campestris. It causes defoliation and pitted fruit.',
        'urgency_level': 'Medium',
        'urgency_text': 'Fruit becomes unmarketable.',
        'symptoms': [
            'Small, angular, water-soaked spots on leaves.',
            'Centers of spots fall out, leaving a "shot-hole" appearance.',
            'Cracks and pits on the fruit surface.',
            'Leaves turn yellow and drop.'
        ],
        'natural_control': [
            'Copper sprays (cautiously, as they can burn peach leaves).',
            'Bacteriophages (viruses that kill bacteria) specifically for Xanthomonas.'
        ],
        'chemical_control': [
            'Oxytetracycline (antibiotic) sprays (Mycoshield).',
            'Copper ammonium complex.'
        ],
        'prevention': [
            'Plant resistant varieties (e.g., Candor, Southern Pearl).',
            'Fertilize appropriately to maintain vigor but avoid excess nitrogen.'
        ],
        'integrated_farming': 'Gardenland Model: Horticulture + Poultry. Free-range chickens in the orchard help control plum curculio and other insect pests that create wounds where bacteria can enter.',
        'ifs_link': '/static/IFS/IFS_Systems/garden-mixed.html'
    },
    'Peach___healthy': {
        'name': 'Healthy Peach Tree',
        'description': 'Leaves are long, lanceolate, and green.',
        'urgency_level': 'Low',
        'urgency_text': 'Good health.',
        'symptoms': [],
        'natural_control': [],
        'chemical_control': [],
        'prevention': ['Dormant oil spray for scale insects.'],
        'integrated_farming': 'Gardenland Model: Horticulture + Apiary. Peaches are self-fertile but bees improve fruit size and quality.',
        'ifs_link': '/static/IFS/IFS_Systems/garden-mixed.html'
    },

    # --- PEPPER ---
    'Pepper,_bell___Bacterial_spot': {
        'name': 'Bacterial Spot (Pepper)',
        'description': 'A serious seed-borne bacterial disease spread by splashing water.',
        'urgency_level': 'High',
        'urgency_text': 'Spreads rapidly in wet seasons.',
        'symptoms': [
            'Small, water-soaked spots on leaves that turn brown/black.',
            'Spots often have a yellow halo.',
            'Raised, scab-like spots on the peppers.',
            'Leaf drop exposes fruit to sunscald.'
        ],
        'natural_control': [
            'Copper fungicides (OMRI listed).',
            'Remove infected plants immediately.',
            'Mulch to prevent soil splash.'
        ],
        'chemical_control': [
            'Fixed copper mixed with Mancozeb (more effective than copper alone).',
            'Agri-Strep (Streptomycin).'
        ],
        'prevention': [
            'Hot water seed treatment (122°F for 25 mins).',
            'Crop rotation (do not plant after tomato/potato).'
        ],
        'integrated_farming': 'Gardenland Model: Vegetable Crop + Vermicompost. Use vermicompost tea as a foliar spray; it has been shown to suppress bacterial spot severity.',
        'ifs_link': '/static/IFS/IFS_Systems/garden-dairy.html'
    },
    'Pepper,_bell___healthy': {
        'name': 'Healthy Bell Pepper',
        'description': 'Sturdy stems and glossy green leaves.',
        'urgency_level': 'Low',
        'urgency_text': 'Optimal.',
        'symptoms': [],
        'natural_control': [],
        'chemical_control': [],
        'prevention': ['Stake plants to keep fruit off the ground.'],
        'integrated_farming': 'Gardenland Model: Crop + Biogas. Pepper plant waste (post-harvest) is excellent for biogas digesters.',
        'ifs_link': '/static/IFS/IFS_Systems/garden-dairy.html'
    },

    # --- POTATO ---
    'Potato___Early_blight': {
        'name': 'Early Blight (Potato)',
        'description': 'Fungal disease (Alternaria solani) affecting older leaves first. It stresses the plant and reduces tuber size.',
        'urgency_level': 'Medium',
        'urgency_text': 'Manageable with good practices.',
        'symptoms': [
            'Dark brown spots with concentric rings (target board pattern).',
            'Yellowing of tissue around the spots.',
            'Lower leaves die and hang on the stem.'
        ],
        'natural_control': [
            'Maintain plant vigor with adequate nitrogen and phosphorus.',
            'Bacillus subtilis bio-fungicide.'
        ],
        'chemical_control': [
            'Chlorothalonil (Bravo).',
            'Mancozeb or Azoxystrobin.'
        ],
        'prevention': [
            'Crop rotation (3-4 years).',
            'Drip irrigation to keep leaves dry.'
        ],
        'integrated_farming': 'Dryland/Gardenland: Crop + Dairy. Potatoes have high nutrient demands; dairy manure (composted) provides the necessary bulk organic matter.',
        'ifs_link': '/static/IFS/IFS_Systems/garden-dairy.html'
    },
    'Potato___Late_blight': {
        'name': 'Late Blight (Potato)',
        'description': 'The historical famine-causing pathogen (Phytophthora infestans). It destroys foliage and rots tubers.',
        'urgency_level': 'Critical',
        'urgency_text': 'Immediate destruction of infected plants required. Extremely contagious.',
        'symptoms': [
            'Large, dark, water-soaked blotches on leaves.',
            'White fuzzy fungal growth on the underside in humid weather.',
            'Tubers have reddish-brown, granular rot under the skin.',
            'Putrid smell.'
        ],
        'natural_control': [
            'Copper fungicides (preventative only).',
            'Kill vines (burn/cut) 2 weeks before harvest to prevent tuber infection.'
        ],
        'chemical_control': [
            'Metalaxyl (often resistance issues).',
            'Cymoxanil or Dimethomorph.'
        ],
        'prevention': [
            'Eliminate "cull piles" (waste potatoes) where the fungus overwinters.',
            'Use certified seed potatoes.'
        ],
        'integrated_farming': 'Broader Integration: Livestock-Crop Mix (Pigs). Pigs can root out and eat leftover tubers after harvest (gleaning), removing volunteer potatoes that would otherwise harbor Late Blight.',
        'ifs_link': '/static/IFS/IFS_Systems/broader-livestock.html'
    },
    'Potato___healthy': {
        'name': 'Healthy Potato',
        'description': 'Bushy growth with no spots.',
        'urgency_level': 'Low',
        'urgency_text': 'Good.',
        'symptoms': [],
        'natural_control': [],
        'chemical_control': [],
        'prevention': ['Hilling soil around stems.'],
        'integrated_farming': 'Dryland Model: Crop + Agroforestry. Alley cropping with nitrogen-fixing trees improves soil fertility for potatoes.',
        'ifs_link': '/static/IFS/IFS_Systems/dryland-agrisilvi.html'
    },

    # --- RASPBERRY ---
    'Raspberry___healthy': {
        'name': 'Healthy Raspberry',
        'description': 'Canes are upright and leaves are green/silver underneath.',
        'urgency_level': 'Low',
        'urgency_text': 'Good.',
        'symptoms': [],
        'natural_control': [],
        'chemical_control': [],
        'prevention': ['Prune old canes after fruiting.'],
        'integrated_farming': 'Gardenland Model: Horticulture + Apiary. Raspberries are major nectar sources; integrating hives produces high-value raspberry honey.',
        'ifs_link': '/static/IFS/IFS_Systems/garden-mixed.html'
    },

    # --- SOYBEAN ---
    'Soybean___healthy': {
        'name': 'Healthy Soybean',
        'description': 'Legume crop with trifoliate leaves.',
        'urgency_level': 'Low',
        'urgency_text': 'Monitor for aphids.',
        'symptoms': [],
        'natural_control': [],
        'chemical_control': [],
        'prevention': [],
        'integrated_farming': 'Dryland Model: Silvi-Pasture (Crop + Cattle). Soybeans fix nitrogen. Following soy with a grass crop for cattle grazing utilizes this nitrogen efficiently.',
        'ifs_link': '/static/IFS/IFS_Systems/dryland-silvipasture.html'
    },

    # --- SQUASH ---
    'Squash___Powdery_mildew': {
        'name': 'Powdery Mildew (Squash)',
        'description': 'Extremely common fungal disease on cucurbits. It blocks sunlight, killing leaves.',
        'urgency_level': 'Medium',
        'urgency_text': 'Treat early to prolong harvest.',
        'symptoms': [
            'White, talcum-powder-like growth on upper and lower leaf surfaces.',
            'Leaves turn yellow and brown.',
            'Premature ripening/sunburn of fruit due to leaf loss.'
        ],
        'natural_control': [
            'Neem oil.',
            'Milk spray (40% milk, 60% water).',
            'Sulfur dust.'
        ],
        'chemical_control': [
            'Chlorothalonil.',
            'Myclobutanil.'
        ],
        'prevention': [
            'Plant resistant varieties (e.g., PM-resistant zucchini).',
            'Space plants widely for airflow.'
        ],
        'integrated_farming': 'Gardenland Model: Crop + Apiculture. Squash requires bees for pollination (male to female flowers). Without bees, fruit will abort.',
        'ifs_link': '/static/IFS/IFS_Systems/garden-mixed.html'
    },

    # --- STRAWBERRY ---
    'Strawberry___Leaf_scorch': {
        'name': 'Leaf Scorch (Strawberry)',
        'description': 'Fungal disease (Diplocarpon earliana). It gives plants a "burned" look.',
        'urgency_level': 'Medium',
        'urgency_text': 'Can kill plants if severe.',
        'symptoms': [
            'Irregular purple blotches on leaves.',
            'Centers of spots turn brown (not white like leaf spot).',
            'Leaves curl up and dry out (scorch).'
        ],
        'natural_control': [
            'Remove and burn infected leaves.',
            'Copper fungicide.'
        ],
        'chemical_control': [
            'Captan or Thiram.',
            'Syngenta Switch.'
        ],
        'prevention': [
            'Plant in well-draining soil.',
            'Renew strawberry beds every 3-4 years.'
        ],
        'integrated_farming': 'Gardenland Model: Horticulture + Rabbits. While rabbits are pests to strawberries, rabbit manure (cold manure) is one of the best fertilizers for strawberry beds if composted.',
        'ifs_link': '/static/IFS/IFS_Systems/garden-mixed.html'
    },
    'Strawberry___healthy': {
        'name': 'Healthy Strawberry',
        'description': 'Low growing rosette with trifoliate leaves.',
        'urgency_level': 'Low',
        'urgency_text': 'Good.',
        'symptoms': [],
        'natural_control': [],
        'chemical_control': [],
        'prevention': ['Mulch with straw to keep fruit clean.'],
        'integrated_farming': 'Gardenland Model: Horticulture + Apiary. Essential for well-shaped berries.',
        'ifs_link': '/static/IFS/IFS_Systems/garden-mixed.html'
    },

    # --- TOMATO ---
    'Tomato___Bacterial_spot': {
        'name': 'Bacterial Spot (Tomato)',
        'description': 'Xanthomonas bacteria cause this disease, thriving in warm (75-85°F), wet conditions.',
        'urgency_level': 'High',
        'urgency_text': 'Can severely damage fruit quality.',
        'symptoms': [
            'Small (1/8 inch) water-soaked spots on leaves.',
            'Spots turn dark brown/black and may fall out.',
            'Raised, scab-like spots on green fruit.',
            'Leaf yellowing and loss.'
        ],
        'natural_control': [
            'Copper-based bactericides.',
            'Avoid working in the garden when wet.',
            'Hot water seed treatment.'
        ],
        'chemical_control': [
            'Copper hydroxide + Mancozeb (tank mix).',
            'Streptomycin (agricultural grade).'
        ],
        'prevention': [
            'Use drip irrigation.',
            'Stake/cage plants to improve airflow.',
            'Rotate away from solanaceous crops for 2 years.'
        ],
        'integrated_farming': 'Gardenland Model: Crop + Biogas + Dairy. Tomato plant residue is acidic but can be mixed with dairy slurry for biogas production.',
        'ifs_link': '/static/IFS/IFS_Systems/garden-dairy.html'
    },
    'Tomato___Early_blight': {
        'name': 'Early Blight (Tomato)',
        'description': 'Alternaria solani fungus. The most common tomato disease.',
        'urgency_level': 'Medium',
        'urgency_text': 'Very common; treatable if caught early.',
        'symptoms': [
            'Brown spots with concentric rings ("bullseye") on lower leaves.',
            'Surrounding leaf tissue turns yellow.',
            'Stem cankers (dark, sunken spots).',
            'Fruit rot at the stem end.'
        ],
        'natural_control': [
            'Remove infected lower leaves (pruning).',
            'Apply mulch to prevent soil spores splashing onto leaves.',
            'Bicarbonate sprays.'
        ],
        'chemical_control': [
            'Chlorothalonil (Daconil).',
            'Mancozeb.'
        ],
        'prevention': [
            'Stake plants.',
            'Ensure adequate calcium and magnesium levels.'
        ],
        'integrated_farming': 'Broader Integration: Livestock-Crop (Poultry). Chickens can range in the tomato patch *after* harvest to eat pests and diseased fallen fruit.',
        'ifs_link': '/static/IFS/IFS_Systems/broader-livestock.html'
    },
    'Tomato___Late_blight': {
        'name': 'Late Blight (Tomato)',
        'description': 'Phytophthora infestans. Aggressive and destructive. Capable of killing plants in days.',
        'urgency_level': 'Critical',
        'urgency_text': 'Act immediately. Isolate and destroy plants.',
        'symptoms': [
            'Large, irregular gray-green patches on leaves.',
            'Patches turn brown and papery.',
            'White fuzzy mold ring around spots in humidity.',
            'Firm, dark brown, rough rot on fruit.'
        ],
        'natural_control': [
            'Pull and bag infected plants immediately.',
            'Copper fungicides as a preventative.'
        ],
        'chemical_control': [
            'Chlorothalonil (preventative).',
            'Propamocarb hydrochloride (curative).'
        ],
        'prevention': [
            'Avoid overhead watering completely.',
            'Plant "Mountain Magic" or "Defiant" (resistant varieties).'
        ],
        'integrated_farming': 'Broader Integration: Aquaculture-Agriculture (Aquaponics). In aquaponics, tomatoes thrive, and the controlled environment (greenhouse) prevents Late Blight spores from entering.',
        'ifs_link': '/static/IFS/IFS_Systems/broader-aqua.html'
    },
    'Tomato___Leaf_Mold': {
        'name': 'Leaf Mold',
        'description': 'Passalora fulva fungus. Common in greenhouses or high humidity.',
        'urgency_level': 'Medium',
        'urgency_text': 'Reduces yield but rarely kills the plant.',
        'symptoms': [
            'Pale green or yellow spots on the upper leaf surface.',
            'Olive-green or brown velvety mold on the underside.',
            'Leaves curl, wither, and drop.'
        ],
        'natural_control': [
            'Increase ventilation/spacing.',
            'Copper sprays.',
            'Neem oil.'
        ],
        'chemical_control': [
            'Chlorothalonil.',
            'Difenoconazole.'
        ],
        'prevention': [
            'Keep humidity below 85%.',
            'Use fans in greenhouses.'
        ],
        'integrated_farming': 'Broader Integration: Aquaculture-Agriculture (Aquaponics). Leaf mold is a greenhouse issue; integrating fish tanks provides heat mass and nutrients while requiring strict humidity control.',
        'ifs_link': '/static/IFS/IFS_Systems/broader-aqua.html'
    },
    'Tomato___Septoria_leaf_spot': {
        'name': 'Septoria Leaf Spot',
        'description': 'Septoria lycopersici fungus. Affects leaves, not fruit.',
        'urgency_level': 'Medium',
        'urgency_text': 'Causes defoliation, exposing fruit to sunscald.',
        'symptoms': [
            'Numerous small, circular spots (1/16 to 1/8 inch).',
            'Spots have dark margins and gray/white centers.',
            'Tiny black dots in the center of spots.',
            'Starts at bottom leaves and moves up.'
        ],
        'natural_control': [
            'Remove lower leaves.',
            'Copper fungicide.',
            'Mulch heavily.'
        ],
        'chemical_control': [
            'Chlorothalonil.',
            'Mancozeb.'
        ],
        'prevention': [
            'Sanitation: Remove all crop debris at end of season.',
            '3-year crop rotation.'
        ],
        'integrated_farming': 'Wetland Model: Crop + Mushroom. Spent tomato haulms (stems) can be composted and used as a substrate component for certain mushroom species.',
        'ifs_link': '/static/IFS/IFS_Systems/wetland-mushroom.html'
    },
    'Tomato___Spider_mites Two-spotted_spider_mite': {
        'name': 'Two-Spotted Spider Mite',
        'description': 'Tiny arachnids that suck plant sap. They thrive in hot, dry conditions.',
        'urgency_level': 'Medium',
        'urgency_text': 'Can explode in population rapidly.',
        'symptoms': [
            'Yellow or white stippling (tiny dots) on leaves.',
            'Fine webbing visible between leaves and stems.',
            'Leaves turn bronze/gray and brittle.'
        ],
        'natural_control': [
            'Strong stream of water to knock them off.',
            'Introduction of predatory mites (Phytoseiulus persimilis).',
            'Neem oil or insecticidal soap.'
        ],
        'chemical_control': [
            'Abamectin (Miticide).',
            'Bifenazate.'
        ],
        'prevention': [
            'Keep plants well-watered (mites hate humidity).',
            'Avoid broad-spectrum insecticides (they kill mite predators).'
        ],
        'integrated_farming': 'Gardenland Model: Horticulture + Mixed (Trap Cropping). Plant marigolds or dill nearby to attract predatory insects that eat mites.',
        'ifs_link': '/static/IFS/IFS_Systems/garden-mixed.html'
    },
    'Tomato___Target_Spot': {
        'name': 'Target Spot',
        'description': 'Corynespora cassiicola fungus. Similar to Early Blight but attacks fruit more aggressively.',
        'urgency_level': 'Medium',
        'urgency_text': 'Can ruin fruit marketability.',
        'symptoms': [
            'Brown-black lesions with subtle concentric rings.',
            'Lesions on fruit are sunken and firm.',
            'Leaf centers may crack and fall out.'
        ],
        'natural_control': [
            'Copper fungicides.',
            'Improve airflow.'
        ],
        'chemical_control': [
            'Azoxystrobin.',
            'Pyraclostrobin.'
        ],
        'prevention': [
            'Remove volunteer plants.',
            'Avoid wetting leaves.'
        ],
        'integrated_farming': 'Gardenland Model: Crop + Dairy. Similar to other tomato fungal issues, soil health is key. Composted dairy manure suppresses soil-borne phases of fungal pathogens.',
        'ifs_link': '/static/IFS/IFS_Systems/garden-dairy.html'
    },
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus': {
        'name': 'Yellow Leaf Curl Virus (TYLCV)',
        'description': 'A Begomovirus transmitted by Silverleaf Whiteflies. It halts fruit production.',
        'urgency_level': 'High',
        'urgency_text': 'Plants infected early will produce no fruit.',
        'symptoms': [
            'New leaves are small, curled upward (cup-shaped), and yellow (chlorotic) at edges.',
            'Plants become stunted/dwarfed.',
            'Flowers drop off.'
        ],
        'natural_control': [
            'Remove and bag infected plants immediately (virus source).',
            'Control whiteflies with sticky traps and Neem oil.',
            'Reflective silver mulch repels whiteflies.'
        ],
        'chemical_control': [
            'Imidacloprid (systemic) to control whitefly vector.',
            'Dinotefuran.'
        ],
        'prevention': [
            'Use virus-resistant varieties (look for "TY" on label).',
            'Weed control (nightshade weeds host the virus).'
        ],
        'integrated_farming': 'Gardenland Model: Crop + Dairy + Biogas. Integrated pest management within a dairy system helps reduce viral vectors.',
        'ifs_link': '/static/IFS/IFS_Systems/garden-dairy.html'
    },
    'Tomato___Tomato_mosaic_virus': {
        'name': 'Tomato Mosaic Virus (ToMV)',
        'description': 'A highly contagious virus (Tobamovirus). It is mechanically transmitted (tools, hands, tobacco products).',
        'urgency_level': 'High',
        'urgency_text': 'No cure. Permanent infection.',
        'symptoms': [
            'Light and dark green mottling (mosaic) on leaves.',
            'Fern-like or distorted leaves.',
            'Brown streaks on stems.',
            'Fruit ripens unevenly.'
        ],
        'natural_control': [
            'Remove infected plants.',
            'Dip tools in milk (the proteins in milk inactivate the virus) or bleach.'
        ],
        'chemical_control': [
            'None exist for viruses.'
        ],
        'prevention': [
            'Wash hands after smoking (tobacco carries the virus).',
            'Plant resistant varieties (look for "T" or "Tm" on label).'
        ],
        'integrated_farming': 'Gardenland Model: Strict Sanitation in Crop + Dairy systems. Ensure workers do not handle livestock/tobacco and then touch crops without sanitation.',
        'ifs_link': '/static/IFS/IFS_Systems/garden-dairy.html'
    },
    'Tomato___healthy': {
        'name': 'Healthy Tomato',
        'description': 'Vigorous growth, deep green leaves, no wilting.',
        'urgency_level': 'Low',
        'urgency_text': 'Keep up the good work.',
        'symptoms': [],
        'natural_control': [],
        'chemical_control': [],
        'prevention': ['Regular sucker pruning.'],
        'integrated_farming': 'Gardenland Model: Crop + Dairy + Biogas. Planting basil with tomatoes improves flavor and repels flies/mosquitoes.',
        'ifs_link': '/static/IFS/IFS_Systems/garden-dairy.html'
    },

    # --- DEFAULT ---
    'default': {
        'name': 'Unknown / Unclassified',
        'description': 'The specific disease could not be identified with high confidence.',
        'urgency_level': 'Low',
        'urgency_text': 'Consult a local agricultural extension office.',
        'symptoms': [],
        'natural_control': [],
        'chemical_control': [],
        'prevention': [],
        'integrated_farming': 'General IPM: Monitor crops weekly, identify pests accurately, and use control thresholds.',
        'ifs_link': '/static/IFS/IFS_Home.html'
    }
}
