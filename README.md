# pymserver
A simple Python-based Music converter and server. The following project aims to offer three main features:
* Convert or just copy audio files into a root server directory.
* Update mp3 tags informations automatically.
* HTTP server to expose the converted audio files to be downloaded or streamed through a web page on the local network.

### Instalation
pymserver depends on the pydub library which requires [FFmpeg](https://ffmpeg.org/) to run.

On Ubuntu Linux based systems, run the following command to install it.
```sh
$ sudo apt-get install ffmpeg
```

Install the dependencies and run the program.

```sh
$ cd PYMSERVER_SOURCE_FOLDER
$ python setup.py install
$ python setup.py develop
$ pymserver
```

You can also use virtual environments.
### License

Not defined yet.
