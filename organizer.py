import os
import datetime
import shutil
import argparse


def organize(folder_path):

    current_time = datetime.datetime.now()

    items = os.listdir(folder_path)

    try:
        os.mkdir(os.path.join(folder_path,"LESS_THAN_A_WEEK"))
        os.mkdir(os.path.join(folder_path,"LESS_THAN_A_MONTH"))
        os.mkdir(os.path.join(folder_path,"GREATER_THAN_A_MONTH"))
        os.mkdir(os.path.join(folder_path,"RARELY OPENED"))
    
    except:
        pass  

    for item in items:

        path = os.path.join(folder_path,item)


        try:

            access_time = os.path.getatime(path)
            time_stamp = datetime.datetime.fromtimestamp(access_time)
            difference = current_time - time_stamp

            if difference.days <= 7:

                destination_directory = os.path.join(folder_path,"LESS_THAN_A_WEEK")
                shutil.move(path,destination_directory)
            
            elif difference.days <= 30:

                destination_directory = os.path.join(folder_path,"LESS_THAN_A_MONTH")
                shutil.move(path,destination_directory)

            elif difference.days <= 60:

                destination_directory = os.path.join(folder_path,"GREATER_THAN_A_MONTH")
                shutil.move(path,destination_directory)

            else:

                destination_directory = os.path.join(folder_path,"RARELY OPENED")
                shutil.move(path,destination_directory)

        except OSError:
            print("Error in a file")


def main():

    parser = argparse.ArgumentParser(description="Organise files in Folder path provided")

    parser.add_argument('folder_path', type=str, help="Path to the folder")

    args = parser.parse_args()

    folder_path = args.folder_path

    if os.path.isdir(folder_path):
        organize(folder_path)
    
    else:
        print("Wrong path")


if __name__ == '__main__':
    main()
