import time
from seedr import SeedrAPI
from get_tor import get_meg

seedr = SeedrAPI(email='email',
                 password='pass')


def get_and_add():
    movie_name = input("Enter Movie Name: ")
    get_ag = get_meg(movie_name)
    seedr.add_torrent(str(get_ag))
    directory = seedr.get_folder('folder_id') or seedr.get_file('file_id')
    if "progress" not in directory:
        print(directory)


def rename():
    folder = seedr.get_drive()
    files = folder['folders']
    try:
        file1 = files[0]
        fileid = file1['id']
        filename = file1['name']
    except:
        fileid = files['id']
        filename = fileid['name']
    splitFileName = str(filename).split()
    toRemove = str(input("Remove"))
    refilename = str(splitFileName).replace(toRemove, "")

    if "mkv" in refilename.split():
        refilename = refilename + " - FilmyFy.Net.mkv"
    elif "mp4" in refilename.split():
        refilename = refilename + " - FilmyFy.Net.mp4"
    print(refilename)
    seedr.rename(fileid, refilename)


if __name__ == "__main__":
    get_and_add()
    time.sleep(5)
    rename()
