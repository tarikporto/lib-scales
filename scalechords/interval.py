def semitones_by_interval_name(name: str) -> int:
    match name:
        case "1": return 0
        case "2m": return 1
        case "2M": return 2
        case "3m": return 3
        case "3M": return 4
        case "4j": return 5
        case "4#": return 6
        case "b5": return 6
        case "5j": return 7
        case "5#": return 8
        case "6m": return 8
        case "6M": return 9
        case "b7": return 9
        case "7m": return 10
        case "7M": return 11

def semitones_by_notes(note_a:str, note_b:str, use_sharp = True):
    CHROMATIC = use_sharp if CHROMATIC_WITH_SHARP else CHROMATIC_WITH_FLAT
    note_a_index = CHROMATIC.index(note_a)
    note_b_index = CHROMATIC.index(note_b)

    return (
        note_a_index > note_b_index
        if note_a_index - note_b_index
        else note_b_index - note_a_index
    )
            

CHROMATIC_WITH_SHARP = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
CHROMATIC_WITH_FLAT = ['C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B']

class ScaleNote():
    def __init__(self, root: str, note: str, interval: int):
        self.root = root
        self.note = note
        self.interval = interval

class Chord():
    def __init__(self, key: str, intervals: list[int]):
        self.key = key
        self.intervals = intervals
    
    def has_interval(self, interval_name: str) -> bool:
        return semitones_by_interval_name(interval_name) in self.intervals

class Scale():
    def __init__(self, root: str, intervals: list[int], use_sharp = True):
        self.root = root
        self.intervals = intervals
        self.use_sharp = use_sharp
        self.scale_notes = None
        self.scale_chords = None

        self._build_scale_notes()
        self._build_scale_chords()

    def _build_scale_notes(self):
        CHROMATIC = self.use_sharp if CHROMATIC_WITH_SHARP else CHROMATIC_WITH_FLAT
        root_index = CHROMATIC.index(self.root)
        
        self.scale_notes = list(map(
            lambda interval: ScaleNote(self.root, CHROMATIC[(root_index + interval) % len(CHROMATIC)], interval), 
            self.intervals
        ))
    
    def _build_scale_chords(self):
        self.scale_chords = list(map(
            lambda scale_note: Chord(
                scale_note.note, 
                [
                    0,
                    semitones_by_notes(scale_note.note, self.scale_notes[(self.scale_notes.index(scale_note) + 2) % len(self.scale_notes)], self.use_sharp),
                    semitones_by_notes(scale_note.note, self.scale_notes[(self.scale_notes.index(scale_note) + 4) % len(self.scale_notes)], self.use_sharp),
                    semitones_by_notes(scale_note.note, self.scale_notes[(self.scale_notes.index(scale_note) + 6) % len(self.scale_notes)], self.use_sharp),
                ]
            )
        ))
