# poetry_agents_system.py

class PoetAgent:
    def generate_poem(self, custom_poem=None):
        if custom_poem:
            return custom_poem.strip()
        return (
            "The night was cold, the moon hung high,\n"
            "I whispered dreams into the sky.\n"
            "My thoughts were drenched in silent rain,\n"
            "Each heartbeat echoed with my pain.\n\n"
            "A shadow danced along the wall,\n"
            "Recalling times I can't recall.\n"
            "My soul adrift in endless sea,\n"
            "Longing for what used to be."
        )


class LyricAnalystAgent:
    def analyze(self, poem):
        return (
            "🎵 **Lyric Analysis:**\n"
            "This is lyric poetry expressing deep personal emotions like sorrow and longing. "
            "Imagery like 'silent rain' and 'shadows' gives it a melancholic tone."
        )


class NarrativeAnalystAgent:
    def analyze(self, poem):
        return (
            "📖 **Narrative Analysis:**\n"
            "There are subtle story elements: a character reflecting on lost time, hinting at a past event. "
            "However, it lacks a full plot structure, so it's not primarily narrative poetry."
        )


class DramaticAnalystAgent:
    def analyze(self, poem):
        return (
            "🎭 **Dramatic Analysis:**\n"
            "The poem could be performed as a dramatic monologue. It has an introspective speaker, "
            "emotive tone, and theatrical potential suitable for stage delivery."
        )


class OrchestratorAgent:
    def __init__(self):
        self.poet_agent = PoetAgent()
        self.lyric_analyst = LyricAnalystAgent()
        self.narrative_analyst = NarrativeAnalystAgent()
        self.dramatic_analyst = DramaticAnalystAgent()

    def run(self, input_poem=None):
        poem = self.poet_agent.generate_poem(input_poem)
        lyric = self.lyric_analyst.analyze(poem)
        narrative = self.narrative_analyst.analyze(poem)
        dramatic = self.dramatic_analyst.analyze(poem)

        return {
            "Poem": poem,
            "Lyric Analysis": lyric,
            "Narrative Analysis": narrative,
            "Dramatic Analysis": dramatic
        }


# Run the full system
if __name__ == "__main__":
    orchestrator = OrchestratorAgent()

    # Optional: replace None with your own poem
    results = orchestrator.run(input_poem=None)

    for key, value in results.items():
        print(f"\n--- {key} ---\n{value}")
