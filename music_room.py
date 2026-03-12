#!/usr/bin/env python3
"""Nexa Music Room - 音乐房间"""
import random, json

class MusicRoom:
    def __init__(self):
        self.playlist = []
        self.now_playing = None
        self.listeners = 0
    
    def add_song(self, title, artist):
        self.playlist.append({"title": title, "artist": artist, "id": random.randint(1000,9999)})
        return f"✅ 已添加: {title} - {artist}"
    
    def play_next(self):
        if self.playlist:
            self.now_playing = self.playlist.pop(0)
            return f"🎵 正在播放: {self.now_playing['title']}"
        return "播放列表为空"
    
    def get_status(self):
        return {"now_playing": self.now_playing, "queue": len(self.playlist), "listeners": self.listeners}

if __name__ == "__main__":
    room = MusicRoom()
    print(room.add_song("晴天", "周杰伦"))
    print(room.play_next())
    print(json.dumps(room.get_status(), ensure_ascii=False))
