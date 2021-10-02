import os
from datetime import datetime, timedelta

from win10toast import ToastNotifier


def push_notification(title: str, message: str) -> None:
    """
    Display a toast notification.
    """
    toaster = ToastNotifier()
    duration = 10
    toaster.show_toast(title, message, duration=duration, threaded=True)


def save(filepath: str, value: str) -> None:
    """
    Save value to a file.
    """
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(str(value))


def load(filepath: str) -> str:
    """
    Load the content from a file.
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()


if __name__ == '__main__':
    # the number of days between each reminder
    days = 5

    # the file name that contains the next reminder date
    filename = 'WindowsUpdateTrigger.txt'

    # get the user folder absolute path
    # this will output the path is this format: C:/Users/youruser
    user_path = os.environ['USERPROFILE']

    # get the absolute path of the file
    filepath = os.path.join(user_path, filename)

    # get current date
    now = datetime.now()

    # check if the file exist
    if os.path.exists(filepath):
        # load the file content
        target_date = load(filepath)

        # convert file content to datetime object
        target_date = datetime.strptime(target_date, '%d-%m-%Y %H:%M:%S')

        # check if the date inside the file is greater or equal to the current date
        if now >= target_date:
            push_notification(
                'Windows Update!', 'Check your Windows 10 for any potential updates.')
        else:
            print('Still Time')

    # if the file does not exist
    else:
        # set the reminder date
        next_date = now + timedelta(days=days)

        # convert datetime object the str format
        next_date = next_date.strftime('%d-%m-%Y %H:%M:%S')

        # save the remainder date in a file
        save(filepath, next_date)
