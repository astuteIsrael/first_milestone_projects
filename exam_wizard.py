questions = [
    {
        "question": "Explain the process of photosynthesis",
        "keywords": {"photosynthesis": 2, "light energy": 1, "chemical energy": 1, "chloroplasts": 2, "chlorophyll": 1, "carbon dioxide": 1, "water": 1, "glucose": 1, "oxygen": 1, "ATP": 1}
    },
    {
        "question": "Describe the stages of the water cycle",
        "keywords": {"water cycle": 2, "evaporation": 1, "condensation": 1, "precipitation": 1, "infiltration": 1, "runoff": 1, "transpiration": 1, "water vapor": 1, "clouds": 1, "groundwater": 1}
    },
    {
        "question": "What are the causes and effects of global warming?",
        "keywords": {"global warming": 2, "greenhouse gases": 1, "carbon dioxide": 1, "methane": 1, "climate change": 1, "sea level rise": 1, "melting ice": 1, "deforestation": 1, "fossil fuels": 1, "renewable energy": 1}
    },
    {
        "question": "Explain how DNA replication occurs in cells",
        "keywords": {"DNA replication": 2, "nucleotides": 1, "DNA polymerase": 1, "helicase": 1, "replication fork": 1, "leading strand": 1, "lagging strand": 1, "Okazaki fragments": 1, "semi-conservative": 1, "template strand": 1}
    },
    {
        "question": "What is the theory of evolution by natural selection?",
        "keywords": {"evolution": 2, "natural selection": 2, "Charles Darwin": 1, "adaptation": 1, "survival of the fittest": 1, "variation": 1, "mutation": 1, "species": 1, "environment": 1, "selection pressure": 1}
    },
    {
        "question": "Describe the structure and function of the human heart",
        "keywords": {"human heart": 2, "atrium": 1, "ventricle": 1, "valves": 1, "arteries": 1, "veins": 1, "aorta": 1, "circulation": 1, "oxygenated blood": 1, "deoxygenated blood": 1, "heartbeat": 1}
    },
    {
        "question": "What is the difference between renewable and non-renewable energy?",
        "keywords": {"renewable energy": 2, "non-renewable energy": 2, "fossil fuels": 1, "solar energy": 1, "wind energy": 1, "hydropower": 1, "coal": 1, "oil": 1, "natural gas": 1, "sustainability": 1}
    },
    {
        "question": "Explain the significance of the Industrial Revolution",
        "keywords": {"Industrial Revolution": 2, "steam engine": 1, "manufacturing": 1, "factories": 1, "urbanization": 1, "economic growth": 1, "innovation": 1, "industrialization": 1, "textile industry": 1, "transportation": 1}
    },
    {
        "question": "Explain the process of cellular respiration",
        "keywords": {"cellular respiration": 2, "glucose": 1, "oxygen": 1, "mitochondria": 2, "ATP": 1, "glycolysis": 1, "Krebs cycle": 1, "electron transport chain": 1, "energy": 1, "carbon dioxide": 1, "water": 1}
    }
]

total_score = 0

# scores = []

# for question in questions:
#     for keyword in question["keywords"]:
#         scores.append(question["keywords"][keyword])

# print(sum(scores))

scores = [question["keywords"][keyword] for question in questions for keyword in question["keywords"]]
max_score = sum(scores)


# numbers = [1, 2, 3]
# inner_numbers = [5, 6, 7]
# numbers_copy = []
# for num in numbers:
#     for inner_num in inner_numbers:
#         numbers_copy.append((num, inner_num))
# print(numbers_copy)


# numbers = [1, 2, 3]
# inner_numbers = [5, 6, 7]
# numbers_copy = [(num, inner_num) for inner_num in inner_numbers for num in numbers]
# print(numbers_copy)

# numbers = [1, 2, 3]
# inner_numbers = [5, 6, 7]
# numbers_copy = [(num, inner_num) for num in numbers for inner_num in inner_numbers]
# print(numbers_copy)


# print(questions[question]["keywords"]["ATP"])

for question in questions:
    answer = input("Enter your answer: ").lower().strip()
    for keyword in question["keywords"]:
        kw, score = question["keywords"]
        if keyword.lower() in answer:
            total_score += question["keywords"][keyword]

print(f"Total Score: {total_score} out of {max_score} points")
