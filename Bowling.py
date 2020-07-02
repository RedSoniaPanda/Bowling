class Bowling:
    _ROLL_PER_FRAME = 2
    _STRIKE_AND_SPARE_SCORE = 10

    def __init__(self):
        self.score = 0
        self._roll_per_frame = 2
        self._current_frame = 1
        self.game = {}

    def get_score(self):
        self._calculate_game_score()
        return self.score

    def num_balls_hit(self, num_balls):
        self._create_frames(num_balls)

    def _calculate_game_score(self):
        frame_keys = list(self.game.keys())
        for frame, rolls in self.game.items():
            if 9 in rolls and 1 in rolls:
                self.score += self._calculate_spare(frame, frame_keys)
            elif 10 in rolls:
                self.score += self._calculate_strike(frame, frame_keys)
            else:
                self.score += self._calculate_frame_score(rolls)

    @staticmethod
    def _calculate_frame_score(rolls):
        return rolls[0] + rolls[1]

    def _calculate_spare(self, frame, frame_keys):
        next_frame_key = frame_keys[frame_keys.index(frame) + 1]
        spare_score = self._STRIKE_AND_SPARE_SCORE + self.game[next_frame_key][0]
        return spare_score

    def _calculate_strike(self, frame, frame_keys):
        next_frame_key = frame_keys[frame_keys.index(frame) + 1]
        next_next_frame_key = frame_keys[frame_keys.index(frame) + 1]
        strike_score = self._STRIKE_AND_SPARE_SCORE + self.game[next_frame_key][0] + self.game[next_next_frame_key][1]
        return strike_score

    def _create_frames(self, num_balls):
        key = 'frame ' + str(self._current_frame)
        if key not in self.game:
            self.game[key] = []
        self.game[key].append(num_balls)
        if len(self.game[key]) is self._roll_per_frame:
            self._current_frame += 1
