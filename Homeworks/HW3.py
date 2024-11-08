CHROMATIC_SCALE = (
    'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'
)

TONES_COUNT = 12
MINOR_THIRD_LEN = 3
MAJOR_THIRD_LEN = 4


class Tone:

    def __init__(self, tone_name):
        self.tone_name = tone_name

    def __str__(self):
        return self.tone_name

    def __eq__(self, other):
        return self.tone_name == other.tone_name

    def __ne__(self, other):
        return self.tone_name != other.tone_name

    def __add__(self, other):
        if isinstance(other, Tone):
            return Chord(self,other)
        elif isinstance(other, Interval):
            new_tone_idx = (CHROMATIC_SCALE.index(self.tone_name) + other.semitones_count) % TONES_COUNT
            return Tone(CHROMATIC_SCALE[new_tone_idx])

    def __sub__(self, other):
        if isinstance(other, Tone):
            self_idx = CHROMATIC_SCALE.index(self.tone_name)
            other_idx = CHROMATIC_SCALE.index(other.tone_name)
            interval_length = (self_idx - other_idx) % TONES_COUNT
            return Interval(interval_length)
        elif isinstance(other, Interval):
            new_tone_idx = (CHROMATIC_SCALE.index(self.tone_name) - other.semitones_count) % TONES_COUNT
            return Tone(CHROMATIC_SCALE[new_tone_idx])


class Interval:

    _INTERVAL_NAMES = (
        'unison', 'minor 2nd', 'major 2nd', 'minor 3rd', 'major 3rd',
        'perfect 4th', 'diminished 5th', 'perfect 5th', 'minor 6th',
        'major 6th', 'minor 7th', 'major 7th'
    )

    def __init__(self, semitones_count):
        self.semitones_count = semitones_count

    def __str__(self):
        return self._INTERVAL_NAMES[self.semitones_count % TONES_COUNT]

    def __add__(self, other):
        if isinstance(other, Tone):
            raise TypeError('Invalid operation')
        elif isinstance(other, Interval):
            new_count = (self.semitones_count + other.semitones_count)
            return Interval(new_count)

    def __sub__(self, other):
        if isinstance(other, Tone):
            raise TypeError('Invalid operation')

    def __neg__(self):
        return Interval(-self.semitones_count)


class Chord:

    def __init__(self, *tones):
        if not self._are_valid_tones(*tones):
            raise TypeError('Cannot have a chord made of only 1 unique tone')
        self.sorted_tones = self._sort_tones(*tones)

    @staticmethod
    def _are_valid_tones(*tones):
        tones_set = {str(tone) for tone in tones}
        return len(tones_set) > 1

    @staticmethod
    def _sort_tones(*tones):
        root = tones[0]
        sorted_tones = [root]
        end_idx = CHROMATIC_SCALE.index(str(root))
        iter_idx = (end_idx + 1) % TONES_COUNT

        while iter_idx != end_idx:
            current_tone = Tone(CHROMATIC_SCALE[iter_idx])
            if current_tone in tones and current_tone not in sorted_tones:
                sorted_tones.append(current_tone)
            iter_idx += 1
            iter_idx %= TONES_COUNT
        return sorted_tones

    def __str__(self):
        return '-'.join(str(tone) for tone in self.sorted_tones)

    def is_minor(self):
        root_idx = CHROMATIC_SCALE.index(str(self.sorted_tones[0]))
        end_tone_idx = (root_idx + MINOR_THIRD_LEN) % TONES_COUNT
        return Tone(CHROMATIC_SCALE[end_tone_idx]) in self.sorted_tones

    def is_major(self):
        root_idx =  CHROMATIC_SCALE.index(str(self.sorted_tones[0]))
        end_tone_idx = (root_idx + MAJOR_THIRD_LEN) % TONES_COUNT
        return Tone(CHROMATIC_SCALE[end_tone_idx]) in self.sorted_tones

    def is_power_chord(self):
        return not self.is_minor() and not self.is_major()

    def __add__(self, other):
        if isinstance(other, Tone):
            new_tones = self.sorted_tones + [other]
            return Chord(*new_tones)
        elif isinstance(other, Chord):
            new_tones = self.sorted_tones[:]
            new_tones.extend(other.sorted_tones)
            return Chord(*new_tones)

    def __sub__(self, other):
        if isinstance(other, Tone):
            if other not in self.sorted_tones:
                raise TypeError(f'Cannot remove tone {str(other)} from chord {str(self)}')
            new_tones = self.sorted_tones[:]
            new_tones.remove(other)
            return Chord(*new_tones)

    def transposed(self, interval):
        transpose = lambda tone : tone + interval
        transposed_tones  = list(map(transpose, self.sorted_tones))
        return Chord(*transposed_tones)
