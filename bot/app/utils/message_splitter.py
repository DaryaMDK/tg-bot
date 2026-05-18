MAX_MESSAGE_LENGTH = 4000


def split_text(text: str, max_length: int = MAX_MESSAGE_LENGTH) -> list[str]:
    chunks = []

    while len(text) > max_length:
        split_index = text.rfind("\n", 0, max_length)

        if split_index == -1:
            split_index = max_length

        chunks.append(text[:split_index])
        text = text[split_index:].strip()

    chunks.append(text)

    return chunks
