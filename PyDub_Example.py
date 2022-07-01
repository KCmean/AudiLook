from pydub import AudioSegment

sound = AudioSegment.from_mp3(  "Addresss/of/the/file/to/be/edited")

# len() and slicing are in milliseconds
halfway_point = len(sound) / 2
second_half = sound[halfway_point:]

# Concatenation is just adding
second_half_3_times = second_half + second_half + second_half

# writing mp3 files is a one liner
second_half_3_times.export("Address/of/the/new/file", format="mp3")