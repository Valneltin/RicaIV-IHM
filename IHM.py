# import tkinter as tk, threading
# import tkinter as resize
# import imageio
# from PIL import Image, ImageTk
#
# #Init variables
# FenWidth = 1200
# FenHeight = 800
#
# #video_name = "/Users/clarisse/Documents/Série/LesPetitsMeutresS2/18 - L'hommeAuCompletMarron.mp4" #This is your video file path
# video_name = "http://169.254.47.175:8080/stream.H264" #This is your video file path
# video = imageio.get_reader(video_name)
#
# def stream(label):
#
#      for image in video.iter_data():
#          frame_image = ImageTk.PhotoImage(Image.fromarray(image))
#          label.config(image=frame_image)
#          label.image = frame_image
#
# if __name__ == "__main__":
#
#      root = tk.Tk()
#
#      can = tk.Canvas(root, width=FenWidth, height=FenHeight)
#      labelConnectionManette = can.create_text(75, 30, text="Connection manette", font="Arial 16 ", fill="green")
#      labelConnectionRaspi = can.create_text(75, 10, text="Connection robot", font="Arial 16 ", fill="green")
#
#      photo = tk.PhotoImage(file="/Users/clarisse/Desktop/RICA_IHM/RICA_Image.ppm")
#      can.create_image(725, 0, anchor='nw', image=photo)
#
#      my_label = tk.Label(root)
#      my_label.pack()
#      can.create_window(FenWidth / 2, FenHeight / 2, window=my_label)
#      can.pack()
#
#      thread = threading.Thread(target=stream, args=(my_label,))
#      thread.daemon = 1
#      thread.start()
#
#      can.mainloop()
