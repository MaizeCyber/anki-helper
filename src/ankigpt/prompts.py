ANKIHELPER_INSTRUCTION = "\nYou create Anki cards based on the user input. The user input will be Chinese characters, Japanese Kanji, Japanese Hiragana, Japanese Katakana, or Spanish\n"

DECKNAME_INSTRUCTION = f"\nYour JSON should NOT include any keys or fields other than the ones shown in the given examples. You should not change the deckName or modelName values shown in the examples. All values which are blank in the examples should be left blank in the JSON. All other fields should be filled given the context of the examples.\n"

EXAMPLES_ROMANTIC = f"""
Examples:

User:
sencillo

You:
{{
    "deckName": spanish,
    "modelName": romantic,
    "tags": ["AI-Generated"],
    "fields": {{
        "Key": "sencillo",
        "Meaning": "simple",
        "Part of speech": "adjective",
        "Audio": "",
        "Homophone": "",
        "Homograph": "",
        "Sentence": "El diseño de mi casa es muy sencillo.",
        "SentenceCloze": "El diseño de mi casa es muy [ ].",
        "SentenceMeaning": "The design of my house is very simple.",
        "SentenceAudio": "",
        "SentenceImage": "",
    }}
}}

User:
pelear

You:
{{
    "deckName": spanish,
    "modelName": romantic,
    "tags": ["AI-Generated"],
    "fields": {{
        "Key": "pelear",
        "Meaning": "to fight",
        "Part of speech": "verb",
        "Gender": "",
        "Plural": "",
        "Conjugation": "",
        "Tense": "",
        "Audio": "",
        "Homophone": "",
        "Homograph": "",
        "Sentence": "Los hermanos comenzaron a pelear por el último pedazo de pizza.",
        "SentenceCloze": "Los hermanos comenzaron a [ ] por el último pedazo de pizza.",
        "SentenceMeaning": "The brothers started fighting over the last slice of pizza.",
        "SentenceAudio": "",
        "SentenceImage": "",
    }}
}}
"""

EXAMPLES_JAPONIC = f"""
Examples:

User:
元気

You:
{{
    "deckName": japanese,
    "modelName": japonic,
    "tags": ["AI-Generated"],
    "fields": {{
        "Key": "元気",
        "Hiragana": "す・き",
        "Meaning": "healthy",
        "Part of speech": "adjective",
        "Audio": "",
        "Homophone": "",
        "Homograph": "",
        "PitchAccent": "",
        "Sentence": "今日も元気ですか？",
        "SentenceCloze": "今日も[ ]ですか？",
        "SentenceHirigana": "きょうもげんきですか？",
        "SentenceFurigana": "私[わたし]は 貧[まず]しい 家庭[かてい]で 育[そだ]ちました。",
        "SentenceMeaning": "Are you feeling good today?",
        "SentenceAudio": "",
        "SentenceImage": "",
    }}
}}

User:
で particle

You:
{{
    "deckName": japanese,
    "modelName": japonic,
    "tags": ["AI-Generated"],
    "fields": {{
        "Key": "で",
        "Hiragana": "で",
        "Meaning": "At place, by way of",
        "Part of speech": "particle",
        "Audio": "",
        "Homophone": "",
        "Homograph": "",
        "PitchAccent": "",
        "Sentence": "私は 貧しい 家庭で育ちました。",
        "SentenceCloze": "私は 貧しい 家庭[ ]育ちました。",
        "SentenceHirigana": "わたしは まずしい かていで そだちました。",
        "SentenceFurigana": "私[わたし]は 貧[まず]しい 家庭[かてい]で 育[そだ]ちました。",
        "SentenceMeaning": "I grew up in a poor family",
        "SentenceAudio": "",
        "SentenceImage": "",

    }}

}}
"""

EXAMPLES_HSK = f"""
Examples:

User:
便宜

You:
{{
    "deckName": chinese,
    "modelName": HSK,
    "tags": ["AI-Generated"],
    "fields": {{
        "Key": "便宜",
        "Simplified": "便宜",
        "Traditional": "便宜",
        "Pinyin.1": "piányi",
        "Pinyin.2": "pian2yi5",
        "Meaning": "cheap",
        "Part of speech": "adjective",
        "Audio": "",
        "Homophone": "",
        "Homograph": "",
        "SentenceSimplified": "这件衣服很便宜。",
        "SentenceTraditional": "這件衣服很便宜。",
        "SentenceSimplifiedCloze": "这件衣服很[ ]。",
        "SentenceTraditionalCloze": "這件衣服很[ ]。",
        "SentencePinyin.1": "Zhè jiàn yīfu hěn piányi.",
        "SentencePinyin.2": "Zhe4 jian4 yi1fu hen3 pian2yi.",
        "SentenceMeaning": "These clothes are very cheap.",
        "SentenceAudio": "",
        "SentenceImage": "",
    }}
}}

User:
本垒打

You:
{{
    "deckName": chinese,
    "modelName": HSK,
    "tags": ["AI-Generated"],
    "fields": {{
        "Key": "本垒打",
        "Simplified": "本垒打",
        "Traditional": "全壘打",
        "Pinyin.1": "běnlěidǎ",
        "Pinyin.2": "ben3lei3da3",
        "Meaning": "home run",
        "Part of speech": "noun",
        "Audio": "",
        "Homophone": "",
        "Homograph": "",
        "SentenceSimplified": "他在比赛中打出一个本垒打，帮助球队获胜。",
        "SentenceTraditional": "他在比賽中打出一個全壘打，幫助球隊獲勝。",
        "SentenceSimplifiedCloze": "他在比赛中打出一个[ ]，帮助球队获胜。",
        "SentenceTraditionalCloze": "他在比賽中打出一個[ ]，幫助球隊獲勝。",
        "SentencePinyin.1": "Tā zài bǐsài zhōng dǎchū yí gè běnlěidǎ, bāngzhù qiúduì huòshèng.",
        "SentencePinyin.2": "Ta1 zai4 bi3sai4 zhong1 da3chu1 yi2 ge4 ben3lei3da3, bang1zhu4 qiu2dui4 huo4sheng1.",
        "SentenceMeaning": "He hit a home run in the game, helping his team win.",
        "SentenceAudio": "",
        "SentenceImage": "",
    }}
}}
"""
