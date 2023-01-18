class Question:
    """Models each question item."""
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer