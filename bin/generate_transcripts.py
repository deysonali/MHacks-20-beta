from video_lib import VideoLib

_COLLEGE_WRITING_101 = "College_Writing_101"
_POLITICAL_SCIENCE_227 = "Political_Science_227"

vid_lib = VideoLib()


vid_lib.get_wav_transcript_from_uri(f"gs://college_writing_101/Why_so_Many_People_Want_to_Be_Writers.wav", _COLLEGE_WRITING_101, "Why_so_Many_People_Want_to_Be_Writers.json")
vid_lib.get_wav_transcript_from_uri(f"gs://college_writing_101/How_to_write_descriptively_Nalo_Hopkinson.wav", _COLLEGE_WRITING_101, "How_to_write_descriptively_Nalo_Hopkinson.json")
vid_lib.get_wav_transcript_from_uri(f"gs://college_writing_101/How_to_build_a_fictional_world_Kate_Messner.wav", _COLLEGE_WRITING_101, "How_to_build_a_fictional_world_Kate_Messner.json")
vid_lib.get_wav_transcript_from_uri(f"gs://political_science_227/The_Bicameral_Congress_Crash_Course_Government_and_Politics_2.wav", _POLITICAL_SCIENCE_227, "The_Bicameral_Congress_Crash_Course_Government_and_Politics_2.json")
vid_lib.get_wav_transcript_from_uri(f"gs://political_science_227/Introduction_Crash_Course_US_Government_and_Politics.wav", _POLITICAL_SCIENCE_227, "Introduction_Crash_Course_US_Government_and_Politics.json")
vid_lib.get_wav_transcript_from_uri(f"gs://political_science_227/Congressional_Elections_Crash_Course_Government_and_Politics_6.wav", _POLITICAL_SCIENCE_227, "Congressional_Elections_Crash_Course_Government_and_Politics_6.json")
