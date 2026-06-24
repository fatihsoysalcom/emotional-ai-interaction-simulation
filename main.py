import random

def soulforge_ai_response(user_input):
    """
    Simulates an AI response that attempts to understand and react to user emotions
    (SoulForge approach) versus a purely rule-based response (Traditional AI).
    """
    user_input_lower = user_input.lower()

    # --- SoulForge: Attempting emotional understanding and connection ---
    # This section simulates a basic emotional intelligence model by looking for keywords.
    # In a real SoulForge system, this would involve sophisticated NLP and emotional AI models.

    # Keywords indicating positive sentiment in Turkish
    if any(keyword in user_input_lower for keyword in ["harika", "mutlu", "iyi hissediyorum", "güzel", "sevdim", "memnunum", "keyifliyim"]):
        # AI responds with empathy and positive reinforcement
        return random.choice([
            "Harika! Senin mutlu olman beni de sevindiriyor. Neler oluyor?",
            "Ne kadar güzel! Bu enerjini benimle paylaştığın için teşekkür ederim.",
            "Çok sevindim! Umarım günün de harika geçer."
        ])
    # Keywords indicating negative sentiment in Turkish
    elif any(keyword in user_input_lower for keyword in ["üzgünüm", "kötü hissediyorum", "canım sıkkın", "mutsuzum", "zorlanıyorum", "moralim bozuk", "sıkıldım"]):
        # AI responds with empathy and offers support
        return random.choice([
            "Üzgün olduğunu duyduğuma üzüldüm. Belki konuşmak iyi gelir mi?",
            "Anlıyorum, bazen böyle hissetmek normal. Yanındayım, istersen dinleyebilirim.",
            "Moralinin bozuk olmasına üzüldüm. Sana nasıl yardımcı olabilirim?"
        ])
    # Keywords indicating curiosity/questioning or seeking deeper interaction
    elif any(keyword in user_input_lower for keyword in ["merak ediyorum", "neden", "nasıl", "bilgi ver", "düşüncen ne", "ne dersin"]):
        # AI responds with an attempt to engage deeper or provide context
        return random.choice([
            "Bu ilginç bir soru. Biraz daha açar mısın, neyi merak ediyorsun?",
            "Konuyu daha detaylı inceleyebiliriz. Hangi konuda bilgi almak istersin?",
            "Bu konuda farklı bakış açıları var. Senin düşüncen ne?"
        ])
    # --- Traditional AI: Rule-based, task-oriented response ---
    # If no strong emotional cues are detected, the AI falls back to a more generic,
    # rule-based or factual response, typical of traditional chatbots.
    else:
        return random.choice([
            "Anladım. Başka ne hakkında konuşmak istersin?",
            "Bu konuda daha fazla bilgiye mi ihtiyacın var?",
            "Peki, başka bir konu hakkında konuşalım mı?",
            "Sana nasıl yardımcı olabilirim?"
        ])

if __name__ == "__main__":
    print("Merhaba! Ben SoulForge AI. Duygusal bağlar kurmaya çalışıyorum.")
    print("Çıkmak için 'çıkış' yazabilirsin.")

    while True:
        user_input = input("Sen: ")
        if user_input.lower() == 'çıkış':
            print("Görüşmek üzere!")
            break
        
        response = soulforge_ai_response(user_input)
        print(f"SoulForge AI: {response}")
