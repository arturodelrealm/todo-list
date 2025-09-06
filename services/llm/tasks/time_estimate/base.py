class TimeEstimateBase:
    OPTIONS = [
        '1 h',
        '2-4 h',
        '1 d',
        '2-3 d',
        '4-5 d',
        '2 w',
        '3-4 w',
        '1-2 m',
        '3-6 m',
        '+6 m',
    ]

    PROMPT_FORMAT = '{title}\n{description}'

    def __init__(self, config=None):
        self.config = config or {}

    def _get_prompt(self, title, description):
        return self.PROMPT_FORMAT.format(
            title=title,
            description=description
        )

    def estimate(self, task_title, task_description):
        prompt = self._get_prompt(task_title, task_description)
        return self._estimate(prompt)

    def _estimate(self, prompt):
        raise NotImplementedError
