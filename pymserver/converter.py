# -*- coding: utf-8 -*-
import os
from pydub import AudioSegment
from mutagen.easyid3 import EasyID3


def getPathsFromFolder(folder_path, extension):
    """
        @folder_path path to a folder containing all the desired audio files to be converted
        @extension audio file extension. For exemple '.mp3', '.ogg' etc
    """
    files = list()
    for folder_name, sub_folders, file_names in os.walk(folder_path):
        for file_name in file_names:
            ext = os.path.splitext(file_name)[-1].lower()
            if ext == "."+extension:
                files.append(folder_name+"/"+file_name)
    return files


class Converter():
    def __init__(self, source_type, output_path, output_type, bitrate):
        self.source_type = source_type
        self.output_path = output_path
        self.output_type = output_type
        self.bitrate = bitrate


    def convert(self, source_paths):
        """
            @source_paths is a list containing paths for all the files selected to be converted
        """
        for music_path in source_paths:
            if self.source_type == "mp3" and os.path.isfile(music_path):
                music_stream = AudioSegment.from_mp3(music_path)
            if self.source_type == "ogg" and os.path.isfile(music_path):
                music_stream = AudioSegment.from_ogg(music_path)
            if self.source_type == "flv" and os.path.isfile(music_path):
                music_stream = AudioSegment.from_flv(music_path)
            music_info = EasyID3(music_path)
            tags = dict()
            tags['title'] = str(music_info["title"][0])
            tags['artist'] = str(music_info["artist"][0])
            tags['album'] = str(music_info["album"][0])
            tags['date'] = str(music_info["date"][0])
            tags['tracknumber'] = str(music_info["tracknumber"][0])
            tags['genre'] = str(music_info["genre"][0])
            if tags['artist'] == '':
                tags['artist'] = 'UnknownArtist'
            if tags['album'] == '':
                tags['album'] = 'UnknownAlbum'
            output_music_path = str(self.output_path+"/"+tags['artist']+"/"+tags['album'])
            # checking either it's needed to create the folders' structure
            if not os.path.isdir(output_music_path):
                os.makedirs(output_music_path)
            music_stream.export(str(output_music_path+"/"+tags['tracknumber']+" "+tags['title']+"."+self.output_type),
                                format="mp3", bitrate=self.bitrate, tags=tags)
