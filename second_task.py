from typing import Tuple, Optional
from re import findall
from os import path

from moviepy.editor import VideoFileClip


class VideoConverter:
    @staticmethod
    def __process_converted_video_path(path: str, video_format: str):
        pattern = "[." + video_format + "]{1,}$"
        res = findall(pattern, path)
        if len(res) != 1:
            return f"{path}.{video_format}"
        return path

    @staticmethod
    def convert_video_to_gif(video_path: str, gif_path: str, time_range: Tuple[int, int] = (0, 3)) -> Optional[str]:
        try:
            clip = VideoFileClip(video_path)
            clip = clip.subclip(time_range[0], time_range[1])
            processed_gif_path = VideoConverter.__process_converted_video_path(gif_path, 'gif')
            clip.write_gif(processed_gif_path)
            return path.abspath(gif_path)
        except FileNotFoundError:
            print("The path of the gif file doesn't exist")
        except OSError:
            print("Please, input correct video path.")


if __name__ == '__main__':
    gif_path = "my_video.gif"
    video_path = "https://v16-webapp.tiktok.com/5bd9c6ad58abdbd149128f2c1422bfaa/62e86f79/video/tos/useast2a/tos-useast2a-ve-0068c003/c3c65d826fa94d67833b676dd6b32aab/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=1698&bt=849&btag=80000&cs=0&ds=3&ft=eXd.6H-oMyq8ZiqKKwe2NXPwyl7Gb&mime_type=video_mp4&qs=0&rc=ZGc0NDg7NTlnODpmOTtkPEBpM2V4PDk6ZjR2ZTMzNzczM0AwMDQyYzNfNV4xLWBfMWNiYSNxbXNkcjRfX2dgLS1kMTZzcw%3D%3D&l=202208011827310101921650711A5014DB"
    # video_path = "/home/kristina/PycharmProjects/bootcamp_tesvt_task/my_video.gif"
    # video_path = "https://v16m-webapp.tiktokcdn-us.com/ed129ecb01ab00e202682e99f68a9288/62e7cb0d/video/tos/useast5/tos-useast5-pve-0068-tx/d69985b1677b4a73a584b56d604011ca/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=4020&bt=2010&cs=0&ds=3&ft=ebtHKH-qMyq8ZjFl1we2N9befl7Gb&mime_type=video_mp4&qs=0&rc=OTU4MzU0NzVnaDpnOGg8OEBpajM5Z2c6ZmYzZTMzZzczNEAuMC9jLWBgNmExMzJfY18tYSMxX28vcjRnMGRgLS1kMS9zcw%3D%3D&l=20220801064449EF653E99EF32BC2EAB55"
    res = VideoConverter.convert_video_to_gif(video_path, gif_path, (1, 5))
    print(res)
