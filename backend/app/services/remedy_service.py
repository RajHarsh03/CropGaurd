from typing import TypedDict, List


class DiseaseInfo(TypedDict):
    display_name: str
    plant: str
    disease: str
    description: str
    symptoms: List[str]
    causes: str
    remedies: List[str]
    prevention: List[str]
    severity: str  # low | medium | high


DISEASE_DATABASE: dict[str, DiseaseInfo] = {
    "Pepper__bell___Bacterial_spot": {
        "display_name": "Bell Pepper – Bacterial Spot",
        "plant": "Bell Pepper",
        "disease": "Bacterial Spot",
        "description": (
            "Bacterial spot is caused by Xanthomonas species and is one of the most "
            "destructive diseases of pepper. It results in significant defoliation and "
            "fruit damage, especially under warm, wet conditions."
        ),
        "symptoms": [
            "Small, water-soaked circular spots on leaves",
            "Spots turn dark brown with yellow halos",
            "Premature leaf drop (defoliation)",
            "Raised, scabby lesions on fruit",
            "Spots may merge forming irregular blotches",
        ],
        "causes": "Xanthomonas euvesicatoria bacteria, spread by rain splash and infected seeds",
        "remedies": [
            "Apply copper-based bactericides (copper hydroxide or copper sulfate) every 7–10 days",
            "Use streptomycin sprays in early infection stages",
            "Remove and destroy heavily infected plant material",
            "Apply fixed copper sprays combined with mancozeb fungicide",
        ],
        "prevention": [
            "Use certified disease-free seeds and transplants",
            "Avoid overhead irrigation; use drip irrigation instead",
            "Maintain proper plant spacing for air circulation",
            "Rotate crops — avoid planting peppers or tomatoes in the same field for 2–3 years",
            "Apply reflective mulches to reduce aphid/vector populations",
        ],
        "severity": "high",
    },
    "Pepper__bell___healthy": {
        "display_name": "Bell Pepper – Healthy",
        "plant": "Bell Pepper",
        "disease": "Healthy",
        "description": (
            "Your bell pepper plant appears healthy with no visible disease symptoms. "
            "Continue your current care routine to maintain plant vitality."
        ),
        "symptoms": [
            "Vibrant green, glossy leaves",
            "No spots, lesions, or discoloration",
            "Firm, well-shaped fruit",
            "Robust stem and branching structure",
        ],
        "causes": "N/A – plant is healthy",
        "remedies": ["No treatment required"],
        "prevention": [
            "Maintain regular fertilization with balanced NPK",
            "Water consistently at soil level",
            "Monitor weekly for early signs of pests or disease",
            "Keep weeds removed around the plant base",
        ],
        "severity": "low",
    },
    "Potato___Early_blight": {
        "display_name": "Potato – Early Blight",
        "plant": "Potato",
        "disease": "Early Blight",
        "description": (
            "Early blight is caused by the fungus Alternaria solani. It primarily affects "
            "older leaves and can significantly reduce yields if not controlled. The disease "
            "thrives in warm temperatures with periods of wetness."
        ),
        "symptoms": [
            "Dark brown to black circular spots with concentric ring patterns (target-board appearance)",
            "Yellow (chlorotic) halo surrounding lesions",
            "Lesions first appear on older, lower leaves",
            "Severe cases cause premature defoliation",
            "Sunken, dark lesions can appear on tubers",
        ],
        "causes": "Alternaria solani fungus; favored by warm (24–29°C), humid conditions",
        "remedies": [
            "Apply chlorothalonil (Daconil) fungicide every 7–10 days",
            "Use mancozeb or azoxystrobin-based fungicides",
            "Apply copper-based fungicides as protectant",
            "Remove infected lower leaves immediately",
            "Use systemic fungicides like propiconazole for moderate-to-severe infections",
        ],
        "prevention": [
            "Use certified disease-free seed potatoes",
            "Maintain adequate plant nutrition (especially nitrogen and potassium)",
            "Rotate crops — avoid solanaceous crops for 2–3 years",
            "Avoid excessive leaf wetness; irrigate in the morning",
            "Space plants adequately to improve air circulation",
        ],
        "severity": "medium",
    },
    "Potato___Late_blight": {
        "display_name": "Potato – Late Blight",
        "plant": "Potato",
        "disease": "Late Blight",
        "description": (
            "Late blight, caused by Phytophthora infestans, is one of the most devastating "
            "plant diseases in history (responsible for the Irish Famine). It can destroy an "
            "entire crop within days under favorable cool, moist conditions."
        ),
        "symptoms": [
            "Irregular, water-soaked pale green to brown lesions on leaves",
            "White, cottony mold on leaf undersides in humid conditions",
            "Lesions rapidly turn brown-black and papery",
            "Brown rot extends into the petiole and stem",
            "Infected tubers show reddish-brown, granular rot",
        ],
        "causes": "Phytophthora infestans (water mold); thrives in cool (10–25°C), wet weather",
        "remedies": [
            "Apply metalaxyl or mefenoxam (systemic oomycide) immediately upon detection",
            "Spray chlorothalonil or mancozeb as protective fungicide",
            "Use cymoxanil + mancozeb tank mixture for dual action",
            "Haulm destruction (kill vines) 2 weeks before harvest to prevent tuber infection",
            "Treat seed potatoes with fungicide before planting",
        ],
        "prevention": [
            "Plant resistant varieties (e.g., Sarpo Mira, Defender)",
            "Monitor weather forecasts and apply preventive sprays before rain events",
            "Destroy all crop debris and volunteer plants after harvest",
            "Ensure proper earthing-up to protect tubers",
            "Never store tubers showing any signs of infection",
        ],
        "severity": "high",
    },
    "Potato___healthy": {
        "display_name": "Potato – Healthy",
        "plant": "Potato",
        "disease": "Healthy",
        "description": (
            "Your potato plant looks healthy! No disease symptoms are detected. "
            "Continue monitoring and maintaining good agricultural practices."
        ),
        "symptoms": [
            "Deep green, fully expanded leaves",
            "No spots, mold, or lesions visible",
            "Strong, upright stems",
            "Normal tuber development underground",
        ],
        "causes": "N/A – plant is healthy",
        "remedies": ["No treatment required"],
        "prevention": [
            "Maintain soil pH between 5.0–6.5",
            "Ensure adequate drainage to prevent waterlogging",
            "Scout weekly for early blight, late blight, and aphid infestations",
            "Apply preventive fungicide sprays during high-risk weather periods",
        ],
        "severity": "low",
    },
    "Tomato_Bacterial_spot": {
        "display_name": "Tomato – Bacterial Spot",
        "plant": "Tomato",
        "disease": "Bacterial Spot",
        "description": (
            "Tomato bacterial spot is caused by four species of Xanthomonas and affects "
            "leaves, stems, and fruit. It is highly destructive in warm, rainy seasons "
            "and can cause significant economic losses."
        ),
        "symptoms": [
            "Small, water-soaked spots (1–3 mm) on leaves turning dark brown",
            "Yellow halos around lesions on leaves",
            "Spots may coalesce causing leaf blight",
            "Small, raised, scab-like spots on green fruit",
            "Fruit spots become irregular, brown, and sunken as fruit matures",
        ],
        "causes": "Xanthomonas species bacteria; spread via infected seeds, transplants, rain, and insects",
        "remedies": [
            "Spray copper hydroxide + mancozeb mixture every 5–7 days",
            "Apply acibenzolar-S-methyl (Actigard) as a plant activator",
            "Use bactericides containing fixed copper at first sign of disease",
            "Remove and bag infected plant debris",
        ],
        "prevention": [
            "Purchase and plant only disease-free certified transplants",
            "Use drip irrigation instead of overhead watering",
            "Disinfect tools between plants with 10% bleach solution",
            "Avoid working in the garden when plants are wet",
            "Implement 2-year crop rotation with non-solanaceous crops",
        ],
        "severity": "high",
    },
    "Tomato_Early_blight": {
        "display_name": "Tomato – Early Blight",
        "plant": "Tomato",
        "disease": "Early Blight",
        "description": (
            "Early blight in tomatoes, caused by Alternaria solani, begins on the oldest "
            "leaves and progresses upward. It is a common fungal disease that weakens the "
            "plant and reduces fruit yield and quality."
        ),
        "symptoms": [
            "Dark brown spots with concentric rings on lower/older leaves",
            "Yellow area surrounding lesions",
            "Progressive defoliation from bottom upward",
            "Dark, leathery lesions at the stem end of fruit",
            "Stem lesions are dark, sunken, and dry",
        ],
        "causes": "Alternaria solani fungus; spreads by wind, rain, and contaminated tools",
        "remedies": [
            "Apply chlorothalonil-based fungicide (e.g., Daconil) every 7 days",
            "Use azoxystrobin (Quadris) or pyraclostrobin (Cabrio) for systemic control",
            "Apply mancozeb as a protective spray before infection",
            "Remove and destroy lower infected leaves",
        ],
        "prevention": [
            "Mulch around the base to prevent soil splash",
            "Stake and cage plants to improve airflow",
            "Water at ground level in the morning",
            "Apply preventive fungicide sprays in wet seasons",
            "Rotate crops every 2–3 years",
        ],
        "severity": "medium",
    },
    "Tomato_Late_blight": {
        "display_name": "Tomato – Late Blight",
        "plant": "Tomato",
        "disease": "Late Blight",
        "description": (
            "Tomato late blight is caused by Phytophthora infestans and is extremely "
            "aggressive. The pathogen can infect all above-ground parts of the plant and "
            "quickly kills entire plants if untreated."
        ),
        "symptoms": [
            "Large, irregular, greasy-looking grayish-green to dark brown spots on leaves",
            "White, downy fungal growth on undersides of leaves in humid conditions",
            "Brown to black lesions on stems and petioles",
            "Firm, brown, rough-surfaced spots on fruit",
            "Entire plant may collapse and die rapidly",
        ],
        "causes": "Phytophthora infestans; spread by wind and rain, favored by cool, wet weather",
        "remedies": [
            "Apply metalaxyl-M (Ridomil Gold) at first symptoms",
            "Spray dimethomorph (Acrobat) or cymoxanil as curative treatment",
            "Use chlorothalonil or mancozeb as protective barrier sprays",
            "Remove and bag all infected plant material",
            "Apply fungicides every 5–7 days during favorable disease weather",
        ],
        "prevention": [
            "Plant resistant tomato varieties (e.g., Mountain Magic, Defiant)",
            "Avoid planting near potato fields",
            "Monitor disease forecasting services (e.g., BlightCast)",
            "Ensure excellent air circulation through pruning and staking",
            "Never compost infected plant material",
        ],
        "severity": "high",
    },
    "Tomato_Leaf_Mold": {
        "display_name": "Tomato – Leaf Mold",
        "plant": "Tomato",
        "disease": "Leaf Mold",
        "description": (
            "Tomato leaf mold is caused by Passalora fulva (formerly Fulvia fulva). "
            "It primarily occurs in greenhouse or high-humidity environments. While it "
            "rarely kills plants outright, severe infections reduce yield significantly."
        ),
        "symptoms": [
            "Pale greenish-yellow spots on upper leaf surface",
            "Olive-green to grayish-brown velvety mold on leaf undersides",
            "Leaves curl, wither, and drop",
            "Can affect blossoms, causing blossom drop",
            "Fruit infection causes black rot at stem end",
        ],
        "causes": "Passalora fulva fungus; thrives in high humidity (>85%) and moderate temperatures",
        "remedies": [
            "Apply chlorothalonil (Bravo) or mancozeb fungicide immediately",
            "Use fungicides containing copper octanoate",
            "Remove and destroy affected leaves",
            "Apply potassium bicarbonate as organic option",
        ],
        "prevention": [
            "Reduce humidity in greenhouses using ventilation fans",
            "Avoid wetting foliage when watering",
            "Space plants adequately for air circulation",
            "Apply fungicide preventively when conditions favor disease",
            "Use resistant varieties (many modern hybrids have Cf resistance genes)",
        ],
        "severity": "medium",
    },
    "Tomato_Septoria_leaf_spot": {
        "display_name": "Tomato – Septoria Leaf Spot",
        "plant": "Tomato",
        "disease": "Septoria Leaf Spot",
        "description": (
            "Septoria leaf spot is caused by the fungus Septoria lycopersici. It is one of "
            "the most common and destructive diseases of tomato foliage. The disease progresses "
            "upward from older leaves and can completely defoliate the plant."
        ),
        "symptoms": [
            "Small, circular spots (3–6mm) with dark brown borders and grayish-white centers",
            "Tiny dark specks (pycnidia) visible in center of spots",
            "Yellowing of affected tissue",
            "Progressive defoliation from lower leaves upward",
            "Rarely infects fruit directly",
        ],
        "causes": "Septoria lycopersici fungus; spreads by rain splash and wind from infected debris",
        "remedies": [
            "Apply chlorothalonil (Daconil) every 7–10 days during wet weather",
            "Use mancozeb or copper-based fungicide sprays",
            "Apply azoxystrobin (Quadris) for systemic protection",
            "Remove and destroy infected lower leaves promptly",
        ],
        "prevention": [
            "Mulch soil around plants to prevent soil splash",
            "Avoid overhead irrigation",
            "Remove all plant debris at end of season",
            "Maintain 2–3 year crop rotation",
            "Stake plants to keep foliage off ground",
        ],
        "severity": "medium",
    },
    "Tomato_Spider_mites_Two_spotted_spider_mite": {
        "display_name": "Tomato – Two-Spotted Spider Mite",
        "plant": "Tomato",
        "disease": "Two-Spotted Spider Mite Infestation",
        "description": (
            "Two-spotted spider mites (Tetranychus urticae) are tiny arachnids that suck "
            "plant cell contents, causing stippled, bronzed foliage. Infestations worsen "
            "rapidly under hot, dry conditions."
        ),
        "symptoms": [
            "Fine webbing on leaf undersides and between stems",
            "Tiny pale stippling/speckles on leaf upper surface",
            "Leaves turning bronze, yellow, or silver in color",
            "Premature leaf drop in severe cases",
            "Visible mites (tiny, 0.5mm, yellow-green with two dark spots) on leaf undersides",
        ],
        "causes": "Tetranychus urticae mites; proliferate in hot, dry, dusty conditions",
        "remedies": [
            "Apply insecticidal soap spray (2% solution) directly to leaf undersides",
            "Use neem oil (2%) or rosemary oil sprays as organic miticide",
            "Apply abamectin (Agrimek) or bifenazate (Acramite) for chemical control",
            "Release predatory mites (Phytoseiulus persimilis) for biological control",
            "Use strong water spray to dislodge mites from leaves",
        ],
        "prevention": [
            "Maintain adequate plant moisture (stressed plants are more susceptible)",
            "Avoid excessive nitrogen fertilization which stimulates mite reproduction",
            "Avoid broad-spectrum pesticides that kill natural predators",
            "Monitor weekly using a 10x hand lens on leaf undersides",
            "Keep dust down around plant areas",
        ],
        "severity": "medium",
    },
    "Tomato__Target_Spot": {
        "display_name": "Tomato – Target Spot",
        "plant": "Tomato",
        "disease": "Target Spot",
        "description": (
            "Target spot is caused by Corynespora cassiicola. It affects leaves, petioles, "
            "stems, and fruit. The characteristic concentric ring pattern resembles a shooting "
            "target, giving the disease its common name."
        ),
        "symptoms": [
            "Brown circular lesions with distinctive concentric ring (target-board) pattern",
            "Lesions may have yellow halos",
            "Small, circular, dark brown to black spots on young fruit",
            "Fruit spots can become sunken and lead to rot",
            "Severe defoliation in humid conditions",
        ],
        "causes": "Corynespora cassiicola fungus; favored by high humidity and warm temperatures",
        "remedies": [
            "Apply chlorothalonil or mancozeb fungicide at 7–10 day intervals",
            "Use fluxapyroxad (Merivon) or pyraclostrobin for more effective control",
            "Remove infected leaves and destroy them",
        ],
        "prevention": [
            "Improve air circulation through pruning lower leaves",
            "Avoid overhead irrigation",
            "Remove crop debris after harvest",
            "Apply preventive fungicides before symptoms appear in high-risk conditions",
        ],
        "severity": "medium",
    },
    "Tomato__Tomato_YellowLeaf__Curl_Virus": {
        "display_name": "Tomato – Yellow Leaf Curl Virus",
        "plant": "Tomato",
        "disease": "Yellow Leaf Curl Virus (TYLCV)",
        "description": (
            "Tomato Yellow Leaf Curl Virus (TYLCV) is transmitted by the silverleaf "
            "whitefly (Bemisia tabaci). It is one of the most damaging tomato viruses "
            "worldwide, causing severe yield losses with no chemical cure once infected."
        ),
        "symptoms": [
            "Yellowing (chlorosis) and upward curling of young leaves",
            "Leaves become small, thick, and leathery",
            "Severe stunting of infected plants",
            "Flowers drop before fruit set",
            "Very little or no fruit production in heavily infected plants",
        ],
        "causes": "Begomovirus (TYLCV) transmitted exclusively by silverleaf whitefly (Bemisia tabaci)",
        "remedies": [
            "There is no cure once a plant is infected",
            "Remove and immediately destroy infected plants to prevent spread",
            "Apply imidacloprid or thiamethoxam insecticide to control whitefly vectors",
            "Use reflective mulches to repel whiteflies",
            "Apply insecticidal soap or neem oil to reduce whitefly populations",
        ],
        "prevention": [
            "Plant TYLCV-resistant/tolerant varieties (e.g., TY-resistant hybrids)",
            "Use fine mesh insect netting (50-mesh) to exclude whiteflies",
            "Install yellow sticky traps to monitor whitefly populations",
            "Eliminate weed hosts around the field",
            "Apply systemic insecticides at transplanting for early whitefly control",
        ],
        "severity": "high",
    },
    "Tomato__Tomato_mosaic_virus": {
        "display_name": "Tomato – Mosaic Virus",
        "plant": "Tomato",
        "disease": "Tomato Mosaic Virus (ToMV)",
        "description": (
            "Tomato Mosaic Virus (ToMV) is a highly stable virus that can survive in "
            "soil and on tools for years. It is mechanically transmitted and can infect "
            "plants at any growth stage, causing mottling and reduced fruit quality."
        ),
        "symptoms": [
            "Mosaic pattern of light and dark green areas on leaves",
            "Leaf distortion, puckering, and curling",
            "Stunted plant growth",
            "Fruit may show internal browning (brown wall disease)",
            "Uneven ripening of fruit",
        ],
        "causes": "Tobamovirus; transmitted through sap contact (mechanical transmission), seed, and soil",
        "remedies": [
            "No chemical cure exists for viral infections",
            "Remove and destroy infected plants immediately",
            "Disinfect tools with 10% bleach or 70% alcohol between plants",
            "Wash hands thoroughly before handling healthy plants",
        ],
        "prevention": [
            "Use certified virus-free seeds or treat seeds with trisodium phosphate (10% TSP)",
            "Plant ToMV-resistant varieties",
            "Disinfect stakes, cages, and tools before use",
            "Do not use tobacco products while handling plants (TMV reservoir)",
            "Control aphids which can spread the virus",
        ],
        "severity": "high",
    },
    "Tomato_healthy": {
        "display_name": "Tomato – Healthy",
        "plant": "Tomato",
        "disease": "Healthy",
        "description": (
            "Your tomato plant appears to be in excellent health. No disease or pest "
            "symptoms are detected. Maintain your current practices for optimal yield."
        ),
        "symptoms": [
            "Lush, dark green leaves with no spots or discoloration",
            "Strong stem and normal internodal spacing",
            "Abundant flower clusters",
            "Firm, evenly colored fruit development",
        ],
        "causes": "N/A – plant is healthy",
        "remedies": ["No treatment required"],
        "prevention": [
            "Continue regular watering at soil level",
            "Maintain fertilization schedule (higher potassium during fruiting)",
            "Scout weekly for whiteflies, aphids, and early disease signs",
            "Prune suckers for indeterminate varieties to maintain airflow",
        ],
        "severity": "low",
    },
}


def get_disease_info(class_name: str) -> DiseaseInfo:
    if class_name in DISEASE_DATABASE:
        return DISEASE_DATABASE[class_name]
    return {
        "display_name": class_name.replace("_", " ").replace("__", " – "),
        "plant": "Unknown",
        "disease": "Unknown",
        "description": "Disease information not available in the database.",
        "symptoms": ["Please consult a plant pathologist for accurate diagnosis."],
        "causes": "Unknown",
        "remedies": ["Consult your local agricultural extension service."],
        "prevention": ["Follow general good agricultural practices."],
        "severity": "medium",
    }
