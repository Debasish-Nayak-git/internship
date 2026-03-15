import os
import shutil
class FileOrganizer:
    def __init__(self,directory):
        self.directory=directory
        self.file_type={"image": [".jpg",".jpeg",".png",".gif"],
                        "Documents":[".pdf",".docx",".txt",".pptx",".xlsx"],
                        "Videos":[".mp4",".mkv",".avi"],
                        "Music":[".mp3",".wav"],
                        "Others":[]}
    def creat_folder(self):
        for folder in self.file_type:
            path=os.path.join(self.directory,folder)
            if not os.path.exists(path):
                os.makedirs(path)
    def move_file(self):
        for file in os.listdir(self.directory):
            file_path=os.path.join(self.directory,file)
            if os.path.isfile(file_path):
                moved=False
                for folder, extensions in self.file_type.items():
                    for ext in extensions:
                        if file.lower().endswith(ext):
                            shutil.move(file_path,os.path.join(self.directory,folder,file))
                            moved=True
                            break
                    if moved:
                        break
                if not moved :
                    shutil.move(file_path,os.path.join(self.directory,"Others",file))
    def organize(self):
        self.creat_folder()
        self.move_file()
class AutomationApp:
    def run(self):
        path=input("Enter folder path :")
        organizer=FileOrganizer(path)
        organizer.organize()
        print("Files organized successfully")
if __name__=="__main__":
    app=AutomationApp()
    app.run()