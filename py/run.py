import folder_paths
import subprocess
NODE_NAME = 'video_frameChange'

video_extensions = ['webm', 'mp4', 'mkv', 'gif']

class VideoFrameChange:

    def __init__(self):
        #确保ffmpeg已安装并且在系统PATH中
        self.ffmpeg_path = 'ffmpeg'  # 或者 'ffmpeg.exe' 在Windows上

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "video": ("STRING", {"default": "X://insert/path/here.mp4", "vhs_path_extensions": video_extensions}),
                "frame_rate": (
                    "FLOAT",
                    {"default": 8, "min": 1, "step": 1},
                ),
            }
        }
    RETURN_TYPES = ("VHS_FILENAMES",)
    RETURN_NAMES = ("Filenames",)
    #RETURN_TYPES = ("IMAGE",)
    #RETURN_NAMES = ("image",)
    FUNCTION = "convert_video"
    CATEGORY = 'videotools/VideoFrameChange'
    OUTPUT_NODE = True

    def convert_video(self, video, frame_rate):
        """
        使用ffmpeg转换视频，设置帧率。

        :param input_path: 输入视频文件的路径。
        :param output_path: 输出视频文件的路径。
        :param fps: 期望的输出视频帧率。
        """
        output_path =  folder_paths.get_output_directory()+f"\\frame{frame_rate}.mp4"
        # 构建ffmpeg命令
        command = [
            self.ffmpeg_path,
            '-i', video,            # 输入文件
            '-filter:v', f'fps=fps={frame_rate}',  # 设置帧率的过滤器
            '-y',
            output_path                   # 输出文件
        ]

        # 使用subprocess.run来执行ffmpeg命令
        try:
            subprocess.run(command, check=True)
            print(f"视频已转换完成，帧率设置为 {frame_rate}，输出文件：{output_path}")
        except subprocess.CalledProcessError as e:
            print(f"视频转换失败: {e}")
        return ({'result': ""},)

NODE_CLASS_MAPPINGS = {
    "VideoFrameChange": VideoFrameChange
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "VideoFrameChange": "VideoFrameChange"
}




