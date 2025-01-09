import random

buzz = (
    'continuous testing', 'continuous integration',
    'continuous deployment', 'continuous improvement', 'devops'
)

adjectives = (
    'complete', 'modern', 'self-service', 'integrated', 'end-to-end'
)

adverbs = (
    'remarkably', 'enormously', 'substantially',
    'significantly', 'seriously'
)

verbs = ('accelerates', 'improves', 'enhances', 'revamps', 'boosts')


def sample(collection, n=1):
    """Select a random sample from a list."""
    result = random.sample(collection, n)
    if n == 1:
        return result[0]
    return result


def generate_buzz():
    """Generate a random buzz phrase."""
    buzz_terms = sample(buzz, 2)
    phrase = ' '.join([
        sample(adjectives),
        buzz_terms[0],
        sample(adverbs),
        sample(verbs),
        buzz_terms[1]
    ])
    return phrase.title()


if __name__ == "__main__":
    print(generate_buzz())
