init python:
    def stop_audio(channel="music", fadeout=None):
        """
        :doc: audio

        This stops the music that is currently playing, and dequeues all
        queued music. If fadeout is None, the music is faded out for the
        time given in config.fade_music, otherwise it is faded for fadeout
        seconds.

        This sets the last queued file to None.

        `channel`
            The channel to stop the sound on.

        `fadeout`
            If not None, this is a time in seconds to fade for. Otherwise the
            fadeout time is taken from config.fade_music.


        """
        renpy.audio.music.stop(channel=channel, fadeout=fadeout)

    def play_audio(
        fnames=[],
        channel="music",
        loop=None,
        fadeout=None,
        synchro_start=False,
        fadein=0,
        tight=None,
        if_changed=False,
        relative_volume=None
    ):
        """
        :doc: audio

        This stops the music currently playing on the numbered channel, dequeues
        any queued music, and begins playing the specified file or files.

        `filenames`
            This may be a single file, or a list of files to be played.

        `channel`
            The channel to play the sound on.

        `loop`
            If this is True, the tracks will loop while they are the last thing
            in the queue.

        `fadeout`
            If not None, this is a time in seconds to fade for. Otherwise the
            fadeout time is taken from config.fade_music.

        `synchro_start`
            Ren'Py will ensure that all channels of with synchro_start set to true
            will start playing at exactly the same time. Synchro_start should be
            true when playing two audio files that are meant to be synchronized
            with each other.

        `fadein`
            This is the number of seconds to fade the music in for, on the
            first loop only.

        `tight`
            If this is True, then fadeouts will span into the next-queued sound. If
            None, this is true when loop is True, and false otherwise.

        `if_changed`
            If this is True, and the music file is currently playing,
            then it will not be stopped/faded out and faded back in again, but
            instead will be kept playing. (This will always queue up an additional
            loop of the music.)

        `relative_volume`
            This is the volume relative to the current channel volume.
            The specified file will be played at that relative volume. If not
            specified, it will always default to None, which plays the file at the
            original volume as determined by the mixer, channel and secondary volume.
            If used (int or float) then the volume of the channel changes to this value.
            Else if used (string) then the volume of the channel changes to this value from relative_volume channel.

        This clears the pause flag for `channel`.
        """
        stop_audio(channel, None)
        if isinstance(fnames, (basestring, str, unicode)):
            fnames = [ fnames ]
        fnames = [store.audio.__dict__[fname] for fname in fnames if store.audio.__dict__.get(fname)]
        if isinstance(relative_volume, (int, float)):
            renpy.game.preferences.volumes["sfx" if channel == "sound" else channel] = relative_volume
        elif isinstance(relative_volume, (basestring, str, unicode)):
            renpy.game.preferences.volumes["sfx" if channel == "sound" else channel] = renpy.game.preferences.volumes.get("sfx" if relative_volume == "sound" else relative_volume, 1.0)
        renpy.audio.music.play(fnames, channel, loop, fadeout, synchro_start, fadein, tight, if_changed, 1.)
