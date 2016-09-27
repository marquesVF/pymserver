import os
from pydub import AudioSegment
from mutagen.easyid3 import EasyID3

class Converter():
    def __init__(self, source_type, output_path, output_type, bitrate):
        self.source_type = source_type
        self.output_path = output_path
        self.output_type = output_type
        self.bitrate = bitrate


    '''
        @source_paths is a list containing paths for all the files selected to be converted
    '''
    def convert(self, source_paths):
        for music_path in source_paths:
            if (self.source_type == "mp3"):
                music_stream = AudioSegment.from_mp3(music_path)
            # checking either it's needed to create the folders' structure
            music_info = EasyID3(music_path)
            title = str(music_info["title"][0])
            artist = str(music_info["artist"][0])
            album = str(music_info["album"][0])
            year = str()
            track = str()
            genre = str()
            date = str()
            description = str()
            output_music_path = str(self.output_path+"/"+music_info["artist"][0]+"/"+music_info["album"][0])
            if not os.path.isdir(output_music_path):
                os.makedirs(output_music_path)
            music_stream.export(str(output_music_path+"/"+music_info["title"][0]+"."+self.output_type), format="mp3", bitrate=self.bitrate)



    '''
        @file_structure store informations about the music and gonna be used to store the resulting audio files
                        into folders that represents artist, album and music name.
    '''
    # def getPathFromFolder(self, source_path):
    #     file_structure = dict()
    #     for folder_name, subfolders, file_names in os.walk(source_path):
    #         for file_name in file_names:
    #             song_path = folder_name+file_name
    #             if(self.source_type == "mp3"):
    #                 song_stream = AudioSegment.from_mp3(song_path)
    #             # checking either it's needed to create the folders' structure
    #             song_info =
    #             song_output_path = self.output_path+
    #             if(os.path.isdir()):


